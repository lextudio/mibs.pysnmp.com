# SNMP MIB module (MWORKS-E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MWORKS-E-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:08 2024
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

_TecElite_ObjectIdentity = ObjectIdentity
tecElite = _TecElite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217)
)
_Mworkse_ObjectIdentity = ObjectIdentity
mworkse = _Mworkse_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 17)
)
_Am501_ObjectIdentity = ObjectIdentity
am501 = _Am501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 17, 1)
)
_AmMem_ObjectIdentity = ObjectIdentity
amMem = _AmMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 1)
)
_AmMemCeiling_Type = Counter32
_AmMemCeiling_Object = MibScalar
amMemCeiling = _AmMemCeiling_Object(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 1, 1),
    _AmMemCeiling_Type()
)
amMemCeiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amMemCeiling.setStatus("mandatory")
_AmMemUsed_Type = Counter32
_AmMemUsed_Object = MibScalar
amMemUsed = _AmMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 1, 2),
    _AmMemUsed_Type()
)
amMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amMemUsed.setStatus("mandatory")
_AmHeap_ObjectIdentity = ObjectIdentity
amHeap = _AmHeap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 2)
)
_AmHeapTotal_Type = Counter32
_AmHeapTotal_Object = MibScalar
amHeapTotal = _AmHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 2, 1),
    _AmHeapTotal_Type()
)
amHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amHeapTotal.setStatus("mandatory")
_AmHeapUsed_Type = Counter32
_AmHeapUsed_Object = MibScalar
amHeapUsed = _AmHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 217, 17, 1, 2, 2),
    _AmHeapUsed_Type()
)
amHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amHeapUsed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWORKS-E-MIB",
    **{"tecElite": tecElite,
       "mworkse": mworkse,
       "am501": am501,
       "amMem": amMem,
       "amMemCeiling": amMemCeiling,
       "amMemUsed": amMemUsed,
       "amHeap": amHeap,
       "amHeapTotal": amHeapTotal,
       "amHeapUsed": amHeapUsed}
)
