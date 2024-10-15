# SNMP MIB module (OLD-CISCO-CPU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-CPU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:58 2024
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

_Lcpu_ObjectIdentity = ObjectIdentity
lcpu = _Lcpu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 1)
)
_BusyPer_Type = Integer32
_BusyPer_Object = MibScalar
busyPer = _BusyPer_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 56),
    _BusyPer_Type()
)
busyPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyPer.setStatus("mandatory")
_AvgBusy1_Type = Integer32
_AvgBusy1_Object = MibScalar
avgBusy1 = _AvgBusy1_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 57),
    _AvgBusy1_Type()
)
avgBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBusy1.setStatus("mandatory")
_AvgBusy5_Type = Integer32
_AvgBusy5_Object = MibScalar
avgBusy5 = _AvgBusy5_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 58),
    _AvgBusy5_Type()
)
avgBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBusy5.setStatus("mandatory")
_IdleCount_Type = Integer32
_IdleCount_Object = MibScalar
idleCount = _IdleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 59),
    _IdleCount_Type()
)
idleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleCount.setStatus("mandatory")
_IdleWired_Type = Integer32
_IdleWired_Object = MibScalar
idleWired = _IdleWired_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 60),
    _IdleWired_Type()
)
idleWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleWired.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-CPU-MIB",
    **{"lcpu": lcpu,
       "busyPer": busyPer,
       "avgBusy1": avgBusy1,
       "avgBusy5": avgBusy5,
       "idleCount": idleCount,
       "idleWired": idleWired}
)
