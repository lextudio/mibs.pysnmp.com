# SNMP MIB module (OLD-CISCO-APPLETALK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-APPLETALK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:56 2024
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

(temporary,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "temporary")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tmpappletalk_ObjectIdentity = ObjectIdentity
tmpappletalk = _Tmpappletalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 3)
)
_AtInput_Type = Integer32
_AtInput_Object = MibScalar
atInput = _AtInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 1),
    _AtInput_Type()
)
atInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atInput.setStatus("mandatory")
_AtLocal_Type = Integer32
_AtLocal_Object = MibScalar
atLocal = _AtLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 2),
    _AtLocal_Type()
)
atLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLocal.setStatus("mandatory")
_AtBcastin_Type = Integer32
_AtBcastin_Object = MibScalar
atBcastin = _AtBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 3),
    _AtBcastin_Type()
)
atBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBcastin.setStatus("mandatory")
_AtForward_Type = Integer32
_AtForward_Object = MibScalar
atForward = _AtForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 4),
    _AtForward_Type()
)
atForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atForward.setStatus("mandatory")
_AtBcastout_Type = Integer32
_AtBcastout_Object = MibScalar
atBcastout = _AtBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 5),
    _AtBcastout_Type()
)
atBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBcastout.setStatus("mandatory")
_AtChksum_Type = Integer32
_AtChksum_Object = MibScalar
atChksum = _AtChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 7),
    _AtChksum_Type()
)
atChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atChksum.setStatus("mandatory")
_AtNotgate_Type = Integer32
_AtNotgate_Object = MibScalar
atNotgate = _AtNotgate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 8),
    _AtNotgate_Type()
)
atNotgate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNotgate.setStatus("mandatory")
_AtHopcnt_Type = Integer32
_AtHopcnt_Object = MibScalar
atHopcnt = _AtHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 9),
    _AtHopcnt_Type()
)
atHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atHopcnt.setStatus("mandatory")
_AtNoaccess_Type = Integer32
_AtNoaccess_Object = MibScalar
atNoaccess = _AtNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 10),
    _AtNoaccess_Type()
)
atNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoaccess.setStatus("mandatory")
_AtNoroute_Type = Integer32
_AtNoroute_Object = MibScalar
atNoroute = _AtNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 11),
    _AtNoroute_Type()
)
atNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoroute.setStatus("mandatory")
_AtNoencap_Type = Integer32
_AtNoencap_Object = MibScalar
atNoencap = _AtNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 12),
    _AtNoencap_Type()
)
atNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoencap.setStatus("mandatory")
_AtOutput_Type = Integer32
_AtOutput_Object = MibScalar
atOutput = _AtOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 13),
    _AtOutput_Type()
)
atOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atOutput.setStatus("mandatory")
_AtInmult_Type = Integer32
_AtInmult_Object = MibScalar
atInmult = _AtInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 14),
    _AtInmult_Type()
)
atInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atInmult.setStatus("mandatory")
_AtRtmpin_Type = Integer32
_AtRtmpin_Object = MibScalar
atRtmpin = _AtRtmpin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 15),
    _AtRtmpin_Type()
)
atRtmpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtmpin.setStatus("mandatory")
_AtRtmpout_Type = Integer32
_AtRtmpout_Object = MibScalar
atRtmpout = _AtRtmpout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 16),
    _AtRtmpout_Type()
)
atRtmpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtmpout.setStatus("mandatory")
_AtNbpin_Type = Integer32
_AtNbpin_Object = MibScalar
atNbpin = _AtNbpin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 17),
    _AtNbpin_Type()
)
atNbpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNbpin.setStatus("mandatory")
_AtNbpout_Type = Integer32
_AtNbpout_Object = MibScalar
atNbpout = _AtNbpout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 18),
    _AtNbpout_Type()
)
atNbpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNbpout.setStatus("mandatory")
_AtAtp_Type = Integer32
_AtAtp_Object = MibScalar
atAtp = _AtAtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 19),
    _AtAtp_Type()
)
atAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtp.setStatus("mandatory")
_AtZipin_Type = Integer32
_AtZipin_Object = MibScalar
atZipin = _AtZipin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 20),
    _AtZipin_Type()
)
atZipin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atZipin.setStatus("mandatory")
_AtZipout_Type = Integer32
_AtZipout_Object = MibScalar
atZipout = _AtZipout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 21),
    _AtZipout_Type()
)
atZipout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atZipout.setStatus("mandatory")
_AtEcho_Type = Integer32
_AtEcho_Object = MibScalar
atEcho = _AtEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 22),
    _AtEcho_Type()
)
atEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEcho.setStatus("mandatory")
_AtEchoill_Type = Integer32
_AtEchoill_Object = MibScalar
atEchoill = _AtEchoill_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 23),
    _AtEchoill_Type()
)
atEchoill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEchoill.setStatus("mandatory")
_AtDdpshort_Type = Integer32
_AtDdpshort_Object = MibScalar
atDdpshort = _AtDdpshort_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 24),
    _AtDdpshort_Type()
)
atDdpshort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdpshort.setStatus("mandatory")
_AtDdplong_Type = Integer32
_AtDdplong_Object = MibScalar
atDdplong = _AtDdplong_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 25),
    _AtDdplong_Type()
)
atDdplong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdplong.setStatus("mandatory")
_AtDdpbad_Type = Integer32
_AtDdpbad_Object = MibScalar
atDdpbad = _AtDdpbad_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 26),
    _AtDdpbad_Type()
)
atDdpbad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdpbad.setStatus("mandatory")
_AtNobuffer_Type = Integer32
_AtNobuffer_Object = MibScalar
atNobuffer = _AtNobuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 27),
    _AtNobuffer_Type()
)
atNobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNobuffer.setStatus("mandatory")
_AtArpreq_Type = Integer32
_AtArpreq_Object = MibScalar
atArpreq = _AtArpreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 28),
    _AtArpreq_Type()
)
atArpreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpreq.setStatus("mandatory")
_AtArpreply_Type = Integer32
_AtArpreply_Object = MibScalar
atArpreply = _AtArpreply_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 29),
    _AtArpreply_Type()
)
atArpreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpreply.setStatus("mandatory")
_AtArpprobe_Type = Integer32
_AtArpprobe_Object = MibScalar
atArpprobe = _AtArpprobe_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 30),
    _AtArpprobe_Type()
)
atArpprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpprobe.setStatus("mandatory")
_AtUnknown_Type = Integer32
_AtUnknown_Object = MibScalar
atUnknown = _AtUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 31),
    _AtUnknown_Type()
)
atUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atUnknown.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-APPLETALK-MIB",
    **{"tmpappletalk": tmpappletalk,
       "atInput": atInput,
       "atLocal": atLocal,
       "atBcastin": atBcastin,
       "atForward": atForward,
       "atBcastout": atBcastout,
       "atChksum": atChksum,
       "atNotgate": atNotgate,
       "atHopcnt": atHopcnt,
       "atNoaccess": atNoaccess,
       "atNoroute": atNoroute,
       "atNoencap": atNoencap,
       "atOutput": atOutput,
       "atInmult": atInmult,
       "atRtmpin": atRtmpin,
       "atRtmpout": atRtmpout,
       "atNbpin": atNbpin,
       "atNbpout": atNbpout,
       "atAtp": atAtp,
       "atZipin": atZipin,
       "atZipout": atZipout,
       "atEcho": atEcho,
       "atEchoill": atEchoill,
       "atDdpshort": atDdpshort,
       "atDdplong": atDdplong,
       "atDdpbad": atDdpbad,
       "atNobuffer": atNobuffer,
       "atArpreq": atArpreq,
       "atArpreply": atArpreply,
       "atArpprobe": atArpprobe,
       "atUnknown": atUnknown}
)
