# SNMP MIB module (MWORKS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MWORKS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:24:09 2024
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
_MeterWorks_ObjectIdentity = ObjectIdentity
meterWorks = _MeterWorks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 16)
)
_Mw501_ObjectIdentity = ObjectIdentity
mw501 = _Mw501_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 16, 1)
)
_MwMem_ObjectIdentity = ObjectIdentity
mwMem = _MwMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 1)
)
_MwMemCeiling_Type = Counter32
_MwMemCeiling_Object = MibScalar
mwMemCeiling = _MwMemCeiling_Object(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 1, 1),
    _MwMemCeiling_Type()
)
mwMemCeiling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMemCeiling.setStatus("mandatory")
_MwMemUsed_Type = Counter32
_MwMemUsed_Object = MibScalar
mwMemUsed = _MwMemUsed_Object(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 1, 2),
    _MwMemUsed_Type()
)
mwMemUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwMemUsed.setStatus("mandatory")
_MwHeap_ObjectIdentity = ObjectIdentity
mwHeap = _MwHeap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 2)
)
_MwHeapTotal_Type = Counter32
_MwHeapTotal_Object = MibScalar
mwHeapTotal = _MwHeapTotal_Object(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 2, 1),
    _MwHeapTotal_Type()
)
mwHeapTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwHeapTotal.setStatus("mandatory")
_MwHeapUsed_Type = Counter32
_MwHeapUsed_Object = MibScalar
mwHeapUsed = _MwHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 217, 16, 1, 2, 2),
    _MwHeapUsed_Type()
)
mwHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwHeapUsed.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MWORKS-MIB",
    **{"tecElite": tecElite,
       "meterWorks": meterWorks,
       "mw501": mw501,
       "mwMem": mwMem,
       "mwMemCeiling": mwMemCeiling,
       "mwMemUsed": mwMemUsed,
       "mwHeap": mwHeap,
       "mwHeapTotal": mwHeapTotal,
       "mwHeapUsed": mwHeapUsed}
)
