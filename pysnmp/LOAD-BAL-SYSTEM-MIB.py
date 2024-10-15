# SNMP MIB module (LOAD-BAL-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LOAD-BAL-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:18 2024
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



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class BigAPIStatus(Integer32):
    """Custom type BigAPIStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("addressDisabled", 8),
          ("addressDown", 10),
          ("checking", 4),
          ("disabled", 7),
          ("down", 2),
          ("enabled", 6),
          ("forcedDown", 3),
          ("maintenance", 5),
          ("portDisabled", 9),
          ("unchecked", 0),
          ("up", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F5_ObjectIdentity = ObjectIdentity
f5 = _F5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375)
)
_F5systems_ObjectIdentity = ObjectIdentity
f5systems = _F5systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1)
)
_Loadbal_ObjectIdentity = ObjectIdentity
loadbal = _Loadbal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1)
)
_Globals_ObjectIdentity = ObjectIdentity
globals = _Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1)
)
_GlobalAttributes_ObjectIdentity = ObjectIdentity
globalAttributes = _GlobalAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1)
)


class _GlobalAttrKernelVersion_Type(DisplayString):
    """Custom type globalAttrKernelVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrKernelVersion_Type.__name__ = "DisplayString"
_GlobalAttrKernelVersion_Object = MibScalar
globalAttrKernelVersion = _GlobalAttrKernelVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 1),
    _GlobalAttrKernelVersion_Type()
)
globalAttrKernelVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrKernelVersion.setStatus("mandatory")


class _GlobalAttrPackageVersion_Type(DisplayString):
    """Custom type globalAttrPackageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrPackageVersion_Type.__name__ = "DisplayString"
_GlobalAttrPackageVersion_Object = MibScalar
globalAttrPackageVersion = _GlobalAttrPackageVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 2),
    _GlobalAttrPackageVersion_Type()
)
globalAttrPackageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPackageVersion.setStatus("mandatory")


class _GlobalAttrPackageEdition_Type(DisplayString):
    """Custom type globalAttrPackageEdition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrPackageEdition_Type.__name__ = "DisplayString"
_GlobalAttrPackageEdition_Object = MibScalar
globalAttrPackageEdition = _GlobalAttrPackageEdition_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 3),
    _GlobalAttrPackageEdition_Type()
)
globalAttrPackageEdition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPackageEdition.setStatus("mandatory")


class _GlobalAttrAgentVersion_Type(DisplayString):
    """Custom type globalAttrAgentVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrAgentVersion_Type.__name__ = "DisplayString"
_GlobalAttrAgentVersion_Object = MibScalar
globalAttrAgentVersion = _GlobalAttrAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 4),
    _GlobalAttrAgentVersion_Type()
)
globalAttrAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrAgentVersion.setStatus("deprecated")


class _GlobalAttrProductCode_Type(Integer32):
    """Custom type globalAttrProductCode based on Integer32"""
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
              10,
              99)
        )
    )
    namedValues = NamedValues(
        *(("clb", 6),
          ("flb", 5),
          ("ha", 2),
          ("indeterminate", 1),
          ("lb", 3),
          ("ssl", 8),
          ("test", 10),
          ("threedns", 4),
          ("unsupported", 99),
          ("xlb", 7))
    )


_GlobalAttrProductCode_Type.__name__ = "Integer32"
_GlobalAttrProductCode_Object = MibScalar
globalAttrProductCode = _GlobalAttrProductCode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 5),
    _GlobalAttrProductCode_Type()
)
globalAttrProductCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrProductCode.setStatus("mandatory")


class _GlobalAttrSerialNumber_Type(DisplayString):
    """Custom type globalAttrSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrSerialNumber_Type.__name__ = "DisplayString"
_GlobalAttrSerialNumber_Object = MibScalar
globalAttrSerialNumber = _GlobalAttrSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 6),
    _GlobalAttrSerialNumber_Type()
)
globalAttrSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSerialNumber.setStatus("mandatory")


class _GlobalAttrVendorName_Type(DisplayString):
    """Custom type globalAttrVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrVendorName_Type.__name__ = "DisplayString"
_GlobalAttrVendorName_Object = MibScalar
globalAttrVendorName = _GlobalAttrVendorName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 7),
    _GlobalAttrVendorName_Type()
)
globalAttrVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrVendorName.setStatus("mandatory")


class _GlobalAttrSSLGatewayLevel_Type(Integer32):
    """Custom type globalAttrSSLGatewayLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              9,
              10,
              11,
              99)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("tps1000", 7),
          ("tps1500", 10),
          ("tps200", 3),
          ("tps2000", 11),
          ("tps400", 4),
          ("tps500", 9),
          ("tps600", 5),
          ("tps800", 6),
          ("unsupported", 99))
    )


_GlobalAttrSSLGatewayLevel_Type.__name__ = "Integer32"
_GlobalAttrSSLGatewayLevel_Object = MibScalar
globalAttrSSLGatewayLevel = _GlobalAttrSSLGatewayLevel_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 8),
    _GlobalAttrSSLGatewayLevel_Type()
)
globalAttrSSLGatewayLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLGatewayLevel.setStatus("mandatory")
_GlobalAttrCPUCount_Type = Integer32
_GlobalAttrCPUCount_Object = MibScalar
globalAttrCPUCount = _GlobalAttrCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 9),
    _GlobalAttrCPUCount_Type()
)
globalAttrCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrCPUCount.setStatus("mandatory")


class _GlobalAttrAuthorized_Type(Integer32):
    """Custom type globalAttrAuthorized based on Integer32"""
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


_GlobalAttrAuthorized_Type.__name__ = "Integer32"
_GlobalAttrAuthorized_Object = MibScalar
globalAttrAuthorized = _GlobalAttrAuthorized_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 10),
    _GlobalAttrAuthorized_Type()
)
globalAttrAuthorized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrAuthorized.setStatus("deprecated")


class _GlobalAttrMaintenceMode_Type(Integer32):
    """Custom type globalAttrMaintenceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrMaintenceMode_Type.__name__ = "Integer32"
_GlobalAttrMaintenceMode_Object = MibScalar
globalAttrMaintenceMode = _GlobalAttrMaintenceMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 11),
    _GlobalAttrMaintenceMode_Type()
)
globalAttrMaintenceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrMaintenceMode.setStatus("mandatory")


class _GlobalAttrMaster_Type(Integer32):
    """Custom type globalAttrMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrMaster_Type.__name__ = "Integer32"
_GlobalAttrMaster_Object = MibScalar
globalAttrMaster = _GlobalAttrMaster_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 12),
    _GlobalAttrMaster_Type()
)
globalAttrMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrMaster.setStatus("mandatory")


class _GlobalAttrUnitID_Type(DisplayString):
    """Custom type globalAttrUnitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrUnitID_Type.__name__ = "DisplayString"
_GlobalAttrUnitID_Object = MibScalar
globalAttrUnitID = _GlobalAttrUnitID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 13),
    _GlobalAttrUnitID_Type()
)
globalAttrUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrUnitID.setStatus("mandatory")


class _GlobalAttrPeerUnitID_Type(DisplayString):
    """Custom type globalAttrPeerUnitID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrPeerUnitID_Type.__name__ = "DisplayString"
_GlobalAttrPeerUnitID_Object = MibScalar
globalAttrPeerUnitID = _GlobalAttrPeerUnitID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 14),
    _GlobalAttrPeerUnitID_Type()
)
globalAttrPeerUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPeerUnitID.setStatus("mandatory")
_GlobalAttrFastestMaxIdleTime_Type = Integer32
_GlobalAttrFastestMaxIdleTime_Object = MibScalar
globalAttrFastestMaxIdleTime = _GlobalAttrFastestMaxIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 15),
    _GlobalAttrFastestMaxIdleTime_Type()
)
globalAttrFastestMaxIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrFastestMaxIdleTime.setStatus("mandatory")
_GlobalAttrFastFlowActive_Type = Integer32
_GlobalAttrFastFlowActive_Object = MibScalar
globalAttrFastFlowActive = _GlobalAttrFastFlowActive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 16),
    _GlobalAttrFastFlowActive_Type()
)
globalAttrFastFlowActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrFastFlowActive.setStatus("mandatory")


class _GlobalAttrGatewayFailsafeArmed_Type(Integer32):
    """Custom type globalAttrGatewayFailsafeArmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrGatewayFailsafeArmed_Type.__name__ = "Integer32"
_GlobalAttrGatewayFailsafeArmed_Object = MibScalar
globalAttrGatewayFailsafeArmed = _GlobalAttrGatewayFailsafeArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 17),
    _GlobalAttrGatewayFailsafeArmed_Type()
)
globalAttrGatewayFailsafeArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrGatewayFailsafeArmed.setStatus("mandatory")
_GlobalAttrMemoryRebootPercent_Type = Integer32
_GlobalAttrMemoryRebootPercent_Object = MibScalar
globalAttrMemoryRebootPercent = _GlobalAttrMemoryRebootPercent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 18),
    _GlobalAttrMemoryRebootPercent_Type()
)
globalAttrMemoryRebootPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrMemoryRebootPercent.setStatus("mandatory")


class _GlobalAttrMirrorEnabled_Type(Integer32):
    """Custom type globalAttrMirrorEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrMirrorEnabled_Type.__name__ = "Integer32"
_GlobalAttrMirrorEnabled_Object = MibScalar
globalAttrMirrorEnabled = _GlobalAttrMirrorEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 19),
    _GlobalAttrMirrorEnabled_Type()
)
globalAttrMirrorEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrMirrorEnabled.setStatus("mandatory")
_GlobalAttrVerboseLogLevel_Type = Integer32
_GlobalAttrVerboseLogLevel_Object = MibScalar
globalAttrVerboseLogLevel = _GlobalAttrVerboseLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 20),
    _GlobalAttrVerboseLogLevel_Type()
)
globalAttrVerboseLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrVerboseLogLevel.setStatus("mandatory")


class _GlobalAttrWatchDogArmed_Type(Integer32):
    """Custom type globalAttrWatchDogArmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrWatchDogArmed_Type.__name__ = "Integer32"
_GlobalAttrWatchDogArmed_Object = MibScalar
globalAttrWatchDogArmed = _GlobalAttrWatchDogArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 21),
    _GlobalAttrWatchDogArmed_Type()
)
globalAttrWatchDogArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrWatchDogArmed.setStatus("mandatory")


class _GlobalAttrAutoLastHop_Type(Integer32):
    """Custom type globalAttrAutoLastHop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrAutoLastHop_Type.__name__ = "Integer32"
_GlobalAttrAutoLastHop_Object = MibScalar
globalAttrAutoLastHop = _GlobalAttrAutoLastHop_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 22),
    _GlobalAttrAutoLastHop_Type()
)
globalAttrAutoLastHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrAutoLastHop.setStatus("mandatory")
_GlobalAttrAkamaiConfigPort_Type = Integer32
_GlobalAttrAkamaiConfigPort_Object = MibScalar
globalAttrAkamaiConfigPort = _GlobalAttrAkamaiConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 23),
    _GlobalAttrAkamaiConfigPort_Type()
)
globalAttrAkamaiConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrAkamaiConfigPort.setStatus("mandatory")
_GlobalAttrNameSurferWebPort_Type = Integer32
_GlobalAttrNameSurferWebPort_Object = MibScalar
globalAttrNameSurferWebPort = _GlobalAttrNameSurferWebPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 24),
    _GlobalAttrNameSurferWebPort_Type()
)
globalAttrNameSurferWebPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrNameSurferWebPort.setStatus("mandatory")
_GlobalAttrNameSurferZonePort_Type = Integer32
_GlobalAttrNameSurferZonePort_Object = MibScalar
globalAttrNameSurferZonePort = _GlobalAttrNameSurferZonePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 25),
    _GlobalAttrNameSurferZonePort_Type()
)
globalAttrNameSurferZonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrNameSurferZonePort.setStatus("mandatory")


class _GlobalAttrOpen3DNSPorts_Type(Integer32):
    """Custom type globalAttrOpen3DNSPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpen3DNSPorts_Type.__name__ = "Integer32"
_GlobalAttrOpen3DNSPorts_Object = MibScalar
globalAttrOpen3DNSPorts = _GlobalAttrOpen3DNSPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 26),
    _GlobalAttrOpen3DNSPorts_Type()
)
globalAttrOpen3DNSPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpen3DNSPorts.setStatus("mandatory")


class _GlobalAttrOpenCorbaPorts_Type(Integer32):
    """Custom type globalAttrOpenCorbaPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpenCorbaPorts_Type.__name__ = "Integer32"
_GlobalAttrOpenCorbaPorts_Object = MibScalar
globalAttrOpenCorbaPorts = _GlobalAttrOpenCorbaPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 27),
    _GlobalAttrOpenCorbaPorts_Type()
)
globalAttrOpenCorbaPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpenCorbaPorts.setStatus("mandatory")


class _GlobalAttrOpenFTPPorts_Type(Integer32):
    """Custom type globalAttrOpenFTPPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpenFTPPorts_Type.__name__ = "Integer32"
_GlobalAttrOpenFTPPorts_Object = MibScalar
globalAttrOpenFTPPorts = _GlobalAttrOpenFTPPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 28),
    _GlobalAttrOpenFTPPorts_Type()
)
globalAttrOpenFTPPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpenFTPPorts.setStatus("mandatory")


class _GlobalAttrOpenRSHPorts_Type(Integer32):
    """Custom type globalAttrOpenRSHPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpenRSHPorts_Type.__name__ = "Integer32"
_GlobalAttrOpenRSHPorts_Object = MibScalar
globalAttrOpenRSHPorts = _GlobalAttrOpenRSHPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 29),
    _GlobalAttrOpenRSHPorts_Type()
)
globalAttrOpenRSHPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpenRSHPorts.setStatus("mandatory")


class _GlobalAttrOpenSSHPorts_Type(Integer32):
    """Custom type globalAttrOpenSSHPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpenSSHPorts_Type.__name__ = "Integer32"
_GlobalAttrOpenSSHPorts_Object = MibScalar
globalAttrOpenSSHPorts = _GlobalAttrOpenSSHPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 30),
    _GlobalAttrOpenSSHPorts_Type()
)
globalAttrOpenSSHPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpenSSHPorts.setStatus("mandatory")


class _GlobalAttrOpenTelnetPorts_Type(Integer32):
    """Custom type globalAttrOpenTelnetPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrOpenTelnetPorts_Type.__name__ = "Integer32"
_GlobalAttrOpenTelnetPorts_Object = MibScalar
globalAttrOpenTelnetPorts = _GlobalAttrOpenTelnetPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 31),
    _GlobalAttrOpenTelnetPorts_Type()
)
globalAttrOpenTelnetPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrOpenTelnetPorts.setStatus("mandatory")
_GlobalAttrWebAdminPort_Type = Integer32
_GlobalAttrWebAdminPort_Object = MibScalar
globalAttrWebAdminPort = _GlobalAttrWebAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 32),
    _GlobalAttrWebAdminPort_Type()
)
globalAttrWebAdminPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrWebAdminPort.setStatus("mandatory")


class _GlobalAttrPersistAcrossServices_Type(Integer32):
    """Custom type globalAttrPersistAcrossServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrPersistAcrossServices_Type.__name__ = "Integer32"
_GlobalAttrPersistAcrossServices_Object = MibScalar
globalAttrPersistAcrossServices = _GlobalAttrPersistAcrossServices_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 33),
    _GlobalAttrPersistAcrossServices_Type()
)
globalAttrPersistAcrossServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPersistAcrossServices.setStatus("mandatory")


class _GlobalAttrPersistAccrossVirtuals_Type(Integer32):
    """Custom type globalAttrPersistAccrossVirtuals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrPersistAccrossVirtuals_Type.__name__ = "Integer32"
_GlobalAttrPersistAccrossVirtuals_Object = MibScalar
globalAttrPersistAccrossVirtuals = _GlobalAttrPersistAccrossVirtuals_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 34),
    _GlobalAttrPersistAccrossVirtuals_Type()
)
globalAttrPersistAccrossVirtuals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPersistAccrossVirtuals.setStatus("mandatory")


class _GlobalAttrPersistMapProxies_Type(Integer32):
    """Custom type globalAttrPersistMapProxies based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrPersistMapProxies_Type.__name__ = "Integer32"
_GlobalAttrPersistMapProxies_Object = MibScalar
globalAttrPersistMapProxies = _GlobalAttrPersistMapProxies_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 35),
    _GlobalAttrPersistMapProxies_Type()
)
globalAttrPersistMapProxies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPersistMapProxies.setStatus("mandatory")


class _GlobalAttrPersistTimerUsedAsLimit_Type(Integer32):
    """Custom type globalAttrPersistTimerUsedAsLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrPersistTimerUsedAsLimit_Type.__name__ = "Integer32"
_GlobalAttrPersistTimerUsedAsLimit_Object = MibScalar
globalAttrPersistTimerUsedAsLimit = _GlobalAttrPersistTimerUsedAsLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 36),
    _GlobalAttrPersistTimerUsedAsLimit_Type()
)
globalAttrPersistTimerUsedAsLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrPersistTimerUsedAsLimit.setStatus("mandatory")
_GlobalAttrStickyTableLimit_Type = Integer32
_GlobalAttrStickyTableLimit_Object = MibScalar
globalAttrStickyTableLimit = _GlobalAttrStickyTableLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 37),
    _GlobalAttrStickyTableLimit_Type()
)
globalAttrStickyTableLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrStickyTableLimit.setStatus("mandatory")
_GlobalAttrSNATConnLimit_Type = Integer32
_GlobalAttrSNATConnLimit_Object = MibScalar
globalAttrSNATConnLimit = _GlobalAttrSNATConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 38),
    _GlobalAttrSNATConnLimit_Type()
)
globalAttrSNATConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSNATConnLimit.setStatus("mandatory")
_GlobalAttrSNATTCPIdleTimeout_Type = Integer32
_GlobalAttrSNATTCPIdleTimeout_Object = MibScalar
globalAttrSNATTCPIdleTimeout = _GlobalAttrSNATTCPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 39),
    _GlobalAttrSNATTCPIdleTimeout_Type()
)
globalAttrSNATTCPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSNATTCPIdleTimeout.setStatus("mandatory")
_GlobalAttrSNATUDPIdleTimeout_Type = Integer32
_GlobalAttrSNATUDPIdleTimeout_Object = MibScalar
globalAttrSNATUDPIdleTimeout = _GlobalAttrSNATUDPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 40),
    _GlobalAttrSNATUDPIdleTimeout_Type()
)
globalAttrSNATUDPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSNATUDPIdleTimeout.setStatus("mandatory")


class _GlobalAttrSystemType_Type(Integer32):
    """Custom type globalAttrSystemType based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("applicationswitch", 7),
          ("d25", 2),
          ("d30", 3),
          ("d35", 6),
          ("d45", 9),
          ("d50", 8),
          ("dell", 5),
          ("f35", 4),
          ("serverappliance", 1),
          ("unsupported", 99))
    )


_GlobalAttrSystemType_Type.__name__ = "Integer32"
_GlobalAttrSystemType_Object = MibScalar
globalAttrSystemType = _GlobalAttrSystemType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 41),
    _GlobalAttrSystemType_Type()
)
globalAttrSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSystemType.setStatus("mandatory")


class _GlobalAttrNetReboot_Type(Integer32):
    """Custom type globalAttrNetReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("notAvailable", 3),
          ("true", 1))
    )


_GlobalAttrNetReboot_Type.__name__ = "Integer32"
_GlobalAttrNetReboot_Object = MibScalar
globalAttrNetReboot = _GlobalAttrNetReboot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 42),
    _GlobalAttrNetReboot_Type()
)
globalAttrNetReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrNetReboot.setStatus("mandatory")


class _GlobalAttrQuietBoot_Type(Integer32):
    """Custom type globalAttrQuietBoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrQuietBoot_Type.__name__ = "Integer32"
_GlobalAttrQuietBoot_Object = MibScalar
globalAttrQuietBoot = _GlobalAttrQuietBoot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 43),
    _GlobalAttrQuietBoot_Type()
)
globalAttrQuietBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrQuietBoot.setStatus("mandatory")
_GlobalAttrL2CacheTimeout_Type = Integer32
_GlobalAttrL2CacheTimeout_Object = MibScalar
globalAttrL2CacheTimeout = _GlobalAttrL2CacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 44),
    _GlobalAttrL2CacheTimeout_Type()
)
globalAttrL2CacheTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrL2CacheTimeout.setStatus("mandatory")


class _GlobalAttrSSLProxyFailOver_Type(Integer32):
    """Custom type globalAttrSSLProxyFailOver based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrSSLProxyFailOver_Type.__name__ = "Integer32"
_GlobalAttrSSLProxyFailOver_Object = MibScalar
globalAttrSSLProxyFailOver = _GlobalAttrSSLProxyFailOver_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 45),
    _GlobalAttrSSLProxyFailOver_Type()
)
globalAttrSSLProxyFailOver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLProxyFailOver.setStatus("mandatory")


class _GlobalAttrAkamaiConfigFile_Type(DisplayString):
    """Custom type globalAttrAkamaiConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GlobalAttrAkamaiConfigFile_Type.__name__ = "DisplayString"
_GlobalAttrAkamaiConfigFile_Object = MibScalar
globalAttrAkamaiConfigFile = _GlobalAttrAkamaiConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 46),
    _GlobalAttrAkamaiConfigFile_Type()
)
globalAttrAkamaiConfigFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrAkamaiConfigFile.setStatus("mandatory")
_GlobalAttrSSLProxyServerSessionTimeout_Type = Integer32
_GlobalAttrSSLProxyServerSessionTimeout_Object = MibScalar
globalAttrSSLProxyServerSessionTimeout = _GlobalAttrSSLProxyServerSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 47),
    _GlobalAttrSSLProxyServerSessionTimeout_Type()
)
globalAttrSSLProxyServerSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLProxyServerSessionTimeout.setStatus("mandatory")
_GlobalAttrSSLProxyServerSessionCacheSize_Type = Integer32
_GlobalAttrSSLProxyServerSessionCacheSize_Object = MibScalar
globalAttrSSLProxyServerSessionCacheSize = _GlobalAttrSSLProxyServerSessionCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 48),
    _GlobalAttrSSLProxyServerSessionCacheSize_Type()
)
globalAttrSSLProxyServerSessionCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLProxyServerSessionCacheSize.setStatus("mandatory")


class _GlobalAttrIPForwarding_Type(Integer32):
    """Custom type globalAttrIPForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrIPForwarding_Type.__name__ = "Integer32"
_GlobalAttrIPForwarding_Object = MibScalar
globalAttrIPForwarding = _GlobalAttrIPForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 49),
    _GlobalAttrIPForwarding_Type()
)
globalAttrIPForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrIPForwarding.setStatus("mandatory")


class _GlobalAttrSSLProxyUncleanShutdown_Type(Integer32):
    """Custom type globalAttrSSLProxyUncleanShutdown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrSSLProxyUncleanShutdown_Type.__name__ = "Integer32"
_GlobalAttrSSLProxyUncleanShutdown_Object = MibScalar
globalAttrSSLProxyUncleanShutdown = _GlobalAttrSSLProxyUncleanShutdown_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 50),
    _GlobalAttrSSLProxyUncleanShutdown_Type()
)
globalAttrSSLProxyUncleanShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLProxyUncleanShutdown.setStatus("mandatory")


class _GlobalAttrSSLProxyStrictResume_Type(Integer32):
    """Custom type globalAttrSSLProxyStrictResume based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrSSLProxyStrictResume_Type.__name__ = "Integer32"
_GlobalAttrSSLProxyStrictResume_Object = MibScalar
globalAttrSSLProxyStrictResume = _GlobalAttrSSLProxyStrictResume_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 51),
    _GlobalAttrSSLProxyStrictResume_Type()
)
globalAttrSSLProxyStrictResume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSSLProxyStrictResume.setStatus("mandatory")
_GlobalAttrSelfConnTimeout_Type = Integer32
_GlobalAttrSelfConnTimeout_Object = MibScalar
globalAttrSelfConnTimeout = _GlobalAttrSelfConnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 52),
    _GlobalAttrSelfConnTimeout_Type()
)
globalAttrSelfConnTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrSelfConnTimeout.setStatus("mandatory")


class _GlobalAttrFailoverPort_Type(Integer32):
    """Custom type globalAttrFailoverPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1),
          ("unsupported", 99))
    )


_GlobalAttrFailoverPort_Type.__name__ = "Integer32"
_GlobalAttrFailoverPort_Object = MibScalar
globalAttrFailoverPort = _GlobalAttrFailoverPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 1, 53),
    _GlobalAttrFailoverPort_Type()
)
globalAttrFailoverPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalAttrFailoverPort.setStatus("mandatory")
_GlobalStats_ObjectIdentity = ObjectIdentity
globalStats = _GlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2)
)
_GlobalStatUptime_Type = Integer32
_GlobalStatUptime_Object = MibScalar
globalStatUptime = _GlobalStatUptime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 1),
    _GlobalStatUptime_Type()
)
globalStatUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatUptime.setStatus("mandatory")
_GlobalStatBitsin_Type = Counter32
_GlobalStatBitsin_Object = MibScalar
globalStatBitsin = _GlobalStatBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 2),
    _GlobalStatBitsin_Type()
)
globalStatBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatBitsin.setStatus("mandatory")
_GlobalStatBitsinHi32_Type = Counter32
_GlobalStatBitsinHi32_Object = MibScalar
globalStatBitsinHi32 = _GlobalStatBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 3),
    _GlobalStatBitsinHi32_Type()
)
globalStatBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatBitsinHi32.setStatus("mandatory")
_GlobalStatBitsout_Type = Counter32
_GlobalStatBitsout_Object = MibScalar
globalStatBitsout = _GlobalStatBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 4),
    _GlobalStatBitsout_Type()
)
globalStatBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatBitsout.setStatus("mandatory")
_GlobalStatBitsoutHi32_Type = Counter32
_GlobalStatBitsoutHi32_Object = MibScalar
globalStatBitsoutHi32 = _GlobalStatBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 5),
    _GlobalStatBitsoutHi32_Type()
)
globalStatBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatBitsoutHi32.setStatus("mandatory")
_GlobalStatPcktsin_Type = Counter32
_GlobalStatPcktsin_Object = MibScalar
globalStatPcktsin = _GlobalStatPcktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 6),
    _GlobalStatPcktsin_Type()
)
globalStatPcktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatPcktsin.setStatus("mandatory")
_GlobalStatPcktsinHi32_Type = Counter32
_GlobalStatPcktsinHi32_Object = MibScalar
globalStatPcktsinHi32 = _GlobalStatPcktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 7),
    _GlobalStatPcktsinHi32_Type()
)
globalStatPcktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatPcktsinHi32.setStatus("mandatory")
_GlobalStatPcktsout_Type = Counter32
_GlobalStatPcktsout_Object = MibScalar
globalStatPcktsout = _GlobalStatPcktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 8),
    _GlobalStatPcktsout_Type()
)
globalStatPcktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatPcktsout.setStatus("mandatory")
_GlobalStatPcktsoutHi32_Type = Counter32
_GlobalStatPcktsoutHi32_Object = MibScalar
globalStatPcktsoutHi32 = _GlobalStatPcktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 9),
    _GlobalStatPcktsoutHi32_Type()
)
globalStatPcktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatPcktsoutHi32.setStatus("mandatory")
_GlobalStatCurrentConn_Type = Counter32
_GlobalStatCurrentConn_Object = MibScalar
globalStatCurrentConn = _GlobalStatCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 10),
    _GlobalStatCurrentConn_Type()
)
globalStatCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatCurrentConn.setStatus("mandatory")
_GlobalStatMaxConn_Type = Counter32
_GlobalStatMaxConn_Object = MibScalar
globalStatMaxConn = _GlobalStatMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 11),
    _GlobalStatMaxConn_Type()
)
globalStatMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaxConn.setStatus("mandatory")
_GlobalStatTotalConn_Type = Counter32
_GlobalStatTotalConn_Object = MibScalar
globalStatTotalConn = _GlobalStatTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 12),
    _GlobalStatTotalConn_Type()
)
globalStatTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatTotalConn.setStatus("mandatory")
_GlobalStatTimeouts_Type = Counter32
_GlobalStatTimeouts_Object = MibScalar
globalStatTimeouts = _GlobalStatTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 13),
    _GlobalStatTimeouts_Type()
)
globalStatTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatTimeouts.setStatus("mandatory")
_GlobalStatMemoryPoolTotal_Type = Integer32
_GlobalStatMemoryPoolTotal_Object = MibScalar
globalStatMemoryPoolTotal = _GlobalStatMemoryPoolTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 14),
    _GlobalStatMemoryPoolTotal_Type()
)
globalStatMemoryPoolTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryPoolTotal.setStatus("mandatory")
_GlobalStatMemoryPoolUsed_Type = Integer32
_GlobalStatMemoryPoolUsed_Object = MibScalar
globalStatMemoryPoolUsed = _GlobalStatMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 15),
    _GlobalStatMemoryPoolUsed_Type()
)
globalStatMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryPoolUsed.setStatus("mandatory")
_GlobalStatStandBySharedDrop_Type = Counter32
_GlobalStatStandBySharedDrop_Object = MibScalar
globalStatStandBySharedDrop = _GlobalStatStandBySharedDrop_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 16),
    _GlobalStatStandBySharedDrop_Type()
)
globalStatStandBySharedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatStandBySharedDrop.setStatus("mandatory")
_GlobalStatSelfTCPPortDeny_Type = Counter32
_GlobalStatSelfTCPPortDeny_Object = MibScalar
globalStatSelfTCPPortDeny = _GlobalStatSelfTCPPortDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 17),
    _GlobalStatSelfTCPPortDeny_Type()
)
globalStatSelfTCPPortDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatSelfTCPPortDeny.setStatus("mandatory")
_GlobalStatSelfUDPPortDeny_Type = Counter32
_GlobalStatSelfUDPPortDeny_Object = MibScalar
globalStatSelfUDPPortDeny = _GlobalStatSelfUDPPortDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 18),
    _GlobalStatSelfUDPPortDeny_Type()
)
globalStatSelfUDPPortDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatSelfUDPPortDeny.setStatus("mandatory")
_GlobalStatMaintenanceModeDeny_Type = Counter32
_GlobalStatMaintenanceModeDeny_Object = MibScalar
globalStatMaintenanceModeDeny = _GlobalStatMaintenanceModeDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 19),
    _GlobalStatMaintenanceModeDeny_Type()
)
globalStatMaintenanceModeDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaintenanceModeDeny.setStatus("mandatory")
_GlobalStatVirtualServerUDPPortDeny_Type = Counter32
_GlobalStatVirtualServerUDPPortDeny_Object = MibScalar
globalStatVirtualServerUDPPortDeny = _GlobalStatVirtualServerUDPPortDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 20),
    _GlobalStatVirtualServerUDPPortDeny_Type()
)
globalStatVirtualServerUDPPortDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerUDPPortDeny.setStatus("mandatory")
_GlobalStatVirtualServerTCPPortDeny_Type = Counter32
_GlobalStatVirtualServerTCPPortDeny_Object = MibScalar
globalStatVirtualServerTCPPortDeny = _GlobalStatVirtualServerTCPPortDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 21),
    _GlobalStatVirtualServerTCPPortDeny_Type()
)
globalStatVirtualServerTCPPortDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerTCPPortDeny.setStatus("mandatory")
_GlobalStatVirtualServerDupSynSSL_Type = Counter32
_GlobalStatVirtualServerDupSynSSL_Object = MibScalar
globalStatVirtualServerDupSynSSL = _GlobalStatVirtualServerDupSynSSL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 22),
    _GlobalStatVirtualServerDupSynSSL_Type()
)
globalStatVirtualServerDupSynSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerDupSynSSL.setStatus("mandatory")
_GlobalStatVirtualServerDupSynWrongDest_Type = Counter32
_GlobalStatVirtualServerDupSynWrongDest_Object = MibScalar
globalStatVirtualServerDupSynWrongDest = _GlobalStatVirtualServerDupSynWrongDest_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 23),
    _GlobalStatVirtualServerDupSynWrongDest_Type()
)
globalStatVirtualServerDupSynWrongDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerDupSynWrongDest.setStatus("mandatory")
_GlobalStatVirtualServerDupSynNodeDown_Type = Counter32
_GlobalStatVirtualServerDupSynNodeDown_Object = MibScalar
globalStatVirtualServerDupSynNodeDown = _GlobalStatVirtualServerDupSynNodeDown_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 24),
    _GlobalStatVirtualServerDupSynNodeDown_Type()
)
globalStatVirtualServerDupSynNodeDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerDupSynNodeDown.setStatus("mandatory")
_GlobalStatVirtualServerNonSynDeny_Type = Counter32
_GlobalStatVirtualServerNonSynDeny_Object = MibScalar
globalStatVirtualServerNonSynDeny = _GlobalStatVirtualServerNonSynDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 25),
    _GlobalStatVirtualServerNonSynDeny_Type()
)
globalStatVirtualServerNonSynDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerNonSynDeny.setStatus("mandatory")
_GlobalStatMaxConnPortDeny_Type = Counter32
_GlobalStatMaxConnPortDeny_Object = MibScalar
globalStatMaxConnPortDeny = _GlobalStatMaxConnPortDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 26),
    _GlobalStatMaxConnPortDeny_Type()
)
globalStatMaxConnPortDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaxConnPortDeny.setStatus("mandatory")
_GlobalStatMaxConnVirtualAddressDeny_Type = Counter32
_GlobalStatMaxConnVirtualAddressDeny_Object = MibScalar
globalStatMaxConnVirtualAddressDeny = _GlobalStatMaxConnVirtualAddressDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 27),
    _GlobalStatMaxConnVirtualAddressDeny_Type()
)
globalStatMaxConnVirtualAddressDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaxConnVirtualAddressDeny.setStatus("mandatory")
_GlobalStatMaxConnVirtualPathDeny_Type = Counter32
_GlobalStatMaxConnVirtualPathDeny_Object = MibScalar
globalStatMaxConnVirtualPathDeny = _GlobalStatMaxConnVirtualPathDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 28),
    _GlobalStatMaxConnVirtualPathDeny_Type()
)
globalStatMaxConnVirtualPathDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaxConnVirtualPathDeny.setStatus("mandatory")
_GlobalStatVirtualServerFragNoPort_Type = Counter32
_GlobalStatVirtualServerFragNoPort_Object = MibScalar
globalStatVirtualServerFragNoPort = _GlobalStatVirtualServerFragNoPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 29),
    _GlobalStatVirtualServerFragNoPort_Type()
)
globalStatVirtualServerFragNoPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerFragNoPort.setStatus("mandatory")
_GlobalStatVirtualServerFragNoConn_Type = Counter32
_GlobalStatVirtualServerFragNoConn_Object = MibScalar
globalStatVirtualServerFragNoConn = _GlobalStatVirtualServerFragNoConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 30),
    _GlobalStatVirtualServerFragNoConn_Type()
)
globalStatVirtualServerFragNoConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatVirtualServerFragNoConn.setStatus("mandatory")
_GlobalStatNoHandlerDeny_Type = Counter32
_GlobalStatNoHandlerDeny_Object = MibScalar
globalStatNoHandlerDeny = _GlobalStatNoHandlerDeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 31),
    _GlobalStatNoHandlerDeny_Type()
)
globalStatNoHandlerDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatNoHandlerDeny.setStatus("mandatory")
_GlobalStatTCPTimeouts_Type = Counter32
_GlobalStatTCPTimeouts_Object = MibScalar
globalStatTCPTimeouts = _GlobalStatTCPTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 32),
    _GlobalStatTCPTimeouts_Type()
)
globalStatTCPTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatTCPTimeouts.setStatus("mandatory")
_GlobalStatUDPTimeouts_Type = Counter32
_GlobalStatUDPTimeouts_Object = MibScalar
globalStatUDPTimeouts = _GlobalStatUDPTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 33),
    _GlobalStatUDPTimeouts_Type()
)
globalStatUDPTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatUDPTimeouts.setStatus("mandatory")
_GlobalStatIPTimeouts_Type = Counter32
_GlobalStatIPTimeouts_Object = MibScalar
globalStatIPTimeouts = _GlobalStatIPTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 34),
    _GlobalStatIPTimeouts_Type()
)
globalStatIPTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatIPTimeouts.setStatus("mandatory")
_GlobalStatSSLTimeouts_Type = Counter32
_GlobalStatSSLTimeouts_Object = MibScalar
globalStatSSLTimeouts = _GlobalStatSSLTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 35),
    _GlobalStatSSLTimeouts_Type()
)
globalStatSSLTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatSSLTimeouts.setStatus("mandatory")
_GlobalStatPersistTimeouts_Type = Counter32
_GlobalStatPersistTimeouts_Object = MibScalar
globalStatPersistTimeouts = _GlobalStatPersistTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 36),
    _GlobalStatPersistTimeouts_Type()
)
globalStatPersistTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatPersistTimeouts.setStatus("mandatory")
_GlobalStatMultiProcessorMode_Type = Integer32
_GlobalStatMultiProcessorMode_Object = MibScalar
globalStatMultiProcessorMode = _GlobalStatMultiProcessorMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 37),
    _GlobalStatMultiProcessorMode_Type()
)
globalStatMultiProcessorMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMultiProcessorMode.setStatus("mandatory")
_GlobalStatCPUCount_Type = Integer32
_GlobalStatCPUCount_Object = MibScalar
globalStatCPUCount = _GlobalStatCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 38),
    _GlobalStatCPUCount_Type()
)
globalStatCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatCPUCount.setStatus("mandatory")
_GlobalStatActiveCPUCount_Type = Integer32
_GlobalStatActiveCPUCount_Object = MibScalar
globalStatActiveCPUCount = _GlobalStatActiveCPUCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 39),
    _GlobalStatActiveCPUCount_Type()
)
globalStatActiveCPUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatActiveCPUCount.setStatus("mandatory")
_GlobalStatANIPPercent_Type = Integer32
_GlobalStatANIPPercent_Object = MibScalar
globalStatANIPPercent = _GlobalStatANIPPercent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 40),
    _GlobalStatANIPPercent_Type()
)
globalStatANIPPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatANIPPercent.setStatus("mandatory")
_GlobalStatMaxANIPPercent_Type = Integer32
_GlobalStatMaxANIPPercent_Object = MibScalar
globalStatMaxANIPPercent = _GlobalStatMaxANIPPercent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 41),
    _GlobalStatMaxANIPPercent_Type()
)
globalStatMaxANIPPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMaxANIPPercent.setStatus("mandatory")
_GlobalStatMemoryErrors_Type = Counter32
_GlobalStatMemoryErrors_Object = MibScalar
globalStatMemoryErrors = _GlobalStatMemoryErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 42),
    _GlobalStatMemoryErrors_Type()
)
globalStatMemoryErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryErrors.setStatus("mandatory")
_GlobalStatNoNodeErrors_Type = Counter32
_GlobalStatNoNodeErrors_Object = MibScalar
globalStatNoNodeErrors = _GlobalStatNoNodeErrors_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 43),
    _GlobalStatNoNodeErrors_Type()
)
globalStatNoNodeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatNoNodeErrors.setStatus("mandatory")
_GlobalStatMemoryInUse_Type = Integer32
_GlobalStatMemoryInUse_Object = MibScalar
globalStatMemoryInUse = _GlobalStatMemoryInUse_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 44),
    _GlobalStatMemoryInUse_Type()
)
globalStatMemoryInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryInUse.setStatus("mandatory")
_GlobalStatMemoryMaxUsed_Type = Integer32
_GlobalStatMemoryMaxUsed_Object = MibScalar
globalStatMemoryMaxUsed = _GlobalStatMemoryMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 45),
    _GlobalStatMemoryMaxUsed_Type()
)
globalStatMemoryMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryMaxUsed.setStatus("mandatory")
_GlobalStatMemoryCurrentSize_Type = Integer32
_GlobalStatMemoryCurrentSize_Object = MibScalar
globalStatMemoryCurrentSize = _GlobalStatMemoryCurrentSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 46),
    _GlobalStatMemoryCurrentSize_Type()
)
globalStatMemoryCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatMemoryCurrentSize.setStatus("mandatory")
_GlobalStatCPUTemperature_Type = Integer32
_GlobalStatCPUTemperature_Object = MibScalar
globalStatCPUTemperature = _GlobalStatCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 47),
    _GlobalStatCPUTemperature_Type()
)
globalStatCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatCPUTemperature.setStatus("deprecated")
_GlobalStatFanSpeed_Type = Integer32
_GlobalStatFanSpeed_Object = MibScalar
globalStatFanSpeed = _GlobalStatFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 1, 2, 48),
    _GlobalStatFanSpeed_Type()
)
globalStatFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    globalStatFanSpeed.setStatus("deprecated")
_VirtualAddress_ObjectIdentity = ObjectIdentity
virtualAddress = _VirtualAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2)
)


class _VirtualAddressNumber_Type(Integer32):
    """Custom type virtualAddressNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressNumber_Type.__name__ = "Integer32"
_VirtualAddressNumber_Object = MibScalar
virtualAddressNumber = _VirtualAddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 1),
    _VirtualAddressNumber_Type()
)
virtualAddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressNumber.setStatus("mandatory")
_VirtualAddressTable_Object = MibTable
virtualAddressTable = _VirtualAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    virtualAddressTable.setStatus("mandatory")
_VirtualAddressEntry_Object = MibTableRow
virtualAddressEntry = _VirtualAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1)
)
virtualAddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualAddressIpAddress"),
)
if mibBuilder.loadTexts:
    virtualAddressEntry.setStatus("mandatory")
_VirtualAddressIpAddress_Type = IpAddress
_VirtualAddressIpAddress_Object = MibTableColumn
virtualAddressIpAddress = _VirtualAddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 1),
    _VirtualAddressIpAddress_Type()
)
virtualAddressIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressIpAddress.setStatus("mandatory")


class _VirtualAddressStatus_Type(Integer32):
    """Custom type virtualAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_VirtualAddressStatus_Type.__name__ = "Integer32"
_VirtualAddressStatus_Object = MibTableColumn
virtualAddressStatus = _VirtualAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 2),
    _VirtualAddressStatus_Type()
)
virtualAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressStatus.setStatus("mandatory")


class _VirtualAddressConnLimit_Type(Integer32):
    """Custom type virtualAddressConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressConnLimit_Type.__name__ = "Integer32"
_VirtualAddressConnLimit_Object = MibTableColumn
virtualAddressConnLimit = _VirtualAddressConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 3),
    _VirtualAddressConnLimit_Type()
)
virtualAddressConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressConnLimit.setStatus("mandatory")
_VirtualAddressNetmask_Type = IpAddress
_VirtualAddressNetmask_Object = MibTableColumn
virtualAddressNetmask = _VirtualAddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 4),
    _VirtualAddressNetmask_Type()
)
virtualAddressNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressNetmask.setStatus("mandatory")
_VirtualAddressBroadcast_Type = IpAddress
_VirtualAddressBroadcast_Object = MibTableColumn
virtualAddressBroadcast = _VirtualAddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 5),
    _VirtualAddressBroadcast_Type()
)
virtualAddressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressBroadcast.setStatus("mandatory")


class _VirtualAddressInterface_Type(DisplayString):
    """Custom type virtualAddressInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VirtualAddressInterface_Type.__name__ = "DisplayString"
_VirtualAddressInterface_Object = MibTableColumn
virtualAddressInterface = _VirtualAddressInterface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 6),
    _VirtualAddressInterface_Type()
)
virtualAddressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressInterface.setStatus("deprecated")


class _VirtualAddressFailoverFlags_Type(Integer32):
    """Custom type virtualAddressFailoverFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mirrorconnections", 1),
          ("mirrorconnectionspersistence", 3),
          ("mirrorpersistence", 2))
    )


_VirtualAddressFailoverFlags_Type.__name__ = "Integer32"
_VirtualAddressFailoverFlags_Object = MibTableColumn
virtualAddressFailoverFlags = _VirtualAddressFailoverFlags_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 7),
    _VirtualAddressFailoverFlags_Type()
)
virtualAddressFailoverFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressFailoverFlags.setStatus("mandatory")
_VirtualAddressOctetsIn_Type = Counter32
_VirtualAddressOctetsIn_Object = MibTableColumn
virtualAddressOctetsIn = _VirtualAddressOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 8),
    _VirtualAddressOctetsIn_Type()
)
virtualAddressOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsIn.setStatus("mandatory")
_VirtualAddressOctetsOut_Type = Counter32
_VirtualAddressOctetsOut_Object = MibTableColumn
virtualAddressOctetsOut = _VirtualAddressOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 9),
    _VirtualAddressOctetsOut_Type()
)
virtualAddressOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsOut.setStatus("mandatory")
_VirtualAddressPacketsIn_Type = Counter32
_VirtualAddressPacketsIn_Object = MibTableColumn
virtualAddressPacketsIn = _VirtualAddressPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 10),
    _VirtualAddressPacketsIn_Type()
)
virtualAddressPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsIn.setStatus("mandatory")
_VirtualAddressPacketsOut_Type = Counter32
_VirtualAddressPacketsOut_Object = MibTableColumn
virtualAddressPacketsOut = _VirtualAddressPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 11),
    _VirtualAddressPacketsOut_Type()
)
virtualAddressPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsOut.setStatus("mandatory")


class _VirtualAddressCurrentConn_Type(Integer32):
    """Custom type virtualAddressCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressCurrentConn_Type.__name__ = "Integer32"
_VirtualAddressCurrentConn_Object = MibTableColumn
virtualAddressCurrentConn = _VirtualAddressCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 12),
    _VirtualAddressCurrentConn_Type()
)
virtualAddressCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressCurrentConn.setStatus("mandatory")


class _VirtualAddressMaxConn_Type(Integer32):
    """Custom type virtualAddressMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualAddressMaxConn_Type.__name__ = "Integer32"
_VirtualAddressMaxConn_Object = MibTableColumn
virtualAddressMaxConn = _VirtualAddressMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 13),
    _VirtualAddressMaxConn_Type()
)
virtualAddressMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressMaxConn.setStatus("mandatory")
_VirtualAddressTotalConn_Type = Counter32
_VirtualAddressTotalConn_Object = MibTableColumn
virtualAddressTotalConn = _VirtualAddressTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 14),
    _VirtualAddressTotalConn_Type()
)
virtualAddressTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressTotalConn.setStatus("mandatory")
_VirtualAddressOctetsInHi32_Type = Counter32
_VirtualAddressOctetsInHi32_Object = MibTableColumn
virtualAddressOctetsInHi32 = _VirtualAddressOctetsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 15),
    _VirtualAddressOctetsInHi32_Type()
)
virtualAddressOctetsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsInHi32.setStatus("mandatory")
_VirtualAddressOctetsOutHi32_Type = Counter32
_VirtualAddressOctetsOutHi32_Object = MibTableColumn
virtualAddressOctetsOutHi32 = _VirtualAddressOctetsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 16),
    _VirtualAddressOctetsOutHi32_Type()
)
virtualAddressOctetsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressOctetsOutHi32.setStatus("mandatory")
_VirtualAddressPacketsInHi32_Type = Counter32
_VirtualAddressPacketsInHi32_Object = MibTableColumn
virtualAddressPacketsInHi32 = _VirtualAddressPacketsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 17),
    _VirtualAddressPacketsInHi32_Type()
)
virtualAddressPacketsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsInHi32.setStatus("mandatory")
_VirtualAddressPacketsOutHi32_Type = Counter32
_VirtualAddressPacketsOutHi32_Object = MibTableColumn
virtualAddressPacketsOutHi32 = _VirtualAddressPacketsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 18),
    _VirtualAddressPacketsOutHi32_Type()
)
virtualAddressPacketsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressPacketsOutHi32.setStatus("mandatory")
_VirtualAddressUnitId_Type = Integer32
_VirtualAddressUnitId_Object = MibTableColumn
virtualAddressUnitId = _VirtualAddressUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 2, 2, 1, 19),
    _VirtualAddressUnitId_Type()
)
virtualAddressUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualAddressUnitId.setStatus("mandatory")
_VirtualServer_ObjectIdentity = ObjectIdentity
virtualServer = _VirtualServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3)
)


class _VirtualServerNumber_Type(Integer32):
    """Custom type virtualServerNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerNumber_Type.__name__ = "Integer32"
_VirtualServerNumber_Object = MibScalar
virtualServerNumber = _VirtualServerNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 1),
    _VirtualServerNumber_Type()
)
virtualServerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerNumber.setStatus("mandatory")
_VirtualServerTable_Object = MibTable
virtualServerTable = _VirtualServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    virtualServerTable.setStatus("mandatory")
_VirtualServerEntry_Object = MibTableRow
virtualServerEntry = _VirtualServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1)
)
virtualServerEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualServerIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "virtualServerPort"),
)
if mibBuilder.loadTexts:
    virtualServerEntry.setStatus("mandatory")
_VirtualServerIpAddress_Type = IpAddress
_VirtualServerIpAddress_Object = MibTableColumn
virtualServerIpAddress = _VirtualServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 1),
    _VirtualServerIpAddress_Type()
)
virtualServerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerIpAddress.setStatus("mandatory")


class _VirtualServerPort_Type(Integer32):
    """Custom type virtualServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerPort_Type.__name__ = "Integer32"
_VirtualServerPort_Object = MibTableColumn
virtualServerPort = _VirtualServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 2),
    _VirtualServerPort_Type()
)
virtualServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPort.setStatus("mandatory")


class _VirtualServerStatus_Type(Integer32):
    """Custom type virtualServerStatus based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("noNodeAvailable", 3),
          ("notOnThisUnit", 4))
    )


_VirtualServerStatus_Type.__name__ = "Integer32"
_VirtualServerStatus_Object = MibTableColumn
virtualServerStatus = _VirtualServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 3),
    _VirtualServerStatus_Type()
)
virtualServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStatus.setStatus("mandatory")


class _VirtualServerConnLimit_Type(Integer32):
    """Custom type virtualServerConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerConnLimit_Type.__name__ = "Integer32"
_VirtualServerConnLimit_Object = MibTableColumn
virtualServerConnLimit = _VirtualServerConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 4),
    _VirtualServerConnLimit_Type()
)
virtualServerConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerConnLimit.setStatus("mandatory")


class _VirtualServerAppProtocol_Type(Integer32):
    """Custom type virtualServerAppProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cookie", 3),
          ("none", 1),
          ("ssl", 2))
    )


_VirtualServerAppProtocol_Type.__name__ = "Integer32"
_VirtualServerAppProtocol_Object = MibTableColumn
virtualServerAppProtocol = _VirtualServerAppProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 5),
    _VirtualServerAppProtocol_Type()
)
virtualServerAppProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocol.setStatus("deprecated")


class _VirtualServerAppProtocolTimeout_Type(Integer32):
    """Custom type virtualServerAppProtocolTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerAppProtocolTimeout_Type.__name__ = "Integer32"
_VirtualServerAppProtocolTimeout_Object = MibTableColumn
virtualServerAppProtocolTimeout = _VirtualServerAppProtocolTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 6),
    _VirtualServerAppProtocolTimeout_Type()
)
virtualServerAppProtocolTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocolTimeout.setStatus("deprecated")


class _VirtualServerAppProtocolReaper_Type(Integer32):
    """Custom type virtualServerAppProtocolReaper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerAppProtocolReaper_Type.__name__ = "Integer32"
_VirtualServerAppProtocolReaper_Object = MibTableColumn
virtualServerAppProtocolReaper = _VirtualServerAppProtocolReaper_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 7),
    _VirtualServerAppProtocolReaper_Type()
)
virtualServerAppProtocolReaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAppProtocolReaper.setStatus("deprecated")
_VirtualServerPersistTimeout_Type = Integer32
_VirtualServerPersistTimeout_Object = MibTableColumn
virtualServerPersistTimeout = _VirtualServerPersistTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 8),
    _VirtualServerPersistTimeout_Type()
)
virtualServerPersistTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistTimeout.setStatus("mandatory")
_VirtualServerPersistMask_Type = IpAddress
_VirtualServerPersistMask_Object = MibTableColumn
virtualServerPersistMask = _VirtualServerPersistMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 9),
    _VirtualServerPersistMask_Type()
)
virtualServerPersistMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPersistMask.setStatus("mandatory")


class _VirtualServerSticky_Type(Integer32):
    """Custom type virtualServerSticky based on Integer32"""
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


_VirtualServerSticky_Type.__name__ = "Integer32"
_VirtualServerSticky_Object = MibTableColumn
virtualServerSticky = _VirtualServerSticky_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 10),
    _VirtualServerSticky_Type()
)
virtualServerSticky.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSticky.setStatus("mandatory")
_VirtualServerStickyMask_Type = IpAddress
_VirtualServerStickyMask_Object = MibTableColumn
virtualServerStickyMask = _VirtualServerStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 11),
    _VirtualServerStickyMask_Type()
)
virtualServerStickyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerStickyMask.setStatus("mandatory")


class _VirtualServerFailoverFlags_Type(Integer32):
    """Custom type virtualServerFailoverFlags based on Integer32"""
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
        *(("mirrorconnections", 1),
          ("mirrorconnectionspersistence", 3),
          ("mirrorpersistence", 2),
          ("nomirroring", 4))
    )


_VirtualServerFailoverFlags_Type.__name__ = "Integer32"
_VirtualServerFailoverFlags_Object = MibTableColumn
virtualServerFailoverFlags = _VirtualServerFailoverFlags_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 12),
    _VirtualServerFailoverFlags_Type()
)
virtualServerFailoverFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerFailoverFlags.setStatus("mandatory")
_VirtualServerOctetsIn_Type = Counter32
_VirtualServerOctetsIn_Object = MibTableColumn
virtualServerOctetsIn = _VirtualServerOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 13),
    _VirtualServerOctetsIn_Type()
)
virtualServerOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsIn.setStatus("mandatory")
_VirtualServerOctetsOut_Type = Counter32
_VirtualServerOctetsOut_Object = MibTableColumn
virtualServerOctetsOut = _VirtualServerOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 14),
    _VirtualServerOctetsOut_Type()
)
virtualServerOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsOut.setStatus("mandatory")
_VirtualServerPacketsIn_Type = Counter32
_VirtualServerPacketsIn_Object = MibTableColumn
virtualServerPacketsIn = _VirtualServerPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 15),
    _VirtualServerPacketsIn_Type()
)
virtualServerPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsIn.setStatus("mandatory")
_VirtualServerPacketsOut_Type = Counter32
_VirtualServerPacketsOut_Object = MibTableColumn
virtualServerPacketsOut = _VirtualServerPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 16),
    _VirtualServerPacketsOut_Type()
)
virtualServerPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsOut.setStatus("mandatory")


class _VirtualServerCurrentConn_Type(Integer32):
    """Custom type virtualServerCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerCurrentConn_Type.__name__ = "Integer32"
_VirtualServerCurrentConn_Object = MibTableColumn
virtualServerCurrentConn = _VirtualServerCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 17),
    _VirtualServerCurrentConn_Type()
)
virtualServerCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerCurrentConn.setStatus("mandatory")


class _VirtualServerMaxConn_Type(Integer32):
    """Custom type virtualServerMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VirtualServerMaxConn_Type.__name__ = "Integer32"
_VirtualServerMaxConn_Object = MibTableColumn
virtualServerMaxConn = _VirtualServerMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 18),
    _VirtualServerMaxConn_Type()
)
virtualServerMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerMaxConn.setStatus("mandatory")
_VirtualServerTotalConn_Type = Counter32
_VirtualServerTotalConn_Object = MibTableColumn
virtualServerTotalConn = _VirtualServerTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 19),
    _VirtualServerTotalConn_Type()
)
virtualServerTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerTotalConn.setStatus("mandatory")
_VirtualServerSslNew_Type = Counter32
_VirtualServerSslNew_Object = MibTableColumn
virtualServerSslNew = _VirtualServerSslNew_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 20),
    _VirtualServerSslNew_Type()
)
virtualServerSslNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslNew.setStatus("mandatory")
_VirtualServerSslHits_Type = Counter32
_VirtualServerSslHits_Object = MibTableColumn
virtualServerSslHits = _VirtualServerSslHits_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 21),
    _VirtualServerSslHits_Type()
)
virtualServerSslHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslHits.setStatus("mandatory")
_VirtualServerSslTimeouts_Type = Counter32
_VirtualServerSslTimeouts_Object = MibTableColumn
virtualServerSslTimeouts = _VirtualServerSslTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 22),
    _VirtualServerSslTimeouts_Type()
)
virtualServerSslTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslTimeouts.setStatus("mandatory")
_VirtualServerSslMisses_Type = Counter32
_VirtualServerSslMisses_Object = MibTableColumn
virtualServerSslMisses = _VirtualServerSslMisses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 23),
    _VirtualServerSslMisses_Type()
)
virtualServerSslMisses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSslMisses.setStatus("mandatory")
_VirtualServerOctetsInHi32_Type = Counter32
_VirtualServerOctetsInHi32_Object = MibTableColumn
virtualServerOctetsInHi32 = _VirtualServerOctetsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 24),
    _VirtualServerOctetsInHi32_Type()
)
virtualServerOctetsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsInHi32.setStatus("mandatory")
_VirtualServerOctetsOutHi32_Type = Counter32
_VirtualServerOctetsOutHi32_Object = MibTableColumn
virtualServerOctetsOutHi32 = _VirtualServerOctetsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 25),
    _VirtualServerOctetsOutHi32_Type()
)
virtualServerOctetsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerOctetsOutHi32.setStatus("mandatory")
_VirtualServerPacketsInHi32_Type = Counter32
_VirtualServerPacketsInHi32_Object = MibTableColumn
virtualServerPacketsInHi32 = _VirtualServerPacketsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 26),
    _VirtualServerPacketsInHi32_Type()
)
virtualServerPacketsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsInHi32.setStatus("mandatory")
_VirtualServerPacketsOutHi32_Type = Counter32
_VirtualServerPacketsOutHi32_Object = MibTableColumn
virtualServerPacketsOutHi32 = _VirtualServerPacketsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 27),
    _VirtualServerPacketsOutHi32_Type()
)
virtualServerPacketsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPacketsOutHi32.setStatus("mandatory")


class _VirtualServerCookieMethod_Type(Integer32):
    """Custom type virtualServerCookieMethod based on Integer32"""
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
        *(("hash", 5),
          ("insert", 2),
          ("passive", 4),
          ("rewrite", 3),
          ("unspecified", 1))
    )


_VirtualServerCookieMethod_Type.__name__ = "Integer32"
_VirtualServerCookieMethod_Object = MibTableColumn
virtualServerCookieMethod = _VirtualServerCookieMethod_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 28),
    _VirtualServerCookieMethod_Type()
)
virtualServerCookieMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerCookieMethod.setStatus("mandatory")


class _VirtualServerRule_Type(DisplayString):
    """Custom type virtualServerRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualServerRule_Type.__name__ = "DisplayString"
_VirtualServerRule_Object = MibTableColumn
virtualServerRule = _VirtualServerRule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 29),
    _VirtualServerRule_Type()
)
virtualServerRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerRule.setStatus("mandatory")


class _VirtualServerPool_Type(DisplayString):
    """Custom type virtualServerPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualServerPool_Type.__name__ = "DisplayString"
_VirtualServerPool_Object = MibTableColumn
virtualServerPool = _VirtualServerPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 30),
    _VirtualServerPool_Type()
)
virtualServerPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerPool.setStatus("mandatory")


class _VirtualServerARPEnabled_Type(Integer32):
    """Custom type virtualServerARPEnabled based on Integer32"""
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


_VirtualServerARPEnabled_Type.__name__ = "Integer32"
_VirtualServerARPEnabled_Object = MibTableColumn
virtualServerARPEnabled = _VirtualServerARPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 31),
    _VirtualServerARPEnabled_Type()
)
virtualServerARPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerARPEnabled.setStatus("mandatory")


class _VirtualServerLastHopPool_Type(DisplayString):
    """Custom type virtualServerLastHopPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VirtualServerLastHopPool_Type.__name__ = "DisplayString"
_VirtualServerLastHopPool_Object = MibTableColumn
virtualServerLastHopPool = _VirtualServerLastHopPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 32),
    _VirtualServerLastHopPool_Type()
)
virtualServerLastHopPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerLastHopPool.setStatus("mandatory")


class _VirtualServerTranslateAddress_Type(Integer32):
    """Custom type virtualServerTranslateAddress based on Integer32"""
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


_VirtualServerTranslateAddress_Type.__name__ = "Integer32"
_VirtualServerTranslateAddress_Object = MibTableColumn
virtualServerTranslateAddress = _VirtualServerTranslateAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 33),
    _VirtualServerTranslateAddress_Type()
)
virtualServerTranslateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerTranslateAddress.setStatus("mandatory")


class _VirtualServerTranslatePort_Type(Integer32):
    """Custom type virtualServerTranslatePort based on Integer32"""
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


_VirtualServerTranslatePort_Type.__name__ = "Integer32"
_VirtualServerTranslatePort_Object = MibTableColumn
virtualServerTranslatePort = _VirtualServerTranslatePort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 34),
    _VirtualServerTranslatePort_Type()
)
virtualServerTranslatePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerTranslatePort.setStatus("mandatory")


class _VirtualServerSvcDownReset_Type(Integer32):
    """Custom type virtualServerSvcDownReset based on Integer32"""
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


_VirtualServerSvcDownReset_Type.__name__ = "Integer32"
_VirtualServerSvcDownReset_Object = MibTableColumn
virtualServerSvcDownReset = _VirtualServerSvcDownReset_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 35),
    _VirtualServerSvcDownReset_Type()
)
virtualServerSvcDownReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerSvcDownReset.setStatus("mandatory")


class _VirtualServerMayUseProxy_Type(Integer32):
    """Custom type virtualServerMayUseProxy based on Integer32"""
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


_VirtualServerMayUseProxy_Type.__name__ = "Integer32"
_VirtualServerMayUseProxy_Object = MibTableColumn
virtualServerMayUseProxy = _VirtualServerMayUseProxy_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 36),
    _VirtualServerMayUseProxy_Type()
)
virtualServerMayUseProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerMayUseProxy.setStatus("mandatory")


class _VirtualServerAccelerate_Type(Integer32):
    """Custom type virtualServerAccelerate based on Integer32"""
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


_VirtualServerAccelerate_Type.__name__ = "Integer32"
_VirtualServerAccelerate_Object = MibTableColumn
virtualServerAccelerate = _VirtualServerAccelerate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 3, 2, 1, 37),
    _VirtualServerAccelerate_Type()
)
virtualServerAccelerate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    virtualServerAccelerate.setStatus("mandatory")
_Snat_ObjectIdentity = ObjectIdentity
snat = _Snat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4)
)
_SnatTransTable_Object = MibTable
snatTransTable = _SnatTransTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    snatTransTable.setStatus("mandatory")
_SnatTransEntry_Object = MibTableRow
snatTransEntry = _SnatTransEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1)
)
snatTransEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "snatTransAddr"),
)
if mibBuilder.loadTexts:
    snatTransEntry.setStatus("mandatory")


class _SnatTransEnabled_Type(Integer32):
    """Custom type snatTransEnabled based on Integer32"""
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


_SnatTransEnabled_Type.__name__ = "Integer32"
_SnatTransEnabled_Object = MibTableColumn
snatTransEnabled = _SnatTransEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 1),
    _SnatTransEnabled_Type()
)
snatTransEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransEnabled.setStatus("mandatory")
_SnatTransAddr_Type = IpAddress
_SnatTransAddr_Object = MibTableColumn
snatTransAddr = _SnatTransAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 2),
    _SnatTransAddr_Type()
)
snatTransAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransAddr.setStatus("mandatory")


class _SnatTransIface_Type(DisplayString):
    """Custom type snatTransIface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_SnatTransIface_Type.__name__ = "DisplayString"
_SnatTransIface_Object = MibTableColumn
snatTransIface = _SnatTransIface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 3),
    _SnatTransIface_Type()
)
snatTransIface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransIface.setStatus("deprecated")
_SnatTransNetmask_Type = IpAddress
_SnatTransNetmask_Object = MibTableColumn
snatTransNetmask = _SnatTransNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 4),
    _SnatTransNetmask_Type()
)
snatTransNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransNetmask.setStatus("mandatory")
_SnatTransBroadcast_Type = IpAddress
_SnatTransBroadcast_Object = MibTableColumn
snatTransBroadcast = _SnatTransBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 5),
    _SnatTransBroadcast_Type()
)
snatTransBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBroadcast.setStatus("mandatory")
_SnatTransSecsCollectingStats_Type = Counter32
_SnatTransSecsCollectingStats_Object = MibTableColumn
snatTransSecsCollectingStats = _SnatTransSecsCollectingStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 6),
    _SnatTransSecsCollectingStats_Type()
)
snatTransSecsCollectingStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransSecsCollectingStats.setStatus("mandatory")
_SnatTransBitsIn_Type = Counter32
_SnatTransBitsIn_Object = MibTableColumn
snatTransBitsIn = _SnatTransBitsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 7),
    _SnatTransBitsIn_Type()
)
snatTransBitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsIn.setStatus("mandatory")
_SnatTransBitsOut_Type = Counter32
_SnatTransBitsOut_Object = MibTableColumn
snatTransBitsOut = _SnatTransBitsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 8),
    _SnatTransBitsOut_Type()
)
snatTransBitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsOut.setStatus("mandatory")
_SnatTransPktsIn_Type = Counter32
_SnatTransPktsIn_Object = MibTableColumn
snatTransPktsIn = _SnatTransPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 9),
    _SnatTransPktsIn_Type()
)
snatTransPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsIn.setStatus("mandatory")
_SnatTransPktsOut_Type = Counter32
_SnatTransPktsOut_Object = MibTableColumn
snatTransPktsOut = _SnatTransPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 10),
    _SnatTransPktsOut_Type()
)
snatTransPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsOut.setStatus("mandatory")
_SnatTransCurrConns_Type = Integer32
_SnatTransCurrConns_Object = MibTableColumn
snatTransCurrConns = _SnatTransCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 11),
    _SnatTransCurrConns_Type()
)
snatTransCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransCurrConns.setStatus("mandatory")
_SnatTransMaxConns_Type = Integer32
_SnatTransMaxConns_Object = MibTableColumn
snatTransMaxConns = _SnatTransMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 12),
    _SnatTransMaxConns_Type()
)
snatTransMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransMaxConns.setStatus("mandatory")
_SnatTransTotalConns_Type = Counter32
_SnatTransTotalConns_Object = MibTableColumn
snatTransTotalConns = _SnatTransTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 13),
    _SnatTransTotalConns_Type()
)
snatTransTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransTotalConns.setStatus("mandatory")
_SnatTransBitsInHi32_Type = Counter32
_SnatTransBitsInHi32_Object = MibTableColumn
snatTransBitsInHi32 = _SnatTransBitsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 14),
    _SnatTransBitsInHi32_Type()
)
snatTransBitsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsInHi32.setStatus("mandatory")
_SnatTransBitsOutHi32_Type = Counter32
_SnatTransBitsOutHi32_Object = MibTableColumn
snatTransBitsOutHi32 = _SnatTransBitsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 15),
    _SnatTransBitsOutHi32_Type()
)
snatTransBitsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransBitsOutHi32.setStatus("mandatory")
_SnatTransPktsInHi32_Type = Counter32
_SnatTransPktsInHi32_Object = MibTableColumn
snatTransPktsInHi32 = _SnatTransPktsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 16),
    _SnatTransPktsInHi32_Type()
)
snatTransPktsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsInHi32.setStatus("mandatory")
_SnatTransPktsOutHi32_Type = Counter32
_SnatTransPktsOutHi32_Object = MibTableColumn
snatTransPktsOutHi32 = _SnatTransPktsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 17),
    _SnatTransPktsOutHi32_Type()
)
snatTransPktsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransPktsOutHi32.setStatus("mandatory")
_SnatTransLastTransPort_Type = Integer32
_SnatTransLastTransPort_Object = MibTableColumn
snatTransLastTransPort = _SnatTransLastTransPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 18),
    _SnatTransLastTransPort_Type()
)
snatTransLastTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransLastTransPort.setStatus("mandatory")
_SnatTransUnitId_Type = Integer32
_SnatTransUnitId_Object = MibTableColumn
snatTransUnitId = _SnatTransUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 19),
    _SnatTransUnitId_Type()
)
snatTransUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransUnitId.setStatus("mandatory")


class _SnatTransVLANs_Type(DisplayString):
    """Custom type snatTransVLANs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnatTransVLANs_Type.__name__ = "DisplayString"
_SnatTransVLANs_Object = MibTableColumn
snatTransVLANs = _SnatTransVLANs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 20),
    _SnatTransVLANs_Type()
)
snatTransVLANs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransVLANs.setStatus("mandatory")


class _SnatTransServices_Type(DisplayString):
    """Custom type snatTransServices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnatTransServices_Type.__name__ = "DisplayString"
_SnatTransServices_Object = MibTableColumn
snatTransServices = _SnatTransServices_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 1, 1, 21),
    _SnatTransServices_Type()
)
snatTransServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTransServices.setStatus("mandatory")
_SnatOrigTable_Object = MibTable
snatOrigTable = _SnatOrigTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    snatOrigTable.setStatus("mandatory")
_SnatOrigEntry_Object = MibTableRow
snatOrigEntry = _SnatOrigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1)
)
snatOrigEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "snatOrigAddr"),
)
if mibBuilder.loadTexts:
    snatOrigEntry.setStatus("mandatory")


class _SnatOrigEnabled_Type(Integer32):
    """Custom type snatOrigEnabled based on Integer32"""
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


_SnatOrigEnabled_Type.__name__ = "Integer32"
_SnatOrigEnabled_Object = MibTableColumn
snatOrigEnabled = _SnatOrigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 1),
    _SnatOrigEnabled_Type()
)
snatOrigEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigEnabled.setStatus("mandatory")
_SnatOrigAddr_Type = IpAddress
_SnatOrigAddr_Object = MibTableColumn
snatOrigAddr = _SnatOrigAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 2),
    _SnatOrigAddr_Type()
)
snatOrigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigAddr.setStatus("mandatory")
_SnatOrigConnLimit_Type = Integer32
_SnatOrigConnLimit_Object = MibTableColumn
snatOrigConnLimit = _SnatOrigConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 3),
    _SnatOrigConnLimit_Type()
)
snatOrigConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigConnLimit.setStatus("mandatory")
_SnatOrigTransAddr_Type = IpAddress
_SnatOrigTransAddr_Object = MibTableColumn
snatOrigTransAddr = _SnatOrigTransAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 4),
    _SnatOrigTransAddr_Type()
)
snatOrigTransAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTransAddr.setStatus("mandatory")
_SnatOrigTcpIdleTimeout_Type = Counter32
_SnatOrigTcpIdleTimeout_Object = MibTableColumn
snatOrigTcpIdleTimeout = _SnatOrigTcpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 5),
    _SnatOrigTcpIdleTimeout_Type()
)
snatOrigTcpIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTcpIdleTimeout.setStatus("mandatory")
_SnatOrigUdpIdleTimeout_Type = Counter32
_SnatOrigUdpIdleTimeout_Object = MibTableColumn
snatOrigUdpIdleTimeout = _SnatOrigUdpIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 6),
    _SnatOrigUdpIdleTimeout_Type()
)
snatOrigUdpIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigUdpIdleTimeout.setStatus("mandatory")
_SnatOrigStatsZeroTime_Type = Counter32
_SnatOrigStatsZeroTime_Object = MibTableColumn
snatOrigStatsZeroTime = _SnatOrigStatsZeroTime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 7),
    _SnatOrigStatsZeroTime_Type()
)
snatOrigStatsZeroTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigStatsZeroTime.setStatus("mandatory")
_SnatOrigSecsCollectingStats_Type = Counter32
_SnatOrigSecsCollectingStats_Object = MibTableColumn
snatOrigSecsCollectingStats = _SnatOrigSecsCollectingStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 8),
    _SnatOrigSecsCollectingStats_Type()
)
snatOrigSecsCollectingStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigSecsCollectingStats.setStatus("mandatory")
_SnatOrigBitsIn_Type = Counter32
_SnatOrigBitsIn_Object = MibTableColumn
snatOrigBitsIn = _SnatOrigBitsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 9),
    _SnatOrigBitsIn_Type()
)
snatOrigBitsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsIn.setStatus("mandatory")
_SnatOrigBitsOut_Type = Counter32
_SnatOrigBitsOut_Object = MibTableColumn
snatOrigBitsOut = _SnatOrigBitsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 10),
    _SnatOrigBitsOut_Type()
)
snatOrigBitsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsOut.setStatus("mandatory")
_SnatOrigPktsIn_Type = Counter32
_SnatOrigPktsIn_Object = MibTableColumn
snatOrigPktsIn = _SnatOrigPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 11),
    _SnatOrigPktsIn_Type()
)
snatOrigPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsIn.setStatus("mandatory")
_SnatOrigPktsOut_Type = Counter32
_SnatOrigPktsOut_Object = MibTableColumn
snatOrigPktsOut = _SnatOrigPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 12),
    _SnatOrigPktsOut_Type()
)
snatOrigPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsOut.setStatus("mandatory")
_SnatOrigCurrConns_Type = Integer32
_SnatOrigCurrConns_Object = MibTableColumn
snatOrigCurrConns = _SnatOrigCurrConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 13),
    _SnatOrigCurrConns_Type()
)
snatOrigCurrConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigCurrConns.setStatus("mandatory")
_SnatOrigMaxConns_Type = Integer32
_SnatOrigMaxConns_Object = MibTableColumn
snatOrigMaxConns = _SnatOrigMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 14),
    _SnatOrigMaxConns_Type()
)
snatOrigMaxConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigMaxConns.setStatus("mandatory")
_SnatOrigTotalConns_Type = Counter32
_SnatOrigTotalConns_Object = MibTableColumn
snatOrigTotalConns = _SnatOrigTotalConns_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 15),
    _SnatOrigTotalConns_Type()
)
snatOrigTotalConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigTotalConns.setStatus("mandatory")
_SnatOrigBitsInHi32_Type = Counter32
_SnatOrigBitsInHi32_Object = MibTableColumn
snatOrigBitsInHi32 = _SnatOrigBitsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 16),
    _SnatOrigBitsInHi32_Type()
)
snatOrigBitsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsInHi32.setStatus("mandatory")
_SnatOrigBitsOutHi32_Type = Counter32
_SnatOrigBitsOutHi32_Object = MibTableColumn
snatOrigBitsOutHi32 = _SnatOrigBitsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 17),
    _SnatOrigBitsOutHi32_Type()
)
snatOrigBitsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigBitsOutHi32.setStatus("mandatory")
_SnatOrigPktsInHi32_Type = Counter32
_SnatOrigPktsInHi32_Object = MibTableColumn
snatOrigPktsInHi32 = _SnatOrigPktsInHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 18),
    _SnatOrigPktsInHi32_Type()
)
snatOrigPktsInHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsInHi32.setStatus("mandatory")
_SnatOrigPktsOutHi32_Type = Counter32
_SnatOrigPktsOutHi32_Object = MibTableColumn
snatOrigPktsOutHi32 = _SnatOrigPktsOutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 19),
    _SnatOrigPktsOutHi32_Type()
)
snatOrigPktsOutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigPktsOutHi32.setStatus("mandatory")
_SnatOrigLastTransPort_Type = Integer32
_SnatOrigLastTransPort_Object = MibTableColumn
snatOrigLastTransPort = _SnatOrigLastTransPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 4, 2, 1, 20),
    _SnatOrigLastTransPort_Type()
)
snatOrigLastTransPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatOrigLastTransPort.setStatus("mandatory")
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5)
)


class _InterfaceNumber_Type(Integer32):
    """Custom type interfaceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_InterfaceNumber_Type.__name__ = "Integer32"
_InterfaceNumber_Object = MibScalar
interfaceNumber = _InterfaceNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 1),
    _InterfaceNumber_Type()
)
interfaceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceNumber.setStatus("mandatory")
_InterfaceTable_Object = MibTable
interfaceTable = _InterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    interfaceTable.setStatus("mandatory")
_InterfaceEntry_Object = MibTableRow
interfaceEntry = _InterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1)
)
interfaceEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "interfaceName"),
)
if mibBuilder.loadTexts:
    interfaceEntry.setStatus("mandatory")


class _InterfaceName_Type(DisplayString):
    """Custom type interfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_InterfaceName_Type.__name__ = "DisplayString"
_InterfaceName_Object = MibTableColumn
interfaceName = _InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 1),
    _InterfaceName_Type()
)
interfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceName.setStatus("mandatory")


class _InterfaceIpAddresses_Type(DisplayString):
    """Custom type interfaceIpAddresses based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceIpAddresses_Type.__name__ = "DisplayString"
_InterfaceIpAddresses_Object = MibTableColumn
interfaceIpAddresses = _InterfaceIpAddresses_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 2),
    _InterfaceIpAddresses_Type()
)
interfaceIpAddresses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceIpAddresses.setStatus("deprecated")


class _InterfaceDestination_Type(Integer32):
    """Custom type interfaceDestination based on Integer32"""
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


_InterfaceDestination_Type.__name__ = "Integer32"
_InterfaceDestination_Object = MibTableColumn
interfaceDestination = _InterfaceDestination_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 3),
    _InterfaceDestination_Type()
)
interfaceDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceDestination.setStatus("deprecated")


class _InterfaceSource_Type(Integer32):
    """Custom type interfaceSource based on Integer32"""
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


_InterfaceSource_Type.__name__ = "Integer32"
_InterfaceSource_Object = MibTableColumn
interfaceSource = _InterfaceSource_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 4),
    _InterfaceSource_Type()
)
interfaceSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSource.setStatus("deprecated")
_InterfaceTimeout_Type = Integer32
_InterfaceTimeout_Object = MibTableColumn
interfaceTimeout = _InterfaceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 5),
    _InterfaceTimeout_Type()
)
interfaceTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceTimeout.setStatus("deprecated")


class _InterfaceArmed_Type(Integer32):
    """Custom type interfaceArmed based on Integer32"""
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


_InterfaceArmed_Type.__name__ = "Integer32"
_InterfaceArmed_Object = MibTableColumn
interfaceArmed = _InterfaceArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 6),
    _InterfaceArmed_Type()
)
interfaceArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceArmed.setStatus("deprecated")


class _InterfaceVLANSEnabled_Type(Integer32):
    """Custom type interfaceVLANSEnabled based on Integer32"""
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


_InterfaceVLANSEnabled_Type.__name__ = "Integer32"
_InterfaceVLANSEnabled_Object = MibTableColumn
interfaceVLANSEnabled = _InterfaceVLANSEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 7),
    _InterfaceVLANSEnabled_Type()
)
interfaceVLANSEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceVLANSEnabled.setStatus("deprecated")


class _InterfaceMasqueradeAddress_Type(DisplayString):
    """Custom type interfaceMasqueradeAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMasqueradeAddress_Type.__name__ = "DisplayString"
_InterfaceMasqueradeAddress_Object = MibTableColumn
interfaceMasqueradeAddress = _InterfaceMasqueradeAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 8),
    _InterfaceMasqueradeAddress_Type()
)
interfaceMasqueradeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMasqueradeAddress.setStatus("mandatory")
_InterfaceLastTimeChanged_Type = Integer32
_InterfaceLastTimeChanged_Object = MibTableColumn
interfaceLastTimeChanged = _InterfaceLastTimeChanged_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 9),
    _InterfaceLastTimeChanged_Type()
)
interfaceLastTimeChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceLastTimeChanged.setStatus("mandatory")
_InterfaceSpeed_Type = Integer32
_InterfaceSpeed_Object = MibTableColumn
interfaceSpeed = _InterfaceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 10),
    _InterfaceSpeed_Type()
)
interfaceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceSpeed.setStatus("mandatory")


class _InterfaceFullDuplex_Type(Integer32):
    """Custom type interfaceFullDuplex based on Integer32"""
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


_InterfaceFullDuplex_Type.__name__ = "Integer32"
_InterfaceFullDuplex_Object = MibTableColumn
interfaceFullDuplex = _InterfaceFullDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 11),
    _InterfaceFullDuplex_Type()
)
interfaceFullDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceFullDuplex.setStatus("mandatory")


class _InterfaceMediaTypeActive_Type(DisplayString):
    """Custom type interfaceMediaTypeActive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMediaTypeActive_Type.__name__ = "DisplayString"
_InterfaceMediaTypeActive_Object = MibTableColumn
interfaceMediaTypeActive = _InterfaceMediaTypeActive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 12),
    _InterfaceMediaTypeActive_Type()
)
interfaceMediaTypeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMediaTypeActive.setStatus("mandatory")


class _InterfaceMediaDuplexActive_Type(DisplayString):
    """Custom type interfaceMediaDuplexActive based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMediaDuplexActive_Type.__name__ = "DisplayString"
_InterfaceMediaDuplexActive_Object = MibTableColumn
interfaceMediaDuplexActive = _InterfaceMediaDuplexActive_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 13),
    _InterfaceMediaDuplexActive_Type()
)
interfaceMediaDuplexActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMediaDuplexActive.setStatus("mandatory")


class _InterfaceMediaStatus_Type(Integer32):
    """Custom type interfaceMediaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("invalid", 3),
          ("nocarrier", 2))
    )


_InterfaceMediaStatus_Type.__name__ = "Integer32"
_InterfaceMediaStatus_Object = MibTableColumn
interfaceMediaStatus = _InterfaceMediaStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 14),
    _InterfaceMediaStatus_Type()
)
interfaceMediaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMediaStatus.setStatus("mandatory")


class _InterfaceMediaType_Type(DisplayString):
    """Custom type interfaceMediaType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMediaType_Type.__name__ = "DisplayString"
_InterfaceMediaType_Object = MibTableColumn
interfaceMediaType = _InterfaceMediaType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 15),
    _InterfaceMediaType_Type()
)
interfaceMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMediaType.setStatus("mandatory")


class _InterfaceMediaDuplex_Type(DisplayString):
    """Custom type interfaceMediaDuplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_InterfaceMediaDuplex_Type.__name__ = "DisplayString"
_InterfaceMediaDuplex_Object = MibTableColumn
interfaceMediaDuplex = _InterfaceMediaDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 16),
    _InterfaceMediaDuplex_Type()
)
interfaceMediaDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMediaDuplex.setStatus("mandatory")
_InterfaceMTU_Type = Integer32
_InterfaceMTU_Object = MibTableColumn
interfaceMTU = _InterfaceMTU_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 5, 2, 1, 17),
    _InterfaceMTU_Type()
)
interfaceMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    interfaceMTU.setStatus("mandatory")
_Ifaddress_ObjectIdentity = ObjectIdentity
ifaddress = _Ifaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6)
)


class _IfaddressNumber_Type(Integer32):
    """Custom type ifaddressNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IfaddressNumber_Type.__name__ = "Integer32"
_IfaddressNumber_Object = MibScalar
ifaddressNumber = _IfaddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 1),
    _IfaddressNumber_Type()
)
ifaddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressNumber.setStatus("deprecated")
_IfaddressTable_Object = MibTable
ifaddressTable = _IfaddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    ifaddressTable.setStatus("deprecated")
_IfaddressEntry_Object = MibTableRow
ifaddressEntry = _IfaddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1)
)
ifaddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "ifaddressIpAddress"),
)
if mibBuilder.loadTexts:
    ifaddressEntry.setStatus("deprecated")
_IfaddressIpAddress_Type = IpAddress
_IfaddressIpAddress_Object = MibTableColumn
ifaddressIpAddress = _IfaddressIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 1),
    _IfaddressIpAddress_Type()
)
ifaddressIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressIpAddress.setStatus("deprecated")


class _IfaddressInterfaceName_Type(DisplayString):
    """Custom type ifaddressInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IfaddressInterfaceName_Type.__name__ = "DisplayString"
_IfaddressInterfaceName_Object = MibTableColumn
ifaddressInterfaceName = _IfaddressInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 2),
    _IfaddressInterfaceName_Type()
)
ifaddressInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressInterfaceName.setStatus("deprecated")
_IfaddressNetmask_Type = IpAddress
_IfaddressNetmask_Object = MibTableColumn
ifaddressNetmask = _IfaddressNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 3),
    _IfaddressNetmask_Type()
)
ifaddressNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressNetmask.setStatus("deprecated")
_IfaddressBroadcast_Type = IpAddress
_IfaddressBroadcast_Object = MibTableColumn
ifaddressBroadcast = _IfaddressBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 4),
    _IfaddressBroadcast_Type()
)
ifaddressBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressBroadcast.setStatus("deprecated")


class _IfaddressType_Type(Integer32):
    """Custom type ifaddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipshared", 2),
          ("iptrue", 1))
    )


_IfaddressType_Type.__name__ = "Integer32"
_IfaddressType_Object = MibTableColumn
ifaddressType = _IfaddressType_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 5),
    _IfaddressType_Type()
)
ifaddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressType.setStatus("deprecated")
_IfaddressUnitId_Type = Integer32
_IfaddressUnitId_Object = MibTableColumn
ifaddressUnitId = _IfaddressUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 6),
    _IfaddressUnitId_Type()
)
ifaddressUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressUnitId.setStatus("deprecated")


class _IfaddressVLANTag_Type(DisplayString):
    """Custom type ifaddressVLANTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_IfaddressVLANTag_Type.__name__ = "DisplayString"
_IfaddressVLANTag_Object = MibTableColumn
ifaddressVLANTag = _IfaddressVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 6, 2, 1, 7),
    _IfaddressVLANTag_Type()
)
ifaddressVLANTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifaddressVLANTag.setStatus("deprecated")
_Pool_ObjectIdentity = ObjectIdentity
pool = _Pool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7)
)


class _PoolNumber_Type(Integer32):
    """Custom type poolNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolNumber_Type.__name__ = "Integer32"
_PoolNumber_Object = MibScalar
poolNumber = _PoolNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 1),
    _PoolNumber_Type()
)
poolNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolNumber.setStatus("mandatory")
_PoolTable_Object = MibTable
poolTable = _PoolTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    poolTable.setStatus("mandatory")
_PoolEntry_Object = MibTableRow
poolEntry = _PoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1)
)
poolEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "poolName"),
)
if mibBuilder.loadTexts:
    poolEntry.setStatus("mandatory")


class _PoolName_Type(DisplayString):
    """Custom type poolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolName_Type.__name__ = "DisplayString"
_PoolName_Object = MibTableColumn
poolName = _PoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 1),
    _PoolName_Type()
)
poolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolName.setStatus("mandatory")


class _PoolLBMode_Type(Integer32):
    """Custom type poolLBMode based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("dynamicRatio", 11),
          ("fastestAppResponse", 12),
          ("fastestNodeAddress", 8),
          ("leastConnMember", 3),
          ("leastConnNodeAddress", 7),
          ("observedMember", 4),
          ("observerdNodeAddress", 9),
          ("predictiveMember", 5),
          ("predictiveNodeAddress", 10),
          ("ratioMember", 2),
          ("ratioNodeAddress", 6),
          ("roundrobin", 1))
    )


_PoolLBMode_Type.__name__ = "Integer32"
_PoolLBMode_Object = MibTableColumn
poolLBMode = _PoolLBMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 2),
    _PoolLBMode_Type()
)
poolLBMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolLBMode.setStatus("mandatory")


class _PoolDependent_Type(Integer32):
    """Custom type poolDependent based on Integer32"""
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


_PoolDependent_Type.__name__ = "Integer32"
_PoolDependent_Object = MibTableColumn
poolDependent = _PoolDependent_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 3),
    _PoolDependent_Type()
)
poolDependent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolDependent.setStatus("mandatory")
_PoolMemberQty_Type = Integer32
_PoolMemberQty_Object = MibTableColumn
poolMemberQty = _PoolMemberQty_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 4),
    _PoolMemberQty_Type()
)
poolMemberQty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberQty.setStatus("mandatory")
_PoolBitsin_Type = Counter32
_PoolBitsin_Object = MibTableColumn
poolBitsin = _PoolBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 5),
    _PoolBitsin_Type()
)
poolBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsin.setStatus("mandatory")
_PoolBitsout_Type = Counter32
_PoolBitsout_Object = MibTableColumn
poolBitsout = _PoolBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 6),
    _PoolBitsout_Type()
)
poolBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsout.setStatus("mandatory")
_PoolBitsinHi32_Type = Counter32
_PoolBitsinHi32_Object = MibTableColumn
poolBitsinHi32 = _PoolBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 7),
    _PoolBitsinHi32_Type()
)
poolBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsinHi32.setStatus("mandatory")
_PoolBitsoutHi32_Type = Counter32
_PoolBitsoutHi32_Object = MibTableColumn
poolBitsoutHi32 = _PoolBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 8),
    _PoolBitsoutHi32_Type()
)
poolBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolBitsoutHi32.setStatus("mandatory")
_PoolPktsin_Type = Counter32
_PoolPktsin_Object = MibTableColumn
poolPktsin = _PoolPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 9),
    _PoolPktsin_Type()
)
poolPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsin.setStatus("mandatory")
_PoolPktsout_Type = Counter32
_PoolPktsout_Object = MibTableColumn
poolPktsout = _PoolPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 10),
    _PoolPktsout_Type()
)
poolPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsout.setStatus("mandatory")
_PoolPktsinHi32_Type = Counter32
_PoolPktsinHi32_Object = MibTableColumn
poolPktsinHi32 = _PoolPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 11),
    _PoolPktsinHi32_Type()
)
poolPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsinHi32.setStatus("mandatory")
_PoolPktsoutHi32_Type = Counter32
_PoolPktsoutHi32_Object = MibTableColumn
poolPktsoutHi32 = _PoolPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 12),
    _PoolPktsoutHi32_Type()
)
poolPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPktsoutHi32.setStatus("mandatory")


class _PoolMaxConn_Type(Integer32):
    """Custom type poolMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMaxConn_Type.__name__ = "Integer32"
_PoolMaxConn_Object = MibTableColumn
poolMaxConn = _PoolMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 13),
    _PoolMaxConn_Type()
)
poolMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMaxConn.setStatus("mandatory")


class _PoolCurrentConn_Type(Integer32):
    """Custom type poolCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolCurrentConn_Type.__name__ = "Integer32"
_PoolCurrentConn_Object = MibTableColumn
poolCurrentConn = _PoolCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 14),
    _PoolCurrentConn_Type()
)
poolCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCurrentConn.setStatus("mandatory")
_PoolTotalConn_Type = Counter32
_PoolTotalConn_Object = MibTableColumn
poolTotalConn = _PoolTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 15),
    _PoolTotalConn_Type()
)
poolTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolTotalConn.setStatus("mandatory")


class _PoolPersistMode_Type(Integer32):
    """Custom type poolPersistMode based on Integer32"""
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
        *(("cookie", 4),
          ("none", 1),
          ("simple", 2),
          ("ssl", 5),
          ("sticky", 3))
    )


_PoolPersistMode_Type.__name__ = "Integer32"
_PoolPersistMode_Object = MibTableColumn
poolPersistMode = _PoolPersistMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 16),
    _PoolPersistMode_Type()
)
poolPersistMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPersistMode.setStatus("mandatory")
_PoolSSLTimeout_Type = Integer32
_PoolSSLTimeout_Object = MibTableColumn
poolSSLTimeout = _PoolSSLTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 17),
    _PoolSSLTimeout_Type()
)
poolSSLTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSSLTimeout.setStatus("mandatory")
_PoolSimpleTimeout_Type = Integer32
_PoolSimpleTimeout_Object = MibTableColumn
poolSimpleTimeout = _PoolSimpleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 18),
    _PoolSimpleTimeout_Type()
)
poolSimpleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSimpleTimeout.setStatus("mandatory")
_PoolSimpleMask_Type = IpAddress
_PoolSimpleMask_Object = MibTableColumn
poolSimpleMask = _PoolSimpleMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 19),
    _PoolSimpleMask_Type()
)
poolSimpleMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolSimpleMask.setStatus("mandatory")
_PoolStickyMask_Type = IpAddress
_PoolStickyMask_Object = MibTableColumn
poolStickyMask = _PoolStickyMask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 20),
    _PoolStickyMask_Type()
)
poolStickyMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolStickyMask.setStatus("mandatory")


class _PoolCookieMode_Type(Integer32):
    """Custom type poolCookieMode based on Integer32"""
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
        *(("hash", 5),
          ("insert", 2),
          ("passive", 4),
          ("rewrite", 3),
          ("unspecified", 1))
    )


_PoolCookieMode_Type.__name__ = "Integer32"
_PoolCookieMode_Object = MibTableColumn
poolCookieMode = _PoolCookieMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 21),
    _PoolCookieMode_Type()
)
poolCookieMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCookieMode.setStatus("mandatory")
_PoolCookieExpiration_Type = Integer32
_PoolCookieExpiration_Object = MibTableColumn
poolCookieExpiration = _PoolCookieExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 22),
    _PoolCookieExpiration_Type()
)
poolCookieExpiration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCookieExpiration.setStatus("mandatory")


class _PoolCookieHashName_Type(DisplayString):
    """Custom type poolCookieHashName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolCookieHashName_Type.__name__ = "DisplayString"
_PoolCookieHashName_Object = MibTableColumn
poolCookieHashName = _PoolCookieHashName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 23),
    _PoolCookieHashName_Type()
)
poolCookieHashName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCookieHashName.setStatus("mandatory")
_PoolCookieHashOffset_Type = Integer32
_PoolCookieHashOffset_Object = MibTableColumn
poolCookieHashOffset = _PoolCookieHashOffset_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 24),
    _PoolCookieHashOffset_Type()
)
poolCookieHashOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCookieHashOffset.setStatus("mandatory")
_PoolCookieHashLength_Type = Integer32
_PoolCookieHashLength_Object = MibTableColumn
poolCookieHashLength = _PoolCookieHashLength_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 25),
    _PoolCookieHashLength_Type()
)
poolCookieHashLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolCookieHashLength.setStatus("mandatory")
_PoolMinActiveMembers_Type = Integer32
_PoolMinActiveMembers_Object = MibTableColumn
poolMinActiveMembers = _PoolMinActiveMembers_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 26),
    _PoolMinActiveMembers_Type()
)
poolMinActiveMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMinActiveMembers.setStatus("mandatory")
_PoolActiveMemberCount_Type = Integer32
_PoolActiveMemberCount_Object = MibTableColumn
poolActiveMemberCount = _PoolActiveMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 27),
    _PoolActiveMemberCount_Type()
)
poolActiveMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolActiveMemberCount.setStatus("mandatory")


class _PoolPersistMirror_Type(Integer32):
    """Custom type poolPersistMirror based on Integer32"""
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


_PoolPersistMirror_Type.__name__ = "Integer32"
_PoolPersistMirror_Object = MibTableColumn
poolPersistMirror = _PoolPersistMirror_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 28),
    _PoolPersistMirror_Type()
)
poolPersistMirror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolPersistMirror.setStatus("mandatory")


class _PoolFallbackHost_Type(DisplayString):
    """Custom type poolFallbackHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolFallbackHost_Type.__name__ = "DisplayString"
_PoolFallbackHost_Object = MibTableColumn
poolFallbackHost = _PoolFallbackHost_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 7, 2, 1, 29),
    _PoolFallbackHost_Type()
)
poolFallbackHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolFallbackHost.setStatus("mandatory")
_PoolMember_ObjectIdentity = ObjectIdentity
poolMember = _PoolMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8)
)


class _PoolMemberNumber_Type(Integer32):
    """Custom type poolMemberNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberNumber_Type.__name__ = "Integer32"
_PoolMemberNumber_Object = MibScalar
poolMemberNumber = _PoolMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 1),
    _PoolMemberNumber_Type()
)
poolMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberNumber.setStatus("mandatory")
_PoolMemberTable_Object = MibTable
poolMemberTable = _PoolMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    poolMemberTable.setStatus("mandatory")
_PoolMemberEntry_Object = MibTableRow
poolMemberEntry = _PoolMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1)
)
poolMemberEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberPoolName"),
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "poolMemberPort"),
)
if mibBuilder.loadTexts:
    poolMemberEntry.setStatus("mandatory")


class _PoolMemberPoolName_Type(DisplayString):
    """Custom type poolMemberPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PoolMemberPoolName_Type.__name__ = "DisplayString"
_PoolMemberPoolName_Object = MibTableColumn
poolMemberPoolName = _PoolMemberPoolName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 1),
    _PoolMemberPoolName_Type()
)
poolMemberPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPoolName.setStatus("mandatory")
_PoolMemberIpAddress_Type = IpAddress
_PoolMemberIpAddress_Object = MibTableColumn
poolMemberIpAddress = _PoolMemberIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 2),
    _PoolMemberIpAddress_Type()
)
poolMemberIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberIpAddress.setStatus("mandatory")


class _PoolMemberPort_Type(Integer32):
    """Custom type poolMemberPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberPort_Type.__name__ = "Integer32"
_PoolMemberPort_Object = MibTableColumn
poolMemberPort = _PoolMemberPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 3),
    _PoolMemberPort_Type()
)
poolMemberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPort.setStatus("mandatory")


class _PoolMemberMaintenance_Type(Integer32):
    """Custom type poolMemberMaintenance based on Integer32"""
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


_PoolMemberMaintenance_Type.__name__ = "Integer32"
_PoolMemberMaintenance_Object = MibTableColumn
poolMemberMaintenance = _PoolMemberMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 4),
    _PoolMemberMaintenance_Type()
)
poolMemberMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberMaintenance.setStatus("mandatory")
_PoolMemberRatio_Type = Integer32
_PoolMemberRatio_Object = MibTableColumn
poolMemberRatio = _PoolMemberRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 5),
    _PoolMemberRatio_Type()
)
poolMemberRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberRatio.setStatus("mandatory")
_PoolMemberPriority_Type = Integer32
_PoolMemberPriority_Object = MibTableColumn
poolMemberPriority = _PoolMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 6),
    _PoolMemberPriority_Type()
)
poolMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPriority.setStatus("mandatory")
_PoolMemberWeight_Type = Integer32
_PoolMemberWeight_Object = MibTableColumn
poolMemberWeight = _PoolMemberWeight_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 7),
    _PoolMemberWeight_Type()
)
poolMemberWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberWeight.setStatus("mandatory")
_PoolMemberRipeness_Type = Integer32
_PoolMemberRipeness_Object = MibTableColumn
poolMemberRipeness = _PoolMemberRipeness_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 8),
    _PoolMemberRipeness_Type()
)
poolMemberRipeness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberRipeness.setStatus("mandatory")
_PoolMemberBitsin_Type = Counter32
_PoolMemberBitsin_Object = MibTableColumn
poolMemberBitsin = _PoolMemberBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 9),
    _PoolMemberBitsin_Type()
)
poolMemberBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsin.setStatus("mandatory")
_PoolMemberBitsout_Type = Counter32
_PoolMemberBitsout_Object = MibTableColumn
poolMemberBitsout = _PoolMemberBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 10),
    _PoolMemberBitsout_Type()
)
poolMemberBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsout.setStatus("mandatory")
_PoolMemberBitsinHi32_Type = Counter32
_PoolMemberBitsinHi32_Object = MibTableColumn
poolMemberBitsinHi32 = _PoolMemberBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 11),
    _PoolMemberBitsinHi32_Type()
)
poolMemberBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsinHi32.setStatus("mandatory")
_PoolMemberBitsoutHi32_Type = Counter32
_PoolMemberBitsoutHi32_Object = MibTableColumn
poolMemberBitsoutHi32 = _PoolMemberBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 12),
    _PoolMemberBitsoutHi32_Type()
)
poolMemberBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberBitsoutHi32.setStatus("mandatory")
_PoolMemberPktsin_Type = Counter32
_PoolMemberPktsin_Object = MibTableColumn
poolMemberPktsin = _PoolMemberPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 13),
    _PoolMemberPktsin_Type()
)
poolMemberPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsin.setStatus("mandatory")
_PoolMemberPktsout_Type = Counter32
_PoolMemberPktsout_Object = MibTableColumn
poolMemberPktsout = _PoolMemberPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 14),
    _PoolMemberPktsout_Type()
)
poolMemberPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsout.setStatus("mandatory")
_PoolMemberPktsinHi32_Type = Counter32
_PoolMemberPktsinHi32_Object = MibTableColumn
poolMemberPktsinHi32 = _PoolMemberPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 15),
    _PoolMemberPktsinHi32_Type()
)
poolMemberPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsinHi32.setStatus("mandatory")
_PoolMemberPktsoutHi32_Type = Counter32
_PoolMemberPktsoutHi32_Object = MibTableColumn
poolMemberPktsoutHi32 = _PoolMemberPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 16),
    _PoolMemberPktsoutHi32_Type()
)
poolMemberPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberPktsoutHi32.setStatus("mandatory")


class _PoolMemberConnLimit_Type(Integer32):
    """Custom type poolMemberConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberConnLimit_Type.__name__ = "Integer32"
_PoolMemberConnLimit_Object = MibTableColumn
poolMemberConnLimit = _PoolMemberConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 17),
    _PoolMemberConnLimit_Type()
)
poolMemberConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberConnLimit.setStatus("mandatory")


class _PoolMemberMaxConn_Type(Integer32):
    """Custom type poolMemberMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberMaxConn_Type.__name__ = "Integer32"
_PoolMemberMaxConn_Object = MibTableColumn
poolMemberMaxConn = _PoolMemberMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 18),
    _PoolMemberMaxConn_Type()
)
poolMemberMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberMaxConn.setStatus("mandatory")


class _PoolMemberCurrentConn_Type(Integer32):
    """Custom type poolMemberCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PoolMemberCurrentConn_Type.__name__ = "Integer32"
_PoolMemberCurrentConn_Object = MibTableColumn
poolMemberCurrentConn = _PoolMemberCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 19),
    _PoolMemberCurrentConn_Type()
)
poolMemberCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberCurrentConn.setStatus("mandatory")
_PoolMemberTotalConn_Type = Counter32
_PoolMemberTotalConn_Object = MibTableColumn
poolMemberTotalConn = _PoolMemberTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 20),
    _PoolMemberTotalConn_Type()
)
poolMemberTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberTotalConn.setStatus("mandatory")
_PoolMemberStatus_Type = BigAPIStatus
_PoolMemberStatus_Object = MibTableColumn
poolMemberStatus = _PoolMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 21),
    _PoolMemberStatus_Type()
)
poolMemberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberStatus.setStatus("mandatory")
_PoolMemberIpStatus_Type = BigAPIStatus
_PoolMemberIpStatus_Object = MibScalar
poolMemberIpStatus = _PoolMemberIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 8, 2, 1, 22),
    _PoolMemberIpStatus_Type()
)
poolMemberIpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    poolMemberIpStatus.setStatus("mandatory")
_SslProxy_ObjectIdentity = ObjectIdentity
sslProxy = _SslProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9)
)


class _SslProxyNumber_Type(Integer32):
    """Custom type sslProxyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyNumber_Type.__name__ = "Integer32"
_SslProxyNumber_Object = MibScalar
sslProxyNumber = _SslProxyNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 1),
    _SslProxyNumber_Type()
)
sslProxyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyNumber.setStatus("mandatory")
_SslProxyTable_Object = MibTable
sslProxyTable = _SslProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2)
)
if mibBuilder.loadTexts:
    sslProxyTable.setStatus("mandatory")
_SslProxyEntry_Object = MibTableRow
sslProxyEntry = _SslProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1)
)
sslProxyEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "sslProxyOrigIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "sslProxyOrigPort"),
    (0, "LOAD-BAL-SYSTEM-MIB", "sslProxyDestIpAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "sslProxyDestPort"),
)
if mibBuilder.loadTexts:
    sslProxyEntry.setStatus("mandatory")
_SslProxyOrigIpAddress_Type = IpAddress
_SslProxyOrigIpAddress_Object = MibTableColumn
sslProxyOrigIpAddress = _SslProxyOrigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 1),
    _SslProxyOrigIpAddress_Type()
)
sslProxyOrigIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyOrigIpAddress.setStatus("mandatory")


class _SslProxyOrigPort_Type(Integer32):
    """Custom type sslProxyOrigPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyOrigPort_Type.__name__ = "Integer32"
_SslProxyOrigPort_Object = MibTableColumn
sslProxyOrigPort = _SslProxyOrigPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 2),
    _SslProxyOrigPort_Type()
)
sslProxyOrigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyOrigPort.setStatus("mandatory")
_SslProxyDestIpAddress_Type = IpAddress
_SslProxyDestIpAddress_Object = MibTableColumn
sslProxyDestIpAddress = _SslProxyDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 3),
    _SslProxyDestIpAddress_Type()
)
sslProxyDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyDestIpAddress.setStatus("mandatory")


class _SslProxyDestPort_Type(Integer32):
    """Custom type sslProxyDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyDestPort_Type.__name__ = "Integer32"
_SslProxyDestPort_Object = MibTableColumn
sslProxyDestPort = _SslProxyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 4),
    _SslProxyDestPort_Type()
)
sslProxyDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyDestPort.setStatus("mandatory")
_SslProxyNetmask_Type = IpAddress
_SslProxyNetmask_Object = MibTableColumn
sslProxyNetmask = _SslProxyNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 5),
    _SslProxyNetmask_Type()
)
sslProxyNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyNetmask.setStatus("mandatory")
_SslProxyBroadcast_Type = IpAddress
_SslProxyBroadcast_Object = MibTableColumn
sslProxyBroadcast = _SslProxyBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 6),
    _SslProxyBroadcast_Type()
)
sslProxyBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBroadcast.setStatus("mandatory")


class _SslProxyUnitId_Type(Integer32):
    """Custom type sslProxyUnitId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyUnitId_Type.__name__ = "Integer32"
_SslProxyUnitId_Object = MibTableColumn
sslProxyUnitId = _SslProxyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 7),
    _SslProxyUnitId_Type()
)
sslProxyUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyUnitId.setStatus("mandatory")


class _SslProxyEnabled_Type(Integer32):
    """Custom type sslProxyEnabled based on Integer32"""
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


_SslProxyEnabled_Type.__name__ = "Integer32"
_SslProxyEnabled_Object = MibTableColumn
sslProxyEnabled = _SslProxyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 8),
    _SslProxyEnabled_Type()
)
sslProxyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyEnabled.setStatus("mandatory")


class _SslProxyInterfaceName_Type(DisplayString):
    """Custom type sslProxyInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SslProxyInterfaceName_Type.__name__ = "DisplayString"
_SslProxyInterfaceName_Object = MibTableColumn
sslProxyInterfaceName = _SslProxyInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 9),
    _SslProxyInterfaceName_Type()
)
sslProxyInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyInterfaceName.setStatus("deprecated")


class _SslProxyLastHopPool_Type(DisplayString):
    """Custom type sslProxyLastHopPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SslProxyLastHopPool_Type.__name__ = "DisplayString"
_SslProxyLastHopPool_Object = MibTableColumn
sslProxyLastHopPool = _SslProxyLastHopPool_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 10),
    _SslProxyLastHopPool_Type()
)
sslProxyLastHopPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyLastHopPool.setStatus("mandatory")


class _SslProxyVLANs_Type(DisplayString):
    """Custom type sslProxyVLANs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SslProxyVLANs_Type.__name__ = "DisplayString"
_SslProxyVLANs_Object = MibTableColumn
sslProxyVLANs = _SslProxyVLANs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 11),
    _SslProxyVLANs_Type()
)
sslProxyVLANs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyVLANs.setStatus("mandatory")


class _SslProxyLocalTarget_Type(Integer32):
    """Custom type sslProxyLocalTarget based on Integer32"""
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


_SslProxyLocalTarget_Type.__name__ = "Integer32"
_SslProxyLocalTarget_Object = MibTableColumn
sslProxyLocalTarget = _SslProxyLocalTarget_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 12),
    _SslProxyLocalTarget_Type()
)
sslProxyLocalTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyLocalTarget.setStatus("mandatory")


class _SslProxyAkamaize_Type(Integer32):
    """Custom type sslProxyAkamaize based on Integer32"""
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


_SslProxyAkamaize_Type.__name__ = "Integer32"
_SslProxyAkamaize_Object = MibTableColumn
sslProxyAkamaize = _SslProxyAkamaize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 13),
    _SslProxyAkamaize_Type()
)
sslProxyAkamaize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyAkamaize.setStatus("mandatory")


class _SslProxyUseSSL_Type(Integer32):
    """Custom type sslProxyUseSSL based on Integer32"""
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


_SslProxyUseSSL_Type.__name__ = "Integer32"
_SslProxyUseSSL_Object = MibTableColumn
sslProxyUseSSL = _SslProxyUseSSL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 14),
    _SslProxyUseSSL_Type()
)
sslProxyUseSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyUseSSL.setStatus("mandatory")
_SslProxyBitsin_Type = Counter32
_SslProxyBitsin_Object = MibTableColumn
sslProxyBitsin = _SslProxyBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 15),
    _SslProxyBitsin_Type()
)
sslProxyBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBitsin.setStatus("mandatory")
_SslProxyBitsout_Type = Counter32
_SslProxyBitsout_Object = MibTableColumn
sslProxyBitsout = _SslProxyBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 16),
    _SslProxyBitsout_Type()
)
sslProxyBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBitsout.setStatus("mandatory")
_SslProxyBitsinHi32_Type = Counter32
_SslProxyBitsinHi32_Object = MibTableColumn
sslProxyBitsinHi32 = _SslProxyBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 17),
    _SslProxyBitsinHi32_Type()
)
sslProxyBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBitsinHi32.setStatus("mandatory")
_SslProxyBitsoutHi32_Type = Counter32
_SslProxyBitsoutHi32_Object = MibTableColumn
sslProxyBitsoutHi32 = _SslProxyBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 18),
    _SslProxyBitsoutHi32_Type()
)
sslProxyBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyBitsoutHi32.setStatus("mandatory")
_SslProxyPktsin_Type = Counter32
_SslProxyPktsin_Object = MibTableColumn
sslProxyPktsin = _SslProxyPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 19),
    _SslProxyPktsin_Type()
)
sslProxyPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyPktsin.setStatus("mandatory")
_SslProxyPktsout_Type = Counter32
_SslProxyPktsout_Object = MibTableColumn
sslProxyPktsout = _SslProxyPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 20),
    _SslProxyPktsout_Type()
)
sslProxyPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyPktsout.setStatus("mandatory")
_SslProxyPktsinHi32_Type = Counter32
_SslProxyPktsinHi32_Object = MibTableColumn
sslProxyPktsinHi32 = _SslProxyPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 21),
    _SslProxyPktsinHi32_Type()
)
sslProxyPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyPktsinHi32.setStatus("mandatory")
_SslProxyPktsoutHi32_Type = Counter32
_SslProxyPktsoutHi32_Object = MibTableColumn
sslProxyPktsoutHi32 = _SslProxyPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 22),
    _SslProxyPktsoutHi32_Type()
)
sslProxyPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyPktsoutHi32.setStatus("mandatory")


class _SslProxyConnLimit_Type(Integer32):
    """Custom type sslProxyConnLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyConnLimit_Type.__name__ = "Integer32"
_SslProxyConnLimit_Object = MibTableColumn
sslProxyConnLimit = _SslProxyConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 23),
    _SslProxyConnLimit_Type()
)
sslProxyConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyConnLimit.setStatus("mandatory")


class _SslProxyMaxConn_Type(Integer32):
    """Custom type sslProxyMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyMaxConn_Type.__name__ = "Integer32"
_SslProxyMaxConn_Object = MibTableColumn
sslProxyMaxConn = _SslProxyMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 24),
    _SslProxyMaxConn_Type()
)
sslProxyMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyMaxConn.setStatus("mandatory")


class _SslProxyCurrentConn_Type(Integer32):
    """Custom type sslProxyCurrentConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SslProxyCurrentConn_Type.__name__ = "Integer32"
_SslProxyCurrentConn_Object = MibTableColumn
sslProxyCurrentConn = _SslProxyCurrentConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 25),
    _SslProxyCurrentConn_Type()
)
sslProxyCurrentConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCurrentConn.setStatus("mandatory")
_SslProxyTotalConn_Type = Counter32
_SslProxyTotalConn_Object = MibTableColumn
sslProxyTotalConn = _SslProxyTotalConn_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 26),
    _SslProxyTotalConn_Type()
)
sslProxyTotalConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyTotalConn.setStatus("mandatory")


class _SslProxyUseServerSSL_Type(Integer32):
    """Custom type sslProxyUseServerSSL based on Integer32"""
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


_SslProxyUseServerSSL_Type.__name__ = "Integer32"
_SslProxyUseServerSSL_Object = MibTableColumn
sslProxyUseServerSSL = _SslProxyUseServerSSL_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 27),
    _SslProxyUseServerSSL_Type()
)
sslProxyUseServerSSL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyUseServerSSL.setStatus("mandatory")


class _SslProxyArpEnabled_Type(Integer32):
    """Custom type sslProxyArpEnabled based on Integer32"""
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


_SslProxyArpEnabled_Type.__name__ = "Integer32"
_SslProxyArpEnabled_Object = MibTableColumn
sslProxyArpEnabled = _SslProxyArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 28),
    _SslProxyArpEnabled_Type()
)
sslProxyArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyArpEnabled.setStatus("mandatory")


class _SslProxyHTTPHeaderToAdd_Type(DisplayString):
    """Custom type sslProxyHTTPHeaderToAdd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SslProxyHTTPHeaderToAdd_Type.__name__ = "DisplayString"
_SslProxyHTTPHeaderToAdd_Object = MibTableColumn
sslProxyHTTPHeaderToAdd = _SslProxyHTTPHeaderToAdd_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 29),
    _SslProxyHTTPHeaderToAdd_Type()
)
sslProxyHTTPHeaderToAdd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyHTTPHeaderToAdd.setStatus("mandatory")


class _SslProxyInsertClientCipher_Type(Integer32):
    """Custom type sslProxyInsertClientCipher based on Integer32"""
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


_SslProxyInsertClientCipher_Type.__name__ = "Integer32"
_SslProxyInsertClientCipher_Object = MibTableColumn
sslProxyInsertClientCipher = _SslProxyInsertClientCipher_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 30),
    _SslProxyInsertClientCipher_Type()
)
sslProxyInsertClientCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyInsertClientCipher.setStatus("mandatory")
_SslProxyRewriteRedirects_Type = Integer32
_SslProxyRewriteRedirects_Object = MibTableColumn
sslProxyRewriteRedirects = _SslProxyRewriteRedirects_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 31),
    _SslProxyRewriteRedirects_Type()
)
sslProxyRewriteRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyRewriteRedirects.setStatus("mandatory")
_SslProxyClientInvalidVersions_Type = Counter32
_SslProxyClientInvalidVersions_Object = MibTableColumn
sslProxyClientInvalidVersions = _SslProxyClientInvalidVersions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 32),
    _SslProxyClientInvalidVersions_Type()
)
sslProxyClientInvalidVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyClientInvalidVersions.setStatus("mandatory")
_SslProxyServerInvalidVersions_Type = Counter32
_SslProxyServerInvalidVersions_Object = MibTableColumn
sslProxyServerInvalidVersions = _SslProxyServerInvalidVersions_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 33),
    _SslProxyServerInvalidVersions_Type()
)
sslProxyServerInvalidVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerInvalidVersions.setStatus("mandatory")


class _SslProxyClientCertificate_Type(Integer32):
    """Custom type sslProxyClientCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clientcertificateignored", 1),
          ("clientcertificaterequested", 2),
          ("clientcertificaterequired", 3))
    )


_SslProxyClientCertificate_Type.__name__ = "Integer32"
_SslProxyClientCertificate_Object = MibTableColumn
sslProxyClientCertificate = _SslProxyClientCertificate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 34),
    _SslProxyClientCertificate_Type()
)
sslProxyClientCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyClientCertificate.setStatus("mandatory")


class _SslProxyVerifyClientOnce_Type(Integer32):
    """Custom type sslProxyVerifyClientOnce based on Integer32"""
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


_SslProxyVerifyClientOnce_Type.__name__ = "Integer32"
_SslProxyVerifyClientOnce_Object = MibTableColumn
sslProxyVerifyClientOnce = _SslProxyVerifyClientOnce_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 35),
    _SslProxyVerifyClientOnce_Type()
)
sslProxyVerifyClientOnce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyVerifyClientOnce.setStatus("mandatory")


class _SslProxyVerifyClientDepth_Type(Integer32):
    """Custom type sslProxyVerifyClientDepth based on Integer32"""
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


_SslProxyVerifyClientDepth_Type.__name__ = "Integer32"
_SslProxyVerifyClientDepth_Object = MibTableColumn
sslProxyVerifyClientDepth = _SslProxyVerifyClientDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 36),
    _SslProxyVerifyClientDepth_Type()
)
sslProxyVerifyClientDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyVerifyClientDepth.setStatus("mandatory")
_SslProxyClientSessionCacheTimeout_Type = Integer32
_SslProxyClientSessionCacheTimeout_Object = MibTableColumn
sslProxyClientSessionCacheTimeout = _SslProxyClientSessionCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 37),
    _SslProxyClientSessionCacheTimeout_Type()
)
sslProxyClientSessionCacheTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyClientSessionCacheTimeout.setStatus("mandatory")
_SslProxyClientSessionCacheSize_Type = Integer32
_SslProxyClientSessionCacheSize_Object = MibTableColumn
sslProxyClientSessionCacheSize = _SslProxyClientSessionCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 38),
    _SslProxyClientSessionCacheSize_Type()
)
sslProxyClientSessionCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyClientSessionCacheSize.setStatus("mandatory")


class _SslProxyChainFileName_Type(DisplayString):
    """Custom type sslProxyChainFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyChainFileName_Type.__name__ = "DisplayString"
_SslProxyChainFileName_Object = MibTableColumn
sslProxyChainFileName = _SslProxyChainFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 39),
    _SslProxyChainFileName_Type()
)
sslProxyChainFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyChainFileName.setStatus("mandatory")


class _SslProxyServerChainFileName_Type(DisplayString):
    """Custom type sslProxyServerChainFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyServerChainFileName_Type.__name__ = "DisplayString"
_SslProxyServerChainFileName_Object = MibTableColumn
sslProxyServerChainFileName = _SslProxyServerChainFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 40),
    _SslProxyServerChainFileName_Type()
)
sslProxyServerChainFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerChainFileName.setStatus("mandatory")


class _SslProxyCAFileFileName_Type(DisplayString):
    """Custom type sslProxyCAFileFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyCAFileFileName_Type.__name__ = "DisplayString"
_SslProxyCAFileFileName_Object = MibTableColumn
sslProxyCAFileFileName = _SslProxyCAFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 41),
    _SslProxyCAFileFileName_Type()
)
sslProxyCAFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCAFileFileName.setStatus("mandatory")


class _SslProxyServerCAFileFileName_Type(DisplayString):
    """Custom type sslProxyServerCAFileFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyServerCAFileFileName_Type.__name__ = "DisplayString"
_SslProxyServerCAFileFileName_Object = MibTableColumn
sslProxyServerCAFileFileName = _SslProxyServerCAFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 42),
    _SslProxyServerCAFileFileName_Type()
)
sslProxyServerCAFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerCAFileFileName.setStatus("mandatory")


class _SslProxyCAPathFileName_Type(DisplayString):
    """Custom type sslProxyCAPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyCAPathFileName_Type.__name__ = "DisplayString"
_SslProxyCAPathFileName_Object = MibTableColumn
sslProxyCAPathFileName = _SslProxyCAPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 43),
    _SslProxyCAPathFileName_Type()
)
sslProxyCAPathFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCAPathFileName.setStatus("mandatory")


class _SslProxyServerCAPathFileName_Type(DisplayString):
    """Custom type sslProxyServerCAPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyServerCAPathFileName_Type.__name__ = "DisplayString"
_SslProxyServerCAPathFileName_Object = MibTableColumn
sslProxyServerCAPathFileName = _SslProxyServerCAPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 44),
    _SslProxyServerCAPathFileName_Type()
)
sslProxyServerCAPathFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerCAPathFileName.setStatus("mandatory")


class _SslProxyCRLFileFileName_Type(DisplayString):
    """Custom type sslProxyCRLFileFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyCRLFileFileName_Type.__name__ = "DisplayString"
_SslProxyCRLFileFileName_Object = MibTableColumn
sslProxyCRLFileFileName = _SslProxyCRLFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 45),
    _SslProxyCRLFileFileName_Type()
)
sslProxyCRLFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCRLFileFileName.setStatus("mandatory")


class _SslProxyServerCRLFileFileName_Type(DisplayString):
    """Custom type sslProxyServerCRLFileFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyServerCRLFileFileName_Type.__name__ = "DisplayString"
_SslProxyServerCRLFileFileName_Object = MibTableColumn
sslProxyServerCRLFileFileName = _SslProxyServerCRLFileFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 46),
    _SslProxyServerCRLFileFileName_Type()
)
sslProxyServerCRLFileFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerCRLFileFileName.setStatus("mandatory")


class _SslProxyCRLPathFileName_Type(DisplayString):
    """Custom type sslProxyCRLPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyCRLPathFileName_Type.__name__ = "DisplayString"
_SslProxyCRLPathFileName_Object = MibTableColumn
sslProxyCRLPathFileName = _SslProxyCRLPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 47),
    _SslProxyCRLPathFileName_Type()
)
sslProxyCRLPathFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyCRLPathFileName.setStatus("mandatory")


class _SslProxyServerCRLPathFileName_Type(DisplayString):
    """Custom type sslProxyServerCRLPathFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyServerCRLPathFileName_Type.__name__ = "DisplayString"
_SslProxyServerCRLPathFileName_Object = MibTableColumn
sslProxyServerCRLPathFileName = _SslProxyServerCRLPathFileName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 48),
    _SslProxyServerCRLPathFileName_Type()
)
sslProxyServerCRLPathFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerCRLPathFileName.setStatus("mandatory")


class _SslProxyClientCertCAFileFilenName_Type(DisplayString):
    """Custom type sslProxyClientCertCAFileFilenName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_SslProxyClientCertCAFileFilenName_Type.__name__ = "DisplayString"
_SslProxyClientCertCAFileFilenName_Object = MibScalar
sslProxyClientCertCAFileFilenName = _SslProxyClientCertCAFileFilenName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 49),
    _SslProxyClientCertCAFileFilenName_Type()
)
sslProxyClientCertCAFileFilenName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyClientCertCAFileFilenName.setStatus("mandatory")
_SslProxyInsertClientSessionID_Type = Integer32
_SslProxyInsertClientSessionID_Object = MibTableColumn
sslProxyInsertClientSessionID = _SslProxyInsertClientSessionID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 50),
    _SslProxyInsertClientSessionID_Type()
)
sslProxyInsertClientSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyInsertClientSessionID.setStatus("mandatory")
_SslProxyInsertClientIPAddrPort_Type = Integer32
_SslProxyInsertClientIPAddrPort_Object = MibTableColumn
sslProxyInsertClientIPAddrPort = _SslProxyInsertClientIPAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 51),
    _SslProxyInsertClientIPAddrPort_Type()
)
sslProxyInsertClientIPAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyInsertClientIPAddrPort.setStatus("mandatory")


class _SslProxyServerCertificate_Type(Integer32):
    """Custom type sslProxyServerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("serverCertificateIgnored", 1),
          ("serverCertificateRequired", 3))
    )


_SslProxyServerCertificate_Type.__name__ = "Integer32"
_SslProxyServerCertificate_Object = MibTableColumn
sslProxyServerCertificate = _SslProxyServerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 52),
    _SslProxyServerCertificate_Type()
)
sslProxyServerCertificate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerCertificate.setStatus("mandatory")
_SslProxyVerifyServerDepth_Type = Integer32
_SslProxyVerifyServerDepth_Object = MibTableColumn
sslProxyVerifyServerDepth = _SslProxyVerifyServerDepth_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 53),
    _SslProxyVerifyServerDepth_Type()
)
sslProxyVerifyServerDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyVerifyServerDepth.setStatus("mandatory")


class _SslProxyTCPKeepAlivesEnabled_Type(Integer32):
    """Custom type sslProxyTCPKeepAlivesEnabled based on Integer32"""
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


_SslProxyTCPKeepAlivesEnabled_Type.__name__ = "Integer32"
_SslProxyTCPKeepAlivesEnabled_Object = MibTableColumn
sslProxyTCPKeepAlivesEnabled = _SslProxyTCPKeepAlivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 54),
    _SslProxyTCPKeepAlivesEnabled_Type()
)
sslProxyTCPKeepAlivesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyTCPKeepAlivesEnabled.setStatus("mandatory")


class _SslProxyServerTCPKeepAlivesEnabled_Type(Integer32):
    """Custom type sslProxyServerTCPKeepAlivesEnabled based on Integer32"""
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


_SslProxyServerTCPKeepAlivesEnabled_Type.__name__ = "Integer32"
_SslProxyServerTCPKeepAlivesEnabled_Object = MibTableColumn
sslProxyServerTCPKeepAlivesEnabled = _SslProxyServerTCPKeepAlivesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 9, 2, 1, 55),
    _SslProxyServerTCPKeepAlivesEnabled_Type()
)
sslProxyServerTCPKeepAlivesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslProxyServerTCPKeepAlivesEnabled.setStatus("mandatory")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10)
)


class _VlanNumber_Type(Integer32):
    """Custom type vlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanNumber_Type.__name__ = "Integer32"
_VlanNumber_Object = MibScalar
vlanNumber = _VlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 1),
    _VlanNumber_Type()
)
vlanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNumber.setStatus("mandatory")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("mandatory")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "vlanName"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("mandatory")


class _VlanName_Type(DisplayString):
    """Custom type vlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanName_Type.__name__ = "DisplayString"
_VlanName_Object = MibTableColumn
vlanName = _VlanName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 1),
    _VlanName_Type()
)
vlanName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanName.setStatus("mandatory")
_VlanID_Type = Integer32
_VlanID_Object = MibTableColumn
vlanID = _VlanID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 2),
    _VlanID_Type()
)
vlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanID.setStatus("mandatory")
_VlanTag_Type = Integer32
_VlanTag_Object = MibTableColumn
vlanTag = _VlanTag_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 3),
    _VlanTag_Type()
)
vlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTag.setStatus("mandatory")


class _VlanAllowOtherProxyARP_Type(Integer32):
    """Custom type vlanAllowOtherProxyARP based on Integer32"""
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


_VlanAllowOtherProxyARP_Type.__name__ = "Integer32"
_VlanAllowOtherProxyARP_Object = MibTableColumn
vlanAllowOtherProxyARP = _VlanAllowOtherProxyARP_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 4),
    _VlanAllowOtherProxyARP_Type()
)
vlanAllowOtherProxyARP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAllowOtherProxyARP.setStatus("mandatory")


class _VlanPortLockedDown_Type(Integer32):
    """Custom type vlanPortLockedDown based on Integer32"""
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


_VlanPortLockedDown_Type.__name__ = "Integer32"
_VlanPortLockedDown_Object = MibTableColumn
vlanPortLockedDown = _VlanPortLockedDown_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 5),
    _VlanPortLockedDown_Type()
)
vlanPortLockedDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortLockedDown.setStatus("mandatory")


class _VlanTaggedPorts_Type(DisplayString):
    """Custom type vlanTaggedPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanTaggedPorts_Type.__name__ = "DisplayString"
_VlanTaggedPorts_Object = MibTableColumn
vlanTaggedPorts = _VlanTaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 6),
    _VlanTaggedPorts_Type()
)
vlanTaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTaggedPorts.setStatus("mandatory")


class _VlanUntaggedPorts_Type(DisplayString):
    """Custom type vlanUntaggedPorts based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VlanUntaggedPorts_Type.__name__ = "DisplayString"
_VlanUntaggedPorts_Object = MibTableColumn
vlanUntaggedPorts = _VlanUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 7),
    _VlanUntaggedPorts_Type()
)
vlanUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanUntaggedPorts.setStatus("mandatory")


class _VlanSnatAutomap_Type(Integer32):
    """Custom type vlanSnatAutomap based on Integer32"""
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


_VlanSnatAutomap_Type.__name__ = "Integer32"
_VlanSnatAutomap_Object = MibTableColumn
vlanSnatAutomap = _VlanSnatAutomap_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 8),
    _VlanSnatAutomap_Type()
)
vlanSnatAutomap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSnatAutomap.setStatus("mandatory")


class _VlanArmed_Type(Integer32):
    """Custom type vlanArmed based on Integer32"""
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


_VlanArmed_Type.__name__ = "Integer32"
_VlanArmed_Object = MibTableColumn
vlanArmed = _VlanArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 9),
    _VlanArmed_Type()
)
vlanArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanArmed.setStatus("mandatory")
_VlanTimeout_Type = Integer32
_VlanTimeout_Object = MibTableColumn
vlanTimeout = _VlanTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 10, 2, 1, 10),
    _VlanTimeout_Type()
)
vlanTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTimeout.setStatus("mandatory")
_SelfIP_ObjectIdentity = ObjectIdentity
selfIP = _SelfIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11)
)


class _SelfIPNumber_Type(Integer32):
    """Custom type selfIPNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SelfIPNumber_Type.__name__ = "Integer32"
_SelfIPNumber_Object = MibScalar
selfIPNumber = _SelfIPNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 1),
    _SelfIPNumber_Type()
)
selfIPNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPNumber.setStatus("mandatory")
_SelfIPTable_Object = MibTable
selfIPTable = _SelfIPTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    selfIPTable.setStatus("mandatory")
_SelfIPEntry_Object = MibTableRow
selfIPEntry = _SelfIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1)
)
selfIPEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "selfIPAddress"),
)
if mibBuilder.loadTexts:
    selfIPEntry.setStatus("mandatory")
_SelfIPAddress_Type = IpAddress
_SelfIPAddress_Object = MibTableColumn
selfIPAddress = _SelfIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 1),
    _SelfIPAddress_Type()
)
selfIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPAddress.setStatus("mandatory")
_SelfIPNetmask_Type = IpAddress
_SelfIPNetmask_Object = MibTableColumn
selfIPNetmask = _SelfIPNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 2),
    _SelfIPNetmask_Type()
)
selfIPNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPNetmask.setStatus("mandatory")
_SelfIPBroadcast_Type = IpAddress
_SelfIPBroadcast_Object = MibTableColumn
selfIPBroadcast = _SelfIPBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 3),
    _SelfIPBroadcast_Type()
)
selfIPBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPBroadcast.setStatus("mandatory")
_SelfIPUnitID_Type = Integer32
_SelfIPUnitID_Object = MibTableColumn
selfIPUnitID = _SelfIPUnitID_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 4),
    _SelfIPUnitID_Type()
)
selfIPUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPUnitID.setStatus("mandatory")


class _SelfIPVLAN_Type(DisplayString):
    """Custom type selfIPVLAN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SelfIPVLAN_Type.__name__ = "DisplayString"
_SelfIPVLAN_Object = MibTableColumn
selfIPVLAN = _SelfIPVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 5),
    _SelfIPVLAN_Type()
)
selfIPVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPVLAN.setStatus("mandatory")


class _SelfIPSnatAutomap_Type(Integer32):
    """Custom type selfIPSnatAutomap based on Integer32"""
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


_SelfIPSnatAutomap_Type.__name__ = "Integer32"
_SelfIPSnatAutomap_Object = MibTableColumn
selfIPSnatAutomap = _SelfIPSnatAutomap_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 6),
    _SelfIPSnatAutomap_Type()
)
selfIPSnatAutomap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPSnatAutomap.setStatus("mandatory")


class _SelfIPIsFloating_Type(Integer32):
    """Custom type selfIPIsFloating based on Integer32"""
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


_SelfIPIsFloating_Type.__name__ = "Integer32"
_SelfIPIsFloating_Object = MibTableColumn
selfIPIsFloating = _SelfIPIsFloating_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 11, 2, 1, 7),
    _SelfIPIsFloating_Type()
)
selfIPIsFloating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    selfIPIsFloating.setStatus("mandatory")
_Trunk_ObjectIdentity = ObjectIdentity
trunk = _Trunk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12)
)


class _TrunkNumber_Type(Integer32):
    """Custom type trunkNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TrunkNumber_Type.__name__ = "Integer32"
_TrunkNumber_Object = MibScalar
trunkNumber = _TrunkNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 1),
    _TrunkNumber_Type()
)
trunkNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkNumber.setStatus("mandatory")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("mandatory")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 2, 1)
)
trunkEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "trunkControllingInterface"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("mandatory")


class _TrunkControllingInterface_Type(DisplayString):
    """Custom type trunkControllingInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrunkControllingInterface_Type.__name__ = "DisplayString"
_TrunkControllingInterface_Object = MibTableColumn
trunkControllingInterface = _TrunkControllingInterface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 2, 1, 1),
    _TrunkControllingInterface_Type()
)
trunkControllingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkControllingInterface.setStatus("mandatory")


class _TrunkInterfaces_Type(DisplayString):
    """Custom type trunkInterfaces based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TrunkInterfaces_Type.__name__ = "DisplayString"
_TrunkInterfaces_Object = MibTableColumn
trunkInterfaces = _TrunkInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 2, 1, 2),
    _TrunkInterfaces_Type()
)
trunkInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkInterfaces.setStatus("mandatory")
_TrunkMediaSpeed_Type = Counter64
_TrunkMediaSpeed_Object = MibTableColumn
trunkMediaSpeed = _TrunkMediaSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 12, 2, 1, 3),
    _TrunkMediaSpeed_Type()
)
trunkMediaSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMediaSpeed.setStatus("mandatory")
_Nodes_ObjectIdentity = ObjectIdentity
nodes = _Nodes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13)
)
_NodesNumber_Type = Integer32
_NodesNumber_Object = MibScalar
nodesNumber = _NodesNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 1),
    _NodesNumber_Type()
)
nodesNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesNumber.setStatus("mandatory")
_NodesTable_Object = MibTable
nodesTable = _NodesTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2)
)
if mibBuilder.loadTexts:
    nodesTable.setStatus("mandatory")
_NodesEntry_Object = MibTableRow
nodesEntry = _NodesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1)
)
nodesEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "nodesIndex"),
)
if mibBuilder.loadTexts:
    nodesEntry.setStatus("mandatory")


class _NodesIndex_Type(Integer32):
    """Custom type nodesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NodesIndex_Type.__name__ = "Integer32"
_NodesIndex_Object = MibTableColumn
nodesIndex = _NodesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 1),
    _NodesIndex_Type()
)
nodesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesIndex.setStatus("mandatory")


class _NodesAddr_Type(DisplayString):
    """Custom type nodesAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NodesAddr_Type.__name__ = "DisplayString"
_NodesAddr_Object = MibTableColumn
nodesAddr = _NodesAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 2),
    _NodesAddr_Type()
)
nodesAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesAddr.setStatus("mandatory")
_NodesPktsinLo32_Type = Counter32
_NodesPktsinLo32_Object = MibTableColumn
nodesPktsinLo32 = _NodesPktsinLo32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 3),
    _NodesPktsinLo32_Type()
)
nodesPktsinLo32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesPktsinLo32.setStatus("mandatory")
_NodesPktsinHi32_Type = Counter32
_NodesPktsinHi32_Object = MibTableColumn
nodesPktsinHi32 = _NodesPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 4),
    _NodesPktsinHi32_Type()
)
nodesPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesPktsinHi32.setStatus("mandatory")
_NodesPktsoutLo32_Type = Counter32
_NodesPktsoutLo32_Object = MibTableColumn
nodesPktsoutLo32 = _NodesPktsoutLo32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 5),
    _NodesPktsoutLo32_Type()
)
nodesPktsoutLo32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesPktsoutLo32.setStatus("mandatory")
_NodesPktsoutHi32_Type = Counter32
_NodesPktsoutHi32_Object = MibTableColumn
nodesPktsoutHi32 = _NodesPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 6),
    _NodesPktsoutHi32_Type()
)
nodesPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesPktsoutHi32.setStatus("mandatory")
_NodesBitsinLo32_Type = Counter32
_NodesBitsinLo32_Object = MibTableColumn
nodesBitsinLo32 = _NodesBitsinLo32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 7),
    _NodesBitsinLo32_Type()
)
nodesBitsinLo32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesBitsinLo32.setStatus("mandatory")
_NodesBitsinHi32_Type = Counter32
_NodesBitsinHi32_Object = MibTableColumn
nodesBitsinHi32 = _NodesBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 8),
    _NodesBitsinHi32_Type()
)
nodesBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesBitsinHi32.setStatus("mandatory")
_NodesBitsoutLo32_Type = Counter32
_NodesBitsoutLo32_Object = MibTableColumn
nodesBitsoutLo32 = _NodesBitsoutLo32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 9),
    _NodesBitsoutLo32_Type()
)
nodesBitsoutLo32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesBitsoutLo32.setStatus("mandatory")
_NodesBitsoutHi32_Type = Counter32
_NodesBitsoutHi32_Object = MibTableColumn
nodesBitsoutHi32 = _NodesBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 10),
    _NodesBitsoutHi32_Type()
)
nodesBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesBitsoutHi32.setStatus("mandatory")
_NodesCurrentConnections_Type = Integer32
_NodesCurrentConnections_Object = MibTableColumn
nodesCurrentConnections = _NodesCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 11),
    _NodesCurrentConnections_Type()
)
nodesCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesCurrentConnections.setStatus("mandatory")
_NodesMaximumConnections_Type = Integer32
_NodesMaximumConnections_Object = MibScalar
nodesMaximumConnections = _NodesMaximumConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 12),
    _NodesMaximumConnections_Type()
)
nodesMaximumConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesMaximumConnections.setStatus("mandatory")
_NodesConnectionLimit_Type = Integer32
_NodesConnectionLimit_Object = MibTableColumn
nodesConnectionLimit = _NodesConnectionLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 13),
    _NodesConnectionLimit_Type()
)
nodesConnectionLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesConnectionLimit.setStatus("mandatory")
_NodesTotalConnections_Type = Counter32
_NodesTotalConnections_Object = MibTableColumn
nodesTotalConnections = _NodesTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 14),
    _NodesTotalConnections_Type()
)
nodesTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesTotalConnections.setStatus("mandatory")


class _NodesEnabled_Type(Integer32):
    """Custom type nodesEnabled based on Integer32"""
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


_NodesEnabled_Type.__name__ = "Integer32"
_NodesEnabled_Object = MibTableColumn
nodesEnabled = _NodesEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 15),
    _NodesEnabled_Type()
)
nodesEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesEnabled.setStatus("mandatory")


class _NodesPingerState_Type(Integer32):
    """Custom type nodesPingerState based on Integer32"""
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
        *(("checking", 5),
          ("down", 3),
          ("forcedDown", 4),
          ("unchecked", 1),
          ("up", 2))
    )


_NodesPingerState_Type.__name__ = "Integer32"
_NodesPingerState_Object = MibTableColumn
nodesPingerState = _NodesPingerState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 13, 2, 1, 16),
    _NodesPingerState_Type()
)
nodesPingerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodesPingerState.setStatus("mandatory")
_Uptime_Type = TimeTicks
_Uptime_Object = MibScalar
uptime = _Uptime_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 50),
    _Uptime_Type()
)
uptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uptime.setStatus("deprecated")
_Contot_Type = Counter32
_Contot_Object = MibScalar
contot = _Contot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 51),
    _Contot_Type()
)
contot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contot.setStatus("deprecated")
_Concur_Type = Integer32
_Concur_Object = MibScalar
concur = _Concur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 52),
    _Concur_Type()
)
concur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concur.setStatus("deprecated")
_Conmax_Type = Integer32
_Conmax_Object = MibScalar
conmax = _Conmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 53),
    _Conmax_Type()
)
conmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conmax.setStatus("deprecated")
_Pktsin_Type = Counter32
_Pktsin_Object = MibScalar
pktsin = _Pktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 54),
    _Pktsin_Type()
)
pktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsin.setStatus("deprecated")
_Pktsout_Type = Counter32
_Pktsout_Object = MibScalar
pktsout = _Pktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 55),
    _Pktsout_Type()
)
pktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsout.setStatus("deprecated")
_Bitsin_Type = Counter32
_Bitsin_Object = MibScalar
bitsin = _Bitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 56),
    _Bitsin_Type()
)
bitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsin.setStatus("deprecated")
_Bitsout_Type = Counter32
_Bitsout_Object = MibScalar
bitsout = _Bitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 57),
    _Bitsout_Type()
)
bitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsout.setStatus("deprecated")
_Portdeny_Type = Counter32
_Portdeny_Object = MibScalar
portdeny = _Portdeny_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 58),
    _Portdeny_Type()
)
portdeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portdeny.setStatus("mandatory")
_Droppedin_Type = Counter32
_Droppedin_Object = MibScalar
droppedin = _Droppedin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 59),
    _Droppedin_Type()
)
droppedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedin.setStatus("mandatory")
_Droppedout_Type = Counter32
_Droppedout_Object = MibScalar
droppedout = _Droppedout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 60),
    _Droppedout_Type()
)
droppedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    droppedout.setStatus("mandatory")


class _Active_Type(Integer32):
    """Custom type active based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("standby", 1),
          ("unsupported", 99))
    )


_Active_Type.__name__ = "Integer32"
_Active_Object = MibScalar
active = _Active_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 61),
    _Active_Type()
)
active.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    active.setStatus("deprecated")


class _Mirrorenabled_Type(Integer32):
    """Custom type mirrorenabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("unsupported", 99))
    )


_Mirrorenabled_Type.__name__ = "Integer32"
_Mirrorenabled_Object = MibScalar
mirrorenabled = _Mirrorenabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 62),
    _Mirrorenabled_Type()
)
mirrorenabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mirrorenabled.setStatus("deprecated")


class _Resetcounters_Type(Integer32):
    """Custom type resetcounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unreset", 2),
          ("unsupported", 99))
    )


_Resetcounters_Type.__name__ = "Integer32"
_Resetcounters_Object = MibScalar
resetcounters = _Resetcounters_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 63),
    _Resetcounters_Type()
)
resetcounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    resetcounters.setStatus("mandatory")
_PktsinHi32_Type = Counter32
_PktsinHi32_Object = MibScalar
pktsinHi32 = _PktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 64),
    _PktsinHi32_Type()
)
pktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsinHi32.setStatus("deprecated")
_PktsoutHi32_Type = Counter32
_PktsoutHi32_Object = MibScalar
pktsoutHi32 = _PktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 65),
    _PktsoutHi32_Type()
)
pktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktsoutHi32.setStatus("deprecated")
_BitsinHi32_Type = Counter32
_BitsinHi32_Object = MibScalar
bitsinHi32 = _BitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 66),
    _BitsinHi32_Type()
)
bitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsinHi32.setStatus("deprecated")
_BitsoutHi32_Type = Counter32
_BitsoutHi32_Object = MibScalar
bitsoutHi32 = _BitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 67),
    _BitsoutHi32_Type()
)
bitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bitsoutHi32.setStatus("deprecated")
_NodePing_Type = Integer32
_NodePing_Object = MibScalar
nodePing = _NodePing_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 68),
    _NodePing_Type()
)
nodePing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodePing.setStatus("deprecated")
_NodeTimeout_Type = Integer32
_NodeTimeout_Object = MibScalar
nodeTimeout = _NodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 69),
    _NodeTimeout_Type()
)
nodeTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeTimeout.setStatus("deprecated")


class _LoadbalMode_Type(Integer32):
    """Custom type loadbalMode based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("dynamicRatio", 11),
          ("fastestAppResponse", 12),
          ("fastestNodeAddress", 8),
          ("leastConnMember", 3),
          ("leastConnNodeAddress", 7),
          ("observedMember", 4),
          ("observerdNodeAddress", 9),
          ("predictiveMember", 5),
          ("predictiveNodeAddress", 10),
          ("ratioMember", 2),
          ("ratioNodeAddress", 6),
          ("roundrobin", 1),
          ("unsupported", 99))
    )


_LoadbalMode_Type.__name__ = "Integer32"
_LoadbalMode_Object = MibScalar
loadbalMode = _LoadbalMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 70),
    _LoadbalMode_Type()
)
loadbalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadbalMode.setStatus("mandatory")


class _WatchDogArmed_Type(Integer32):
    """Custom type watchDogArmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("armed", 1),
          ("disarmed", 2),
          ("unsupported", 99))
    )


_WatchDogArmed_Type.__name__ = "Integer32"
_WatchDogArmed_Object = MibScalar
watchDogArmed = _WatchDogArmed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 71),
    _WatchDogArmed_Type()
)
watchDogArmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    watchDogArmed.setStatus("deprecated")
_SnatConnLimit_Type = Integer32
_SnatConnLimit_Object = MibScalar
snatConnLimit = _SnatConnLimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 72),
    _SnatConnLimit_Type()
)
snatConnLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatConnLimit.setStatus("deprecated")
_SnatTCPIdleTimeout_Type = Integer32
_SnatTCPIdleTimeout_Object = MibScalar
snatTCPIdleTimeout = _SnatTCPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 73),
    _SnatTCPIdleTimeout_Type()
)
snatTCPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatTCPIdleTimeout.setStatus("deprecated")
_SnatUDPIdleTimeout_Type = Integer32
_SnatUDPIdleTimeout_Object = MibScalar
snatUDPIdleTimeout = _SnatUDPIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 74),
    _SnatUDPIdleTimeout_Type()
)
snatUDPIdleTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snatUDPIdleTimeout.setStatus("deprecated")


class _GatewayFailsafe_Type(Integer32):
    """Custom type gatewayFailsafe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              99)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unsupported", 99))
    )


_GatewayFailsafe_Type.__name__ = "Integer32"
_GatewayFailsafe_Object = MibScalar
gatewayFailsafe = _GatewayFailsafe_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 75),
    _GatewayFailsafe_Type()
)
gatewayFailsafe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gatewayFailsafe.setStatus("deprecated")


class _UnitId_Type(DisplayString):
    """Custom type unitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UnitId_Type.__name__ = "DisplayString"
_UnitId_Object = MibScalar
unitId = _UnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 76),
    _UnitId_Type()
)
unitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitId.setStatus("deprecated")
_MemoryUsed_Type = Integer32
_MemoryUsed_Object = MibScalar
memoryUsed = _MemoryUsed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 77),
    _MemoryUsed_Type()
)
memoryUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsed.setStatus("deprecated")
_MemoryTotal_Type = Integer32
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 78),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("deprecated")
_CpuTemperature_Type = Integer32
_CpuTemperature_Object = MibScalar
cpuTemperature = _CpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 79),
    _CpuTemperature_Type()
)
cpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTemperature.setStatus("deprecated")
_FanSpeed_Type = Integer32
_FanSpeed_Object = MibScalar
fanSpeed = _FanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 80),
    _FanSpeed_Type()
)
fanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeed.setStatus("deprecated")


class _MultiprocessingMode_Type(Integer32):
    """Custom type multiprocessingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              99)
        )
    )
    namedValues = NamedValues(
        *(("anip", 2),
          ("smp", 3),
          ("unsupported", 99),
          ("up", 1))
    )


_MultiprocessingMode_Type.__name__ = "Integer32"
_MultiprocessingMode_Object = MibScalar
multiprocessingMode = _MultiprocessingMode_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 81),
    _MultiprocessingMode_Type()
)
multiprocessingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    multiprocessingMode.setStatus("deprecated")
_PercentANIP_Type = Integer32
_PercentANIP_Object = MibScalar
percentANIP = _PercentANIP_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 82),
    _PercentANIP_Type()
)
percentANIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    percentANIP.setStatus("deprecated")
_CpuCount_Type = Integer32
_CpuCount_Object = MibScalar
cpuCount = _CpuCount_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 83),
    _CpuCount_Type()
)
cpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCount.setStatus("deprecated")
_Vaddress_ObjectIdentity = ObjectIdentity
vaddress = _Vaddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100)
)
_VaddressNumber_Type = Integer32
_VaddressNumber_Object = MibScalar
vaddressNumber = _VaddressNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 1),
    _VaddressNumber_Type()
)
vaddressNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressNumber.setStatus("mandatory")
_VaddressTable_Object = MibTable
vaddressTable = _VaddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2)
)
if mibBuilder.loadTexts:
    vaddressTable.setStatus("mandatory")
_VaddressEntry_Object = MibTableRow
vaddressEntry = _VaddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1)
)
vaddressEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "vaddressIndex"),
)
if mibBuilder.loadTexts:
    vaddressEntry.setStatus("mandatory")


class _VaddressIndex_Type(Integer32):
    """Custom type vaddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VaddressIndex_Type.__name__ = "Integer32"
_VaddressIndex_Object = MibTableColumn
vaddressIndex = _VaddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 1),
    _VaddressIndex_Type()
)
vaddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressIndex.setStatus("mandatory")


class _VaddressDescr_Type(DisplayString):
    """Custom type vaddressDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VaddressDescr_Type.__name__ = "DisplayString"
_VaddressDescr_Object = MibTableColumn
vaddressDescr = _VaddressDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 2),
    _VaddressDescr_Type()
)
vaddressDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressDescr.setStatus("mandatory")
_VaddressIpAddr_Type = IpAddress
_VaddressIpAddr_Object = MibTableColumn
vaddressIpAddr = _VaddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 3),
    _VaddressIpAddr_Type()
)
vaddressIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressIpAddr.setStatus("mandatory")
_VaddressPktsin_Type = Counter32
_VaddressPktsin_Object = MibTableColumn
vaddressPktsin = _VaddressPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 4),
    _VaddressPktsin_Type()
)
vaddressPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsin.setStatus("mandatory")
_VaddressPktsout_Type = Counter32
_VaddressPktsout_Object = MibTableColumn
vaddressPktsout = _VaddressPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 5),
    _VaddressPktsout_Type()
)
vaddressPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsout.setStatus("mandatory")
_VaddressBitsin_Type = Counter32
_VaddressBitsin_Object = MibTableColumn
vaddressBitsin = _VaddressBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 6),
    _VaddressBitsin_Type()
)
vaddressBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsin.setStatus("mandatory")
_VaddressBitsout_Type = Counter32
_VaddressBitsout_Object = MibTableColumn
vaddressBitsout = _VaddressBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 7),
    _VaddressBitsout_Type()
)
vaddressBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsout.setStatus("mandatory")
_VaddressConcur_Type = Integer32
_VaddressConcur_Object = MibTableColumn
vaddressConcur = _VaddressConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 8),
    _VaddressConcur_Type()
)
vaddressConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConcur.setStatus("mandatory")
_VaddressConmax_Type = Integer32
_VaddressConmax_Object = MibTableColumn
vaddressConmax = _VaddressConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 9),
    _VaddressConmax_Type()
)
vaddressConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConmax.setStatus("mandatory")
_VaddressConlimit_Type = Integer32
_VaddressConlimit_Object = MibTableColumn
vaddressConlimit = _VaddressConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 10),
    _VaddressConlimit_Type()
)
vaddressConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressConlimit.setStatus("mandatory")
_VaddressContot_Type = Counter32
_VaddressContot_Object = MibTableColumn
vaddressContot = _VaddressContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 11),
    _VaddressContot_Type()
)
vaddressContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressContot.setStatus("mandatory")


class _VaddressStatus_Type(Integer32):
    """Custom type vaddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maintenance", 2),
          ("ready", 1))
    )


_VaddressStatus_Type.__name__ = "Integer32"
_VaddressStatus_Object = MibTableColumn
vaddressStatus = _VaddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 12),
    _VaddressStatus_Type()
)
vaddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressStatus.setStatus("mandatory")
_VaddressPktsinHi32_Type = Counter32
_VaddressPktsinHi32_Object = MibTableColumn
vaddressPktsinHi32 = _VaddressPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 13),
    _VaddressPktsinHi32_Type()
)
vaddressPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsinHi32.setStatus("mandatory")
_VaddressPktsoutHi32_Type = Counter32
_VaddressPktsoutHi32_Object = MibTableColumn
vaddressPktsoutHi32 = _VaddressPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 14),
    _VaddressPktsoutHi32_Type()
)
vaddressPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressPktsoutHi32.setStatus("mandatory")
_VaddressBitsinHi32_Type = Counter32
_VaddressBitsinHi32_Object = MibTableColumn
vaddressBitsinHi32 = _VaddressBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 15),
    _VaddressBitsinHi32_Type()
)
vaddressBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsinHi32.setStatus("mandatory")
_VaddressBitsoutHi32_Type = Counter32
_VaddressBitsoutHi32_Object = MibTableColumn
vaddressBitsoutHi32 = _VaddressBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 100, 2, 1, 16),
    _VaddressBitsoutHi32_Type()
)
vaddressBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vaddressBitsoutHi32.setStatus("mandatory")
_Ndaddr_ObjectIdentity = ObjectIdentity
ndaddr = _Ndaddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101)
)
_NdaddrNumber_Type = Integer32
_NdaddrNumber_Object = MibScalar
ndaddrNumber = _NdaddrNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 1),
    _NdaddrNumber_Type()
)
ndaddrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrNumber.setStatus("mandatory")
_NdaddrTable_Object = MibTable
ndaddrTable = _NdaddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2)
)
if mibBuilder.loadTexts:
    ndaddrTable.setStatus("mandatory")
_NdaddrEntry_Object = MibTableRow
ndaddrEntry = _NdaddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1)
)
ndaddrEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "ndaddrIndex"),
)
if mibBuilder.loadTexts:
    ndaddrEntry.setStatus("mandatory")


class _NdaddrIndex_Type(Integer32):
    """Custom type ndaddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NdaddrIndex_Type.__name__ = "Integer32"
_NdaddrIndex_Object = MibTableColumn
ndaddrIndex = _NdaddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 1),
    _NdaddrIndex_Type()
)
ndaddrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrIndex.setStatus("mandatory")


class _NdaddrDescr_Type(DisplayString):
    """Custom type ndaddrDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NdaddrDescr_Type.__name__ = "DisplayString"
_NdaddrDescr_Object = MibTableColumn
ndaddrDescr = _NdaddrDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 2),
    _NdaddrDescr_Type()
)
ndaddrDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrDescr.setStatus("mandatory")
_NdaddrIpAddr_Type = IpAddress
_NdaddrIpAddr_Object = MibTableColumn
ndaddrIpAddr = _NdaddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 3),
    _NdaddrIpAddr_Type()
)
ndaddrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrIpAddr.setStatus("mandatory")
_NdaddrPktsin_Type = Counter32
_NdaddrPktsin_Object = MibTableColumn
ndaddrPktsin = _NdaddrPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 4),
    _NdaddrPktsin_Type()
)
ndaddrPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsin.setStatus("mandatory")
_NdaddrPktsout_Type = Counter32
_NdaddrPktsout_Object = MibTableColumn
ndaddrPktsout = _NdaddrPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 5),
    _NdaddrPktsout_Type()
)
ndaddrPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsout.setStatus("mandatory")
_NdaddrBitsin_Type = Counter32
_NdaddrBitsin_Object = MibTableColumn
ndaddrBitsin = _NdaddrBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 6),
    _NdaddrBitsin_Type()
)
ndaddrBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsin.setStatus("mandatory")
_NdaddrBitsout_Type = Counter32
_NdaddrBitsout_Object = MibTableColumn
ndaddrBitsout = _NdaddrBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 7),
    _NdaddrBitsout_Type()
)
ndaddrBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsout.setStatus("mandatory")
_NdaddrConcur_Type = Integer32
_NdaddrConcur_Object = MibTableColumn
ndaddrConcur = _NdaddrConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 8),
    _NdaddrConcur_Type()
)
ndaddrConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConcur.setStatus("mandatory")
_NdaddrConmax_Type = Integer32
_NdaddrConmax_Object = MibTableColumn
ndaddrConmax = _NdaddrConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 9),
    _NdaddrConmax_Type()
)
ndaddrConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConmax.setStatus("mandatory")
_NdaddrConlimit_Type = Integer32
_NdaddrConlimit_Object = MibTableColumn
ndaddrConlimit = _NdaddrConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 10),
    _NdaddrConlimit_Type()
)
ndaddrConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrConlimit.setStatus("mandatory")
_NdaddrContot_Type = Counter32
_NdaddrContot_Object = MibTableColumn
ndaddrContot = _NdaddrContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 11),
    _NdaddrContot_Type()
)
ndaddrContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrContot.setStatus("mandatory")
_NdaddrStatus_Type = BigAPIStatus
_NdaddrStatus_Object = MibTableColumn
ndaddrStatus = _NdaddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 12),
    _NdaddrStatus_Type()
)
ndaddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrStatus.setStatus("mandatory")
_NdaddrPktsinHi32_Type = Counter32
_NdaddrPktsinHi32_Object = MibTableColumn
ndaddrPktsinHi32 = _NdaddrPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 13),
    _NdaddrPktsinHi32_Type()
)
ndaddrPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsinHi32.setStatus("mandatory")
_NdaddrPktsoutHi32_Type = Counter32
_NdaddrPktsoutHi32_Object = MibTableColumn
ndaddrPktsoutHi32 = _NdaddrPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 14),
    _NdaddrPktsoutHi32_Type()
)
ndaddrPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPktsoutHi32.setStatus("mandatory")
_NdaddrBitsinHi32_Type = Counter32
_NdaddrBitsinHi32_Object = MibTableColumn
ndaddrBitsinHi32 = _NdaddrBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 15),
    _NdaddrBitsinHi32_Type()
)
ndaddrBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsinHi32.setStatus("mandatory")
_NdaddrBitsoutHi32_Type = Counter32
_NdaddrBitsoutHi32_Object = MibTableColumn
ndaddrBitsoutHi32 = _NdaddrBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 16),
    _NdaddrBitsoutHi32_Type()
)
ndaddrBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrBitsoutHi32.setStatus("mandatory")


class _NdaddrMaintenance_Type(Integer32):
    """Custom type ndaddrMaintenance based on Integer32"""
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


_NdaddrMaintenance_Type.__name__ = "Integer32"
_NdaddrMaintenance_Object = MibTableColumn
ndaddrMaintenance = _NdaddrMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 17),
    _NdaddrMaintenance_Type()
)
ndaddrMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrMaintenance.setStatus("mandatory")


class _NdaddrIsVirtual_Type(Integer32):
    """Custom type ndaddrIsVirtual based on Integer32"""
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


_NdaddrIsVirtual_Type.__name__ = "Integer32"
_NdaddrIsVirtual_Object = MibTableColumn
ndaddrIsVirtual = _NdaddrIsVirtual_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 18),
    _NdaddrIsVirtual_Type()
)
ndaddrIsVirtual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrIsVirtual.setStatus("mandatory")
_NdaddrRatio_Type = Integer32
_NdaddrRatio_Object = MibTableColumn
ndaddrRatio = _NdaddrRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 19),
    _NdaddrRatio_Type()
)
ndaddrRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrRatio.setStatus("mandatory")
_NdaddrTotalRealMemory_Type = Integer32
_NdaddrTotalRealMemory_Object = MibTableColumn
ndaddrTotalRealMemory = _NdaddrTotalRealMemory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 20),
    _NdaddrTotalRealMemory_Type()
)
ndaddrTotalRealMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrTotalRealMemory.setStatus("mandatory")
_NdaddrAvailableRealMemory_Type = Integer32
_NdaddrAvailableRealMemory_Object = MibTableColumn
ndaddrAvailableRealMemory = _NdaddrAvailableRealMemory_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 21),
    _NdaddrAvailableRealMemory_Type()
)
ndaddrAvailableRealMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrAvailableRealMemory.setStatus("mandatory")
_NdaddrTotalDisk_Type = Integer32
_NdaddrTotalDisk_Object = MibTableColumn
ndaddrTotalDisk = _NdaddrTotalDisk_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 22),
    _NdaddrTotalDisk_Type()
)
ndaddrTotalDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrTotalDisk.setStatus("mandatory")
_NdaddrAvailableDisk_Type = Integer32
_NdaddrAvailableDisk_Object = MibTableColumn
ndaddrAvailableDisk = _NdaddrAvailableDisk_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 23),
    _NdaddrAvailableDisk_Type()
)
ndaddrAvailableDisk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrAvailableDisk.setStatus("mandatory")
_NdaddrAvailableCPU_Type = Integer32
_NdaddrAvailableCPU_Object = MibTableColumn
ndaddrAvailableCPU = _NdaddrAvailableCPU_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 24),
    _NdaddrAvailableCPU_Type()
)
ndaddrAvailableCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrAvailableCPU.setStatus("mandatory")
_NdaddrDynamicRatio_Type = Integer32
_NdaddrDynamicRatio_Object = MibTableColumn
ndaddrDynamicRatio = _NdaddrDynamicRatio_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 25),
    _NdaddrDynamicRatio_Type()
)
ndaddrDynamicRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrDynamicRatio.setStatus("mandatory")


class _NdaddrPingerState_Type(Integer32):
    """Custom type ndaddrPingerState based on Integer32"""
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
        *(("checking", 5),
          ("down", 3),
          ("forcedDown", 4),
          ("unchecked", 1),
          ("up", 2))
    )


_NdaddrPingerState_Type.__name__ = "Integer32"
_NdaddrPingerState_Object = MibTableColumn
ndaddrPingerState = _NdaddrPingerState_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 101, 2, 1, 26),
    _NdaddrPingerState_Type()
)
ndaddrPingerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ndaddrPingerState.setStatus("mandatory")
_Nat_ObjectIdentity = ObjectIdentity
nat = _Nat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102)
)
_NatNumber_Type = Integer32
_NatNumber_Object = MibScalar
natNumber = _NatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 1),
    _NatNumber_Type()
)
natNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natNumber.setStatus("mandatory")
_NatTable_Object = MibTable
natTable = _NatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2)
)
if mibBuilder.loadTexts:
    natTable.setStatus("mandatory")
_NatEntry_Object = MibTableRow
natEntry = _NatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1)
)
natEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "natIndex"),
)
if mibBuilder.loadTexts:
    natEntry.setStatus("mandatory")


class _NatIndex_Type(Integer32):
    """Custom type natIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_NatIndex_Type.__name__ = "Integer32"
_NatIndex_Object = MibTableColumn
natIndex = _NatIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 1),
    _NatIndex_Type()
)
natIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIndex.setStatus("mandatory")


class _NatDescr_Type(DisplayString):
    """Custom type natDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatDescr_Type.__name__ = "DisplayString"
_NatDescr_Object = MibTableColumn
natDescr = _NatDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 2),
    _NatDescr_Type()
)
natDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natDescr.setStatus("mandatory")
_NatIpAddrFR_Type = IpAddress
_NatIpAddrFR_Object = MibTableColumn
natIpAddrFR = _NatIpAddrFR_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 3),
    _NatIpAddrFR_Type()
)
natIpAddrFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIpAddrFR.setStatus("mandatory")
_NatIpAddrTO_Type = IpAddress
_NatIpAddrTO_Object = MibTableColumn
natIpAddrTO = _NatIpAddrTO_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 4),
    _NatIpAddrTO_Type()
)
natIpAddrTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natIpAddrTO.setStatus("mandatory")
_NatPktsin_Type = Counter32
_NatPktsin_Object = MibTableColumn
natPktsin = _NatPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 5),
    _NatPktsin_Type()
)
natPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsin.setStatus("mandatory")
_NatPktsout_Type = Counter32
_NatPktsout_Object = MibTableColumn
natPktsout = _NatPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 6),
    _NatPktsout_Type()
)
natPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsout.setStatus("mandatory")
_NatBitsin_Type = Counter32
_NatBitsin_Object = MibTableColumn
natBitsin = _NatBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 7),
    _NatBitsin_Type()
)
natBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsin.setStatus("mandatory")
_NatBitsout_Type = Counter32
_NatBitsout_Object = MibTableColumn
natBitsout = _NatBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 8),
    _NatBitsout_Type()
)
natBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsout.setStatus("mandatory")
_NatPktsinHi32_Type = Counter32
_NatPktsinHi32_Object = MibTableColumn
natPktsinHi32 = _NatPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 9),
    _NatPktsinHi32_Type()
)
natPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsinHi32.setStatus("mandatory")
_NatPktsoutHi32_Type = Counter32
_NatPktsoutHi32_Object = MibTableColumn
natPktsoutHi32 = _NatPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 10),
    _NatPktsoutHi32_Type()
)
natPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natPktsoutHi32.setStatus("mandatory")
_NatBitsinHi32_Type = Counter32
_NatBitsinHi32_Object = MibTableColumn
natBitsinHi32 = _NatBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 11),
    _NatBitsinHi32_Type()
)
natBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsinHi32.setStatus("mandatory")
_NatBitsoutHi32_Type = Counter32
_NatBitsoutHi32_Object = MibTableColumn
natBitsoutHi32 = _NatBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 12),
    _NatBitsoutHi32_Type()
)
natBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natBitsoutHi32.setStatus("mandatory")
_NatOutsideNetmask_Type = IpAddress
_NatOutsideNetmask_Object = MibTableColumn
natOutsideNetmask = _NatOutsideNetmask_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 13),
    _NatOutsideNetmask_Type()
)
natOutsideNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natOutsideNetmask.setStatus("mandatory")
_NatOutsideBroadcast_Type = IpAddress
_NatOutsideBroadcast_Object = MibTableColumn
natOutsideBroadcast = _NatOutsideBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 14),
    _NatOutsideBroadcast_Type()
)
natOutsideBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natOutsideBroadcast.setStatus("mandatory")


class _NatInterface_Type(DisplayString):
    """Custom type natInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatInterface_Type.__name__ = "DisplayString"
_NatInterface_Object = MibTableColumn
natInterface = _NatInterface_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 15),
    _NatInterface_Type()
)
natInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natInterface.setStatus("deprecated")
_NatUnitId_Type = Integer32
_NatUnitId_Object = MibTableColumn
natUnitId = _NatUnitId_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 16),
    _NatUnitId_Type()
)
natUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natUnitId.setStatus("mandatory")


class _NatVLANs_Type(DisplayString):
    """Custom type natVLANs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatVLANs_Type.__name__ = "DisplayString"
_NatVLANs_Object = MibTableColumn
natVLANs = _NatVLANs_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 17),
    _NatVLANs_Type()
)
natVLANs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natVLANs.setStatus("mandatory")


class _NatARPEnabled_Type(Integer32):
    """Custom type natARPEnabled based on Integer32"""
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


_NatARPEnabled_Type.__name__ = "Integer32"
_NatARPEnabled_Object = MibTableColumn
natARPEnabled = _NatARPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 18),
    _NatARPEnabled_Type()
)
natARPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natARPEnabled.setStatus("mandatory")


class _NatEnabled_Type(Integer32):
    """Custom type natEnabled based on Integer32"""
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


_NatEnabled_Type.__name__ = "Integer32"
_NatEnabled_Object = MibTableColumn
natEnabled = _NatEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 19),
    _NatEnabled_Type()
)
natEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natEnabled.setStatus("mandatory")


class _NatServices_Type(DisplayString):
    """Custom type natServices based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NatServices_Type.__name__ = "DisplayString"
_NatServices_Object = MibTableColumn
natServices = _NatServices_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 102, 2, 1, 20),
    _NatServices_Type()
)
natServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natServices.setStatus("mandatory")
_Vport_ObjectIdentity = ObjectIdentity
vport = _Vport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103)
)
_VportNumber_Type = Integer32
_VportNumber_Object = MibScalar
vportNumber = _VportNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 1),
    _VportNumber_Type()
)
vportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportNumber.setStatus("mandatory")
_VportTable_Object = MibTable
vportTable = _VportTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2)
)
if mibBuilder.loadTexts:
    vportTable.setStatus("mandatory")
_VportEntry_Object = MibTableRow
vportEntry = _VportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1)
)
vportEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "vportIndex"),
)
if mibBuilder.loadTexts:
    vportEntry.setStatus("mandatory")


class _VportIndex_Type(Integer32):
    """Custom type vportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VportIndex_Type.__name__ = "Integer32"
_VportIndex_Object = MibTableColumn
vportIndex = _VportIndex_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 1),
    _VportIndex_Type()
)
vportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportIndex.setStatus("mandatory")
_VportPort_Type = Integer32
_VportPort_Object = MibTableColumn
vportPort = _VportPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 2),
    _VportPort_Type()
)
vportPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPort.setStatus("mandatory")


class _VportDescr_Type(DisplayString):
    """Custom type vportDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VportDescr_Type.__name__ = "DisplayString"
_VportDescr_Object = MibTableColumn
vportDescr = _VportDescr_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 3),
    _VportDescr_Type()
)
vportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportDescr.setStatus("mandatory")
_VportPktsin_Type = Counter32
_VportPktsin_Object = MibTableColumn
vportPktsin = _VportPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 4),
    _VportPktsin_Type()
)
vportPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsin.setStatus("mandatory")
_VportPktsout_Type = Counter32
_VportPktsout_Object = MibTableColumn
vportPktsout = _VportPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 5),
    _VportPktsout_Type()
)
vportPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsout.setStatus("mandatory")
_VportBitsin_Type = Counter32
_VportBitsin_Object = MibTableColumn
vportBitsin = _VportBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 6),
    _VportBitsin_Type()
)
vportBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsin.setStatus("mandatory")
_VportBitsout_Type = Counter32
_VportBitsout_Object = MibTableColumn
vportBitsout = _VportBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 7),
    _VportBitsout_Type()
)
vportBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsout.setStatus("mandatory")
_VportConcur_Type = Integer32
_VportConcur_Object = MibTableColumn
vportConcur = _VportConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 8),
    _VportConcur_Type()
)
vportConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConcur.setStatus("mandatory")
_VportConmax_Type = Integer32
_VportConmax_Object = MibTableColumn
vportConmax = _VportConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 9),
    _VportConmax_Type()
)
vportConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConmax.setStatus("mandatory")
_VportConlimit_Type = Integer32
_VportConlimit_Object = MibTableColumn
vportConlimit = _VportConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 10),
    _VportConlimit_Type()
)
vportConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportConlimit.setStatus("mandatory")
_VportContot_Type = Counter32
_VportContot_Object = MibTableColumn
vportContot = _VportContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 11),
    _VportContot_Type()
)
vportContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportContot.setStatus("mandatory")
_VportReaped_Type = Counter32
_VportReaped_Object = MibTableColumn
vportReaped = _VportReaped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 12),
    _VportReaped_Type()
)
vportReaped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportReaped.setStatus("mandatory")
_VportPktsinHi32_Type = Counter32
_VportPktsinHi32_Object = MibTableColumn
vportPktsinHi32 = _VportPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 13),
    _VportPktsinHi32_Type()
)
vportPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsinHi32.setStatus("mandatory")
_VportPktsoutHi32_Type = Counter32
_VportPktsoutHi32_Object = MibTableColumn
vportPktsoutHi32 = _VportPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 14),
    _VportPktsoutHi32_Type()
)
vportPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportPktsoutHi32.setStatus("mandatory")
_VportBitsinHi32_Type = Counter32
_VportBitsinHi32_Object = MibTableColumn
vportBitsinHi32 = _VportBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 15),
    _VportBitsinHi32_Type()
)
vportBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsinHi32.setStatus("mandatory")
_VportBitsoutHi32_Type = Counter32
_VportBitsoutHi32_Object = MibTableColumn
vportBitsoutHi32 = _VportBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 16),
    _VportBitsoutHi32_Type()
)
vportBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportBitsoutHi32.setStatus("mandatory")


class _VportAllowed_Type(Integer32):
    """Custom type vportAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_VportAllowed_Type.__name__ = "Integer32"
_VportAllowed_Object = MibTableColumn
vportAllowed = _VportAllowed_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 17),
    _VportAllowed_Type()
)
vportAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportAllowed.setStatus("mandatory")
_VportTCPpersistence_Type = Integer32
_VportTCPpersistence_Object = MibTableColumn
vportTCPpersistence = _VportTCPpersistence_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 18),
    _VportTCPpersistence_Type()
)
vportTCPpersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportTCPpersistence.setStatus("mandatory")
_VportUDPpersistence_Type = Integer32
_VportUDPpersistence_Object = MibTableColumn
vportUDPpersistence = _VportUDPpersistence_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 19),
    _VportUDPpersistence_Type()
)
vportUDPpersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportUDPpersistence.setStatus("mandatory")
_VportIPpersistence_Type = Integer32
_VportIPpersistence_Object = MibTableColumn
vportIPpersistence = _VportIPpersistence_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 20),
    _VportIPpersistence_Type()
)
vportIPpersistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportIPpersistence.setStatus("mandatory")


class _VportUDPEnabled_Type(Integer32):
    """Custom type vportUDPEnabled based on Integer32"""
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


_VportUDPEnabled_Type.__name__ = "Integer32"
_VportUDPEnabled_Object = MibTableColumn
vportUDPEnabled = _VportUDPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 103, 2, 1, 21),
    _VportUDPEnabled_Type()
)
vportUDPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vportUDPEnabled.setStatus("mandatory")
_Member_ObjectIdentity = ObjectIdentity
member = _Member_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104)
)
_MemberTable_Object = MibTable
memberTable = _MemberTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2)
)
if mibBuilder.loadTexts:
    memberTable.setStatus("mandatory")
_MemberEntry_Object = MibTableRow
memberEntry = _MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1)
)
memberEntry.setIndexNames(
    (0, "LOAD-BAL-SYSTEM-MIB", "memberVirtualAddress"),
    (0, "LOAD-BAL-SYSTEM-MIB", "memberVirtualAddressPort"),
    (0, "LOAD-BAL-SYSTEM-MIB", "memberOrdinal"),
)
if mibBuilder.loadTexts:
    memberEntry.setStatus("mandatory")
_MemberVirtualAddress_Type = IpAddress
_MemberVirtualAddress_Object = MibTableColumn
memberVirtualAddress = _MemberVirtualAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 1),
    _MemberVirtualAddress_Type()
)
memberVirtualAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberVirtualAddress.setStatus("mandatory")


class _MemberVirtualAddressPort_Type(Integer32):
    """Custom type memberVirtualAddressPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemberVirtualAddressPort_Type.__name__ = "Integer32"
_MemberVirtualAddressPort_Object = MibTableColumn
memberVirtualAddressPort = _MemberVirtualAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 2),
    _MemberVirtualAddressPort_Type()
)
memberVirtualAddressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberVirtualAddressPort.setStatus("mandatory")


class _MemberOrdinal_Type(Integer32):
    """Custom type memberOrdinal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MemberOrdinal_Type.__name__ = "Integer32"
_MemberOrdinal_Object = MibTableColumn
memberOrdinal = _MemberOrdinal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 3),
    _MemberOrdinal_Type()
)
memberOrdinal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberOrdinal.setStatus("mandatory")
_MemberAddress_Type = IpAddress
_MemberAddress_Object = MibTableColumn
memberAddress = _MemberAddress_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 4),
    _MemberAddress_Type()
)
memberAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberAddress.setStatus("mandatory")
_MemberPort_Type = Integer32
_MemberPort_Object = MibTableColumn
memberPort = _MemberPort_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 5),
    _MemberPort_Type()
)
memberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPort.setStatus("mandatory")
_MemberStatus_Type = BigAPIStatus
_MemberStatus_Object = MibTableColumn
memberStatus = _MemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 6),
    _MemberStatus_Type()
)
memberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberStatus.setStatus("mandatory")
_MemberPktsin_Type = Counter32
_MemberPktsin_Object = MibTableColumn
memberPktsin = _MemberPktsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 7),
    _MemberPktsin_Type()
)
memberPktsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsin.setStatus("mandatory")
_MemberPktsout_Type = Counter32
_MemberPktsout_Object = MibTableColumn
memberPktsout = _MemberPktsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 8),
    _MemberPktsout_Type()
)
memberPktsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsout.setStatus("mandatory")
_MemberBitsin_Type = Counter32
_MemberBitsin_Object = MibTableColumn
memberBitsin = _MemberBitsin_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 9),
    _MemberBitsin_Type()
)
memberBitsin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsin.setStatus("mandatory")
_MemberBitsout_Type = Counter32
_MemberBitsout_Object = MibTableColumn
memberBitsout = _MemberBitsout_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 10),
    _MemberBitsout_Type()
)
memberBitsout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsout.setStatus("mandatory")
_MemberConcur_Type = Integer32
_MemberConcur_Object = MibTableColumn
memberConcur = _MemberConcur_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 11),
    _MemberConcur_Type()
)
memberConcur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConcur.setStatus("mandatory")
_MemberConmax_Type = Integer32
_MemberConmax_Object = MibTableColumn
memberConmax = _MemberConmax_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 12),
    _MemberConmax_Type()
)
memberConmax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConmax.setStatus("mandatory")
_MemberConlimit_Type = Integer32
_MemberConlimit_Object = MibTableColumn
memberConlimit = _MemberConlimit_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 13),
    _MemberConlimit_Type()
)
memberConlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberConlimit.setStatus("mandatory")
_MemberContot_Type = Counter32
_MemberContot_Object = MibTableColumn
memberContot = _MemberContot_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 14),
    _MemberContot_Type()
)
memberContot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberContot.setStatus("mandatory")
_MemberPktsinHi32_Type = Counter32
_MemberPktsinHi32_Object = MibTableColumn
memberPktsinHi32 = _MemberPktsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 15),
    _MemberPktsinHi32_Type()
)
memberPktsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsinHi32.setStatus("mandatory")
_MemberPktsoutHi32_Type = Counter32
_MemberPktsoutHi32_Object = MibTableColumn
memberPktsoutHi32 = _MemberPktsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 16),
    _MemberPktsoutHi32_Type()
)
memberPktsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberPktsoutHi32.setStatus("mandatory")
_MemberBitsinHi32_Type = Counter32
_MemberBitsinHi32_Object = MibTableColumn
memberBitsinHi32 = _MemberBitsinHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 17),
    _MemberBitsinHi32_Type()
)
memberBitsinHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsinHi32.setStatus("mandatory")
_MemberBitsoutHi32_Type = Counter32
_MemberBitsoutHi32_Object = MibTableColumn
memberBitsoutHi32 = _MemberBitsoutHi32_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 104, 2, 1, 18),
    _MemberBitsoutHi32_Type()
)
memberBitsoutHi32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memberBitsoutHi32.setStatus("mandatory")
_LoadBalTrap_ObjectIdentity = ObjectIdentity
loadBalTrap = _LoadBalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110)
)
_LoadBalTraps_ObjectIdentity = ObjectIdentity
loadBalTraps = _LoadBalTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2)
)
_LoadBalTrapMessage_Type = DisplayString
_LoadBalTrapMessage_Object = MibScalar
loadBalTrapMessage = _LoadBalTrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 1),
    _LoadBalTrapMessage_Type()
)
loadBalTrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadBalTrapMessage.setStatus("mandatory")
_IpAddressString_Type = DisplayString
_IpAddressString_Object = MibScalar
ipAddressString = _IpAddressString_Object(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 2),
    _IpAddressString_Type()
)
ipAddressString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressString.setStatus("mandatory")

# Managed Objects groups


# Notification objects

loadBalTrapMisc = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 1)
)
loadBalTrapMisc.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapMisc.setStatus(
        ""
    )

loadBalTrapServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 2)
)
loadBalTrapServiceDown.setObjects(
      *(("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage"),
        ("LOAD-BAL-SYSTEM-MIB", "ipAddressString"),
        ("LOAD-BAL-SYSTEM-MIB", "memberPort"))
)
if mibBuilder.loadTexts:
    loadBalTrapServiceDown.setStatus(
        ""
    )

loadBalTrapServiceUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 3)
)
loadBalTrapServiceUP.setObjects(
      *(("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage"),
        ("LOAD-BAL-SYSTEM-MIB", "ipAddressString"),
        ("LOAD-BAL-SYSTEM-MIB", "memberPort"))
)
if mibBuilder.loadTexts:
    loadBalTrapServiceUP.setStatus(
        ""
    )

loadBalTrapReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 4)
)
loadBalTrapReset.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapReset.setStatus(
        ""
    )

loadBalTrapDenial = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 5)
)
loadBalTrapDenial.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapDenial.setStatus(
        ""
    )

loadBalTrapLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 6)
)
loadBalTrapLogin.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapLogin.setStatus(
        ""
    )

loadBalTrapRemoveUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 7)
)
loadBalTrapRemoveUnit.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapRemoveUnit.setStatus(
        ""
    )

loadBalTrapAddUnit = NotificationType(
    (1, 3, 6, 1, 4, 1, 3375, 1, 1, 110, 2, 0, 8)
)
loadBalTrapAddUnit.setObjects(
    ("LOAD-BAL-SYSTEM-MIB", "loadBalTrapMessage")
)
if mibBuilder.loadTexts:
    loadBalTrapAddUnit.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOAD-BAL-SYSTEM-MIB",
    **{"DisplayString": DisplayString,
       "BigAPIStatus": BigAPIStatus,
       "f5": f5,
       "f5systems": f5systems,
       "loadbal": loadbal,
       "globals": globals,
       "globalAttributes": globalAttributes,
       "globalAttrKernelVersion": globalAttrKernelVersion,
       "globalAttrPackageVersion": globalAttrPackageVersion,
       "globalAttrPackageEdition": globalAttrPackageEdition,
       "globalAttrAgentVersion": globalAttrAgentVersion,
       "globalAttrProductCode": globalAttrProductCode,
       "globalAttrSerialNumber": globalAttrSerialNumber,
       "globalAttrVendorName": globalAttrVendorName,
       "globalAttrSSLGatewayLevel": globalAttrSSLGatewayLevel,
       "globalAttrCPUCount": globalAttrCPUCount,
       "globalAttrAuthorized": globalAttrAuthorized,
       "globalAttrMaintenceMode": globalAttrMaintenceMode,
       "globalAttrMaster": globalAttrMaster,
       "globalAttrUnitID": globalAttrUnitID,
       "globalAttrPeerUnitID": globalAttrPeerUnitID,
       "globalAttrFastestMaxIdleTime": globalAttrFastestMaxIdleTime,
       "globalAttrFastFlowActive": globalAttrFastFlowActive,
       "globalAttrGatewayFailsafeArmed": globalAttrGatewayFailsafeArmed,
       "globalAttrMemoryRebootPercent": globalAttrMemoryRebootPercent,
       "globalAttrMirrorEnabled": globalAttrMirrorEnabled,
       "globalAttrVerboseLogLevel": globalAttrVerboseLogLevel,
       "globalAttrWatchDogArmed": globalAttrWatchDogArmed,
       "globalAttrAutoLastHop": globalAttrAutoLastHop,
       "globalAttrAkamaiConfigPort": globalAttrAkamaiConfigPort,
       "globalAttrNameSurferWebPort": globalAttrNameSurferWebPort,
       "globalAttrNameSurferZonePort": globalAttrNameSurferZonePort,
       "globalAttrOpen3DNSPorts": globalAttrOpen3DNSPorts,
       "globalAttrOpenCorbaPorts": globalAttrOpenCorbaPorts,
       "globalAttrOpenFTPPorts": globalAttrOpenFTPPorts,
       "globalAttrOpenRSHPorts": globalAttrOpenRSHPorts,
       "globalAttrOpenSSHPorts": globalAttrOpenSSHPorts,
       "globalAttrOpenTelnetPorts": globalAttrOpenTelnetPorts,
       "globalAttrWebAdminPort": globalAttrWebAdminPort,
       "globalAttrPersistAcrossServices": globalAttrPersistAcrossServices,
       "globalAttrPersistAccrossVirtuals": globalAttrPersistAccrossVirtuals,
       "globalAttrPersistMapProxies": globalAttrPersistMapProxies,
       "globalAttrPersistTimerUsedAsLimit": globalAttrPersistTimerUsedAsLimit,
       "globalAttrStickyTableLimit": globalAttrStickyTableLimit,
       "globalAttrSNATConnLimit": globalAttrSNATConnLimit,
       "globalAttrSNATTCPIdleTimeout": globalAttrSNATTCPIdleTimeout,
       "globalAttrSNATUDPIdleTimeout": globalAttrSNATUDPIdleTimeout,
       "globalAttrSystemType": globalAttrSystemType,
       "globalAttrNetReboot": globalAttrNetReboot,
       "globalAttrQuietBoot": globalAttrQuietBoot,
       "globalAttrL2CacheTimeout": globalAttrL2CacheTimeout,
       "globalAttrSSLProxyFailOver": globalAttrSSLProxyFailOver,
       "globalAttrAkamaiConfigFile": globalAttrAkamaiConfigFile,
       "globalAttrSSLProxyServerSessionTimeout": globalAttrSSLProxyServerSessionTimeout,
       "globalAttrSSLProxyServerSessionCacheSize": globalAttrSSLProxyServerSessionCacheSize,
       "globalAttrIPForwarding": globalAttrIPForwarding,
       "globalAttrSSLProxyUncleanShutdown": globalAttrSSLProxyUncleanShutdown,
       "globalAttrSSLProxyStrictResume": globalAttrSSLProxyStrictResume,
       "globalAttrSelfConnTimeout": globalAttrSelfConnTimeout,
       "globalAttrFailoverPort": globalAttrFailoverPort,
       "globalStats": globalStats,
       "globalStatUptime": globalStatUptime,
       "globalStatBitsin": globalStatBitsin,
       "globalStatBitsinHi32": globalStatBitsinHi32,
       "globalStatBitsout": globalStatBitsout,
       "globalStatBitsoutHi32": globalStatBitsoutHi32,
       "globalStatPcktsin": globalStatPcktsin,
       "globalStatPcktsinHi32": globalStatPcktsinHi32,
       "globalStatPcktsout": globalStatPcktsout,
       "globalStatPcktsoutHi32": globalStatPcktsoutHi32,
       "globalStatCurrentConn": globalStatCurrentConn,
       "globalStatMaxConn": globalStatMaxConn,
       "globalStatTotalConn": globalStatTotalConn,
       "globalStatTimeouts": globalStatTimeouts,
       "globalStatMemoryPoolTotal": globalStatMemoryPoolTotal,
       "globalStatMemoryPoolUsed": globalStatMemoryPoolUsed,
       "globalStatStandBySharedDrop": globalStatStandBySharedDrop,
       "globalStatSelfTCPPortDeny": globalStatSelfTCPPortDeny,
       "globalStatSelfUDPPortDeny": globalStatSelfUDPPortDeny,
       "globalStatMaintenanceModeDeny": globalStatMaintenanceModeDeny,
       "globalStatVirtualServerUDPPortDeny": globalStatVirtualServerUDPPortDeny,
       "globalStatVirtualServerTCPPortDeny": globalStatVirtualServerTCPPortDeny,
       "globalStatVirtualServerDupSynSSL": globalStatVirtualServerDupSynSSL,
       "globalStatVirtualServerDupSynWrongDest": globalStatVirtualServerDupSynWrongDest,
       "globalStatVirtualServerDupSynNodeDown": globalStatVirtualServerDupSynNodeDown,
       "globalStatVirtualServerNonSynDeny": globalStatVirtualServerNonSynDeny,
       "globalStatMaxConnPortDeny": globalStatMaxConnPortDeny,
       "globalStatMaxConnVirtualAddressDeny": globalStatMaxConnVirtualAddressDeny,
       "globalStatMaxConnVirtualPathDeny": globalStatMaxConnVirtualPathDeny,
       "globalStatVirtualServerFragNoPort": globalStatVirtualServerFragNoPort,
       "globalStatVirtualServerFragNoConn": globalStatVirtualServerFragNoConn,
       "globalStatNoHandlerDeny": globalStatNoHandlerDeny,
       "globalStatTCPTimeouts": globalStatTCPTimeouts,
       "globalStatUDPTimeouts": globalStatUDPTimeouts,
       "globalStatIPTimeouts": globalStatIPTimeouts,
       "globalStatSSLTimeouts": globalStatSSLTimeouts,
       "globalStatPersistTimeouts": globalStatPersistTimeouts,
       "globalStatMultiProcessorMode": globalStatMultiProcessorMode,
       "globalStatCPUCount": globalStatCPUCount,
       "globalStatActiveCPUCount": globalStatActiveCPUCount,
       "globalStatANIPPercent": globalStatANIPPercent,
       "globalStatMaxANIPPercent": globalStatMaxANIPPercent,
       "globalStatMemoryErrors": globalStatMemoryErrors,
       "globalStatNoNodeErrors": globalStatNoNodeErrors,
       "globalStatMemoryInUse": globalStatMemoryInUse,
       "globalStatMemoryMaxUsed": globalStatMemoryMaxUsed,
       "globalStatMemoryCurrentSize": globalStatMemoryCurrentSize,
       "globalStatCPUTemperature": globalStatCPUTemperature,
       "globalStatFanSpeed": globalStatFanSpeed,
       "virtualAddress": virtualAddress,
       "virtualAddressNumber": virtualAddressNumber,
       "virtualAddressTable": virtualAddressTable,
       "virtualAddressEntry": virtualAddressEntry,
       "virtualAddressIpAddress": virtualAddressIpAddress,
       "virtualAddressStatus": virtualAddressStatus,
       "virtualAddressConnLimit": virtualAddressConnLimit,
       "virtualAddressNetmask": virtualAddressNetmask,
       "virtualAddressBroadcast": virtualAddressBroadcast,
       "virtualAddressInterface": virtualAddressInterface,
       "virtualAddressFailoverFlags": virtualAddressFailoverFlags,
       "virtualAddressOctetsIn": virtualAddressOctetsIn,
       "virtualAddressOctetsOut": virtualAddressOctetsOut,
       "virtualAddressPacketsIn": virtualAddressPacketsIn,
       "virtualAddressPacketsOut": virtualAddressPacketsOut,
       "virtualAddressCurrentConn": virtualAddressCurrentConn,
       "virtualAddressMaxConn": virtualAddressMaxConn,
       "virtualAddressTotalConn": virtualAddressTotalConn,
       "virtualAddressOctetsInHi32": virtualAddressOctetsInHi32,
       "virtualAddressOctetsOutHi32": virtualAddressOctetsOutHi32,
       "virtualAddressPacketsInHi32": virtualAddressPacketsInHi32,
       "virtualAddressPacketsOutHi32": virtualAddressPacketsOutHi32,
       "virtualAddressUnitId": virtualAddressUnitId,
       "virtualServer": virtualServer,
       "virtualServerNumber": virtualServerNumber,
       "virtualServerTable": virtualServerTable,
       "virtualServerEntry": virtualServerEntry,
       "virtualServerIpAddress": virtualServerIpAddress,
       "virtualServerPort": virtualServerPort,
       "virtualServerStatus": virtualServerStatus,
       "virtualServerConnLimit": virtualServerConnLimit,
       "virtualServerAppProtocol": virtualServerAppProtocol,
       "virtualServerAppProtocolTimeout": virtualServerAppProtocolTimeout,
       "virtualServerAppProtocolReaper": virtualServerAppProtocolReaper,
       "virtualServerPersistTimeout": virtualServerPersistTimeout,
       "virtualServerPersistMask": virtualServerPersistMask,
       "virtualServerSticky": virtualServerSticky,
       "virtualServerStickyMask": virtualServerStickyMask,
       "virtualServerFailoverFlags": virtualServerFailoverFlags,
       "virtualServerOctetsIn": virtualServerOctetsIn,
       "virtualServerOctetsOut": virtualServerOctetsOut,
       "virtualServerPacketsIn": virtualServerPacketsIn,
       "virtualServerPacketsOut": virtualServerPacketsOut,
       "virtualServerCurrentConn": virtualServerCurrentConn,
       "virtualServerMaxConn": virtualServerMaxConn,
       "virtualServerTotalConn": virtualServerTotalConn,
       "virtualServerSslNew": virtualServerSslNew,
       "virtualServerSslHits": virtualServerSslHits,
       "virtualServerSslTimeouts": virtualServerSslTimeouts,
       "virtualServerSslMisses": virtualServerSslMisses,
       "virtualServerOctetsInHi32": virtualServerOctetsInHi32,
       "virtualServerOctetsOutHi32": virtualServerOctetsOutHi32,
       "virtualServerPacketsInHi32": virtualServerPacketsInHi32,
       "virtualServerPacketsOutHi32": virtualServerPacketsOutHi32,
       "virtualServerCookieMethod": virtualServerCookieMethod,
       "virtualServerRule": virtualServerRule,
       "virtualServerPool": virtualServerPool,
       "virtualServerARPEnabled": virtualServerARPEnabled,
       "virtualServerLastHopPool": virtualServerLastHopPool,
       "virtualServerTranslateAddress": virtualServerTranslateAddress,
       "virtualServerTranslatePort": virtualServerTranslatePort,
       "virtualServerSvcDownReset": virtualServerSvcDownReset,
       "virtualServerMayUseProxy": virtualServerMayUseProxy,
       "virtualServerAccelerate": virtualServerAccelerate,
       "snat": snat,
       "snatTransTable": snatTransTable,
       "snatTransEntry": snatTransEntry,
       "snatTransEnabled": snatTransEnabled,
       "snatTransAddr": snatTransAddr,
       "snatTransIface": snatTransIface,
       "snatTransNetmask": snatTransNetmask,
       "snatTransBroadcast": snatTransBroadcast,
       "snatTransSecsCollectingStats": snatTransSecsCollectingStats,
       "snatTransBitsIn": snatTransBitsIn,
       "snatTransBitsOut": snatTransBitsOut,
       "snatTransPktsIn": snatTransPktsIn,
       "snatTransPktsOut": snatTransPktsOut,
       "snatTransCurrConns": snatTransCurrConns,
       "snatTransMaxConns": snatTransMaxConns,
       "snatTransTotalConns": snatTransTotalConns,
       "snatTransBitsInHi32": snatTransBitsInHi32,
       "snatTransBitsOutHi32": snatTransBitsOutHi32,
       "snatTransPktsInHi32": snatTransPktsInHi32,
       "snatTransPktsOutHi32": snatTransPktsOutHi32,
       "snatTransLastTransPort": snatTransLastTransPort,
       "snatTransUnitId": snatTransUnitId,
       "snatTransVLANs": snatTransVLANs,
       "snatTransServices": snatTransServices,
       "snatOrigTable": snatOrigTable,
       "snatOrigEntry": snatOrigEntry,
       "snatOrigEnabled": snatOrigEnabled,
       "snatOrigAddr": snatOrigAddr,
       "snatOrigConnLimit": snatOrigConnLimit,
       "snatOrigTransAddr": snatOrigTransAddr,
       "snatOrigTcpIdleTimeout": snatOrigTcpIdleTimeout,
       "snatOrigUdpIdleTimeout": snatOrigUdpIdleTimeout,
       "snatOrigStatsZeroTime": snatOrigStatsZeroTime,
       "snatOrigSecsCollectingStats": snatOrigSecsCollectingStats,
       "snatOrigBitsIn": snatOrigBitsIn,
       "snatOrigBitsOut": snatOrigBitsOut,
       "snatOrigPktsIn": snatOrigPktsIn,
       "snatOrigPktsOut": snatOrigPktsOut,
       "snatOrigCurrConns": snatOrigCurrConns,
       "snatOrigMaxConns": snatOrigMaxConns,
       "snatOrigTotalConns": snatOrigTotalConns,
       "snatOrigBitsInHi32": snatOrigBitsInHi32,
       "snatOrigBitsOutHi32": snatOrigBitsOutHi32,
       "snatOrigPktsInHi32": snatOrigPktsInHi32,
       "snatOrigPktsOutHi32": snatOrigPktsOutHi32,
       "snatOrigLastTransPort": snatOrigLastTransPort,
       "interface": interface,
       "interfaceNumber": interfaceNumber,
       "interfaceTable": interfaceTable,
       "interfaceEntry": interfaceEntry,
       "interfaceName": interfaceName,
       "interfaceIpAddresses": interfaceIpAddresses,
       "interfaceDestination": interfaceDestination,
       "interfaceSource": interfaceSource,
       "interfaceTimeout": interfaceTimeout,
       "interfaceArmed": interfaceArmed,
       "interfaceVLANSEnabled": interfaceVLANSEnabled,
       "interfaceMasqueradeAddress": interfaceMasqueradeAddress,
       "interfaceLastTimeChanged": interfaceLastTimeChanged,
       "interfaceSpeed": interfaceSpeed,
       "interfaceFullDuplex": interfaceFullDuplex,
       "interfaceMediaTypeActive": interfaceMediaTypeActive,
       "interfaceMediaDuplexActive": interfaceMediaDuplexActive,
       "interfaceMediaStatus": interfaceMediaStatus,
       "interfaceMediaType": interfaceMediaType,
       "interfaceMediaDuplex": interfaceMediaDuplex,
       "interfaceMTU": interfaceMTU,
       "ifaddress": ifaddress,
       "ifaddressNumber": ifaddressNumber,
       "ifaddressTable": ifaddressTable,
       "ifaddressEntry": ifaddressEntry,
       "ifaddressIpAddress": ifaddressIpAddress,
       "ifaddressInterfaceName": ifaddressInterfaceName,
       "ifaddressNetmask": ifaddressNetmask,
       "ifaddressBroadcast": ifaddressBroadcast,
       "ifaddressType": ifaddressType,
       "ifaddressUnitId": ifaddressUnitId,
       "ifaddressVLANTag": ifaddressVLANTag,
       "pool": pool,
       "poolNumber": poolNumber,
       "poolTable": poolTable,
       "poolEntry": poolEntry,
       "poolName": poolName,
       "poolLBMode": poolLBMode,
       "poolDependent": poolDependent,
       "poolMemberQty": poolMemberQty,
       "poolBitsin": poolBitsin,
       "poolBitsout": poolBitsout,
       "poolBitsinHi32": poolBitsinHi32,
       "poolBitsoutHi32": poolBitsoutHi32,
       "poolPktsin": poolPktsin,
       "poolPktsout": poolPktsout,
       "poolPktsinHi32": poolPktsinHi32,
       "poolPktsoutHi32": poolPktsoutHi32,
       "poolMaxConn": poolMaxConn,
       "poolCurrentConn": poolCurrentConn,
       "poolTotalConn": poolTotalConn,
       "poolPersistMode": poolPersistMode,
       "poolSSLTimeout": poolSSLTimeout,
       "poolSimpleTimeout": poolSimpleTimeout,
       "poolSimpleMask": poolSimpleMask,
       "poolStickyMask": poolStickyMask,
       "poolCookieMode": poolCookieMode,
       "poolCookieExpiration": poolCookieExpiration,
       "poolCookieHashName": poolCookieHashName,
       "poolCookieHashOffset": poolCookieHashOffset,
       "poolCookieHashLength": poolCookieHashLength,
       "poolMinActiveMembers": poolMinActiveMembers,
       "poolActiveMemberCount": poolActiveMemberCount,
       "poolPersistMirror": poolPersistMirror,
       "poolFallbackHost": poolFallbackHost,
       "poolMember": poolMember,
       "poolMemberNumber": poolMemberNumber,
       "poolMemberTable": poolMemberTable,
       "poolMemberEntry": poolMemberEntry,
       "poolMemberPoolName": poolMemberPoolName,
       "poolMemberIpAddress": poolMemberIpAddress,
       "poolMemberPort": poolMemberPort,
       "poolMemberMaintenance": poolMemberMaintenance,
       "poolMemberRatio": poolMemberRatio,
       "poolMemberPriority": poolMemberPriority,
       "poolMemberWeight": poolMemberWeight,
       "poolMemberRipeness": poolMemberRipeness,
       "poolMemberBitsin": poolMemberBitsin,
       "poolMemberBitsout": poolMemberBitsout,
       "poolMemberBitsinHi32": poolMemberBitsinHi32,
       "poolMemberBitsoutHi32": poolMemberBitsoutHi32,
       "poolMemberPktsin": poolMemberPktsin,
       "poolMemberPktsout": poolMemberPktsout,
       "poolMemberPktsinHi32": poolMemberPktsinHi32,
       "poolMemberPktsoutHi32": poolMemberPktsoutHi32,
       "poolMemberConnLimit": poolMemberConnLimit,
       "poolMemberMaxConn": poolMemberMaxConn,
       "poolMemberCurrentConn": poolMemberCurrentConn,
       "poolMemberTotalConn": poolMemberTotalConn,
       "poolMemberStatus": poolMemberStatus,
       "poolMemberIpStatus": poolMemberIpStatus,
       "sslProxy": sslProxy,
       "sslProxyNumber": sslProxyNumber,
       "sslProxyTable": sslProxyTable,
       "sslProxyEntry": sslProxyEntry,
       "sslProxyOrigIpAddress": sslProxyOrigIpAddress,
       "sslProxyOrigPort": sslProxyOrigPort,
       "sslProxyDestIpAddress": sslProxyDestIpAddress,
       "sslProxyDestPort": sslProxyDestPort,
       "sslProxyNetmask": sslProxyNetmask,
       "sslProxyBroadcast": sslProxyBroadcast,
       "sslProxyUnitId": sslProxyUnitId,
       "sslProxyEnabled": sslProxyEnabled,
       "sslProxyInterfaceName": sslProxyInterfaceName,
       "sslProxyLastHopPool": sslProxyLastHopPool,
       "sslProxyVLANs": sslProxyVLANs,
       "sslProxyLocalTarget": sslProxyLocalTarget,
       "sslProxyAkamaize": sslProxyAkamaize,
       "sslProxyUseSSL": sslProxyUseSSL,
       "sslProxyBitsin": sslProxyBitsin,
       "sslProxyBitsout": sslProxyBitsout,
       "sslProxyBitsinHi32": sslProxyBitsinHi32,
       "sslProxyBitsoutHi32": sslProxyBitsoutHi32,
       "sslProxyPktsin": sslProxyPktsin,
       "sslProxyPktsout": sslProxyPktsout,
       "sslProxyPktsinHi32": sslProxyPktsinHi32,
       "sslProxyPktsoutHi32": sslProxyPktsoutHi32,
       "sslProxyConnLimit": sslProxyConnLimit,
       "sslProxyMaxConn": sslProxyMaxConn,
       "sslProxyCurrentConn": sslProxyCurrentConn,
       "sslProxyTotalConn": sslProxyTotalConn,
       "sslProxyUseServerSSL": sslProxyUseServerSSL,
       "sslProxyArpEnabled": sslProxyArpEnabled,
       "sslProxyHTTPHeaderToAdd": sslProxyHTTPHeaderToAdd,
       "sslProxyInsertClientCipher": sslProxyInsertClientCipher,
       "sslProxyRewriteRedirects": sslProxyRewriteRedirects,
       "sslProxyClientInvalidVersions": sslProxyClientInvalidVersions,
       "sslProxyServerInvalidVersions": sslProxyServerInvalidVersions,
       "sslProxyClientCertificate": sslProxyClientCertificate,
       "sslProxyVerifyClientOnce": sslProxyVerifyClientOnce,
       "sslProxyVerifyClientDepth": sslProxyVerifyClientDepth,
       "sslProxyClientSessionCacheTimeout": sslProxyClientSessionCacheTimeout,
       "sslProxyClientSessionCacheSize": sslProxyClientSessionCacheSize,
       "sslProxyChainFileName": sslProxyChainFileName,
       "sslProxyServerChainFileName": sslProxyServerChainFileName,
       "sslProxyCAFileFileName": sslProxyCAFileFileName,
       "sslProxyServerCAFileFileName": sslProxyServerCAFileFileName,
       "sslProxyCAPathFileName": sslProxyCAPathFileName,
       "sslProxyServerCAPathFileName": sslProxyServerCAPathFileName,
       "sslProxyCRLFileFileName": sslProxyCRLFileFileName,
       "sslProxyServerCRLFileFileName": sslProxyServerCRLFileFileName,
       "sslProxyCRLPathFileName": sslProxyCRLPathFileName,
       "sslProxyServerCRLPathFileName": sslProxyServerCRLPathFileName,
       "sslProxyClientCertCAFileFilenName": sslProxyClientCertCAFileFilenName,
       "sslProxyInsertClientSessionID": sslProxyInsertClientSessionID,
       "sslProxyInsertClientIPAddrPort": sslProxyInsertClientIPAddrPort,
       "sslProxyServerCertificate": sslProxyServerCertificate,
       "sslProxyVerifyServerDepth": sslProxyVerifyServerDepth,
       "sslProxyTCPKeepAlivesEnabled": sslProxyTCPKeepAlivesEnabled,
       "sslProxyServerTCPKeepAlivesEnabled": sslProxyServerTCPKeepAlivesEnabled,
       "vlan": vlan,
       "vlanNumber": vlanNumber,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanName": vlanName,
       "vlanID": vlanID,
       "vlanTag": vlanTag,
       "vlanAllowOtherProxyARP": vlanAllowOtherProxyARP,
       "vlanPortLockedDown": vlanPortLockedDown,
       "vlanTaggedPorts": vlanTaggedPorts,
       "vlanUntaggedPorts": vlanUntaggedPorts,
       "vlanSnatAutomap": vlanSnatAutomap,
       "vlanArmed": vlanArmed,
       "vlanTimeout": vlanTimeout,
       "selfIP": selfIP,
       "selfIPNumber": selfIPNumber,
       "selfIPTable": selfIPTable,
       "selfIPEntry": selfIPEntry,
       "selfIPAddress": selfIPAddress,
       "selfIPNetmask": selfIPNetmask,
       "selfIPBroadcast": selfIPBroadcast,
       "selfIPUnitID": selfIPUnitID,
       "selfIPVLAN": selfIPVLAN,
       "selfIPSnatAutomap": selfIPSnatAutomap,
       "selfIPIsFloating": selfIPIsFloating,
       "trunk": trunk,
       "trunkNumber": trunkNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkControllingInterface": trunkControllingInterface,
       "trunkInterfaces": trunkInterfaces,
       "trunkMediaSpeed": trunkMediaSpeed,
       "nodes": nodes,
       "nodesNumber": nodesNumber,
       "nodesTable": nodesTable,
       "nodesEntry": nodesEntry,
       "nodesIndex": nodesIndex,
       "nodesAddr": nodesAddr,
       "nodesPktsinLo32": nodesPktsinLo32,
       "nodesPktsinHi32": nodesPktsinHi32,
       "nodesPktsoutLo32": nodesPktsoutLo32,
       "nodesPktsoutHi32": nodesPktsoutHi32,
       "nodesBitsinLo32": nodesBitsinLo32,
       "nodesBitsinHi32": nodesBitsinHi32,
       "nodesBitsoutLo32": nodesBitsoutLo32,
       "nodesBitsoutHi32": nodesBitsoutHi32,
       "nodesCurrentConnections": nodesCurrentConnections,
       "nodesMaximumConnections": nodesMaximumConnections,
       "nodesConnectionLimit": nodesConnectionLimit,
       "nodesTotalConnections": nodesTotalConnections,
       "nodesEnabled": nodesEnabled,
       "nodesPingerState": nodesPingerState,
       "uptime": uptime,
       "contot": contot,
       "concur": concur,
       "conmax": conmax,
       "pktsin": pktsin,
       "pktsout": pktsout,
       "bitsin": bitsin,
       "bitsout": bitsout,
       "portdeny": portdeny,
       "droppedin": droppedin,
       "droppedout": droppedout,
       "active": active,
       "mirrorenabled": mirrorenabled,
       "resetcounters": resetcounters,
       "pktsinHi32": pktsinHi32,
       "pktsoutHi32": pktsoutHi32,
       "bitsinHi32": bitsinHi32,
       "bitsoutHi32": bitsoutHi32,
       "nodePing": nodePing,
       "nodeTimeout": nodeTimeout,
       "loadbalMode": loadbalMode,
       "watchDogArmed": watchDogArmed,
       "snatConnLimit": snatConnLimit,
       "snatTCPIdleTimeout": snatTCPIdleTimeout,
       "snatUDPIdleTimeout": snatUDPIdleTimeout,
       "gatewayFailsafe": gatewayFailsafe,
       "unitId": unitId,
       "memoryUsed": memoryUsed,
       "memoryTotal": memoryTotal,
       "cpuTemperature": cpuTemperature,
       "fanSpeed": fanSpeed,
       "multiprocessingMode": multiprocessingMode,
       "percentANIP": percentANIP,
       "cpuCount": cpuCount,
       "vaddress": vaddress,
       "vaddressNumber": vaddressNumber,
       "vaddressTable": vaddressTable,
       "vaddressEntry": vaddressEntry,
       "vaddressIndex": vaddressIndex,
       "vaddressDescr": vaddressDescr,
       "vaddressIpAddr": vaddressIpAddr,
       "vaddressPktsin": vaddressPktsin,
       "vaddressPktsout": vaddressPktsout,
       "vaddressBitsin": vaddressBitsin,
       "vaddressBitsout": vaddressBitsout,
       "vaddressConcur": vaddressConcur,
       "vaddressConmax": vaddressConmax,
       "vaddressConlimit": vaddressConlimit,
       "vaddressContot": vaddressContot,
       "vaddressStatus": vaddressStatus,
       "vaddressPktsinHi32": vaddressPktsinHi32,
       "vaddressPktsoutHi32": vaddressPktsoutHi32,
       "vaddressBitsinHi32": vaddressBitsinHi32,
       "vaddressBitsoutHi32": vaddressBitsoutHi32,
       "ndaddr": ndaddr,
       "ndaddrNumber": ndaddrNumber,
       "ndaddrTable": ndaddrTable,
       "ndaddrEntry": ndaddrEntry,
       "ndaddrIndex": ndaddrIndex,
       "ndaddrDescr": ndaddrDescr,
       "ndaddrIpAddr": ndaddrIpAddr,
       "ndaddrPktsin": ndaddrPktsin,
       "ndaddrPktsout": ndaddrPktsout,
       "ndaddrBitsin": ndaddrBitsin,
       "ndaddrBitsout": ndaddrBitsout,
       "ndaddrConcur": ndaddrConcur,
       "ndaddrConmax": ndaddrConmax,
       "ndaddrConlimit": ndaddrConlimit,
       "ndaddrContot": ndaddrContot,
       "ndaddrStatus": ndaddrStatus,
       "ndaddrPktsinHi32": ndaddrPktsinHi32,
       "ndaddrPktsoutHi32": ndaddrPktsoutHi32,
       "ndaddrBitsinHi32": ndaddrBitsinHi32,
       "ndaddrBitsoutHi32": ndaddrBitsoutHi32,
       "ndaddrMaintenance": ndaddrMaintenance,
       "ndaddrIsVirtual": ndaddrIsVirtual,
       "ndaddrRatio": ndaddrRatio,
       "ndaddrTotalRealMemory": ndaddrTotalRealMemory,
       "ndaddrAvailableRealMemory": ndaddrAvailableRealMemory,
       "ndaddrTotalDisk": ndaddrTotalDisk,
       "ndaddrAvailableDisk": ndaddrAvailableDisk,
       "ndaddrAvailableCPU": ndaddrAvailableCPU,
       "ndaddrDynamicRatio": ndaddrDynamicRatio,
       "ndaddrPingerState": ndaddrPingerState,
       "nat": nat,
       "natNumber": natNumber,
       "natTable": natTable,
       "natEntry": natEntry,
       "natIndex": natIndex,
       "natDescr": natDescr,
       "natIpAddrFR": natIpAddrFR,
       "natIpAddrTO": natIpAddrTO,
       "natPktsin": natPktsin,
       "natPktsout": natPktsout,
       "natBitsin": natBitsin,
       "natBitsout": natBitsout,
       "natPktsinHi32": natPktsinHi32,
       "natPktsoutHi32": natPktsoutHi32,
       "natBitsinHi32": natBitsinHi32,
       "natBitsoutHi32": natBitsoutHi32,
       "natOutsideNetmask": natOutsideNetmask,
       "natOutsideBroadcast": natOutsideBroadcast,
       "natInterface": natInterface,
       "natUnitId": natUnitId,
       "natVLANs": natVLANs,
       "natARPEnabled": natARPEnabled,
       "natEnabled": natEnabled,
       "natServices": natServices,
       "vport": vport,
       "vportNumber": vportNumber,
       "vportTable": vportTable,
       "vportEntry": vportEntry,
       "vportIndex": vportIndex,
       "vportPort": vportPort,
       "vportDescr": vportDescr,
       "vportPktsin": vportPktsin,
       "vportPktsout": vportPktsout,
       "vportBitsin": vportBitsin,
       "vportBitsout": vportBitsout,
       "vportConcur": vportConcur,
       "vportConmax": vportConmax,
       "vportConlimit": vportConlimit,
       "vportContot": vportContot,
       "vportReaped": vportReaped,
       "vportPktsinHi32": vportPktsinHi32,
       "vportPktsoutHi32": vportPktsoutHi32,
       "vportBitsinHi32": vportBitsinHi32,
       "vportBitsoutHi32": vportBitsoutHi32,
       "vportAllowed": vportAllowed,
       "vportTCPpersistence": vportTCPpersistence,
       "vportUDPpersistence": vportUDPpersistence,
       "vportIPpersistence": vportIPpersistence,
       "vportUDPEnabled": vportUDPEnabled,
       "member": member,
       "memberTable": memberTable,
       "memberEntry": memberEntry,
       "memberVirtualAddress": memberVirtualAddress,
       "memberVirtualAddressPort": memberVirtualAddressPort,
       "memberOrdinal": memberOrdinal,
       "memberAddress": memberAddress,
       "memberPort": memberPort,
       "memberStatus": memberStatus,
       "memberPktsin": memberPktsin,
       "memberPktsout": memberPktsout,
       "memberBitsin": memberBitsin,
       "memberBitsout": memberBitsout,
       "memberConcur": memberConcur,
       "memberConmax": memberConmax,
       "memberConlimit": memberConlimit,
       "memberContot": memberContot,
       "memberPktsinHi32": memberPktsinHi32,
       "memberPktsoutHi32": memberPktsoutHi32,
       "memberBitsinHi32": memberBitsinHi32,
       "memberBitsoutHi32": memberBitsoutHi32,
       "loadBalTrap": loadBalTrap,
       "loadBalTraps": loadBalTraps,
       "loadBalTrapMisc": loadBalTrapMisc,
       "loadBalTrapServiceDown": loadBalTrapServiceDown,
       "loadBalTrapServiceUP": loadBalTrapServiceUP,
       "loadBalTrapReset": loadBalTrapReset,
       "loadBalTrapDenial": loadBalTrapDenial,
       "loadBalTrapLogin": loadBalTrapLogin,
       "loadBalTrapRemoveUnit": loadBalTrapRemoveUnit,
       "loadBalTrapAddUnit": loadBalTrapAddUnit,
       "loadBalTrapMessage": loadBalTrapMessage,
       "ipAddressString": ipAddressString}
)
