# SNMP MIB module (PIPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PIPE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:50 2024
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

(neStatistics,) = mibBuilder.importSymbols(
    "NE-STAT-MIB",
    "neStatistics")

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

_PipeStatMIB_ObjectIdentity = ObjectIdentity
pipeStatMIB = _PipeStatMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2)
)
_PipeStat_ObjectIdentity = ObjectIdentity
pipeStat = _PipeStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1)
)
_PipeStatTable_Object = MibTable
pipeStatTable = _PipeStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pipeStatTable.setStatus("mandatory")
_PipeEntry_Object = MibTableRow
pipeEntry = _PipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1)
)
pipeEntry.setIndexNames(
    (0, "PIPE-MIB", "pipePosition"),
    (0, "PIPE-MIB", "pipeInstancePosition"),
)
if mibBuilder.loadTexts:
    pipeEntry.setStatus("mandatory")
_PipePosition_Type = Integer32
_PipePosition_Object = MibTableColumn
pipePosition = _PipePosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 1),
    _PipePosition_Type()
)
pipePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipePosition.setStatus("mandatory")
_PipeInstancePosition_Type = Integer32
_PipeInstancePosition_Object = MibTableColumn
pipeInstancePosition = _PipeInstancePosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 2),
    _PipeInstancePosition_Type()
)
pipeInstancePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeInstancePosition.setStatus("mandatory")
_PipeName_Type = DisplayString
_PipeName_Object = MibTableColumn
pipeName = _PipeName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 3),
    _PipeName_Type()
)
pipeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeName.setStatus("mandatory")
_PipeByteCountIn_Type = Counter32
_PipeByteCountIn_Object = MibTableColumn
pipeByteCountIn = _PipeByteCountIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 4),
    _PipeByteCountIn_Type()
)
pipeByteCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeByteCountIn.setStatus("mandatory")
_PipeByteCountOut_Type = Counter32
_PipeByteCountOut_Object = MibTableColumn
pipeByteCountOut = _PipeByteCountOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 5),
    _PipeByteCountOut_Type()
)
pipeByteCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeByteCountOut.setStatus("mandatory")
_PipeByteCountTotal_Type = Counter32
_PipeByteCountTotal_Object = MibTableColumn
pipeByteCountTotal = _PipeByteCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 6),
    _PipeByteCountTotal_Type()
)
pipeByteCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeByteCountTotal.setStatus("mandatory")
_PipeLiveConnections_Type = Counter32
_PipeLiveConnections_Object = MibTableColumn
pipeLiveConnections = _PipeLiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 7),
    _PipeLiveConnections_Type()
)
pipeLiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeLiveConnections.setStatus("mandatory")
_PipeNewConnections_Type = Counter32
_PipeNewConnections_Object = MibTableColumn
pipeNewConnections = _PipeNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 8),
    _PipeNewConnections_Type()
)
pipeNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipeNewConnections.setStatus("mandatory")
_PipePacketsIn_Type = Counter32
_PipePacketsIn_Object = MibTableColumn
pipePacketsIn = _PipePacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 9),
    _PipePacketsIn_Type()
)
pipePacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipePacketsIn.setStatus("mandatory")
_PipePacketsOut_Type = Counter32
_PipePacketsOut_Object = MibTableColumn
pipePacketsOut = _PipePacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 10),
    _PipePacketsOut_Type()
)
pipePacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipePacketsOut.setStatus("mandatory")
_PipePacketsTotal_Type = Counter32
_PipePacketsTotal_Object = MibTableColumn
pipePacketsTotal = _PipePacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 2, 1, 1, 1, 11),
    _PipePacketsTotal_Type()
)
pipePacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pipePacketsTotal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PIPE-MIB",
    **{"pipeStatMIB": pipeStatMIB,
       "pipeStat": pipeStat,
       "pipeStatTable": pipeStatTable,
       "pipeEntry": pipeEntry,
       "pipePosition": pipePosition,
       "pipeInstancePosition": pipeInstancePosition,
       "pipeName": pipeName,
       "pipeByteCountIn": pipeByteCountIn,
       "pipeByteCountOut": pipeByteCountOut,
       "pipeByteCountTotal": pipeByteCountTotal,
       "pipeLiveConnections": pipeLiveConnections,
       "pipeNewConnections": pipeNewConnections,
       "pipePacketsIn": pipePacketsIn,
       "pipePacketsOut": pipePacketsOut,
       "pipePacketsTotal": pipePacketsTotal}
)
