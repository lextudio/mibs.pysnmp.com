# SNMP MIB module (PERIBIT-SR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PERIBIT-SR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:27 2024
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

(pnCommonEventDescr,) = mibBuilder.importSymbols(
    "PERIBIT-COMMON-MIB",
    "pnCommonEventDescr")

(pnModules,
 pnSpecificMib) = mibBuilder.importSymbols(
    "PERIBIT-GLOBAL-REG",
    "pnModules",
    "pnSpecificMib")

(TcAppName,) = mibBuilder.importSymbols(
    "PERIBIT-GLOBAL-TC",
    "TcAppName")

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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

pnSrMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 4)
)
pnSrMibModule.setRevisions(
        ("2004-05-24 00:00",
         "2003-06-23 00:00",
         "2002-03-28 00:00",
         "2002-03-27 00:00",
         "2001-12-19 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PnSrMib_ObjectIdentity = ObjectIdentity
pnSrMib = _PnSrMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pnSrMib.setStatus("current")
_PnSrConfMib_ObjectIdentity = ObjectIdentity
pnSrConfMib = _PnSrConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pnSrConfMib.setStatus("current")
_PnSrObjs_ObjectIdentity = ObjectIdentity
pnSrObjs = _PnSrObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    pnSrObjs.setStatus("current")
_PnSrStatsUpdateTime_Type = TimeStamp
_PnSrStatsUpdateTime_Object = MibScalar
pnSrStatsUpdateTime = _PnSrStatsUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 1),
    _PnSrStatsUpdateTime_Type()
)
pnSrStatsUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrStatsUpdateTime.setStatus("current")
_PnSrStatsAsmCount_Type = Integer32
_PnSrStatsAsmCount_Object = MibScalar
pnSrStatsAsmCount = _PnSrStatsAsmCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 2),
    _PnSrStatsAsmCount_Type()
)
pnSrStatsAsmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrStatsAsmCount.setStatus("current")
_PnSrStatsAppCount_Type = Integer32
_PnSrStatsAppCount_Object = MibScalar
pnSrStatsAppCount = _PnSrStatsAppCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 3),
    _PnSrStatsAppCount_Type()
)
pnSrStatsAppCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrStatsAppCount.setStatus("current")
_PnSrSysStats_ObjectIdentity = ObjectIdentity
pnSrSysStats = _PnSrSysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    pnSrSysStats.setStatus("current")
_PnSrSysStatsBytesInAe_Type = Counter64
_PnSrSysStatsBytesInAe_Object = MibScalar
pnSrSysStatsBytesInAe = _PnSrSysStatsBytesInAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 1),
    _PnSrSysStatsBytesInAe_Type()
)
pnSrSysStatsBytesInAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesInAe.setStatus("current")
_PnSrSysStatsBytesOutAe_Type = Counter64
_PnSrSysStatsBytesOutAe_Object = MibScalar
pnSrSysStatsBytesOutAe = _PnSrSysStatsBytesOutAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 2),
    _PnSrSysStatsBytesOutAe_Type()
)
pnSrSysStatsBytesOutAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesOutAe.setStatus("current")
_PnSrSysStatsPktsInAe_Type = Counter64
_PnSrSysStatsPktsInAe_Object = MibScalar
pnSrSysStatsPktsInAe = _PnSrSysStatsPktsInAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 3),
    _PnSrSysStatsPktsInAe_Type()
)
pnSrSysStatsPktsInAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsInAe.setStatus("current")
_PnSrSysStatsPktsOutAe_Type = Counter64
_PnSrSysStatsPktsOutAe_Object = MibScalar
pnSrSysStatsPktsOutAe = _PnSrSysStatsPktsOutAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 4),
    _PnSrSysStatsPktsOutAe_Type()
)
pnSrSysStatsPktsOutAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsOutAe.setStatus("current")
_PnSrSysStatsBytesOutOob_Type = Counter64
_PnSrSysStatsBytesOutOob_Object = MibScalar
pnSrSysStatsBytesOutOob = _PnSrSysStatsBytesOutOob_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 5),
    _PnSrSysStatsBytesOutOob_Type()
)
pnSrSysStatsBytesOutOob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesOutOob.setStatus("current")
_PnSrSysStatsBytesPtNoAe_Type = Counter64
_PnSrSysStatsBytesPtNoAe_Object = MibScalar
pnSrSysStatsBytesPtNoAe = _PnSrSysStatsBytesPtNoAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 6),
    _PnSrSysStatsBytesPtNoAe_Type()
)
pnSrSysStatsBytesPtNoAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesPtNoAe.setStatus("current")
_PnSrSysStatsPktsPtNoAe_Type = Counter64
_PnSrSysStatsPktsPtNoAe_Object = MibScalar
pnSrSysStatsPktsPtNoAe = _PnSrSysStatsPktsPtNoAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 7),
    _PnSrSysStatsPktsPtNoAe_Type()
)
pnSrSysStatsPktsPtNoAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsPtNoAe.setStatus("current")
_PnSrSysStatsBytesPtFilter_Type = Counter64
_PnSrSysStatsBytesPtFilter_Object = MibScalar
pnSrSysStatsBytesPtFilter = _PnSrSysStatsBytesPtFilter_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 8),
    _PnSrSysStatsBytesPtFilter_Type()
)
pnSrSysStatsBytesPtFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesPtFilter.setStatus("current")
_PnSrSysStatsPktsPtFilter_Type = Counter64
_PnSrSysStatsPktsPtFilter_Object = MibScalar
pnSrSysStatsPktsPtFilter = _PnSrSysStatsPktsPtFilter_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 9),
    _PnSrSysStatsPktsPtFilter_Type()
)
pnSrSysStatsPktsPtFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsPtFilter.setStatus("current")
_PnSrSysStatsBytesOfPt_Type = Counter64
_PnSrSysStatsBytesOfPt_Object = MibScalar
pnSrSysStatsBytesOfPt = _PnSrSysStatsBytesOfPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 10),
    _PnSrSysStatsBytesOfPt_Type()
)
pnSrSysStatsBytesOfPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesOfPt.setStatus("current")
_PnSrSysStatsPktsOfPt_Type = Counter64
_PnSrSysStatsPktsOfPt_Object = MibScalar
pnSrSysStatsPktsOfPt = _PnSrSysStatsPktsOfPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 11),
    _PnSrSysStatsPktsOfPt_Type()
)
pnSrSysStatsPktsOfPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsOfPt.setStatus("current")
_PnSrSysStatsBytesTpIn_Type = Counter64
_PnSrSysStatsBytesTpIn_Object = MibScalar
pnSrSysStatsBytesTpIn = _PnSrSysStatsBytesTpIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 12),
    _PnSrSysStatsBytesTpIn_Type()
)
pnSrSysStatsBytesTpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesTpIn.setStatus("current")
_PnSrSysStatsPktsTpIn_Type = Counter64
_PnSrSysStatsPktsTpIn_Object = MibScalar
pnSrSysStatsPktsTpIn = _PnSrSysStatsPktsTpIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 13),
    _PnSrSysStatsPktsTpIn_Type()
)
pnSrSysStatsPktsTpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsTpIn.setStatus("current")
_PnSrSysStatsBytesTpOut_Type = Counter64
_PnSrSysStatsBytesTpOut_Object = MibScalar
pnSrSysStatsBytesTpOut = _PnSrSysStatsBytesTpOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 14),
    _PnSrSysStatsBytesTpOut_Type()
)
pnSrSysStatsBytesTpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesTpOut.setStatus("current")
_PnSrSysStatsPktsTpOut_Type = Counter64
_PnSrSysStatsPktsTpOut_Object = MibScalar
pnSrSysStatsPktsTpOut = _PnSrSysStatsPktsTpOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 15),
    _PnSrSysStatsPktsTpOut_Type()
)
pnSrSysStatsPktsTpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsTpOut.setStatus("current")
_PnSrSysStatsBytesTpPt_Type = Counter64
_PnSrSysStatsBytesTpPt_Object = MibScalar
pnSrSysStatsBytesTpPt = _PnSrSysStatsBytesTpPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 16),
    _PnSrSysStatsBytesTpPt_Type()
)
pnSrSysStatsBytesTpPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesTpPt.setStatus("current")
_PnSrSysStatsPktsTpPt_Type = Counter64
_PnSrSysStatsPktsTpPt_Object = MibScalar
pnSrSysStatsPktsTpPt = _PnSrSysStatsPktsTpPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 17),
    _PnSrSysStatsPktsTpPt_Type()
)
pnSrSysStatsPktsTpPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsTpPt.setStatus("current")
_PnSrSysStatsPeakRdn_Type = Unsigned32
_PnSrSysStatsPeakRdn_Object = MibScalar
pnSrSysStatsPeakRdn = _PnSrSysStatsPeakRdn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 18),
    _PnSrSysStatsPeakRdn_Type()
)
pnSrSysStatsPeakRdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPeakRdn.setStatus("current")
_PnSrSysStatsThruputIn_Type = Gauge32
_PnSrSysStatsThruputIn_Object = MibScalar
pnSrSysStatsThruputIn = _PnSrSysStatsThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 19),
    _PnSrSysStatsThruputIn_Type()
)
pnSrSysStatsThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsThruputIn.setStatus("current")
_PnSrSysStatsThruputOut_Type = Gauge32
_PnSrSysStatsThruputOut_Object = MibScalar
pnSrSysStatsThruputOut = _PnSrSysStatsThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 20),
    _PnSrSysStatsThruputOut_Type()
)
pnSrSysStatsThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsThruputOut.setStatus("current")
_PnSrSysStatsBytesInRe_Type = Counter64
_PnSrSysStatsBytesInRe_Object = MibScalar
pnSrSysStatsBytesInRe = _PnSrSysStatsBytesInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 21),
    _PnSrSysStatsBytesInRe_Type()
)
pnSrSysStatsBytesInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesInRe.setStatus("current")
_PnSrSysStatsBytesOutRe_Type = Counter64
_PnSrSysStatsBytesOutRe_Object = MibScalar
pnSrSysStatsBytesOutRe = _PnSrSysStatsBytesOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 22),
    _PnSrSysStatsBytesOutRe_Type()
)
pnSrSysStatsBytesOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsBytesOutRe.setStatus("current")
_PnSrSysStatsPktsInRe_Type = Counter64
_PnSrSysStatsPktsInRe_Object = MibScalar
pnSrSysStatsPktsInRe = _PnSrSysStatsPktsInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 23),
    _PnSrSysStatsPktsInRe_Type()
)
pnSrSysStatsPktsInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsInRe.setStatus("current")
_PnSrSysStatsPktsOutRe_Type = Counter64
_PnSrSysStatsPktsOutRe_Object = MibScalar
pnSrSysStatsPktsOutRe = _PnSrSysStatsPktsOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 24),
    _PnSrSysStatsPktsOutRe_Type()
)
pnSrSysStatsPktsOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrSysStatsPktsOutRe.setStatus("current")
_PnSrAsm_ObjectIdentity = ObjectIdentity
pnSrAsm = _PnSrAsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    pnSrAsm.setStatus("current")
_PnSrAsmTable_Object = MibTable
pnSrAsmTable = _PnSrAsmTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pnSrAsmTable.setStatus("current")
_PnSrAsmEntry_Object = MibTableRow
pnSrAsmEntry = _PnSrAsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1)
)
pnSrAsmEntry.setIndexNames(
    (0, "PERIBIT-SR-MIB", "pnSrAsmIndex"),
)
if mibBuilder.loadTexts:
    pnSrAsmEntry.setStatus("current")
_PnSrAsmIndex_Type = Integer32
_PnSrAsmIndex_Object = MibTableColumn
pnSrAsmIndex = _PnSrAsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1, 1),
    _PnSrAsmIndex_Type()
)
pnSrAsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnSrAsmIndex.setStatus("current")
_PnSrAsmIpAddress_Type = IpAddress
_PnSrAsmIpAddress_Object = MibTableColumn
pnSrAsmIpAddress = _PnSrAsmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1, 2),
    _PnSrAsmIpAddress_Type()
)
pnSrAsmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAsmIpAddress.setStatus("current")
_PnSrAsmStatsTable_Object = MibTable
pnSrAsmStatsTable = _PnSrAsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    pnSrAsmStatsTable.setStatus("current")
_PnSrAsmStatsEntry_Object = MibTableRow
pnSrAsmStatsEntry = _PnSrAsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    pnSrAsmStatsEntry.setStatus("current")
_PnSrAsmStatsPktsIn_Type = Counter64
_PnSrAsmStatsPktsIn_Object = MibTableColumn
pnSrAsmStatsPktsIn = _PnSrAsmStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 1),
    _PnSrAsmStatsPktsIn_Type()
)
pnSrAsmStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAsmStatsPktsIn.setStatus("current")
_PnSrAsmStatsPktsOut_Type = Counter64
_PnSrAsmStatsPktsOut_Object = MibTableColumn
pnSrAsmStatsPktsOut = _PnSrAsmStatsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 2),
    _PnSrAsmStatsPktsOut_Type()
)
pnSrAsmStatsPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAsmStatsPktsOut.setStatus("current")
_PnSrAsmStatsBytesIn_Type = Counter64
_PnSrAsmStatsBytesIn_Object = MibTableColumn
pnSrAsmStatsBytesIn = _PnSrAsmStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 3),
    _PnSrAsmStatsBytesIn_Type()
)
pnSrAsmStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAsmStatsBytesIn.setStatus("current")
_PnSrAsmStatsBytesOut_Type = Counter64
_PnSrAsmStatsBytesOut_Object = MibTableColumn
pnSrAsmStatsBytesOut = _PnSrAsmStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 4),
    _PnSrAsmStatsBytesOut_Type()
)
pnSrAsmStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAsmStatsBytesOut.setStatus("current")
_PnSrApp_ObjectIdentity = ObjectIdentity
pnSrApp = _PnSrApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    pnSrApp.setStatus("current")
_PnSrAppTable_Object = MibTable
pnSrAppTable = _PnSrAppTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pnSrAppTable.setStatus("current")
_PnSrAppEntry_Object = MibTableRow
pnSrAppEntry = _PnSrAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1)
)
pnSrAppEntry.setIndexNames(
    (0, "PERIBIT-SR-MIB", "pnSrAppIndex"),
)
if mibBuilder.loadTexts:
    pnSrAppEntry.setStatus("current")
_PnSrAppIndex_Type = Integer32
_PnSrAppIndex_Object = MibTableColumn
pnSrAppIndex = _PnSrAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1, 1),
    _PnSrAppIndex_Type()
)
pnSrAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pnSrAppIndex.setStatus("current")
_PnSrAppAppName_Type = TcAppName
_PnSrAppAppName_Object = MibTableColumn
pnSrAppAppName = _PnSrAppAppName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1, 2),
    _PnSrAppAppName_Type()
)
pnSrAppAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppAppName.setStatus("current")
_PnSrAppStatsTable_Object = MibTable
pnSrAppStatsTable = _PnSrAppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    pnSrAppStatsTable.setStatus("current")
_PnSrAppStatsEntry_Object = MibTableRow
pnSrAppStatsEntry = _PnSrAppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1)
)
pnSrAppStatsEntry.setIndexNames(
    (0, "PERIBIT-SR-MIB", "pnSrAsmIndex"),
    (0, "PERIBIT-SR-MIB", "pnSrAppIndex"),
)
if mibBuilder.loadTexts:
    pnSrAppStatsEntry.setStatus("current")
_PnSrAppStatsBytesIn_Type = Counter64
_PnSrAppStatsBytesIn_Object = MibTableColumn
pnSrAppStatsBytesIn = _PnSrAppStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 1),
    _PnSrAppStatsBytesIn_Type()
)
pnSrAppStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppStatsBytesIn.setStatus("current")
_PnSrAppStatsBytesOut_Type = Counter64
_PnSrAppStatsBytesOut_Object = MibTableColumn
pnSrAppStatsBytesOut = _PnSrAppStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 2),
    _PnSrAppStatsBytesOut_Type()
)
pnSrAppStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppStatsBytesOut.setStatus("current")
_PnSrAppStatsBytesInPercent_Type = Gauge32
_PnSrAppStatsBytesInPercent_Object = MibTableColumn
pnSrAppStatsBytesInPercent = _PnSrAppStatsBytesInPercent_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 3),
    _PnSrAppStatsBytesInPercent_Type()
)
pnSrAppStatsBytesInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppStatsBytesInPercent.setStatus("current")
_PnSrAppStatsAppName_Type = TcAppName
_PnSrAppStatsAppName_Object = MibTableColumn
pnSrAppStatsAppName = _PnSrAppStatsAppName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 4),
    _PnSrAppStatsAppName_Type()
)
pnSrAppStatsAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppStatsAppName.setStatus("current")
_PnSrAppAggrStatsTable_Object = MibTable
pnSrAppAggrStatsTable = _PnSrAppAggrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    pnSrAppAggrStatsTable.setStatus("current")
_PnSrAppAggrStatsEntry_Object = MibTableRow
pnSrAppAggrStatsEntry = _PnSrAppAggrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    pnSrAppAggrStatsEntry.setStatus("current")
_PnSrAppAggrStatsBytesInRe_Type = Counter64
_PnSrAppAggrStatsBytesInRe_Object = MibTableColumn
pnSrAppAggrStatsBytesInRe = _PnSrAppAggrStatsBytesInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 1),
    _PnSrAppAggrStatsBytesInRe_Type()
)
pnSrAppAggrStatsBytesInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppAggrStatsBytesInRe.setStatus("current")
_PnSrAppAggrStatsBytesOutRe_Type = Counter64
_PnSrAppAggrStatsBytesOutRe_Object = MibTableColumn
pnSrAppAggrStatsBytesOutRe = _PnSrAppAggrStatsBytesOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 2),
    _PnSrAppAggrStatsBytesOutRe_Type()
)
pnSrAppAggrStatsBytesOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppAggrStatsBytesOutRe.setStatus("current")
_PnSrAppAggrStatsBytesInPercent_Type = Gauge32
_PnSrAppAggrStatsBytesInPercent_Object = MibTableColumn
pnSrAppAggrStatsBytesInPercent = _PnSrAppAggrStatsBytesInPercent_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 3),
    _PnSrAppAggrStatsBytesInPercent_Type()
)
pnSrAppAggrStatsBytesInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrAppAggrStatsBytesInPercent.setStatus("current")
_PnSrBurstStats_ObjectIdentity = ObjectIdentity
pnSrBurstStats = _PnSrBurstStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    pnSrBurstStats.setStatus("current")
_PnSrBurstStatsStartTime_Type = Integer32
_PnSrBurstStatsStartTime_Object = MibScalar
pnSrBurstStatsStartTime = _PnSrBurstStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 1),
    _PnSrBurstStatsStartTime_Type()
)
pnSrBurstStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrBurstStatsStartTime.setStatus("current")
_PnSrBurstStatsBpsIn_Type = Gauge32
_PnSrBurstStatsBpsIn_Object = MibScalar
pnSrBurstStatsBpsIn = _PnSrBurstStatsBpsIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 2),
    _PnSrBurstStatsBpsIn_Type()
)
pnSrBurstStatsBpsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrBurstStatsBpsIn.setStatus("current")
_PnSrBurstStatsBpsOut_Type = Gauge32
_PnSrBurstStatsBpsOut_Object = MibScalar
pnSrBurstStatsBpsOut = _PnSrBurstStatsBpsOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 3),
    _PnSrBurstStatsBpsOut_Type()
)
pnSrBurstStatsBpsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrBurstStatsBpsOut.setStatus("current")
_PnSrBurstStatsBpsPt_Type = Gauge32
_PnSrBurstStatsBpsPt_Object = MibScalar
pnSrBurstStatsBpsPt = _PnSrBurstStatsBpsPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 4),
    _PnSrBurstStatsBpsPt_Type()
)
pnSrBurstStatsBpsPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pnSrBurstStatsBpsPt.setStatus("current")
_PnSrEvents_ObjectIdentity = ObjectIdentity
pnSrEvents = _PnSrEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    pnSrEvents.setStatus("current")
_PnSrEventObjs_ObjectIdentity = ObjectIdentity
pnSrEventObjs = _PnSrEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pnSrEventObjs.setStatus("current")
_PnSrEventEvents_ObjectIdentity = ObjectIdentity
pnSrEventEvents = _PnSrEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    pnSrEventEvents.setStatus("current")
_PnSrEventEventsV2_ObjectIdentity = ObjectIdentity
pnSrEventEventsV2 = _PnSrEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    pnSrEventEventsV2.setStatus("current")
pnSrAsmEntry.registerAugmentions(
    ("PERIBIT-SR-MIB",
     "pnSrAsmStatsEntry")
)
pnSrAsmStatsEntry.setIndexNames(*pnSrAsmEntry.getIndexNames())
pnSrAppEntry.registerAugmentions(
    ("PERIBIT-SR-MIB",
     "pnSrAppAggrStatsEntry")
)
pnSrAppAggrStatsEntry.setIndexNames(*pnSrAppEntry.getIndexNames())

# Managed Objects groups


# Notification objects

pnSrEventRipAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 1)
)
pnSrEventRipAuthFailure.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventRipAuthFailure.setStatus(
        "current"
    )

pnSrEventReducerBufferOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 2)
)
pnSrEventReducerBufferOverflow.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventReducerBufferOverflow.setStatus(
        "current"
    )

pnSrEventReducerSessionClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 3)
)
pnSrEventReducerSessionClosed.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventReducerSessionClosed.setStatus(
        "current"
    )

pnSrEventAssemblerSessionClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 4)
)
pnSrEventAssemblerSessionClosed.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventAssemblerSessionClosed.setStatus(
        "current"
    )

pnSrEventReducerSessionOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 5)
)
pnSrEventReducerSessionOpened.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventReducerSessionOpened.setStatus(
        "current"
    )

pnSrEventAssemblerSessionOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 6)
)
pnSrEventAssemblerSessionOpened.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventAssemblerSessionOpened.setStatus(
        "current"
    )

pnSrEventPrimaryRegServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 7)
)
pnSrEventPrimaryRegServerUnreachable.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventPrimaryRegServerUnreachable.setStatus(
        "current"
    )

pnSrEventSecondaryRegServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 8)
)
pnSrEventSecondaryRegServerUnreachable.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventSecondaryRegServerUnreachable.setStatus(
        "current"
    )

pnSrEventMultiNodeMasterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 9)
)
pnSrEventMultiNodeMasterUp.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventMultiNodeMasterUp.setStatus(
        "current"
    )

pnSrEventMultiNodeMasterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 10)
)
pnSrEventMultiNodeMasterDown.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventMultiNodeMasterDown.setStatus(
        "current"
    )

pnSrEventMultiNodeLastUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 11)
)
pnSrEventMultiNodeLastUp.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventMultiNodeLastUp.setStatus(
        "current"
    )

pnSrEventMultiNodeLastDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 12)
)
pnSrEventMultiNodeLastDown.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventMultiNodeLastDown.setStatus(
        "current"
    )

pnSrEventPrimaryDownBackupEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 13)
)
pnSrEventPrimaryDownBackupEngaged.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventPrimaryDownBackupEngaged.setStatus(
        "current"
    )

pnSrEventPrimaryDownBackupEngageFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 14)
)
pnSrEventPrimaryDownBackupEngageFailed.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventPrimaryDownBackupEngageFailed.setStatus(
        "current"
    )

pnSrEventPrimaryUpBackupDisengaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 15)
)
pnSrEventPrimaryUpBackupDisengaged.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventPrimaryUpBackupDisengaged.setStatus(
        "current"
    )

pnSrEventMultiPathStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 16)
)
pnSrEventMultiPathStatusChange.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventMultiPathStatusChange.setStatus(
        "current"
    )

pnSrEventDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 17)
)
pnSrEventDiskFailure.setObjects(
    ("PERIBIT-COMMON-MIB", "pnCommonEventDescr")
)
if mibBuilder.loadTexts:
    pnSrEventDiskFailure.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PERIBIT-SR-MIB",
    **{"pnSrMibModule": pnSrMibModule,
       "pnSrMib": pnSrMib,
       "pnSrConfMib": pnSrConfMib,
       "pnSrObjs": pnSrObjs,
       "pnSrStatsUpdateTime": pnSrStatsUpdateTime,
       "pnSrStatsAsmCount": pnSrStatsAsmCount,
       "pnSrStatsAppCount": pnSrStatsAppCount,
       "pnSrSysStats": pnSrSysStats,
       "pnSrSysStatsBytesInAe": pnSrSysStatsBytesInAe,
       "pnSrSysStatsBytesOutAe": pnSrSysStatsBytesOutAe,
       "pnSrSysStatsPktsInAe": pnSrSysStatsPktsInAe,
       "pnSrSysStatsPktsOutAe": pnSrSysStatsPktsOutAe,
       "pnSrSysStatsBytesOutOob": pnSrSysStatsBytesOutOob,
       "pnSrSysStatsBytesPtNoAe": pnSrSysStatsBytesPtNoAe,
       "pnSrSysStatsPktsPtNoAe": pnSrSysStatsPktsPtNoAe,
       "pnSrSysStatsBytesPtFilter": pnSrSysStatsBytesPtFilter,
       "pnSrSysStatsPktsPtFilter": pnSrSysStatsPktsPtFilter,
       "pnSrSysStatsBytesOfPt": pnSrSysStatsBytesOfPt,
       "pnSrSysStatsPktsOfPt": pnSrSysStatsPktsOfPt,
       "pnSrSysStatsBytesTpIn": pnSrSysStatsBytesTpIn,
       "pnSrSysStatsPktsTpIn": pnSrSysStatsPktsTpIn,
       "pnSrSysStatsBytesTpOut": pnSrSysStatsBytesTpOut,
       "pnSrSysStatsPktsTpOut": pnSrSysStatsPktsTpOut,
       "pnSrSysStatsBytesTpPt": pnSrSysStatsBytesTpPt,
       "pnSrSysStatsPktsTpPt": pnSrSysStatsPktsTpPt,
       "pnSrSysStatsPeakRdn": pnSrSysStatsPeakRdn,
       "pnSrSysStatsThruputIn": pnSrSysStatsThruputIn,
       "pnSrSysStatsThruputOut": pnSrSysStatsThruputOut,
       "pnSrSysStatsBytesInRe": pnSrSysStatsBytesInRe,
       "pnSrSysStatsBytesOutRe": pnSrSysStatsBytesOutRe,
       "pnSrSysStatsPktsInRe": pnSrSysStatsPktsInRe,
       "pnSrSysStatsPktsOutRe": pnSrSysStatsPktsOutRe,
       "pnSrAsm": pnSrAsm,
       "pnSrAsmTable": pnSrAsmTable,
       "pnSrAsmEntry": pnSrAsmEntry,
       "pnSrAsmIndex": pnSrAsmIndex,
       "pnSrAsmIpAddress": pnSrAsmIpAddress,
       "pnSrAsmStatsTable": pnSrAsmStatsTable,
       "pnSrAsmStatsEntry": pnSrAsmStatsEntry,
       "pnSrAsmStatsPktsIn": pnSrAsmStatsPktsIn,
       "pnSrAsmStatsPktsOut": pnSrAsmStatsPktsOut,
       "pnSrAsmStatsBytesIn": pnSrAsmStatsBytesIn,
       "pnSrAsmStatsBytesOut": pnSrAsmStatsBytesOut,
       "pnSrApp": pnSrApp,
       "pnSrAppTable": pnSrAppTable,
       "pnSrAppEntry": pnSrAppEntry,
       "pnSrAppIndex": pnSrAppIndex,
       "pnSrAppAppName": pnSrAppAppName,
       "pnSrAppStatsTable": pnSrAppStatsTable,
       "pnSrAppStatsEntry": pnSrAppStatsEntry,
       "pnSrAppStatsBytesIn": pnSrAppStatsBytesIn,
       "pnSrAppStatsBytesOut": pnSrAppStatsBytesOut,
       "pnSrAppStatsBytesInPercent": pnSrAppStatsBytesInPercent,
       "pnSrAppStatsAppName": pnSrAppStatsAppName,
       "pnSrAppAggrStatsTable": pnSrAppAggrStatsTable,
       "pnSrAppAggrStatsEntry": pnSrAppAggrStatsEntry,
       "pnSrAppAggrStatsBytesInRe": pnSrAppAggrStatsBytesInRe,
       "pnSrAppAggrStatsBytesOutRe": pnSrAppAggrStatsBytesOutRe,
       "pnSrAppAggrStatsBytesInPercent": pnSrAppAggrStatsBytesInPercent,
       "pnSrBurstStats": pnSrBurstStats,
       "pnSrBurstStatsStartTime": pnSrBurstStatsStartTime,
       "pnSrBurstStatsBpsIn": pnSrBurstStatsBpsIn,
       "pnSrBurstStatsBpsOut": pnSrBurstStatsBpsOut,
       "pnSrBurstStatsBpsPt": pnSrBurstStatsBpsPt,
       "pnSrEvents": pnSrEvents,
       "pnSrEventObjs": pnSrEventObjs,
       "pnSrEventEvents": pnSrEventEvents,
       "pnSrEventEventsV2": pnSrEventEventsV2,
       "pnSrEventRipAuthFailure": pnSrEventRipAuthFailure,
       "pnSrEventReducerBufferOverflow": pnSrEventReducerBufferOverflow,
       "pnSrEventReducerSessionClosed": pnSrEventReducerSessionClosed,
       "pnSrEventAssemblerSessionClosed": pnSrEventAssemblerSessionClosed,
       "pnSrEventReducerSessionOpened": pnSrEventReducerSessionOpened,
       "pnSrEventAssemblerSessionOpened": pnSrEventAssemblerSessionOpened,
       "pnSrEventPrimaryRegServerUnreachable": pnSrEventPrimaryRegServerUnreachable,
       "pnSrEventSecondaryRegServerUnreachable": pnSrEventSecondaryRegServerUnreachable,
       "pnSrEventMultiNodeMasterUp": pnSrEventMultiNodeMasterUp,
       "pnSrEventMultiNodeMasterDown": pnSrEventMultiNodeMasterDown,
       "pnSrEventMultiNodeLastUp": pnSrEventMultiNodeLastUp,
       "pnSrEventMultiNodeLastDown": pnSrEventMultiNodeLastDown,
       "pnSrEventPrimaryDownBackupEngaged": pnSrEventPrimaryDownBackupEngaged,
       "pnSrEventPrimaryDownBackupEngageFailed": pnSrEventPrimaryDownBackupEngageFailed,
       "pnSrEventPrimaryUpBackupDisengaged": pnSrEventPrimaryUpBackupDisengaged,
       "pnSrEventMultiPathStatusChange": pnSrEventMultiPathStatusChange,
       "pnSrEventDiskFailure": pnSrEventDiskFailure}
)
