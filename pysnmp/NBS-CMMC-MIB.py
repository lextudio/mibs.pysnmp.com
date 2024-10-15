# SNMP MIB module (NBS-CMMC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NBS-CMMC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:33 2024
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

nbsCmmcMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200)
)


# Types definitions



class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nbs_ObjectIdentity = ObjectIdentity
nbs = _Nbs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629)
)
if mibBuilder.loadTexts:
    nbs.setStatus("current")
_NbsCmmcObjects_ObjectIdentity = ObjectIdentity
nbsCmmcObjects = _NbsCmmcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 1)
)
if mibBuilder.loadTexts:
    nbsCmmcObjects.setStatus("current")
_NbsCmmcSystemGrp_ObjectIdentity = ObjectIdentity
nbsCmmcSystemGrp = _NbsCmmcSystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 2)
)
if mibBuilder.loadTexts:
    nbsCmmcSystemGrp.setStatus("current")


class _NbsCmmcSysFwDescr_Type(DisplayString):
    """Custom type nbsCmmcSysFwDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFwDescr_Type.__name__ = "DisplayString"
_NbsCmmcSysFwDescr_Object = MibScalar
nbsCmmcSysFwDescr = _NbsCmmcSysFwDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1),
    _NbsCmmcSysFwDescr_Type()
)
nbsCmmcSysFwDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFwDescr.setStatus("current")


class _NbsCmmcSysFwVers_Type(DisplayString):
    """Custom type nbsCmmcSysFwVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsCmmcSysFwVers_Type.__name__ = "DisplayString"
_NbsCmmcSysFwVers_Object = MibScalar
nbsCmmcSysFwVers = _NbsCmmcSysFwVers_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 2),
    _NbsCmmcSysFwVers_Type()
)
nbsCmmcSysFwVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFwVers.setStatus("current")


class _NbsCmmcSysRestart_Type(Integer32):
    """Custom type nbsCmmcSysRestart based on Integer32"""
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
        *(("coldRestart", 2),
          ("running", 1),
          ("upgrRestart", 4),
          ("warmRestart", 3))
    )


_NbsCmmcSysRestart_Type.__name__ = "Integer32"
_NbsCmmcSysRestart_Object = MibScalar
nbsCmmcSysRestart = _NbsCmmcSysRestart_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3),
    _NbsCmmcSysRestart_Type()
)
nbsCmmcSysRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysRestart.setStatus("current")
_NbsCmmcSysNumRestarts_Type = Counter32
_NbsCmmcSysNumRestarts_Object = MibScalar
nbsCmmcSysNumRestarts = _NbsCmmcSysNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 4),
    _NbsCmmcSysNumRestarts_Type()
)
nbsCmmcSysNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNumRestarts.setStatus("current")
_NbsCmmcSysErrUptime_Type = TimeTicks
_NbsCmmcSysErrUptime_Object = MibScalar
nbsCmmcSysErrUptime = _NbsCmmcSysErrUptime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 5),
    _NbsCmmcSysErrUptime_Type()
)
nbsCmmcSysErrUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysErrUptime.setStatus("current")


class _NbsCmmcSysSetNvramDefaults_Type(Integer32):
    """Custom type nbsCmmcSysSetNvramDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setDefaults", 1)
    )


_NbsCmmcSysSetNvramDefaults_Type.__name__ = "Integer32"
_NbsCmmcSysSetNvramDefaults_Object = MibScalar
nbsCmmcSysSetNvramDefaults = _NbsCmmcSysSetNvramDefaults_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 6),
    _NbsCmmcSysSetNvramDefaults_Type()
)
nbsCmmcSysSetNvramDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSetNvramDefaults.setStatus("current")


class _NbsCmmcSysSelftestLevel_Type(Integer32):
    """Custom type nbsCmmcSysSelftestLevel based on Integer32"""
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
        *(("ststDiagnostics", 4),
          ("ststLong", 3),
          ("ststNone", 1),
          ("ststShort", 2))
    )


_NbsCmmcSysSelftestLevel_Type.__name__ = "Integer32"
_NbsCmmcSysSelftestLevel_Object = MibScalar
nbsCmmcSysSelftestLevel = _NbsCmmcSysSelftestLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 7),
    _NbsCmmcSysSelftestLevel_Type()
)
nbsCmmcSysSelftestLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSelftestLevel.setStatus("deprecated")


class _NbsCmmcSysCurrentTime_Type(Unsigned32):
    """Custom type nbsCmmcSysCurrentTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2208988800, 4294967295),
    )


_NbsCmmcSysCurrentTime_Type.__name__ = "Unsigned32"
_NbsCmmcSysCurrentTime_Object = MibScalar
nbsCmmcSysCurrentTime = _NbsCmmcSysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 8),
    _NbsCmmcSysCurrentTime_Type()
)
nbsCmmcSysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysCurrentTime.setStatus("current")


class _NbsCmmcSysCurrentDateTime_Type(DisplayString):
    """Custom type nbsCmmcSysCurrentDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NbsCmmcSysCurrentDateTime_Type.__name__ = "DisplayString"
_NbsCmmcSysCurrentDateTime_Object = MibScalar
nbsCmmcSysCurrentDateTime = _NbsCmmcSysCurrentDateTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 9),
    _NbsCmmcSysCurrentDateTime_Type()
)
nbsCmmcSysCurrentDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysCurrentDateTime.setStatus("current")
_NbsCmmcSysNvramTable_Object = MibTable
nbsCmmcSysNvramTable = _NbsCmmcSysNvramTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 10)
)
if mibBuilder.loadTexts:
    nbsCmmcSysNvramTable.setStatus("current")
_NbsCmmcSysNvramEntry_Object = MibTableRow
nbsCmmcSysNvramEntry = _NbsCmmcSysNvramEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 10, 1)
)
nbsCmmcSysNvramEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysNvramIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysNvramEntry.setStatus("current")
_NbsCmmcSysNvramIndex_Type = Integer32
_NbsCmmcSysNvramIndex_Object = MibTableColumn
nbsCmmcSysNvramIndex = _NbsCmmcSysNvramIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 10, 1, 1),
    _NbsCmmcSysNvramIndex_Type()
)
nbsCmmcSysNvramIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramIndex.setStatus("current")


class _NbsCmmcSysNvramBlock_Type(OctetString):
    """Custom type nbsCmmcSysNvramBlock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_NbsCmmcSysNvramBlock_Type.__name__ = "OctetString"
_NbsCmmcSysNvramBlock_Object = MibTableColumn
nbsCmmcSysNvramBlock = _NbsCmmcSysNvramBlock_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 10, 1, 2),
    _NbsCmmcSysNvramBlock_Type()
)
nbsCmmcSysNvramBlock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramBlock.setStatus("current")


class _NbsCmmcSysWriteConfig_Type(Integer32):
    """Custom type nbsCmmcSysWriteConfig based on Integer32"""
    defaultValue = 2

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
        *(("copyTempFile", 4),
          ("notSupported", 1),
          ("supported", 2),
          ("write", 3))
    )


_NbsCmmcSysWriteConfig_Type.__name__ = "Integer32"
_NbsCmmcSysWriteConfig_Object = MibScalar
nbsCmmcSysWriteConfig = _NbsCmmcSysWriteConfig_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 11),
    _NbsCmmcSysWriteConfig_Type()
)
nbsCmmcSysWriteConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysWriteConfig.setStatus("current")
_NbsCmmcSysUpgrade_Type = DisplayString
_NbsCmmcSysUpgrade_Object = MibScalar
nbsCmmcSysUpgrade = _NbsCmmcSysUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 12),
    _NbsCmmcSysUpgrade_Type()
)
nbsCmmcSysUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysUpgrade.setStatus("deprecated")


class _NbsCmmcSysLoginIdleTimeout_Type(Integer32):
    """Custom type nbsCmmcSysLoginIdleTimeout based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400000),
    )


_NbsCmmcSysLoginIdleTimeout_Type.__name__ = "Integer32"
_NbsCmmcSysLoginIdleTimeout_Object = MibScalar
nbsCmmcSysLoginIdleTimeout = _NbsCmmcSysLoginIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 13),
    _NbsCmmcSysLoginIdleTimeout_Type()
)
nbsCmmcSysLoginIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLoginIdleTimeout.setStatus("current")


class _NbsCmmcSysDiscovery_Type(Integer32):
    """Custom type nbsCmmcSysDiscovery based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysDiscovery_Type.__name__ = "Integer32"
_NbsCmmcSysDiscovery_Object = MibScalar
nbsCmmcSysDiscovery = _NbsCmmcSysDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 14),
    _NbsCmmcSysDiscovery_Type()
)
nbsCmmcSysDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysDiscovery.setStatus("current")
_NbsCmmcSysDiscoveryHostTable_Object = MibTable
nbsCmmcSysDiscoveryHostTable = _NbsCmmcSysDiscoveryHostTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 15)
)
if mibBuilder.loadTexts:
    nbsCmmcSysDiscoveryHostTable.setStatus("current")
_NbsCmmcSysDiscoveryHostEntry_Object = MibTableRow
nbsCmmcSysDiscoveryHostEntry = _NbsCmmcSysDiscoveryHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 15, 1)
)
nbsCmmcSysDiscoveryHostEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysDiscoveryHostMACAddress"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysDiscoveryHostEntry.setStatus("current")


class _NbsCmmcSysDiscoveryHostMACAddress_Type(OctetString):
    """Custom type nbsCmmcSysDiscoveryHostMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_NbsCmmcSysDiscoveryHostMACAddress_Type.__name__ = "OctetString"
_NbsCmmcSysDiscoveryHostMACAddress_Object = MibTableColumn
nbsCmmcSysDiscoveryHostMACAddress = _NbsCmmcSysDiscoveryHostMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 15, 1, 1),
    _NbsCmmcSysDiscoveryHostMACAddress_Type()
)
nbsCmmcSysDiscoveryHostMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysDiscoveryHostMACAddress.setStatus("current")


class _NbsCmmcSysDiscoveryHostDistance_Type(Integer32):
    """Custom type nbsCmmcSysDiscoveryHostDistance based on Integer32"""
    defaultValue = 0


_NbsCmmcSysDiscoveryHostDistance_Object = MibTableColumn
nbsCmmcSysDiscoveryHostDistance = _NbsCmmcSysDiscoveryHostDistance_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 15, 1, 2),
    _NbsCmmcSysDiscoveryHostDistance_Type()
)
nbsCmmcSysDiscoveryHostDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysDiscoveryHostDistance.setStatus("current")


class _NbsCmmcSysDiscoveryHostIPAddress_Type(IpAddress):
    """Custom type nbsCmmcSysDiscoveryHostIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_NbsCmmcSysDiscoveryHostIPAddress_Object = MibTableColumn
nbsCmmcSysDiscoveryHostIPAddress = _NbsCmmcSysDiscoveryHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 15, 1, 3),
    _NbsCmmcSysDiscoveryHostIPAddress_Type()
)
nbsCmmcSysDiscoveryHostIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysDiscoveryHostIPAddress.setStatus("current")


class _NbsCmmcSysLastSetFailure_Type(DisplayString):
    """Custom type nbsCmmcSysLastSetFailure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysLastSetFailure_Type.__name__ = "DisplayString"
_NbsCmmcSysLastSetFailure_Object = MibScalar
nbsCmmcSysLastSetFailure = _NbsCmmcSysLastSetFailure_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 16),
    _NbsCmmcSysLastSetFailure_Type()
)
nbsCmmcSysLastSetFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLastSetFailure.setStatus("current")


class _NbsCmmcSysTimeProtocol_Type(Integer32):
    """Custom type nbsCmmcSysTimeProtocol based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysTimeProtocol_Type.__name__ = "Integer32"
_NbsCmmcSysTimeProtocol_Object = MibScalar
nbsCmmcSysTimeProtocol = _NbsCmmcSysTimeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 17),
    _NbsCmmcSysTimeProtocol_Type()
)
nbsCmmcSysTimeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeProtocol.setStatus("current")
_NbsCmmcSysTimeServer_Type = IpAddress
_NbsCmmcSysTimeServer_Object = MibScalar
nbsCmmcSysTimeServer = _NbsCmmcSysTimeServer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 18),
    _NbsCmmcSysTimeServer_Type()
)
nbsCmmcSysTimeServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeServer.setStatus("current")
_NbsCmmcSysFirmwareTable_Object = MibTable
nbsCmmcSysFirmwareTable = _NbsCmmcSysFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19)
)
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareTable.setStatus("current")
_NbsCmmcSysFirmwareEntry_Object = MibTableRow
nbsCmmcSysFirmwareEntry = _NbsCmmcSysFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1)
)
nbsCmmcSysFirmwareEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysFirmwareIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareEntry.setStatus("current")
_NbsCmmcSysFirmwareIndex_Type = Integer32
_NbsCmmcSysFirmwareIndex_Object = MibTableColumn
nbsCmmcSysFirmwareIndex = _NbsCmmcSysFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 1),
    _NbsCmmcSysFirmwareIndex_Type()
)
nbsCmmcSysFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareIndex.setStatus("current")


class _NbsCmmcSysFirmwareDescr_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFirmwareDescr_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareDescr_Object = MibTableColumn
nbsCmmcSysFirmwareDescr = _NbsCmmcSysFirmwareDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 2),
    _NbsCmmcSysFirmwareDescr_Type()
)
nbsCmmcSysFirmwareDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareDescr.setStatus("current")


class _NbsCmmcSysFirmwareFilename_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFirmwareFilename_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareFilename_Object = MibTableColumn
nbsCmmcSysFirmwareFilename = _NbsCmmcSysFirmwareFilename_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 3),
    _NbsCmmcSysFirmwareFilename_Type()
)
nbsCmmcSysFirmwareFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareFilename.setStatus("current")
_NbsCmmcSysFirmwareSize_Type = Integer32
_NbsCmmcSysFirmwareSize_Object = MibTableColumn
nbsCmmcSysFirmwareSize = _NbsCmmcSysFirmwareSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 4),
    _NbsCmmcSysFirmwareSize_Type()
)
nbsCmmcSysFirmwareSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareSize.setStatus("current")
_NbsCmmcSysFirmwareMTime_Type = Integer32
_NbsCmmcSysFirmwareMTime_Object = MibTableColumn
nbsCmmcSysFirmwareMTime = _NbsCmmcSysFirmwareMTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 5),
    _NbsCmmcSysFirmwareMTime_Type()
)
nbsCmmcSysFirmwareMTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareMTime.setStatus("current")


class _NbsCmmcSysFirmwareVersion_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFirmwareVersion_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareVersion_Object = MibTableColumn
nbsCmmcSysFirmwareVersion = _NbsCmmcSysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 6),
    _NbsCmmcSysFirmwareVersion_Type()
)
nbsCmmcSysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareVersion.setStatus("current")


class _NbsCmmcSysFirmwareDate_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NbsCmmcSysFirmwareDate_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareDate_Object = MibTableColumn
nbsCmmcSysFirmwareDate = _NbsCmmcSysFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 7),
    _NbsCmmcSysFirmwareDate_Type()
)
nbsCmmcSysFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareDate.setStatus("current")


class _NbsCmmcSysFirmwareType_Type(Integer32):
    """Custom type nbsCmmcSysFirmwareType based on Integer32"""
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
        *(("chassis", 2),
          ("deleted", 5),
          ("invalid", 1),
          ("port", 4),
          ("slot", 3))
    )


_NbsCmmcSysFirmwareType_Type.__name__ = "Integer32"
_NbsCmmcSysFirmwareType_Object = MibTableColumn
nbsCmmcSysFirmwareType = _NbsCmmcSysFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 8),
    _NbsCmmcSysFirmwareType_Type()
)
nbsCmmcSysFirmwareType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareType.setStatus("current")


class _NbsCmmcSysFirmwareIDCs_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareIDCs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFirmwareIDCs_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareIDCs_Object = MibTableColumn
nbsCmmcSysFirmwareIDCs = _NbsCmmcSysFirmwareIDCs_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 9),
    _NbsCmmcSysFirmwareIDCs_Type()
)
nbsCmmcSysFirmwareIDCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareIDCs.setStatus("current")


class _NbsCmmcSysFirmwareCksum_Type(Unsigned32):
    """Custom type nbsCmmcSysFirmwareCksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NbsCmmcSysFirmwareCksum_Type.__name__ = "Unsigned32"
_NbsCmmcSysFirmwareCksum_Object = MibTableColumn
nbsCmmcSysFirmwareCksum = _NbsCmmcSysFirmwareCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 19, 1, 10),
    _NbsCmmcSysFirmwareCksum_Type()
)
nbsCmmcSysFirmwareCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareCksum.setStatus("current")


class _NbsCmmcSysTimeZone_Type(Integer32):
    """Custom type nbsCmmcSysTimeZone based on Integer32"""
    defaultValue = 14

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
              26)
        )
    )
    namedValues = NamedValues(
        *(("gmt", 14),
          ("gmtMinus0100", 13),
          ("gmtMinus0200", 12),
          ("gmtMinus0300", 11),
          ("gmtMinus0400", 10),
          ("gmtMinus0500", 9),
          ("gmtMinus0600", 8),
          ("gmtMinus0700", 7),
          ("gmtMinus0800", 6),
          ("gmtMinus0900", 5),
          ("gmtMinus1000", 4),
          ("gmtMinus1100", 3),
          ("gmtMinus1200", 2),
          ("gmtPlus0100", 15),
          ("gmtPlus0200", 16),
          ("gmtPlus0300", 17),
          ("gmtPlus0400", 18),
          ("gmtPlus0500", 19),
          ("gmtPlus0600", 20),
          ("gmtPlus0700", 21),
          ("gmtPlus0800", 22),
          ("gmtPlus0900", 23),
          ("gmtPlus1000", 24),
          ("gmtPlus1100", 25),
          ("gmtPlus1200", 26),
          ("notSupported", 1))
    )


_NbsCmmcSysTimeZone_Type.__name__ = "Integer32"
_NbsCmmcSysTimeZone_Object = MibScalar
nbsCmmcSysTimeZone = _NbsCmmcSysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 20),
    _NbsCmmcSysTimeZone_Type()
)
nbsCmmcSysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZone.setStatus("current")


class _NbsCmmcSysSnmpV1_Type(Integer32):
    """Custom type nbsCmmcSysSnmpV1 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysSnmpV1_Type.__name__ = "Integer32"
_NbsCmmcSysSnmpV1_Object = MibScalar
nbsCmmcSysSnmpV1 = _NbsCmmcSysSnmpV1_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 21),
    _NbsCmmcSysSnmpV1_Type()
)
nbsCmmcSysSnmpV1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSnmpV1.setStatus("current")


class _NbsCmmcSysSnmpV2c_Type(Integer32):
    """Custom type nbsCmmcSysSnmpV2c based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysSnmpV2c_Type.__name__ = "Integer32"
_NbsCmmcSysSnmpV2c_Object = MibScalar
nbsCmmcSysSnmpV2c = _NbsCmmcSysSnmpV2c_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 22),
    _NbsCmmcSysSnmpV2c_Type()
)
nbsCmmcSysSnmpV2c.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSnmpV2c.setStatus("current")


class _NbsCmmcSysSnmpV3_Type(Integer32):
    """Custom type nbsCmmcSysSnmpV3 based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysSnmpV3_Type.__name__ = "Integer32"
_NbsCmmcSysSnmpV3_Object = MibScalar
nbsCmmcSysSnmpV3 = _NbsCmmcSysSnmpV3_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 23),
    _NbsCmmcSysSnmpV3_Type()
)
nbsCmmcSysSnmpV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSnmpV3.setStatus("current")


class _NbsCmmcSysLmp_Type(Integer32):
    """Custom type nbsCmmcSysLmp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysLmp_Type.__name__ = "Integer32"
_NbsCmmcSysLmp_Object = MibScalar
nbsCmmcSysLmp = _NbsCmmcSysLmp_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 24),
    _NbsCmmcSysLmp_Type()
)
nbsCmmcSysLmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLmp.setStatus("current")


class _NbsCmmcSysLockTypes_Type(Integer32):
    """Custom type nbsCmmcSysLockTypes based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysLockTypes_Type.__name__ = "Integer32"
_NbsCmmcSysLockTypes_Object = MibScalar
nbsCmmcSysLockTypes = _NbsCmmcSysLockTypes_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 25),
    _NbsCmmcSysLockTypes_Type()
)
nbsCmmcSysLockTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLockTypes.setStatus("current")


class _NbsCmmcSysSerialTerminalType_Type(DisplayString):
    """Custom type nbsCmmcSysSerialTerminalType based on DisplayString"""
    defaultValue = OctetString("vt102")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysSerialTerminalType_Type.__name__ = "DisplayString"
_NbsCmmcSysSerialTerminalType_Object = MibScalar
nbsCmmcSysSerialTerminalType = _NbsCmmcSysSerialTerminalType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 26),
    _NbsCmmcSysSerialTerminalType_Type()
)
nbsCmmcSysSerialTerminalType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSerialTerminalType.setStatus("current")


class _NbsCmmcSysCrossConnect_Type(Integer32):
    """Custom type nbsCmmcSysCrossConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcSysCrossConnect_Type.__name__ = "Integer32"
_NbsCmmcSysCrossConnect_Object = MibScalar
nbsCmmcSysCrossConnect = _NbsCmmcSysCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 27),
    _NbsCmmcSysCrossConnect_Type()
)
nbsCmmcSysCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysCrossConnect.setStatus("current")


class _NbsCmmcSysCountersState_Type(Integer32):
    """Custom type nbsCmmcSysCountersState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsCmmcSysCountersState_Type.__name__ = "Integer32"
_NbsCmmcSysCountersState_Object = MibScalar
nbsCmmcSysCountersState = _NbsCmmcSysCountersState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 28),
    _NbsCmmcSysCountersState_Type()
)
nbsCmmcSysCountersState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysCountersState.setStatus("current")
_NbsCmmcSysProtoTableSize_Type = Unsigned32
_NbsCmmcSysProtoTableSize_Object = MibScalar
nbsCmmcSysProtoTableSize = _NbsCmmcSysProtoTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1001),
    _NbsCmmcSysProtoTableSize_Type()
)
nbsCmmcSysProtoTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysProtoTableSize.setStatus("current")
_NbsCmmcSysProtoTable_Object = MibTable
nbsCmmcSysProtoTable = _NbsCmmcSysProtoTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1002)
)
if mibBuilder.loadTexts:
    nbsCmmcSysProtoTable.setStatus("current")
_NbsCmmcSysProtoEntry_Object = MibTableRow
nbsCmmcSysProtoEntry = _NbsCmmcSysProtoEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1002, 1)
)
nbsCmmcSysProtoEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysProtoIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysProtoEntry.setStatus("current")
_NbsCmmcSysProtoIndex_Type = Unsigned32
_NbsCmmcSysProtoIndex_Object = MibTableColumn
nbsCmmcSysProtoIndex = _NbsCmmcSysProtoIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1002, 1, 1),
    _NbsCmmcSysProtoIndex_Type()
)
nbsCmmcSysProtoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysProtoIndex.setStatus("current")


class _NbsCmmcSysProtoFamily_Type(DisplayString):
    """Custom type nbsCmmcSysProtoFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 16),
    )


_NbsCmmcSysProtoFamily_Type.__name__ = "DisplayString"
_NbsCmmcSysProtoFamily_Object = MibTableColumn
nbsCmmcSysProtoFamily = _NbsCmmcSysProtoFamily_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1002, 1, 2),
    _NbsCmmcSysProtoFamily_Type()
)
nbsCmmcSysProtoFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysProtoFamily.setStatus("current")


class _NbsCmmcSysProtoRate_Type(DisplayString):
    """Custom type nbsCmmcSysProtoRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 30),
    )


_NbsCmmcSysProtoRate_Type.__name__ = "DisplayString"
_NbsCmmcSysProtoRate_Object = MibTableColumn
nbsCmmcSysProtoRate = _NbsCmmcSysProtoRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1002, 1, 3),
    _NbsCmmcSysProtoRate_Type()
)
nbsCmmcSysProtoRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysProtoRate.setStatus("current")
_NbsCmmcSysTimeZoneTableSize_Type = Unsigned32
_NbsCmmcSysTimeZoneTableSize_Object = MibScalar
nbsCmmcSysTimeZoneTableSize = _NbsCmmcSysTimeZoneTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1003),
    _NbsCmmcSysTimeZoneTableSize_Type()
)
nbsCmmcSysTimeZoneTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZoneTableSize.setStatus("current")
_NbsCmmcSysTimeZoneTable_Object = MibTable
nbsCmmcSysTimeZoneTable = _NbsCmmcSysTimeZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1004)
)
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZoneTable.setStatus("current")
_NbsCmmcSysTimeZoneEntry_Object = MibTableRow
nbsCmmcSysTimeZoneEntry = _NbsCmmcSysTimeZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1004, 1)
)
nbsCmmcSysTimeZoneEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysTimeZoneIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZoneEntry.setStatus("current")
_NbsCmmcSysTimeZoneIndex_Type = Unsigned32
_NbsCmmcSysTimeZoneIndex_Object = MibTableColumn
nbsCmmcSysTimeZoneIndex = _NbsCmmcSysTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1004, 1, 1),
    _NbsCmmcSysTimeZoneIndex_Type()
)
nbsCmmcSysTimeZoneIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZoneIndex.setStatus("current")


class _NbsCmmcSysTimeZoneName_Type(DisplayString):
    """Custom type nbsCmmcSysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 30),
    )


_NbsCmmcSysTimeZoneName_Type.__name__ = "DisplayString"
_NbsCmmcSysTimeZoneName_Object = MibTableColumn
nbsCmmcSysTimeZoneName = _NbsCmmcSysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1004, 1, 2),
    _NbsCmmcSysTimeZoneName_Type()
)
nbsCmmcSysTimeZoneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTimeZoneName.setStatus("current")
_NbsCmmcSysLoaderTableSize_Type = Integer32
_NbsCmmcSysLoaderTableSize_Object = MibScalar
nbsCmmcSysLoaderTableSize = _NbsCmmcSysLoaderTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1010),
    _NbsCmmcSysLoaderTableSize_Type()
)
nbsCmmcSysLoaderTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderTableSize.setStatus("current")
_NbsCmmcSysLoaderTable_Object = MibTable
nbsCmmcSysLoaderTable = _NbsCmmcSysLoaderTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011)
)
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderTable.setStatus("current")
_NbsCmmcSysLoaderEntry_Object = MibTableRow
nbsCmmcSysLoaderEntry = _NbsCmmcSysLoaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1)
)
nbsCmmcSysLoaderEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysLoaderIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderEntry.setStatus("current")


class _NbsCmmcSysLoaderIndex_Type(InterfaceIndex):
    """Custom type nbsCmmcSysLoaderIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000, 9999999),
    )


_NbsCmmcSysLoaderIndex_Type.__name__ = "InterfaceIndex"
_NbsCmmcSysLoaderIndex_Object = MibTableColumn
nbsCmmcSysLoaderIndex = _NbsCmmcSysLoaderIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 1),
    _NbsCmmcSysLoaderIndex_Type()
)
nbsCmmcSysLoaderIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderIndex.setStatus("current")
_NbsCmmcSysLoaderFileId_Type = Integer32
_NbsCmmcSysLoaderFileId_Object = MibTableColumn
nbsCmmcSysLoaderFileId = _NbsCmmcSysLoaderFileId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 2),
    _NbsCmmcSysLoaderFileId_Type()
)
nbsCmmcSysLoaderFileId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderFileId.setStatus("current")
_NbsCmmcSysLoaderProgress_Type = Integer32
_NbsCmmcSysLoaderProgress_Object = MibTableColumn
nbsCmmcSysLoaderProgress = _NbsCmmcSysLoaderProgress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 3),
    _NbsCmmcSysLoaderProgress_Type()
)
nbsCmmcSysLoaderProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderProgress.setStatus("current")


class _NbsCmmcSysLoaderStatus_Type(Integer32):
    """Custom type nbsCmmcSysLoaderStatus based on Integer32"""
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
        *(("aborted", 4),
          ("completed", 3),
          ("idle", 1),
          ("transferring", 2))
    )


_NbsCmmcSysLoaderStatus_Type.__name__ = "Integer32"
_NbsCmmcSysLoaderStatus_Object = MibTableColumn
nbsCmmcSysLoaderStatus = _NbsCmmcSysLoaderStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 4),
    _NbsCmmcSysLoaderStatus_Type()
)
nbsCmmcSysLoaderStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderStatus.setStatus("current")


class _NbsCmmcSysLoaderAbort_Type(Integer32):
    """Custom type nbsCmmcSysLoaderAbort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("abort", 3),
          ("notSupported", 1),
          ("supported", 2))
    )


_NbsCmmcSysLoaderAbort_Type.__name__ = "Integer32"
_NbsCmmcSysLoaderAbort_Object = MibTableColumn
nbsCmmcSysLoaderAbort = _NbsCmmcSysLoaderAbort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 5),
    _NbsCmmcSysLoaderAbort_Type()
)
nbsCmmcSysLoaderAbort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderAbort.setStatus("current")


class _NbsCmmcSysLoaderAck_Type(Integer32):
    """Custom type nbsCmmcSysLoaderAck based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acknowledge", 3),
          ("notSupported", 1),
          ("supported", 2))
    )


_NbsCmmcSysLoaderAck_Type.__name__ = "Integer32"
_NbsCmmcSysLoaderAck_Object = MibTableColumn
nbsCmmcSysLoaderAck = _NbsCmmcSysLoaderAck_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 6),
    _NbsCmmcSysLoaderAck_Type()
)
nbsCmmcSysLoaderAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderAck.setStatus("current")
_NbsCmmcSysLoaderFilename_Type = DisplayString
_NbsCmmcSysLoaderFilename_Object = MibTableColumn
nbsCmmcSysLoaderFilename = _NbsCmmcSysLoaderFilename_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1011, 1, 7),
    _NbsCmmcSysLoaderFilename_Type()
)
nbsCmmcSysLoaderFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLoaderFilename.setStatus("current")


class _NbsCmmcSysFirmwareURL_Type(DisplayString):
    """Custom type nbsCmmcSysFirmwareURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysFirmwareURL_Type.__name__ = "DisplayString"
_NbsCmmcSysFirmwareURL_Object = MibScalar
nbsCmmcSysFirmwareURL = _NbsCmmcSysFirmwareURL_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1020),
    _NbsCmmcSysFirmwareURL_Type()
)
nbsCmmcSysFirmwareURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareURL.setStatus("current")


class _NbsCmmcSysFirmwareURLStatus_Type(Integer32):
    """Custom type nbsCmmcSysFirmwareURLStatus based on Integer32"""
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
        *(("completed", 4),
          ("failed", 5),
          ("idle", 2),
          ("notSupported", 1),
          ("transferring", 3))
    )


_NbsCmmcSysFirmwareURLStatus_Type.__name__ = "Integer32"
_NbsCmmcSysFirmwareURLStatus_Object = MibScalar
nbsCmmcSysFirmwareURLStatus = _NbsCmmcSysFirmwareURLStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 1021),
    _NbsCmmcSysFirmwareURLStatus_Type()
)
nbsCmmcSysFirmwareURLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysFirmwareURLStatus.setStatus("current")
_NbsCmmcSysNVAreaTableSize_Type = Integer32
_NbsCmmcSysNVAreaTableSize_Object = MibScalar
nbsCmmcSysNVAreaTableSize = _NbsCmmcSysNVAreaTableSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3000),
    _NbsCmmcSysNVAreaTableSize_Type()
)
nbsCmmcSysNVAreaTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaTableSize.setStatus("current")
_NbsCmmcSysNVAreaTable_Object = MibTable
nbsCmmcSysNVAreaTable = _NbsCmmcSysNVAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001)
)
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaTable.setStatus("current")
_NbsCmmcSysNVAreaEntry_Object = MibTableRow
nbsCmmcSysNVAreaEntry = _NbsCmmcSysNVAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1)
)
nbsCmmcSysNVAreaEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysNVAreaIfIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcSysNVAreaBank"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaEntry.setStatus("current")


class _NbsCmmcSysNVAreaIfIndex_Type(InterfaceIndex):
    """Custom type nbsCmmcSysNVAreaIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100000, 9999999),
    )


_NbsCmmcSysNVAreaIfIndex_Type.__name__ = "InterfaceIndex"
_NbsCmmcSysNVAreaIfIndex_Object = MibTableColumn
nbsCmmcSysNVAreaIfIndex = _NbsCmmcSysNVAreaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 1),
    _NbsCmmcSysNVAreaIfIndex_Type()
)
nbsCmmcSysNVAreaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaIfIndex.setStatus("current")
_NbsCmmcSysNVAreaBank_Type = Integer32
_NbsCmmcSysNVAreaBank_Object = MibTableColumn
nbsCmmcSysNVAreaBank = _NbsCmmcSysNVAreaBank_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 2),
    _NbsCmmcSysNVAreaBank_Type()
)
nbsCmmcSysNVAreaBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaBank.setStatus("current")


class _NbsCmmcSysNVAreaStatus_Type(Integer32):
    """Custom type nbsCmmcSysNVAreaStatus based on Integer32"""
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
        *(("backup", 3),
          ("busy", 5),
          ("erased", 4),
          ("invalid", 1),
          ("primary", 2))
    )


_NbsCmmcSysNVAreaStatus_Type.__name__ = "Integer32"
_NbsCmmcSysNVAreaStatus_Object = MibTableColumn
nbsCmmcSysNVAreaStatus = _NbsCmmcSysNVAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 3),
    _NbsCmmcSysNVAreaStatus_Type()
)
nbsCmmcSysNVAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaStatus.setStatus("current")


class _NbsCmmcSysNVAreaDescr_Type(DisplayString):
    """Custom type nbsCmmcSysNVAreaDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysNVAreaDescr_Type.__name__ = "DisplayString"
_NbsCmmcSysNVAreaDescr_Object = MibTableColumn
nbsCmmcSysNVAreaDescr = _NbsCmmcSysNVAreaDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 4),
    _NbsCmmcSysNVAreaDescr_Type()
)
nbsCmmcSysNVAreaDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaDescr.setStatus("current")


class _NbsCmmcSysNVAreaVersion_Type(DisplayString):
    """Custom type nbsCmmcSysNVAreaVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysNVAreaVersion_Type.__name__ = "DisplayString"
_NbsCmmcSysNVAreaVersion_Object = MibTableColumn
nbsCmmcSysNVAreaVersion = _NbsCmmcSysNVAreaVersion_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 5),
    _NbsCmmcSysNVAreaVersion_Type()
)
nbsCmmcSysNVAreaVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaVersion.setStatus("current")


class _NbsCmmcSysNVAreaCksum_Type(Unsigned32):
    """Custom type nbsCmmcSysNVAreaCksum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_NbsCmmcSysNVAreaCksum_Type.__name__ = "Unsigned32"
_NbsCmmcSysNVAreaCksum_Object = MibTableColumn
nbsCmmcSysNVAreaCksum = _NbsCmmcSysNVAreaCksum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 2, 3001, 1, 6),
    _NbsCmmcSysNVAreaCksum_Type()
)
nbsCmmcSysNVAreaCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNVAreaCksum.setStatus("current")
_NbsCmmcIpSnmpGrp_ObjectIdentity = ObjectIdentity
nbsCmmcIpSnmpGrp = _NbsCmmcIpSnmpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 3)
)
if mibBuilder.loadTexts:
    nbsCmmcIpSnmpGrp.setStatus("current")
_NbsCmmcIpCfg_ObjectIdentity = ObjectIdentity
nbsCmmcIpCfg = _NbsCmmcIpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1)
)
_NbsCmmcPrvIpAddr_Type = IpAddress
_NbsCmmcPrvIpAddr_Object = MibScalar
nbsCmmcPrvIpAddr = _NbsCmmcPrvIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 1),
    _NbsCmmcPrvIpAddr_Type()
)
nbsCmmcPrvIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPrvIpAddr.setStatus("deprecated")
_NbsCmmcPrvNetMask_Type = IpAddress
_NbsCmmcPrvNetMask_Object = MibScalar
nbsCmmcPrvNetMask = _NbsCmmcPrvNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 2),
    _NbsCmmcPrvNetMask_Type()
)
nbsCmmcPrvNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPrvNetMask.setStatus("deprecated")
_NbsCmmcPrvBcastAddr_Type = IpAddress
_NbsCmmcPrvBcastAddr_Object = MibScalar
nbsCmmcPrvBcastAddr = _NbsCmmcPrvBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 3),
    _NbsCmmcPrvBcastAddr_Type()
)
nbsCmmcPrvBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPrvBcastAddr.setStatus("deprecated")
_NbsCmmcSysIpAddr_Type = IpAddress
_NbsCmmcSysIpAddr_Object = MibScalar
nbsCmmcSysIpAddr = _NbsCmmcSysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 4),
    _NbsCmmcSysIpAddr_Type()
)
nbsCmmcSysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysIpAddr.setStatus("current")
_NbsCmmcSysNetMask_Type = IpAddress
_NbsCmmcSysNetMask_Object = MibScalar
nbsCmmcSysNetMask = _NbsCmmcSysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 5),
    _NbsCmmcSysNetMask_Type()
)
nbsCmmcSysNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysNetMask.setStatus("current")
_NbsCmmcSysBcastAddr_Type = IpAddress
_NbsCmmcSysBcastAddr_Object = MibScalar
nbsCmmcSysBcastAddr = _NbsCmmcSysBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 6),
    _NbsCmmcSysBcastAddr_Type()
)
nbsCmmcSysBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysBcastAddr.setStatus("current")
_NbsCmmcSysObIpAddr_Type = IpAddress
_NbsCmmcSysObIpAddr_Object = MibScalar
nbsCmmcSysObIpAddr = _NbsCmmcSysObIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 7),
    _NbsCmmcSysObIpAddr_Type()
)
nbsCmmcSysObIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysObIpAddr.setStatus("current")
_NbsCmmcSysObNetMask_Type = IpAddress
_NbsCmmcSysObNetMask_Object = MibScalar
nbsCmmcSysObNetMask = _NbsCmmcSysObNetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 8),
    _NbsCmmcSysObNetMask_Type()
)
nbsCmmcSysObNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysObNetMask.setStatus("current")
_NbsCmmcSysObBcastAddr_Type = IpAddress
_NbsCmmcSysObBcastAddr_Object = MibScalar
nbsCmmcSysObBcastAddr = _NbsCmmcSysObBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 9),
    _NbsCmmcSysObBcastAddr_Type()
)
nbsCmmcSysObBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysObBcastAddr.setStatus("current")
_NbsCmmcSysDefaultGateway_Type = IpAddress
_NbsCmmcSysDefaultGateway_Object = MibScalar
nbsCmmcSysDefaultGateway = _NbsCmmcSysDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 10),
    _NbsCmmcSysDefaultGateway_Type()
)
nbsCmmcSysDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysDefaultGateway.setStatus("current")


class _NbsCmmcSysAdminBootpState_Type(Integer32):
    """Custom type nbsCmmcSysAdminBootpState based on Integer32"""
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


_NbsCmmcSysAdminBootpState_Type.__name__ = "Integer32"
_NbsCmmcSysAdminBootpState_Object = MibScalar
nbsCmmcSysAdminBootpState = _NbsCmmcSysAdminBootpState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 11),
    _NbsCmmcSysAdminBootpState_Type()
)
nbsCmmcSysAdminBootpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysAdminBootpState.setStatus("current")


class _NbsCmmcSysRunBootpState_Type(Integer32):
    """Custom type nbsCmmcSysRunBootpState based on Integer32"""
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


_NbsCmmcSysRunBootpState_Type.__name__ = "Integer32"
_NbsCmmcSysRunBootpState_Object = MibScalar
nbsCmmcSysRunBootpState = _NbsCmmcSysRunBootpState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 12),
    _NbsCmmcSysRunBootpState_Type()
)
nbsCmmcSysRunBootpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunBootpState.setStatus("current")


class _NbsCmmcSysSerialLineMode_Type(Integer32):
    """Custom type nbsCmmcSysSerialLineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminIf", 1),
          ("slipIf", 2))
    )


_NbsCmmcSysSerialLineMode_Type.__name__ = "Integer32"
_NbsCmmcSysSerialLineMode_Object = MibScalar
nbsCmmcSysSerialLineMode = _NbsCmmcSysSerialLineMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 13),
    _NbsCmmcSysSerialLineMode_Type()
)
nbsCmmcSysSerialLineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSerialLineMode.setStatus("current")


class _NbsCmmcSysSerialSlipBaudRate_Type(Integer32):
    """Custom type nbsCmmcSysSerialSlipBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b19200", 2),
          ("b38400", 3),
          ("b9600", 1))
    )


_NbsCmmcSysSerialSlipBaudRate_Type.__name__ = "Integer32"
_NbsCmmcSysSerialSlipBaudRate_Object = MibScalar
nbsCmmcSysSerialSlipBaudRate = _NbsCmmcSysSerialSlipBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 14),
    _NbsCmmcSysSerialSlipBaudRate_Type()
)
nbsCmmcSysSerialSlipBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSerialSlipBaudRate.setStatus("current")


class _NbsCmmcSysArpAgingTime_Type(Integer32):
    """Custom type nbsCmmcSysArpAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_NbsCmmcSysArpAgingTime_Type.__name__ = "Integer32"
_NbsCmmcSysArpAgingTime_Object = MibScalar
nbsCmmcSysArpAgingTime = _NbsCmmcSysArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 15),
    _NbsCmmcSysArpAgingTime_Type()
)
nbsCmmcSysArpAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysArpAgingTime.setStatus("current")
_NbsCmmcSysMaxTelnetSessions_Type = Integer32
_NbsCmmcSysMaxTelnetSessions_Object = MibScalar
nbsCmmcSysMaxTelnetSessions = _NbsCmmcSysMaxTelnetSessions_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 16),
    _NbsCmmcSysMaxTelnetSessions_Type()
)
nbsCmmcSysMaxTelnetSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysMaxTelnetSessions.setStatus("current")
_NbsCmmcSysTelnetTable_Object = MibTable
nbsCmmcSysTelnetTable = _NbsCmmcSysTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17)
)
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetTable.setStatus("current")
_NbsCmmcSysTelnetEntry_Object = MibTableRow
nbsCmmcSysTelnetEntry = _NbsCmmcSysTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1)
)
nbsCmmcSysTelnetEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysTelnetSessionIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetEntry.setStatus("current")
_NbsCmmcSysTelnetSessionIndex_Type = Integer32
_NbsCmmcSysTelnetSessionIndex_Object = MibTableColumn
nbsCmmcSysTelnetSessionIndex = _NbsCmmcSysTelnetSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 1),
    _NbsCmmcSysTelnetSessionIndex_Type()
)
nbsCmmcSysTelnetSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetSessionIndex.setStatus("current")


class _NbsCmmcSysTelnetSessionStat_Type(Integer32):
    """Custom type nbsCmmcSysTelnetSessionStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnect", 2))
    )


_NbsCmmcSysTelnetSessionStat_Type.__name__ = "Integer32"
_NbsCmmcSysTelnetSessionStat_Object = MibTableColumn
nbsCmmcSysTelnetSessionStat = _NbsCmmcSysTelnetSessionStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 2),
    _NbsCmmcSysTelnetSessionStat_Type()
)
nbsCmmcSysTelnetSessionStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetSessionStat.setStatus("current")
_NbsCmmcSysTelnetHost_Type = IpAddress
_NbsCmmcSysTelnetHost_Object = MibTableColumn
nbsCmmcSysTelnetHost = _NbsCmmcSysTelnetHost_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 3),
    _NbsCmmcSysTelnetHost_Type()
)
nbsCmmcSysTelnetHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetHost.setStatus("current")
_NbsCmmcSysTelnetHostPort_Type = Integer32
_NbsCmmcSysTelnetHostPort_Object = MibTableColumn
nbsCmmcSysTelnetHostPort = _NbsCmmcSysTelnetHostPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 4),
    _NbsCmmcSysTelnetHostPort_Type()
)
nbsCmmcSysTelnetHostPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetHostPort.setStatus("current")
_NbsCmmcSysTelnetLocal_Type = IpAddress
_NbsCmmcSysTelnetLocal_Object = MibTableColumn
nbsCmmcSysTelnetLocal = _NbsCmmcSysTelnetLocal_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 5),
    _NbsCmmcSysTelnetLocal_Type()
)
nbsCmmcSysTelnetLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetLocal.setStatus("current")
_NbsCmmcSysTelnetLocalPort_Type = Integer32
_NbsCmmcSysTelnetLocalPort_Object = MibTableColumn
nbsCmmcSysTelnetLocalPort = _NbsCmmcSysTelnetLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 6),
    _NbsCmmcSysTelnetLocalPort_Type()
)
nbsCmmcSysTelnetLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetLocalPort.setStatus("current")
_NbsCmmcSysTelnetSessionId_Type = Integer32
_NbsCmmcSysTelnetSessionId_Object = MibTableColumn
nbsCmmcSysTelnetSessionId = _NbsCmmcSysTelnetSessionId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 7),
    _NbsCmmcSysTelnetSessionId_Type()
)
nbsCmmcSysTelnetSessionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetSessionId.setStatus("current")


class _NbsCmmcSysTelnetConnectTime_Type(DisplayString):
    """Custom type nbsCmmcSysTelnetConnectTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysTelnetConnectTime_Type.__name__ = "DisplayString"
_NbsCmmcSysTelnetConnectTime_Object = MibTableColumn
nbsCmmcSysTelnetConnectTime = _NbsCmmcSysTelnetConnectTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 17, 1, 8),
    _NbsCmmcSysTelnetConnectTime_Type()
)
nbsCmmcSysTelnetConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetConnectTime.setStatus("current")
_NbsCmmcSysMaxPingSessions_Type = Integer32
_NbsCmmcSysMaxPingSessions_Object = MibScalar
nbsCmmcSysMaxPingSessions = _NbsCmmcSysMaxPingSessions_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 18),
    _NbsCmmcSysMaxPingSessions_Type()
)
nbsCmmcSysMaxPingSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysMaxPingSessions.setStatus("current")
_NbsCmmcSysPingTable_Object = MibTable
nbsCmmcSysPingTable = _NbsCmmcSysPingTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19)
)
if mibBuilder.loadTexts:
    nbsCmmcSysPingTable.setStatus("current")
_NbsCmmcSysPingEntry_Object = MibTableRow
nbsCmmcSysPingEntry = _NbsCmmcSysPingEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1)
)
nbsCmmcSysPingEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysPingSessionIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysPingEntry.setStatus("current")
_NbsCmmcSysPingSessionIndex_Type = Integer32
_NbsCmmcSysPingSessionIndex_Object = MibTableColumn
nbsCmmcSysPingSessionIndex = _NbsCmmcSysPingSessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 1),
    _NbsCmmcSysPingSessionIndex_Type()
)
nbsCmmcSysPingSessionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysPingSessionIndex.setStatus("current")


class _NbsCmmcSysPingSessionStat_Type(Integer32):
    """Custom type nbsCmmcSysPingSessionStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idlePing", 1),
          ("runPing", 2))
    )


_NbsCmmcSysPingSessionStat_Type.__name__ = "Integer32"
_NbsCmmcSysPingSessionStat_Object = MibTableColumn
nbsCmmcSysPingSessionStat = _NbsCmmcSysPingSessionStat_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 2),
    _NbsCmmcSysPingSessionStat_Type()
)
nbsCmmcSysPingSessionStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysPingSessionStat.setStatus("current")


class _NbsCmmcSysPingAddr_Type(IpAddress):
    """Custom type nbsCmmcSysPingAddr based on IpAddress"""
    defaultHexValue = "7F000001"


_NbsCmmcSysPingAddr_Object = MibTableColumn
nbsCmmcSysPingAddr = _NbsCmmcSysPingAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 3),
    _NbsCmmcSysPingAddr_Type()
)
nbsCmmcSysPingAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysPingAddr.setStatus("current")
_NbsCmmcSysPingNumber_Type = Counter32
_NbsCmmcSysPingNumber_Object = MibTableColumn
nbsCmmcSysPingNumber = _NbsCmmcSysPingNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 4),
    _NbsCmmcSysPingNumber_Type()
)
nbsCmmcSysPingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysPingNumber.setStatus("current")


class _NbsCmmcSysPingOwner_Type(Integer32):
    """Custom type nbsCmmcSysPingOwner based on Integer32"""
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
        *(("adminInterface", 2),
          ("none", 1),
          ("snmpAgent", 3),
          ("webManager", 4))
    )


_NbsCmmcSysPingOwner_Type.__name__ = "Integer32"
_NbsCmmcSysPingOwner_Object = MibTableColumn
nbsCmmcSysPingOwner = _NbsCmmcSysPingOwner_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 5),
    _NbsCmmcSysPingOwner_Type()
)
nbsCmmcSysPingOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysPingOwner.setStatus("current")
_NbsCmmcSysPingRequests_Type = Counter32
_NbsCmmcSysPingRequests_Object = MibTableColumn
nbsCmmcSysPingRequests = _NbsCmmcSysPingRequests_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 6),
    _NbsCmmcSysPingRequests_Type()
)
nbsCmmcSysPingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysPingRequests.setStatus("current")
_NbsCmmcSysPingResponses_Type = Counter32
_NbsCmmcSysPingResponses_Object = MibTableColumn
nbsCmmcSysPingResponses = _NbsCmmcSysPingResponses_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 19, 1, 7),
    _NbsCmmcSysPingResponses_Type()
)
nbsCmmcSysPingResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysPingResponses.setStatus("current")


class _NbsCmmcSysTelnetServer_Type(Integer32):
    """Custom type nbsCmmcSysTelnetServer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysTelnetServer_Type.__name__ = "Integer32"
_NbsCmmcSysTelnetServer_Object = MibScalar
nbsCmmcSysTelnetServer = _NbsCmmcSysTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 20),
    _NbsCmmcSysTelnetServer_Type()
)
nbsCmmcSysTelnetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetServer.setStatus("current")


class _NbsCmmcSysSshServer_Type(Integer32):
    """Custom type nbsCmmcSysSshServer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysSshServer_Type.__name__ = "Integer32"
_NbsCmmcSysSshServer_Object = MibScalar
nbsCmmcSysSshServer = _NbsCmmcSysSshServer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 21),
    _NbsCmmcSysSshServer_Type()
)
nbsCmmcSysSshServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSshServer.setStatus("current")
_NbsCmmcSysIpAddrOper_Type = IpAddress
_NbsCmmcSysIpAddrOper_Object = MibScalar
nbsCmmcSysIpAddrOper = _NbsCmmcSysIpAddrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 22),
    _NbsCmmcSysIpAddrOper_Type()
)
nbsCmmcSysIpAddrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysIpAddrOper.setStatus("current")
_NbsCmmcSysNetMaskOper_Type = IpAddress
_NbsCmmcSysNetMaskOper_Object = MibScalar
nbsCmmcSysNetMaskOper = _NbsCmmcSysNetMaskOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 23),
    _NbsCmmcSysNetMaskOper_Type()
)
nbsCmmcSysNetMaskOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNetMaskOper.setStatus("current")
_NbsCmmcSysBcastAddrOper_Type = IpAddress
_NbsCmmcSysBcastAddrOper_Object = MibScalar
nbsCmmcSysBcastAddrOper = _NbsCmmcSysBcastAddrOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 24),
    _NbsCmmcSysBcastAddrOper_Type()
)
nbsCmmcSysBcastAddrOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysBcastAddrOper.setStatus("current")
_NbsCmmcSysDefaultGatewayOper_Type = IpAddress
_NbsCmmcSysDefaultGatewayOper_Object = MibScalar
nbsCmmcSysDefaultGatewayOper = _NbsCmmcSysDefaultGatewayOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 25),
    _NbsCmmcSysDefaultGatewayOper_Type()
)
nbsCmmcSysDefaultGatewayOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysDefaultGatewayOper.setStatus("current")


class _NbsCmmcSysWebServer_Type(Integer32):
    """Custom type nbsCmmcSysWebServer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSysWebServer_Type.__name__ = "Integer32"
_NbsCmmcSysWebServer_Object = MibScalar
nbsCmmcSysWebServer = _NbsCmmcSysWebServer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 26),
    _NbsCmmcSysWebServer_Type()
)
nbsCmmcSysWebServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysWebServer.setStatus("current")


class _NbsCmmcSysWebPort_Type(Integer32):
    """Custom type nbsCmmcSysWebPort based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysWebPort_Type.__name__ = "Integer32"
_NbsCmmcSysWebPort_Object = MibScalar
nbsCmmcSysWebPort = _NbsCmmcSysWebPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 27),
    _NbsCmmcSysWebPort_Type()
)
nbsCmmcSysWebPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysWebPort.setStatus("current")


class _NbsCmmcSysTelnetPort_Type(Integer32):
    """Custom type nbsCmmcSysTelnetPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysTelnetPort_Type.__name__ = "Integer32"
_NbsCmmcSysTelnetPort_Object = MibScalar
nbsCmmcSysTelnetPort = _NbsCmmcSysTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 28),
    _NbsCmmcSysTelnetPort_Type()
)
nbsCmmcSysTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTelnetPort.setStatus("current")


class _NbsCmmcSysSshPort_Type(Integer32):
    """Custom type nbsCmmcSysSshPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysSshPort_Type.__name__ = "Integer32"
_NbsCmmcSysSshPort_Object = MibScalar
nbsCmmcSysSshPort = _NbsCmmcSysSshPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 1, 29),
    _NbsCmmcSysSshPort_Type()
)
nbsCmmcSysSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSshPort.setStatus("current")
_NbsCmmcSnmpCfg_ObjectIdentity = ObjectIdentity
nbsCmmcSnmpCfg = _NbsCmmcSnmpCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2)
)


class _NbsCmmcSysWriteCommunity_Type(DisplayString):
    """Custom type nbsCmmcSysWriteCommunity based on DisplayString"""
    defaultValue = OctetString("private")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysWriteCommunity_Type.__name__ = "DisplayString"
_NbsCmmcSysWriteCommunity_Object = MibScalar
nbsCmmcSysWriteCommunity = _NbsCmmcSysWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 1),
    _NbsCmmcSysWriteCommunity_Type()
)
nbsCmmcSysWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysWriteCommunity.setStatus("current")


class _NbsCmmcSysReadCommunity_Type(DisplayString):
    """Custom type nbsCmmcSysReadCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysReadCommunity_Type.__name__ = "DisplayString"
_NbsCmmcSysReadCommunity_Object = MibScalar
nbsCmmcSysReadCommunity = _NbsCmmcSysReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 2),
    _NbsCmmcSysReadCommunity_Type()
)
nbsCmmcSysReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysReadCommunity.setStatus("current")
_NbsCmmcSysTrapTblMaxSize_Type = Integer32
_NbsCmmcSysTrapTblMaxSize_Object = MibScalar
nbsCmmcSysTrapTblMaxSize = _NbsCmmcSysTrapTblMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 3),
    _NbsCmmcSysTrapTblMaxSize_Type()
)
nbsCmmcSysTrapTblMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblMaxSize.setStatus("current")
_NbsCmmcSysTrapTable_Object = MibTable
nbsCmmcSysTrapTable = _NbsCmmcSysTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4)
)
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTable.setStatus("current")
_NbsCmmcSysTrapEntry_Object = MibTableRow
nbsCmmcSysTrapEntry = _NbsCmmcSysTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1)
)
nbsCmmcSysTrapEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysTrapTblEntIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysTrapEntry.setStatus("current")
_NbsCmmcSysTrapTblEntIndex_Type = Integer32
_NbsCmmcSysTrapTblEntIndex_Object = MibTableColumn
nbsCmmcSysTrapTblEntIndex = _NbsCmmcSysTrapTblEntIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 1),
    _NbsCmmcSysTrapTblEntIndex_Type()
)
nbsCmmcSysTrapTblEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntIndex.setStatus("current")


class _NbsCmmcSysTrapTblEntStatus_Type(Integer32):
    """Custom type nbsCmmcSysTrapTblEntStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("invalid", 1))
    )


_NbsCmmcSysTrapTblEntStatus_Type.__name__ = "Integer32"
_NbsCmmcSysTrapTblEntStatus_Object = MibTableColumn
nbsCmmcSysTrapTblEntStatus = _NbsCmmcSysTrapTblEntStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 2),
    _NbsCmmcSysTrapTblEntStatus_Type()
)
nbsCmmcSysTrapTblEntStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntStatus.setStatus("current")
_NbsCmmcSysTrapTblEntIpAddr_Type = IpAddress
_NbsCmmcSysTrapTblEntIpAddr_Object = MibTableColumn
nbsCmmcSysTrapTblEntIpAddr = _NbsCmmcSysTrapTblEntIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 3),
    _NbsCmmcSysTrapTblEntIpAddr_Type()
)
nbsCmmcSysTrapTblEntIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntIpAddr.setStatus("current")


class _NbsCmmcSysTrapTblEntComm_Type(DisplayString):
    """Custom type nbsCmmcSysTrapTblEntComm based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysTrapTblEntComm_Type.__name__ = "DisplayString"
_NbsCmmcSysTrapTblEntComm_Object = MibTableColumn
nbsCmmcSysTrapTblEntComm = _NbsCmmcSysTrapTblEntComm_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 4),
    _NbsCmmcSysTrapTblEntComm_Type()
)
nbsCmmcSysTrapTblEntComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntComm.setStatus("current")


class _NbsCmmcSysTrapTblEntLevel_Type(Integer32):
    """Custom type nbsCmmcSysTrapTblEntLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 7),
          ("deprecated5", 5),
          ("deprecated6", 6),
          ("disabled", 1),
          ("error", 3),
          ("fatal", 2),
          ("warning", 4))
    )


_NbsCmmcSysTrapTblEntLevel_Type.__name__ = "Integer32"
_NbsCmmcSysTrapTblEntLevel_Object = MibTableColumn
nbsCmmcSysTrapTblEntLevel = _NbsCmmcSysTrapTblEntLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 5),
    _NbsCmmcSysTrapTblEntLevel_Type()
)
nbsCmmcSysTrapTblEntLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntLevel.setStatus("current")


class _NbsCmmcSysTrapTblEntPort_Type(Integer32):
    """Custom type nbsCmmcSysTrapTblEntPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysTrapTblEntPort_Type.__name__ = "Integer32"
_NbsCmmcSysTrapTblEntPort_Object = MibTableColumn
nbsCmmcSysTrapTblEntPort = _NbsCmmcSysTrapTblEntPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 4, 1, 6),
    _NbsCmmcSysTrapTblEntPort_Type()
)
nbsCmmcSysTrapTblEntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTrapTblEntPort.setStatus("current")


class _NbsCmmcSysEnablePowerSupplyTraps_Type(Integer32):
    """Custom type nbsCmmcSysEnablePowerSupplyTraps based on Integer32"""
    defaultValue = 2

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


_NbsCmmcSysEnablePowerSupplyTraps_Type.__name__ = "Integer32"
_NbsCmmcSysEnablePowerSupplyTraps_Object = MibScalar
nbsCmmcSysEnablePowerSupplyTraps = _NbsCmmcSysEnablePowerSupplyTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 11),
    _NbsCmmcSysEnablePowerSupplyTraps_Type()
)
nbsCmmcSysEnablePowerSupplyTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysEnablePowerSupplyTraps.setStatus("current")


class _NbsCmmcSysEnableModuleTraps_Type(Integer32):
    """Custom type nbsCmmcSysEnableModuleTraps based on Integer32"""
    defaultValue = 2

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


_NbsCmmcSysEnableModuleTraps_Type.__name__ = "Integer32"
_NbsCmmcSysEnableModuleTraps_Object = MibScalar
nbsCmmcSysEnableModuleTraps = _NbsCmmcSysEnableModuleTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 12),
    _NbsCmmcSysEnableModuleTraps_Type()
)
nbsCmmcSysEnableModuleTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysEnableModuleTraps.setStatus("current")


class _NbsCmmcSysEnableBridgeTraps_Type(Integer32):
    """Custom type nbsCmmcSysEnableBridgeTraps based on Integer32"""
    defaultValue = 2

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


_NbsCmmcSysEnableBridgeTraps_Type.__name__ = "Integer32"
_NbsCmmcSysEnableBridgeTraps_Object = MibScalar
nbsCmmcSysEnableBridgeTraps = _NbsCmmcSysEnableBridgeTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 13),
    _NbsCmmcSysEnableBridgeTraps_Type()
)
nbsCmmcSysEnableBridgeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysEnableBridgeTraps.setStatus("current")


class _NbsCmmcSysEnableIpAccessTraps_Type(Integer32):
    """Custom type nbsCmmcSysEnableIpAccessTraps based on Integer32"""
    defaultValue = 2

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


_NbsCmmcSysEnableIpAccessTraps_Type.__name__ = "Integer32"
_NbsCmmcSysEnableIpAccessTraps_Object = MibScalar
nbsCmmcSysEnableIpAccessTraps = _NbsCmmcSysEnableIpAccessTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 14),
    _NbsCmmcSysEnableIpAccessTraps_Type()
)
nbsCmmcSysEnableIpAccessTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysEnableIpAccessTraps.setStatus("current")


class _NbsCmmcSysSnmpPortAdmin_Type(Integer32):
    """Custom type nbsCmmcSysSnmpPortAdmin based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysSnmpPortAdmin_Type.__name__ = "Integer32"
_NbsCmmcSysSnmpPortAdmin_Object = MibScalar
nbsCmmcSysSnmpPortAdmin = _NbsCmmcSysSnmpPortAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 15),
    _NbsCmmcSysSnmpPortAdmin_Type()
)
nbsCmmcSysSnmpPortAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysSnmpPortAdmin.setStatus("current")


class _NbsCmmcSysSnmpPortOper_Type(Integer32):
    """Custom type nbsCmmcSysSnmpPortOper based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NbsCmmcSysSnmpPortOper_Type.__name__ = "Integer32"
_NbsCmmcSysSnmpPortOper_Object = MibScalar
nbsCmmcSysSnmpPortOper = _NbsCmmcSysSnmpPortOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 3, 2, 16),
    _NbsCmmcSysSnmpPortOper_Type()
)
nbsCmmcSysSnmpPortOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysSnmpPortOper.setStatus("current")
_NbsCmmcTftpGrp_ObjectIdentity = ObjectIdentity
nbsCmmcTftpGrp = _NbsCmmcTftpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 4)
)
if mibBuilder.loadTexts:
    nbsCmmcTftpGrp.setStatus("current")


class _NbsCmmcSysTftpHostIP_Type(IpAddress):
    """Custom type nbsCmmcSysTftpHostIP based on IpAddress"""
    defaultHexValue = "00000000"


_NbsCmmcSysTftpHostIP_Object = MibScalar
nbsCmmcSysTftpHostIP = _NbsCmmcSysTftpHostIP_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 1),
    _NbsCmmcSysTftpHostIP_Type()
)
nbsCmmcSysTftpHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysTftpHostIP.setStatus("current")


class _NbsCmmcTftpMaxSessionNum_Type(Integer32):
    """Custom type nbsCmmcTftpMaxSessionNum based on Integer32"""
    defaultValue = 5


_NbsCmmcTftpMaxSessionNum_Object = MibScalar
nbsCmmcTftpMaxSessionNum = _NbsCmmcTftpMaxSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 2),
    _NbsCmmcTftpMaxSessionNum_Type()
)
nbsCmmcTftpMaxSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcTftpMaxSessionNum.setStatus("current")
_NbsCmmcTftpSessTable_Object = MibTable
nbsCmmcTftpSessTable = _NbsCmmcTftpSessTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3)
)
if mibBuilder.loadTexts:
    nbsCmmcTftpSessTable.setStatus("current")
_NbsCmmcTftpSessEntry_Object = MibTableRow
nbsCmmcTftpSessEntry = _NbsCmmcTftpSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1)
)
nbsCmmcTftpSessEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcTftpSessIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcTftpSessEntry.setStatus("current")
_NbsCmmcTftpSessIndex_Type = Integer32
_NbsCmmcTftpSessIndex_Object = MibTableColumn
nbsCmmcTftpSessIndex = _NbsCmmcTftpSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 1),
    _NbsCmmcTftpSessIndex_Type()
)
nbsCmmcTftpSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessIndex.setStatus("current")


class _NbsCmmcTftpSessStatus_Type(Integer32):
    """Custom type nbsCmmcTftpSessStatus based on Integer32"""
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
        *(("active", 4),
          ("create", 2),
          ("inactive", 1),
          ("transferEnded", 5),
          ("underCreation", 3))
    )


_NbsCmmcTftpSessStatus_Type.__name__ = "Integer32"
_NbsCmmcTftpSessStatus_Object = MibTableColumn
nbsCmmcTftpSessStatus = _NbsCmmcTftpSessStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 2),
    _NbsCmmcTftpSessStatus_Type()
)
nbsCmmcTftpSessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessStatus.setStatus("current")


class _NbsCmmcTftpSessHostIp_Type(IpAddress):
    """Custom type nbsCmmcTftpSessHostIp based on IpAddress"""
    defaultHexValue = "00000000"


_NbsCmmcTftpSessHostIp_Object = MibTableColumn
nbsCmmcTftpSessHostIp = _NbsCmmcTftpSessHostIp_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 3),
    _NbsCmmcTftpSessHostIp_Type()
)
nbsCmmcTftpSessHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessHostIp.setStatus("current")
_NbsCmmcTftpSessModuleId_Type = Integer32
_NbsCmmcTftpSessModuleId_Object = MibTableColumn
nbsCmmcTftpSessModuleId = _NbsCmmcTftpSessModuleId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 4),
    _NbsCmmcTftpSessModuleId_Type()
)
nbsCmmcTftpSessModuleId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessModuleId.setStatus("deprecated")


class _NbsCmmcTftpSessAction_Type(Integer32):
    """Custom type nbsCmmcTftpSessAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("downloadFile", 6),
          ("downloadNM", 2),
          ("downloadPar", 4),
          ("inactive", 1),
          ("uploadFile", 7),
          ("uploadNM", 3),
          ("uploadPar", 5))
    )


_NbsCmmcTftpSessAction_Type.__name__ = "Integer32"
_NbsCmmcTftpSessAction_Object = MibTableColumn
nbsCmmcTftpSessAction = _NbsCmmcTftpSessAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 5),
    _NbsCmmcTftpSessAction_Type()
)
nbsCmmcTftpSessAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessAction.setStatus("current")


class _NbsCmmcTftpSessFileName_Type(DisplayString):
    """Custom type nbsCmmcTftpSessFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcTftpSessFileName_Type.__name__ = "DisplayString"
_NbsCmmcTftpSessFileName_Object = MibTableColumn
nbsCmmcTftpSessFileName = _NbsCmmcTftpSessFileName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 6),
    _NbsCmmcTftpSessFileName_Type()
)
nbsCmmcTftpSessFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessFileName.setStatus("current")


class _NbsCmmcTftpSessFileSize_Type(Integer32):
    """Custom type nbsCmmcTftpSessFileSize based on Integer32"""
    defaultValue = -1


_NbsCmmcTftpSessFileSize_Object = MibTableColumn
nbsCmmcTftpSessFileSize = _NbsCmmcTftpSessFileSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 7),
    _NbsCmmcTftpSessFileSize_Type()
)
nbsCmmcTftpSessFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessFileSize.setStatus("deprecated")


class _NbsCmmcTftpSessProgress_Type(Integer32):
    """Custom type nbsCmmcTftpSessProgress based on Integer32"""
    defaultValue = -1


_NbsCmmcTftpSessProgress_Object = MibTableColumn
nbsCmmcTftpSessProgress = _NbsCmmcTftpSessProgress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 4, 3, 1, 8),
    _NbsCmmcTftpSessProgress_Type()
)
nbsCmmcTftpSessProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcTftpSessProgress.setStatus("deprecated")
_NbsCmmcChassisGrp_ObjectIdentity = ObjectIdentity
nbsCmmcChassisGrp = _NbsCmmcChassisGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 6)
)
if mibBuilder.loadTexts:
    nbsCmmcChassisGrp.setStatus("current")
_NbsCmmcChassisTable_Object = MibTable
nbsCmmcChassisTable = _NbsCmmcChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1)
)
if mibBuilder.loadTexts:
    nbsCmmcChassisTable.setStatus("current")
_NbsCmmcChassisEntry_Object = MibTableRow
nbsCmmcChassisEntry = _NbsCmmcChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1)
)
nbsCmmcChassisEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcChassisEntry.setStatus("current")
_NbsCmmcChassisIndex_Type = Integer32
_NbsCmmcChassisIndex_Object = MibTableColumn
nbsCmmcChassisIndex = _NbsCmmcChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 1),
    _NbsCmmcChassisIndex_Type()
)
nbsCmmcChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisIndex.setStatus("current")


class _NbsCmmcChassisType_Type(Integer32):
    """Custom type nbsCmmcChassisType based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("bmc", 9),
          ("bu1", 4),
          ("bu12", 21),
          ("bu16", 2),
          ("bu2", 7),
          ("bu21", 11),
          ("bu22", 17),
          ("bu3", 6),
          ("bu3v", 19),
          ("bu4", 3),
          ("bu42", 12),
          ("bu5", 5),
          ("bu82", 18),
          ("fCpe", 8),
          ("other", 1),
          ("virtual1", 13),
          ("virtual16", 10),
          ("virtual2", 14),
          ("virtual3", 15),
          ("virtual3v", 20),
          ("virtual4", 16))
    )


_NbsCmmcChassisType_Type.__name__ = "Integer32"
_NbsCmmcChassisType_Object = MibTableColumn
nbsCmmcChassisType = _NbsCmmcChassisType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 2),
    _NbsCmmcChassisType_Type()
)
nbsCmmcChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisType.setStatus("current")


class _NbsCmmcChassisModel_Type(DisplayString):
    """Custom type nbsCmmcChassisModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcChassisModel_Type.__name__ = "DisplayString"
_NbsCmmcChassisModel_Object = MibTableColumn
nbsCmmcChassisModel = _NbsCmmcChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 3),
    _NbsCmmcChassisModel_Type()
)
nbsCmmcChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisModel.setStatus("current")
_NbsCmmcChassisObjectId_Type = ObjectIdentifier
_NbsCmmcChassisObjectId_Object = MibTableColumn
nbsCmmcChassisObjectId = _NbsCmmcChassisObjectId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 4),
    _NbsCmmcChassisObjectId_Type()
)
nbsCmmcChassisObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisObjectId.setStatus("current")
_NbsCmmcChassisNumberOfSlots_Type = Integer32
_NbsCmmcChassisNumberOfSlots_Object = MibTableColumn
nbsCmmcChassisNumberOfSlots = _NbsCmmcChassisNumberOfSlots_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 5),
    _NbsCmmcChassisNumberOfSlots_Type()
)
nbsCmmcChassisNumberOfSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisNumberOfSlots.setStatus("current")


class _NbsCmmcChassisHardwareRevision_Type(DisplayString):
    """Custom type nbsCmmcChassisHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsCmmcChassisHardwareRevision_Type.__name__ = "DisplayString"
_NbsCmmcChassisHardwareRevision_Object = MibTableColumn
nbsCmmcChassisHardwareRevision = _NbsCmmcChassisHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 6),
    _NbsCmmcChassisHardwareRevision_Type()
)
nbsCmmcChassisHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisHardwareRevision.setStatus("current")


class _NbsCmmcChassisPS1Status_Type(Integer32):
    """Custom type nbsCmmcChassisPS1Status based on Integer32"""
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
        *(("acBad", 2),
          ("acGood", 4),
          ("bad", 8),
          ("dcBad", 3),
          ("dcGood", 5),
          ("good", 7),
          ("notInstalled", 1),
          ("notSupported", 6))
    )


_NbsCmmcChassisPS1Status_Type.__name__ = "Integer32"
_NbsCmmcChassisPS1Status_Object = MibTableColumn
nbsCmmcChassisPS1Status = _NbsCmmcChassisPS1Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 7),
    _NbsCmmcChassisPS1Status_Type()
)
nbsCmmcChassisPS1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisPS1Status.setStatus("current")


class _NbsCmmcChassisPS2Status_Type(Integer32):
    """Custom type nbsCmmcChassisPS2Status based on Integer32"""
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
        *(("acBad", 2),
          ("acGood", 4),
          ("bad", 8),
          ("dcBad", 3),
          ("dcGood", 5),
          ("good", 7),
          ("notInstalled", 1),
          ("notSupported", 6))
    )


_NbsCmmcChassisPS2Status_Type.__name__ = "Integer32"
_NbsCmmcChassisPS2Status_Object = MibTableColumn
nbsCmmcChassisPS2Status = _NbsCmmcChassisPS2Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 8),
    _NbsCmmcChassisPS2Status_Type()
)
nbsCmmcChassisPS2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisPS2Status.setStatus("current")


class _NbsCmmcChassisPS3Status_Type(Integer32):
    """Custom type nbsCmmcChassisPS3Status based on Integer32"""
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
        *(("acBad", 2),
          ("acGood", 4),
          ("bad", 8),
          ("dcBad", 3),
          ("dcGood", 5),
          ("good", 7),
          ("notInstalled", 1),
          ("notSupported", 6))
    )


_NbsCmmcChassisPS3Status_Type.__name__ = "Integer32"
_NbsCmmcChassisPS3Status_Object = MibTableColumn
nbsCmmcChassisPS3Status = _NbsCmmcChassisPS3Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 9),
    _NbsCmmcChassisPS3Status_Type()
)
nbsCmmcChassisPS3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisPS3Status.setStatus("current")


class _NbsCmmcChassisPS4Status_Type(Integer32):
    """Custom type nbsCmmcChassisPS4Status based on Integer32"""
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
        *(("acBad", 2),
          ("acGood", 4),
          ("bad", 8),
          ("dcBad", 3),
          ("dcGood", 5),
          ("good", 7),
          ("notInstalled", 1),
          ("notSupported", 6))
    )


_NbsCmmcChassisPS4Status_Type.__name__ = "Integer32"
_NbsCmmcChassisPS4Status_Object = MibTableColumn
nbsCmmcChassisPS4Status = _NbsCmmcChassisPS4Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 10),
    _NbsCmmcChassisPS4Status_Type()
)
nbsCmmcChassisPS4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisPS4Status.setStatus("current")


class _NbsCmmcChassisFan1Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan1Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan1Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan1Status_Object = MibTableColumn
nbsCmmcChassisFan1Status = _NbsCmmcChassisFan1Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 11),
    _NbsCmmcChassisFan1Status_Type()
)
nbsCmmcChassisFan1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan1Status.setStatus("current")


class _NbsCmmcChassisFan2Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan2Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan2Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan2Status_Object = MibTableColumn
nbsCmmcChassisFan2Status = _NbsCmmcChassisFan2Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 12),
    _NbsCmmcChassisFan2Status_Type()
)
nbsCmmcChassisFan2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan2Status.setStatus("current")


class _NbsCmmcChassisFan3Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan3Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan3Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan3Status_Object = MibTableColumn
nbsCmmcChassisFan3Status = _NbsCmmcChassisFan3Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 13),
    _NbsCmmcChassisFan3Status_Type()
)
nbsCmmcChassisFan3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan3Status.setStatus("current")


class _NbsCmmcChassisFan4Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan4Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan4Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan4Status_Object = MibTableColumn
nbsCmmcChassisFan4Status = _NbsCmmcChassisFan4Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 14),
    _NbsCmmcChassisFan4Status_Type()
)
nbsCmmcChassisFan4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan4Status.setStatus("current")


class _NbsCmmcChassisTemperature_Type(Integer32):
    """Custom type nbsCmmcChassisTemperature based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcChassisTemperature_Type.__name__ = "Integer32"
_NbsCmmcChassisTemperature_Object = MibTableColumn
nbsCmmcChassisTemperature = _NbsCmmcChassisTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 15),
    _NbsCmmcChassisTemperature_Type()
)
nbsCmmcChassisTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisTemperature.setStatus("current")


class _NbsCmmcChassisTemperatureLimit_Type(Integer32):
    """Custom type nbsCmmcChassisTemperatureLimit based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NbsCmmcChassisTemperatureLimit_Type.__name__ = "Integer32"
_NbsCmmcChassisTemperatureLimit_Object = MibTableColumn
nbsCmmcChassisTemperatureLimit = _NbsCmmcChassisTemperatureLimit_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 16),
    _NbsCmmcChassisTemperatureLimit_Type()
)
nbsCmmcChassisTemperatureLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisTemperatureLimit.setStatus("current")


class _NbsCmmcChassisTemperatureMin_Type(Integer32):
    """Custom type nbsCmmcChassisTemperatureMin based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_NbsCmmcChassisTemperatureMin_Type.__name__ = "Integer32"
_NbsCmmcChassisTemperatureMin_Object = MibTableColumn
nbsCmmcChassisTemperatureMin = _NbsCmmcChassisTemperatureMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 17),
    _NbsCmmcChassisTemperatureMin_Type()
)
nbsCmmcChassisTemperatureMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisTemperatureMin.setStatus("current")
_NbsCmmcChassisSignalStrength_Type = Integer32
_NbsCmmcChassisSignalStrength_Object = MibTableColumn
nbsCmmcChassisSignalStrength = _NbsCmmcChassisSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 18),
    _NbsCmmcChassisSignalStrength_Type()
)
nbsCmmcChassisSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisSignalStrength.setStatus("deprecated")
_NbsCmmcChassisSignalStrengthMinimum_Type = Integer32
_NbsCmmcChassisSignalStrengthMinimum_Object = MibTableColumn
nbsCmmcChassisSignalStrengthMinimum = _NbsCmmcChassisSignalStrengthMinimum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 19),
    _NbsCmmcChassisSignalStrengthMinimum_Type()
)
nbsCmmcChassisSignalStrengthMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisSignalStrengthMinimum.setStatus("deprecated")


class _NbsCmmcChassisEnableAutoReset_Type(Integer32):
    """Custom type nbsCmmcChassisEnableAutoReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deprecatedoff", 2),
          ("deprecatedon", 3),
          ("notSupported", 1))
    )


_NbsCmmcChassisEnableAutoReset_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableAutoReset_Object = MibTableColumn
nbsCmmcChassisEnableAutoReset = _NbsCmmcChassisEnableAutoReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 20),
    _NbsCmmcChassisEnableAutoReset_Type()
)
nbsCmmcChassisEnableAutoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableAutoReset.setStatus("current")


class _NbsCmmcChassisEnableLinkTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableLinkTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableLinkTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableLinkTraps_Object = MibTableColumn
nbsCmmcChassisEnableLinkTraps = _NbsCmmcChassisEnableLinkTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 21),
    _NbsCmmcChassisEnableLinkTraps_Type()
)
nbsCmmcChassisEnableLinkTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableLinkTraps.setStatus("current")


class _NbsCmmcChassisEnableChassisTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableChassisTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableChassisTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableChassisTraps_Object = MibTableColumn
nbsCmmcChassisEnableChassisTraps = _NbsCmmcChassisEnableChassisTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 22),
    _NbsCmmcChassisEnableChassisTraps_Type()
)
nbsCmmcChassisEnableChassisTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableChassisTraps.setStatus("current")


class _NbsCmmcChassisEnableLoopbackTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableLoopbackTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableLoopbackTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableLoopbackTraps_Object = MibTableColumn
nbsCmmcChassisEnableLoopbackTraps = _NbsCmmcChassisEnableLoopbackTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 23),
    _NbsCmmcChassisEnableLoopbackTraps_Type()
)
nbsCmmcChassisEnableLoopbackTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableLoopbackTraps.setStatus("current")


class _NbsCmmcChassisEnableSlotChangeTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableSlotChangeTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableSlotChangeTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableSlotChangeTraps_Object = MibTableColumn
nbsCmmcChassisEnableSlotChangeTraps = _NbsCmmcChassisEnableSlotChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 24),
    _NbsCmmcChassisEnableSlotChangeTraps_Type()
)
nbsCmmcChassisEnableSlotChangeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableSlotChangeTraps.setStatus("current")


class _NbsCmmcChassisEnablePortTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnablePortTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnablePortTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnablePortTraps_Object = MibTableColumn
nbsCmmcChassisEnablePortTraps = _NbsCmmcChassisEnablePortTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 25),
    _NbsCmmcChassisEnablePortTraps_Type()
)
nbsCmmcChassisEnablePortTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnablePortTraps.setStatus("current")


class _NbsCmmcChassisResetAllModules_Type(Integer32):
    """Custom type nbsCmmcChassisResetAllModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deprecatedOperating", 2),
          ("deprecatedReset", 3),
          ("notSupported", 1))
    )


_NbsCmmcChassisResetAllModules_Type.__name__ = "Integer32"
_NbsCmmcChassisResetAllModules_Object = MibTableColumn
nbsCmmcChassisResetAllModules = _NbsCmmcChassisResetAllModules_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 26),
    _NbsCmmcChassisResetAllModules_Type()
)
nbsCmmcChassisResetAllModules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisResetAllModules.setStatus("current")


class _NbsCmmcChassisEnableModuleSpecificTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableModuleSpecificTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableModuleSpecificTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableModuleSpecificTraps_Object = MibTableColumn
nbsCmmcChassisEnableModuleSpecificTraps = _NbsCmmcChassisEnableModuleSpecificTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 27),
    _NbsCmmcChassisEnableModuleSpecificTraps_Type()
)
nbsCmmcChassisEnableModuleSpecificTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableModuleSpecificTraps.setStatus("current")


class _NbsCmmcChassisLoopbackTimeout_Type(Integer32):
    """Custom type nbsCmmcChassisLoopbackTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NbsCmmcChassisLoopbackTimeout_Type.__name__ = "Integer32"
_NbsCmmcChassisLoopbackTimeout_Object = MibTableColumn
nbsCmmcChassisLoopbackTimeout = _NbsCmmcChassisLoopbackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 28),
    _NbsCmmcChassisLoopbackTimeout_Type()
)
nbsCmmcChassisLoopbackTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisLoopbackTimeout.setStatus("current")
_NbsCmmcChassisPortInfoBitMap_Type = OctetString
_NbsCmmcChassisPortInfoBitMap_Object = MibTableColumn
nbsCmmcChassisPortInfoBitMap = _NbsCmmcChassisPortInfoBitMap_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 29),
    _NbsCmmcChassisPortInfoBitMap_Type()
)
nbsCmmcChassisPortInfoBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisPortInfoBitMap.setStatus("current")
_NbsCmmcChassisSlotListBitMap_Type = OctetString
_NbsCmmcChassisSlotListBitMap_Object = MibTableColumn
nbsCmmcChassisSlotListBitMap = _NbsCmmcChassisSlotListBitMap_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 30),
    _NbsCmmcChassisSlotListBitMap_Type()
)
nbsCmmcChassisSlotListBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisSlotListBitMap.setStatus("current")
_NbsCmmcChassisNumberOfPortsBitMap_Type = OctetString
_NbsCmmcChassisNumberOfPortsBitMap_Object = MibTableColumn
nbsCmmcChassisNumberOfPortsBitMap = _NbsCmmcChassisNumberOfPortsBitMap_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 31),
    _NbsCmmcChassisNumberOfPortsBitMap_Type()
)
nbsCmmcChassisNumberOfPortsBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisNumberOfPortsBitMap.setStatus("current")


class _NbsCmmcChassisName_Type(DisplayString):
    """Custom type nbsCmmcChassisName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcChassisName_Type.__name__ = "DisplayString"
_NbsCmmcChassisName_Object = MibTableColumn
nbsCmmcChassisName = _NbsCmmcChassisName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 32),
    _NbsCmmcChassisName_Type()
)
nbsCmmcChassisName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisName.setStatus("current")


class _NbsCmmcChassisEnableLINTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableLINTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableLINTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableLINTraps_Object = MibTableColumn
nbsCmmcChassisEnableLINTraps = _NbsCmmcChassisEnableLINTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 33),
    _NbsCmmcChassisEnableLINTraps_Type()
)
nbsCmmcChassisEnableLINTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableLINTraps.setStatus("current")


class _NbsCmmcChassisEnablePortChangeTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnablePortChangeTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnablePortChangeTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnablePortChangeTraps_Object = MibTableColumn
nbsCmmcChassisEnablePortChangeTraps = _NbsCmmcChassisEnablePortChangeTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 34),
    _NbsCmmcChassisEnablePortChangeTraps_Type()
)
nbsCmmcChassisEnablePortChangeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnablePortChangeTraps.setStatus("current")


class _NbsCmmcChassisEnablePortDiagsTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnablePortDiagsTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnablePortDiagsTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnablePortDiagsTraps_Object = MibTableColumn
nbsCmmcChassisEnablePortDiagsTraps = _NbsCmmcChassisEnablePortDiagsTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 35),
    _NbsCmmcChassisEnablePortDiagsTraps_Type()
)
nbsCmmcChassisEnablePortDiagsTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnablePortDiagsTraps.setStatus("current")


class _NbsCmmcChassisFan5Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan5Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan5Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan5Status_Object = MibTableColumn
nbsCmmcChassisFan5Status = _NbsCmmcChassisFan5Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 36),
    _NbsCmmcChassisFan5Status_Type()
)
nbsCmmcChassisFan5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan5Status.setStatus("current")


class _NbsCmmcChassisFan6Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan6Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan6Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan6Status_Object = MibTableColumn
nbsCmmcChassisFan6Status = _NbsCmmcChassisFan6Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 37),
    _NbsCmmcChassisFan6Status_Type()
)
nbsCmmcChassisFan6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan6Status.setStatus("current")


class _NbsCmmcChassisFan7Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan7Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan7Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan7Status_Object = MibTableColumn
nbsCmmcChassisFan7Status = _NbsCmmcChassisFan7Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 38),
    _NbsCmmcChassisFan7Status_Type()
)
nbsCmmcChassisFan7Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan7Status.setStatus("current")


class _NbsCmmcChassisFan8Status_Type(Integer32):
    """Custom type nbsCmmcChassisFan8Status based on Integer32"""
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
        *(("bad", 2),
          ("good", 3),
          ("notInstalled", 4),
          ("notSupported", 1))
    )


_NbsCmmcChassisFan8Status_Type.__name__ = "Integer32"
_NbsCmmcChassisFan8Status_Object = MibTableColumn
nbsCmmcChassisFan8Status = _NbsCmmcChassisFan8Status_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 39),
    _NbsCmmcChassisFan8Status_Type()
)
nbsCmmcChassisFan8Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFan8Status.setStatus("current")


class _NbsCmmcChassisEnableSwitchoverTraps_Type(Integer32):
    """Custom type nbsCmmcChassisEnableSwitchoverTraps based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcChassisEnableSwitchoverTraps_Type.__name__ = "Integer32"
_NbsCmmcChassisEnableSwitchoverTraps_Object = MibTableColumn
nbsCmmcChassisEnableSwitchoverTraps = _NbsCmmcChassisEnableSwitchoverTraps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 40),
    _NbsCmmcChassisEnableSwitchoverTraps_Type()
)
nbsCmmcChassisEnableSwitchoverTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisEnableSwitchoverTraps.setStatus("current")


class _NbsCmmcChassisCrossConnect_Type(Integer32):
    """Custom type nbsCmmcChassisCrossConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcChassisCrossConnect_Type.__name__ = "Integer32"
_NbsCmmcChassisCrossConnect_Object = MibTableColumn
nbsCmmcChassisCrossConnect = _NbsCmmcChassisCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 41),
    _NbsCmmcChassisCrossConnect_Type()
)
nbsCmmcChassisCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisCrossConnect.setStatus("current")


class _NbsCmmcChassisNVAreaBanks_Type(Integer32):
    """Custom type nbsCmmcChassisNVAreaBanks based on Integer32"""
    defaultValue = 0


_NbsCmmcChassisNVAreaBanks_Object = MibTableColumn
nbsCmmcChassisNVAreaBanks = _NbsCmmcChassisNVAreaBanks_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 42),
    _NbsCmmcChassisNVAreaBanks_Type()
)
nbsCmmcChassisNVAreaBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisNVAreaBanks.setStatus("current")


class _NbsCmmcChassisFirmwareCaps_Type(OctetString):
    """Custom type nbsCmmcChassisFirmwareCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsCmmcChassisFirmwareCaps_Type.__name__ = "OctetString"
_NbsCmmcChassisFirmwareCaps_Object = MibTableColumn
nbsCmmcChassisFirmwareCaps = _NbsCmmcChassisFirmwareCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 43),
    _NbsCmmcChassisFirmwareCaps_Type()
)
nbsCmmcChassisFirmwareCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFirmwareCaps.setStatus("current")


class _NbsCmmcChassisFirmwareLoad_Type(OctetString):
    """Custom type nbsCmmcChassisFirmwareLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsCmmcChassisFirmwareLoad_Type.__name__ = "OctetString"
_NbsCmmcChassisFirmwareLoad_Object = MibTableColumn
nbsCmmcChassisFirmwareLoad = _NbsCmmcChassisFirmwareLoad_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 44),
    _NbsCmmcChassisFirmwareLoad_Type()
)
nbsCmmcChassisFirmwareLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisFirmwareLoad.setStatus("current")


class _NbsCmmcChassisNVAreaAdmin_Type(Integer32):
    """Custom type nbsCmmcChassisNVAreaAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcChassisNVAreaAdmin_Object = MibTableColumn
nbsCmmcChassisNVAreaAdmin = _NbsCmmcChassisNVAreaAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 45),
    _NbsCmmcChassisNVAreaAdmin_Type()
)
nbsCmmcChassisNVAreaAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisNVAreaAdmin.setStatus("current")


class _NbsCmmcChassisNVAreaOper_Type(Integer32):
    """Custom type nbsCmmcChassisNVAreaOper based on Integer32"""
    defaultValue = 0


_NbsCmmcChassisNVAreaOper_Object = MibTableColumn
nbsCmmcChassisNVAreaOper = _NbsCmmcChassisNVAreaOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 46),
    _NbsCmmcChassisNVAreaOper_Type()
)
nbsCmmcChassisNVAreaOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisNVAreaOper.setStatus("current")


class _NbsCmmcChassisLoader_Type(Integer32):
    """Custom type nbsCmmcChassisLoader based on Integer32"""
    defaultValue = 0


_NbsCmmcChassisLoader_Object = MibTableColumn
nbsCmmcChassisLoader = _NbsCmmcChassisLoader_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 47),
    _NbsCmmcChassisLoader_Type()
)
nbsCmmcChassisLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisLoader.setStatus("current")


class _NbsCmmcChassisSerialNum_Type(DisplayString):
    """Custom type nbsCmmcChassisSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NbsCmmcChassisSerialNum_Type.__name__ = "DisplayString"
_NbsCmmcChassisSerialNum_Object = MibTableColumn
nbsCmmcChassisSerialNum = _NbsCmmcChassisSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 48),
    _NbsCmmcChassisSerialNum_Type()
)
nbsCmmcChassisSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisSerialNum.setStatus("current")


class _NbsCmmcChassisFace_Type(OctetString):
    """Custom type nbsCmmcChassisFace based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_NbsCmmcChassisFace_Type.__name__ = "OctetString"
_NbsCmmcChassisFace_Object = MibTableColumn
nbsCmmcChassisFace = _NbsCmmcChassisFace_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 49),
    _NbsCmmcChassisFace_Type()
)
nbsCmmcChassisFace.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisFace.setStatus("current")


class _NbsCmmcChassisCountersState_Type(Integer32):
    """Custom type nbsCmmcChassisCountersState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsCmmcChassisCountersState_Type.__name__ = "Integer32"
_NbsCmmcChassisCountersState_Object = MibTableColumn
nbsCmmcChassisCountersState = _NbsCmmcChassisCountersState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 1, 1, 50),
    _NbsCmmcChassisCountersState_Type()
)
nbsCmmcChassisCountersState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcChassisCountersState.setStatus("current")
_NbsCmmcChassisCount_Type = Integer32
_NbsCmmcChassisCount_Object = MibScalar
nbsCmmcChassisCount = _NbsCmmcChassisCount_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 6, 2),
    _NbsCmmcChassisCount_Type()
)
nbsCmmcChassisCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcChassisCount.setStatus("current")
_NbsCmmcSlotGrp_ObjectIdentity = ObjectIdentity
nbsCmmcSlotGrp = _NbsCmmcSlotGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 7)
)
if mibBuilder.loadTexts:
    nbsCmmcSlotGrp.setStatus("current")
_NbsCmmcSlotTable_Object = MibTable
nbsCmmcSlotTable = _NbsCmmcSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1)
)
if mibBuilder.loadTexts:
    nbsCmmcSlotTable.setStatus("current")
_NbsCmmcSlotEntry_Object = MibTableRow
nbsCmmcSlotEntry = _NbsCmmcSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1)
)
nbsCmmcSlotEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSlotChassisIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSlotEntry.setStatus("current")
_NbsCmmcSlotChassisIndex_Type = Integer32
_NbsCmmcSlotChassisIndex_Object = MibTableColumn
nbsCmmcSlotChassisIndex = _NbsCmmcSlotChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 1),
    _NbsCmmcSlotChassisIndex_Type()
)
nbsCmmcSlotChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotChassisIndex.setStatus("current")
_NbsCmmcSlotIndex_Type = Integer32
_NbsCmmcSlotIndex_Object = MibTableColumn
nbsCmmcSlotIndex = _NbsCmmcSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 2),
    _NbsCmmcSlotIndex_Type()
)
nbsCmmcSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotIndex.setStatus("current")
_NbsCmmcSlotType_Type = Integer32
_NbsCmmcSlotType_Object = MibTableColumn
nbsCmmcSlotType = _NbsCmmcSlotType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 3),
    _NbsCmmcSlotType_Type()
)
nbsCmmcSlotType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotType.setStatus("current")


class _NbsCmmcSlotModel_Type(DisplayString):
    """Custom type nbsCmmcSlotModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcSlotModel_Type.__name__ = "DisplayString"
_NbsCmmcSlotModel_Object = MibTableColumn
nbsCmmcSlotModel = _NbsCmmcSlotModel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 4),
    _NbsCmmcSlotModel_Type()
)
nbsCmmcSlotModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotModel.setStatus("current")
_NbsCmmcSlotObjectId_Type = ObjectIdentifier
_NbsCmmcSlotObjectId_Object = MibTableColumn
nbsCmmcSlotObjectId = _NbsCmmcSlotObjectId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 5),
    _NbsCmmcSlotObjectId_Type()
)
nbsCmmcSlotObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotObjectId.setStatus("current")


class _NbsCmmcSlotNumberOfPorts_Type(Integer32):
    """Custom type nbsCmmcSlotNumberOfPorts based on Integer32"""
    defaultValue = 0


_NbsCmmcSlotNumberOfPorts_Object = MibTableColumn
nbsCmmcSlotNumberOfPorts = _NbsCmmcSlotNumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 6),
    _NbsCmmcSlotNumberOfPorts_Type()
)
nbsCmmcSlotNumberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotNumberOfPorts.setStatus("current")


class _NbsCmmcSlotHardwareRevision_Type(DisplayString):
    """Custom type nbsCmmcSlotHardwareRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsCmmcSlotHardwareRevision_Type.__name__ = "DisplayString"
_NbsCmmcSlotHardwareRevision_Object = MibTableColumn
nbsCmmcSlotHardwareRevision = _NbsCmmcSlotHardwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 7),
    _NbsCmmcSlotHardwareRevision_Type()
)
nbsCmmcSlotHardwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotHardwareRevision.setStatus("current")


class _NbsCmmcSlotOperationType_Type(Integer32):
    """Custom type nbsCmmcSlotOperationType based on Integer32"""
    defaultValue = 1

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
              38)
        )
    )
    namedValues = NamedValues(
        *(("addDropMux", 34),
          ("centralOffice", 13),
          ("coDualActive", 25),
          ("coDualInactive", 26),
          ("converter", 3),
          ("customerPremise", 14),
          ("deprecated16", 16),
          ("deprecated17", 17),
          ("deprecated18", 18),
          ("fastRepeater", 7),
          ("gigabitRepeater", 8),
          ("management", 2),
          ("monitor", 9),
          ("multiCO10g", 33),
          ("multiCO1g", 32),
          ("multicast", 35),
          ("multiplexer", 15),
          ("multiplexer4x10G", 38),
          ("optAmpBoosterAGC", 19),
          ("optAmpBoosterAPC", 20),
          ("optAmpInlineAGC", 21),
          ("optAmpInlineAPC", 22),
          ("optAmpMidstageAGC", 30),
          ("optAmpMidstageAPC", 31),
          ("optAmpPreampAGC", 23),
          ("optAmpPreampAPC", 24),
          ("optAmpVariableGain", 29),
          ("optAttenuator", 36),
          ("opticSwitch", 10),
          ("other", 1),
          ("packetMux", 28),
          ("physLayerSwitch", 27),
          ("redundant", 12),
          ("remote", 11),
          ("repeater", 4),
          ("repeater40G", 37),
          ("splitterCombiner", 6),
          ("switch", 5))
    )


_NbsCmmcSlotOperationType_Type.__name__ = "Integer32"
_NbsCmmcSlotOperationType_Object = MibTableColumn
nbsCmmcSlotOperationType = _NbsCmmcSlotOperationType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 8),
    _NbsCmmcSlotOperationType_Type()
)
nbsCmmcSlotOperationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotOperationType.setStatus("current")


class _NbsCmmcSlotReset_Type(Integer32):
    """Custom type nbsCmmcSlotReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("deprecatedPhy", 3),
          ("deprecatedQueue", 4),
          ("initSlot", 6),
          ("notSupported", 1),
          ("operating", 2),
          ("resetSlot", 5),
          ("resetWarm", 7))
    )


_NbsCmmcSlotReset_Type.__name__ = "Integer32"
_NbsCmmcSlotReset_Object = MibTableColumn
nbsCmmcSlotReset = _NbsCmmcSlotReset_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 9),
    _NbsCmmcSlotReset_Type()
)
nbsCmmcSlotReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotReset.setStatus("current")


class _NbsCmmcSlotName_Type(DisplayString):
    """Custom type nbsCmmcSlotName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcSlotName_Type.__name__ = "DisplayString"
_NbsCmmcSlotName_Object = MibTableColumn
nbsCmmcSlotName = _NbsCmmcSlotName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 10),
    _NbsCmmcSlotName_Type()
)
nbsCmmcSlotName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotName.setStatus("current")
_NbsCmmcSlotModuleType_Type = Integer32
_NbsCmmcSlotModuleType_Object = MibTableColumn
nbsCmmcSlotModuleType = _NbsCmmcSlotModuleType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 11),
    _NbsCmmcSlotModuleType_Type()
)
nbsCmmcSlotModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotModuleType.setStatus("current")


class _NbsCmmcSlotModuleSlot_Type(Integer32):
    """Custom type nbsCmmcSlotModuleSlot based on Integer32"""
    defaultValue = 1


_NbsCmmcSlotModuleSlot_Object = MibTableColumn
nbsCmmcSlotModuleSlot = _NbsCmmcSlotModuleSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 12),
    _NbsCmmcSlotModuleSlot_Type()
)
nbsCmmcSlotModuleSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotModuleSlot.setStatus("current")


class _NbsCmmcSlotSwConfigurable_Type(Integer32):
    """Custom type nbsCmmcSlotSwConfigurable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("other", 1),
          ("yes", 3))
    )


_NbsCmmcSlotSwConfigurable_Type.__name__ = "Integer32"
_NbsCmmcSlotSwConfigurable_Object = MibTableColumn
nbsCmmcSlotSwConfigurable = _NbsCmmcSlotSwConfigurable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 13),
    _NbsCmmcSlotSwConfigurable_Type()
)
nbsCmmcSlotSwConfigurable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotSwConfigurable.setStatus("current")


class _NbsCmmcSlotConfiguration_Type(OctetString):
    """Custom type nbsCmmcSlotConfiguration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_NbsCmmcSlotConfiguration_Type.__name__ = "OctetString"
_NbsCmmcSlotConfiguration_Object = MibTableColumn
nbsCmmcSlotConfiguration = _NbsCmmcSlotConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 14),
    _NbsCmmcSlotConfiguration_Type()
)
nbsCmmcSlotConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotConfiguration.setStatus("current")


class _NbsCmmcSlotMacAddress_Type(OctetString):
    """Custom type nbsCmmcSlotMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_NbsCmmcSlotMacAddress_Type.__name__ = "OctetString"
_NbsCmmcSlotMacAddress_Object = MibTableColumn
nbsCmmcSlotMacAddress = _NbsCmmcSlotMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 15),
    _NbsCmmcSlotMacAddress_Type()
)
nbsCmmcSlotMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotMacAddress.setStatus("current")
_NbsCmmcSlotIPAddress_Type = IpAddress
_NbsCmmcSlotIPAddress_Object = MibTableColumn
nbsCmmcSlotIPAddress = _NbsCmmcSlotIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 16),
    _NbsCmmcSlotIPAddress_Type()
)
nbsCmmcSlotIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotIPAddress.setStatus("current")
_NbsCmmcSlotSubnetMask_Type = IpAddress
_NbsCmmcSlotSubnetMask_Object = MibTableColumn
nbsCmmcSlotSubnetMask = _NbsCmmcSlotSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 17),
    _NbsCmmcSlotSubnetMask_Type()
)
nbsCmmcSlotSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotSubnetMask.setStatus("current")
_NbsCmmcSlotBroadcastAddr_Type = IpAddress
_NbsCmmcSlotBroadcastAddr_Object = MibTableColumn
nbsCmmcSlotBroadcastAddr = _NbsCmmcSlotBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 18),
    _NbsCmmcSlotBroadcastAddr_Type()
)
nbsCmmcSlotBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotBroadcastAddr.setStatus("current")
_NbsCmmcSlotDefGateway_Type = IpAddress
_NbsCmmcSlotDefGateway_Object = MibTableColumn
nbsCmmcSlotDefGateway = _NbsCmmcSlotDefGateway_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 19),
    _NbsCmmcSlotDefGateway_Type()
)
nbsCmmcSlotDefGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotDefGateway.setStatus("current")


class _NbsCmmcSlotHoming_Type(Integer32):
    """Custom type nbsCmmcSlotHoming based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualCOs", 3),
          ("notSupported", 1),
          ("singleCO", 2))
    )


_NbsCmmcSlotHoming_Type.__name__ = "Integer32"
_NbsCmmcSlotHoming_Object = MibTableColumn
nbsCmmcSlotHoming = _NbsCmmcSlotHoming_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 20),
    _NbsCmmcSlotHoming_Type()
)
nbsCmmcSlotHoming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotHoming.setStatus("current")


class _NbsCmmcSlotRedundancy_Type(Integer32):
    """Custom type nbsCmmcSlotRedundancy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSlotRedundancy_Type.__name__ = "Integer32"
_NbsCmmcSlotRedundancy_Object = MibTableColumn
nbsCmmcSlotRedundancy = _NbsCmmcSlotRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 21),
    _NbsCmmcSlotRedundancy_Type()
)
nbsCmmcSlotRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotRedundancy.setStatus("current")


class _NbsCmmcSlotDescr_Type(DisplayString):
    """Custom type nbsCmmcSlotDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NbsCmmcSlotDescr_Type.__name__ = "DisplayString"
_NbsCmmcSlotDescr_Object = MibTableColumn
nbsCmmcSlotDescr = _NbsCmmcSlotDescr_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 22),
    _NbsCmmcSlotDescr_Type()
)
nbsCmmcSlotDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotDescr.setStatus("current")


class _NbsCmmcSlotUpgradable_Type(Integer32):
    """Custom type nbsCmmcSlotUpgradable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_NbsCmmcSlotUpgradable_Type.__name__ = "Integer32"
_NbsCmmcSlotUpgradable_Object = MibTableColumn
nbsCmmcSlotUpgradable = _NbsCmmcSlotUpgradable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 23),
    _NbsCmmcSlotUpgradable_Type()
)
nbsCmmcSlotUpgradable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotUpgradable.setStatus("current")


class _NbsCmmcSlotCrossConnect_Type(Integer32):
    """Custom type nbsCmmcSlotCrossConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcSlotCrossConnect_Type.__name__ = "Integer32"
_NbsCmmcSlotCrossConnect_Object = MibTableColumn
nbsCmmcSlotCrossConnect = _NbsCmmcSlotCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 24),
    _NbsCmmcSlotCrossConnect_Type()
)
nbsCmmcSlotCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotCrossConnect.setStatus("current")


class _NbsCmmcSlotClearType_Type(Integer32):
    """Custom type nbsCmmcSlotClearType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearType", 3),
          ("idle", 2),
          ("notSupported", 1))
    )


_NbsCmmcSlotClearType_Type.__name__ = "Integer32"
_NbsCmmcSlotClearType_Object = MibTableColumn
nbsCmmcSlotClearType = _NbsCmmcSlotClearType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 25),
    _NbsCmmcSlotClearType_Type()
)
nbsCmmcSlotClearType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotClearType.setStatus("current")


class _NbsCmmcSlotNVAreaBanks_Type(Integer32):
    """Custom type nbsCmmcSlotNVAreaBanks based on Integer32"""
    defaultValue = 0


_NbsCmmcSlotNVAreaBanks_Object = MibTableColumn
nbsCmmcSlotNVAreaBanks = _NbsCmmcSlotNVAreaBanks_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 26),
    _NbsCmmcSlotNVAreaBanks_Type()
)
nbsCmmcSlotNVAreaBanks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotNVAreaBanks.setStatus("current")


class _NbsCmmcSlotFirmwareCaps_Type(OctetString):
    """Custom type nbsCmmcSlotFirmwareCaps based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsCmmcSlotFirmwareCaps_Type.__name__ = "OctetString"
_NbsCmmcSlotFirmwareCaps_Object = MibTableColumn
nbsCmmcSlotFirmwareCaps = _NbsCmmcSlotFirmwareCaps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 27),
    _NbsCmmcSlotFirmwareCaps_Type()
)
nbsCmmcSlotFirmwareCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotFirmwareCaps.setStatus("current")


class _NbsCmmcSlotFirmwareLoad_Type(OctetString):
    """Custom type nbsCmmcSlotFirmwareLoad based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_NbsCmmcSlotFirmwareLoad_Type.__name__ = "OctetString"
_NbsCmmcSlotFirmwareLoad_Object = MibTableColumn
nbsCmmcSlotFirmwareLoad = _NbsCmmcSlotFirmwareLoad_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 28),
    _NbsCmmcSlotFirmwareLoad_Type()
)
nbsCmmcSlotFirmwareLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotFirmwareLoad.setStatus("current")


class _NbsCmmcSlotNVAreaAdmin_Type(Integer32):
    """Custom type nbsCmmcSlotNVAreaAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcSlotNVAreaAdmin_Object = MibTableColumn
nbsCmmcSlotNVAreaAdmin = _NbsCmmcSlotNVAreaAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 29),
    _NbsCmmcSlotNVAreaAdmin_Type()
)
nbsCmmcSlotNVAreaAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotNVAreaAdmin.setStatus("current")


class _NbsCmmcSlotNVAreaOper_Type(Integer32):
    """Custom type nbsCmmcSlotNVAreaOper based on Integer32"""
    defaultValue = 0


_NbsCmmcSlotNVAreaOper_Object = MibTableColumn
nbsCmmcSlotNVAreaOper = _NbsCmmcSlotNVAreaOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 30),
    _NbsCmmcSlotNVAreaOper_Type()
)
nbsCmmcSlotNVAreaOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotNVAreaOper.setStatus("current")


class _NbsCmmcSlotLoader_Type(Integer32):
    """Custom type nbsCmmcSlotLoader based on Integer32"""
    defaultValue = 0


_NbsCmmcSlotLoader_Object = MibTableColumn
nbsCmmcSlotLoader = _NbsCmmcSlotLoader_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 31),
    _NbsCmmcSlotLoader_Type()
)
nbsCmmcSlotLoader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotLoader.setStatus("current")


class _NbsCmmcSlotSerialNum_Type(DisplayString):
    """Custom type nbsCmmcSlotSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_NbsCmmcSlotSerialNum_Type.__name__ = "DisplayString"
_NbsCmmcSlotSerialNum_Object = MibTableColumn
nbsCmmcSlotSerialNum = _NbsCmmcSlotSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 32),
    _NbsCmmcSlotSerialNum_Type()
)
nbsCmmcSlotSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotSerialNum.setStatus("current")


class _NbsCmmcSlotToggleRate_Type(Integer32):
    """Custom type nbsCmmcSlotToggleRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NbsCmmcSlotToggleRate_Type.__name__ = "Integer32"
_NbsCmmcSlotToggleRate_Object = MibTableColumn
nbsCmmcSlotToggleRate = _NbsCmmcSlotToggleRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 33),
    _NbsCmmcSlotToggleRate_Type()
)
nbsCmmcSlotToggleRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotToggleRate.setStatus("current")


class _NbsCmmcSlotTemperature_Type(Integer32):
    """Custom type nbsCmmcSlotTemperature based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcSlotTemperature_Type.__name__ = "Integer32"
_NbsCmmcSlotTemperature_Object = MibTableColumn
nbsCmmcSlotTemperature = _NbsCmmcSlotTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 34),
    _NbsCmmcSlotTemperature_Type()
)
nbsCmmcSlotTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotTemperature.setStatus("current")


class _NbsCmmcSlotCountersState_Type(Integer32):
    """Custom type nbsCmmcSlotCountersState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsCmmcSlotCountersState_Type.__name__ = "Integer32"
_NbsCmmcSlotCountersState_Object = MibTableColumn
nbsCmmcSlotCountersState = _NbsCmmcSlotCountersState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 35),
    _NbsCmmcSlotCountersState_Type()
)
nbsCmmcSlotCountersState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSlotCountersState.setStatus("current")


class _NbsCmmcSlotRedundancyOper_Type(Integer32):
    """Custom type nbsCmmcSlotRedundancyOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcSlotRedundancyOper_Type.__name__ = "Integer32"
_NbsCmmcSlotRedundancyOper_Object = MibTableColumn
nbsCmmcSlotRedundancyOper = _NbsCmmcSlotRedundancyOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 1, 1, 36),
    _NbsCmmcSlotRedundancyOper_Type()
)
nbsCmmcSlotRedundancyOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotRedundancyOper.setStatus("current")
_NbsCmmcLedTable_Object = MibTable
nbsCmmcLedTable = _NbsCmmcLedTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2)
)
if mibBuilder.loadTexts:
    nbsCmmcLedTable.setStatus("current")
_NbsCmmcLedEntry_Object = MibTableRow
nbsCmmcLedEntry = _NbsCmmcLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1)
)
nbsCmmcLedEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcLedChassisIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcLedSlotIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcLedIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcLedEntry.setStatus("current")
_NbsCmmcLedChassisIndex_Type = Integer32
_NbsCmmcLedChassisIndex_Object = MibTableColumn
nbsCmmcLedChassisIndex = _NbsCmmcLedChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1, 1),
    _NbsCmmcLedChassisIndex_Type()
)
nbsCmmcLedChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcLedChassisIndex.setStatus("current")
_NbsCmmcLedSlotIndex_Type = Integer32
_NbsCmmcLedSlotIndex_Object = MibTableColumn
nbsCmmcLedSlotIndex = _NbsCmmcLedSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1, 2),
    _NbsCmmcLedSlotIndex_Type()
)
nbsCmmcLedSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcLedSlotIndex.setStatus("current")
_NbsCmmcLedIndex_Type = Integer32
_NbsCmmcLedIndex_Object = MibTableColumn
nbsCmmcLedIndex = _NbsCmmcLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1, 3),
    _NbsCmmcLedIndex_Type()
)
nbsCmmcLedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcLedIndex.setStatus("current")


class _NbsCmmcLedColor_Type(Integer32):
    """Custom type nbsCmmcLedColor based on Integer32"""
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
        *(("amber", 3),
          ("green", 2),
          ("off", 1),
          ("other", 4))
    )


_NbsCmmcLedColor_Type.__name__ = "Integer32"
_NbsCmmcLedColor_Object = MibTableColumn
nbsCmmcLedColor = _NbsCmmcLedColor_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1, 4),
    _NbsCmmcLedColor_Type()
)
nbsCmmcLedColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcLedColor.setStatus("current")


class _NbsCmmcLedDescription_Type(DisplayString):
    """Custom type nbsCmmcLedDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcLedDescription_Type.__name__ = "DisplayString"
_NbsCmmcLedDescription_Object = MibTableColumn
nbsCmmcLedDescription = _NbsCmmcLedDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 2, 1, 5),
    _NbsCmmcLedDescription_Type()
)
nbsCmmcLedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcLedDescription.setStatus("current")
_NbsCmmcSlotFaceTable_Object = MibTable
nbsCmmcSlotFaceTable = _NbsCmmcSlotFaceTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3)
)
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceTable.setStatus("current")
_NbsCmmcSlotFaceEntry_Object = MibTableRow
nbsCmmcSlotFaceEntry = _NbsCmmcSlotFaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3, 1)
)
nbsCmmcSlotFaceEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSlotFaceChassisIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcSlotFaceSlotIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcSlotFaceRowIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceEntry.setStatus("current")
_NbsCmmcSlotFaceChassisIndex_Type = Integer32
_NbsCmmcSlotFaceChassisIndex_Object = MibTableColumn
nbsCmmcSlotFaceChassisIndex = _NbsCmmcSlotFaceChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3, 1, 1),
    _NbsCmmcSlotFaceChassisIndex_Type()
)
nbsCmmcSlotFaceChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceChassisIndex.setStatus("current")
_NbsCmmcSlotFaceSlotIndex_Type = Integer32
_NbsCmmcSlotFaceSlotIndex_Object = MibTableColumn
nbsCmmcSlotFaceSlotIndex = _NbsCmmcSlotFaceSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3, 1, 2),
    _NbsCmmcSlotFaceSlotIndex_Type()
)
nbsCmmcSlotFaceSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceSlotIndex.setStatus("current")
_NbsCmmcSlotFaceRowIndex_Type = Integer32
_NbsCmmcSlotFaceRowIndex_Object = MibTableColumn
nbsCmmcSlotFaceRowIndex = _NbsCmmcSlotFaceRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3, 1, 3),
    _NbsCmmcSlotFaceRowIndex_Type()
)
nbsCmmcSlotFaceRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceRowIndex.setStatus("current")


class _NbsCmmcSlotFaceSummary_Type(OctetString):
    """Custom type nbsCmmcSlotFaceSummary based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 500),
    )


_NbsCmmcSlotFaceSummary_Type.__name__ = "OctetString"
_NbsCmmcSlotFaceSummary_Object = MibTableColumn
nbsCmmcSlotFaceSummary = _NbsCmmcSlotFaceSummary_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 7, 3, 1, 4),
    _NbsCmmcSlotFaceSummary_Type()
)
nbsCmmcSlotFaceSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSlotFaceSummary.setStatus("current")
_NbsCmmcPortGrp_ObjectIdentity = ObjectIdentity
nbsCmmcPortGrp = _NbsCmmcPortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 8)
)
if mibBuilder.loadTexts:
    nbsCmmcPortGrp.setStatus("current")
_NbsCmmcPortTable_Object = MibTable
nbsCmmcPortTable = _NbsCmmcPortTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1)
)
if mibBuilder.loadTexts:
    nbsCmmcPortTable.setStatus("current")
_NbsCmmcPortEntry_Object = MibTableRow
nbsCmmcPortEntry = _NbsCmmcPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1)
)
nbsCmmcPortEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcPortChassisIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcPortSlotIndex"),
    (0, "NBS-CMMC-MIB", "nbsCmmcPortIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcPortEntry.setStatus("current")
_NbsCmmcPortChassisIndex_Type = Integer32
_NbsCmmcPortChassisIndex_Object = MibTableColumn
nbsCmmcPortChassisIndex = _NbsCmmcPortChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 1),
    _NbsCmmcPortChassisIndex_Type()
)
nbsCmmcPortChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortChassisIndex.setStatus("current")
_NbsCmmcPortSlotIndex_Type = Integer32
_NbsCmmcPortSlotIndex_Object = MibTableColumn
nbsCmmcPortSlotIndex = _NbsCmmcPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 2),
    _NbsCmmcPortSlotIndex_Type()
)
nbsCmmcPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortSlotIndex.setStatus("current")
_NbsCmmcPortIndex_Type = Integer32
_NbsCmmcPortIndex_Object = MibTableColumn
nbsCmmcPortIndex = _NbsCmmcPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 3),
    _NbsCmmcPortIndex_Type()
)
nbsCmmcPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortIndex.setStatus("current")
_NbsCmmcPortType_Type = Integer32
_NbsCmmcPortType_Object = MibTableColumn
nbsCmmcPortType = _NbsCmmcPortType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 4),
    _NbsCmmcPortType_Type()
)
nbsCmmcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortType.setStatus("current")
_NbsCmmcPortObjectId_Type = ObjectIdentifier
_NbsCmmcPortObjectId_Object = MibTableColumn
nbsCmmcPortObjectId = _NbsCmmcPortObjectId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 5),
    _NbsCmmcPortObjectId_Type()
)
nbsCmmcPortObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortObjectId.setStatus("current")


class _NbsCmmcPortLink_Type(Integer32):
    """Custom type nbsCmmcPortLink based on Integer32"""
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
        *(("link", 4),
          ("lock", 5),
          ("noSignal", 2),
          ("other", 1),
          ("signalDetect", 3))
    )


_NbsCmmcPortLink_Type.__name__ = "Integer32"
_NbsCmmcPortLink_Object = MibTableColumn
nbsCmmcPortLink = _NbsCmmcPortLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 6),
    _NbsCmmcPortLink_Type()
)
nbsCmmcPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortLink.setStatus("current")


class _NbsCmmcPortAutoNegotiation_Type(Integer32):
    """Custom type nbsCmmcPortAutoNegotiation based on Integer32"""
    defaultValue = 3

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
        *(("deprecated4", 4),
          ("deprecated5", 5),
          ("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortAutoNegotiation_Type.__name__ = "Integer32"
_NbsCmmcPortAutoNegotiation_Object = MibTableColumn
nbsCmmcPortAutoNegotiation = _NbsCmmcPortAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 7),
    _NbsCmmcPortAutoNegotiation_Type()
)
nbsCmmcPortAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAutoNegotiation.setStatus("current")


class _NbsCmmcPortDuplex_Type(Integer32):
    """Custom type nbsCmmcPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("notSupported", 1))
    )


_NbsCmmcPortDuplex_Type.__name__ = "Integer32"
_NbsCmmcPortDuplex_Object = MibTableColumn
nbsCmmcPortDuplex = _NbsCmmcPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 8),
    _NbsCmmcPortDuplex_Type()
)
nbsCmmcPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortDuplex.setStatus("current")


class _NbsCmmcPortSpeed_Type(Integer32):
    """Custom type nbsCmmcPortSpeed based on Integer32"""
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
        *(("other", 1),
          ("spd100Mbps", 3),
          ("spd10Gbps", 5),
          ("spd10Mbps", 2),
          ("spdGigabit", 4))
    )


_NbsCmmcPortSpeed_Type.__name__ = "Integer32"
_NbsCmmcPortSpeed_Object = MibTableColumn
nbsCmmcPortSpeed = _NbsCmmcPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 9),
    _NbsCmmcPortSpeed_Type()
)
nbsCmmcPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortSpeed.setStatus("current")


class _NbsCmmcPortRxActivity_Type(Integer32):
    """Custom type nbsCmmcPortRxActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortRxActivity_Type.__name__ = "Integer32"
_NbsCmmcPortRxActivity_Object = MibTableColumn
nbsCmmcPortRxActivity = _NbsCmmcPortRxActivity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 10),
    _NbsCmmcPortRxActivity_Type()
)
nbsCmmcPortRxActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortRxActivity.setStatus("current")


class _NbsCmmcPortTxActivity_Type(Integer32):
    """Custom type nbsCmmcPortTxActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortTxActivity_Type.__name__ = "Integer32"
_NbsCmmcPortTxActivity_Object = MibTableColumn
nbsCmmcPortTxActivity = _NbsCmmcPortTxActivity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 11),
    _NbsCmmcPortTxActivity_Type()
)
nbsCmmcPortTxActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortTxActivity.setStatus("current")


class _NbsCmmcPortCollisionActivity_Type(Integer32):
    """Custom type nbsCmmcPortCollisionActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortCollisionActivity_Type.__name__ = "Integer32"
_NbsCmmcPortCollisionActivity_Object = MibTableColumn
nbsCmmcPortCollisionActivity = _NbsCmmcPortCollisionActivity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 12),
    _NbsCmmcPortCollisionActivity_Type()
)
nbsCmmcPortCollisionActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortCollisionActivity.setStatus("current")


class _NbsCmmcPortLoopback_Type(Integer32):
    """Custom type nbsCmmcPortLoopback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortLoopback_Type.__name__ = "Integer32"
_NbsCmmcPortLoopback_Object = MibTableColumn
nbsCmmcPortLoopback = _NbsCmmcPortLoopback_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 13),
    _NbsCmmcPortLoopback_Type()
)
nbsCmmcPortLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortLoopback.setStatus("current")


class _NbsCmmcPortEnable_Type(Integer32):
    """Custom type nbsCmmcPortEnable based on Integer32"""
    defaultValue = 3

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
        *(("deprecatedAuto", 4),
          ("disable", 2),
          ("enable", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortEnable_Type.__name__ = "Integer32"
_NbsCmmcPortEnable_Object = MibTableColumn
nbsCmmcPortEnable = _NbsCmmcPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 14),
    _NbsCmmcPortEnable_Type()
)
nbsCmmcPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortEnable.setStatus("current")


class _NbsCmmcPortSelectLink_Type(Integer32):
    """Custom type nbsCmmcPortSelectLink based on Integer32"""
    defaultValue = 3

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
        *(("active", 3),
          ("deprecatedActivePreferred", 6),
          ("deprecatedAuto", 4),
          ("deprecatedStandbyPreferred", 5),
          ("notSupported", 1),
          ("standby", 2))
    )


_NbsCmmcPortSelectLink_Type.__name__ = "Integer32"
_NbsCmmcPortSelectLink_Object = MibTableColumn
nbsCmmcPortSelectLink = _NbsCmmcPortSelectLink_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 15),
    _NbsCmmcPortSelectLink_Type()
)
nbsCmmcPortSelectLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortSelectLink.setStatus("current")


class _NbsCmmcPortLIN_Type(Integer32):
    """Custom type nbsCmmcPortLIN based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortLIN_Type.__name__ = "Integer32"
_NbsCmmcPortLIN_Object = MibTableColumn
nbsCmmcPortLIN = _NbsCmmcPortLIN_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 16),
    _NbsCmmcPortLIN_Type()
)
nbsCmmcPortLIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortLIN.setStatus("current")


class _NbsCmmcPortAging_Type(Integer32):
    """Custom type nbsCmmcPortAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortAging_Type.__name__ = "Integer32"
_NbsCmmcPortAging_Object = MibTableColumn
nbsCmmcPortAging = _NbsCmmcPortAging_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 17),
    _NbsCmmcPortAging_Type()
)
nbsCmmcPortAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAging.setStatus("current")


class _NbsCmmcPortMaxPacketSize_Type(Integer32):
    """Custom type nbsCmmcPortMaxPacketSize based on Integer32"""
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
        *(("max1518", 2),
          ("max1536", 3),
          ("max6k", 4),
          ("notSupported", 1))
    )


_NbsCmmcPortMaxPacketSize_Type.__name__ = "Integer32"
_NbsCmmcPortMaxPacketSize_Object = MibTableColumn
nbsCmmcPortMaxPacketSize = _NbsCmmcPortMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 18),
    _NbsCmmcPortMaxPacketSize_Type()
)
nbsCmmcPortMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortMaxPacketSize.setStatus("current")


class _NbsCmmcPortRemoteLoopback_Type(Integer32):
    """Custom type nbsCmmcPortRemoteLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortRemoteLoopback_Type.__name__ = "Integer32"
_NbsCmmcPortRemoteLoopback_Object = MibTableColumn
nbsCmmcPortRemoteLoopback = _NbsCmmcPortRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 19),
    _NbsCmmcPortRemoteLoopback_Type()
)
nbsCmmcPortRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortRemoteLoopback.setStatus("current")


class _NbsCmmcPortErrorActivity_Type(Integer32):
    """Custom type nbsCmmcPortErrorActivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortErrorActivity_Type.__name__ = "Integer32"
_NbsCmmcPortErrorActivity_Object = MibTableColumn
nbsCmmcPortErrorActivity = _NbsCmmcPortErrorActivity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 20),
    _NbsCmmcPortErrorActivity_Type()
)
nbsCmmcPortErrorActivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortErrorActivity.setStatus("current")


class _NbsCmmcPortName_Type(DisplayString):
    """Custom type nbsCmmcPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcPortName_Type.__name__ = "DisplayString"
_NbsCmmcPortName_Object = MibTableColumn
nbsCmmcPortName = _NbsCmmcPortName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 21),
    _NbsCmmcPortName_Type()
)
nbsCmmcPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortName.setStatus("current")


class _NbsCmmcPortValue_Type(OctetString):
    """Custom type nbsCmmcPortValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NbsCmmcPortValue_Type.__name__ = "OctetString"
_NbsCmmcPortValue_Object = MibTableColumn
nbsCmmcPortValue = _NbsCmmcPortValue_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 22),
    _NbsCmmcPortValue_Type()
)
nbsCmmcPortValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortValue.setStatus("current")


class _NbsCmmcPortThreshold_Type(Integer32):
    """Custom type nbsCmmcPortThreshold based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcPortThreshold_Type.__name__ = "Integer32"
_NbsCmmcPortThreshold_Object = MibTableColumn
nbsCmmcPortThreshold = _NbsCmmcPortThreshold_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 23),
    _NbsCmmcPortThreshold_Type()
)
nbsCmmcPortThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortThreshold.setStatus("current")


class _NbsCmmcPortThresholdAction_Type(Integer32):
    """Custom type nbsCmmcPortThresholdAction based on Integer32"""
    defaultValue = 1


_NbsCmmcPortThresholdAction_Object = MibTableColumn
nbsCmmcPortThresholdAction = _NbsCmmcPortThresholdAction_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 24),
    _NbsCmmcPortThresholdAction_Type()
)
nbsCmmcPortThresholdAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortThresholdAction.setStatus("current")


class _NbsCmmcPortRMChassis_Type(Integer32):
    """Custom type nbsCmmcPortRMChassis based on Integer32"""
    defaultValue = 0


_NbsCmmcPortRMChassis_Object = MibTableColumn
nbsCmmcPortRMChassis = _NbsCmmcPortRMChassis_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 25),
    _NbsCmmcPortRMChassis_Type()
)
nbsCmmcPortRMChassis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortRMChassis.setStatus("current")


class _NbsCmmcPortRMSlot_Type(Integer32):
    """Custom type nbsCmmcPortRMSlot based on Integer32"""
    defaultValue = 0


_NbsCmmcPortRMSlot_Object = MibTableColumn
nbsCmmcPortRMSlot = _NbsCmmcPortRMSlot_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 26),
    _NbsCmmcPortRMSlot_Type()
)
nbsCmmcPortRMSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortRMSlot.setStatus("current")


class _NbsCmmcPortRMPort_Type(Integer32):
    """Custom type nbsCmmcPortRMPort based on Integer32"""
    defaultValue = 0


_NbsCmmcPortRMPort_Object = MibTableColumn
nbsCmmcPortRMPort = _NbsCmmcPortRMPort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 27),
    _NbsCmmcPortRMPort_Type()
)
nbsCmmcPortRMPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortRMPort.setStatus("current")


class _NbsCmmcPortSerialNumber_Type(DisplayString):
    """Custom type nbsCmmcPortSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcPortSerialNumber_Type.__name__ = "DisplayString"
_NbsCmmcPortSerialNumber_Object = MibTableColumn
nbsCmmcPortSerialNumber = _NbsCmmcPortSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 28),
    _NbsCmmcPortSerialNumber_Type()
)
nbsCmmcPortSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortSerialNumber.setStatus("current")


class _NbsCmmcPortVendorInfo_Type(DisplayString):
    """Custom type nbsCmmcPortVendorInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcPortVendorInfo_Type.__name__ = "DisplayString"
_NbsCmmcPortVendorInfo_Object = MibTableColumn
nbsCmmcPortVendorInfo = _NbsCmmcPortVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 29),
    _NbsCmmcPortVendorInfo_Type()
)
nbsCmmcPortVendorInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortVendorInfo.setStatus("current")


class _NbsCmmcPortTemperature_Type(Integer32):
    """Custom type nbsCmmcPortTemperature based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcPortTemperature_Type.__name__ = "Integer32"
_NbsCmmcPortTemperature_Object = MibTableColumn
nbsCmmcPortTemperature = _NbsCmmcPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 30),
    _NbsCmmcPortTemperature_Type()
)
nbsCmmcPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortTemperature.setStatus("current")


class _NbsCmmcPortTxPower_Type(Integer32):
    """Custom type nbsCmmcPortTxPower based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcPortTxPower_Type.__name__ = "Integer32"
_NbsCmmcPortTxPower_Object = MibTableColumn
nbsCmmcPortTxPower = _NbsCmmcPortTxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 31),
    _NbsCmmcPortTxPower_Type()
)
nbsCmmcPortTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortTxPower.setStatus("current")


class _NbsCmmcPortRxPower_Type(Integer32):
    """Custom type nbsCmmcPortRxPower based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcPortRxPower_Type.__name__ = "Integer32"
_NbsCmmcPortRxPower_Object = MibTableColumn
nbsCmmcPortRxPower = _NbsCmmcPortRxPower_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 32),
    _NbsCmmcPortRxPower_Type()
)
nbsCmmcPortRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortRxPower.setStatus("current")


class _NbsCmmcPortBiasAmps_Type(Integer32):
    """Custom type nbsCmmcPortBiasAmps based on Integer32"""
    defaultValue = -1


_NbsCmmcPortBiasAmps_Object = MibTableColumn
nbsCmmcPortBiasAmps = _NbsCmmcPortBiasAmps_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 33),
    _NbsCmmcPortBiasAmps_Type()
)
nbsCmmcPortBiasAmps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortBiasAmps.setStatus("current")


class _NbsCmmcPortSupplyVolts_Type(Integer32):
    """Custom type nbsCmmcPortSupplyVolts based on Integer32"""
    defaultValue = -1


_NbsCmmcPortSupplyVolts_Object = MibTableColumn
nbsCmmcPortSupplyVolts = _NbsCmmcPortSupplyVolts_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 34),
    _NbsCmmcPortSupplyVolts_Type()
)
nbsCmmcPortSupplyVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortSupplyVolts.setStatus("current")


class _NbsCmmcPortMedium_Type(Integer32):
    """Custom type nbsCmmcPortMedium based on Integer32"""
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
        *(("coax", 2),
          ("multiMode", 5),
          ("notSupported", 1),
          ("singleMode", 4),
          ("twistedPair", 3))
    )


_NbsCmmcPortMedium_Type.__name__ = "Integer32"
_NbsCmmcPortMedium_Object = MibTableColumn
nbsCmmcPortMedium = _NbsCmmcPortMedium_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 35),
    _NbsCmmcPortMedium_Type()
)
nbsCmmcPortMedium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortMedium.setStatus("current")


class _NbsCmmcPortConnector_Type(Integer32):
    """Custom type nbsCmmcPortConnector based on Integer32"""
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
              32)
        )
    )
    namedValues = NamedValues(
        *(("coax2BNC", 9),
          ("coaxBNC", 8),
          ("coaxF", 7),
          ("coaxHeader", 14),
          ("cuDb9", 12),
          ("cuHssdc", 13),
          ("cuPigtail", 20),
          ("cuRj11", 11),
          ("cuRj45", 5),
          ("cuRj45wLEDs", 10),
          ("cuRj48", 24),
          ("cxp", 32),
          ("firewireA", 22),
          ("firewireB", 23),
          ("fo1LC", 25),
          ("fo2ST", 26),
          ("foDSC", 3),
          ("foFiberJack", 15),
          ("foLC", 6),
          ("foMtRj", 16),
          ("foMu", 17),
          ("foPigtail", 19),
          ("foSC", 4),
          ("miniCoax", 29),
          ("miniSAS4x", 31),
          ("mpo", 30),
          ("removed", 2),
          ("sataDevicePlug", 27),
          ("sataHostPlug", 28),
          ("sg", 18),
          ("smb", 21),
          ("unknown", 1))
    )


_NbsCmmcPortConnector_Type.__name__ = "Integer32"
_NbsCmmcPortConnector_Object = MibTableColumn
nbsCmmcPortConnector = _NbsCmmcPortConnector_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 36),
    _NbsCmmcPortConnector_Type()
)
nbsCmmcPortConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortConnector.setStatus("current")


class _NbsCmmcPortWavelength_Type(Integer32):
    """Custom type nbsCmmcPortWavelength based on Integer32"""
    defaultValue = -1


_NbsCmmcPortWavelength_Object = MibTableColumn
nbsCmmcPortWavelength = _NbsCmmcPortWavelength_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 37),
    _NbsCmmcPortWavelength_Type()
)
nbsCmmcPortWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortWavelength.setStatus("current")


class _NbsCmmcPortDigitalDiags_Type(Integer32):
    """Custom type nbsCmmcPortDigitalDiags based on Integer32"""
    defaultValue = 2

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
        *(("diagsAlarm", 4),
          ("diagsOk", 2),
          ("diagsWarning", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortDigitalDiags_Type.__name__ = "Integer32"
_NbsCmmcPortDigitalDiags_Object = MibTableColumn
nbsCmmcPortDigitalDiags = _NbsCmmcPortDigitalDiags_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 38),
    _NbsCmmcPortDigitalDiags_Type()
)
nbsCmmcPortDigitalDiags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortDigitalDiags.setStatus("current")


class _NbsCmmcPortZoneIdAdmin_Type(Integer32):
    """Custom type nbsCmmcPortZoneIdAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneIdAdmin_Object = MibTableColumn
nbsCmmcPortZoneIdAdmin = _NbsCmmcPortZoneIdAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 39),
    _NbsCmmcPortZoneIdAdmin_Type()
)
nbsCmmcPortZoneIdAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneIdAdmin.setStatus("current")


class _NbsCmmcPortNominalBitRate_Type(Integer32):
    """Custom type nbsCmmcPortNominalBitRate based on Integer32"""
    defaultValue = -1


_NbsCmmcPortNominalBitRate_Object = MibTableColumn
nbsCmmcPortNominalBitRate = _NbsCmmcPortNominalBitRate_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 40),
    _NbsCmmcPortNominalBitRate_Type()
)
nbsCmmcPortNominalBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortNominalBitRate.setStatus("current")
_NbsCmmcPortModulePort_Type = Integer32
_NbsCmmcPortModulePort_Object = MibTableColumn
nbsCmmcPortModulePort = _NbsCmmcPortModulePort_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 41),
    _NbsCmmcPortModulePort_Type()
)
nbsCmmcPortModulePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortModulePort.setStatus("current")


class _NbsCmmcPortPartRev_Type(DisplayString):
    """Custom type nbsCmmcPortPartRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcPortPartRev_Type.__name__ = "DisplayString"
_NbsCmmcPortPartRev_Object = MibTableColumn
nbsCmmcPortPartRev = _NbsCmmcPortPartRev_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 42),
    _NbsCmmcPortPartRev_Type()
)
nbsCmmcPortPartRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortPartRev.setStatus("current")
_NbsCmmcPortIfIndex_Type = Integer32
_NbsCmmcPortIfIndex_Object = MibTableColumn
nbsCmmcPortIfIndex = _NbsCmmcPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 43),
    _NbsCmmcPortIfIndex_Type()
)
nbsCmmcPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortIfIndex.setStatus("current")


class _NbsCmmcPortLinked_Type(Integer32):
    """Custom type nbsCmmcPortLinked based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsCmmcPortLinked_Type.__name__ = "Integer32"
_NbsCmmcPortLinked_Object = MibTableColumn
nbsCmmcPortLinked = _NbsCmmcPortLinked_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 44),
    _NbsCmmcPortLinked_Type()
)
nbsCmmcPortLinked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortLinked.setStatus("current")


class _NbsCmmcPortOperational_Type(Integer32):
    """Custom type nbsCmmcPortOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_NbsCmmcPortOperational_Type.__name__ = "Integer32"
_NbsCmmcPortOperational_Object = MibTableColumn
nbsCmmcPortOperational = _NbsCmmcPortOperational_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 45),
    _NbsCmmcPortOperational_Type()
)
nbsCmmcPortOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortOperational.setStatus("current")


class _NbsCmmcPortZoneChassisAdmin_Type(Integer32):
    """Custom type nbsCmmcPortZoneChassisAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneChassisAdmin_Object = MibTableColumn
nbsCmmcPortZoneChassisAdmin = _NbsCmmcPortZoneChassisAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 46),
    _NbsCmmcPortZoneChassisAdmin_Type()
)
nbsCmmcPortZoneChassisAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneChassisAdmin.setStatus("current")


class _NbsCmmcPortZoneSlotAdmin_Type(Integer32):
    """Custom type nbsCmmcPortZoneSlotAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneSlotAdmin_Object = MibTableColumn
nbsCmmcPortZoneSlotAdmin = _NbsCmmcPortZoneSlotAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 47),
    _NbsCmmcPortZoneSlotAdmin_Type()
)
nbsCmmcPortZoneSlotAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneSlotAdmin.setStatus("current")


class _NbsCmmcPortAlarmCause_Type(DisplayString):
    """Custom type nbsCmmcPortAlarmCause based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcPortAlarmCause_Type.__name__ = "DisplayString"
_NbsCmmcPortAlarmCause_Object = MibTableColumn
nbsCmmcPortAlarmCause = _NbsCmmcPortAlarmCause_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 48),
    _NbsCmmcPortAlarmCause_Type()
)
nbsCmmcPortAlarmCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAlarmCause.setStatus("current")


class _NbsCmmcPortFlowControl_Type(Integer32):
    """Custom type nbsCmmcPortFlowControl based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortFlowControl_Type.__name__ = "Integer32"
_NbsCmmcPortFlowControl_Object = MibTableColumn
nbsCmmcPortFlowControl = _NbsCmmcPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 49),
    _NbsCmmcPortFlowControl_Type()
)
nbsCmmcPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortFlowControl.setStatus("current")


class _NbsCmmcPortAutoNegAd_Type(OctetString):
    """Custom type nbsCmmcPortAutoNegAd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsCmmcPortAutoNegAd_Type.__name__ = "OctetString"
_NbsCmmcPortAutoNegAd_Object = MibTableColumn
nbsCmmcPortAutoNegAd = _NbsCmmcPortAutoNegAd_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 50),
    _NbsCmmcPortAutoNegAd_Type()
)
nbsCmmcPortAutoNegAd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAutoNegAd.setStatus("current")


class _NbsCmmcPortAutoNegEditable_Type(OctetString):
    """Custom type nbsCmmcPortAutoNegEditable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_NbsCmmcPortAutoNegEditable_Type.__name__ = "OctetString"
_NbsCmmcPortAutoNegEditable_Object = MibTableColumn
nbsCmmcPortAutoNegEditable = _NbsCmmcPortAutoNegEditable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 51),
    _NbsCmmcPortAutoNegEditable_Type()
)
nbsCmmcPortAutoNegEditable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAutoNegEditable.setStatus("current")


class _NbsCmmcPortWavelengthX_Type(DisplayString):
    """Custom type nbsCmmcPortWavelengthX based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 150),
    )


_NbsCmmcPortWavelengthX_Type.__name__ = "DisplayString"
_NbsCmmcPortWavelengthX_Object = MibTableColumn
nbsCmmcPortWavelengthX = _NbsCmmcPortWavelengthX_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 52),
    _NbsCmmcPortWavelengthX_Type()
)
nbsCmmcPortWavelengthX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortWavelengthX.setStatus("current")


class _NbsCmmcPortZoneIdOper_Type(Integer32):
    """Custom type nbsCmmcPortZoneIdOper based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneIdOper_Object = MibTableColumn
nbsCmmcPortZoneIdOper = _NbsCmmcPortZoneIdOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 53),
    _NbsCmmcPortZoneIdOper_Type()
)
nbsCmmcPortZoneIdOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneIdOper.setStatus("current")


class _NbsCmmcPortZoneSlotOper_Type(Integer32):
    """Custom type nbsCmmcPortZoneSlotOper based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneSlotOper_Object = MibTableColumn
nbsCmmcPortZoneSlotOper = _NbsCmmcPortZoneSlotOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 54),
    _NbsCmmcPortZoneSlotOper_Type()
)
nbsCmmcPortZoneSlotOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneSlotOper.setStatus("current")


class _NbsCmmcPortZoneChassisOper_Type(Integer32):
    """Custom type nbsCmmcPortZoneChassisOper based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneChassisOper_Object = MibTableColumn
nbsCmmcPortZoneChassisOper = _NbsCmmcPortZoneChassisOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 55),
    _NbsCmmcPortZoneChassisOper_Type()
)
nbsCmmcPortZoneChassisOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneChassisOper.setStatus("current")


class _NbsCmmcPortLinkMatch_Type(Integer32):
    """Custom type nbsCmmcPortLinkMatch based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortLinkMatch_Type.__name__ = "Integer32"
_NbsCmmcPortLinkMatch_Object = MibTableColumn
nbsCmmcPortLinkMatch = _NbsCmmcPortLinkMatch_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 56),
    _NbsCmmcPortLinkMatch_Type()
)
nbsCmmcPortLinkMatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortLinkMatch.setStatus("current")


class _NbsCmmcPortMDIPinoutAdmin_Type(Integer32):
    """Custom type nbsCmmcPortMDIPinoutAdmin based on Integer32"""
    defaultValue = 4

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
        *(("autoSense", 4),
          ("mdi", 2),
          ("mdix", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortMDIPinoutAdmin_Type.__name__ = "Integer32"
_NbsCmmcPortMDIPinoutAdmin_Object = MibTableColumn
nbsCmmcPortMDIPinoutAdmin = _NbsCmmcPortMDIPinoutAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 57),
    _NbsCmmcPortMDIPinoutAdmin_Type()
)
nbsCmmcPortMDIPinoutAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortMDIPinoutAdmin.setStatus("current")


class _NbsCmmcPortMDIPinoutOper_Type(Integer32):
    """Custom type nbsCmmcPortMDIPinoutOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 2),
          ("mdix", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortMDIPinoutOper_Type.__name__ = "Integer32"
_NbsCmmcPortMDIPinoutOper_Object = MibTableColumn
nbsCmmcPortMDIPinoutOper = _NbsCmmcPortMDIPinoutOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 58),
    _NbsCmmcPortMDIPinoutOper_Type()
)
nbsCmmcPortMDIPinoutOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortMDIPinoutOper.setStatus("current")


class _NbsCmmcPortFCRecvAdmin_Type(Integer32):
    """Custom type nbsCmmcPortFCRecvAdmin based on Integer32"""
    defaultValue = 3

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
        *(("comply", 3),
          ("drop", 2),
          ("notSupported", 1),
          ("passThru", 4))
    )


_NbsCmmcPortFCRecvAdmin_Type.__name__ = "Integer32"
_NbsCmmcPortFCRecvAdmin_Object = MibTableColumn
nbsCmmcPortFCRecvAdmin = _NbsCmmcPortFCRecvAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 59),
    _NbsCmmcPortFCRecvAdmin_Type()
)
nbsCmmcPortFCRecvAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortFCRecvAdmin.setStatus("current")


class _NbsCmmcPortFCRecvOper_Type(Integer32):
    """Custom type nbsCmmcPortFCRecvOper based on Integer32"""
    defaultValue = 3

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
        *(("comply", 3),
          ("drop", 2),
          ("notSupported", 1),
          ("passThru", 4))
    )


_NbsCmmcPortFCRecvOper_Type.__name__ = "Integer32"
_NbsCmmcPortFCRecvOper_Object = MibTableColumn
nbsCmmcPortFCRecvOper = _NbsCmmcPortFCRecvOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 60),
    _NbsCmmcPortFCRecvOper_Type()
)
nbsCmmcPortFCRecvOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortFCRecvOper.setStatus("current")


class _NbsCmmcPortFCSendAdmin_Type(Integer32):
    """Custom type nbsCmmcPortFCSendAdmin based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortFCSendAdmin_Type.__name__ = "Integer32"
_NbsCmmcPortFCSendAdmin_Object = MibTableColumn
nbsCmmcPortFCSendAdmin = _NbsCmmcPortFCSendAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 61),
    _NbsCmmcPortFCSendAdmin_Type()
)
nbsCmmcPortFCSendAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortFCSendAdmin.setStatus("current")


class _NbsCmmcPortFCSendOper_Type(Integer32):
    """Custom type nbsCmmcPortFCSendOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortFCSendOper_Type.__name__ = "Integer32"
_NbsCmmcPortFCSendOper_Object = MibTableColumn
nbsCmmcPortFCSendOper = _NbsCmmcPortFCSendOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 62),
    _NbsCmmcPortFCSendOper_Type()
)
nbsCmmcPortFCSendOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortFCSendOper.setStatus("current")


class _NbsCmmcPortAutoNegWait_Type(Integer32):
    """Custom type nbsCmmcPortAutoNegWait based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 254),
    )


_NbsCmmcPortAutoNegWait_Type.__name__ = "Integer32"
_NbsCmmcPortAutoNegWait_Object = MibTableColumn
nbsCmmcPortAutoNegWait = _NbsCmmcPortAutoNegWait_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 63),
    _NbsCmmcPortAutoNegWait_Type()
)
nbsCmmcPortAutoNegWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAutoNegWait.setStatus("current")


class _NbsCmmcPortTemperatureLevel_Type(Integer32):
    """Custom type nbsCmmcPortTemperatureLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsCmmcPortTemperatureLevel_Type.__name__ = "Integer32"
_NbsCmmcPortTemperatureLevel_Object = MibTableColumn
nbsCmmcPortTemperatureLevel = _NbsCmmcPortTemperatureLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 64),
    _NbsCmmcPortTemperatureLevel_Type()
)
nbsCmmcPortTemperatureLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortTemperatureLevel.setStatus("current")


class _NbsCmmcPortTxPowerLevel_Type(Integer32):
    """Custom type nbsCmmcPortTxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsCmmcPortTxPowerLevel_Type.__name__ = "Integer32"
_NbsCmmcPortTxPowerLevel_Object = MibTableColumn
nbsCmmcPortTxPowerLevel = _NbsCmmcPortTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 65),
    _NbsCmmcPortTxPowerLevel_Type()
)
nbsCmmcPortTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortTxPowerLevel.setStatus("current")


class _NbsCmmcPortRxPowerLevel_Type(Integer32):
    """Custom type nbsCmmcPortRxPowerLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsCmmcPortRxPowerLevel_Type.__name__ = "Integer32"
_NbsCmmcPortRxPowerLevel_Object = MibTableColumn
nbsCmmcPortRxPowerLevel = _NbsCmmcPortRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 66),
    _NbsCmmcPortRxPowerLevel_Type()
)
nbsCmmcPortRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortRxPowerLevel.setStatus("current")


class _NbsCmmcPortBiasAmpsLevel_Type(Integer32):
    """Custom type nbsCmmcPortBiasAmpsLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsCmmcPortBiasAmpsLevel_Type.__name__ = "Integer32"
_NbsCmmcPortBiasAmpsLevel_Object = MibTableColumn
nbsCmmcPortBiasAmpsLevel = _NbsCmmcPortBiasAmpsLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 67),
    _NbsCmmcPortBiasAmpsLevel_Type()
)
nbsCmmcPortBiasAmpsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortBiasAmpsLevel.setStatus("current")


class _NbsCmmcPortSupplyVoltsLevel_Type(Integer32):
    """Custom type nbsCmmcPortSupplyVoltsLevel based on Integer32"""
    defaultValue = 4

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
        *(("highAlarm", 6),
          ("highWarning", 5),
          ("lowAlarm", 2),
          ("lowWarning", 3),
          ("notSupported", 1),
          ("ok", 4))
    )


_NbsCmmcPortSupplyVoltsLevel_Type.__name__ = "Integer32"
_NbsCmmcPortSupplyVoltsLevel_Object = MibTableColumn
nbsCmmcPortSupplyVoltsLevel = _NbsCmmcPortSupplyVoltsLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 68),
    _NbsCmmcPortSupplyVoltsLevel_Type()
)
nbsCmmcPortSupplyVoltsLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortSupplyVoltsLevel.setStatus("current")


class _NbsCmmcPortAmpGainOper_Type(Integer32):
    """Custom type nbsCmmcPortAmpGainOper based on Integer32"""
    defaultValue = -1


_NbsCmmcPortAmpGainOper_Object = MibTableColumn
nbsCmmcPortAmpGainOper = _NbsCmmcPortAmpGainOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 69),
    _NbsCmmcPortAmpGainOper_Type()
)
nbsCmmcPortAmpGainOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpGainOper.setStatus("current")


class _NbsCmmcPortAmpGainAdmin_Type(Integer32):
    """Custom type nbsCmmcPortAmpGainAdmin based on Integer32"""
    defaultValue = -1


_NbsCmmcPortAmpGainAdmin_Object = MibTableColumn
nbsCmmcPortAmpGainAdmin = _NbsCmmcPortAmpGainAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 70),
    _NbsCmmcPortAmpGainAdmin_Type()
)
nbsCmmcPortAmpGainAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpGainAdmin.setStatus("current")


class _NbsCmmcPortAmpOutputPwrAdmin_Type(Integer32):
    """Custom type nbsCmmcPortAmpOutputPwrAdmin based on Integer32"""
    defaultValue = -2147483648

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_NbsCmmcPortAmpOutputPwrAdmin_Type.__name__ = "Integer32"
_NbsCmmcPortAmpOutputPwrAdmin_Object = MibTableColumn
nbsCmmcPortAmpOutputPwrAdmin = _NbsCmmcPortAmpOutputPwrAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 71),
    _NbsCmmcPortAmpOutputPwrAdmin_Type()
)
nbsCmmcPortAmpOutputPwrAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpOutputPwrAdmin.setStatus("current")


class _NbsCmmcPortProtoCapabilities_Type(OctetString):
    """Custom type nbsCmmcPortProtoCapabilities based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_NbsCmmcPortProtoCapabilities_Type.__name__ = "OctetString"
_NbsCmmcPortProtoCapabilities_Object = MibTableColumn
nbsCmmcPortProtoCapabilities = _NbsCmmcPortProtoCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 72),
    _NbsCmmcPortProtoCapabilities_Type()
)
nbsCmmcPortProtoCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortProtoCapabilities.setStatus("current")


class _NbsCmmcPortProtoAdmin_Type(Integer32):
    """Custom type nbsCmmcPortProtoAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcPortProtoAdmin_Object = MibTableColumn
nbsCmmcPortProtoAdmin = _NbsCmmcPortProtoAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 73),
    _NbsCmmcPortProtoAdmin_Type()
)
nbsCmmcPortProtoAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortProtoAdmin.setStatus("current")


class _NbsCmmcPortProtoOper_Type(Integer32):
    """Custom type nbsCmmcPortProtoOper based on Integer32"""
    defaultValue = 0


_NbsCmmcPortProtoOper_Object = MibTableColumn
nbsCmmcPortProtoOper = _NbsCmmcPortProtoOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 74),
    _NbsCmmcPortProtoOper_Type()
)
nbsCmmcPortProtoOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortProtoOper.setStatus("current")


class _NbsCmmcPortPreambleLen_Type(Integer32):
    """Custom type nbsCmmcPortPreambleLen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("standard", 2),
          ("variable", 3))
    )


_NbsCmmcPortPreambleLen_Type.__name__ = "Integer32"
_NbsCmmcPortPreambleLen_Object = MibTableColumn
nbsCmmcPortPreambleLen = _NbsCmmcPortPreambleLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 75),
    _NbsCmmcPortPreambleLen_Type()
)
nbsCmmcPortPreambleLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortPreambleLen.setStatus("current")


class _NbsCmmcPortPreferred_Type(Integer32):
    """Custom type nbsCmmcPortPreferred based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("notSupported", 1),
          ("yes", 3))
    )


_NbsCmmcPortPreferred_Type.__name__ = "Integer32"
_NbsCmmcPortPreferred_Object = MibTableColumn
nbsCmmcPortPreferred = _NbsCmmcPortPreferred_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 76),
    _NbsCmmcPortPreferred_Type()
)
nbsCmmcPortPreferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortPreferred.setStatus("current")


class _NbsCmmcPortCableLen_Type(Integer32):
    """Custom type nbsCmmcPortCableLen based on Integer32"""
    defaultValue = 1

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
        *(("len133", 2),
          ("len266", 3),
          ("len399", 4),
          ("len533", 5),
          ("len655", 6),
          ("longHaul", 8),
          ("notSupported", 1),
          ("shortHaul", 7))
    )


_NbsCmmcPortCableLen_Type.__name__ = "Integer32"
_NbsCmmcPortCableLen_Object = MibTableColumn
nbsCmmcPortCableLen = _NbsCmmcPortCableLen_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 77),
    _NbsCmmcPortCableLen_Type()
)
nbsCmmcPortCableLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortCableLen.setStatus("current")


class _NbsCmmcPortRedundantTxMode_Type(Integer32):
    """Custom type nbsCmmcPortRedundantTxMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("oneColonOne", 2),
          ("onePlusOne", 3))
    )


_NbsCmmcPortRedundantTxMode_Type.__name__ = "Integer32"
_NbsCmmcPortRedundantTxMode_Object = MibTableColumn
nbsCmmcPortRedundantTxMode = _NbsCmmcPortRedundantTxMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 78),
    _NbsCmmcPortRedundantTxMode_Type()
)
nbsCmmcPortRedundantTxMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortRedundantTxMode.setStatus("current")


class _NbsCmmcPortTermination_Type(Integer32):
    """Custom type nbsCmmcPortTermination based on Integer32"""
    defaultValue = 2

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
        *(("disable", 2),
          ("notSupported", 1),
          ("ohm100", 4),
          ("ohm120", 3),
          ("ohm75", 5))
    )


_NbsCmmcPortTermination_Type.__name__ = "Integer32"
_NbsCmmcPortTermination_Object = MibTableColumn
nbsCmmcPortTermination = _NbsCmmcPortTermination_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 79),
    _NbsCmmcPortTermination_Type()
)
nbsCmmcPortTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortTermination.setStatus("current")


class _NbsCmmcPortDescription_Type(DisplayString):
    """Custom type nbsCmmcPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 240),
    )


_NbsCmmcPortDescription_Type.__name__ = "DisplayString"
_NbsCmmcPortDescription_Object = MibTableColumn
nbsCmmcPortDescription = _NbsCmmcPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 80),
    _NbsCmmcPortDescription_Type()
)
nbsCmmcPortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortDescription.setStatus("current")


class _NbsCmmcPortTransmitUnmapped_Type(Integer32):
    """Custom type nbsCmmcPortTransmitUnmapped based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortTransmitUnmapped_Type.__name__ = "Integer32"
_NbsCmmcPortTransmitUnmapped_Object = MibTableColumn
nbsCmmcPortTransmitUnmapped = _NbsCmmcPortTransmitUnmapped_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 81),
    _NbsCmmcPortTransmitUnmapped_Type()
)
nbsCmmcPortTransmitUnmapped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortTransmitUnmapped.setStatus("current")


class _NbsCmmcPortToggleMode_Type(Integer32):
    """Custom type nbsCmmcPortToggleMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortToggleMode_Type.__name__ = "Integer32"
_NbsCmmcPortToggleMode_Object = MibTableColumn
nbsCmmcPortToggleMode = _NbsCmmcPortToggleMode_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 82),
    _NbsCmmcPortToggleMode_Type()
)
nbsCmmcPortToggleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortToggleMode.setStatus("current")


class _NbsCmmcPortCrossConnect_Type(Integer32):
    """Custom type nbsCmmcPortCrossConnect based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcPortCrossConnect_Type.__name__ = "Integer32"
_NbsCmmcPortCrossConnect_Object = MibTableColumn
nbsCmmcPortCrossConnect = _NbsCmmcPortCrossConnect_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 83),
    _NbsCmmcPortCrossConnect_Type()
)
nbsCmmcPortCrossConnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortCrossConnect.setStatus("current")


class _NbsCmmcPortZoneIfIndexAdmin_Type(Integer32):
    """Custom type nbsCmmcPortZoneIfIndexAdmin based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneIfIndexAdmin_Object = MibTableColumn
nbsCmmcPortZoneIfIndexAdmin = _NbsCmmcPortZoneIfIndexAdmin_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 84),
    _NbsCmmcPortZoneIfIndexAdmin_Type()
)
nbsCmmcPortZoneIfIndexAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneIfIndexAdmin.setStatus("current")


class _NbsCmmcPortZoneIfIndexOper_Type(Integer32):
    """Custom type nbsCmmcPortZoneIfIndexOper based on Integer32"""
    defaultValue = 0


_NbsCmmcPortZoneIfIndexOper_Object = MibTableColumn
nbsCmmcPortZoneIfIndexOper = _NbsCmmcPortZoneIfIndexOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 85),
    _NbsCmmcPortZoneIfIndexOper_Type()
)
nbsCmmcPortZoneIfIndexOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortZoneIfIndexOper.setStatus("current")


class _NbsCmmcPortEnableOper_Type(Integer32):
    """Custom type nbsCmmcPortEnableOper based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("notSupported", 1))
    )


_NbsCmmcPortEnableOper_Type.__name__ = "Integer32"
_NbsCmmcPortEnableOper_Object = MibTableColumn
nbsCmmcPortEnableOper = _NbsCmmcPortEnableOper_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 86),
    _NbsCmmcPortEnableOper_Type()
)
nbsCmmcPortEnableOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortEnableOper.setStatus("current")


class _NbsCmmcPortMappingType_Type(Integer32):
    """Custom type nbsCmmcPortMappingType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("destination", 5),
          ("interChasLink", 7),
          ("notSupported", 1),
          ("open", 3),
          ("source", 4),
          ("sourceHelper", 6),
          ("unavailable", 2))
    )


_NbsCmmcPortMappingType_Type.__name__ = "Integer32"
_NbsCmmcPortMappingType_Object = MibTableColumn
nbsCmmcPortMappingType = _NbsCmmcPortMappingType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 87),
    _NbsCmmcPortMappingType_Type()
)
nbsCmmcPortMappingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortMappingType.setStatus("current")


class _NbsCmmcPortCountersState_Type(Integer32):
    """Custom type nbsCmmcPortCountersState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("counting", 2),
          ("notSupported", 1))
    )


_NbsCmmcPortCountersState_Type.__name__ = "Integer32"
_NbsCmmcPortCountersState_Object = MibTableColumn
nbsCmmcPortCountersState = _NbsCmmcPortCountersState_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 88),
    _NbsCmmcPortCountersState_Type()
)
nbsCmmcPortCountersState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortCountersState.setStatus("current")


class _NbsCmmcPortAmpGainMinimum_Type(Integer32):
    """Custom type nbsCmmcPortAmpGainMinimum based on Integer32"""
    defaultValue = 0


_NbsCmmcPortAmpGainMinimum_Object = MibTableColumn
nbsCmmcPortAmpGainMinimum = _NbsCmmcPortAmpGainMinimum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 89),
    _NbsCmmcPortAmpGainMinimum_Type()
)
nbsCmmcPortAmpGainMinimum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpGainMinimum.setStatus("current")


class _NbsCmmcPortAmpGainMaximum_Type(Integer32):
    """Custom type nbsCmmcPortAmpGainMaximum based on Integer32"""
    defaultValue = 0


_NbsCmmcPortAmpGainMaximum_Object = MibTableColumn
nbsCmmcPortAmpGainMaximum = _NbsCmmcPortAmpGainMaximum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 90),
    _NbsCmmcPortAmpGainMaximum_Type()
)
nbsCmmcPortAmpGainMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpGainMaximum.setStatus("current")


class _NbsCmmcPortAmpGainStepSize_Type(Integer32):
    """Custom type nbsCmmcPortAmpGainStepSize based on Integer32"""
    defaultValue = 100


_NbsCmmcPortAmpGainStepSize_Object = MibTableColumn
nbsCmmcPortAmpGainStepSize = _NbsCmmcPortAmpGainStepSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 91),
    _NbsCmmcPortAmpGainStepSize_Type()
)
nbsCmmcPortAmpGainStepSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcPortAmpGainStepSize.setStatus("current")


class _NbsCmmcPortSniffer_Type(Integer32):
    """Custom type nbsCmmcPortSniffer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("off", 2),
          ("on", 3))
    )


_NbsCmmcPortSniffer_Type.__name__ = "Integer32"
_NbsCmmcPortSniffer_Object = MibTableColumn
nbsCmmcPortSniffer = _NbsCmmcPortSniffer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 8, 1, 1, 92),
    _NbsCmmcPortSniffer_Type()
)
nbsCmmcPortSniffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcPortSniffer.setStatus("current")
_NbsCmmcNtpGrp_ObjectIdentity = ObjectIdentity
nbsCmmcNtpGrp = _NbsCmmcNtpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 9)
)
if mibBuilder.loadTexts:
    nbsCmmcNtpGrp.setStatus("current")
_NbsCmmcSmtpGrp_ObjectIdentity = ObjectIdentity
nbsCmmcSmtpGrp = _NbsCmmcSmtpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 10)
)
if mibBuilder.loadTexts:
    nbsCmmcSmtpGrp.setStatus("current")


class _NbsCmmcSmtpDomainName_Type(DisplayString):
    """Custom type nbsCmmcSmtpDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcSmtpDomainName_Type.__name__ = "DisplayString"
_NbsCmmcSmtpDomainName_Object = MibScalar
nbsCmmcSmtpDomainName = _NbsCmmcSmtpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 1),
    _NbsCmmcSmtpDomainName_Type()
)
nbsCmmcSmtpDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSmtpDomainName.setStatus("current")
_NbsCmmcSmtpServerAddress_Type = IpAddress
_NbsCmmcSmtpServerAddress_Object = MibScalar
nbsCmmcSmtpServerAddress = _NbsCmmcSmtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 2),
    _NbsCmmcSmtpServerAddress_Type()
)
nbsCmmcSmtpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSmtpServerAddress.setStatus("current")


class _NbsCmmcSmtpRcvrLevel_Type(Integer32):
    """Custom type nbsCmmcSmtpRcvrLevel based on Integer32"""
    defaultValue = 0


_NbsCmmcSmtpRcvrLevel_Object = MibScalar
nbsCmmcSmtpRcvrLevel = _NbsCmmcSmtpRcvrLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 3),
    _NbsCmmcSmtpRcvrLevel_Type()
)
nbsCmmcSmtpRcvrLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrLevel.setStatus("current")
_NbsCmmcSmtpRcvrNum_Type = Integer32
_NbsCmmcSmtpRcvrNum_Object = MibScalar
nbsCmmcSmtpRcvrNum = _NbsCmmcSmtpRcvrNum_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 4),
    _NbsCmmcSmtpRcvrNum_Type()
)
nbsCmmcSmtpRcvrNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrNum.setStatus("current")
_NbsCmmcSmtpRcvrTable_Object = MibTable
nbsCmmcSmtpRcvrTable = _NbsCmmcSmtpRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 5)
)
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrTable.setStatus("current")
_NbsCmmcSmtpRcvrEntry_Object = MibTableRow
nbsCmmcSmtpRcvrEntry = _NbsCmmcSmtpRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 5, 1)
)
nbsCmmcSmtpRcvrEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSmtpRcvrIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrEntry.setStatus("current")
_NbsCmmcSmtpRcvrIndex_Type = Integer32
_NbsCmmcSmtpRcvrIndex_Object = MibTableColumn
nbsCmmcSmtpRcvrIndex = _NbsCmmcSmtpRcvrIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 5, 1, 1),
    _NbsCmmcSmtpRcvrIndex_Type()
)
nbsCmmcSmtpRcvrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrIndex.setStatus("current")


class _NbsCmmcSmtpRcvrEmailAddress_Type(DisplayString):
    """Custom type nbsCmmcSmtpRcvrEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcSmtpRcvrEmailAddress_Type.__name__ = "DisplayString"
_NbsCmmcSmtpRcvrEmailAddress_Object = MibTableColumn
nbsCmmcSmtpRcvrEmailAddress = _NbsCmmcSmtpRcvrEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 5, 1, 2),
    _NbsCmmcSmtpRcvrEmailAddress_Type()
)
nbsCmmcSmtpRcvrEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrEmailAddress.setStatus("current")


class _NbsCmmcSmtpRcvrStatus_Type(Integer32):
    """Custom type nbsCmmcSmtpRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2))
    )


_NbsCmmcSmtpRcvrStatus_Type.__name__ = "Integer32"
_NbsCmmcSmtpRcvrStatus_Object = MibTableColumn
nbsCmmcSmtpRcvrStatus = _NbsCmmcSmtpRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 10, 5, 1, 3),
    _NbsCmmcSmtpRcvrStatus_Type()
)
nbsCmmcSmtpRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSmtpRcvrStatus.setStatus("current")
_NbsCmmcSysLogGrp_ObjectIdentity = ObjectIdentity
nbsCmmcSysLogGrp = _NbsCmmcSysLogGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 11)
)
if mibBuilder.loadTexts:
    nbsCmmcSysLogGrp.setStatus("current")


class _NbsCmmcSysLogRunningLevel_Type(Integer32):
    """Custom type nbsCmmcSysLogRunningLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 7),
          ("disabled", 1),
          ("error", 3),
          ("fatal", 2),
          ("info", 5),
          ("memo", 6),
          ("warning", 4))
    )


_NbsCmmcSysLogRunningLevel_Type.__name__ = "Integer32"
_NbsCmmcSysLogRunningLevel_Object = MibScalar
nbsCmmcSysLogRunningLevel = _NbsCmmcSysLogRunningLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 1),
    _NbsCmmcSysLogRunningLevel_Type()
)
nbsCmmcSysLogRunningLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogRunningLevel.setStatus("current")


class _NbsCmmcSysLogNvLevel_Type(Integer32):
    """Custom type nbsCmmcSysLogNvLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 7),
          ("disabled", 1),
          ("error", 3),
          ("fatal", 2),
          ("info", 5),
          ("memo", 6),
          ("warning", 4))
    )


_NbsCmmcSysLogNvLevel_Type.__name__ = "Integer32"
_NbsCmmcSysLogNvLevel_Object = MibScalar
nbsCmmcSysLogNvLevel = _NbsCmmcSysLogNvLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 2),
    _NbsCmmcSysLogNvLevel_Type()
)
nbsCmmcSysLogNvLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogNvLevel.setStatus("current")


class _NbsCmmcSysLogTrapLevel_Type(Integer32):
    """Custom type nbsCmmcSysLogTrapLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 7),
          ("deprecated5", 5),
          ("deprecated6", 6),
          ("disabled", 1),
          ("error", 3),
          ("fatal", 2),
          ("warning", 4))
    )


_NbsCmmcSysLogTrapLevel_Type.__name__ = "Integer32"
_NbsCmmcSysLogTrapLevel_Object = MibScalar
nbsCmmcSysLogTrapLevel = _NbsCmmcSysLogTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 3),
    _NbsCmmcSysLogTrapLevel_Type()
)
nbsCmmcSysLogTrapLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogTrapLevel.setStatus("current")


class _NbsCmmcSysLogEmailLevel_Type(Integer32):
    """Custom type nbsCmmcSysLogEmailLevel based on Integer32"""
    defaultValue = 1

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
        *(("alarm", 7),
          ("deprecated5", 5),
          ("deprecated6", 6),
          ("disabled", 1),
          ("error", 3),
          ("fatal", 2),
          ("notSupported", 8),
          ("warning", 4))
    )


_NbsCmmcSysLogEmailLevel_Type.__name__ = "Integer32"
_NbsCmmcSysLogEmailLevel_Object = MibScalar
nbsCmmcSysLogEmailLevel = _NbsCmmcSysLogEmailLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 4),
    _NbsCmmcSysLogEmailLevel_Type()
)
nbsCmmcSysLogEmailLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogEmailLevel.setStatus("current")
_NbsCmmcSysLogMessageTable_Object = MibTable
nbsCmmcSysLogMessageTable = _NbsCmmcSysLogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 5)
)
if mibBuilder.loadTexts:
    nbsCmmcSysLogMessageTable.setStatus("current")
_NbsCmmcSysLogMessageEntry_Object = MibTableRow
nbsCmmcSysLogMessageEntry = _NbsCmmcSysLogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 5, 1)
)
nbsCmmcSysLogMessageEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysLogMessageType"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysLogMessageEntry.setStatus("current")


class _NbsCmmcSysLogMessageType_Type(Integer32):
    """Custom type nbsCmmcSysLogMessageType based on Integer32"""
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
        *(("dot1dBridge", 4),
          ("physTraps", 3),
          ("snmp", 2),
          ("sysAuthentic", 5),
          ("sysReset", 1))
    )


_NbsCmmcSysLogMessageType_Type.__name__ = "Integer32"
_NbsCmmcSysLogMessageType_Object = MibTableColumn
nbsCmmcSysLogMessageType = _NbsCmmcSysLogMessageType_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 5, 1, 1),
    _NbsCmmcSysLogMessageType_Type()
)
nbsCmmcSysLogMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLogMessageType.setStatus("current")


class _NbsCmmcSysLogMessageSeverity_Type(Integer32):
    """Custom type nbsCmmcSysLogMessageSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100,
              1000,
              10000)
        )
    )
    namedValues = NamedValues(
        *(("debugging", 10000),
          ("emergencies", 1000),
          ("errors", 100),
          ("informational", 1),
          ("warnings", 10))
    )


_NbsCmmcSysLogMessageSeverity_Type.__name__ = "Integer32"
_NbsCmmcSysLogMessageSeverity_Object = MibTableColumn
nbsCmmcSysLogMessageSeverity = _NbsCmmcSysLogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 5, 1, 2),
    _NbsCmmcSysLogMessageSeverity_Type()
)
nbsCmmcSysLogMessageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysLogMessageSeverity.setStatus("current")
_NbsCmmcSysRunningLogMessageTotal_Type = Integer32
_NbsCmmcSysRunningLogMessageTotal_Object = MibScalar
nbsCmmcSysRunningLogMessageTotal = _NbsCmmcSysRunningLogMessageTotal_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 6),
    _NbsCmmcSysRunningLogMessageTotal_Type()
)
nbsCmmcSysRunningLogMessageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageTotal.setStatus("current")
_NbsCmmcSysRunningLogMessageTable_Object = MibTable
nbsCmmcSysRunningLogMessageTable = _NbsCmmcSysRunningLogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7)
)
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageTable.setStatus("current")
_NbsCmmcSysRunningLogMessageEntry_Object = MibTableRow
nbsCmmcSysRunningLogMessageEntry = _NbsCmmcSysRunningLogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1)
)
nbsCmmcSysRunningLogMessageEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysRunningLogMessageIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageEntry.setStatus("current")
_NbsCmmcSysRunningLogMessageIndex_Type = Integer32
_NbsCmmcSysRunningLogMessageIndex_Object = MibTableColumn
nbsCmmcSysRunningLogMessageIndex = _NbsCmmcSysRunningLogMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 1),
    _NbsCmmcSysRunningLogMessageIndex_Type()
)
nbsCmmcSysRunningLogMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageIndex.setStatus("current")


class _NbsCmmcSysRunningLogMessageSeverity_Type(DisplayString):
    """Custom type nbsCmmcSysRunningLogMessageSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysRunningLogMessageSeverity_Type.__name__ = "DisplayString"
_NbsCmmcSysRunningLogMessageSeverity_Object = MibTableColumn
nbsCmmcSysRunningLogMessageSeverity = _NbsCmmcSysRunningLogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 2),
    _NbsCmmcSysRunningLogMessageSeverity_Type()
)
nbsCmmcSysRunningLogMessageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageSeverity.setStatus("current")
_NbsCmmcSysRunningLogMessageErrorID_Type = Integer32
_NbsCmmcSysRunningLogMessageErrorID_Object = MibTableColumn
nbsCmmcSysRunningLogMessageErrorID = _NbsCmmcSysRunningLogMessageErrorID_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 3),
    _NbsCmmcSysRunningLogMessageErrorID_Type()
)
nbsCmmcSysRunningLogMessageErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageErrorID.setStatus("current")
_NbsCmmcSysRunningLogMessageSession_Type = Integer32
_NbsCmmcSysRunningLogMessageSession_Object = MibTableColumn
nbsCmmcSysRunningLogMessageSession = _NbsCmmcSysRunningLogMessageSession_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 4),
    _NbsCmmcSysRunningLogMessageSession_Type()
)
nbsCmmcSysRunningLogMessageSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageSession.setStatus("current")
_NbsCmmcSysRunningLogMessageTime_Type = Integer32
_NbsCmmcSysRunningLogMessageTime_Object = MibTableColumn
nbsCmmcSysRunningLogMessageTime = _NbsCmmcSysRunningLogMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 5),
    _NbsCmmcSysRunningLogMessageTime_Type()
)
nbsCmmcSysRunningLogMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageTime.setStatus("current")


class _NbsCmmcSysRunningLogMessageModule_Type(DisplayString):
    """Custom type nbsCmmcSysRunningLogMessageModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysRunningLogMessageModule_Type.__name__ = "DisplayString"
_NbsCmmcSysRunningLogMessageModule_Object = MibTableColumn
nbsCmmcSysRunningLogMessageModule = _NbsCmmcSysRunningLogMessageModule_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 6),
    _NbsCmmcSysRunningLogMessageModule_Type()
)
nbsCmmcSysRunningLogMessageModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageModule.setStatus("current")


class _NbsCmmcSysRunningLogMessageString_Type(DisplayString):
    """Custom type nbsCmmcSysRunningLogMessageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysRunningLogMessageString_Type.__name__ = "DisplayString"
_NbsCmmcSysRunningLogMessageString_Object = MibTableColumn
nbsCmmcSysRunningLogMessageString = _NbsCmmcSysRunningLogMessageString_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 7, 1, 7),
    _NbsCmmcSysRunningLogMessageString_Type()
)
nbsCmmcSysRunningLogMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageString.setStatus("current")
_NbsCmmcSysNvramLogMessageTotal_Type = Integer32
_NbsCmmcSysNvramLogMessageTotal_Object = MibScalar
nbsCmmcSysNvramLogMessageTotal = _NbsCmmcSysNvramLogMessageTotal_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 8),
    _NbsCmmcSysNvramLogMessageTotal_Type()
)
nbsCmmcSysNvramLogMessageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageTotal.setStatus("current")
_NbsCmmcSysNvramLogMessageTable_Object = MibTable
nbsCmmcSysNvramLogMessageTable = _NbsCmmcSysNvramLogMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9)
)
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageTable.setStatus("current")
_NbsCmmcSysNvramLogMessageEntry_Object = MibTableRow
nbsCmmcSysNvramLogMessageEntry = _NbsCmmcSysNvramLogMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1)
)
nbsCmmcSysNvramLogMessageEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysNvramLogMessageIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageEntry.setStatus("current")
_NbsCmmcSysNvramLogMessageIndex_Type = Integer32
_NbsCmmcSysNvramLogMessageIndex_Object = MibTableColumn
nbsCmmcSysNvramLogMessageIndex = _NbsCmmcSysNvramLogMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 1),
    _NbsCmmcSysNvramLogMessageIndex_Type()
)
nbsCmmcSysNvramLogMessageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageIndex.setStatus("current")


class _NbsCmmcSysNvramLogMessageSeverity_Type(DisplayString):
    """Custom type nbsCmmcSysNvramLogMessageSeverity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysNvramLogMessageSeverity_Type.__name__ = "DisplayString"
_NbsCmmcSysNvramLogMessageSeverity_Object = MibTableColumn
nbsCmmcSysNvramLogMessageSeverity = _NbsCmmcSysNvramLogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 2),
    _NbsCmmcSysNvramLogMessageSeverity_Type()
)
nbsCmmcSysNvramLogMessageSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageSeverity.setStatus("current")
_NbsCmmcSysNvramLogMessageErrorID_Type = Integer32
_NbsCmmcSysNvramLogMessageErrorID_Object = MibTableColumn
nbsCmmcSysNvramLogMessageErrorID = _NbsCmmcSysNvramLogMessageErrorID_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 3),
    _NbsCmmcSysNvramLogMessageErrorID_Type()
)
nbsCmmcSysNvramLogMessageErrorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageErrorID.setStatus("current")
_NbsCmmcSysNvramLogMessageSession_Type = Integer32
_NbsCmmcSysNvramLogMessageSession_Object = MibTableColumn
nbsCmmcSysNvramLogMessageSession = _NbsCmmcSysNvramLogMessageSession_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 4),
    _NbsCmmcSysNvramLogMessageSession_Type()
)
nbsCmmcSysNvramLogMessageSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageSession.setStatus("current")
_NbsCmmcSysNvramLogMessageTime_Type = Integer32
_NbsCmmcSysNvramLogMessageTime_Object = MibTableColumn
nbsCmmcSysNvramLogMessageTime = _NbsCmmcSysNvramLogMessageTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 5),
    _NbsCmmcSysNvramLogMessageTime_Type()
)
nbsCmmcSysNvramLogMessageTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageTime.setStatus("current")


class _NbsCmmcSysNvramLogMessageModule_Type(DisplayString):
    """Custom type nbsCmmcSysNvramLogMessageModule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysNvramLogMessageModule_Type.__name__ = "DisplayString"
_NbsCmmcSysNvramLogMessageModule_Object = MibTableColumn
nbsCmmcSysNvramLogMessageModule = _NbsCmmcSysNvramLogMessageModule_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 6),
    _NbsCmmcSysNvramLogMessageModule_Type()
)
nbsCmmcSysNvramLogMessageModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageModule.setStatus("current")


class _NbsCmmcSysNvramLogMessageString_Type(DisplayString):
    """Custom type nbsCmmcSysNvramLogMessageString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcSysNvramLogMessageString_Type.__name__ = "DisplayString"
_NbsCmmcSysNvramLogMessageString_Object = MibTableColumn
nbsCmmcSysNvramLogMessageString = _NbsCmmcSysNvramLogMessageString_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 7),
    _NbsCmmcSysNvramLogMessageString_Type()
)
nbsCmmcSysNvramLogMessageString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageString.setStatus("current")
_NbsCmmcSysNvramLogMessagePTime_Type = Integer32
_NbsCmmcSysNvramLogMessagePTime_Object = MibTableColumn
nbsCmmcSysNvramLogMessagePTime = _NbsCmmcSysNvramLogMessagePTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 8),
    _NbsCmmcSysNvramLogMessagePTime_Type()
)
nbsCmmcSysNvramLogMessagePTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessagePTime.setStatus("current")


class _NbsCmmcSysNvramLogMessageDateTime_Type(DisplayString):
    """Custom type nbsCmmcSysNvramLogMessageDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NbsCmmcSysNvramLogMessageDateTime_Type.__name__ = "DisplayString"
_NbsCmmcSysNvramLogMessageDateTime_Object = MibTableColumn
nbsCmmcSysNvramLogMessageDateTime = _NbsCmmcSysNvramLogMessageDateTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 9, 1, 9),
    _NbsCmmcSysNvramLogMessageDateTime_Type()
)
nbsCmmcSysNvramLogMessageDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageDateTime.setStatus("current")
_NbsCmmcSysAuditLogTotal_Type = Integer32
_NbsCmmcSysAuditLogTotal_Object = MibScalar
nbsCmmcSysAuditLogTotal = _NbsCmmcSysAuditLogTotal_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 10),
    _NbsCmmcSysAuditLogTotal_Type()
)
nbsCmmcSysAuditLogTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogTotal.setStatus("current")
_NbsCmmcSysAuditLogTable_Object = MibTable
nbsCmmcSysAuditLogTable = _NbsCmmcSysAuditLogTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11)
)
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogTable.setStatus("current")
_NbsCmmcSysAuditLogEntry_Object = MibTableRow
nbsCmmcSysAuditLogEntry = _NbsCmmcSysAuditLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11, 1)
)
nbsCmmcSysAuditLogEntry.setIndexNames(
    (0, "NBS-CMMC-MIB", "nbsCmmcSysAuditLogIndex"),
)
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogEntry.setStatus("current")
_NbsCmmcSysAuditLogIndex_Type = Integer32
_NbsCmmcSysAuditLogIndex_Object = MibTableColumn
nbsCmmcSysAuditLogIndex = _NbsCmmcSysAuditLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11, 1, 1),
    _NbsCmmcSysAuditLogIndex_Type()
)
nbsCmmcSysAuditLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogIndex.setStatus("current")
_NbsCmmcSysAuditLogUpTime_Type = Integer32
_NbsCmmcSysAuditLogUpTime_Object = MibTableColumn
nbsCmmcSysAuditLogUpTime = _NbsCmmcSysAuditLogUpTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11, 1, 2),
    _NbsCmmcSysAuditLogUpTime_Type()
)
nbsCmmcSysAuditLogUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogUpTime.setStatus("current")


class _NbsCmmcSysAuditLogDateTime_Type(DisplayString):
    """Custom type nbsCmmcSysAuditLogDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_NbsCmmcSysAuditLogDateTime_Type.__name__ = "DisplayString"
_NbsCmmcSysAuditLogDateTime_Object = MibTableColumn
nbsCmmcSysAuditLogDateTime = _NbsCmmcSysAuditLogDateTime_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11, 1, 3),
    _NbsCmmcSysAuditLogDateTime_Type()
)
nbsCmmcSysAuditLogDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogDateTime.setStatus("current")


class _NbsCmmcSysAuditLogString_Type(DisplayString):
    """Custom type nbsCmmcSysAuditLogString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_NbsCmmcSysAuditLogString_Type.__name__ = "DisplayString"
_NbsCmmcSysAuditLogString_Object = MibTableColumn
nbsCmmcSysAuditLogString = _NbsCmmcSysAuditLogString_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 11, 1, 4),
    _NbsCmmcSysAuditLogString_Type()
)
nbsCmmcSysAuditLogString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogString.setStatus("current")
_NbsCmmcSysLogRemoteServer_Type = IpAddress
_NbsCmmcSysLogRemoteServer_Object = MibScalar
nbsCmmcSysLogRemoteServer = _NbsCmmcSysLogRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 12),
    _NbsCmmcSysLogRemoteServer_Type()
)
nbsCmmcSysLogRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogRemoteServer.setStatus("current")


class _NbsCmmcSysLogRemoteLevel_Type(Integer32):
    """Custom type nbsCmmcSysLogRemoteLevel based on Integer32"""
    defaultValue = 7

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("alert", 3),
          ("crit", 4),
          ("debug", 9),
          ("disabled", 1),
          ("emerg", 2),
          ("error", 5),
          ("info", 8),
          ("notice", 7),
          ("warning", 6))
    )


_NbsCmmcSysLogRemoteLevel_Type.__name__ = "Integer32"
_NbsCmmcSysLogRemoteLevel_Object = MibScalar
nbsCmmcSysLogRemoteLevel = _NbsCmmcSysLogRemoteLevel_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 13),
    _NbsCmmcSysLogRemoteLevel_Type()
)
nbsCmmcSysLogRemoteLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogRemoteLevel.setStatus("current")


class _NbsCmmcSysRunningLogMessageClear_Type(Integer32):
    """Custom type nbsCmmcSysRunningLogMessageClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcSysRunningLogMessageClear_Type.__name__ = "Integer32"
_NbsCmmcSysRunningLogMessageClear_Object = MibScalar
nbsCmmcSysRunningLogMessageClear = _NbsCmmcSysRunningLogMessageClear_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 14),
    _NbsCmmcSysRunningLogMessageClear_Type()
)
nbsCmmcSysRunningLogMessageClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysRunningLogMessageClear.setStatus("current")


class _NbsCmmcSysNvramLogMessageClear_Type(Integer32):
    """Custom type nbsCmmcSysNvramLogMessageClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcSysNvramLogMessageClear_Type.__name__ = "Integer32"
_NbsCmmcSysNvramLogMessageClear_Object = MibScalar
nbsCmmcSysNvramLogMessageClear = _NbsCmmcSysNvramLogMessageClear_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 15),
    _NbsCmmcSysNvramLogMessageClear_Type()
)
nbsCmmcSysNvramLogMessageClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysNvramLogMessageClear.setStatus("current")


class _NbsCmmcSysAuditLogClear_Type(Integer32):
    """Custom type nbsCmmcSysAuditLogClear based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearing", 3),
          ("notSupported", 1),
          ("operating", 2))
    )


_NbsCmmcSysAuditLogClear_Type.__name__ = "Integer32"
_NbsCmmcSysAuditLogClear_Object = MibScalar
nbsCmmcSysAuditLogClear = _NbsCmmcSysAuditLogClear_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 16),
    _NbsCmmcSysAuditLogClear_Type()
)
nbsCmmcSysAuditLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysAuditLogClear.setStatus("current")


class _NbsCmmcSysLogNvSize_Type(Integer32):
    """Custom type nbsCmmcSysLogNvSize based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 65535),
    )


_NbsCmmcSysLogNvSize_Type.__name__ = "Integer32"
_NbsCmmcSysLogNvSize_Object = MibScalar
nbsCmmcSysLogNvSize = _NbsCmmcSysLogNvSize_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 11, 17),
    _NbsCmmcSysLogNvSize_Type()
)
nbsCmmcSysLogNvSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbsCmmcSysLogNvSize.setStatus("current")
_NbsCmmcTrapGrp_ObjectIdentity = ObjectIdentity
nbsCmmcTrapGrp = _NbsCmmcTrapGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 12)
)
if mibBuilder.loadTexts:
    nbsCmmcTrapGrp.setStatus("current")


class _NbsCmmcTrapLastMessage_Type(DisplayString):
    """Custom type nbsCmmcTrapLastMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcTrapLastMessage_Type.__name__ = "DisplayString"
_NbsCmmcTrapLastMessage_Object = MibScalar
nbsCmmcTrapLastMessage = _NbsCmmcTrapLastMessage_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 1),
    _NbsCmmcTrapLastMessage_Type()
)
nbsCmmcTrapLastMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapLastMessage.setStatus("current")
_NbsCmmcTrapPowerSupplyId_Type = Integer32
_NbsCmmcTrapPowerSupplyId_Object = MibScalar
nbsCmmcTrapPowerSupplyId = _NbsCmmcTrapPowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 2),
    _NbsCmmcTrapPowerSupplyId_Type()
)
nbsCmmcTrapPowerSupplyId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapPowerSupplyId.setStatus("current")
_NbsCmmcTrapFanId_Type = Integer32
_NbsCmmcTrapFanId_Object = MibScalar
nbsCmmcTrapFanId = _NbsCmmcTrapFanId_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 3),
    _NbsCmmcTrapFanId_Type()
)
nbsCmmcTrapFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapFanId.setStatus("current")
_NbsCmmcTrapPortIndex_Type = Integer32
_NbsCmmcTrapPortIndex_Object = MibScalar
nbsCmmcTrapPortIndex = _NbsCmmcTrapPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 4),
    _NbsCmmcTrapPortIndex_Type()
)
nbsCmmcTrapPortIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapPortIndex.setStatus("current")


class _NbsCmmcTrapPortName_Type(DisplayString):
    """Custom type nbsCmmcTrapPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_NbsCmmcTrapPortName_Type.__name__ = "DisplayString"
_NbsCmmcTrapPortName_Object = MibScalar
nbsCmmcTrapPortName = _NbsCmmcTrapPortName_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 5),
    _NbsCmmcTrapPortName_Type()
)
nbsCmmcTrapPortName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapPortName.setStatus("current")


class _NbsCmmcTrapShutdownReason_Type(DisplayString):
    """Custom type nbsCmmcTrapShutdownReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcTrapShutdownReason_Type.__name__ = "DisplayString"
_NbsCmmcTrapShutdownReason_Object = MibScalar
nbsCmmcTrapShutdownReason = _NbsCmmcTrapShutdownReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 6),
    _NbsCmmcTrapShutdownReason_Type()
)
nbsCmmcTrapShutdownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapShutdownReason.setStatus("current")


class _NbsCmmcTrapErrorInfo_Type(DisplayString):
    """Custom type nbsCmmcTrapErrorInfo based on DisplayString"""
    defaultValue = OctetString("Ethernet.")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NbsCmmcTrapErrorInfo_Type.__name__ = "DisplayString"
_NbsCmmcTrapErrorInfo_Object = MibScalar
nbsCmmcTrapErrorInfo = _NbsCmmcTrapErrorInfo_Object(
    (1, 3, 6, 1, 4, 1, 629, 200, 12, 7),
    _NbsCmmcTrapErrorInfo_Type()
)
nbsCmmcTrapErrorInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nbsCmmcTrapErrorInfo.setStatus("current")
_NbsCmmcTraps_ObjectIdentity = ObjectIdentity
nbsCmmcTraps = _NbsCmmcTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 13)
)
if mibBuilder.loadTexts:
    nbsCmmcTraps.setStatus("current")
_NbsCmmcTraps0_ObjectIdentity = ObjectIdentity
nbsCmmcTraps0 = _NbsCmmcTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0)
)
if mibBuilder.loadTexts:
    nbsCmmcTraps0.setStatus("current")

# Managed Objects groups


# Notification objects

nbsCmmcTrapGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 1)
)
nbsCmmcTrapGenericTrap.setObjects(
    ("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage")
)
if mibBuilder.loadTexts:
    nbsCmmcTrapGenericTrap.setStatus(
        "deprecated"
    )

nbsCmmcTrapSpecificTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 2)
)
nbsCmmcTrapSpecificTrap.setObjects(
    ("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage")
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSpecificTrap.setStatus(
        "deprecated"
    )

nbsCmmcTrapDeviceRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 3)
)
nbsCmmcTrapDeviceRebooted.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapShutdownReason"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapDeviceRebooted.setStatus(
        "current"
    )

nbsCmmcTrapDeviceOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 4)
)
nbsCmmcTrapDeviceOnline.setObjects(
    ("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage")
)
if mibBuilder.loadTexts:
    nbsCmmcTrapDeviceOnline.setStatus(
        "current"
    )

nbsCmmcTrapDeviceShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 5)
)
nbsCmmcTrapDeviceShuttingDown.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapShutdownReason"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapDeviceShuttingDown.setStatus(
        "current"
    )

nbsCmmcTrapPowerSupplyFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 6)
)
nbsCmmcTrapPowerSupplyFailure.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapPowerSupplyId"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPowerSupplyFailure.setStatus(
        "current"
    )

nbsCmmcTrapPowerSupplyRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 7)
)
nbsCmmcTrapPowerSupplyRestored.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapPowerSupplyId"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPowerSupplyRestored.setStatus(
        "current"
    )

nbsCmmcTrapFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 8)
)
nbsCmmcTrapFanFailure.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapFanId"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapFanFailure.setStatus(
        "current"
    )

nbsCmmcTrapFanRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 9)
)
nbsCmmcTrapFanRestored.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapFanId"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapFanRestored.setStatus(
        "current"
    )

nbsCmmcTrapChassisTooHot = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 10)
)
nbsCmmcTrapChassisTooHot.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisTemperatureLimit"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapChassisTooHot.setStatus(
        "current"
    )

nbsCmmcTrapChassisTooCold = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 11)
)
nbsCmmcTrapChassisTooCold.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisTemperatureMin"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapChassisTooCold.setStatus(
        "current"
    )

nbsCmmcTrapChassisTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 12)
)
nbsCmmcTrapChassisTempOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapChassisTempOk.setStatus(
        "current"
    )

nbsCmmcTrapSlotModuleIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 13)
)
nbsCmmcTrapSlotModuleIn.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotType"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotModuleIn.setStatus(
        "current"
    )

nbsCmmcTrapSlotModuleOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 14)
)
nbsCmmcTrapSlotModuleOut.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotType"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotModuleOut.setStatus(
        "current"
    )

nbsCmmcTrapPortEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 15)
)
nbsCmmcTrapPortEnabled.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortEnabled.setStatus(
        "current"
    )

nbsCmmcTrapPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 16)
)
nbsCmmcTrapPortDisabled.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortDisabled.setStatus(
        "current"
    )

nbsCmmcTrapPortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 17)
)
nbsCmmcTrapPortLinkUp.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortLink"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLinkUp.setStatus(
        "current"
    )

nbsCmmcTrapPortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 18)
)
nbsCmmcTrapPortLinkDown.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLinkDown.setStatus(
        "current"
    )

nbsCmmcTrapPortLINOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 19)
)
nbsCmmcTrapPortLINOn.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLINOn.setStatus(
        "current"
    )

nbsCmmcTrapPortLINOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 20)
)
nbsCmmcTrapPortLINOff.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLINOff.setStatus(
        "current"
    )

nbsCmmcTrapPortLoopbackOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 21)
)
nbsCmmcTrapPortLoopbackOn.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLoopbackOn.setStatus(
        "current"
    )

nbsCmmcTrapPortLoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 22)
)
nbsCmmcTrapPortLoopbackOff.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortLoopbackOff.setStatus(
        "current"
    )

nbsCmmcTrapPortMaximumExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 23)
)
nbsCmmcTrapPortMaximumExceeded.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortValue"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortMaximumExceeded.setStatus(
        "current"
    )

nbsCmmcTrapPortRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 24)
)
nbsCmmcTrapPortRemoved.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortRemoved.setStatus(
        "current"
    )

nbsCmmcTrapPortInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 25)
)
nbsCmmcTrapPortInserted.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortConnector"),
        ("NBS-CMMC-MIB", "nbsCmmcPortWavelength"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortInserted.setStatus(
        "current"
    )

nbsCmmcTrapPortTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 26)
)
nbsCmmcTrapPortTempTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTemperatureLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTempTooLow.setStatus(
        "current"
    )

nbsCmmcTrapPortTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 27)
)
nbsCmmcTrapPortTempTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTemperatureLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTempTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapPortRxPowerTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 28)
)
nbsCmmcTrapPortRxPowerTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortRxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortRxPowerLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortRxPowerTooLow.setStatus(
        "current"
    )

nbsCmmcTrapPortRxPowerTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 29)
)
nbsCmmcTrapPortRxPowerTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortRxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortRxPowerLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortRxPowerTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapPortTxPowerTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 30)
)
nbsCmmcTrapPortTxPowerTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTxPowerLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTxPowerTooLow.setStatus(
        "current"
    )

nbsCmmcTrapPortTxPowerTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 31)
)
nbsCmmcTrapPortTxPowerTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTxPowerLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTxPowerTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapPortAmpsTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 32)
)
nbsCmmcTrapPortAmpsTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortBiasAmps"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortBiasAmpsLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortAmpsTooLow.setStatus(
        "current"
    )

nbsCmmcTrapPortAmpsTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 33)
)
nbsCmmcTrapPortAmpsTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortBiasAmps"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortBiasAmpsLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortAmpsTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapPortVoltsTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 34)
)
nbsCmmcTrapPortVoltsTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortSupplyVolts"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortSupplyVoltsLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortVoltsTooLow.setStatus(
        "current"
    )

nbsCmmcTrapPortVoltsTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 35)
)
nbsCmmcTrapPortVoltsTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortSupplyVolts"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortThreshold"),
        ("NBS-CMMC-MIB", "nbsCmmcPortSupplyVoltsLevel"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortVoltsTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 36)
)
nbsCmmcTrapSwitchover.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSwitchover.setStatus(
        "current"
    )

nbsCmmcTrapSlotShuttingDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 37)
)
nbsCmmcTrapSlotShuttingDown.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapShutdownReason"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotShuttingDown.setStatus(
        "current"
    )

nbsCmmcTrapPortCrcError = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 38)
)
nbsCmmcTrapPortCrcError.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortCrcError.setStatus(
        "current"
    )

nbsCmmcTrapCpeInManagedChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 39)
)
nbsCmmcTrapCpeInManagedChassis.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCpeInManagedChassis.setStatus(
        "current"
    )

nbsCmmcTrapCoWithoutCpe = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 40)
)
nbsCmmcTrapCoWithoutCpe.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCoWithoutCpe.setStatus(
        "current"
    )

nbsCmmcTrapCoTakesControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 41)
)
nbsCmmcTrapCoTakesControl.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCoTakesControl.setStatus(
        "current"
    )

nbsCmmcTrapCoYieldsControl = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 42)
)
nbsCmmcTrapCoYieldsControl.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCoYieldsControl.setStatus(
        "current"
    )

nbsCmmcTrapCoLinkedToCo = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 43)
)
nbsCmmcTrapCoLinkedToCo.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCoLinkedToCo.setStatus(
        "current"
    )

nbsCmmcTrapCpeFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 44)
)
nbsCmmcTrapCpeFound.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapCpeFound.setStatus(
        "current"
    )

nbsCmmcTrapPortReflectionDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 45)
)
nbsCmmcTrapPortReflectionDetected.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortReflectionDetected.setStatus(
        "current"
    )

nbsCmmcTrapPortReflectionCeased = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 46)
)
nbsCmmcTrapPortReflectionCeased.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortReflectionCeased.setStatus(
        "current"
    )

nbsCmmcTrapPortTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 47)
)
nbsCmmcTrapPortTempOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTempOk.setStatus(
        "current"
    )

nbsCmmcTrapPortRxPowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 48)
)
nbsCmmcTrapPortRxPowerOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortRxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortRxPowerOk.setStatus(
        "current"
    )

nbsCmmcTrapPortTxPowerOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 49)
)
nbsCmmcTrapPortTxPowerOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortTxPower"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortTxPowerOk.setStatus(
        "current"
    )

nbsCmmcTrapPortAmpsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 50)
)
nbsCmmcTrapPortAmpsOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortBiasAmps"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortAmpsOk.setStatus(
        "current"
    )

nbsCmmcTrapPortVoltsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 51)
)
nbsCmmcTrapPortVoltsOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortSupplyVolts"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortVoltsOk.setStatus(
        "current"
    )

nbsCmmcTrapSlotTempTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 52)
)
nbsCmmcTrapSlotTempTooLow.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotTempTooLow.setStatus(
        "current"
    )

nbsCmmcTrapSlotTempTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 53)
)
nbsCmmcTrapSlotTempTooHigh.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotTempTooHigh.setStatus(
        "current"
    )

nbsCmmcTrapSlotTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 54)
)
nbsCmmcTrapSlotTempOk.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotTemperature"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapSlotTempOk.setStatus(
        "current"
    )

nbsCmmcTrapPortErrorsDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 55)
)
nbsCmmcTrapPortErrorsDetected.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcTrapErrorInfo"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortErrorsDetected.setStatus(
        "current"
    )

nbsCmmcTrapPortErrorsStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 200, 13, 0, 56)
)
nbsCmmcTrapPortErrorsStopped.setObjects(
      *(("NBS-CMMC-MIB", "nbsCmmcTrapLastMessage"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcPortIndex"),
        ("NBS-CMMC-MIB", "nbsCmmcChassisName"),
        ("NBS-CMMC-MIB", "nbsCmmcSlotName"),
        ("NBS-CMMC-MIB", "nbsCmmcPortName"))
)
if mibBuilder.loadTexts:
    nbsCmmcTrapPortErrorsStopped.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NBS-CMMC-MIB",
    **{"InterfaceIndex": InterfaceIndex,
       "nbs": nbs,
       "nbsCmmcMib": nbsCmmcMib,
       "nbsCmmcObjects": nbsCmmcObjects,
       "nbsCmmcSystemGrp": nbsCmmcSystemGrp,
       "nbsCmmcSysFwDescr": nbsCmmcSysFwDescr,
       "nbsCmmcSysFwVers": nbsCmmcSysFwVers,
       "nbsCmmcSysRestart": nbsCmmcSysRestart,
       "nbsCmmcSysNumRestarts": nbsCmmcSysNumRestarts,
       "nbsCmmcSysErrUptime": nbsCmmcSysErrUptime,
       "nbsCmmcSysSetNvramDefaults": nbsCmmcSysSetNvramDefaults,
       "nbsCmmcSysSelftestLevel": nbsCmmcSysSelftestLevel,
       "nbsCmmcSysCurrentTime": nbsCmmcSysCurrentTime,
       "nbsCmmcSysCurrentDateTime": nbsCmmcSysCurrentDateTime,
       "nbsCmmcSysNvramTable": nbsCmmcSysNvramTable,
       "nbsCmmcSysNvramEntry": nbsCmmcSysNvramEntry,
       "nbsCmmcSysNvramIndex": nbsCmmcSysNvramIndex,
       "nbsCmmcSysNvramBlock": nbsCmmcSysNvramBlock,
       "nbsCmmcSysWriteConfig": nbsCmmcSysWriteConfig,
       "nbsCmmcSysUpgrade": nbsCmmcSysUpgrade,
       "nbsCmmcSysLoginIdleTimeout": nbsCmmcSysLoginIdleTimeout,
       "nbsCmmcSysDiscovery": nbsCmmcSysDiscovery,
       "nbsCmmcSysDiscoveryHostTable": nbsCmmcSysDiscoveryHostTable,
       "nbsCmmcSysDiscoveryHostEntry": nbsCmmcSysDiscoveryHostEntry,
       "nbsCmmcSysDiscoveryHostMACAddress": nbsCmmcSysDiscoveryHostMACAddress,
       "nbsCmmcSysDiscoveryHostDistance": nbsCmmcSysDiscoveryHostDistance,
       "nbsCmmcSysDiscoveryHostIPAddress": nbsCmmcSysDiscoveryHostIPAddress,
       "nbsCmmcSysLastSetFailure": nbsCmmcSysLastSetFailure,
       "nbsCmmcSysTimeProtocol": nbsCmmcSysTimeProtocol,
       "nbsCmmcSysTimeServer": nbsCmmcSysTimeServer,
       "nbsCmmcSysFirmwareTable": nbsCmmcSysFirmwareTable,
       "nbsCmmcSysFirmwareEntry": nbsCmmcSysFirmwareEntry,
       "nbsCmmcSysFirmwareIndex": nbsCmmcSysFirmwareIndex,
       "nbsCmmcSysFirmwareDescr": nbsCmmcSysFirmwareDescr,
       "nbsCmmcSysFirmwareFilename": nbsCmmcSysFirmwareFilename,
       "nbsCmmcSysFirmwareSize": nbsCmmcSysFirmwareSize,
       "nbsCmmcSysFirmwareMTime": nbsCmmcSysFirmwareMTime,
       "nbsCmmcSysFirmwareVersion": nbsCmmcSysFirmwareVersion,
       "nbsCmmcSysFirmwareDate": nbsCmmcSysFirmwareDate,
       "nbsCmmcSysFirmwareType": nbsCmmcSysFirmwareType,
       "nbsCmmcSysFirmwareIDCs": nbsCmmcSysFirmwareIDCs,
       "nbsCmmcSysFirmwareCksum": nbsCmmcSysFirmwareCksum,
       "nbsCmmcSysTimeZone": nbsCmmcSysTimeZone,
       "nbsCmmcSysSnmpV1": nbsCmmcSysSnmpV1,
       "nbsCmmcSysSnmpV2c": nbsCmmcSysSnmpV2c,
       "nbsCmmcSysSnmpV3": nbsCmmcSysSnmpV3,
       "nbsCmmcSysLmp": nbsCmmcSysLmp,
       "nbsCmmcSysLockTypes": nbsCmmcSysLockTypes,
       "nbsCmmcSysSerialTerminalType": nbsCmmcSysSerialTerminalType,
       "nbsCmmcSysCrossConnect": nbsCmmcSysCrossConnect,
       "nbsCmmcSysCountersState": nbsCmmcSysCountersState,
       "nbsCmmcSysProtoTableSize": nbsCmmcSysProtoTableSize,
       "nbsCmmcSysProtoTable": nbsCmmcSysProtoTable,
       "nbsCmmcSysProtoEntry": nbsCmmcSysProtoEntry,
       "nbsCmmcSysProtoIndex": nbsCmmcSysProtoIndex,
       "nbsCmmcSysProtoFamily": nbsCmmcSysProtoFamily,
       "nbsCmmcSysProtoRate": nbsCmmcSysProtoRate,
       "nbsCmmcSysTimeZoneTableSize": nbsCmmcSysTimeZoneTableSize,
       "nbsCmmcSysTimeZoneTable": nbsCmmcSysTimeZoneTable,
       "nbsCmmcSysTimeZoneEntry": nbsCmmcSysTimeZoneEntry,
       "nbsCmmcSysTimeZoneIndex": nbsCmmcSysTimeZoneIndex,
       "nbsCmmcSysTimeZoneName": nbsCmmcSysTimeZoneName,
       "nbsCmmcSysLoaderTableSize": nbsCmmcSysLoaderTableSize,
       "nbsCmmcSysLoaderTable": nbsCmmcSysLoaderTable,
       "nbsCmmcSysLoaderEntry": nbsCmmcSysLoaderEntry,
       "nbsCmmcSysLoaderIndex": nbsCmmcSysLoaderIndex,
       "nbsCmmcSysLoaderFileId": nbsCmmcSysLoaderFileId,
       "nbsCmmcSysLoaderProgress": nbsCmmcSysLoaderProgress,
       "nbsCmmcSysLoaderStatus": nbsCmmcSysLoaderStatus,
       "nbsCmmcSysLoaderAbort": nbsCmmcSysLoaderAbort,
       "nbsCmmcSysLoaderAck": nbsCmmcSysLoaderAck,
       "nbsCmmcSysLoaderFilename": nbsCmmcSysLoaderFilename,
       "nbsCmmcSysFirmwareURL": nbsCmmcSysFirmwareURL,
       "nbsCmmcSysFirmwareURLStatus": nbsCmmcSysFirmwareURLStatus,
       "nbsCmmcSysNVAreaTableSize": nbsCmmcSysNVAreaTableSize,
       "nbsCmmcSysNVAreaTable": nbsCmmcSysNVAreaTable,
       "nbsCmmcSysNVAreaEntry": nbsCmmcSysNVAreaEntry,
       "nbsCmmcSysNVAreaIfIndex": nbsCmmcSysNVAreaIfIndex,
       "nbsCmmcSysNVAreaBank": nbsCmmcSysNVAreaBank,
       "nbsCmmcSysNVAreaStatus": nbsCmmcSysNVAreaStatus,
       "nbsCmmcSysNVAreaDescr": nbsCmmcSysNVAreaDescr,
       "nbsCmmcSysNVAreaVersion": nbsCmmcSysNVAreaVersion,
       "nbsCmmcSysNVAreaCksum": nbsCmmcSysNVAreaCksum,
       "nbsCmmcIpSnmpGrp": nbsCmmcIpSnmpGrp,
       "nbsCmmcIpCfg": nbsCmmcIpCfg,
       "nbsCmmcPrvIpAddr": nbsCmmcPrvIpAddr,
       "nbsCmmcPrvNetMask": nbsCmmcPrvNetMask,
       "nbsCmmcPrvBcastAddr": nbsCmmcPrvBcastAddr,
       "nbsCmmcSysIpAddr": nbsCmmcSysIpAddr,
       "nbsCmmcSysNetMask": nbsCmmcSysNetMask,
       "nbsCmmcSysBcastAddr": nbsCmmcSysBcastAddr,
       "nbsCmmcSysObIpAddr": nbsCmmcSysObIpAddr,
       "nbsCmmcSysObNetMask": nbsCmmcSysObNetMask,
       "nbsCmmcSysObBcastAddr": nbsCmmcSysObBcastAddr,
       "nbsCmmcSysDefaultGateway": nbsCmmcSysDefaultGateway,
       "nbsCmmcSysAdminBootpState": nbsCmmcSysAdminBootpState,
       "nbsCmmcSysRunBootpState": nbsCmmcSysRunBootpState,
       "nbsCmmcSysSerialLineMode": nbsCmmcSysSerialLineMode,
       "nbsCmmcSysSerialSlipBaudRate": nbsCmmcSysSerialSlipBaudRate,
       "nbsCmmcSysArpAgingTime": nbsCmmcSysArpAgingTime,
       "nbsCmmcSysMaxTelnetSessions": nbsCmmcSysMaxTelnetSessions,
       "nbsCmmcSysTelnetTable": nbsCmmcSysTelnetTable,
       "nbsCmmcSysTelnetEntry": nbsCmmcSysTelnetEntry,
       "nbsCmmcSysTelnetSessionIndex": nbsCmmcSysTelnetSessionIndex,
       "nbsCmmcSysTelnetSessionStat": nbsCmmcSysTelnetSessionStat,
       "nbsCmmcSysTelnetHost": nbsCmmcSysTelnetHost,
       "nbsCmmcSysTelnetHostPort": nbsCmmcSysTelnetHostPort,
       "nbsCmmcSysTelnetLocal": nbsCmmcSysTelnetLocal,
       "nbsCmmcSysTelnetLocalPort": nbsCmmcSysTelnetLocalPort,
       "nbsCmmcSysTelnetSessionId": nbsCmmcSysTelnetSessionId,
       "nbsCmmcSysTelnetConnectTime": nbsCmmcSysTelnetConnectTime,
       "nbsCmmcSysMaxPingSessions": nbsCmmcSysMaxPingSessions,
       "nbsCmmcSysPingTable": nbsCmmcSysPingTable,
       "nbsCmmcSysPingEntry": nbsCmmcSysPingEntry,
       "nbsCmmcSysPingSessionIndex": nbsCmmcSysPingSessionIndex,
       "nbsCmmcSysPingSessionStat": nbsCmmcSysPingSessionStat,
       "nbsCmmcSysPingAddr": nbsCmmcSysPingAddr,
       "nbsCmmcSysPingNumber": nbsCmmcSysPingNumber,
       "nbsCmmcSysPingOwner": nbsCmmcSysPingOwner,
       "nbsCmmcSysPingRequests": nbsCmmcSysPingRequests,
       "nbsCmmcSysPingResponses": nbsCmmcSysPingResponses,
       "nbsCmmcSysTelnetServer": nbsCmmcSysTelnetServer,
       "nbsCmmcSysSshServer": nbsCmmcSysSshServer,
       "nbsCmmcSysIpAddrOper": nbsCmmcSysIpAddrOper,
       "nbsCmmcSysNetMaskOper": nbsCmmcSysNetMaskOper,
       "nbsCmmcSysBcastAddrOper": nbsCmmcSysBcastAddrOper,
       "nbsCmmcSysDefaultGatewayOper": nbsCmmcSysDefaultGatewayOper,
       "nbsCmmcSysWebServer": nbsCmmcSysWebServer,
       "nbsCmmcSysWebPort": nbsCmmcSysWebPort,
       "nbsCmmcSysTelnetPort": nbsCmmcSysTelnetPort,
       "nbsCmmcSysSshPort": nbsCmmcSysSshPort,
       "nbsCmmcSnmpCfg": nbsCmmcSnmpCfg,
       "nbsCmmcSysWriteCommunity": nbsCmmcSysWriteCommunity,
       "nbsCmmcSysReadCommunity": nbsCmmcSysReadCommunity,
       "nbsCmmcSysTrapTblMaxSize": nbsCmmcSysTrapTblMaxSize,
       "nbsCmmcSysTrapTable": nbsCmmcSysTrapTable,
       "nbsCmmcSysTrapEntry": nbsCmmcSysTrapEntry,
       "nbsCmmcSysTrapTblEntIndex": nbsCmmcSysTrapTblEntIndex,
       "nbsCmmcSysTrapTblEntStatus": nbsCmmcSysTrapTblEntStatus,
       "nbsCmmcSysTrapTblEntIpAddr": nbsCmmcSysTrapTblEntIpAddr,
       "nbsCmmcSysTrapTblEntComm": nbsCmmcSysTrapTblEntComm,
       "nbsCmmcSysTrapTblEntLevel": nbsCmmcSysTrapTblEntLevel,
       "nbsCmmcSysTrapTblEntPort": nbsCmmcSysTrapTblEntPort,
       "nbsCmmcSysEnablePowerSupplyTraps": nbsCmmcSysEnablePowerSupplyTraps,
       "nbsCmmcSysEnableModuleTraps": nbsCmmcSysEnableModuleTraps,
       "nbsCmmcSysEnableBridgeTraps": nbsCmmcSysEnableBridgeTraps,
       "nbsCmmcSysEnableIpAccessTraps": nbsCmmcSysEnableIpAccessTraps,
       "nbsCmmcSysSnmpPortAdmin": nbsCmmcSysSnmpPortAdmin,
       "nbsCmmcSysSnmpPortOper": nbsCmmcSysSnmpPortOper,
       "nbsCmmcTftpGrp": nbsCmmcTftpGrp,
       "nbsCmmcSysTftpHostIP": nbsCmmcSysTftpHostIP,
       "nbsCmmcTftpMaxSessionNum": nbsCmmcTftpMaxSessionNum,
       "nbsCmmcTftpSessTable": nbsCmmcTftpSessTable,
       "nbsCmmcTftpSessEntry": nbsCmmcTftpSessEntry,
       "nbsCmmcTftpSessIndex": nbsCmmcTftpSessIndex,
       "nbsCmmcTftpSessStatus": nbsCmmcTftpSessStatus,
       "nbsCmmcTftpSessHostIp": nbsCmmcTftpSessHostIp,
       "nbsCmmcTftpSessModuleId": nbsCmmcTftpSessModuleId,
       "nbsCmmcTftpSessAction": nbsCmmcTftpSessAction,
       "nbsCmmcTftpSessFileName": nbsCmmcTftpSessFileName,
       "nbsCmmcTftpSessFileSize": nbsCmmcTftpSessFileSize,
       "nbsCmmcTftpSessProgress": nbsCmmcTftpSessProgress,
       "nbsCmmcChassisGrp": nbsCmmcChassisGrp,
       "nbsCmmcChassisTable": nbsCmmcChassisTable,
       "nbsCmmcChassisEntry": nbsCmmcChassisEntry,
       "nbsCmmcChassisIndex": nbsCmmcChassisIndex,
       "nbsCmmcChassisType": nbsCmmcChassisType,
       "nbsCmmcChassisModel": nbsCmmcChassisModel,
       "nbsCmmcChassisObjectId": nbsCmmcChassisObjectId,
       "nbsCmmcChassisNumberOfSlots": nbsCmmcChassisNumberOfSlots,
       "nbsCmmcChassisHardwareRevision": nbsCmmcChassisHardwareRevision,
       "nbsCmmcChassisPS1Status": nbsCmmcChassisPS1Status,
       "nbsCmmcChassisPS2Status": nbsCmmcChassisPS2Status,
       "nbsCmmcChassisPS3Status": nbsCmmcChassisPS3Status,
       "nbsCmmcChassisPS4Status": nbsCmmcChassisPS4Status,
       "nbsCmmcChassisFan1Status": nbsCmmcChassisFan1Status,
       "nbsCmmcChassisFan2Status": nbsCmmcChassisFan2Status,
       "nbsCmmcChassisFan3Status": nbsCmmcChassisFan3Status,
       "nbsCmmcChassisFan4Status": nbsCmmcChassisFan4Status,
       "nbsCmmcChassisTemperature": nbsCmmcChassisTemperature,
       "nbsCmmcChassisTemperatureLimit": nbsCmmcChassisTemperatureLimit,
       "nbsCmmcChassisTemperatureMin": nbsCmmcChassisTemperatureMin,
       "nbsCmmcChassisSignalStrength": nbsCmmcChassisSignalStrength,
       "nbsCmmcChassisSignalStrengthMinimum": nbsCmmcChassisSignalStrengthMinimum,
       "nbsCmmcChassisEnableAutoReset": nbsCmmcChassisEnableAutoReset,
       "nbsCmmcChassisEnableLinkTraps": nbsCmmcChassisEnableLinkTraps,
       "nbsCmmcChassisEnableChassisTraps": nbsCmmcChassisEnableChassisTraps,
       "nbsCmmcChassisEnableLoopbackTraps": nbsCmmcChassisEnableLoopbackTraps,
       "nbsCmmcChassisEnableSlotChangeTraps": nbsCmmcChassisEnableSlotChangeTraps,
       "nbsCmmcChassisEnablePortTraps": nbsCmmcChassisEnablePortTraps,
       "nbsCmmcChassisResetAllModules": nbsCmmcChassisResetAllModules,
       "nbsCmmcChassisEnableModuleSpecificTraps": nbsCmmcChassisEnableModuleSpecificTraps,
       "nbsCmmcChassisLoopbackTimeout": nbsCmmcChassisLoopbackTimeout,
       "nbsCmmcChassisPortInfoBitMap": nbsCmmcChassisPortInfoBitMap,
       "nbsCmmcChassisSlotListBitMap": nbsCmmcChassisSlotListBitMap,
       "nbsCmmcChassisNumberOfPortsBitMap": nbsCmmcChassisNumberOfPortsBitMap,
       "nbsCmmcChassisName": nbsCmmcChassisName,
       "nbsCmmcChassisEnableLINTraps": nbsCmmcChassisEnableLINTraps,
       "nbsCmmcChassisEnablePortChangeTraps": nbsCmmcChassisEnablePortChangeTraps,
       "nbsCmmcChassisEnablePortDiagsTraps": nbsCmmcChassisEnablePortDiagsTraps,
       "nbsCmmcChassisFan5Status": nbsCmmcChassisFan5Status,
       "nbsCmmcChassisFan6Status": nbsCmmcChassisFan6Status,
       "nbsCmmcChassisFan7Status": nbsCmmcChassisFan7Status,
       "nbsCmmcChassisFan8Status": nbsCmmcChassisFan8Status,
       "nbsCmmcChassisEnableSwitchoverTraps": nbsCmmcChassisEnableSwitchoverTraps,
       "nbsCmmcChassisCrossConnect": nbsCmmcChassisCrossConnect,
       "nbsCmmcChassisNVAreaBanks": nbsCmmcChassisNVAreaBanks,
       "nbsCmmcChassisFirmwareCaps": nbsCmmcChassisFirmwareCaps,
       "nbsCmmcChassisFirmwareLoad": nbsCmmcChassisFirmwareLoad,
       "nbsCmmcChassisNVAreaAdmin": nbsCmmcChassisNVAreaAdmin,
       "nbsCmmcChassisNVAreaOper": nbsCmmcChassisNVAreaOper,
       "nbsCmmcChassisLoader": nbsCmmcChassisLoader,
       "nbsCmmcChassisSerialNum": nbsCmmcChassisSerialNum,
       "nbsCmmcChassisFace": nbsCmmcChassisFace,
       "nbsCmmcChassisCountersState": nbsCmmcChassisCountersState,
       "nbsCmmcChassisCount": nbsCmmcChassisCount,
       "nbsCmmcSlotGrp": nbsCmmcSlotGrp,
       "nbsCmmcSlotTable": nbsCmmcSlotTable,
       "nbsCmmcSlotEntry": nbsCmmcSlotEntry,
       "nbsCmmcSlotChassisIndex": nbsCmmcSlotChassisIndex,
       "nbsCmmcSlotIndex": nbsCmmcSlotIndex,
       "nbsCmmcSlotType": nbsCmmcSlotType,
       "nbsCmmcSlotModel": nbsCmmcSlotModel,
       "nbsCmmcSlotObjectId": nbsCmmcSlotObjectId,
       "nbsCmmcSlotNumberOfPorts": nbsCmmcSlotNumberOfPorts,
       "nbsCmmcSlotHardwareRevision": nbsCmmcSlotHardwareRevision,
       "nbsCmmcSlotOperationType": nbsCmmcSlotOperationType,
       "nbsCmmcSlotReset": nbsCmmcSlotReset,
       "nbsCmmcSlotName": nbsCmmcSlotName,
       "nbsCmmcSlotModuleType": nbsCmmcSlotModuleType,
       "nbsCmmcSlotModuleSlot": nbsCmmcSlotModuleSlot,
       "nbsCmmcSlotSwConfigurable": nbsCmmcSlotSwConfigurable,
       "nbsCmmcSlotConfiguration": nbsCmmcSlotConfiguration,
       "nbsCmmcSlotMacAddress": nbsCmmcSlotMacAddress,
       "nbsCmmcSlotIPAddress": nbsCmmcSlotIPAddress,
       "nbsCmmcSlotSubnetMask": nbsCmmcSlotSubnetMask,
       "nbsCmmcSlotBroadcastAddr": nbsCmmcSlotBroadcastAddr,
       "nbsCmmcSlotDefGateway": nbsCmmcSlotDefGateway,
       "nbsCmmcSlotHoming": nbsCmmcSlotHoming,
       "nbsCmmcSlotRedundancy": nbsCmmcSlotRedundancy,
       "nbsCmmcSlotDescr": nbsCmmcSlotDescr,
       "nbsCmmcSlotUpgradable": nbsCmmcSlotUpgradable,
       "nbsCmmcSlotCrossConnect": nbsCmmcSlotCrossConnect,
       "nbsCmmcSlotClearType": nbsCmmcSlotClearType,
       "nbsCmmcSlotNVAreaBanks": nbsCmmcSlotNVAreaBanks,
       "nbsCmmcSlotFirmwareCaps": nbsCmmcSlotFirmwareCaps,
       "nbsCmmcSlotFirmwareLoad": nbsCmmcSlotFirmwareLoad,
       "nbsCmmcSlotNVAreaAdmin": nbsCmmcSlotNVAreaAdmin,
       "nbsCmmcSlotNVAreaOper": nbsCmmcSlotNVAreaOper,
       "nbsCmmcSlotLoader": nbsCmmcSlotLoader,
       "nbsCmmcSlotSerialNum": nbsCmmcSlotSerialNum,
       "nbsCmmcSlotToggleRate": nbsCmmcSlotToggleRate,
       "nbsCmmcSlotTemperature": nbsCmmcSlotTemperature,
       "nbsCmmcSlotCountersState": nbsCmmcSlotCountersState,
       "nbsCmmcSlotRedundancyOper": nbsCmmcSlotRedundancyOper,
       "nbsCmmcLedTable": nbsCmmcLedTable,
       "nbsCmmcLedEntry": nbsCmmcLedEntry,
       "nbsCmmcLedChassisIndex": nbsCmmcLedChassisIndex,
       "nbsCmmcLedSlotIndex": nbsCmmcLedSlotIndex,
       "nbsCmmcLedIndex": nbsCmmcLedIndex,
       "nbsCmmcLedColor": nbsCmmcLedColor,
       "nbsCmmcLedDescription": nbsCmmcLedDescription,
       "nbsCmmcSlotFaceTable": nbsCmmcSlotFaceTable,
       "nbsCmmcSlotFaceEntry": nbsCmmcSlotFaceEntry,
       "nbsCmmcSlotFaceChassisIndex": nbsCmmcSlotFaceChassisIndex,
       "nbsCmmcSlotFaceSlotIndex": nbsCmmcSlotFaceSlotIndex,
       "nbsCmmcSlotFaceRowIndex": nbsCmmcSlotFaceRowIndex,
       "nbsCmmcSlotFaceSummary": nbsCmmcSlotFaceSummary,
       "nbsCmmcPortGrp": nbsCmmcPortGrp,
       "nbsCmmcPortTable": nbsCmmcPortTable,
       "nbsCmmcPortEntry": nbsCmmcPortEntry,
       "nbsCmmcPortChassisIndex": nbsCmmcPortChassisIndex,
       "nbsCmmcPortSlotIndex": nbsCmmcPortSlotIndex,
       "nbsCmmcPortIndex": nbsCmmcPortIndex,
       "nbsCmmcPortType": nbsCmmcPortType,
       "nbsCmmcPortObjectId": nbsCmmcPortObjectId,
       "nbsCmmcPortLink": nbsCmmcPortLink,
       "nbsCmmcPortAutoNegotiation": nbsCmmcPortAutoNegotiation,
       "nbsCmmcPortDuplex": nbsCmmcPortDuplex,
       "nbsCmmcPortSpeed": nbsCmmcPortSpeed,
       "nbsCmmcPortRxActivity": nbsCmmcPortRxActivity,
       "nbsCmmcPortTxActivity": nbsCmmcPortTxActivity,
       "nbsCmmcPortCollisionActivity": nbsCmmcPortCollisionActivity,
       "nbsCmmcPortLoopback": nbsCmmcPortLoopback,
       "nbsCmmcPortEnable": nbsCmmcPortEnable,
       "nbsCmmcPortSelectLink": nbsCmmcPortSelectLink,
       "nbsCmmcPortLIN": nbsCmmcPortLIN,
       "nbsCmmcPortAging": nbsCmmcPortAging,
       "nbsCmmcPortMaxPacketSize": nbsCmmcPortMaxPacketSize,
       "nbsCmmcPortRemoteLoopback": nbsCmmcPortRemoteLoopback,
       "nbsCmmcPortErrorActivity": nbsCmmcPortErrorActivity,
       "nbsCmmcPortName": nbsCmmcPortName,
       "nbsCmmcPortValue": nbsCmmcPortValue,
       "nbsCmmcPortThreshold": nbsCmmcPortThreshold,
       "nbsCmmcPortThresholdAction": nbsCmmcPortThresholdAction,
       "nbsCmmcPortRMChassis": nbsCmmcPortRMChassis,
       "nbsCmmcPortRMSlot": nbsCmmcPortRMSlot,
       "nbsCmmcPortRMPort": nbsCmmcPortRMPort,
       "nbsCmmcPortSerialNumber": nbsCmmcPortSerialNumber,
       "nbsCmmcPortVendorInfo": nbsCmmcPortVendorInfo,
       "nbsCmmcPortTemperature": nbsCmmcPortTemperature,
       "nbsCmmcPortTxPower": nbsCmmcPortTxPower,
       "nbsCmmcPortRxPower": nbsCmmcPortRxPower,
       "nbsCmmcPortBiasAmps": nbsCmmcPortBiasAmps,
       "nbsCmmcPortSupplyVolts": nbsCmmcPortSupplyVolts,
       "nbsCmmcPortMedium": nbsCmmcPortMedium,
       "nbsCmmcPortConnector": nbsCmmcPortConnector,
       "nbsCmmcPortWavelength": nbsCmmcPortWavelength,
       "nbsCmmcPortDigitalDiags": nbsCmmcPortDigitalDiags,
       "nbsCmmcPortZoneIdAdmin": nbsCmmcPortZoneIdAdmin,
       "nbsCmmcPortNominalBitRate": nbsCmmcPortNominalBitRate,
       "nbsCmmcPortModulePort": nbsCmmcPortModulePort,
       "nbsCmmcPortPartRev": nbsCmmcPortPartRev,
       "nbsCmmcPortIfIndex": nbsCmmcPortIfIndex,
       "nbsCmmcPortLinked": nbsCmmcPortLinked,
       "nbsCmmcPortOperational": nbsCmmcPortOperational,
       "nbsCmmcPortZoneChassisAdmin": nbsCmmcPortZoneChassisAdmin,
       "nbsCmmcPortZoneSlotAdmin": nbsCmmcPortZoneSlotAdmin,
       "nbsCmmcPortAlarmCause": nbsCmmcPortAlarmCause,
       "nbsCmmcPortFlowControl": nbsCmmcPortFlowControl,
       "nbsCmmcPortAutoNegAd": nbsCmmcPortAutoNegAd,
       "nbsCmmcPortAutoNegEditable": nbsCmmcPortAutoNegEditable,
       "nbsCmmcPortWavelengthX": nbsCmmcPortWavelengthX,
       "nbsCmmcPortZoneIdOper": nbsCmmcPortZoneIdOper,
       "nbsCmmcPortZoneSlotOper": nbsCmmcPortZoneSlotOper,
       "nbsCmmcPortZoneChassisOper": nbsCmmcPortZoneChassisOper,
       "nbsCmmcPortLinkMatch": nbsCmmcPortLinkMatch,
       "nbsCmmcPortMDIPinoutAdmin": nbsCmmcPortMDIPinoutAdmin,
       "nbsCmmcPortMDIPinoutOper": nbsCmmcPortMDIPinoutOper,
       "nbsCmmcPortFCRecvAdmin": nbsCmmcPortFCRecvAdmin,
       "nbsCmmcPortFCRecvOper": nbsCmmcPortFCRecvOper,
       "nbsCmmcPortFCSendAdmin": nbsCmmcPortFCSendAdmin,
       "nbsCmmcPortFCSendOper": nbsCmmcPortFCSendOper,
       "nbsCmmcPortAutoNegWait": nbsCmmcPortAutoNegWait,
       "nbsCmmcPortTemperatureLevel": nbsCmmcPortTemperatureLevel,
       "nbsCmmcPortTxPowerLevel": nbsCmmcPortTxPowerLevel,
       "nbsCmmcPortRxPowerLevel": nbsCmmcPortRxPowerLevel,
       "nbsCmmcPortBiasAmpsLevel": nbsCmmcPortBiasAmpsLevel,
       "nbsCmmcPortSupplyVoltsLevel": nbsCmmcPortSupplyVoltsLevel,
       "nbsCmmcPortAmpGainOper": nbsCmmcPortAmpGainOper,
       "nbsCmmcPortAmpGainAdmin": nbsCmmcPortAmpGainAdmin,
       "nbsCmmcPortAmpOutputPwrAdmin": nbsCmmcPortAmpOutputPwrAdmin,
       "nbsCmmcPortProtoCapabilities": nbsCmmcPortProtoCapabilities,
       "nbsCmmcPortProtoAdmin": nbsCmmcPortProtoAdmin,
       "nbsCmmcPortProtoOper": nbsCmmcPortProtoOper,
       "nbsCmmcPortPreambleLen": nbsCmmcPortPreambleLen,
       "nbsCmmcPortPreferred": nbsCmmcPortPreferred,
       "nbsCmmcPortCableLen": nbsCmmcPortCableLen,
       "nbsCmmcPortRedundantTxMode": nbsCmmcPortRedundantTxMode,
       "nbsCmmcPortTermination": nbsCmmcPortTermination,
       "nbsCmmcPortDescription": nbsCmmcPortDescription,
       "nbsCmmcPortTransmitUnmapped": nbsCmmcPortTransmitUnmapped,
       "nbsCmmcPortToggleMode": nbsCmmcPortToggleMode,
       "nbsCmmcPortCrossConnect": nbsCmmcPortCrossConnect,
       "nbsCmmcPortZoneIfIndexAdmin": nbsCmmcPortZoneIfIndexAdmin,
       "nbsCmmcPortZoneIfIndexOper": nbsCmmcPortZoneIfIndexOper,
       "nbsCmmcPortEnableOper": nbsCmmcPortEnableOper,
       "nbsCmmcPortMappingType": nbsCmmcPortMappingType,
       "nbsCmmcPortCountersState": nbsCmmcPortCountersState,
       "nbsCmmcPortAmpGainMinimum": nbsCmmcPortAmpGainMinimum,
       "nbsCmmcPortAmpGainMaximum": nbsCmmcPortAmpGainMaximum,
       "nbsCmmcPortAmpGainStepSize": nbsCmmcPortAmpGainStepSize,
       "nbsCmmcPortSniffer": nbsCmmcPortSniffer,
       "nbsCmmcNtpGrp": nbsCmmcNtpGrp,
       "nbsCmmcSmtpGrp": nbsCmmcSmtpGrp,
       "nbsCmmcSmtpDomainName": nbsCmmcSmtpDomainName,
       "nbsCmmcSmtpServerAddress": nbsCmmcSmtpServerAddress,
       "nbsCmmcSmtpRcvrLevel": nbsCmmcSmtpRcvrLevel,
       "nbsCmmcSmtpRcvrNum": nbsCmmcSmtpRcvrNum,
       "nbsCmmcSmtpRcvrTable": nbsCmmcSmtpRcvrTable,
       "nbsCmmcSmtpRcvrEntry": nbsCmmcSmtpRcvrEntry,
       "nbsCmmcSmtpRcvrIndex": nbsCmmcSmtpRcvrIndex,
       "nbsCmmcSmtpRcvrEmailAddress": nbsCmmcSmtpRcvrEmailAddress,
       "nbsCmmcSmtpRcvrStatus": nbsCmmcSmtpRcvrStatus,
       "nbsCmmcSysLogGrp": nbsCmmcSysLogGrp,
       "nbsCmmcSysLogRunningLevel": nbsCmmcSysLogRunningLevel,
       "nbsCmmcSysLogNvLevel": nbsCmmcSysLogNvLevel,
       "nbsCmmcSysLogTrapLevel": nbsCmmcSysLogTrapLevel,
       "nbsCmmcSysLogEmailLevel": nbsCmmcSysLogEmailLevel,
       "nbsCmmcSysLogMessageTable": nbsCmmcSysLogMessageTable,
       "nbsCmmcSysLogMessageEntry": nbsCmmcSysLogMessageEntry,
       "nbsCmmcSysLogMessageType": nbsCmmcSysLogMessageType,
       "nbsCmmcSysLogMessageSeverity": nbsCmmcSysLogMessageSeverity,
       "nbsCmmcSysRunningLogMessageTotal": nbsCmmcSysRunningLogMessageTotal,
       "nbsCmmcSysRunningLogMessageTable": nbsCmmcSysRunningLogMessageTable,
       "nbsCmmcSysRunningLogMessageEntry": nbsCmmcSysRunningLogMessageEntry,
       "nbsCmmcSysRunningLogMessageIndex": nbsCmmcSysRunningLogMessageIndex,
       "nbsCmmcSysRunningLogMessageSeverity": nbsCmmcSysRunningLogMessageSeverity,
       "nbsCmmcSysRunningLogMessageErrorID": nbsCmmcSysRunningLogMessageErrorID,
       "nbsCmmcSysRunningLogMessageSession": nbsCmmcSysRunningLogMessageSession,
       "nbsCmmcSysRunningLogMessageTime": nbsCmmcSysRunningLogMessageTime,
       "nbsCmmcSysRunningLogMessageModule": nbsCmmcSysRunningLogMessageModule,
       "nbsCmmcSysRunningLogMessageString": nbsCmmcSysRunningLogMessageString,
       "nbsCmmcSysNvramLogMessageTotal": nbsCmmcSysNvramLogMessageTotal,
       "nbsCmmcSysNvramLogMessageTable": nbsCmmcSysNvramLogMessageTable,
       "nbsCmmcSysNvramLogMessageEntry": nbsCmmcSysNvramLogMessageEntry,
       "nbsCmmcSysNvramLogMessageIndex": nbsCmmcSysNvramLogMessageIndex,
       "nbsCmmcSysNvramLogMessageSeverity": nbsCmmcSysNvramLogMessageSeverity,
       "nbsCmmcSysNvramLogMessageErrorID": nbsCmmcSysNvramLogMessageErrorID,
       "nbsCmmcSysNvramLogMessageSession": nbsCmmcSysNvramLogMessageSession,
       "nbsCmmcSysNvramLogMessageTime": nbsCmmcSysNvramLogMessageTime,
       "nbsCmmcSysNvramLogMessageModule": nbsCmmcSysNvramLogMessageModule,
       "nbsCmmcSysNvramLogMessageString": nbsCmmcSysNvramLogMessageString,
       "nbsCmmcSysNvramLogMessagePTime": nbsCmmcSysNvramLogMessagePTime,
       "nbsCmmcSysNvramLogMessageDateTime": nbsCmmcSysNvramLogMessageDateTime,
       "nbsCmmcSysAuditLogTotal": nbsCmmcSysAuditLogTotal,
       "nbsCmmcSysAuditLogTable": nbsCmmcSysAuditLogTable,
       "nbsCmmcSysAuditLogEntry": nbsCmmcSysAuditLogEntry,
       "nbsCmmcSysAuditLogIndex": nbsCmmcSysAuditLogIndex,
       "nbsCmmcSysAuditLogUpTime": nbsCmmcSysAuditLogUpTime,
       "nbsCmmcSysAuditLogDateTime": nbsCmmcSysAuditLogDateTime,
       "nbsCmmcSysAuditLogString": nbsCmmcSysAuditLogString,
       "nbsCmmcSysLogRemoteServer": nbsCmmcSysLogRemoteServer,
       "nbsCmmcSysLogRemoteLevel": nbsCmmcSysLogRemoteLevel,
       "nbsCmmcSysRunningLogMessageClear": nbsCmmcSysRunningLogMessageClear,
       "nbsCmmcSysNvramLogMessageClear": nbsCmmcSysNvramLogMessageClear,
       "nbsCmmcSysAuditLogClear": nbsCmmcSysAuditLogClear,
       "nbsCmmcSysLogNvSize": nbsCmmcSysLogNvSize,
       "nbsCmmcTrapGrp": nbsCmmcTrapGrp,
       "nbsCmmcTrapLastMessage": nbsCmmcTrapLastMessage,
       "nbsCmmcTrapPowerSupplyId": nbsCmmcTrapPowerSupplyId,
       "nbsCmmcTrapFanId": nbsCmmcTrapFanId,
       "nbsCmmcTrapPortIndex": nbsCmmcTrapPortIndex,
       "nbsCmmcTrapPortName": nbsCmmcTrapPortName,
       "nbsCmmcTrapShutdownReason": nbsCmmcTrapShutdownReason,
       "nbsCmmcTrapErrorInfo": nbsCmmcTrapErrorInfo,
       "nbsCmmcTraps": nbsCmmcTraps,
       "nbsCmmcTraps0": nbsCmmcTraps0,
       "nbsCmmcTrapGenericTrap": nbsCmmcTrapGenericTrap,
       "nbsCmmcTrapSpecificTrap": nbsCmmcTrapSpecificTrap,
       "nbsCmmcTrapDeviceRebooted": nbsCmmcTrapDeviceRebooted,
       "nbsCmmcTrapDeviceOnline": nbsCmmcTrapDeviceOnline,
       "nbsCmmcTrapDeviceShuttingDown": nbsCmmcTrapDeviceShuttingDown,
       "nbsCmmcTrapPowerSupplyFailure": nbsCmmcTrapPowerSupplyFailure,
       "nbsCmmcTrapPowerSupplyRestored": nbsCmmcTrapPowerSupplyRestored,
       "nbsCmmcTrapFanFailure": nbsCmmcTrapFanFailure,
       "nbsCmmcTrapFanRestored": nbsCmmcTrapFanRestored,
       "nbsCmmcTrapChassisTooHot": nbsCmmcTrapChassisTooHot,
       "nbsCmmcTrapChassisTooCold": nbsCmmcTrapChassisTooCold,
       "nbsCmmcTrapChassisTempOk": nbsCmmcTrapChassisTempOk,
       "nbsCmmcTrapSlotModuleIn": nbsCmmcTrapSlotModuleIn,
       "nbsCmmcTrapSlotModuleOut": nbsCmmcTrapSlotModuleOut,
       "nbsCmmcTrapPortEnabled": nbsCmmcTrapPortEnabled,
       "nbsCmmcTrapPortDisabled": nbsCmmcTrapPortDisabled,
       "nbsCmmcTrapPortLinkUp": nbsCmmcTrapPortLinkUp,
       "nbsCmmcTrapPortLinkDown": nbsCmmcTrapPortLinkDown,
       "nbsCmmcTrapPortLINOn": nbsCmmcTrapPortLINOn,
       "nbsCmmcTrapPortLINOff": nbsCmmcTrapPortLINOff,
       "nbsCmmcTrapPortLoopbackOn": nbsCmmcTrapPortLoopbackOn,
       "nbsCmmcTrapPortLoopbackOff": nbsCmmcTrapPortLoopbackOff,
       "nbsCmmcTrapPortMaximumExceeded": nbsCmmcTrapPortMaximumExceeded,
       "nbsCmmcTrapPortRemoved": nbsCmmcTrapPortRemoved,
       "nbsCmmcTrapPortInserted": nbsCmmcTrapPortInserted,
       "nbsCmmcTrapPortTempTooLow": nbsCmmcTrapPortTempTooLow,
       "nbsCmmcTrapPortTempTooHigh": nbsCmmcTrapPortTempTooHigh,
       "nbsCmmcTrapPortRxPowerTooLow": nbsCmmcTrapPortRxPowerTooLow,
       "nbsCmmcTrapPortRxPowerTooHigh": nbsCmmcTrapPortRxPowerTooHigh,
       "nbsCmmcTrapPortTxPowerTooLow": nbsCmmcTrapPortTxPowerTooLow,
       "nbsCmmcTrapPortTxPowerTooHigh": nbsCmmcTrapPortTxPowerTooHigh,
       "nbsCmmcTrapPortAmpsTooLow": nbsCmmcTrapPortAmpsTooLow,
       "nbsCmmcTrapPortAmpsTooHigh": nbsCmmcTrapPortAmpsTooHigh,
       "nbsCmmcTrapPortVoltsTooLow": nbsCmmcTrapPortVoltsTooLow,
       "nbsCmmcTrapPortVoltsTooHigh": nbsCmmcTrapPortVoltsTooHigh,
       "nbsCmmcTrapSwitchover": nbsCmmcTrapSwitchover,
       "nbsCmmcTrapSlotShuttingDown": nbsCmmcTrapSlotShuttingDown,
       "nbsCmmcTrapPortCrcError": nbsCmmcTrapPortCrcError,
       "nbsCmmcTrapCpeInManagedChassis": nbsCmmcTrapCpeInManagedChassis,
       "nbsCmmcTrapCoWithoutCpe": nbsCmmcTrapCoWithoutCpe,
       "nbsCmmcTrapCoTakesControl": nbsCmmcTrapCoTakesControl,
       "nbsCmmcTrapCoYieldsControl": nbsCmmcTrapCoYieldsControl,
       "nbsCmmcTrapCoLinkedToCo": nbsCmmcTrapCoLinkedToCo,
       "nbsCmmcTrapCpeFound": nbsCmmcTrapCpeFound,
       "nbsCmmcTrapPortReflectionDetected": nbsCmmcTrapPortReflectionDetected,
       "nbsCmmcTrapPortReflectionCeased": nbsCmmcTrapPortReflectionCeased,
       "nbsCmmcTrapPortTempOk": nbsCmmcTrapPortTempOk,
       "nbsCmmcTrapPortRxPowerOk": nbsCmmcTrapPortRxPowerOk,
       "nbsCmmcTrapPortTxPowerOk": nbsCmmcTrapPortTxPowerOk,
       "nbsCmmcTrapPortAmpsOk": nbsCmmcTrapPortAmpsOk,
       "nbsCmmcTrapPortVoltsOk": nbsCmmcTrapPortVoltsOk,
       "nbsCmmcTrapSlotTempTooLow": nbsCmmcTrapSlotTempTooLow,
       "nbsCmmcTrapSlotTempTooHigh": nbsCmmcTrapSlotTempTooHigh,
       "nbsCmmcTrapSlotTempOk": nbsCmmcTrapSlotTempOk,
       "nbsCmmcTrapPortErrorsDetected": nbsCmmcTrapPortErrorsDetected,
       "nbsCmmcTrapPortErrorsStopped": nbsCmmcTrapPortErrorsStopped}
)
