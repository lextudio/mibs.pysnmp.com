# SNMP MIB module (NETSWITCH-DMA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSWITCH-DMA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:13 2024
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Icf_ObjectIdentity = ObjectIdentity
icf = _Icf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14)
)
_HpicfObjects_ObjectIdentity = ObjectIdentity
hpicfObjects = _HpicfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11)
)
_HpicfSwitch_ObjectIdentity = ObjectIdentity
hpicfSwitch = _HpicfSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5)
)
_HpSwitch_ObjectIdentity = ObjectIdentity
hpSwitch = _HpSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1)
)
_HpOpSystem_ObjectIdentity = ObjectIdentity
hpOpSystem = _HpOpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 1)
)
_HpHwSystem_ObjectIdentity = ObjectIdentity
hpHwSystem = _HpHwSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2)
)
_HpDMAStats_ObjectIdentity = ObjectIdentity
hpDMAStats = _HpDMAStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2)
)


class _HpDMAReset_Type(Integer32):
    """Custom type hpDMAReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_HpDMAReset_Type.__name__ = "Integer32"
_HpDMAReset_Object = MibScalar
hpDMAReset = _HpDMAReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 1),
    _HpDMAReset_Type()
)
hpDMAReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpDMAReset.setStatus("mandatory")
_HpDMAFrameRcvcnt_Type = Counter32
_HpDMAFrameRcvcnt_Object = MibScalar
hpDMAFrameRcvcnt = _HpDMAFrameRcvcnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 2),
    _HpDMAFrameRcvcnt_Type()
)
hpDMAFrameRcvcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameRcvcnt.setStatus("mandatory")
_HpDMAOctetsRcvcnt_Type = Counter32
_HpDMAOctetsRcvcnt_Object = MibScalar
hpDMAOctetsRcvcnt = _HpDMAOctetsRcvcnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 3),
    _HpDMAOctetsRcvcnt_Type()
)
hpDMAOctetsRcvcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAOctetsRcvcnt.setStatus("mandatory")
_HpDMAPrevRcvFrames_Type = Counter32
_HpDMAPrevRcvFrames_Object = MibScalar
hpDMAPrevRcvFrames = _HpDMAPrevRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 4),
    _HpDMAPrevRcvFrames_Type()
)
hpDMAPrevRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPrevRcvFrames.setStatus("mandatory")
_HpDMAFrameRcvPerSec_Type = Counter32
_HpDMAFrameRcvPerSec_Object = MibScalar
hpDMAFrameRcvPerSec = _HpDMAFrameRcvPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 5),
    _HpDMAFrameRcvPerSec_Type()
)
hpDMAFrameRcvPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameRcvPerSec.setStatus("mandatory")
_HpDMAPeakRcvFrames_Type = Counter32
_HpDMAPeakRcvFrames_Object = MibScalar
hpDMAPeakRcvFrames = _HpDMAPeakRcvFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 6),
    _HpDMAPeakRcvFrames_Type()
)
hpDMAPeakRcvFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPeakRcvFrames.setStatus("mandatory")
_HpDMAPrevRcvOctets_Type = Counter32
_HpDMAPrevRcvOctets_Object = MibScalar
hpDMAPrevRcvOctets = _HpDMAPrevRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 7),
    _HpDMAPrevRcvOctets_Type()
)
hpDMAPrevRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPrevRcvOctets.setStatus("mandatory")
_HpDMAOctetsRcvPerSec_Type = Counter32
_HpDMAOctetsRcvPerSec_Object = MibScalar
hpDMAOctetsRcvPerSec = _HpDMAOctetsRcvPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 8),
    _HpDMAOctetsRcvPerSec_Type()
)
hpDMAOctetsRcvPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAOctetsRcvPerSec.setStatus("mandatory")
_HpDMAPeakRcvOctets_Type = Counter32
_HpDMAPeakRcvOctets_Object = MibScalar
hpDMAPeakRcvOctets = _HpDMAPeakRcvOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 9),
    _HpDMAPeakRcvOctets_Type()
)
hpDMAPeakRcvOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPeakRcvOctets.setStatus("mandatory")
_HpDMAFrameXmtcnt_Type = Counter32
_HpDMAFrameXmtcnt_Object = MibScalar
hpDMAFrameXmtcnt = _HpDMAFrameXmtcnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 10),
    _HpDMAFrameXmtcnt_Type()
)
hpDMAFrameXmtcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameXmtcnt.setStatus("mandatory")
_HpDMAOctetsXmtcnt_Type = Counter32
_HpDMAOctetsXmtcnt_Object = MibScalar
hpDMAOctetsXmtcnt = _HpDMAOctetsXmtcnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 11),
    _HpDMAOctetsXmtcnt_Type()
)
hpDMAOctetsXmtcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAOctetsXmtcnt.setStatus("mandatory")
_HpDMAPrevXmtFrames_Type = Counter32
_HpDMAPrevXmtFrames_Object = MibScalar
hpDMAPrevXmtFrames = _HpDMAPrevXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 12),
    _HpDMAPrevXmtFrames_Type()
)
hpDMAPrevXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPrevXmtFrames.setStatus("mandatory")
_HpDMAFrameXmtPerSec_Type = Counter32
_HpDMAFrameXmtPerSec_Object = MibScalar
hpDMAFrameXmtPerSec = _HpDMAFrameXmtPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 13),
    _HpDMAFrameXmtPerSec_Type()
)
hpDMAFrameXmtPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameXmtPerSec.setStatus("mandatory")
_HpDMAPeakXmtFrames_Type = Counter32
_HpDMAPeakXmtFrames_Object = MibScalar
hpDMAPeakXmtFrames = _HpDMAPeakXmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 14),
    _HpDMAPeakXmtFrames_Type()
)
hpDMAPeakXmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPeakXmtFrames.setStatus("mandatory")
_HpDMAPrevXmtOctets_Type = Counter32
_HpDMAPrevXmtOctets_Object = MibScalar
hpDMAPrevXmtOctets = _HpDMAPrevXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 15),
    _HpDMAPrevXmtOctets_Type()
)
hpDMAPrevXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPrevXmtOctets.setStatus("mandatory")
_HpDMAOctetsXmtPerSec_Type = Counter32
_HpDMAOctetsXmtPerSec_Object = MibScalar
hpDMAOctetsXmtPerSec = _HpDMAOctetsXmtPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 16),
    _HpDMAOctetsXmtPerSec_Type()
)
hpDMAOctetsXmtPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAOctetsXmtPerSec.setStatus("mandatory")
_HpDMAPeakXmtOctets_Type = Counter32
_HpDMAPeakXmtOctets_Object = MibScalar
hpDMAPeakXmtOctets = _HpDMAPeakXmtOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 17),
    _HpDMAPeakXmtOctets_Type()
)
hpDMAPeakXmtOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAPeakXmtOctets.setStatus("mandatory")
_HpDMAFrameClippedcnt_Type = Counter32
_HpDMAFrameClippedcnt_Object = MibScalar
hpDMAFrameClippedcnt = _HpDMAFrameClippedcnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 18),
    _HpDMAFrameClippedcnt_Type()
)
hpDMAFrameClippedcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameClippedcnt.setStatus("mandatory")
_HpDMAFrameClippedOccurance_Type = Counter32
_HpDMAFrameClippedOccurance_Object = MibScalar
hpDMAFrameClippedOccurance = _HpDMAFrameClippedOccurance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 19),
    _HpDMAFrameClippedOccurance_Type()
)
hpDMAFrameClippedOccurance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAFrameClippedOccurance.setStatus("mandatory")
_HpDMAMissBufCnt_Type = Counter32
_HpDMAMissBufCnt_Object = MibScalar
hpDMAMissBufCnt = _HpDMAMissBufCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 2, 2, 20),
    _HpDMAMissBufCnt_Type()
)
hpDMAMissBufCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpDMAMissBufCnt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSWITCH-DMA-MIB",
    **{"hp": hp,
       "nm": nm,
       "icf": icf,
       "hpicfObjects": hpicfObjects,
       "hpicfSwitch": hpicfSwitch,
       "hpSwitch": hpSwitch,
       "hpOpSystem": hpOpSystem,
       "hpHwSystem": hpHwSystem,
       "hpDMAStats": hpDMAStats,
       "hpDMAReset": hpDMAReset,
       "hpDMAFrameRcvcnt": hpDMAFrameRcvcnt,
       "hpDMAOctetsRcvcnt": hpDMAOctetsRcvcnt,
       "hpDMAPrevRcvFrames": hpDMAPrevRcvFrames,
       "hpDMAFrameRcvPerSec": hpDMAFrameRcvPerSec,
       "hpDMAPeakRcvFrames": hpDMAPeakRcvFrames,
       "hpDMAPrevRcvOctets": hpDMAPrevRcvOctets,
       "hpDMAOctetsRcvPerSec": hpDMAOctetsRcvPerSec,
       "hpDMAPeakRcvOctets": hpDMAPeakRcvOctets,
       "hpDMAFrameXmtcnt": hpDMAFrameXmtcnt,
       "hpDMAOctetsXmtcnt": hpDMAOctetsXmtcnt,
       "hpDMAPrevXmtFrames": hpDMAPrevXmtFrames,
       "hpDMAFrameXmtPerSec": hpDMAFrameXmtPerSec,
       "hpDMAPeakXmtFrames": hpDMAPeakXmtFrames,
       "hpDMAPrevXmtOctets": hpDMAPrevXmtOctets,
       "hpDMAOctetsXmtPerSec": hpDMAOctetsXmtPerSec,
       "hpDMAPeakXmtOctets": hpDMAPeakXmtOctets,
       "hpDMAFrameClippedcnt": hpDMAFrameClippedcnt,
       "hpDMAFrameClippedOccurance": hpDMAFrameClippedOccurance,
       "hpDMAMissBufCnt": hpDMAMissBufCnt}
)
