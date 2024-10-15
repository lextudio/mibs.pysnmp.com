# SNMP MIB module (NE-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NE-STAT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:25:18 2024
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

(allotCom,) = mibBuilder.importSymbols(
    "COMPANY-MIB",
    "allotCom")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

neStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NeStatMIB_ObjectIdentity = ObjectIdentity
neStatMIB = _NeStatMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1)
)
_NeStat_ObjectIdentity = ObjectIdentity
neStat = _NeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1)
)
_NeByteCountIn_Type = Counter32
_NeByteCountIn_Object = MibScalar
neByteCountIn = _NeByteCountIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 1),
    _NeByteCountIn_Type()
)
neByteCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neByteCountIn.setStatus("current")
_NeByteCountOut_Type = Counter32
_NeByteCountOut_Object = MibScalar
neByteCountOut = _NeByteCountOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 2),
    _NeByteCountOut_Type()
)
neByteCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neByteCountOut.setStatus("current")
_NeByteCountTotal_Type = Counter32
_NeByteCountTotal_Object = MibScalar
neByteCountTotal = _NeByteCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 3),
    _NeByteCountTotal_Type()
)
neByteCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neByteCountTotal.setStatus("current")
_NeLiveConnections_Type = Counter32
_NeLiveConnections_Object = MibScalar
neLiveConnections = _NeLiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 4),
    _NeLiveConnections_Type()
)
neLiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neLiveConnections.setStatus("current")
_NeNewConnections_Type = Counter32
_NeNewConnections_Object = MibScalar
neNewConnections = _NeNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 5),
    _NeNewConnections_Type()
)
neNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    neNewConnections.setStatus("current")
_NePacketsIn_Type = Counter32
_NePacketsIn_Object = MibScalar
nePacketsIn = _NePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 6),
    _NePacketsIn_Type()
)
nePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nePacketsIn.setStatus("current")
_NePacketsOut_Type = Counter32
_NePacketsOut_Object = MibScalar
nePacketsOut = _NePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 7),
    _NePacketsOut_Type()
)
nePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nePacketsOut.setStatus("current")
_NePacketsTotal_Type = Counter32
_NePacketsTotal_Object = MibScalar
nePacketsTotal = _NePacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 1, 8),
    _NePacketsTotal_Type()
)
nePacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nePacketsTotal.setStatus("current")

# Managed Objects groups

neByteCountersGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2603, 1, 1, 2)
)
neByteCountersGroup.setObjects(
      *(("NE-STAT-MIB", "neByteCountIn"),
        ("NE-STAT-MIB", "neByteCountOut"),
        ("NE-STAT-MIB", "neByteCountTotal"),
        ("NE-STAT-MIB", "neLiveConnections"),
        ("NE-STAT-MIB", "neNewConnections"),
        ("NE-STAT-MIB", "nePacketsIn"),
        ("NE-STAT-MIB", "nePacketsOut"),
        ("NE-STAT-MIB", "nePacketsTotal"))
)
if mibBuilder.loadTexts:
    neByteCountersGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NE-STAT-MIB",
    **{"neStatistics": neStatistics,
       "neStatMIB": neStatMIB,
       "neStat": neStat,
       "neByteCountIn": neByteCountIn,
       "neByteCountOut": neByteCountOut,
       "neByteCountTotal": neByteCountTotal,
       "neLiveConnections": neLiveConnections,
       "neNewConnections": neNewConnections,
       "nePacketsIn": nePacketsIn,
       "nePacketsOut": nePacketsOut,
       "nePacketsTotal": nePacketsTotal,
       "neByteCountersGroup": neByteCountersGroup}
)
