# SNMP MIB module (CX-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CX-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:01 2024
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

(cxIpx,) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "cxIpx")

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

_IpxStatsTable_Object = MibTable
ipxStatsTable = _IpxStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2)
)
if mibBuilder.loadTexts:
    ipxStatsTable.setStatus("mandatory")
_IpxStatsEntry_Object = MibTableRow
ipxStatsEntry = _IpxStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1)
)
ipxStatsEntry.setIndexNames(
    (0, "CX-IPX-MIB", "ipxSysIndex"),
)
if mibBuilder.loadTexts:
    ipxStatsEntry.setStatus("mandatory")
_IpxSysIndex_Type = Integer32
_IpxSysIndex_Object = MibTableColumn
ipxSysIndex = _IpxSysIndex_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 1),
    _IpxSysIndex_Type()
)
ipxSysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysIndex.setStatus("mandatory")
_IpxSysInReceives_Type = Counter32
_IpxSysInReceives_Object = MibTableColumn
ipxSysInReceives = _IpxSysInReceives_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 2),
    _IpxSysInReceives_Type()
)
ipxSysInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInReceives.setStatus("mandatory")
_IpxSysInHdrErrors_Type = Counter32
_IpxSysInHdrErrors_Object = MibTableColumn
ipxSysInHdrErrors = _IpxSysInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 3),
    _IpxSysInHdrErrors_Type()
)
ipxSysInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInHdrErrors.setStatus("mandatory")
_IpxSysInFiltered_Type = Counter32
_IpxSysInFiltered_Object = MibTableColumn
ipxSysInFiltered = _IpxSysInFiltered_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 4),
    _IpxSysInFiltered_Type()
)
ipxSysInFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInFiltered.setStatus("mandatory")
_IpxSysInDiscards_Type = Counter32
_IpxSysInDiscards_Object = MibTableColumn
ipxSysInDiscards = _IpxSysInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 5),
    _IpxSysInDiscards_Type()
)
ipxSysInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysInDiscards.setStatus("mandatory")
_IpxSysForwPackets_Type = Counter32
_IpxSysForwPackets_Object = MibTableColumn
ipxSysForwPackets = _IpxSysForwPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 6),
    _IpxSysForwPackets_Type()
)
ipxSysForwPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysForwPackets.setStatus("mandatory")
_IpxSysOutFiltered_Type = Counter32
_IpxSysOutFiltered_Object = MibTableColumn
ipxSysOutFiltered = _IpxSysOutFiltered_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 7),
    _IpxSysOutFiltered_Type()
)
ipxSysOutFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutFiltered.setStatus("mandatory")
_IpxSysOutDiscards_Type = Counter32
_IpxSysOutDiscards_Object = MibTableColumn
ipxSysOutDiscards = _IpxSysOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 8),
    _IpxSysOutDiscards_Type()
)
ipxSysOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutDiscards.setStatus("mandatory")
_IpxSysOutPackets_Type = Counter32
_IpxSysOutPackets_Object = MibTableColumn
ipxSysOutPackets = _IpxSysOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 9),
    _IpxSysOutPackets_Type()
)
ipxSysOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysOutPackets.setStatus("mandatory")
_IpxSysResourceFailures_Type = Counter32
_IpxSysResourceFailures_Object = MibTableColumn
ipxSysResourceFailures = _IpxSysResourceFailures_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 10),
    _IpxSysResourceFailures_Type()
)
ipxSysResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysResourceFailures.setStatus("mandatory")
_RipsapSysRIPIncorrectPackets_Type = Counter32
_RipsapSysRIPIncorrectPackets_Object = MibTableColumn
ripsapSysRIPIncorrectPackets = _RipsapSysRIPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 11),
    _RipsapSysRIPIncorrectPackets_Type()
)
ripsapSysRIPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapSysRIPIncorrectPackets.setStatus("mandatory")
_RipsapSysSAPIncorrectPackets_Type = Counter32
_RipsapSysSAPIncorrectPackets_Object = MibTableColumn
ripsapSysSAPIncorrectPackets = _RipsapSysSAPIncorrectPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 12),
    _RipsapSysSAPIncorrectPackets_Type()
)
ripsapSysSAPIncorrectPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapSysSAPIncorrectPackets.setStatus("mandatory")
_RipsapCircRIPOutPackets_Type = Counter32
_RipsapCircRIPOutPackets_Object = MibTableColumn
ripsapCircRIPOutPackets = _RipsapCircRIPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 13),
    _RipsapCircRIPOutPackets_Type()
)
ripsapCircRIPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapCircRIPOutPackets.setStatus("mandatory")
_RipsapCircRIPInPackets_Type = Counter32
_RipsapCircRIPInPackets_Object = MibTableColumn
ripsapCircRIPInPackets = _RipsapCircRIPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 14),
    _RipsapCircRIPInPackets_Type()
)
ripsapCircRIPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapCircRIPInPackets.setStatus("mandatory")
_RipsapCircSAPOutPackets_Type = Counter32
_RipsapCircSAPOutPackets_Object = MibTableColumn
ripsapCircSAPOutPackets = _RipsapCircSAPOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 15),
    _RipsapCircSAPOutPackets_Type()
)
ripsapCircSAPOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapCircSAPOutPackets.setStatus("mandatory")
_RipsapCircSAPInPackets_Type = Counter32
_RipsapCircSAPInPackets_Object = MibTableColumn
ripsapCircSAPInPackets = _RipsapCircSAPInPackets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 16),
    _RipsapCircSAPInPackets_Type()
)
ripsapCircSAPInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripsapCircSAPInPackets.setStatus("mandatory")
_IpxSysWatchReq_Type = Counter32
_IpxSysWatchReq_Object = MibTableColumn
ipxSysWatchReq = _IpxSysWatchReq_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 17),
    _IpxSysWatchReq_Type()
)
ipxSysWatchReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysWatchReq.setStatus("mandatory")
_IpxSysWatchRsp_Type = Counter32
_IpxSysWatchRsp_Object = MibTableColumn
ipxSysWatchRsp = _IpxSysWatchRsp_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 18),
    _IpxSysWatchRsp_Type()
)
ipxSysWatchRsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysWatchRsp.setStatus("mandatory")
_IpxSysSerRcv_Type = Counter32
_IpxSysSerRcv_Object = MibTableColumn
ipxSysSerRcv = _IpxSysSerRcv_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 13, 2, 1, 19),
    _IpxSysSerRcv_Type()
)
ipxSysSerRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSysSerRcv.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CX-IPX-MIB",
    **{"ipxStatsTable": ipxStatsTable,
       "ipxStatsEntry": ipxStatsEntry,
       "ipxSysIndex": ipxSysIndex,
       "ipxSysInReceives": ipxSysInReceives,
       "ipxSysInHdrErrors": ipxSysInHdrErrors,
       "ipxSysInFiltered": ipxSysInFiltered,
       "ipxSysInDiscards": ipxSysInDiscards,
       "ipxSysForwPackets": ipxSysForwPackets,
       "ipxSysOutFiltered": ipxSysOutFiltered,
       "ipxSysOutDiscards": ipxSysOutDiscards,
       "ipxSysOutPackets": ipxSysOutPackets,
       "ipxSysResourceFailures": ipxSysResourceFailures,
       "ripsapSysRIPIncorrectPackets": ripsapSysRIPIncorrectPackets,
       "ripsapSysSAPIncorrectPackets": ripsapSysSAPIncorrectPackets,
       "ripsapCircRIPOutPackets": ripsapCircRIPOutPackets,
       "ripsapCircRIPInPackets": ripsapCircRIPInPackets,
       "ripsapCircSAPOutPackets": ripsapCircSAPOutPackets,
       "ripsapCircSAPInPackets": ripsapCircSAPInPackets,
       "ipxSysWatchReq": ipxSysWatchReq,
       "ipxSysWatchRsp": ipxSysWatchRsp,
       "ipxSysSerRcv": ipxSysSerRcv}
)
