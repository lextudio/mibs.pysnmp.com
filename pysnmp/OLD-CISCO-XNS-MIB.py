# SNMP MIB module (OLD-CISCO-XNS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-XNS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:08 2024
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

_Tmpxns_ObjectIdentity = ObjectIdentity
tmpxns = _Tmpxns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 2)
)
_XnsInput_Type = Integer32
_XnsInput_Object = MibScalar
xnsInput = _XnsInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 1),
    _XnsInput_Type()
)
xnsInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsInput.setStatus("mandatory")
_XnsLocal_Type = Integer32
_XnsLocal_Object = MibScalar
xnsLocal = _XnsLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 2),
    _XnsLocal_Type()
)
xnsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsLocal.setStatus("mandatory")
_XnsBcastin_Type = Integer32
_XnsBcastin_Object = MibScalar
xnsBcastin = _XnsBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 3),
    _XnsBcastin_Type()
)
xnsBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsBcastin.setStatus("mandatory")
_XnsForward_Type = Integer32
_XnsForward_Object = MibScalar
xnsForward = _XnsForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 4),
    _XnsForward_Type()
)
xnsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsForward.setStatus("mandatory")
_XnsBcastout_Type = Integer32
_XnsBcastout_Object = MibScalar
xnsBcastout = _XnsBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 5),
    _XnsBcastout_Type()
)
xnsBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsBcastout.setStatus("mandatory")
_XnsErrin_Type = Integer32
_XnsErrin_Object = MibScalar
xnsErrin = _XnsErrin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 6),
    _XnsErrin_Type()
)
xnsErrin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsErrin.setStatus("mandatory")
_XnsErrout_Type = Integer32
_XnsErrout_Object = MibScalar
xnsErrout = _XnsErrout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 7),
    _XnsErrout_Type()
)
xnsErrout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsErrout.setStatus("mandatory")
_XnsFormerr_Type = Integer32
_XnsFormerr_Object = MibScalar
xnsFormerr = _XnsFormerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 8),
    _XnsFormerr_Type()
)
xnsFormerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsFormerr.setStatus("mandatory")
_XnsChksum_Type = Integer32
_XnsChksum_Object = MibScalar
xnsChksum = _XnsChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 9),
    _XnsChksum_Type()
)
xnsChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsChksum.setStatus("mandatory")
_XnsNotgate_Type = Integer32
_XnsNotgate_Object = MibScalar
xnsNotgate = _XnsNotgate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 10),
    _XnsNotgate_Type()
)
xnsNotgate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNotgate.setStatus("mandatory")
_XnsHopcnt_Type = Integer32
_XnsHopcnt_Object = MibScalar
xnsHopcnt = _XnsHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 11),
    _XnsHopcnt_Type()
)
xnsHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsHopcnt.setStatus("mandatory")
_XnsNoroute_Type = Integer32
_XnsNoroute_Object = MibScalar
xnsNoroute = _XnsNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 12),
    _XnsNoroute_Type()
)
xnsNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNoroute.setStatus("mandatory")
_XnsNoencap_Type = Integer32
_XnsNoencap_Object = MibScalar
xnsNoencap = _XnsNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 13),
    _XnsNoencap_Type()
)
xnsNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNoencap.setStatus("mandatory")
_XnsOutput_Type = Integer32
_XnsOutput_Object = MibScalar
xnsOutput = _XnsOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 14),
    _XnsOutput_Type()
)
xnsOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsOutput.setStatus("mandatory")
_XnsInmult_Type = Integer32
_XnsInmult_Object = MibScalar
xnsInmult = _XnsInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 15),
    _XnsInmult_Type()
)
xnsInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsInmult.setStatus("mandatory")
_XnsUnknown_Type = Integer32
_XnsUnknown_Object = MibScalar
xnsUnknown = _XnsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 16),
    _XnsUnknown_Type()
)
xnsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsUnknown.setStatus("mandatory")
_XnsFwdbrd_Type = Integer32
_XnsFwdbrd_Object = MibScalar
xnsFwdbrd = _XnsFwdbrd_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 17),
    _XnsFwdbrd_Type()
)
xnsFwdbrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsFwdbrd.setStatus("mandatory")
_XnsEchoreqin_Type = Integer32
_XnsEchoreqin_Object = MibScalar
xnsEchoreqin = _XnsEchoreqin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 18),
    _XnsEchoreqin_Type()
)
xnsEchoreqin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchoreqin.setStatus("mandatory")
_XnsEchoreqout_Type = Integer32
_XnsEchoreqout_Object = MibScalar
xnsEchoreqout = _XnsEchoreqout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 19),
    _XnsEchoreqout_Type()
)
xnsEchoreqout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchoreqout.setStatus("mandatory")
_XnsEchorepin_Type = Integer32
_XnsEchorepin_Object = MibScalar
xnsEchorepin = _XnsEchorepin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 20),
    _XnsEchorepin_Type()
)
xnsEchorepin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchorepin.setStatus("mandatory")
_XnsEchorepout_Type = Integer32
_XnsEchorepout_Object = MibScalar
xnsEchorepout = _XnsEchorepout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 21),
    _XnsEchorepout_Type()
)
xnsEchorepout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchorepout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-XNS-MIB",
    **{"tmpxns": tmpxns,
       "xnsInput": xnsInput,
       "xnsLocal": xnsLocal,
       "xnsBcastin": xnsBcastin,
       "xnsForward": xnsForward,
       "xnsBcastout": xnsBcastout,
       "xnsErrin": xnsErrin,
       "xnsErrout": xnsErrout,
       "xnsFormerr": xnsFormerr,
       "xnsChksum": xnsChksum,
       "xnsNotgate": xnsNotgate,
       "xnsHopcnt": xnsHopcnt,
       "xnsNoroute": xnsNoroute,
       "xnsNoencap": xnsNoencap,
       "xnsOutput": xnsOutput,
       "xnsInmult": xnsInmult,
       "xnsUnknown": xnsUnknown,
       "xnsFwdbrd": xnsFwdbrd,
       "xnsEchoreqin": xnsEchoreqin,
       "xnsEchoreqout": xnsEchoreqout,
       "xnsEchorepin": xnsEchorepin,
       "xnsEchorepout": xnsEchorepout}
)
