# SNMP MIB module (HPN-ICF-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-NTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:22 2024
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

(hpnicfRhw,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfRhw")

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

hpnicfNTP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22)
)
hpnicfNTP.setRevisions(
        ("2003-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfNTPSystemMIB_ObjectIdentity = ObjectIdentity
hpnicfNTPSystemMIB = _HpnicfNTPSystemMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1)
)
_HpnicfNTPSystemMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfNTPSystemMIBObjects = _HpnicfNTPSystemMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1)
)


class _HpnicfNTPSysLeap_Type(Integer32):
    """Custom type hpnicfNTPSysLeap based on Integer32"""
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


_HpnicfNTPSysLeap_Type.__name__ = "Integer32"
_HpnicfNTPSysLeap_Object = MibScalar
hpnicfNTPSysLeap = _HpnicfNTPSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 1),
    _HpnicfNTPSysLeap_Type()
)
hpnicfNTPSysLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysLeap.setStatus("current")


class _HpnicfNTPSysStratum_Type(Integer32):
    """Custom type hpnicfNTPSysStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpnicfNTPSysStratum_Type.__name__ = "Integer32"
_HpnicfNTPSysStratum_Object = MibScalar
hpnicfNTPSysStratum = _HpnicfNTPSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 2),
    _HpnicfNTPSysStratum_Type()
)
hpnicfNTPSysStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysStratum.setStatus("current")


class _HpnicfNTPSysPrecision_Type(Integer32):
    """Custom type hpnicfNTPSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HpnicfNTPSysPrecision_Type.__name__ = "Integer32"
_HpnicfNTPSysPrecision_Object = MibScalar
hpnicfNTPSysPrecision = _HpnicfNTPSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 3),
    _HpnicfNTPSysPrecision_Type()
)
hpnicfNTPSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysPrecision.setStatus("current")


class _HpnicfNTPSysRootdelay_Type(OctetString):
    """Custom type hpnicfNTPSysRootdelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysRootdelay_Type.__name__ = "OctetString"
_HpnicfNTPSysRootdelay_Object = MibScalar
hpnicfNTPSysRootdelay = _HpnicfNTPSysRootdelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 4),
    _HpnicfNTPSysRootdelay_Type()
)
hpnicfNTPSysRootdelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysRootdelay.setStatus("current")


class _HpnicfNTPSysRootdispersion_Type(OctetString):
    """Custom type hpnicfNTPSysRootdispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysRootdispersion_Type.__name__ = "OctetString"
_HpnicfNTPSysRootdispersion_Object = MibScalar
hpnicfNTPSysRootdispersion = _HpnicfNTPSysRootdispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 5),
    _HpnicfNTPSysRootdispersion_Type()
)
hpnicfNTPSysRootdispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysRootdispersion.setStatus("current")


class _HpnicfNTPSysRefid_Type(OctetString):
    """Custom type hpnicfNTPSysRefid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysRefid_Type.__name__ = "OctetString"
_HpnicfNTPSysRefid_Object = MibScalar
hpnicfNTPSysRefid = _HpnicfNTPSysRefid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 6),
    _HpnicfNTPSysRefid_Type()
)
hpnicfNTPSysRefid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysRefid.setStatus("current")


class _HpnicfNTPSysReftime_Type(OctetString):
    """Custom type hpnicfNTPSysReftime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysReftime_Type.__name__ = "OctetString"
_HpnicfNTPSysReftime_Object = MibScalar
hpnicfNTPSysReftime = _HpnicfNTPSysReftime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 7),
    _HpnicfNTPSysReftime_Type()
)
hpnicfNTPSysReftime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysReftime.setStatus("current")


class _HpnicfNTPSysPoll_Type(Integer32):
    """Custom type hpnicfNTPSysPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HpnicfNTPSysPoll_Type.__name__ = "Integer32"
_HpnicfNTPSysPoll_Object = MibScalar
hpnicfNTPSysPoll = _HpnicfNTPSysPoll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 8),
    _HpnicfNTPSysPoll_Type()
)
hpnicfNTPSysPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysPoll.setStatus("current")


class _HpnicfNTPSysPeer_Type(Integer32):
    """Custom type hpnicfNTPSysPeer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfNTPSysPeer_Type.__name__ = "Integer32"
_HpnicfNTPSysPeer_Object = MibScalar
hpnicfNTPSysPeer = _HpnicfNTPSysPeer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 9),
    _HpnicfNTPSysPeer_Type()
)
hpnicfNTPSysPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysPeer.setStatus("obsolete")


class _HpnicfNTPSysState_Type(Integer32):
    """Custom type hpnicfNTPSysState based on Integer32"""
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


_HpnicfNTPSysState_Type.__name__ = "Integer32"
_HpnicfNTPSysState_Object = MibScalar
hpnicfNTPSysState = _HpnicfNTPSysState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 10),
    _HpnicfNTPSysState_Type()
)
hpnicfNTPSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysState.setStatus("current")


class _HpnicfNTPSysOffset_Type(OctetString):
    """Custom type hpnicfNTPSysOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysOffset_Type.__name__ = "OctetString"
_HpnicfNTPSysOffset_Object = MibScalar
hpnicfNTPSysOffset = _HpnicfNTPSysOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 11),
    _HpnicfNTPSysOffset_Type()
)
hpnicfNTPSysOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysOffset.setStatus("current")


class _HpnicfNTPSysDrift_Type(OctetString):
    """Custom type hpnicfNTPSysDrift based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysDrift_Type.__name__ = "OctetString"
_HpnicfNTPSysDrift_Object = MibScalar
hpnicfNTPSysDrift = _HpnicfNTPSysDrift_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 12),
    _HpnicfNTPSysDrift_Type()
)
hpnicfNTPSysDrift.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysDrift.setStatus("current")


class _HpnicfNTPSysCompliance_Type(OctetString):
    """Custom type hpnicfNTPSysCompliance based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysCompliance_Type.__name__ = "OctetString"
_HpnicfNTPSysCompliance_Object = MibScalar
hpnicfNTPSysCompliance = _HpnicfNTPSysCompliance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 13),
    _HpnicfNTPSysCompliance_Type()
)
hpnicfNTPSysCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysCompliance.setStatus("current")


class _HpnicfNTPSysClock_Type(OctetString):
    """Custom type hpnicfNTPSysClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysClock_Type.__name__ = "OctetString"
_HpnicfNTPSysClock_Object = MibScalar
hpnicfNTPSysClock = _HpnicfNTPSysClock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 14),
    _HpnicfNTPSysClock_Type()
)
hpnicfNTPSysClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysClock.setStatus("current")


class _HpnicfNTPSysStabil_Type(OctetString):
    """Custom type hpnicfNTPSysStabil based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPSysStabil_Type.__name__ = "OctetString"
_HpnicfNTPSysStabil_Object = MibScalar
hpnicfNTPSysStabil = _HpnicfNTPSysStabil_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 15),
    _HpnicfNTPSysStabil_Type()
)
hpnicfNTPSysStabil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysStabil.setStatus("current")


class _HpnicfNTPSysAuthenticate_Type(Integer32):
    """Custom type hpnicfNTPSysAuthenticate based on Integer32"""
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


_HpnicfNTPSysAuthenticate_Type.__name__ = "Integer32"
_HpnicfNTPSysAuthenticate_Object = MibScalar
hpnicfNTPSysAuthenticate = _HpnicfNTPSysAuthenticate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 16),
    _HpnicfNTPSysAuthenticate_Type()
)
hpnicfNTPSysAuthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNTPSysAuthenticate.setStatus("current")


class _HpnicfNTPSysPollSec_Type(Integer32):
    """Custom type hpnicfNTPSysPollSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1048576),
    )


_HpnicfNTPSysPollSec_Type.__name__ = "Integer32"
_HpnicfNTPSysPollSec_Object = MibScalar
hpnicfNTPSysPollSec = _HpnicfNTPSysPollSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 17),
    _HpnicfNTPSysPollSec_Type()
)
hpnicfNTPSysPollSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNTPSysPollSec.setStatus("current")
_HpnicfNTPSysClockSec_Type = Integer32
_HpnicfNTPSysClockSec_Object = MibScalar
hpnicfNTPSysClockSec = _HpnicfNTPSysClockSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 18),
    _HpnicfNTPSysClockSec_Type()
)
hpnicfNTPSysClockSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysClockSec.setStatus("current")
_HpnicfNTPServerIP_Type = IpAddress
_HpnicfNTPServerIP_Object = MibScalar
hpnicfNTPServerIP = _HpnicfNTPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 19),
    _HpnicfNTPServerIP_Type()
)
hpnicfNTPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfNTPServerIP.setStatus("current")


class _HpnicfNTPSysSrcPeer_Type(Unsigned32):
    """Custom type hpnicfNTPSysSrcPeer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfNTPSysSrcPeer_Type.__name__ = "Unsigned32"
_HpnicfNTPSysSrcPeer_Object = MibScalar
hpnicfNTPSysSrcPeer = _HpnicfNTPSysSrcPeer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 1, 1, 20),
    _HpnicfNTPSysSrcPeer_Type()
)
hpnicfNTPSysSrcPeer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPSysSrcPeer.setStatus("current")
_HpnicfNTPPeerMIB_ObjectIdentity = ObjectIdentity
hpnicfNTPPeerMIB = _HpnicfNTPPeerMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2)
)
_HpnicfNTPPeerMIBObjects_ObjectIdentity = ObjectIdentity
hpnicfNTPPeerMIBObjects = _HpnicfNTPPeerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1)
)
_HpnicfNTPPeerTable_Object = MibTable
hpnicfNTPPeerTable = _HpnicfNTPPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfNTPPeerTable.setStatus("current")
_HpnicfNTPPeerEntry_Object = MibTableRow
hpnicfNTPPeerEntry = _HpnicfNTPPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1)
)
hpnicfNTPPeerEntry.setIndexNames(
    (0, "HPN-ICF-NTP-MIB", "hpnicfNTPPeerRemAdr"),
    (0, "HPN-ICF-NTP-MIB", "hpnicfNTPPeerHMode"),
)
if mibBuilder.loadTexts:
    hpnicfNTPPeerEntry.setStatus("current")
_HpnicfNTPPeerConfig_Type = TruthValue
_HpnicfNTPPeerConfig_Object = MibTableColumn
hpnicfNTPPeerConfig = _HpnicfNTPPeerConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 1),
    _HpnicfNTPPeerConfig_Type()
)
hpnicfNTPPeerConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerConfig.setStatus("current")
_HpnicfNTPPeerAuthenable_Type = TruthValue
_HpnicfNTPPeerAuthenable_Object = MibTableColumn
hpnicfNTPPeerAuthenable = _HpnicfNTPPeerAuthenable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 2),
    _HpnicfNTPPeerAuthenable_Type()
)
hpnicfNTPPeerAuthenable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerAuthenable.setStatus("current")
_HpnicfNTPPeerAuthentic_Type = TruthValue
_HpnicfNTPPeerAuthentic_Object = MibTableColumn
hpnicfNTPPeerAuthentic = _HpnicfNTPPeerAuthentic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 3),
    _HpnicfNTPPeerAuthentic_Type()
)
hpnicfNTPPeerAuthentic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerAuthentic.setStatus("current")
_HpnicfNTPPeerRemAdr_Type = IpAddress
_HpnicfNTPPeerRemAdr_Object = MibTableColumn
hpnicfNTPPeerRemAdr = _HpnicfNTPPeerRemAdr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 4),
    _HpnicfNTPPeerRemAdr_Type()
)
hpnicfNTPPeerRemAdr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRemAdr.setStatus("current")


class _HpnicfNTPPeerRemPort_Type(Integer32):
    """Custom type hpnicfNTPPeerRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfNTPPeerRemPort_Type.__name__ = "Integer32"
_HpnicfNTPPeerRemPort_Object = MibTableColumn
hpnicfNTPPeerRemPort = _HpnicfNTPPeerRemPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 5),
    _HpnicfNTPPeerRemPort_Type()
)
hpnicfNTPPeerRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRemPort.setStatus("current")
_HpnicfNTPPeerLocAdr_Type = IpAddress
_HpnicfNTPPeerLocAdr_Object = MibTableColumn
hpnicfNTPPeerLocAdr = _HpnicfNTPPeerLocAdr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 6),
    _HpnicfNTPPeerLocAdr_Type()
)
hpnicfNTPPeerLocAdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerLocAdr.setStatus("current")


class _HpnicfNTPPeerLocPort_Type(Integer32):
    """Custom type hpnicfNTPPeerLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfNTPPeerLocPort_Type.__name__ = "Integer32"
_HpnicfNTPPeerLocPort_Object = MibTableColumn
hpnicfNTPPeerLocPort = _HpnicfNTPPeerLocPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 7),
    _HpnicfNTPPeerLocPort_Type()
)
hpnicfNTPPeerLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerLocPort.setStatus("current")


class _HpnicfNTPPeerLeap_Type(Integer32):
    """Custom type hpnicfNTPPeerLeap based on Integer32"""
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


_HpnicfNTPPeerLeap_Type.__name__ = "Integer32"
_HpnicfNTPPeerLeap_Object = MibTableColumn
hpnicfNTPPeerLeap = _HpnicfNTPPeerLeap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 8),
    _HpnicfNTPPeerLeap_Type()
)
hpnicfNTPPeerLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerLeap.setStatus("current")


class _HpnicfNTPPeerHMode_Type(Integer32):
    """Custom type hpnicfNTPPeerHMode based on Integer32"""
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


_HpnicfNTPPeerHMode_Type.__name__ = "Integer32"
_HpnicfNTPPeerHMode_Object = MibTableColumn
hpnicfNTPPeerHMode = _HpnicfNTPPeerHMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 9),
    _HpnicfNTPPeerHMode_Type()
)
hpnicfNTPPeerHMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfNTPPeerHMode.setStatus("current")


class _HpnicfNTPPeerStratum_Type(Integer32):
    """Custom type hpnicfNTPPeerStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfNTPPeerStratum_Type.__name__ = "Integer32"
_HpnicfNTPPeerStratum_Object = MibTableColumn
hpnicfNTPPeerStratum = _HpnicfNTPPeerStratum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 10),
    _HpnicfNTPPeerStratum_Type()
)
hpnicfNTPPeerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerStratum.setStatus("current")


class _HpnicfNTPPeerPPoll_Type(Integer32):
    """Custom type hpnicfNTPPeerPPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HpnicfNTPPeerPPoll_Type.__name__ = "Integer32"
_HpnicfNTPPeerPPoll_Object = MibTableColumn
hpnicfNTPPeerPPoll = _HpnicfNTPPeerPPoll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 11),
    _HpnicfNTPPeerPPoll_Type()
)
hpnicfNTPPeerPPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerPPoll.setStatus("current")


class _HpnicfNTPPeerHPoll_Type(Integer32):
    """Custom type hpnicfNTPPeerHPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HpnicfNTPPeerHPoll_Type.__name__ = "Integer32"
_HpnicfNTPPeerHPoll_Object = MibTableColumn
hpnicfNTPPeerHPoll = _HpnicfNTPPeerHPoll_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 12),
    _HpnicfNTPPeerHPoll_Type()
)
hpnicfNTPPeerHPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerHPoll.setStatus("current")


class _HpnicfNTPPeerPrecision_Type(Integer32):
    """Custom type hpnicfNTPPeerPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-20, 20),
    )


_HpnicfNTPPeerPrecision_Type.__name__ = "Integer32"
_HpnicfNTPPeerPrecision_Object = MibTableColumn
hpnicfNTPPeerPrecision = _HpnicfNTPPeerPrecision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 13),
    _HpnicfNTPPeerPrecision_Type()
)
hpnicfNTPPeerPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerPrecision.setStatus("current")


class _HpnicfNTPPeerRootDelay_Type(OctetString):
    """Custom type hpnicfNTPPeerRootDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerRootDelay_Type.__name__ = "OctetString"
_HpnicfNTPPeerRootDelay_Object = MibTableColumn
hpnicfNTPPeerRootDelay = _HpnicfNTPPeerRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 14),
    _HpnicfNTPPeerRootDelay_Type()
)
hpnicfNTPPeerRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRootDelay.setStatus("current")


class _HpnicfNTPPeerRootDispersion_Type(OctetString):
    """Custom type hpnicfNTPPeerRootDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerRootDispersion_Type.__name__ = "OctetString"
_HpnicfNTPPeerRootDispersion_Object = MibTableColumn
hpnicfNTPPeerRootDispersion = _HpnicfNTPPeerRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 15),
    _HpnicfNTPPeerRootDispersion_Type()
)
hpnicfNTPPeerRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRootDispersion.setStatus("current")


class _HpnicfNTPPeerRefId_Type(OctetString):
    """Custom type hpnicfNTPPeerRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerRefId_Type.__name__ = "OctetString"
_HpnicfNTPPeerRefId_Object = MibTableColumn
hpnicfNTPPeerRefId = _HpnicfNTPPeerRefId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 16),
    _HpnicfNTPPeerRefId_Type()
)
hpnicfNTPPeerRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRefId.setStatus("current")


class _HpnicfNTPPeerRefTime_Type(OctetString):
    """Custom type hpnicfNTPPeerRefTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerRefTime_Type.__name__ = "OctetString"
_HpnicfNTPPeerRefTime_Object = MibTableColumn
hpnicfNTPPeerRefTime = _HpnicfNTPPeerRefTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 17),
    _HpnicfNTPPeerRefTime_Type()
)
hpnicfNTPPeerRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRefTime.setStatus("current")


class _HpnicfNTPPeerOrg_Type(OctetString):
    """Custom type hpnicfNTPPeerOrg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerOrg_Type.__name__ = "OctetString"
_HpnicfNTPPeerOrg_Object = MibTableColumn
hpnicfNTPPeerOrg = _HpnicfNTPPeerOrg_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 18),
    _HpnicfNTPPeerOrg_Type()
)
hpnicfNTPPeerOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerOrg.setStatus("current")


class _HpnicfNTPPeerRec_Type(OctetString):
    """Custom type hpnicfNTPPeerRec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerRec_Type.__name__ = "OctetString"
_HpnicfNTPPeerRec_Object = MibTableColumn
hpnicfNTPPeerRec = _HpnicfNTPPeerRec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 19),
    _HpnicfNTPPeerRec_Type()
)
hpnicfNTPPeerRec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRec.setStatus("current")


class _HpnicfNTPPeerXmt_Type(OctetString):
    """Custom type hpnicfNTPPeerXmt based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerXmt_Type.__name__ = "OctetString"
_HpnicfNTPPeerXmt_Object = MibTableColumn
hpnicfNTPPeerXmt = _HpnicfNTPPeerXmt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 20),
    _HpnicfNTPPeerXmt_Type()
)
hpnicfNTPPeerXmt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerXmt.setStatus("current")


class _HpnicfNTPPeerReach_Type(Integer32):
    """Custom type hpnicfNTPPeerReach based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfNTPPeerReach_Type.__name__ = "Integer32"
_HpnicfNTPPeerReach_Object = MibTableColumn
hpnicfNTPPeerReach = _HpnicfNTPPeerReach_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 21),
    _HpnicfNTPPeerReach_Type()
)
hpnicfNTPPeerReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerReach.setStatus("current")


class _HpnicfNTPPeerValid_Type(Integer32):
    """Custom type hpnicfNTPPeerValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfNTPPeerValid_Type.__name__ = "Integer32"
_HpnicfNTPPeerValid_Object = MibTableColumn
hpnicfNTPPeerValid = _HpnicfNTPPeerValid_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 22),
    _HpnicfNTPPeerValid_Type()
)
hpnicfNTPPeerValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerValid.setStatus("current")


class _HpnicfNTPPeerTimer_Type(Integer32):
    """Custom type hpnicfNTPPeerTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HpnicfNTPPeerTimer_Type.__name__ = "Integer32"
_HpnicfNTPPeerTimer_Object = MibTableColumn
hpnicfNTPPeerTimer = _HpnicfNTPPeerTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 23),
    _HpnicfNTPPeerTimer_Type()
)
hpnicfNTPPeerTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerTimer.setStatus("current")


class _HpnicfNTPPeerDelay_Type(OctetString):
    """Custom type hpnicfNTPPeerDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerDelay_Type.__name__ = "OctetString"
_HpnicfNTPPeerDelay_Object = MibTableColumn
hpnicfNTPPeerDelay = _HpnicfNTPPeerDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 24),
    _HpnicfNTPPeerDelay_Type()
)
hpnicfNTPPeerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerDelay.setStatus("current")


class _HpnicfNTPPeerOffset_Type(OctetString):
    """Custom type hpnicfNTPPeerOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerOffset_Type.__name__ = "OctetString"
_HpnicfNTPPeerOffset_Object = MibTableColumn
hpnicfNTPPeerOffset = _HpnicfNTPPeerOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 25),
    _HpnicfNTPPeerOffset_Type()
)
hpnicfNTPPeerOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerOffset.setStatus("current")


class _HpnicfNTPPeerJitter_Type(OctetString):
    """Custom type hpnicfNTPPeerJitter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerJitter_Type.__name__ = "OctetString"
_HpnicfNTPPeerJitter_Object = MibTableColumn
hpnicfNTPPeerJitter = _HpnicfNTPPeerJitter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 26),
    _HpnicfNTPPeerJitter_Type()
)
hpnicfNTPPeerJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerJitter.setStatus("current")


class _HpnicfNTPPeerDispersion_Type(OctetString):
    """Custom type hpnicfNTPPeerDispersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerDispersion_Type.__name__ = "OctetString"
_HpnicfNTPPeerDispersion_Object = MibTableColumn
hpnicfNTPPeerDispersion = _HpnicfNTPPeerDispersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 27),
    _HpnicfNTPPeerDispersion_Type()
)
hpnicfNTPPeerDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerDispersion.setStatus("current")


class _HpnicfNTPPeerKeyId_Type(Unsigned32):
    """Custom type hpnicfNTPPeerKeyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_HpnicfNTPPeerKeyId_Type.__name__ = "Unsigned32"
_HpnicfNTPPeerKeyId_Object = MibTableColumn
hpnicfNTPPeerKeyId = _HpnicfNTPPeerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 28),
    _HpnicfNTPPeerKeyId_Type()
)
hpnicfNTPPeerKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerKeyId.setStatus("current")


class _HpnicfNTPPeerFiltDelay_Type(OctetString):
    """Custom type hpnicfNTPPeerFiltDelay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerFiltDelay_Type.__name__ = "OctetString"
_HpnicfNTPPeerFiltDelay_Object = MibTableColumn
hpnicfNTPPeerFiltDelay = _HpnicfNTPPeerFiltDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 29),
    _HpnicfNTPPeerFiltDelay_Type()
)
hpnicfNTPPeerFiltDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerFiltDelay.setStatus("current")


class _HpnicfNTPPeerFiltOffset_Type(OctetString):
    """Custom type hpnicfNTPPeerFiltOffset based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerFiltOffset_Type.__name__ = "OctetString"
_HpnicfNTPPeerFiltOffset_Object = MibTableColumn
hpnicfNTPPeerFiltOffset = _HpnicfNTPPeerFiltOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 30),
    _HpnicfNTPPeerFiltOffset_Type()
)
hpnicfNTPPeerFiltOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerFiltOffset.setStatus("current")


class _HpnicfNTPPeerFiltError_Type(OctetString):
    """Custom type hpnicfNTPPeerFiltError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpnicfNTPPeerFiltError_Type.__name__ = "OctetString"
_HpnicfNTPPeerFiltError_Object = MibTableColumn
hpnicfNTPPeerFiltError = _HpnicfNTPPeerFiltError_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 31),
    _HpnicfNTPPeerFiltError_Type()
)
hpnicfNTPPeerFiltError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerFiltError.setStatus("current")


class _HpnicfNTPPeerPMode_Type(Integer32):
    """Custom type hpnicfNTPPeerPMode based on Integer32"""
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


_HpnicfNTPPeerPMode_Type.__name__ = "Integer32"
_HpnicfNTPPeerPMode_Object = MibTableColumn
hpnicfNTPPeerPMode = _HpnicfNTPPeerPMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 32),
    _HpnicfNTPPeerPMode_Type()
)
hpnicfNTPPeerPMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerPMode.setStatus("current")
_HpnicfNTPPeerReceived_Type = Counter32
_HpnicfNTPPeerReceived_Object = MibTableColumn
hpnicfNTPPeerReceived = _HpnicfNTPPeerReceived_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 33),
    _HpnicfNTPPeerReceived_Type()
)
hpnicfNTPPeerReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerReceived.setStatus("current")
_HpnicfNTPPeerSent_Type = Counter32
_HpnicfNTPPeerSent_Object = MibTableColumn
hpnicfNTPPeerSent = _HpnicfNTPPeerSent_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 34),
    _HpnicfNTPPeerSent_Type()
)
hpnicfNTPPeerSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerSent.setStatus("current")


class _HpnicfNTPPeerFlash_Type(Bits):
    """Custom type hpnicfNTPPeerFlash based on Bits"""
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

_HpnicfNTPPeerFlash_Type.__name__ = "Bits"
_HpnicfNTPPeerFlash_Object = MibTableColumn
hpnicfNTPPeerFlash = _HpnicfNTPPeerFlash_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 35),
    _HpnicfNTPPeerFlash_Type()
)
hpnicfNTPPeerFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfNTPPeerFlash.setStatus("current")
_HpnicfNTPPeerRowStatus_Type = RowStatus
_HpnicfNTPPeerRowStatus_Object = MibTableColumn
hpnicfNTPPeerRowStatus = _HpnicfNTPPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 22, 2, 1, 1, 1, 36),
    _HpnicfNTPPeerRowStatus_Type()
)
hpnicfNTPPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfNTPPeerRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-NTP-MIB",
    **{"hpnicfNTP": hpnicfNTP,
       "hpnicfNTPSystemMIB": hpnicfNTPSystemMIB,
       "hpnicfNTPSystemMIBObjects": hpnicfNTPSystemMIBObjects,
       "hpnicfNTPSysLeap": hpnicfNTPSysLeap,
       "hpnicfNTPSysStratum": hpnicfNTPSysStratum,
       "hpnicfNTPSysPrecision": hpnicfNTPSysPrecision,
       "hpnicfNTPSysRootdelay": hpnicfNTPSysRootdelay,
       "hpnicfNTPSysRootdispersion": hpnicfNTPSysRootdispersion,
       "hpnicfNTPSysRefid": hpnicfNTPSysRefid,
       "hpnicfNTPSysReftime": hpnicfNTPSysReftime,
       "hpnicfNTPSysPoll": hpnicfNTPSysPoll,
       "hpnicfNTPSysPeer": hpnicfNTPSysPeer,
       "hpnicfNTPSysState": hpnicfNTPSysState,
       "hpnicfNTPSysOffset": hpnicfNTPSysOffset,
       "hpnicfNTPSysDrift": hpnicfNTPSysDrift,
       "hpnicfNTPSysCompliance": hpnicfNTPSysCompliance,
       "hpnicfNTPSysClock": hpnicfNTPSysClock,
       "hpnicfNTPSysStabil": hpnicfNTPSysStabil,
       "hpnicfNTPSysAuthenticate": hpnicfNTPSysAuthenticate,
       "hpnicfNTPSysPollSec": hpnicfNTPSysPollSec,
       "hpnicfNTPSysClockSec": hpnicfNTPSysClockSec,
       "hpnicfNTPServerIP": hpnicfNTPServerIP,
       "hpnicfNTPSysSrcPeer": hpnicfNTPSysSrcPeer,
       "hpnicfNTPPeerMIB": hpnicfNTPPeerMIB,
       "hpnicfNTPPeerMIBObjects": hpnicfNTPPeerMIBObjects,
       "hpnicfNTPPeerTable": hpnicfNTPPeerTable,
       "hpnicfNTPPeerEntry": hpnicfNTPPeerEntry,
       "hpnicfNTPPeerConfig": hpnicfNTPPeerConfig,
       "hpnicfNTPPeerAuthenable": hpnicfNTPPeerAuthenable,
       "hpnicfNTPPeerAuthentic": hpnicfNTPPeerAuthentic,
       "hpnicfNTPPeerRemAdr": hpnicfNTPPeerRemAdr,
       "hpnicfNTPPeerRemPort": hpnicfNTPPeerRemPort,
       "hpnicfNTPPeerLocAdr": hpnicfNTPPeerLocAdr,
       "hpnicfNTPPeerLocPort": hpnicfNTPPeerLocPort,
       "hpnicfNTPPeerLeap": hpnicfNTPPeerLeap,
       "hpnicfNTPPeerHMode": hpnicfNTPPeerHMode,
       "hpnicfNTPPeerStratum": hpnicfNTPPeerStratum,
       "hpnicfNTPPeerPPoll": hpnicfNTPPeerPPoll,
       "hpnicfNTPPeerHPoll": hpnicfNTPPeerHPoll,
       "hpnicfNTPPeerPrecision": hpnicfNTPPeerPrecision,
       "hpnicfNTPPeerRootDelay": hpnicfNTPPeerRootDelay,
       "hpnicfNTPPeerRootDispersion": hpnicfNTPPeerRootDispersion,
       "hpnicfNTPPeerRefId": hpnicfNTPPeerRefId,
       "hpnicfNTPPeerRefTime": hpnicfNTPPeerRefTime,
       "hpnicfNTPPeerOrg": hpnicfNTPPeerOrg,
       "hpnicfNTPPeerRec": hpnicfNTPPeerRec,
       "hpnicfNTPPeerXmt": hpnicfNTPPeerXmt,
       "hpnicfNTPPeerReach": hpnicfNTPPeerReach,
       "hpnicfNTPPeerValid": hpnicfNTPPeerValid,
       "hpnicfNTPPeerTimer": hpnicfNTPPeerTimer,
       "hpnicfNTPPeerDelay": hpnicfNTPPeerDelay,
       "hpnicfNTPPeerOffset": hpnicfNTPPeerOffset,
       "hpnicfNTPPeerJitter": hpnicfNTPPeerJitter,
       "hpnicfNTPPeerDispersion": hpnicfNTPPeerDispersion,
       "hpnicfNTPPeerKeyId": hpnicfNTPPeerKeyId,
       "hpnicfNTPPeerFiltDelay": hpnicfNTPPeerFiltDelay,
       "hpnicfNTPPeerFiltOffset": hpnicfNTPPeerFiltOffset,
       "hpnicfNTPPeerFiltError": hpnicfNTPPeerFiltError,
       "hpnicfNTPPeerPMode": hpnicfNTPPeerPMode,
       "hpnicfNTPPeerReceived": hpnicfNTPPeerReceived,
       "hpnicfNTPPeerSent": hpnicfNTPPeerSent,
       "hpnicfNTPPeerFlash": hpnicfNTPPeerFlash,
       "hpnicfNTPPeerRowStatus": hpnicfNTPPeerRowStatus}
)
