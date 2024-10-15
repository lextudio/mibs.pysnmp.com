# SNMP MIB module (IPVS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPVS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:32 2024
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

(one4net,) = mibBuilder.importSymbols(
    "ONE4NET-MIB",
    "one4net")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

ipvs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12196, 12)
)
ipvs.setRevisions(
        ("2011-12-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpvsVSTable_Object = MibTable
ipvsVSTable = _IpvsVSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1)
)
if mibBuilder.loadTexts:
    ipvsVSTable.setStatus("current")
_VsEntry_Object = MibTableRow
vsEntry = _VsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1)
)
vsEntry.setIndexNames(
    (0, "IPVS-MIB", "vSidx"),
)
if mibBuilder.loadTexts:
    vsEntry.setStatus("current")


class _VSidx_Type(Integer32):
    """Custom type vSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VSidx_Type.__name__ = "Integer32"
_VSidx_Object = MibTableColumn
vSidx = _VSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 1),
    _VSidx_Type()
)
vSidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSidx.setStatus("current")


class _VSDesc_Type(OctetString):
    """Custom type vSDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_VSDesc_Type.__name__ = "OctetString"
_VSDesc_Object = MibTableColumn
vSDesc = _VSDesc_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 11),
    _VSDesc_Type()
)
vSDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSDesc.setStatus("current")
_VSConns_Type = Counter32
_VSConns_Object = MibTableColumn
vSConns = _VSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 12),
    _VSConns_Type()
)
vSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSConns.setStatus("current")
_VSInPkts_Type = Counter32
_VSInPkts_Object = MibTableColumn
vSInPkts = _VSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 13),
    _VSInPkts_Type()
)
vSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInPkts.setStatus("current")
_VSOutPkts_Type = Counter32
_VSOutPkts_Object = MibTableColumn
vSOutPkts = _VSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 14),
    _VSOutPkts_Type()
)
vSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutPkts.setStatus("current")
_VSInBytes_Type = Counter64
_VSInBytes_Object = MibTableColumn
vSInBytes = _VSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 15),
    _VSInBytes_Type()
)
vSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSInBytes.setStatus("current")
_VSOutBytes_Type = Counter64
_VSOutBytes_Object = MibTableColumn
vSOutBytes = _VSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 16),
    _VSOutBytes_Type()
)
vSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSOutBytes.setStatus("current")
_VSActivConns_Type = Counter32
_VSActivConns_Object = MibTableColumn
vSActivConns = _VSActivConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 1, 1, 17),
    _VSActivConns_Type()
)
vSActivConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vSActivConns.setStatus("current")
_IpvsRSTable_Object = MibTable
ipvsRSTable = _IpvsRSTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2)
)
if mibBuilder.loadTexts:
    ipvsRSTable.setStatus("current")
_RsEntry_Object = MibTableRow
rsEntry = _RsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1)
)
rsEntry.setIndexNames(
    (0, "IPVS-MIB", "rSidx"),
)
if mibBuilder.loadTexts:
    rsEntry.setStatus("current")


class _RSidx_Type(Integer32):
    """Custom type rSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RSidx_Type.__name__ = "Integer32"
_RSidx_Object = MibTableColumn
rSidx = _RSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 1),
    _RSidx_Type()
)
rSidx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rSidx.setStatus("current")


class _RSVSidx_Type(Integer32):
    """Custom type rSVSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_RSVSidx_Type.__name__ = "Integer32"
_RSVSidx_Object = MibTableColumn
rSVSidx = _RSVSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 2),
    _RSVSidx_Type()
)
rSVSidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSVSidx.setStatus("current")


class _RSDesc_Type(OctetString):
    """Custom type rSDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RSDesc_Type.__name__ = "OctetString"
_RSDesc_Object = MibTableColumn
rSDesc = _RSDesc_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 11),
    _RSDesc_Type()
)
rSDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSDesc.setStatus("current")
_RSConns_Type = Counter32
_RSConns_Object = MibTableColumn
rSConns = _RSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 12),
    _RSConns_Type()
)
rSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSConns.setStatus("current")
_RSInPkts_Type = Counter32
_RSInPkts_Object = MibTableColumn
rSInPkts = _RSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 13),
    _RSInPkts_Type()
)
rSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInPkts.setStatus("current")
_RSOutPkts_Type = Counter32
_RSOutPkts_Object = MibTableColumn
rSOutPkts = _RSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 14),
    _RSOutPkts_Type()
)
rSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutPkts.setStatus("current")
_RSInBytes_Type = Counter64
_RSInBytes_Object = MibTableColumn
rSInBytes = _RSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 15),
    _RSInBytes_Type()
)
rSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInBytes.setStatus("current")
_RSOutBytes_Type = Counter64
_RSOutBytes_Object = MibTableColumn
rSOutBytes = _RSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 16),
    _RSOutBytes_Type()
)
rSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSOutBytes.setStatus("current")
_RSActiveConns_Type = Counter32
_RSActiveConns_Object = MibTableColumn
rSActiveConns = _RSActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 17),
    _RSActiveConns_Type()
)
rSActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSActiveConns.setStatus("current")
_RSInactiveConns_Type = Counter32
_RSInactiveConns_Object = MibTableColumn
rSInactiveConns = _RSInactiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 18),
    _RSInactiveConns_Type()
)
rSInactiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSInactiveConns.setStatus("current")
_RSWeight_Type = Counter32
_RSWeight_Object = MibTableColumn
rSWeight = _RSWeight_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 2, 1, 19),
    _RSWeight_Type()
)
rSWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rSWeight.setStatus("current")
_Conns_Type = Counter32
_Conns_Object = MibScalar
conns = _Conns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 3),
    _Conns_Type()
)
conns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    conns.setStatus("current")
_InPkts_Type = Counter32
_InPkts_Object = MibScalar
inPkts = _InPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 4),
    _InPkts_Type()
)
inPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inPkts.setStatus("current")
_OutPkts_Type = Counter32
_OutPkts_Object = MibScalar
outPkts = _OutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 5),
    _OutPkts_Type()
)
outPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outPkts.setStatus("current")
_InBytes_Type = Counter64
_InBytes_Object = MibScalar
inBytes = _InBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 6),
    _InBytes_Type()
)
inBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inBytes.setStatus("current")
_OutBytes_Type = Counter64
_OutBytes_Object = MibScalar
outBytes = _OutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 7),
    _OutBytes_Type()
)
outBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    outBytes.setStatus("current")
_IpvsRSTotalTable_Object = MibTable
ipvsRSTotalTable = _IpvsRSTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8)
)
if mibBuilder.loadTexts:
    ipvsRSTotalTable.setStatus("current")
_RsTotalEntry_Object = MibTableRow
rsTotalEntry = _RsTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1)
)
rsTotalEntry.setIndexNames(
    (0, "IPVS-MIB", "totRSidx"),
)
if mibBuilder.loadTexts:
    rsTotalEntry.setStatus("current")


class _TotRSidx_Type(Integer32):
    """Custom type totRSidx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_TotRSidx_Type.__name__ = "Integer32"
_TotRSidx_Object = MibTableColumn
totRSidx = _TotRSidx_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 1),
    _TotRSidx_Type()
)
totRSidx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSidx.setStatus("current")


class _TotRSDesc_Type(OctetString):
    """Custom type totRSDesc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_TotRSDesc_Type.__name__ = "OctetString"
_TotRSDesc_Object = MibTableColumn
totRSDesc = _TotRSDesc_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 2),
    _TotRSDesc_Type()
)
totRSDesc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    totRSDesc.setStatus("current")
_TotRSConns_Type = Counter32
_TotRSConns_Object = MibTableColumn
totRSConns = _TotRSConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 3),
    _TotRSConns_Type()
)
totRSConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSConns.setStatus("current")
_TotRSInPkts_Type = Counter32
_TotRSInPkts_Object = MibTableColumn
totRSInPkts = _TotRSInPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 4),
    _TotRSInPkts_Type()
)
totRSInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSInPkts.setStatus("current")
_TotRSOutPkts_Type = Counter32
_TotRSOutPkts_Object = MibTableColumn
totRSOutPkts = _TotRSOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 5),
    _TotRSOutPkts_Type()
)
totRSOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSOutPkts.setStatus("current")
_TotRSInBytes_Type = Counter64
_TotRSInBytes_Object = MibTableColumn
totRSInBytes = _TotRSInBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 6),
    _TotRSInBytes_Type()
)
totRSInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSInBytes.setStatus("current")
_TotRSOutBytes_Type = Counter64
_TotRSOutBytes_Object = MibTableColumn
totRSOutBytes = _TotRSOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 7),
    _TotRSOutBytes_Type()
)
totRSOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSOutBytes.setStatus("current")
_TotRSActiveConns_Type = Counter32
_TotRSActiveConns_Object = MibTableColumn
totRSActiveConns = _TotRSActiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 8),
    _TotRSActiveConns_Type()
)
totRSActiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSActiveConns.setStatus("current")
_TotRSInactiveConns_Type = Counter32
_TotRSInactiveConns_Object = MibTableColumn
totRSInactiveConns = _TotRSInactiveConns_Object(
    (1, 3, 6, 1, 4, 1, 12196, 12, 8, 1, 9),
    _TotRSInactiveConns_Type()
)
totRSInactiveConns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totRSInactiveConns.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPVS-MIB",
    **{"ipvs": ipvs,
       "ipvsVSTable": ipvsVSTable,
       "vsEntry": vsEntry,
       "vSidx": vSidx,
       "vSDesc": vSDesc,
       "vSConns": vSConns,
       "vSInPkts": vSInPkts,
       "vSOutPkts": vSOutPkts,
       "vSInBytes": vSInBytes,
       "vSOutBytes": vSOutBytes,
       "vSActivConns": vSActivConns,
       "ipvsRSTable": ipvsRSTable,
       "rsEntry": rsEntry,
       "rSidx": rSidx,
       "rSVSidx": rSVSidx,
       "rSDesc": rSDesc,
       "rSConns": rSConns,
       "rSInPkts": rSInPkts,
       "rSOutPkts": rSOutPkts,
       "rSInBytes": rSInBytes,
       "rSOutBytes": rSOutBytes,
       "rSActiveConns": rSActiveConns,
       "rSInactiveConns": rSInactiveConns,
       "rSWeight": rSWeight,
       "conns": conns,
       "inPkts": inPkts,
       "outPkts": outPkts,
       "inBytes": inBytes,
       "outBytes": outBytes,
       "ipvsRSTotalTable": ipvsRSTotalTable,
       "rsTotalEntry": rsTotalEntry,
       "totRSidx": totRSidx,
       "totRSDesc": totRSDesc,
       "totRSConns": totRSConns,
       "totRSInPkts": totRSInPkts,
       "totRSOutPkts": totRSOutPkts,
       "totRSInBytes": totRSInBytes,
       "totRSOutBytes": totRSOutBytes,
       "totRSActiveConns": totRSActiveConns,
       "totRSInactiveConns": totRSInactiveConns}
)
