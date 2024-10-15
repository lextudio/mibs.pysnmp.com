# SNMP MIB module (SYMM-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SYMM-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 22:59:41 2024
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

symmetricom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070)
)
symmetricom.setRevisions(
        ("1910-02-06 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SymmNetworkManagement_ObjectIdentity = ObjectIdentity
symmNetworkManagement = _SymmNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1)
)
if mibBuilder.loadTexts:
    symmNetworkManagement.setStatus("current")
_SymmCmipManagement_ObjectIdentity = ObjectIdentity
symmCmipManagement = _SymmCmipManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 1)
)
if mibBuilder.loadTexts:
    symmCmipManagement.setStatus("current")
_SymmSnmpManagement_ObjectIdentity = ObjectIdentity
symmSnmpManagement = _SymmSnmpManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2)
)
if mibBuilder.loadTexts:
    symmSnmpManagement.setStatus("current")
_SymmTimePictra_ObjectIdentity = ObjectIdentity
symmTimePictra = _SymmTimePictra_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 1)
)
if mibBuilder.loadTexts:
    symmTimePictra.setStatus("current")
_SymmBroadband_ObjectIdentity = ObjectIdentity
symmBroadband = _SymmBroadband_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 2)
)
if mibBuilder.loadTexts:
    symmBroadband.setStatus("current")
_SymmTTM_ObjectIdentity = ObjectIdentity
symmTTM = _SymmTTM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3)
)
if mibBuilder.loadTexts:
    symmTTM.setStatus("current")
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1)
)
_Ts2000_ObjectIdentity = ObjectIdentity
ts2000 = _Ts2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 1)
)
_Nts_ObjectIdentity = ObjectIdentity
nts = _Nts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 2)
)
_Ts2100_ObjectIdentity = ObjectIdentity
ts2100 = _Ts2100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 3)
)
_S100_ObjectIdentity = ObjectIdentity
s100 = _S100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 4)
)
_Syncserver_ObjectIdentity = ObjectIdentity
syncserver = _Syncserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5)
)
_Version_ObjectIdentity = ObjectIdentity
version = _Version_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1)
)
_NtpSystem_ObjectIdentity = ObjectIdentity
ntpSystem = _NtpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1)
)


class _NtpSysLeap_Type(Integer32):
    """Custom type ntpSysLeap based on Integer32"""
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
        *(("addSecond", 1),
          ("alarm", 3),
          ("noWarning", 0),
          ("subtractSecond", 2))
    )


_NtpSysLeap_Type.__name__ = "Integer32"
_NtpSysLeap_Object = MibScalar
ntpSysLeap = _NtpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 1),
    _NtpSysLeap_Type()
)
ntpSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysLeap.setStatus("current")


class _NtpSysStratum_Type(Integer32):
    """Custom type ntpSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NtpSysStratum_Type.__name__ = "Integer32"
_NtpSysStratum_Object = MibScalar
ntpSysStratum = _NtpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 2),
    _NtpSysStratum_Type()
)
ntpSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysStratum.setStatus("current")
_NtpSysPrecision_Type = Integer32
_NtpSysPrecision_Object = MibScalar
ntpSysPrecision = _NtpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 3),
    _NtpSysPrecision_Type()
)
ntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPrecision.setStatus("current")
_NtpSysRootDelay_Type = OctetString
_NtpSysRootDelay_Object = MibScalar
ntpSysRootDelay = _NtpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 4),
    _NtpSysRootDelay_Type()
)
ntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRootDelay.setStatus("current")
_NtpSysRootDispersion_Type = OctetString
_NtpSysRootDispersion_Object = MibScalar
ntpSysRootDispersion = _NtpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 5),
    _NtpSysRootDispersion_Type()
)
ntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRootDispersion.setStatus("current")


class _NtpSysRefID_Type(DisplayString):
    """Custom type ntpSysRefID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysRefID_Type.__name__ = "DisplayString"
_NtpSysRefID_Object = MibScalar
ntpSysRefID = _NtpSysRefID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 6),
    _NtpSysRefID_Type()
)
ntpSysRefID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRefID.setStatus("current")


class _NtpSysRefTime_Type(DisplayString):
    """Custom type ntpSysRefTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysRefTime_Type.__name__ = "DisplayString"
_NtpSysRefTime_Object = MibScalar
ntpSysRefTime = _NtpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 7),
    _NtpSysRefTime_Type()
)
ntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysRefTime.setStatus("current")
_NtpSysPoll_Type = Integer32
_NtpSysPoll_Object = MibScalar
ntpSysPoll = _NtpSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 8),
    _NtpSysPoll_Type()
)
ntpSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPoll.setStatus("current")
_NtpSysPeer_Type = Unsigned32
_NtpSysPeer_Object = MibScalar
ntpSysPeer = _NtpSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 9),
    _NtpSysPeer_Type()
)
ntpSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPeer.setStatus("current")


class _NtpSysPhase_Type(DisplayString):
    """Custom type ntpSysPhase based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysPhase_Type.__name__ = "DisplayString"
_NtpSysPhase_Object = MibScalar
ntpSysPhase = _NtpSysPhase_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 10),
    _NtpSysPhase_Type()
)
ntpSysPhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPhase.setStatus("current")


class _NtpSysFreq_Type(DisplayString):
    """Custom type ntpSysFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysFreq_Type.__name__ = "DisplayString"
_NtpSysFreq_Object = MibScalar
ntpSysFreq = _NtpSysFreq_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 11),
    _NtpSysFreq_Type()
)
ntpSysFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysFreq.setStatus("current")


class _NtpSysError_Type(DisplayString):
    """Custom type ntpSysError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysError_Type.__name__ = "DisplayString"
_NtpSysError_Object = MibScalar
ntpSysError = _NtpSysError_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 12),
    _NtpSysError_Type()
)
ntpSysError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysError.setStatus("current")


class _NtpSysClock_Type(DisplayString):
    """Custom type ntpSysClock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysClock_Type.__name__ = "DisplayString"
_NtpSysClock_Object = MibScalar
ntpSysClock = _NtpSysClock_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 13),
    _NtpSysClock_Type()
)
ntpSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysClock.setStatus("current")


class _NtpSysSystem_Type(DisplayString):
    """Custom type ntpSysSystem based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_NtpSysSystem_Type.__name__ = "DisplayString"
_NtpSysSystem_Object = MibScalar
ntpSysSystem = _NtpSysSystem_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 14),
    _NtpSysSystem_Type()
)
ntpSysSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysSystem.setStatus("current")


class _NtpSysProcessor_Type(DisplayString):
    """Custom type ntpSysProcessor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_NtpSysProcessor_Type.__name__ = "DisplayString"
_NtpSysProcessor_Object = MibScalar
ntpSysProcessor = _NtpSysProcessor_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 15),
    _NtpSysProcessor_Type()
)
ntpSysProcessor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysProcessor.setStatus("current")


class _NtpSysNotrust_Type(Integer32):
    """Custom type ntpSysNotrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NtpSysNotrust_Type.__name__ = "Integer32"
_NtpSysNotrust_Object = MibScalar
ntpSysNotrust = _NtpSysNotrust_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 16),
    _NtpSysNotrust_Type()
)
ntpSysNotrust.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysNotrust.setStatus("mandatory")


class _NtpSysPktsReceived_Type(Integer32):
    """Custom type ntpSysPktsReceived based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32768),
    )


_NtpSysPktsReceived_Type.__name__ = "Integer32"
_NtpSysPktsReceived_Object = MibScalar
ntpSysPktsReceived = _NtpSysPktsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 17),
    _NtpSysPktsReceived_Type()
)
ntpSysPktsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysPktsReceived.setStatus("mandatory")


class _NtpSysMode_Type(Integer32):
    """Custom type ntpSysMode based on Integer32"""
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
        *(("broadcast", 5),
          ("client", 3),
          ("reservedctl", 6),
          ("reservedpriv", 7),
          ("server", 4),
          ("symactive", 1),
          ("sympassive", 2),
          ("unspecified", 0))
    )


_NtpSysMode_Type.__name__ = "Integer32"
_NtpSysMode_Object = MibScalar
ntpSysMode = _NtpSysMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 18),
    _NtpSysMode_Type()
)
ntpSysMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysMode.setStatus("mandatory")


class _NtpSysVersion_Type(DisplayString):
    """Custom type ntpSysVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_NtpSysVersion_Type.__name__ = "DisplayString"
_NtpSysVersion_Object = MibScalar
ntpSysVersion = _NtpSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 1, 19),
    _NtpSysVersion_Type()
)
ntpSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpSysVersion.setStatus("current")
_Tyming_ObjectIdentity = ObjectIdentity
tyming = _Tyming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2)
)


class _TymingStatus_Type(DisplayString):
    """Custom type tymingStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_TymingStatus_Type.__name__ = "DisplayString"
_TymingStatus_Object = MibScalar
tymingStatus = _TymingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 1),
    _TymingStatus_Type()
)
tymingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tymingStatus.setStatus("current")


class _TymingSource_Type(DisplayString):
    """Custom type tymingSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TymingSource_Type.__name__ = "DisplayString"
_TymingSource_Object = MibScalar
tymingSource = _TymingSource_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 2),
    _TymingSource_Type()
)
tymingSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tymingSource.setStatus("current")


class _TymingTime_Type(DisplayString):
    """Custom type tymingTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TymingTime_Type.__name__ = "DisplayString"
_TymingTime_Object = MibScalar
tymingTime = _TymingTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 3),
    _TymingTime_Type()
)
tymingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tymingTime.setStatus("current")


class _TymingVersion_Type(DisplayString):
    """Custom type tymingVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_TymingVersion_Type.__name__ = "DisplayString"
_TymingVersion_Object = MibScalar
tymingVersion = _TymingVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 4),
    _TymingVersion_Type()
)
tymingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tymingVersion.setStatus("current")
_TymingFlyPeriod_Type = Integer32
_TymingFlyPeriod_Object = MibScalar
tymingFlyPeriod = _TymingFlyPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 2, 5),
    _TymingFlyPeriod_Type()
)
tymingFlyPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tymingFlyPeriod.setStatus("current")
_Gps_ObjectIdentity = ObjectIdentity
gps = _Gps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3)
)


class _GpsPosition_Type(DisplayString):
    """Custom type gpsPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GpsPosition_Type.__name__ = "DisplayString"
_GpsPosition_Object = MibScalar
gpsPosition = _GpsPosition_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 1),
    _GpsPosition_Type()
)
gpsPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsPosition.setStatus("current")


class _GpsUTCOffset_Type(Integer32):
    """Custom type gpsUTCOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_GpsUTCOffset_Type.__name__ = "Integer32"
_GpsUTCOffset_Object = MibScalar
gpsUTCOffset = _GpsUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 2),
    _GpsUTCOffset_Type()
)
gpsUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsUTCOffset.setStatus("current")


class _GpsHealth_Type(DisplayString):
    """Custom type gpsHealth based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GpsHealth_Type.__name__ = "DisplayString"
_GpsHealth_Object = MibScalar
gpsHealth = _GpsHealth_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 3),
    _GpsHealth_Type()
)
gpsHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsHealth.setStatus("current")


class _GpsSatlist_Type(DisplayString):
    """Custom type gpsSatlist based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_GpsSatlist_Type.__name__ = "DisplayString"
_GpsSatlist_Object = MibScalar
gpsSatlist = _GpsSatlist_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 4),
    _GpsSatlist_Type()
)
gpsSatlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsSatlist.setStatus("current")


class _GpsMode_Type(DisplayString):
    """Custom type gpsMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_GpsMode_Type.__name__ = "DisplayString"
_GpsMode_Object = MibScalar
gpsMode = _GpsMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 3, 5),
    _GpsMode_Type()
)
gpsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gpsMode.setStatus("current")
_Dialup_ObjectIdentity = ObjectIdentity
dialup = _Dialup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 4)
)
_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 5)
)
_Etc_ObjectIdentity = ObjectIdentity
etc = _Etc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6)
)


class _EtcVersion_Type(DisplayString):
    """Custom type etcVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_EtcVersion_Type.__name__ = "DisplayString"
_EtcVersion_Object = MibScalar
etcVersion = _EtcVersion_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 1),
    _EtcVersion_Type()
)
etcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcVersion.setStatus("current")


class _EtcSerialNbr_Type(DisplayString):
    """Custom type etcSerialNbr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_EtcSerialNbr_Type.__name__ = "DisplayString"
_EtcSerialNbr_Object = MibScalar
etcSerialNbr = _EtcSerialNbr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 2),
    _EtcSerialNbr_Type()
)
etcSerialNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcSerialNbr.setStatus("current")


class _EtcModel_Type(DisplayString):
    """Custom type etcModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_EtcModel_Type.__name__ = "DisplayString"
_EtcModel_Object = MibScalar
etcModel = _EtcModel_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 3),
    _EtcModel_Type()
)
etcModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcModel.setStatus("current")


class _EtcUpgrade_Type(DisplayString):
    """Custom type etcUpgrade based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_EtcUpgrade_Type.__name__ = "DisplayString"
_EtcUpgrade_Object = MibScalar
etcUpgrade = _EtcUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 4),
    _EtcUpgrade_Type()
)
etcUpgrade.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcUpgrade.setStatus("current")


class _EtcUpgradeServer_Type(DisplayString):
    """Custom type etcUpgradeServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_EtcUpgradeServer_Type.__name__ = "DisplayString"
_EtcUpgradeServer_Object = MibScalar
etcUpgradeServer = _EtcUpgradeServer_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 5),
    _EtcUpgradeServer_Type()
)
etcUpgradeServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcUpgradeServer.setStatus("current")


class _EtcAlarmString_Type(DisplayString):
    """Custom type etcAlarmString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_EtcAlarmString_Type.__name__ = "DisplayString"
_EtcAlarmString_Object = MibScalar
etcAlarmString = _EtcAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 5, 1, 6, 6),
    _EtcAlarmString_Type()
)
etcAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etcAlarmString.setStatus("current")
_Xli_ObjectIdentity = ObjectIdentity
xli = _Xli_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 1, 6)
)
_Experiment_ObjectIdentity = ObjectIdentity
experiment = _Experiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 3, 99)
)

# Managed Objects groups


# Notification objects

etcAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9070, 0, 0)
)
etcAlarm.setObjects(
    ("SYMM-SMI", "etcAlarmString")
)
if mibBuilder.loadTexts:
    etcAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SYMM-SMI",
    **{"symmetricom": symmetricom,
       "etcAlarm": etcAlarm,
       "symmNetworkManagement": symmNetworkManagement,
       "symmCmipManagement": symmCmipManagement,
       "symmSnmpManagement": symmSnmpManagement,
       "symmTimePictra": symmTimePictra,
       "symmBroadband": symmBroadband,
       "symmTTM": symmTTM,
       "products": products,
       "ts2000": ts2000,
       "nts": nts,
       "ts2100": ts2100,
       "s100": s100,
       "syncserver": syncserver,
       "version": version,
       "ntpSystem": ntpSystem,
       "ntpSysLeap": ntpSysLeap,
       "ntpSysStratum": ntpSysStratum,
       "ntpSysPrecision": ntpSysPrecision,
       "ntpSysRootDelay": ntpSysRootDelay,
       "ntpSysRootDispersion": ntpSysRootDispersion,
       "ntpSysRefID": ntpSysRefID,
       "ntpSysRefTime": ntpSysRefTime,
       "ntpSysPoll": ntpSysPoll,
       "ntpSysPeer": ntpSysPeer,
       "ntpSysPhase": ntpSysPhase,
       "ntpSysFreq": ntpSysFreq,
       "ntpSysError": ntpSysError,
       "ntpSysClock": ntpSysClock,
       "ntpSysSystem": ntpSysSystem,
       "ntpSysProcessor": ntpSysProcessor,
       "ntpSysNotrust": ntpSysNotrust,
       "ntpSysPktsReceived": ntpSysPktsReceived,
       "ntpSysMode": ntpSysMode,
       "ntpSysVersion": ntpSysVersion,
       "tyming": tyming,
       "tymingStatus": tymingStatus,
       "tymingSource": tymingSource,
       "tymingTime": tymingTime,
       "tymingVersion": tymingVersion,
       "tymingFlyPeriod": tymingFlyPeriod,
       "gps": gps,
       "gpsPosition": gpsPosition,
       "gpsUTCOffset": gpsUTCOffset,
       "gpsHealth": gpsHealth,
       "gpsSatlist": gpsSatlist,
       "gpsMode": gpsMode,
       "dialup": dialup,
       "net": net,
       "etc": etc,
       "etcVersion": etcVersion,
       "etcSerialNbr": etcSerialNbr,
       "etcModel": etcModel,
       "etcUpgrade": etcUpgrade,
       "etcUpgradeServer": etcUpgradeServer,
       "etcAlarmString": etcAlarmString,
       "xli": xli,
       "experiment": experiment}
)
