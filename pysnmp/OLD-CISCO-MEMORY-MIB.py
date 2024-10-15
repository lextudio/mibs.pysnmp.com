# SNMP MIB module (OLD-CISCO-MEMORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-MEMORY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:03 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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

_Lmem_ObjectIdentity = ObjectIdentity
lmem = _Lmem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 1)
)
_FreeMem_Type = Integer32
_FreeMem_Object = MibScalar
freeMem = _FreeMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 8),
    _FreeMem_Type()
)
freeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMem.setStatus("obsolete")
_BufferElFree_Type = Integer32
_BufferElFree_Object = MibScalar
bufferElFree = _BufferElFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 9),
    _BufferElFree_Type()
)
bufferElFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElFree.setStatus("mandatory")
_BufferElMax_Type = Integer32
_BufferElMax_Object = MibScalar
bufferElMax = _BufferElMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 10),
    _BufferElMax_Type()
)
bufferElMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElMax.setStatus("mandatory")
_BufferElHit_Type = Integer32
_BufferElHit_Object = MibScalar
bufferElHit = _BufferElHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 11),
    _BufferElHit_Type()
)
bufferElHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElHit.setStatus("mandatory")
_BufferElMiss_Type = Integer32
_BufferElMiss_Object = MibScalar
bufferElMiss = _BufferElMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 12),
    _BufferElMiss_Type()
)
bufferElMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElMiss.setStatus("mandatory")
_BufferElCreate_Type = Integer32
_BufferElCreate_Object = MibScalar
bufferElCreate = _BufferElCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 13),
    _BufferElCreate_Type()
)
bufferElCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElCreate.setStatus("mandatory")
_BufferSmSize_Type = Integer32
_BufferSmSize_Object = MibScalar
bufferSmSize = _BufferSmSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 14),
    _BufferSmSize_Type()
)
bufferSmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmSize.setStatus("mandatory")
_BufferSmTotal_Type = Integer32
_BufferSmTotal_Object = MibScalar
bufferSmTotal = _BufferSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 15),
    _BufferSmTotal_Type()
)
bufferSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmTotal.setStatus("mandatory")
_BufferSmFree_Type = Integer32
_BufferSmFree_Object = MibScalar
bufferSmFree = _BufferSmFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 16),
    _BufferSmFree_Type()
)
bufferSmFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmFree.setStatus("mandatory")
_BufferSmMax_Type = Integer32
_BufferSmMax_Object = MibScalar
bufferSmMax = _BufferSmMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 17),
    _BufferSmMax_Type()
)
bufferSmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmMax.setStatus("mandatory")
_BufferSmHit_Type = Integer32
_BufferSmHit_Object = MibScalar
bufferSmHit = _BufferSmHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 18),
    _BufferSmHit_Type()
)
bufferSmHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmHit.setStatus("mandatory")
_BufferSmMiss_Type = Integer32
_BufferSmMiss_Object = MibScalar
bufferSmMiss = _BufferSmMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 19),
    _BufferSmMiss_Type()
)
bufferSmMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmMiss.setStatus("mandatory")
_BufferSmTrim_Type = Integer32
_BufferSmTrim_Object = MibScalar
bufferSmTrim = _BufferSmTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 20),
    _BufferSmTrim_Type()
)
bufferSmTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmTrim.setStatus("mandatory")
_BufferSmCreate_Type = Integer32
_BufferSmCreate_Object = MibScalar
bufferSmCreate = _BufferSmCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 21),
    _BufferSmCreate_Type()
)
bufferSmCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmCreate.setStatus("mandatory")
_BufferMdSize_Type = Integer32
_BufferMdSize_Object = MibScalar
bufferMdSize = _BufferMdSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 22),
    _BufferMdSize_Type()
)
bufferMdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdSize.setStatus("mandatory")
_BufferMdTotal_Type = Integer32
_BufferMdTotal_Object = MibScalar
bufferMdTotal = _BufferMdTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 23),
    _BufferMdTotal_Type()
)
bufferMdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdTotal.setStatus("mandatory")
_BufferMdFree_Type = Integer32
_BufferMdFree_Object = MibScalar
bufferMdFree = _BufferMdFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 24),
    _BufferMdFree_Type()
)
bufferMdFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdFree.setStatus("mandatory")
_BufferMdMax_Type = Integer32
_BufferMdMax_Object = MibScalar
bufferMdMax = _BufferMdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 25),
    _BufferMdMax_Type()
)
bufferMdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdMax.setStatus("mandatory")
_BufferMdHit_Type = Integer32
_BufferMdHit_Object = MibScalar
bufferMdHit = _BufferMdHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 26),
    _BufferMdHit_Type()
)
bufferMdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdHit.setStatus("mandatory")
_BufferMdMiss_Type = Integer32
_BufferMdMiss_Object = MibScalar
bufferMdMiss = _BufferMdMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 27),
    _BufferMdMiss_Type()
)
bufferMdMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdMiss.setStatus("mandatory")
_BufferMdTrim_Type = Integer32
_BufferMdTrim_Object = MibScalar
bufferMdTrim = _BufferMdTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 28),
    _BufferMdTrim_Type()
)
bufferMdTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdTrim.setStatus("mandatory")
_BufferMdCreate_Type = Integer32
_BufferMdCreate_Object = MibScalar
bufferMdCreate = _BufferMdCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 29),
    _BufferMdCreate_Type()
)
bufferMdCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdCreate.setStatus("mandatory")
_BufferBgSize_Type = Integer32
_BufferBgSize_Object = MibScalar
bufferBgSize = _BufferBgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 30),
    _BufferBgSize_Type()
)
bufferBgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgSize.setStatus("mandatory")
_BufferBgTotal_Type = Integer32
_BufferBgTotal_Object = MibScalar
bufferBgTotal = _BufferBgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 31),
    _BufferBgTotal_Type()
)
bufferBgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgTotal.setStatus("mandatory")
_BufferBgFree_Type = Integer32
_BufferBgFree_Object = MibScalar
bufferBgFree = _BufferBgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 32),
    _BufferBgFree_Type()
)
bufferBgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgFree.setStatus("mandatory")
_BufferBgMax_Type = Integer32
_BufferBgMax_Object = MibScalar
bufferBgMax = _BufferBgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 33),
    _BufferBgMax_Type()
)
bufferBgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgMax.setStatus("mandatory")
_BufferBgHit_Type = Integer32
_BufferBgHit_Object = MibScalar
bufferBgHit = _BufferBgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 34),
    _BufferBgHit_Type()
)
bufferBgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgHit.setStatus("mandatory")
_BufferBgMiss_Type = Integer32
_BufferBgMiss_Object = MibScalar
bufferBgMiss = _BufferBgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 35),
    _BufferBgMiss_Type()
)
bufferBgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgMiss.setStatus("mandatory")
_BufferBgTrim_Type = Integer32
_BufferBgTrim_Object = MibScalar
bufferBgTrim = _BufferBgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 36),
    _BufferBgTrim_Type()
)
bufferBgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgTrim.setStatus("mandatory")
_BufferBgCreate_Type = Integer32
_BufferBgCreate_Object = MibScalar
bufferBgCreate = _BufferBgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 37),
    _BufferBgCreate_Type()
)
bufferBgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgCreate.setStatus("mandatory")
_BufferLgSize_Type = Integer32
_BufferLgSize_Object = MibScalar
bufferLgSize = _BufferLgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 38),
    _BufferLgSize_Type()
)
bufferLgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgSize.setStatus("mandatory")
_BufferLgTotal_Type = Integer32
_BufferLgTotal_Object = MibScalar
bufferLgTotal = _BufferLgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 39),
    _BufferLgTotal_Type()
)
bufferLgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgTotal.setStatus("mandatory")
_BufferLgFree_Type = Integer32
_BufferLgFree_Object = MibScalar
bufferLgFree = _BufferLgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 40),
    _BufferLgFree_Type()
)
bufferLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgFree.setStatus("mandatory")
_BufferLgMax_Type = Integer32
_BufferLgMax_Object = MibScalar
bufferLgMax = _BufferLgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 41),
    _BufferLgMax_Type()
)
bufferLgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgMax.setStatus("mandatory")
_BufferLgHit_Type = Integer32
_BufferLgHit_Object = MibScalar
bufferLgHit = _BufferLgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 42),
    _BufferLgHit_Type()
)
bufferLgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgHit.setStatus("mandatory")
_BufferLgMiss_Type = Integer32
_BufferLgMiss_Object = MibScalar
bufferLgMiss = _BufferLgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 43),
    _BufferLgMiss_Type()
)
bufferLgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgMiss.setStatus("mandatory")
_BufferLgTrim_Type = Integer32
_BufferLgTrim_Object = MibScalar
bufferLgTrim = _BufferLgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 44),
    _BufferLgTrim_Type()
)
bufferLgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgTrim.setStatus("mandatory")
_BufferLgCreate_Type = Integer32
_BufferLgCreate_Object = MibScalar
bufferLgCreate = _BufferLgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 45),
    _BufferLgCreate_Type()
)
bufferLgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgCreate.setStatus("mandatory")
_BufferFail_Type = Integer32
_BufferFail_Object = MibScalar
bufferFail = _BufferFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 46),
    _BufferFail_Type()
)
bufferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferFail.setStatus("mandatory")
_BufferNoMem_Type = Integer32
_BufferNoMem_Object = MibScalar
bufferNoMem = _BufferNoMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 47),
    _BufferNoMem_Type()
)
bufferNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferNoMem.setStatus("mandatory")
_BufferHgSize_Type = Integer32
_BufferHgSize_Object = MibScalar
bufferHgSize = _BufferHgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 62),
    _BufferHgSize_Type()
)
bufferHgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgSize.setStatus("mandatory")
_BufferHgTotal_Type = Integer32
_BufferHgTotal_Object = MibScalar
bufferHgTotal = _BufferHgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 63),
    _BufferHgTotal_Type()
)
bufferHgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgTotal.setStatus("mandatory")
_BufferHgFree_Type = Integer32
_BufferHgFree_Object = MibScalar
bufferHgFree = _BufferHgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 64),
    _BufferHgFree_Type()
)
bufferHgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgFree.setStatus("mandatory")
_BufferHgMax_Type = Integer32
_BufferHgMax_Object = MibScalar
bufferHgMax = _BufferHgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 65),
    _BufferHgMax_Type()
)
bufferHgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgMax.setStatus("mandatory")
_BufferHgHit_Type = Integer32
_BufferHgHit_Object = MibScalar
bufferHgHit = _BufferHgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 66),
    _BufferHgHit_Type()
)
bufferHgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgHit.setStatus("mandatory")
_BufferHgMiss_Type = Integer32
_BufferHgMiss_Object = MibScalar
bufferHgMiss = _BufferHgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 67),
    _BufferHgMiss_Type()
)
bufferHgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgMiss.setStatus("mandatory")
_BufferHgTrim_Type = Integer32
_BufferHgTrim_Object = MibScalar
bufferHgTrim = _BufferHgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 68),
    _BufferHgTrim_Type()
)
bufferHgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgTrim.setStatus("mandatory")
_BufferHgCreate_Type = Integer32
_BufferHgCreate_Object = MibScalar
bufferHgCreate = _BufferHgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 69),
    _BufferHgCreate_Type()
)
bufferHgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgCreate.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-MEMORY-MIB",
    **{"lmem": lmem,
       "freeMem": freeMem,
       "bufferElFree": bufferElFree,
       "bufferElMax": bufferElMax,
       "bufferElHit": bufferElHit,
       "bufferElMiss": bufferElMiss,
       "bufferElCreate": bufferElCreate,
       "bufferSmSize": bufferSmSize,
       "bufferSmTotal": bufferSmTotal,
       "bufferSmFree": bufferSmFree,
       "bufferSmMax": bufferSmMax,
       "bufferSmHit": bufferSmHit,
       "bufferSmMiss": bufferSmMiss,
       "bufferSmTrim": bufferSmTrim,
       "bufferSmCreate": bufferSmCreate,
       "bufferMdSize": bufferMdSize,
       "bufferMdTotal": bufferMdTotal,
       "bufferMdFree": bufferMdFree,
       "bufferMdMax": bufferMdMax,
       "bufferMdHit": bufferMdHit,
       "bufferMdMiss": bufferMdMiss,
       "bufferMdTrim": bufferMdTrim,
       "bufferMdCreate": bufferMdCreate,
       "bufferBgSize": bufferBgSize,
       "bufferBgTotal": bufferBgTotal,
       "bufferBgFree": bufferBgFree,
       "bufferBgMax": bufferBgMax,
       "bufferBgHit": bufferBgHit,
       "bufferBgMiss": bufferBgMiss,
       "bufferBgTrim": bufferBgTrim,
       "bufferBgCreate": bufferBgCreate,
       "bufferLgSize": bufferLgSize,
       "bufferLgTotal": bufferLgTotal,
       "bufferLgFree": bufferLgFree,
       "bufferLgMax": bufferLgMax,
       "bufferLgHit": bufferLgHit,
       "bufferLgMiss": bufferLgMiss,
       "bufferLgTrim": bufferLgTrim,
       "bufferLgCreate": bufferLgCreate,
       "bufferFail": bufferFail,
       "bufferNoMem": bufferNoMem,
       "bufferHgSize": bufferHgSize,
       "bufferHgTotal": bufferHgTotal,
       "bufferHgFree": bufferHgFree,
       "bufferHgMax": bufferHgMax,
       "bufferHgHit": bufferHgHit,
       "bufferHgMiss": bufferHgMiss,
       "bufferHgTrim": bufferHgTrim,
       "bufferHgCreate": bufferHgCreate}
)
