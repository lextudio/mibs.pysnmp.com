# SNMP MIB module (VC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:01 2024
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

_VcStatMIB_ObjectIdentity = ObjectIdentity
vcStatMIB = _VcStatMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3)
)
_VcStat_ObjectIdentity = ObjectIdentity
vcStat = _VcStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1)
)
_VcStatTable_Object = MibTable
vcStatTable = _VcStatTable_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    vcStatTable.setStatus("mandatory")
_VcEntry_Object = MibTableRow
vcEntry = _VcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1)
)
vcEntry.setIndexNames(
    (0, "VC-MIB", "vcPipePosition"),
    (0, "VC-MIB", "vcPipeInstancePosition"),
    (0, "VC-MIB", "vcPosition"),
    (0, "VC-MIB", "vcInstancePosition"),
)
if mibBuilder.loadTexts:
    vcEntry.setStatus("mandatory")
_VcPipePosition_Type = Integer32
_VcPipePosition_Object = MibTableColumn
vcPipePosition = _VcPipePosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 1),
    _VcPipePosition_Type()
)
vcPipePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPipePosition.setStatus("mandatory")
_VcPipeInstancePosition_Type = Integer32
_VcPipeInstancePosition_Object = MibTableColumn
vcPipeInstancePosition = _VcPipeInstancePosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 2),
    _VcPipeInstancePosition_Type()
)
vcPipeInstancePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPipeInstancePosition.setStatus("mandatory")
_VcPosition_Type = Integer32
_VcPosition_Object = MibTableColumn
vcPosition = _VcPosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 3),
    _VcPosition_Type()
)
vcPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPosition.setStatus("mandatory")
_VcInstancePosition_Type = Integer32
_VcInstancePosition_Object = MibTableColumn
vcInstancePosition = _VcInstancePosition_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 4),
    _VcInstancePosition_Type()
)
vcInstancePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcInstancePosition.setStatus("mandatory")
_VcName_Type = DisplayString
_VcName_Object = MibTableColumn
vcName = _VcName_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 5),
    _VcName_Type()
)
vcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcName.setStatus("mandatory")
_VcByteCountIn_Type = Counter32
_VcByteCountIn_Object = MibTableColumn
vcByteCountIn = _VcByteCountIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 6),
    _VcByteCountIn_Type()
)
vcByteCountIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcByteCountIn.setStatus("mandatory")
_VcByteCountOut_Type = Counter32
_VcByteCountOut_Object = MibTableColumn
vcByteCountOut = _VcByteCountOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 7),
    _VcByteCountOut_Type()
)
vcByteCountOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcByteCountOut.setStatus("mandatory")
_VcByteCountTotal_Type = Counter32
_VcByteCountTotal_Object = MibTableColumn
vcByteCountTotal = _VcByteCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 8),
    _VcByteCountTotal_Type()
)
vcByteCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcByteCountTotal.setStatus("mandatory")
_VcLiveConnections_Type = Counter32
_VcLiveConnections_Object = MibTableColumn
vcLiveConnections = _VcLiveConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 9),
    _VcLiveConnections_Type()
)
vcLiveConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcLiveConnections.setStatus("mandatory")
_VcNewConnections_Type = Counter32
_VcNewConnections_Object = MibTableColumn
vcNewConnections = _VcNewConnections_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 10),
    _VcNewConnections_Type()
)
vcNewConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcNewConnections.setStatus("mandatory")
_VcPacketsIn_Type = Counter32
_VcPacketsIn_Object = MibTableColumn
vcPacketsIn = _VcPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 11),
    _VcPacketsIn_Type()
)
vcPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPacketsIn.setStatus("mandatory")
_VcPacketsOut_Type = Counter32
_VcPacketsOut_Object = MibTableColumn
vcPacketsOut = _VcPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 12),
    _VcPacketsOut_Type()
)
vcPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPacketsOut.setStatus("mandatory")
_VcPacketsTotal_Type = Counter32
_VcPacketsTotal_Object = MibTableColumn
vcPacketsTotal = _VcPacketsTotal_Object(
    (1, 3, 6, 1, 4, 1, 2603, 1, 3, 1, 1, 1, 13),
    _VcPacketsTotal_Type()
)
vcPacketsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vcPacketsTotal.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VC-MIB",
    **{"vcStatMIB": vcStatMIB,
       "vcStat": vcStat,
       "vcStatTable": vcStatTable,
       "vcEntry": vcEntry,
       "vcPipePosition": vcPipePosition,
       "vcPipeInstancePosition": vcPipeInstancePosition,
       "vcPosition": vcPosition,
       "vcInstancePosition": vcInstancePosition,
       "vcName": vcName,
       "vcByteCountIn": vcByteCountIn,
       "vcByteCountOut": vcByteCountOut,
       "vcByteCountTotal": vcByteCountTotal,
       "vcLiveConnections": vcLiveConnections,
       "vcNewConnections": vcNewConnections,
       "vcPacketsIn": vcPacketsIn,
       "vcPacketsOut": vcPacketsOut,
       "vcPacketsTotal": vcPacketsTotal}
)
