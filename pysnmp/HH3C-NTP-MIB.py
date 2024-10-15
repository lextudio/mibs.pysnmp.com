# SNMP MIB module (HH3C-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:23 2024
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

(hh3cRhw,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cRhw")

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

hh3cNTP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22)
)
hh3cNTP.setRevisions(
        ("2003-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cNTPSystemMIB_ObjectIdentity = ObjectIdentity
hh3cNTPSystemMIB = _Hh3cNTPSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1)
)
_Hh3cNTPSystemMIBObjects_ObjectIdentity = ObjectIdentity
hh3cNTPSystemMIBObjects = _Hh3cNTPSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1)
)


class _Hh3cNTPSysLeap_Type(Integer32):
    """Custom type hh3cNTPSysLeap based on Integer32"""
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


_Hh3cNTPSysLeap_Type.__name__ = "Integer32"
_Hh3cNTPSysLeap_Object = MibScalar
hh3cNTPSysLeap = _Hh3cNTPSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 1),
    _Hh3cNTPSysLeap_Type()
)
hh3cNTPSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysLeap.setStatus("current")


class _Hh3cNTPSysStratum_Type(Integer32):
    """Custom type hh3cNTPSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Hh3cNTPSysStratum_Type.__name__ = "Integer32"
_Hh3cNTPSysStratum_Object = MibScalar
hh3cNTPSysStratum = _Hh3cNTPSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 2),
    _Hh3cNTPSysStratum_Type()
)
hh3cNTPSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysStratum.setStatus("current")


class _Hh3cNTPSysPrecision_Type(Integer32):
    """Custom type hh3cNTPSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Hh3cNTPSysPrecision_Type.__name__ = "Integer32"
_Hh3cNTPSysPrecision_Object = MibScalar
hh3cNTPSysPrecision = _Hh3cNTPSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 3),
    _Hh3cNTPSysPrecision_Type()
)
hh3cNTPSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysPrecision.setStatus("current")


class _Hh3cNTPSysRootdelay_Type(OctetString):
    """Custom type hh3cNTPSysRootdelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysRootdelay_Type.__name__ = "OctetString"
_Hh3cNTPSysRootdelay_Object = MibScalar
hh3cNTPSysRootdelay = _Hh3cNTPSysRootdelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 4),
    _Hh3cNTPSysRootdelay_Type()
)
hh3cNTPSysRootdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysRootdelay.setStatus("current")


class _Hh3cNTPSysRootdispersion_Type(OctetString):
    """Custom type hh3cNTPSysRootdispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysRootdispersion_Type.__name__ = "OctetString"
_Hh3cNTPSysRootdispersion_Object = MibScalar
hh3cNTPSysRootdispersion = _Hh3cNTPSysRootdispersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 5),
    _Hh3cNTPSysRootdispersion_Type()
)
hh3cNTPSysRootdispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysRootdispersion.setStatus("current")


class _Hh3cNTPSysRefid_Type(OctetString):
    """Custom type hh3cNTPSysRefid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysRefid_Type.__name__ = "OctetString"
_Hh3cNTPSysRefid_Object = MibScalar
hh3cNTPSysRefid = _Hh3cNTPSysRefid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 6),
    _Hh3cNTPSysRefid_Type()
)
hh3cNTPSysRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysRefid.setStatus("current")


class _Hh3cNTPSysReftime_Type(OctetString):
    """Custom type hh3cNTPSysReftime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysReftime_Type.__name__ = "OctetString"
_Hh3cNTPSysReftime_Object = MibScalar
hh3cNTPSysReftime = _Hh3cNTPSysReftime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 7),
    _Hh3cNTPSysReftime_Type()
)
hh3cNTPSysReftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysReftime.setStatus("current")


class _Hh3cNTPSysPoll_Type(Integer32):
    """Custom type hh3cNTPSysPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Hh3cNTPSysPoll_Type.__name__ = "Integer32"
_Hh3cNTPSysPoll_Object = MibScalar
hh3cNTPSysPoll = _Hh3cNTPSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 8),
    _Hh3cNTPSysPoll_Type()
)
hh3cNTPSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysPoll.setStatus("current")


class _Hh3cNTPSysPeer_Type(Integer32):
    """Custom type hh3cNTPSysPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cNTPSysPeer_Type.__name__ = "Integer32"
_Hh3cNTPSysPeer_Object = MibScalar
hh3cNTPSysPeer = _Hh3cNTPSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 9),
    _Hh3cNTPSysPeer_Type()
)
hh3cNTPSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysPeer.setStatus("current")


class _Hh3cNTPSysState_Type(Integer32):
    """Custom type hh3cNTPSysState based on Integer32"""
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


_Hh3cNTPSysState_Type.__name__ = "Integer32"
_Hh3cNTPSysState_Object = MibScalar
hh3cNTPSysState = _Hh3cNTPSysState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 10),
    _Hh3cNTPSysState_Type()
)
hh3cNTPSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysState.setStatus("current")


class _Hh3cNTPSysOffset_Type(OctetString):
    """Custom type hh3cNTPSysOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysOffset_Type.__name__ = "OctetString"
_Hh3cNTPSysOffset_Object = MibScalar
hh3cNTPSysOffset = _Hh3cNTPSysOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 11),
    _Hh3cNTPSysOffset_Type()
)
hh3cNTPSysOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysOffset.setStatus("current")


class _Hh3cNTPSysDrift_Type(OctetString):
    """Custom type hh3cNTPSysDrift based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysDrift_Type.__name__ = "OctetString"
_Hh3cNTPSysDrift_Object = MibScalar
hh3cNTPSysDrift = _Hh3cNTPSysDrift_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 12),
    _Hh3cNTPSysDrift_Type()
)
hh3cNTPSysDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysDrift.setStatus("current")


class _Hh3cNTPSysCompliance_Type(OctetString):
    """Custom type hh3cNTPSysCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysCompliance_Type.__name__ = "OctetString"
_Hh3cNTPSysCompliance_Object = MibScalar
hh3cNTPSysCompliance = _Hh3cNTPSysCompliance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 13),
    _Hh3cNTPSysCompliance_Type()
)
hh3cNTPSysCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysCompliance.setStatus("current")


class _Hh3cNTPSysClock_Type(OctetString):
    """Custom type hh3cNTPSysClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysClock_Type.__name__ = "OctetString"
_Hh3cNTPSysClock_Object = MibScalar
hh3cNTPSysClock = _Hh3cNTPSysClock_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 14),
    _Hh3cNTPSysClock_Type()
)
hh3cNTPSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysClock.setStatus("current")


class _Hh3cNTPSysStabil_Type(OctetString):
    """Custom type hh3cNTPSysStabil based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPSysStabil_Type.__name__ = "OctetString"
_Hh3cNTPSysStabil_Object = MibScalar
hh3cNTPSysStabil = _Hh3cNTPSysStabil_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 15),
    _Hh3cNTPSysStabil_Type()
)
hh3cNTPSysStabil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysStabil.setStatus("current")


class _Hh3cNTPSysAuthenticate_Type(Integer32):
    """Custom type hh3cNTPSysAuthenticate based on Integer32"""
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


_Hh3cNTPSysAuthenticate_Type.__name__ = "Integer32"
_Hh3cNTPSysAuthenticate_Object = MibScalar
hh3cNTPSysAuthenticate = _Hh3cNTPSysAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 16),
    _Hh3cNTPSysAuthenticate_Type()
)
hh3cNTPSysAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNTPSysAuthenticate.setStatus("current")


class _Hh3cNTPSysPollSec_Type(Integer32):
    """Custom type hh3cNTPSysPollSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1048576),
    )


_Hh3cNTPSysPollSec_Type.__name__ = "Integer32"
_Hh3cNTPSysPollSec_Object = MibScalar
hh3cNTPSysPollSec = _Hh3cNTPSysPollSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 17),
    _Hh3cNTPSysPollSec_Type()
)
hh3cNTPSysPollSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNTPSysPollSec.setStatus("current")
_Hh3cNTPSysClockSec_Type = Integer32
_Hh3cNTPSysClockSec_Object = MibScalar
hh3cNTPSysClockSec = _Hh3cNTPSysClockSec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 18),
    _Hh3cNTPSysClockSec_Type()
)
hh3cNTPSysClockSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPSysClockSec.setStatus("current")
_Hh3cNTPServerIP_Type = IpAddress
_Hh3cNTPServerIP_Object = MibScalar
hh3cNTPServerIP = _Hh3cNTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 1, 1, 19),
    _Hh3cNTPServerIP_Type()
)
hh3cNTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cNTPServerIP.setStatus("current")
_Hh3cNTPPeerMIB_ObjectIdentity = ObjectIdentity
hh3cNTPPeerMIB = _Hh3cNTPPeerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2)
)
_Hh3cNTPPeerMIBObjects_ObjectIdentity = ObjectIdentity
hh3cNTPPeerMIBObjects = _Hh3cNTPPeerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1)
)
_Hh3cNTPPeerTable_Object = MibTable
hh3cNTPPeerTable = _Hh3cNTPPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cNTPPeerTable.setStatus("current")
_Hh3cNTPPeerEntry_Object = MibTableRow
hh3cNTPPeerEntry = _Hh3cNTPPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1)
)
hh3cNTPPeerEntry.setIndexNames(
    (0, "HH3C-NTP-MIB", "hh3cNTPPeerRemAdr"),
    (0, "HH3C-NTP-MIB", "hh3cNTPPeerHMode"),
)
if mibBuilder.loadTexts:
    hh3cNTPPeerEntry.setStatus("current")
_Hh3cNTPPeerConfig_Type = TruthValue
_Hh3cNTPPeerConfig_Object = MibTableColumn
hh3cNTPPeerConfig = _Hh3cNTPPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 1),
    _Hh3cNTPPeerConfig_Type()
)
hh3cNTPPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerConfig.setStatus("current")
_Hh3cNTPPeerAuthenable_Type = TruthValue
_Hh3cNTPPeerAuthenable_Object = MibTableColumn
hh3cNTPPeerAuthenable = _Hh3cNTPPeerAuthenable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 2),
    _Hh3cNTPPeerAuthenable_Type()
)
hh3cNTPPeerAuthenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerAuthenable.setStatus("current")
_Hh3cNTPPeerAuthentic_Type = TruthValue
_Hh3cNTPPeerAuthentic_Object = MibTableColumn
hh3cNTPPeerAuthentic = _Hh3cNTPPeerAuthentic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 3),
    _Hh3cNTPPeerAuthentic_Type()
)
hh3cNTPPeerAuthentic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerAuthentic.setStatus("current")
_Hh3cNTPPeerRemAdr_Type = IpAddress
_Hh3cNTPPeerRemAdr_Object = MibTableColumn
hh3cNTPPeerRemAdr = _Hh3cNTPPeerRemAdr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 4),
    _Hh3cNTPPeerRemAdr_Type()
)
hh3cNTPPeerRemAdr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNTPPeerRemAdr.setStatus("current")


class _Hh3cNTPPeerRemPort_Type(Integer32):
    """Custom type hh3cNTPPeerRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cNTPPeerRemPort_Type.__name__ = "Integer32"
_Hh3cNTPPeerRemPort_Object = MibTableColumn
hh3cNTPPeerRemPort = _Hh3cNTPPeerRemPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 5),
    _Hh3cNTPPeerRemPort_Type()
)
hh3cNTPPeerRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRemPort.setStatus("current")
_Hh3cNTPPeerLocAdr_Type = IpAddress
_Hh3cNTPPeerLocAdr_Object = MibTableColumn
hh3cNTPPeerLocAdr = _Hh3cNTPPeerLocAdr_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 6),
    _Hh3cNTPPeerLocAdr_Type()
)
hh3cNTPPeerLocAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerLocAdr.setStatus("current")


class _Hh3cNTPPeerLocPort_Type(Integer32):
    """Custom type hh3cNTPPeerLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cNTPPeerLocPort_Type.__name__ = "Integer32"
_Hh3cNTPPeerLocPort_Object = MibTableColumn
hh3cNTPPeerLocPort = _Hh3cNTPPeerLocPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 7),
    _Hh3cNTPPeerLocPort_Type()
)
hh3cNTPPeerLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerLocPort.setStatus("current")


class _Hh3cNTPPeerLeap_Type(Integer32):
    """Custom type hh3cNTPPeerLeap based on Integer32"""
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


_Hh3cNTPPeerLeap_Type.__name__ = "Integer32"
_Hh3cNTPPeerLeap_Object = MibTableColumn
hh3cNTPPeerLeap = _Hh3cNTPPeerLeap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 8),
    _Hh3cNTPPeerLeap_Type()
)
hh3cNTPPeerLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerLeap.setStatus("current")


class _Hh3cNTPPeerHMode_Type(Integer32):
    """Custom type hh3cNTPPeerHMode based on Integer32"""
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


_Hh3cNTPPeerHMode_Type.__name__ = "Integer32"
_Hh3cNTPPeerHMode_Object = MibTableColumn
hh3cNTPPeerHMode = _Hh3cNTPPeerHMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 9),
    _Hh3cNTPPeerHMode_Type()
)
hh3cNTPPeerHMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cNTPPeerHMode.setStatus("current")


class _Hh3cNTPPeerStratum_Type(Integer32):
    """Custom type hh3cNTPPeerStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cNTPPeerStratum_Type.__name__ = "Integer32"
_Hh3cNTPPeerStratum_Object = MibTableColumn
hh3cNTPPeerStratum = _Hh3cNTPPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 10),
    _Hh3cNTPPeerStratum_Type()
)
hh3cNTPPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerStratum.setStatus("current")


class _Hh3cNTPPeerPPoll_Type(Integer32):
    """Custom type hh3cNTPPeerPPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Hh3cNTPPeerPPoll_Type.__name__ = "Integer32"
_Hh3cNTPPeerPPoll_Object = MibTableColumn
hh3cNTPPeerPPoll = _Hh3cNTPPeerPPoll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 11),
    _Hh3cNTPPeerPPoll_Type()
)
hh3cNTPPeerPPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerPPoll.setStatus("current")


class _Hh3cNTPPeerHPoll_Type(Integer32):
    """Custom type hh3cNTPPeerHPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Hh3cNTPPeerHPoll_Type.__name__ = "Integer32"
_Hh3cNTPPeerHPoll_Object = MibTableColumn
hh3cNTPPeerHPoll = _Hh3cNTPPeerHPoll_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 12),
    _Hh3cNTPPeerHPoll_Type()
)
hh3cNTPPeerHPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerHPoll.setStatus("current")


class _Hh3cNTPPeerPrecision_Type(Integer32):
    """Custom type hh3cNTPPeerPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_Hh3cNTPPeerPrecision_Type.__name__ = "Integer32"
_Hh3cNTPPeerPrecision_Object = MibTableColumn
hh3cNTPPeerPrecision = _Hh3cNTPPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 13),
    _Hh3cNTPPeerPrecision_Type()
)
hh3cNTPPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerPrecision.setStatus("current")


class _Hh3cNTPPeerRootDelay_Type(OctetString):
    """Custom type hh3cNTPPeerRootDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerRootDelay_Type.__name__ = "OctetString"
_Hh3cNTPPeerRootDelay_Object = MibTableColumn
hh3cNTPPeerRootDelay = _Hh3cNTPPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 14),
    _Hh3cNTPPeerRootDelay_Type()
)
hh3cNTPPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRootDelay.setStatus("current")


class _Hh3cNTPPeerRootDispersion_Type(OctetString):
    """Custom type hh3cNTPPeerRootDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerRootDispersion_Type.__name__ = "OctetString"
_Hh3cNTPPeerRootDispersion_Object = MibTableColumn
hh3cNTPPeerRootDispersion = _Hh3cNTPPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 15),
    _Hh3cNTPPeerRootDispersion_Type()
)
hh3cNTPPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRootDispersion.setStatus("current")


class _Hh3cNTPPeerRefId_Type(OctetString):
    """Custom type hh3cNTPPeerRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerRefId_Type.__name__ = "OctetString"
_Hh3cNTPPeerRefId_Object = MibTableColumn
hh3cNTPPeerRefId = _Hh3cNTPPeerRefId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 16),
    _Hh3cNTPPeerRefId_Type()
)
hh3cNTPPeerRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRefId.setStatus("current")


class _Hh3cNTPPeerRefTime_Type(OctetString):
    """Custom type hh3cNTPPeerRefTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerRefTime_Type.__name__ = "OctetString"
_Hh3cNTPPeerRefTime_Object = MibTableColumn
hh3cNTPPeerRefTime = _Hh3cNTPPeerRefTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 17),
    _Hh3cNTPPeerRefTime_Type()
)
hh3cNTPPeerRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRefTime.setStatus("current")


class _Hh3cNTPPeerOrg_Type(OctetString):
    """Custom type hh3cNTPPeerOrg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerOrg_Type.__name__ = "OctetString"
_Hh3cNTPPeerOrg_Object = MibTableColumn
hh3cNTPPeerOrg = _Hh3cNTPPeerOrg_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 18),
    _Hh3cNTPPeerOrg_Type()
)
hh3cNTPPeerOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerOrg.setStatus("current")


class _Hh3cNTPPeerRec_Type(OctetString):
    """Custom type hh3cNTPPeerRec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerRec_Type.__name__ = "OctetString"
_Hh3cNTPPeerRec_Object = MibTableColumn
hh3cNTPPeerRec = _Hh3cNTPPeerRec_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 19),
    _Hh3cNTPPeerRec_Type()
)
hh3cNTPPeerRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerRec.setStatus("current")


class _Hh3cNTPPeerXmt_Type(OctetString):
    """Custom type hh3cNTPPeerXmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerXmt_Type.__name__ = "OctetString"
_Hh3cNTPPeerXmt_Object = MibTableColumn
hh3cNTPPeerXmt = _Hh3cNTPPeerXmt_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 20),
    _Hh3cNTPPeerXmt_Type()
)
hh3cNTPPeerXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerXmt.setStatus("current")


class _Hh3cNTPPeerReach_Type(Integer32):
    """Custom type hh3cNTPPeerReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cNTPPeerReach_Type.__name__ = "Integer32"
_Hh3cNTPPeerReach_Object = MibTableColumn
hh3cNTPPeerReach = _Hh3cNTPPeerReach_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 21),
    _Hh3cNTPPeerReach_Type()
)
hh3cNTPPeerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerReach.setStatus("current")


class _Hh3cNTPPeerValid_Type(Integer32):
    """Custom type hh3cNTPPeerValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cNTPPeerValid_Type.__name__ = "Integer32"
_Hh3cNTPPeerValid_Object = MibTableColumn
hh3cNTPPeerValid = _Hh3cNTPPeerValid_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 22),
    _Hh3cNTPPeerValid_Type()
)
hh3cNTPPeerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerValid.setStatus("current")


class _Hh3cNTPPeerTimer_Type(Integer32):
    """Custom type hh3cNTPPeerTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Hh3cNTPPeerTimer_Type.__name__ = "Integer32"
_Hh3cNTPPeerTimer_Object = MibTableColumn
hh3cNTPPeerTimer = _Hh3cNTPPeerTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 23),
    _Hh3cNTPPeerTimer_Type()
)
hh3cNTPPeerTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerTimer.setStatus("current")


class _Hh3cNTPPeerDelay_Type(OctetString):
    """Custom type hh3cNTPPeerDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerDelay_Type.__name__ = "OctetString"
_Hh3cNTPPeerDelay_Object = MibTableColumn
hh3cNTPPeerDelay = _Hh3cNTPPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 24),
    _Hh3cNTPPeerDelay_Type()
)
hh3cNTPPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerDelay.setStatus("current")


class _Hh3cNTPPeerOffset_Type(OctetString):
    """Custom type hh3cNTPPeerOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerOffset_Type.__name__ = "OctetString"
_Hh3cNTPPeerOffset_Object = MibTableColumn
hh3cNTPPeerOffset = _Hh3cNTPPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 25),
    _Hh3cNTPPeerOffset_Type()
)
hh3cNTPPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerOffset.setStatus("current")


class _Hh3cNTPPeerJitter_Type(OctetString):
    """Custom type hh3cNTPPeerJitter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerJitter_Type.__name__ = "OctetString"
_Hh3cNTPPeerJitter_Object = MibTableColumn
hh3cNTPPeerJitter = _Hh3cNTPPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 26),
    _Hh3cNTPPeerJitter_Type()
)
hh3cNTPPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerJitter.setStatus("current")


class _Hh3cNTPPeerDispersion_Type(OctetString):
    """Custom type hh3cNTPPeerDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerDispersion_Type.__name__ = "OctetString"
_Hh3cNTPPeerDispersion_Object = MibTableColumn
hh3cNTPPeerDispersion = _Hh3cNTPPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 27),
    _Hh3cNTPPeerDispersion_Type()
)
hh3cNTPPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerDispersion.setStatus("current")


class _Hh3cNTPPeerKeyId_Type(Unsigned32):
    """Custom type hh3cNTPPeerKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_Hh3cNTPPeerKeyId_Type.__name__ = "Unsigned32"
_Hh3cNTPPeerKeyId_Object = MibTableColumn
hh3cNTPPeerKeyId = _Hh3cNTPPeerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 28),
    _Hh3cNTPPeerKeyId_Type()
)
hh3cNTPPeerKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerKeyId.setStatus("current")


class _Hh3cNTPPeerFiltDelay_Type(OctetString):
    """Custom type hh3cNTPPeerFiltDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerFiltDelay_Type.__name__ = "OctetString"
_Hh3cNTPPeerFiltDelay_Object = MibTableColumn
hh3cNTPPeerFiltDelay = _Hh3cNTPPeerFiltDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 29),
    _Hh3cNTPPeerFiltDelay_Type()
)
hh3cNTPPeerFiltDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerFiltDelay.setStatus("current")


class _Hh3cNTPPeerFiltOffset_Type(OctetString):
    """Custom type hh3cNTPPeerFiltOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerFiltOffset_Type.__name__ = "OctetString"
_Hh3cNTPPeerFiltOffset_Object = MibTableColumn
hh3cNTPPeerFiltOffset = _Hh3cNTPPeerFiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 30),
    _Hh3cNTPPeerFiltOffset_Type()
)
hh3cNTPPeerFiltOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerFiltOffset.setStatus("current")


class _Hh3cNTPPeerFiltError_Type(OctetString):
    """Custom type hh3cNTPPeerFiltError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_Hh3cNTPPeerFiltError_Type.__name__ = "OctetString"
_Hh3cNTPPeerFiltError_Object = MibTableColumn
hh3cNTPPeerFiltError = _Hh3cNTPPeerFiltError_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 31),
    _Hh3cNTPPeerFiltError_Type()
)
hh3cNTPPeerFiltError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerFiltError.setStatus("current")


class _Hh3cNTPPeerPMode_Type(Integer32):
    """Custom type hh3cNTPPeerPMode based on Integer32"""
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


_Hh3cNTPPeerPMode_Type.__name__ = "Integer32"
_Hh3cNTPPeerPMode_Object = MibTableColumn
hh3cNTPPeerPMode = _Hh3cNTPPeerPMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 32),
    _Hh3cNTPPeerPMode_Type()
)
hh3cNTPPeerPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerPMode.setStatus("current")
_Hh3cNTPPeerReceived_Type = Counter32
_Hh3cNTPPeerReceived_Object = MibTableColumn
hh3cNTPPeerReceived = _Hh3cNTPPeerReceived_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 33),
    _Hh3cNTPPeerReceived_Type()
)
hh3cNTPPeerReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerReceived.setStatus("current")
_Hh3cNTPPeerSent_Type = Counter32
_Hh3cNTPPeerSent_Object = MibTableColumn
hh3cNTPPeerSent = _Hh3cNTPPeerSent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 34),
    _Hh3cNTPPeerSent_Type()
)
hh3cNTPPeerSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerSent.setStatus("current")


class _Hh3cNTPPeerFlash_Type(Bits):
    """Custom type hh3cNTPPeerFlash based on Bits"""
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

_Hh3cNTPPeerFlash_Type.__name__ = "Bits"
_Hh3cNTPPeerFlash_Object = MibTableColumn
hh3cNTPPeerFlash = _Hh3cNTPPeerFlash_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 35),
    _Hh3cNTPPeerFlash_Type()
)
hh3cNTPPeerFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cNTPPeerFlash.setStatus("current")
_Hh3cNTPPeerRowStatus_Type = RowStatus
_Hh3cNTPPeerRowStatus_Object = MibTableColumn
hh3cNTPPeerRowStatus = _Hh3cNTPPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 22, 2, 1, 1, 1, 36),
    _Hh3cNTPPeerRowStatus_Type()
)
hh3cNTPPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cNTPPeerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-NTP-MIB",
    **{"hh3cNTP": hh3cNTP,
       "hh3cNTPSystemMIB": hh3cNTPSystemMIB,
       "hh3cNTPSystemMIBObjects": hh3cNTPSystemMIBObjects,
       "hh3cNTPSysLeap": hh3cNTPSysLeap,
       "hh3cNTPSysStratum": hh3cNTPSysStratum,
       "hh3cNTPSysPrecision": hh3cNTPSysPrecision,
       "hh3cNTPSysRootdelay": hh3cNTPSysRootdelay,
       "hh3cNTPSysRootdispersion": hh3cNTPSysRootdispersion,
       "hh3cNTPSysRefid": hh3cNTPSysRefid,
       "hh3cNTPSysReftime": hh3cNTPSysReftime,
       "hh3cNTPSysPoll": hh3cNTPSysPoll,
       "hh3cNTPSysPeer": hh3cNTPSysPeer,
       "hh3cNTPSysState": hh3cNTPSysState,
       "hh3cNTPSysOffset": hh3cNTPSysOffset,
       "hh3cNTPSysDrift": hh3cNTPSysDrift,
       "hh3cNTPSysCompliance": hh3cNTPSysCompliance,
       "hh3cNTPSysClock": hh3cNTPSysClock,
       "hh3cNTPSysStabil": hh3cNTPSysStabil,
       "hh3cNTPSysAuthenticate": hh3cNTPSysAuthenticate,
       "hh3cNTPSysPollSec": hh3cNTPSysPollSec,
       "hh3cNTPSysClockSec": hh3cNTPSysClockSec,
       "hh3cNTPServerIP": hh3cNTPServerIP,
       "hh3cNTPPeerMIB": hh3cNTPPeerMIB,
       "hh3cNTPPeerMIBObjects": hh3cNTPPeerMIBObjects,
       "hh3cNTPPeerTable": hh3cNTPPeerTable,
       "hh3cNTPPeerEntry": hh3cNTPPeerEntry,
       "hh3cNTPPeerConfig": hh3cNTPPeerConfig,
       "hh3cNTPPeerAuthenable": hh3cNTPPeerAuthenable,
       "hh3cNTPPeerAuthentic": hh3cNTPPeerAuthentic,
       "hh3cNTPPeerRemAdr": hh3cNTPPeerRemAdr,
       "hh3cNTPPeerRemPort": hh3cNTPPeerRemPort,
       "hh3cNTPPeerLocAdr": hh3cNTPPeerLocAdr,
       "hh3cNTPPeerLocPort": hh3cNTPPeerLocPort,
       "hh3cNTPPeerLeap": hh3cNTPPeerLeap,
       "hh3cNTPPeerHMode": hh3cNTPPeerHMode,
       "hh3cNTPPeerStratum": hh3cNTPPeerStratum,
       "hh3cNTPPeerPPoll": hh3cNTPPeerPPoll,
       "hh3cNTPPeerHPoll": hh3cNTPPeerHPoll,
       "hh3cNTPPeerPrecision": hh3cNTPPeerPrecision,
       "hh3cNTPPeerRootDelay": hh3cNTPPeerRootDelay,
       "hh3cNTPPeerRootDispersion": hh3cNTPPeerRootDispersion,
       "hh3cNTPPeerRefId": hh3cNTPPeerRefId,
       "hh3cNTPPeerRefTime": hh3cNTPPeerRefTime,
       "hh3cNTPPeerOrg": hh3cNTPPeerOrg,
       "hh3cNTPPeerRec": hh3cNTPPeerRec,
       "hh3cNTPPeerXmt": hh3cNTPPeerXmt,
       "hh3cNTPPeerReach": hh3cNTPPeerReach,
       "hh3cNTPPeerValid": hh3cNTPPeerValid,
       "hh3cNTPPeerTimer": hh3cNTPPeerTimer,
       "hh3cNTPPeerDelay": hh3cNTPPeerDelay,
       "hh3cNTPPeerOffset": hh3cNTPPeerOffset,
       "hh3cNTPPeerJitter": hh3cNTPPeerJitter,
       "hh3cNTPPeerDispersion": hh3cNTPPeerDispersion,
       "hh3cNTPPeerKeyId": hh3cNTPPeerKeyId,
       "hh3cNTPPeerFiltDelay": hh3cNTPPeerFiltDelay,
       "hh3cNTPPeerFiltOffset": hh3cNTPPeerFiltOffset,
       "hh3cNTPPeerFiltError": hh3cNTPPeerFiltError,
       "hh3cNTPPeerPMode": hh3cNTPPeerPMode,
       "hh3cNTPPeerReceived": hh3cNTPPeerReceived,
       "hh3cNTPPeerSent": hh3cNTPPeerSent,
       "hh3cNTPPeerFlash": hh3cNTPPeerFlash,
       "hh3cNTPPeerRowStatus": hh3cNTPPeerRowStatus}
)
