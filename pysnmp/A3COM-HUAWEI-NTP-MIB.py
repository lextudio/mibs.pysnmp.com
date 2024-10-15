# SNMP MIB module (A3COM-HUAWEI-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:28:45 2024
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

(huaweiDatacomm,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "huaweiDatacomm")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwNTP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22)
)
hwNTP.setRevisions(
        ("2003-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwNTPSystemMIB_ObjectIdentity = ObjectIdentity
hwNTPSystemMIB = _HwNTPSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1)
)
_HwNTPSystemMIBObjects_ObjectIdentity = ObjectIdentity
hwNTPSystemMIBObjects = _HwNTPSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1)
)


class _HwNTPSysLeap_Type(Integer32):
    """Custom type hwNTPSysLeap based on Integer32"""
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


_HwNTPSysLeap_Type.__name__ = "Integer32"
_HwNTPSysLeap_Object = MibScalar
hwNTPSysLeap = _HwNTPSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 1),
    _HwNTPSysLeap_Type()
)
hwNTPSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysLeap.setStatus("current")


class _HwNTPSysStratum_Type(Integer32):
    """Custom type hwNTPSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwNTPSysStratum_Type.__name__ = "Integer32"
_HwNTPSysStratum_Object = MibScalar
hwNTPSysStratum = _HwNTPSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 2),
    _HwNTPSysStratum_Type()
)
hwNTPSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysStratum.setStatus("current")


class _HwNTPSysPrecision_Type(Integer32):
    """Custom type hwNTPSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HwNTPSysPrecision_Type.__name__ = "Integer32"
_HwNTPSysPrecision_Object = MibScalar
hwNTPSysPrecision = _HwNTPSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 3),
    _HwNTPSysPrecision_Type()
)
hwNTPSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysPrecision.setStatus("current")


class _HwNTPSysRootdelay_Type(OctetString):
    """Custom type hwNTPSysRootdelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysRootdelay_Type.__name__ = "OctetString"
_HwNTPSysRootdelay_Object = MibScalar
hwNTPSysRootdelay = _HwNTPSysRootdelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 4),
    _HwNTPSysRootdelay_Type()
)
hwNTPSysRootdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysRootdelay.setStatus("current")


class _HwNTPSysRootdispersion_Type(OctetString):
    """Custom type hwNTPSysRootdispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysRootdispersion_Type.__name__ = "OctetString"
_HwNTPSysRootdispersion_Object = MibScalar
hwNTPSysRootdispersion = _HwNTPSysRootdispersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 5),
    _HwNTPSysRootdispersion_Type()
)
hwNTPSysRootdispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysRootdispersion.setStatus("current")


class _HwNTPSysRefid_Type(OctetString):
    """Custom type hwNTPSysRefid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysRefid_Type.__name__ = "OctetString"
_HwNTPSysRefid_Object = MibScalar
hwNTPSysRefid = _HwNTPSysRefid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 6),
    _HwNTPSysRefid_Type()
)
hwNTPSysRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysRefid.setStatus("current")


class _HwNTPSysReftime_Type(OctetString):
    """Custom type hwNTPSysReftime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysReftime_Type.__name__ = "OctetString"
_HwNTPSysReftime_Object = MibScalar
hwNTPSysReftime = _HwNTPSysReftime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 7),
    _HwNTPSysReftime_Type()
)
hwNTPSysReftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysReftime.setStatus("current")


class _HwNTPSysPoll_Type(Integer32):
    """Custom type hwNTPSysPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HwNTPSysPoll_Type.__name__ = "Integer32"
_HwNTPSysPoll_Object = MibScalar
hwNTPSysPoll = _HwNTPSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 8),
    _HwNTPSysPoll_Type()
)
hwNTPSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysPoll.setStatus("current")


class _HwNTPSysPeer_Type(Integer32):
    """Custom type hwNTPSysPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwNTPSysPeer_Type.__name__ = "Integer32"
_HwNTPSysPeer_Object = MibScalar
hwNTPSysPeer = _HwNTPSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 9),
    _HwNTPSysPeer_Type()
)
hwNTPSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysPeer.setStatus("current")


class _HwNTPSysState_Type(Integer32):
    """Custom type hwNTPSysState based on Integer32"""
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
        *(("clockBySet", 2),
          ("clockBySetAndNoFreq", 3),
          ("clockBySyns", 4),
          ("findError", 5),
          ("getfreqInfo", 1),
          ("noUpdateClock", 0))
    )


_HwNTPSysState_Type.__name__ = "Integer32"
_HwNTPSysState_Object = MibScalar
hwNTPSysState = _HwNTPSysState_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 10),
    _HwNTPSysState_Type()
)
hwNTPSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysState.setStatus("current")


class _HwNTPSysOffset_Type(OctetString):
    """Custom type hwNTPSysOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysOffset_Type.__name__ = "OctetString"
_HwNTPSysOffset_Object = MibScalar
hwNTPSysOffset = _HwNTPSysOffset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 11),
    _HwNTPSysOffset_Type()
)
hwNTPSysOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysOffset.setStatus("current")


class _HwNTPSysDrift_Type(OctetString):
    """Custom type hwNTPSysDrift based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysDrift_Type.__name__ = "OctetString"
_HwNTPSysDrift_Object = MibScalar
hwNTPSysDrift = _HwNTPSysDrift_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 12),
    _HwNTPSysDrift_Type()
)
hwNTPSysDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysDrift.setStatus("current")


class _HwNTPSysCompliance_Type(OctetString):
    """Custom type hwNTPSysCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysCompliance_Type.__name__ = "OctetString"
_HwNTPSysCompliance_Object = MibScalar
hwNTPSysCompliance = _HwNTPSysCompliance_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 13),
    _HwNTPSysCompliance_Type()
)
hwNTPSysCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysCompliance.setStatus("current")


class _HwNTPSysClock_Type(OctetString):
    """Custom type hwNTPSysClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysClock_Type.__name__ = "OctetString"
_HwNTPSysClock_Object = MibScalar
hwNTPSysClock = _HwNTPSysClock_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 14),
    _HwNTPSysClock_Type()
)
hwNTPSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysClock.setStatus("current")


class _HwNTPSysStabil_Type(OctetString):
    """Custom type hwNTPSysStabil based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPSysStabil_Type.__name__ = "OctetString"
_HwNTPSysStabil_Object = MibScalar
hwNTPSysStabil = _HwNTPSysStabil_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 15),
    _HwNTPSysStabil_Type()
)
hwNTPSysStabil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysStabil.setStatus("current")


class _HwNTPSysAuthenticate_Type(Integer32):
    """Custom type hwNTPSysAuthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("authenticate", 1),
          ("noAuthenticate", 0))
    )


_HwNTPSysAuthenticate_Type.__name__ = "Integer32"
_HwNTPSysAuthenticate_Object = MibScalar
hwNTPSysAuthenticate = _HwNTPSysAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 16),
    _HwNTPSysAuthenticate_Type()
)
hwNTPSysAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNTPSysAuthenticate.setStatus("current")


class _HwNTPSysPollSec_Type(Integer32):
    """Custom type hwNTPSysPollSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1048576),
    )


_HwNTPSysPollSec_Type.__name__ = "Integer32"
_HwNTPSysPollSec_Object = MibScalar
hwNTPSysPollSec = _HwNTPSysPollSec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 17),
    _HwNTPSysPollSec_Type()
)
hwNTPSysPollSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNTPSysPollSec.setStatus("current")
_HwNTPSysClockSec_Type = Integer32
_HwNTPSysClockSec_Object = MibScalar
hwNTPSysClockSec = _HwNTPSysClockSec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 18),
    _HwNTPSysClockSec_Type()
)
hwNTPSysClockSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPSysClockSec.setStatus("current")
_HwNTPServerIP_Type = IpAddress
_HwNTPServerIP_Object = MibScalar
hwNTPServerIP = _HwNTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 1, 1, 19),
    _HwNTPServerIP_Type()
)
hwNTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNTPServerIP.setStatus("current")
_HwNTPPeerMIB_ObjectIdentity = ObjectIdentity
hwNTPPeerMIB = _HwNTPPeerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2)
)
_HwNTPPeerMIBObjects_ObjectIdentity = ObjectIdentity
hwNTPPeerMIBObjects = _HwNTPPeerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1)
)
_HwNTPPeerTable_Object = MibTable
hwNTPPeerTable = _HwNTPPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwNTPPeerTable.setStatus("current")
_HwNTPPeerEntry_Object = MibTableRow
hwNTPPeerEntry = _HwNTPPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1)
)
hwNTPPeerEntry.setIndexNames(
    (0, "A3COM-HUAWEI-NTP-MIB", "hwNTPPeerRemAdr"),
    (0, "A3COM-HUAWEI-NTP-MIB", "hwNTPPeerHMode"),
)
if mibBuilder.loadTexts:
    hwNTPPeerEntry.setStatus("current")
_HwNTPPeerConfig_Type = TruthValue
_HwNTPPeerConfig_Object = MibTableColumn
hwNTPPeerConfig = _HwNTPPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 1),
    _HwNTPPeerConfig_Type()
)
hwNTPPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerConfig.setStatus("current")
_HwNTPPeerAuthenable_Type = TruthValue
_HwNTPPeerAuthenable_Object = MibTableColumn
hwNTPPeerAuthenable = _HwNTPPeerAuthenable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 2),
    _HwNTPPeerAuthenable_Type()
)
hwNTPPeerAuthenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerAuthenable.setStatus("current")
_HwNTPPeerAuthentic_Type = TruthValue
_HwNTPPeerAuthentic_Object = MibTableColumn
hwNTPPeerAuthentic = _HwNTPPeerAuthentic_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 3),
    _HwNTPPeerAuthentic_Type()
)
hwNTPPeerAuthentic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerAuthentic.setStatus("current")
_HwNTPPeerRemAdr_Type = IpAddress
_HwNTPPeerRemAdr_Object = MibTableColumn
hwNTPPeerRemAdr = _HwNTPPeerRemAdr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 4),
    _HwNTPPeerRemAdr_Type()
)
hwNTPPeerRemAdr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNTPPeerRemAdr.setStatus("current")


class _HwNTPPeerRemPort_Type(Integer32):
    """Custom type hwNTPPeerRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNTPPeerRemPort_Type.__name__ = "Integer32"
_HwNTPPeerRemPort_Object = MibTableColumn
hwNTPPeerRemPort = _HwNTPPeerRemPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 5),
    _HwNTPPeerRemPort_Type()
)
hwNTPPeerRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRemPort.setStatus("current")
_HwNTPPeerLocAdr_Type = IpAddress
_HwNTPPeerLocAdr_Object = MibTableColumn
hwNTPPeerLocAdr = _HwNTPPeerLocAdr_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 6),
    _HwNTPPeerLocAdr_Type()
)
hwNTPPeerLocAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerLocAdr.setStatus("current")


class _HwNTPPeerLocPort_Type(Integer32):
    """Custom type hwNTPPeerLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwNTPPeerLocPort_Type.__name__ = "Integer32"
_HwNTPPeerLocPort_Object = MibTableColumn
hwNTPPeerLocPort = _HwNTPPeerLocPort_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 7),
    _HwNTPPeerLocPort_Type()
)
hwNTPPeerLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerLocPort.setStatus("current")


class _HwNTPPeerLeap_Type(Integer32):
    """Custom type hwNTPPeerLeap based on Integer32"""
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


_HwNTPPeerLeap_Type.__name__ = "Integer32"
_HwNTPPeerLeap_Object = MibTableColumn
hwNTPPeerLeap = _HwNTPPeerLeap_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 8),
    _HwNTPPeerLeap_Type()
)
hwNTPPeerLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerLeap.setStatus("current")


class _HwNTPPeerHMode_Type(Integer32):
    """Custom type hwNTPPeerHMode based on Integer32"""
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
        *(("broadcast", 5),
          ("broadcastclient", 8),
          ("client", 3),
          ("multicastclient", 9),
          ("reservedControl", 6),
          ("reservedPrivate", 7),
          ("server", 4),
          ("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("unspecified", 0))
    )


_HwNTPPeerHMode_Type.__name__ = "Integer32"
_HwNTPPeerHMode_Object = MibTableColumn
hwNTPPeerHMode = _HwNTPPeerHMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 9),
    _HwNTPPeerHMode_Type()
)
hwNTPPeerHMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNTPPeerHMode.setStatus("current")


class _HwNTPPeerStratum_Type(Integer32):
    """Custom type hwNTPPeerStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwNTPPeerStratum_Type.__name__ = "Integer32"
_HwNTPPeerStratum_Object = MibTableColumn
hwNTPPeerStratum = _HwNTPPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 10),
    _HwNTPPeerStratum_Type()
)
hwNTPPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerStratum.setStatus("current")


class _HwNTPPeerPPoll_Type(Integer32):
    """Custom type hwNTPPeerPPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HwNTPPeerPPoll_Type.__name__ = "Integer32"
_HwNTPPeerPPoll_Object = MibTableColumn
hwNTPPeerPPoll = _HwNTPPeerPPoll_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 11),
    _HwNTPPeerPPoll_Type()
)
hwNTPPeerPPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerPPoll.setStatus("current")


class _HwNTPPeerHPoll_Type(Integer32):
    """Custom type hwNTPPeerHPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HwNTPPeerHPoll_Type.__name__ = "Integer32"
_HwNTPPeerHPoll_Object = MibTableColumn
hwNTPPeerHPoll = _HwNTPPeerHPoll_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 12),
    _HwNTPPeerHPoll_Type()
)
hwNTPPeerHPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerHPoll.setStatus("current")


class _HwNTPPeerPrecision_Type(Integer32):
    """Custom type hwNTPPeerPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HwNTPPeerPrecision_Type.__name__ = "Integer32"
_HwNTPPeerPrecision_Object = MibTableColumn
hwNTPPeerPrecision = _HwNTPPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 13),
    _HwNTPPeerPrecision_Type()
)
hwNTPPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerPrecision.setStatus("current")


class _HwNTPPeerRootDelay_Type(OctetString):
    """Custom type hwNTPPeerRootDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerRootDelay_Type.__name__ = "OctetString"
_HwNTPPeerRootDelay_Object = MibTableColumn
hwNTPPeerRootDelay = _HwNTPPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 14),
    _HwNTPPeerRootDelay_Type()
)
hwNTPPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRootDelay.setStatus("current")


class _HwNTPPeerRootDispersion_Type(OctetString):
    """Custom type hwNTPPeerRootDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerRootDispersion_Type.__name__ = "OctetString"
_HwNTPPeerRootDispersion_Object = MibTableColumn
hwNTPPeerRootDispersion = _HwNTPPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 15),
    _HwNTPPeerRootDispersion_Type()
)
hwNTPPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRootDispersion.setStatus("current")


class _HwNTPPeerRefId_Type(OctetString):
    """Custom type hwNTPPeerRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerRefId_Type.__name__ = "OctetString"
_HwNTPPeerRefId_Object = MibTableColumn
hwNTPPeerRefId = _HwNTPPeerRefId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 16),
    _HwNTPPeerRefId_Type()
)
hwNTPPeerRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRefId.setStatus("current")


class _HwNTPPeerRefTime_Type(OctetString):
    """Custom type hwNTPPeerRefTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerRefTime_Type.__name__ = "OctetString"
_HwNTPPeerRefTime_Object = MibTableColumn
hwNTPPeerRefTime = _HwNTPPeerRefTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 17),
    _HwNTPPeerRefTime_Type()
)
hwNTPPeerRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRefTime.setStatus("current")


class _HwNTPPeerOrg_Type(OctetString):
    """Custom type hwNTPPeerOrg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerOrg_Type.__name__ = "OctetString"
_HwNTPPeerOrg_Object = MibTableColumn
hwNTPPeerOrg = _HwNTPPeerOrg_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 18),
    _HwNTPPeerOrg_Type()
)
hwNTPPeerOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerOrg.setStatus("current")


class _HwNTPPeerRec_Type(OctetString):
    """Custom type hwNTPPeerRec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerRec_Type.__name__ = "OctetString"
_HwNTPPeerRec_Object = MibTableColumn
hwNTPPeerRec = _HwNTPPeerRec_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 19),
    _HwNTPPeerRec_Type()
)
hwNTPPeerRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerRec.setStatus("current")


class _HwNTPPeerXmt_Type(OctetString):
    """Custom type hwNTPPeerXmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerXmt_Type.__name__ = "OctetString"
_HwNTPPeerXmt_Object = MibTableColumn
hwNTPPeerXmt = _HwNTPPeerXmt_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 20),
    _HwNTPPeerXmt_Type()
)
hwNTPPeerXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerXmt.setStatus("current")


class _HwNTPPeerReach_Type(Integer32):
    """Custom type hwNTPPeerReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwNTPPeerReach_Type.__name__ = "Integer32"
_HwNTPPeerReach_Object = MibTableColumn
hwNTPPeerReach = _HwNTPPeerReach_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 21),
    _HwNTPPeerReach_Type()
)
hwNTPPeerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerReach.setStatus("current")


class _HwNTPPeerValid_Type(Integer32):
    """Custom type hwNTPPeerValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwNTPPeerValid_Type.__name__ = "Integer32"
_HwNTPPeerValid_Object = MibTableColumn
hwNTPPeerValid = _HwNTPPeerValid_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 22),
    _HwNTPPeerValid_Type()
)
hwNTPPeerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerValid.setStatus("current")


class _HwNTPPeerTimer_Type(Integer32):
    """Custom type hwNTPPeerTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwNTPPeerTimer_Type.__name__ = "Integer32"
_HwNTPPeerTimer_Object = MibTableColumn
hwNTPPeerTimer = _HwNTPPeerTimer_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 23),
    _HwNTPPeerTimer_Type()
)
hwNTPPeerTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerTimer.setStatus("current")


class _HwNTPPeerDelay_Type(OctetString):
    """Custom type hwNTPPeerDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerDelay_Type.__name__ = "OctetString"
_HwNTPPeerDelay_Object = MibTableColumn
hwNTPPeerDelay = _HwNTPPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 24),
    _HwNTPPeerDelay_Type()
)
hwNTPPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerDelay.setStatus("current")


class _HwNTPPeerOffset_Type(OctetString):
    """Custom type hwNTPPeerOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerOffset_Type.__name__ = "OctetString"
_HwNTPPeerOffset_Object = MibTableColumn
hwNTPPeerOffset = _HwNTPPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 25),
    _HwNTPPeerOffset_Type()
)
hwNTPPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerOffset.setStatus("current")


class _HwNTPPeerJitter_Type(OctetString):
    """Custom type hwNTPPeerJitter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerJitter_Type.__name__ = "OctetString"
_HwNTPPeerJitter_Object = MibTableColumn
hwNTPPeerJitter = _HwNTPPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 26),
    _HwNTPPeerJitter_Type()
)
hwNTPPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerJitter.setStatus("current")


class _HwNTPPeerDispersion_Type(OctetString):
    """Custom type hwNTPPeerDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerDispersion_Type.__name__ = "OctetString"
_HwNTPPeerDispersion_Object = MibTableColumn
hwNTPPeerDispersion = _HwNTPPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 27),
    _HwNTPPeerDispersion_Type()
)
hwNTPPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerDispersion.setStatus("current")


class _HwNTPPeerKeyId_Type(Unsigned32):
    """Custom type hwNTPPeerKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HwNTPPeerKeyId_Type.__name__ = "Unsigned32"
_HwNTPPeerKeyId_Object = MibTableColumn
hwNTPPeerKeyId = _HwNTPPeerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 28),
    _HwNTPPeerKeyId_Type()
)
hwNTPPeerKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerKeyId.setStatus("current")


class _HwNTPPeerFiltDelay_Type(OctetString):
    """Custom type hwNTPPeerFiltDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerFiltDelay_Type.__name__ = "OctetString"
_HwNTPPeerFiltDelay_Object = MibTableColumn
hwNTPPeerFiltDelay = _HwNTPPeerFiltDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 29),
    _HwNTPPeerFiltDelay_Type()
)
hwNTPPeerFiltDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerFiltDelay.setStatus("current")


class _HwNTPPeerFiltOffset_Type(OctetString):
    """Custom type hwNTPPeerFiltOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerFiltOffset_Type.__name__ = "OctetString"
_HwNTPPeerFiltOffset_Object = MibTableColumn
hwNTPPeerFiltOffset = _HwNTPPeerFiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 30),
    _HwNTPPeerFiltOffset_Type()
)
hwNTPPeerFiltOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerFiltOffset.setStatus("current")


class _HwNTPPeerFiltError_Type(OctetString):
    """Custom type hwNTPPeerFiltError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HwNTPPeerFiltError_Type.__name__ = "OctetString"
_HwNTPPeerFiltError_Object = MibTableColumn
hwNTPPeerFiltError = _HwNTPPeerFiltError_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 31),
    _HwNTPPeerFiltError_Type()
)
hwNTPPeerFiltError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerFiltError.setStatus("current")


class _HwNTPPeerPMode_Type(Integer32):
    """Custom type hwNTPPeerPMode based on Integer32"""
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
        *(("broadcast", 5),
          ("broadcastclient", 8),
          ("client", 3),
          ("multicastclient", 9),
          ("reservedControl", 6),
          ("reservedPrivate", 7),
          ("server", 4),
          ("symmetricActive", 1),
          ("symmetricPassive", 2),
          ("unspecified", 0))
    )


_HwNTPPeerPMode_Type.__name__ = "Integer32"
_HwNTPPeerPMode_Object = MibTableColumn
hwNTPPeerPMode = _HwNTPPeerPMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 32),
    _HwNTPPeerPMode_Type()
)
hwNTPPeerPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerPMode.setStatus("current")
_HwNTPPeerReceived_Type = Counter32
_HwNTPPeerReceived_Object = MibTableColumn
hwNTPPeerReceived = _HwNTPPeerReceived_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 33),
    _HwNTPPeerReceived_Type()
)
hwNTPPeerReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerReceived.setStatus("current")
_HwNTPPeerSent_Type = Counter32
_HwNTPPeerSent_Object = MibTableColumn
hwNTPPeerSent = _HwNTPPeerSent_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 34),
    _HwNTPPeerSent_Type()
)
hwNTPPeerSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerSent.setStatus("current")


class _HwNTPPeerFlash_Type(Bits):
    """Custom type hwNTPPeerFlash based on Bits"""
    namedValues = NamedValues(
        *(("dispBeyond", 3),
          ("noAuthen", 8),
          ("recvRepeatMsg", 0),
          ("recvremanMsg", 1),
          ("refuOperate", 9),
          ("rootDispBeyond", 7),
          ("straBeyond", 6),
          ("unSynClock", 5),
          ("unSynMsg", 2),
          ("unauthenticate", 4))
    )

_HwNTPPeerFlash_Type.__name__ = "Bits"
_HwNTPPeerFlash_Object = MibTableColumn
hwNTPPeerFlash = _HwNTPPeerFlash_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 35),
    _HwNTPPeerFlash_Type()
)
hwNTPPeerFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNTPPeerFlash.setStatus("current")
_HwNTPPeerRowStatus_Type = RowStatus
_HwNTPPeerRowStatus_Object = MibTableColumn
hwNTPPeerRowStatus = _HwNTPPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 5, 25, 22, 2, 1, 1, 1, 36),
    _HwNTPPeerRowStatus_Type()
)
hwNTPPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwNTPPeerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-NTP-MIB",
    **{"hwNTP": hwNTP,
       "hwNTPSystemMIB": hwNTPSystemMIB,
       "hwNTPSystemMIBObjects": hwNTPSystemMIBObjects,
       "hwNTPSysLeap": hwNTPSysLeap,
       "hwNTPSysStratum": hwNTPSysStratum,
       "hwNTPSysPrecision": hwNTPSysPrecision,
       "hwNTPSysRootdelay": hwNTPSysRootdelay,
       "hwNTPSysRootdispersion": hwNTPSysRootdispersion,
       "hwNTPSysRefid": hwNTPSysRefid,
       "hwNTPSysReftime": hwNTPSysReftime,
       "hwNTPSysPoll": hwNTPSysPoll,
       "hwNTPSysPeer": hwNTPSysPeer,
       "hwNTPSysState": hwNTPSysState,
       "hwNTPSysOffset": hwNTPSysOffset,
       "hwNTPSysDrift": hwNTPSysDrift,
       "hwNTPSysCompliance": hwNTPSysCompliance,
       "hwNTPSysClock": hwNTPSysClock,
       "hwNTPSysStabil": hwNTPSysStabil,
       "hwNTPSysAuthenticate": hwNTPSysAuthenticate,
       "hwNTPSysPollSec": hwNTPSysPollSec,
       "hwNTPSysClockSec": hwNTPSysClockSec,
       "hwNTPServerIP": hwNTPServerIP,
       "hwNTPPeerMIB": hwNTPPeerMIB,
       "hwNTPPeerMIBObjects": hwNTPPeerMIBObjects,
       "hwNTPPeerTable": hwNTPPeerTable,
       "hwNTPPeerEntry": hwNTPPeerEntry,
       "hwNTPPeerConfig": hwNTPPeerConfig,
       "hwNTPPeerAuthenable": hwNTPPeerAuthenable,
       "hwNTPPeerAuthentic": hwNTPPeerAuthentic,
       "hwNTPPeerRemAdr": hwNTPPeerRemAdr,
       "hwNTPPeerRemPort": hwNTPPeerRemPort,
       "hwNTPPeerLocAdr": hwNTPPeerLocAdr,
       "hwNTPPeerLocPort": hwNTPPeerLocPort,
       "hwNTPPeerLeap": hwNTPPeerLeap,
       "hwNTPPeerHMode": hwNTPPeerHMode,
       "hwNTPPeerStratum": hwNTPPeerStratum,
       "hwNTPPeerPPoll": hwNTPPeerPPoll,
       "hwNTPPeerHPoll": hwNTPPeerHPoll,
       "hwNTPPeerPrecision": hwNTPPeerPrecision,
       "hwNTPPeerRootDelay": hwNTPPeerRootDelay,
       "hwNTPPeerRootDispersion": hwNTPPeerRootDispersion,
       "hwNTPPeerRefId": hwNTPPeerRefId,
       "hwNTPPeerRefTime": hwNTPPeerRefTime,
       "hwNTPPeerOrg": hwNTPPeerOrg,
       "hwNTPPeerRec": hwNTPPeerRec,
       "hwNTPPeerXmt": hwNTPPeerXmt,
       "hwNTPPeerReach": hwNTPPeerReach,
       "hwNTPPeerValid": hwNTPPeerValid,
       "hwNTPPeerTimer": hwNTPPeerTimer,
       "hwNTPPeerDelay": hwNTPPeerDelay,
       "hwNTPPeerOffset": hwNTPPeerOffset,
       "hwNTPPeerJitter": hwNTPPeerJitter,
       "hwNTPPeerDispersion": hwNTPPeerDispersion,
       "hwNTPPeerKeyId": hwNTPPeerKeyId,
       "hwNTPPeerFiltDelay": hwNTPPeerFiltDelay,
       "hwNTPPeerFiltOffset": hwNTPPeerFiltOffset,
       "hwNTPPeerFiltError": hwNTPPeerFiltError,
       "hwNTPPeerPMode": hwNTPPeerPMode,
       "hwNTPPeerReceived": hwNTPPeerReceived,
       "hwNTPPeerSent": hwNTPPeerSent,
       "hwNTPPeerFlash": hwNTPPeerFlash,
       "hwNTPPeerRowStatus": hwNTPPeerRowStatus}
)
