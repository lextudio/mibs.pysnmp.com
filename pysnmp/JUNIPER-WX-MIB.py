# SNMP MIB module (JUNIPER-WX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-WX-GLOBAL-REG
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:30 2024
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

(jnxWxCommonEventDescr,) = mibBuilder.importSymbols(
    "JUNIPER-WX-COMMON-MIB",
    "jnxWxCommonEventDescr")

(jnxWxModules,
 jnxWxSpecificMib) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-REG",
    "jnxWxModules",
    "jnxWxSpecificMib")

(TcAppName,
 TcQosIdentifier) = mibBuilder.importSymbols(
    "JUNIPER-WX-GLOBAL-TC",
    "TcAppName",
    "TcQosIdentifier")

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

jnxWxMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 1, 1, 4)
)
jnxWxMibModule.setRevisions(
        ("2004-05-24 00:00",
         "2003-06-23 00:00",
         "2002-03-28 00:00",
         "2002-03-27 00:00",
         "2001-12-19 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxWxMib_ObjectIdentity = ObjectIdentity
jnxWxMib = _JnxWxMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWxMib.setStatus("current")
_JnxWxConfMib_ObjectIdentity = ObjectIdentity
jnxWxConfMib = _JnxWxConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxWxConfMib.setStatus("current")
_JnxWxObjs_ObjectIdentity = ObjectIdentity
jnxWxObjs = _JnxWxObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jnxWxObjs.setStatus("current")
_JnxWxStatsUpdateTime_Type = TimeStamp
_JnxWxStatsUpdateTime_Object = MibScalar
jnxWxStatsUpdateTime = _JnxWxStatsUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 1),
    _JnxWxStatsUpdateTime_Type()
)
jnxWxStatsUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsUpdateTime.setStatus("current")
_JnxWxStatsAsmCount_Type = Integer32
_JnxWxStatsAsmCount_Object = MibScalar
jnxWxStatsAsmCount = _JnxWxStatsAsmCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 2),
    _JnxWxStatsAsmCount_Type()
)
jnxWxStatsAsmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsAsmCount.setStatus("current")
_JnxWxStatsAppCount_Type = Integer32
_JnxWxStatsAppCount_Object = MibScalar
jnxWxStatsAppCount = _JnxWxStatsAppCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 3),
    _JnxWxStatsAppCount_Type()
)
jnxWxStatsAppCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsAppCount.setStatus("current")
_JnxWxSysStats_ObjectIdentity = ObjectIdentity
jnxWxSysStats = _JnxWxSysStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    jnxWxSysStats.setStatus("current")
_JnxWxSysStatsBytesInAe_Type = Counter64
_JnxWxSysStatsBytesInAe_Object = MibScalar
jnxWxSysStatsBytesInAe = _JnxWxSysStatsBytesInAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 1),
    _JnxWxSysStatsBytesInAe_Type()
)
jnxWxSysStatsBytesInAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesInAe.setStatus("current")
_JnxWxSysStatsBytesOutAe_Type = Counter64
_JnxWxSysStatsBytesOutAe_Object = MibScalar
jnxWxSysStatsBytesOutAe = _JnxWxSysStatsBytesOutAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 2),
    _JnxWxSysStatsBytesOutAe_Type()
)
jnxWxSysStatsBytesOutAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesOutAe.setStatus("current")
_JnxWxSysStatsPktsInAe_Type = Counter64
_JnxWxSysStatsPktsInAe_Object = MibScalar
jnxWxSysStatsPktsInAe = _JnxWxSysStatsPktsInAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 3),
    _JnxWxSysStatsPktsInAe_Type()
)
jnxWxSysStatsPktsInAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsInAe.setStatus("current")
_JnxWxSysStatsPktsOutAe_Type = Counter64
_JnxWxSysStatsPktsOutAe_Object = MibScalar
jnxWxSysStatsPktsOutAe = _JnxWxSysStatsPktsOutAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 4),
    _JnxWxSysStatsPktsOutAe_Type()
)
jnxWxSysStatsPktsOutAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsOutAe.setStatus("current")
_JnxWxSysStatsBytesOutOob_Type = Counter64
_JnxWxSysStatsBytesOutOob_Object = MibScalar
jnxWxSysStatsBytesOutOob = _JnxWxSysStatsBytesOutOob_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 5),
    _JnxWxSysStatsBytesOutOob_Type()
)
jnxWxSysStatsBytesOutOob.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesOutOob.setStatus("current")
_JnxWxSysStatsBytesPtNoAe_Type = Counter64
_JnxWxSysStatsBytesPtNoAe_Object = MibScalar
jnxWxSysStatsBytesPtNoAe = _JnxWxSysStatsBytesPtNoAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 6),
    _JnxWxSysStatsBytesPtNoAe_Type()
)
jnxWxSysStatsBytesPtNoAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesPtNoAe.setStatus("current")
_JnxWxSysStatsPktsPtNoAe_Type = Counter64
_JnxWxSysStatsPktsPtNoAe_Object = MibScalar
jnxWxSysStatsPktsPtNoAe = _JnxWxSysStatsPktsPtNoAe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 7),
    _JnxWxSysStatsPktsPtNoAe_Type()
)
jnxWxSysStatsPktsPtNoAe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsPtNoAe.setStatus("current")
_JnxWxSysStatsBytesPtFilter_Type = Counter64
_JnxWxSysStatsBytesPtFilter_Object = MibScalar
jnxWxSysStatsBytesPtFilter = _JnxWxSysStatsBytesPtFilter_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 8),
    _JnxWxSysStatsBytesPtFilter_Type()
)
jnxWxSysStatsBytesPtFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesPtFilter.setStatus("current")
_JnxWxSysStatsPktsPtFilter_Type = Counter64
_JnxWxSysStatsPktsPtFilter_Object = MibScalar
jnxWxSysStatsPktsPtFilter = _JnxWxSysStatsPktsPtFilter_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 9),
    _JnxWxSysStatsPktsPtFilter_Type()
)
jnxWxSysStatsPktsPtFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsPtFilter.setStatus("current")
_JnxWxSysStatsBytesOfPt_Type = Counter64
_JnxWxSysStatsBytesOfPt_Object = MibScalar
jnxWxSysStatsBytesOfPt = _JnxWxSysStatsBytesOfPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 10),
    _JnxWxSysStatsBytesOfPt_Type()
)
jnxWxSysStatsBytesOfPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesOfPt.setStatus("current")
_JnxWxSysStatsPktsOfPt_Type = Counter64
_JnxWxSysStatsPktsOfPt_Object = MibScalar
jnxWxSysStatsPktsOfPt = _JnxWxSysStatsPktsOfPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 11),
    _JnxWxSysStatsPktsOfPt_Type()
)
jnxWxSysStatsPktsOfPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsOfPt.setStatus("current")
_JnxWxSysStatsBytesTpIn_Type = Counter64
_JnxWxSysStatsBytesTpIn_Object = MibScalar
jnxWxSysStatsBytesTpIn = _JnxWxSysStatsBytesTpIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 12),
    _JnxWxSysStatsBytesTpIn_Type()
)
jnxWxSysStatsBytesTpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesTpIn.setStatus("current")
_JnxWxSysStatsPktsTpIn_Type = Counter64
_JnxWxSysStatsPktsTpIn_Object = MibScalar
jnxWxSysStatsPktsTpIn = _JnxWxSysStatsPktsTpIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 13),
    _JnxWxSysStatsPktsTpIn_Type()
)
jnxWxSysStatsPktsTpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsTpIn.setStatus("current")
_JnxWxSysStatsBytesTpOut_Type = Counter64
_JnxWxSysStatsBytesTpOut_Object = MibScalar
jnxWxSysStatsBytesTpOut = _JnxWxSysStatsBytesTpOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 14),
    _JnxWxSysStatsBytesTpOut_Type()
)
jnxWxSysStatsBytesTpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesTpOut.setStatus("current")
_JnxWxSysStatsPktsTpOut_Type = Counter64
_JnxWxSysStatsPktsTpOut_Object = MibScalar
jnxWxSysStatsPktsTpOut = _JnxWxSysStatsPktsTpOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 15),
    _JnxWxSysStatsPktsTpOut_Type()
)
jnxWxSysStatsPktsTpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsTpOut.setStatus("current")
_JnxWxSysStatsBytesTpPt_Type = Counter64
_JnxWxSysStatsBytesTpPt_Object = MibScalar
jnxWxSysStatsBytesTpPt = _JnxWxSysStatsBytesTpPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 16),
    _JnxWxSysStatsBytesTpPt_Type()
)
jnxWxSysStatsBytesTpPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesTpPt.setStatus("current")
_JnxWxSysStatsPktsTpPt_Type = Counter64
_JnxWxSysStatsPktsTpPt_Object = MibScalar
jnxWxSysStatsPktsTpPt = _JnxWxSysStatsPktsTpPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 17),
    _JnxWxSysStatsPktsTpPt_Type()
)
jnxWxSysStatsPktsTpPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsTpPt.setStatus("current")
_JnxWxSysStatsPeakRdn_Type = Unsigned32
_JnxWxSysStatsPeakRdn_Object = MibScalar
jnxWxSysStatsPeakRdn = _JnxWxSysStatsPeakRdn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 18),
    _JnxWxSysStatsPeakRdn_Type()
)
jnxWxSysStatsPeakRdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPeakRdn.setStatus("current")
_JnxWxSysStatsThruputIn_Type = Gauge32
_JnxWxSysStatsThruputIn_Object = MibScalar
jnxWxSysStatsThruputIn = _JnxWxSysStatsThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 19),
    _JnxWxSysStatsThruputIn_Type()
)
jnxWxSysStatsThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsThruputIn.setStatus("current")
_JnxWxSysStatsThruputOut_Type = Gauge32
_JnxWxSysStatsThruputOut_Object = MibScalar
jnxWxSysStatsThruputOut = _JnxWxSysStatsThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 20),
    _JnxWxSysStatsThruputOut_Type()
)
jnxWxSysStatsThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsThruputOut.setStatus("current")
_JnxWxSysStatsBytesInRe_Type = Counter64
_JnxWxSysStatsBytesInRe_Object = MibScalar
jnxWxSysStatsBytesInRe = _JnxWxSysStatsBytesInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 21),
    _JnxWxSysStatsBytesInRe_Type()
)
jnxWxSysStatsBytesInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesInRe.setStatus("current")
_JnxWxSysStatsBytesOutRe_Type = Counter64
_JnxWxSysStatsBytesOutRe_Object = MibScalar
jnxWxSysStatsBytesOutRe = _JnxWxSysStatsBytesOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 22),
    _JnxWxSysStatsBytesOutRe_Type()
)
jnxWxSysStatsBytesOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsBytesOutRe.setStatus("current")
_JnxWxSysStatsPktsInRe_Type = Counter64
_JnxWxSysStatsPktsInRe_Object = MibScalar
jnxWxSysStatsPktsInRe = _JnxWxSysStatsPktsInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 23),
    _JnxWxSysStatsPktsInRe_Type()
)
jnxWxSysStatsPktsInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsInRe.setStatus("current")
_JnxWxSysStatsPktsOutRe_Type = Counter64
_JnxWxSysStatsPktsOutRe_Object = MibScalar
jnxWxSysStatsPktsOutRe = _JnxWxSysStatsPktsOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 24),
    _JnxWxSysStatsPktsOutRe_Type()
)
jnxWxSysStatsPktsOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktsOutRe.setStatus("current")
_JnxWxSysStatsPktSizeIn1_Type = Counter64
_JnxWxSysStatsPktSizeIn1_Object = MibScalar
jnxWxSysStatsPktSizeIn1 = _JnxWxSysStatsPktSizeIn1_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 25),
    _JnxWxSysStatsPktSizeIn1_Type()
)
jnxWxSysStatsPktSizeIn1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn1.setStatus("current")
_JnxWxSysStatsPktSizeIn2_Type = Counter64
_JnxWxSysStatsPktSizeIn2_Object = MibScalar
jnxWxSysStatsPktSizeIn2 = _JnxWxSysStatsPktSizeIn2_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 26),
    _JnxWxSysStatsPktSizeIn2_Type()
)
jnxWxSysStatsPktSizeIn2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn2.setStatus("current")
_JnxWxSysStatsPktSizeIn3_Type = Counter64
_JnxWxSysStatsPktSizeIn3_Object = MibScalar
jnxWxSysStatsPktSizeIn3 = _JnxWxSysStatsPktSizeIn3_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 27),
    _JnxWxSysStatsPktSizeIn3_Type()
)
jnxWxSysStatsPktSizeIn3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn3.setStatus("current")
_JnxWxSysStatsPktSizeIn4_Type = Counter64
_JnxWxSysStatsPktSizeIn4_Object = MibScalar
jnxWxSysStatsPktSizeIn4 = _JnxWxSysStatsPktSizeIn4_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 28),
    _JnxWxSysStatsPktSizeIn4_Type()
)
jnxWxSysStatsPktSizeIn4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn4.setStatus("current")
_JnxWxSysStatsPktSizeIn5_Type = Counter64
_JnxWxSysStatsPktSizeIn5_Object = MibScalar
jnxWxSysStatsPktSizeIn5 = _JnxWxSysStatsPktSizeIn5_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 29),
    _JnxWxSysStatsPktSizeIn5_Type()
)
jnxWxSysStatsPktSizeIn5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn5.setStatus("current")
_JnxWxSysStatsPktSizeIn6_Type = Counter64
_JnxWxSysStatsPktSizeIn6_Object = MibScalar
jnxWxSysStatsPktSizeIn6 = _JnxWxSysStatsPktSizeIn6_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 30),
    _JnxWxSysStatsPktSizeIn6_Type()
)
jnxWxSysStatsPktSizeIn6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeIn6.setStatus("current")
_JnxWxSysStatsPktSizeOut1_Type = Counter64
_JnxWxSysStatsPktSizeOut1_Object = MibScalar
jnxWxSysStatsPktSizeOut1 = _JnxWxSysStatsPktSizeOut1_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 31),
    _JnxWxSysStatsPktSizeOut1_Type()
)
jnxWxSysStatsPktSizeOut1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut1.setStatus("current")
_JnxWxSysStatsPktSizeOut2_Type = Counter64
_JnxWxSysStatsPktSizeOut2_Object = MibScalar
jnxWxSysStatsPktSizeOut2 = _JnxWxSysStatsPktSizeOut2_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 32),
    _JnxWxSysStatsPktSizeOut2_Type()
)
jnxWxSysStatsPktSizeOut2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut2.setStatus("current")
_JnxWxSysStatsPktSizeOut3_Type = Counter64
_JnxWxSysStatsPktSizeOut3_Object = MibScalar
jnxWxSysStatsPktSizeOut3 = _JnxWxSysStatsPktSizeOut3_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 33),
    _JnxWxSysStatsPktSizeOut3_Type()
)
jnxWxSysStatsPktSizeOut3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut3.setStatus("current")
_JnxWxSysStatsPktSizeOut4_Type = Counter64
_JnxWxSysStatsPktSizeOut4_Object = MibScalar
jnxWxSysStatsPktSizeOut4 = _JnxWxSysStatsPktSizeOut4_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 34),
    _JnxWxSysStatsPktSizeOut4_Type()
)
jnxWxSysStatsPktSizeOut4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut4.setStatus("current")
_JnxWxSysStatsPktSizeOut5_Type = Counter64
_JnxWxSysStatsPktSizeOut5_Object = MibScalar
jnxWxSysStatsPktSizeOut5 = _JnxWxSysStatsPktSizeOut5_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 35),
    _JnxWxSysStatsPktSizeOut5_Type()
)
jnxWxSysStatsPktSizeOut5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut5.setStatus("current")
_JnxWxSysStatsPktSizeOut6_Type = Counter64
_JnxWxSysStatsPktSizeOut6_Object = MibScalar
jnxWxSysStatsPktSizeOut6 = _JnxWxSysStatsPktSizeOut6_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 4, 36),
    _JnxWxSysStatsPktSizeOut6_Type()
)
jnxWxSysStatsPktSizeOut6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxSysStatsPktSizeOut6.setStatus("current")
_JnxWxAsm_ObjectIdentity = ObjectIdentity
jnxWxAsm = _JnxWxAsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    jnxWxAsm.setStatus("current")
_JnxWxAsmTable_Object = MibTable
jnxWxAsmTable = _JnxWxAsmTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    jnxWxAsmTable.setStatus("current")
_JnxWxAsmEntry_Object = MibTableRow
jnxWxAsmEntry = _JnxWxAsmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1)
)
jnxWxAsmEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAsmIndex"),
)
if mibBuilder.loadTexts:
    jnxWxAsmEntry.setStatus("current")
_JnxWxAsmIndex_Type = Integer32
_JnxWxAsmIndex_Object = MibTableColumn
jnxWxAsmIndex = _JnxWxAsmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1, 1),
    _JnxWxAsmIndex_Type()
)
jnxWxAsmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxAsmIndex.setStatus("current")
_JnxWxAsmIpAddress_Type = IpAddress
_JnxWxAsmIpAddress_Object = MibTableColumn
jnxWxAsmIpAddress = _JnxWxAsmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 1, 1, 2),
    _JnxWxAsmIpAddress_Type()
)
jnxWxAsmIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAsmIpAddress.setStatus("current")
_JnxWxAsmStatsTable_Object = MibTable
jnxWxAsmStatsTable = _JnxWxAsmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    jnxWxAsmStatsTable.setStatus("current")
_JnxWxAsmStatsEntry_Object = MibTableRow
jnxWxAsmStatsEntry = _JnxWxAsmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1)
)
if mibBuilder.loadTexts:
    jnxWxAsmStatsEntry.setStatus("current")
_JnxWxAsmStatsPktsIn_Type = Counter64
_JnxWxAsmStatsPktsIn_Object = MibTableColumn
jnxWxAsmStatsPktsIn = _JnxWxAsmStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 1),
    _JnxWxAsmStatsPktsIn_Type()
)
jnxWxAsmStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAsmStatsPktsIn.setStatus("current")
_JnxWxAsmStatsPktsOut_Type = Counter64
_JnxWxAsmStatsPktsOut_Object = MibTableColumn
jnxWxAsmStatsPktsOut = _JnxWxAsmStatsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 2),
    _JnxWxAsmStatsPktsOut_Type()
)
jnxWxAsmStatsPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAsmStatsPktsOut.setStatus("current")
_JnxWxAsmStatsBytesIn_Type = Counter64
_JnxWxAsmStatsBytesIn_Object = MibTableColumn
jnxWxAsmStatsBytesIn = _JnxWxAsmStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 3),
    _JnxWxAsmStatsBytesIn_Type()
)
jnxWxAsmStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAsmStatsBytesIn.setStatus("current")
_JnxWxAsmStatsBytesOut_Type = Counter64
_JnxWxAsmStatsBytesOut_Object = MibTableColumn
jnxWxAsmStatsBytesOut = _JnxWxAsmStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 2, 1, 4),
    _JnxWxAsmStatsBytesOut_Type()
)
jnxWxAsmStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAsmStatsBytesOut.setStatus("current")
_JnxWxVirtEndptTable_Object = MibTable
jnxWxVirtEndptTable = _JnxWxVirtEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    jnxWxVirtEndptTable.setStatus("current")
_JnxWxVirtEndptEntry_Object = MibTableRow
jnxWxVirtEndptEntry = _JnxWxVirtEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 3, 1)
)
jnxWxVirtEndptEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxVirtEndptIndex"),
)
if mibBuilder.loadTexts:
    jnxWxVirtEndptEntry.setStatus("current")
_JnxWxVirtEndptIndex_Type = Integer32
_JnxWxVirtEndptIndex_Object = MibTableColumn
jnxWxVirtEndptIndex = _JnxWxVirtEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 3, 1, 1),
    _JnxWxVirtEndptIndex_Type()
)
jnxWxVirtEndptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxVirtEndptIndex.setStatus("current")
_JnxWxVirtEndptName_Type = TcAppName
_JnxWxVirtEndptName_Object = MibTableColumn
jnxWxVirtEndptName = _JnxWxVirtEndptName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 3, 1, 2),
    _JnxWxVirtEndptName_Type()
)
jnxWxVirtEndptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxVirtEndptName.setStatus("current")
_JnxWxVirtEndptSubnetCount_Type = Integer32
_JnxWxVirtEndptSubnetCount_Object = MibTableColumn
jnxWxVirtEndptSubnetCount = _JnxWxVirtEndptSubnetCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 5, 3, 1, 3),
    _JnxWxVirtEndptSubnetCount_Type()
)
jnxWxVirtEndptSubnetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxVirtEndptSubnetCount.setStatus("current")
_JnxWxApp_ObjectIdentity = ObjectIdentity
jnxWxApp = _JnxWxApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    jnxWxApp.setStatus("current")
_JnxWxAppTable_Object = MibTable
jnxWxAppTable = _JnxWxAppTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    jnxWxAppTable.setStatus("current")
_JnxWxAppEntry_Object = MibTableRow
jnxWxAppEntry = _JnxWxAppEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1)
)
jnxWxAppEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAppIndex"),
)
if mibBuilder.loadTexts:
    jnxWxAppEntry.setStatus("current")
_JnxWxAppIndex_Type = Integer32
_JnxWxAppIndex_Object = MibTableColumn
jnxWxAppIndex = _JnxWxAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1, 1),
    _JnxWxAppIndex_Type()
)
jnxWxAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxAppIndex.setStatus("current")
_JnxWxAppAppName_Type = TcAppName
_JnxWxAppAppName_Object = MibTableColumn
jnxWxAppAppName = _JnxWxAppAppName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 1, 1, 2),
    _JnxWxAppAppName_Type()
)
jnxWxAppAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppAppName.setStatus("current")
_JnxWxAppStatsTable_Object = MibTable
jnxWxAppStatsTable = _JnxWxAppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    jnxWxAppStatsTable.setStatus("current")
_JnxWxAppStatsEntry_Object = MibTableRow
jnxWxAppStatsEntry = _JnxWxAppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1)
)
jnxWxAppStatsEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAsmIndex"),
    (0, "JUNIPER-WX-MIB", "jnxWxAppIndex"),
)
if mibBuilder.loadTexts:
    jnxWxAppStatsEntry.setStatus("current")
_JnxWxAppStatsBytesIn_Type = Counter64
_JnxWxAppStatsBytesIn_Object = MibTableColumn
jnxWxAppStatsBytesIn = _JnxWxAppStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 1),
    _JnxWxAppStatsBytesIn_Type()
)
jnxWxAppStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsBytesIn.setStatus("current")
_JnxWxAppStatsBytesOut_Type = Counter64
_JnxWxAppStatsBytesOut_Object = MibTableColumn
jnxWxAppStatsBytesOut = _JnxWxAppStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 2),
    _JnxWxAppStatsBytesOut_Type()
)
jnxWxAppStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsBytesOut.setStatus("current")
_JnxWxAppStatsBytesInPercent_Type = Gauge32
_JnxWxAppStatsBytesInPercent_Object = MibTableColumn
jnxWxAppStatsBytesInPercent = _JnxWxAppStatsBytesInPercent_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 3),
    _JnxWxAppStatsBytesInPercent_Type()
)
jnxWxAppStatsBytesInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsBytesInPercent.setStatus("current")
_JnxWxAppStatsAppName_Type = TcAppName
_JnxWxAppStatsAppName_Object = MibTableColumn
jnxWxAppStatsAppName = _JnxWxAppStatsAppName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 4),
    _JnxWxAppStatsAppName_Type()
)
jnxWxAppStatsAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsAppName.setStatus("current")
_JnxWxAppStatsAccelBytesIn_Type = Counter64
_JnxWxAppStatsAccelBytesIn_Object = MibTableColumn
jnxWxAppStatsAccelBytesIn = _JnxWxAppStatsAccelBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 5),
    _JnxWxAppStatsAccelBytesIn_Type()
)
jnxWxAppStatsAccelBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsAccelBytesIn.setStatus("current")
_JnxWxAppStatsActiveSessionTime_Type = Counter64
_JnxWxAppStatsActiveSessionTime_Object = MibTableColumn
jnxWxAppStatsActiveSessionTime = _JnxWxAppStatsActiveSessionTime_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 6),
    _JnxWxAppStatsActiveSessionTime_Type()
)
jnxWxAppStatsActiveSessionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsActiveSessionTime.setStatus("current")
_JnxWxAppStatsEstBoostBytes_Type = Counter64
_JnxWxAppStatsEstBoostBytes_Object = MibTableColumn
jnxWxAppStatsEstBoostBytes = _JnxWxAppStatsEstBoostBytes_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 7),
    _JnxWxAppStatsEstBoostBytes_Type()
)
jnxWxAppStatsEstBoostBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsEstBoostBytes.setStatus("current")
_JnxWxAppStatsBytesOutWxc_Type = Counter64
_JnxWxAppStatsBytesOutWxc_Object = MibTableColumn
jnxWxAppStatsBytesOutWxc = _JnxWxAppStatsBytesOutWxc_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 2, 1, 8),
    _JnxWxAppStatsBytesOutWxc_Type()
)
jnxWxAppStatsBytesOutWxc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppStatsBytesOutWxc.setStatus("current")
_JnxWxAppAggrStatsTable_Object = MibTable
jnxWxAppAggrStatsTable = _JnxWxAppAggrStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3)
)
if mibBuilder.loadTexts:
    jnxWxAppAggrStatsTable.setStatus("current")
_JnxWxAppAggrStatsEntry_Object = MibTableRow
jnxWxAppAggrStatsEntry = _JnxWxAppAggrStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1)
)
if mibBuilder.loadTexts:
    jnxWxAppAggrStatsEntry.setStatus("current")
_JnxWxAppAggrStatsBytesInRe_Type = Counter64
_JnxWxAppAggrStatsBytesInRe_Object = MibTableColumn
jnxWxAppAggrStatsBytesInRe = _JnxWxAppAggrStatsBytesInRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 1),
    _JnxWxAppAggrStatsBytesInRe_Type()
)
jnxWxAppAggrStatsBytesInRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppAggrStatsBytesInRe.setStatus("current")
_JnxWxAppAggrStatsBytesOutRe_Type = Counter64
_JnxWxAppAggrStatsBytesOutRe_Object = MibTableColumn
jnxWxAppAggrStatsBytesOutRe = _JnxWxAppAggrStatsBytesOutRe_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 2),
    _JnxWxAppAggrStatsBytesOutRe_Type()
)
jnxWxAppAggrStatsBytesOutRe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppAggrStatsBytesOutRe.setStatus("current")
_JnxWxAppAggrStatsBytesInPercent_Type = Gauge32
_JnxWxAppAggrStatsBytesInPercent_Object = MibTableColumn
jnxWxAppAggrStatsBytesInPercent = _JnxWxAppAggrStatsBytesInPercent_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 3, 1, 3),
    _JnxWxAppAggrStatsBytesInPercent_Type()
)
jnxWxAppAggrStatsBytesInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAppAggrStatsBytesInPercent.setStatus("current")
_JnxWxWanStatsTable_Object = MibTable
jnxWxWanStatsTable = _JnxWxWanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 4)
)
if mibBuilder.loadTexts:
    jnxWxWanStatsTable.setStatus("current")
_JnxWxWanStatsEntry_Object = MibTableRow
jnxWxWanStatsEntry = _JnxWxWanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 4, 1)
)
jnxWxWanStatsEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAsmIndex"),
    (0, "JUNIPER-WX-MIB", "jnxWxAppIndex"),
)
if mibBuilder.loadTexts:
    jnxWxWanStatsEntry.setStatus("current")
_JnxWxWanStatsBytesToWan_Type = Counter64
_JnxWxWanStatsBytesToWan_Object = MibTableColumn
jnxWxWanStatsBytesToWan = _JnxWxWanStatsBytesToWan_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 4, 1, 1),
    _JnxWxWanStatsBytesToWan_Type()
)
jnxWxWanStatsBytesToWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWanStatsBytesToWan.setStatus("current")
_JnxWxWanStatsBytesFromWan_Type = Counter64
_JnxWxWanStatsBytesFromWan_Object = MibTableColumn
jnxWxWanStatsBytesFromWan = _JnxWxWanStatsBytesFromWan_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 4, 1, 2),
    _JnxWxWanStatsBytesFromWan_Type()
)
jnxWxWanStatsBytesFromWan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWanStatsBytesFromWan.setStatus("current")
_JnxWxAccelAppNameTable_Object = MibTable
jnxWxAccelAppNameTable = _JnxWxAccelAppNameTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 5)
)
if mibBuilder.loadTexts:
    jnxWxAccelAppNameTable.setStatus("current")
_JnxWxAccelAppNameEntry_Object = MibTableRow
jnxWxAccelAppNameEntry = _JnxWxAccelAppNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 5, 1)
)
jnxWxAccelAppNameEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAccelAppIndex"),
)
if mibBuilder.loadTexts:
    jnxWxAccelAppNameEntry.setStatus("current")
_JnxWxAccelAppIndex_Type = Integer32
_JnxWxAccelAppIndex_Object = MibTableColumn
jnxWxAccelAppIndex = _JnxWxAccelAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 5, 1, 1),
    _JnxWxAccelAppIndex_Type()
)
jnxWxAccelAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxAccelAppIndex.setStatus("current")
_JnxWxAccelAppName_Type = TcAppName
_JnxWxAccelAppName_Object = MibTableColumn
jnxWxAccelAppName = _JnxWxAccelAppName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 5, 1, 2),
    _JnxWxAccelAppName_Type()
)
jnxWxAccelAppName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAccelAppName.setStatus("current")
_JnxWxAccelAppStatsTable_Object = MibTable
jnxWxAccelAppStatsTable = _JnxWxAccelAppStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 6)
)
if mibBuilder.loadTexts:
    jnxWxAccelAppStatsTable.setStatus("current")
_JnxWxAccelAppStatsEntry_Object = MibTableRow
jnxWxAccelAppStatsEntry = _JnxWxAccelAppStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 6, 1)
)
jnxWxAccelAppStatsEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxAsmIndex"),
    (0, "JUNIPER-WX-MIB", "jnxWxAccelAppIndex"),
)
if mibBuilder.loadTexts:
    jnxWxAccelAppStatsEntry.setStatus("current")
_JnxWxAccelAppTimeWithAccel_Type = Unsigned32
_JnxWxAccelAppTimeWithAccel_Object = MibTableColumn
jnxWxAccelAppTimeWithAccel = _JnxWxAccelAppTimeWithAccel_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 6, 1, 3),
    _JnxWxAccelAppTimeWithAccel_Type()
)
jnxWxAccelAppTimeWithAccel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAccelAppTimeWithAccel.setStatus("current")
_JnxWxAccelAppTimeWithoutAccel_Type = Unsigned32
_JnxWxAccelAppTimeWithoutAccel_Object = MibTableColumn
jnxWxAccelAppTimeWithoutAccel = _JnxWxAccelAppTimeWithoutAccel_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 6, 6, 1, 4),
    _JnxWxAccelAppTimeWithoutAccel_Type()
)
jnxWxAccelAppTimeWithoutAccel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxAccelAppTimeWithoutAccel.setStatus("current")
_JnxWxBurstStats_ObjectIdentity = ObjectIdentity
jnxWxBurstStats = _JnxWxBurstStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7)
)
if mibBuilder.loadTexts:
    jnxWxBurstStats.setStatus("current")
_JnxWxBurstStatsStartTime_Type = Integer32
_JnxWxBurstStatsStartTime_Object = MibScalar
jnxWxBurstStatsStartTime = _JnxWxBurstStatsStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 1),
    _JnxWxBurstStatsStartTime_Type()
)
jnxWxBurstStatsStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxBurstStatsStartTime.setStatus("current")
_JnxWxBurstStatsBpsIn_Type = Gauge32
_JnxWxBurstStatsBpsIn_Object = MibScalar
jnxWxBurstStatsBpsIn = _JnxWxBurstStatsBpsIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 2),
    _JnxWxBurstStatsBpsIn_Type()
)
jnxWxBurstStatsBpsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxBurstStatsBpsIn.setStatus("current")
_JnxWxBurstStatsBpsOut_Type = Gauge32
_JnxWxBurstStatsBpsOut_Object = MibScalar
jnxWxBurstStatsBpsOut = _JnxWxBurstStatsBpsOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 3),
    _JnxWxBurstStatsBpsOut_Type()
)
jnxWxBurstStatsBpsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxBurstStatsBpsOut.setStatus("current")
_JnxWxBurstStatsBpsPt_Type = Gauge32
_JnxWxBurstStatsBpsPt_Object = MibScalar
jnxWxBurstStatsBpsPt = _JnxWxBurstStatsBpsPt_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 7, 4),
    _JnxWxBurstStatsBpsPt_Type()
)
jnxWxBurstStatsBpsPt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxBurstStatsBpsPt.setStatus("current")
_JnxWxStatsAccelAppCount_Type = Integer32
_JnxWxStatsAccelAppCount_Object = MibScalar
jnxWxStatsAccelAppCount = _JnxWxStatsAccelAppCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 8),
    _JnxWxStatsAccelAppCount_Type()
)
jnxWxStatsAccelAppCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsAccelAppCount.setStatus("current")
_JnxWxStatsVirtEndptCount_Type = Integer32
_JnxWxStatsVirtEndptCount_Object = MibScalar
jnxWxStatsVirtEndptCount = _JnxWxStatsVirtEndptCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 9),
    _JnxWxStatsVirtEndptCount_Type()
)
jnxWxStatsVirtEndptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsVirtEndptCount.setStatus("current")
_JnxWxQos_ObjectIdentity = ObjectIdentity
jnxWxQos = _JnxWxQos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10)
)
if mibBuilder.loadTexts:
    jnxWxQos.setStatus("current")
_JnxWxQosEndptTable_Object = MibTable
jnxWxQosEndptTable = _JnxWxQosEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    jnxWxQosEndptTable.setStatus("current")
_JnxWxQosEndptEntry_Object = MibTableRow
jnxWxQosEndptEntry = _JnxWxQosEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 1, 1)
)
jnxWxQosEndptEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxQosEndptIndex"),
)
if mibBuilder.loadTexts:
    jnxWxQosEndptEntry.setStatus("current")
_JnxWxQosEndptIndex_Type = Integer32
_JnxWxQosEndptIndex_Object = MibTableColumn
jnxWxQosEndptIndex = _JnxWxQosEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 1, 1, 1),
    _JnxWxQosEndptIndex_Type()
)
jnxWxQosEndptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxQosEndptIndex.setStatus("current")
_JnxWxQosEndptIdentifier_Type = TcQosIdentifier
_JnxWxQosEndptIdentifier_Object = MibTableColumn
jnxWxQosEndptIdentifier = _JnxWxQosEndptIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 1, 1, 2),
    _JnxWxQosEndptIdentifier_Type()
)
jnxWxQosEndptIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosEndptIdentifier.setStatus("current")
_JnxWxQosClassTable_Object = MibTable
jnxWxQosClassTable = _JnxWxQosClassTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 2)
)
if mibBuilder.loadTexts:
    jnxWxQosClassTable.setStatus("current")
_JnxWxQosClassEntry_Object = MibTableRow
jnxWxQosClassEntry = _JnxWxQosClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 2, 1)
)
jnxWxQosClassEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxQosClassIndex"),
)
if mibBuilder.loadTexts:
    jnxWxQosClassEntry.setStatus("current")
_JnxWxQosClassIndex_Type = Integer32
_JnxWxQosClassIndex_Object = MibTableColumn
jnxWxQosClassIndex = _JnxWxQosClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 2, 1, 1),
    _JnxWxQosClassIndex_Type()
)
jnxWxQosClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxQosClassIndex.setStatus("current")
_JnxWxQosClassName_Type = TcQosIdentifier
_JnxWxQosClassName_Object = MibTableColumn
jnxWxQosClassName = _JnxWxQosClassName_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 2, 1, 2),
    _JnxWxQosClassName_Type()
)
jnxWxQosClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosClassName.setStatus("current")
_JnxWxQosStatsTable_Object = MibTable
jnxWxQosStatsTable = _JnxWxQosStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3)
)
if mibBuilder.loadTexts:
    jnxWxQosStatsTable.setStatus("current")
_JnxWxQosStatsEntry_Object = MibTableRow
jnxWxQosStatsEntry = _JnxWxQosStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1)
)
jnxWxQosStatsEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxQosEndptIndex"),
    (0, "JUNIPER-WX-MIB", "jnxWxQosClassIndex"),
)
if mibBuilder.loadTexts:
    jnxWxQosStatsEntry.setStatus("current")
_JnxWxQosStatsBytesIn_Type = Counter64
_JnxWxQosStatsBytesIn_Object = MibTableColumn
jnxWxQosStatsBytesIn = _JnxWxQosStatsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 3),
    _JnxWxQosStatsBytesIn_Type()
)
jnxWxQosStatsBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsBytesIn.setStatus("current")
_JnxWxQosStatsBytesOut_Type = Counter64
_JnxWxQosStatsBytesOut_Object = MibTableColumn
jnxWxQosStatsBytesOut = _JnxWxQosStatsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 4),
    _JnxWxQosStatsBytesOut_Type()
)
jnxWxQosStatsBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsBytesOut.setStatus("current")
_JnxWxQosStatsBytesDropped_Type = Counter64
_JnxWxQosStatsBytesDropped_Object = MibTableColumn
jnxWxQosStatsBytesDropped = _JnxWxQosStatsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 5),
    _JnxWxQosStatsBytesDropped_Type()
)
jnxWxQosStatsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsBytesDropped.setStatus("current")
_JnxWxQosStatsPktsIn_Type = Counter64
_JnxWxQosStatsPktsIn_Object = MibTableColumn
jnxWxQosStatsPktsIn = _JnxWxQosStatsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 6),
    _JnxWxQosStatsPktsIn_Type()
)
jnxWxQosStatsPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsPktsIn.setStatus("current")
_JnxWxQosStatsPktsOut_Type = Counter64
_JnxWxQosStatsPktsOut_Object = MibTableColumn
jnxWxQosStatsPktsOut = _JnxWxQosStatsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 7),
    _JnxWxQosStatsPktsOut_Type()
)
jnxWxQosStatsPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsPktsOut.setStatus("current")
_JnxWxQosStatsPktsDropped_Type = Counter64
_JnxWxQosStatsPktsDropped_Object = MibTableColumn
jnxWxQosStatsPktsDropped = _JnxWxQosStatsPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 10, 3, 1, 8),
    _JnxWxQosStatsPktsDropped_Type()
)
jnxWxQosStatsPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxQosStatsPktsDropped.setStatus("current")
_JnxWxStatsQosClassCount_Type = Integer32
_JnxWxStatsQosClassCount_Object = MibScalar
jnxWxStatsQosClassCount = _JnxWxStatsQosClassCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 11),
    _JnxWxStatsQosClassCount_Type()
)
jnxWxStatsQosClassCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsQosClassCount.setStatus("current")
_JnxWxStatsQosEndptCount_Type = Integer32
_JnxWxStatsQosEndptCount_Object = MibScalar
jnxWxStatsQosEndptCount = _JnxWxStatsQosEndptCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 12),
    _JnxWxStatsQosEndptCount_Type()
)
jnxWxStatsQosEndptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsQosEndptCount.setStatus("current")
_JnxWxStatsWpEndptCount_Type = Integer32
_JnxWxStatsWpEndptCount_Object = MibScalar
jnxWxStatsWpEndptCount = _JnxWxStatsWpEndptCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 13),
    _JnxWxStatsWpEndptCount_Type()
)
jnxWxStatsWpEndptCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxStatsWpEndptCount.setStatus("current")
_JnxWxWanPerf_ObjectIdentity = ObjectIdentity
jnxWxWanPerf = _JnxWxWanPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14)
)
if mibBuilder.loadTexts:
    jnxWxWanPerf.setStatus("current")
_JnxWxWpEndptTable_Object = MibTable
jnxWxWpEndptTable = _JnxWxWpEndptTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 1)
)
if mibBuilder.loadTexts:
    jnxWxWpEndptTable.setStatus("current")
_JnxWxWpEndptEntry_Object = MibTableRow
jnxWxWpEndptEntry = _JnxWxWpEndptEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 1, 1)
)
jnxWxWpEndptEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxWpEndptIndex"),
)
if mibBuilder.loadTexts:
    jnxWxWpEndptEntry.setStatus("current")
_JnxWxWpEndptIndex_Type = Integer32
_JnxWxWpEndptIndex_Object = MibTableColumn
jnxWxWpEndptIndex = _JnxWxWpEndptIndex_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 1, 1, 1),
    _JnxWxWpEndptIndex_Type()
)
jnxWxWpEndptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxWxWpEndptIndex.setStatus("current")
_JnxWxWpEndptIp_Type = IpAddress
_JnxWxWpEndptIp_Object = MibTableColumn
jnxWxWpEndptIp = _JnxWxWpEndptIp_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 1, 1, 2),
    _JnxWxWpEndptIp_Type()
)
jnxWxWpEndptIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpEndptIp.setStatus("current")
_JnxWxWpStatsTable_Object = MibTable
jnxWxWpStatsTable = _JnxWxWpStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    jnxWxWpStatsTable.setStatus("current")
_JnxWxWpStatsEntry_Object = MibTableRow
jnxWxWpStatsEntry = _JnxWxWpStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1)
)
jnxWxWpStatsEntry.setIndexNames(
    (0, "JUNIPER-WX-MIB", "jnxWxWpEndptIndex"),
)
if mibBuilder.loadTexts:
    jnxWxWpStatsEntry.setStatus("current")
_JnxWxWpStatsLatencyThresh_Type = Unsigned32
_JnxWxWpStatsLatencyThresh_Object = MibTableColumn
jnxWxWpStatsLatencyThresh = _JnxWxWpStatsLatencyThresh_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 3),
    _JnxWxWpStatsLatencyThresh_Type()
)
jnxWxWpStatsLatencyThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLatencyThresh.setStatus("current")
_JnxWxWpStatsAvgLatency_Type = Unsigned32
_JnxWxWpStatsAvgLatency_Object = MibTableColumn
jnxWxWpStatsAvgLatency = _JnxWxWpStatsAvgLatency_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 4),
    _JnxWxWpStatsAvgLatency_Type()
)
jnxWxWpStatsAvgLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsAvgLatency.setStatus("current")
_JnxWxWpStatsLatencyCount_Type = Unsigned32
_JnxWxWpStatsLatencyCount_Object = MibTableColumn
jnxWxWpStatsLatencyCount = _JnxWxWpStatsLatencyCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 5),
    _JnxWxWpStatsLatencyCount_Type()
)
jnxWxWpStatsLatencyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLatencyCount.setStatus("current")
_JnxWxWpStatsLatencyAboveThresh_Type = Unsigned32
_JnxWxWpStatsLatencyAboveThresh_Object = MibTableColumn
jnxWxWpStatsLatencyAboveThresh = _JnxWxWpStatsLatencyAboveThresh_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 6),
    _JnxWxWpStatsLatencyAboveThresh_Type()
)
jnxWxWpStatsLatencyAboveThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLatencyAboveThresh.setStatus("current")
_JnxWxWpStatsLatencyAboveThreshCount_Type = Unsigned32
_JnxWxWpStatsLatencyAboveThreshCount_Object = MibTableColumn
jnxWxWpStatsLatencyAboveThreshCount = _JnxWxWpStatsLatencyAboveThreshCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 7),
    _JnxWxWpStatsLatencyAboveThreshCount_Type()
)
jnxWxWpStatsLatencyAboveThreshCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLatencyAboveThreshCount.setStatus("current")
_JnxWxWpStatsLossPercent_Type = Unsigned32
_JnxWxWpStatsLossPercent_Object = MibTableColumn
jnxWxWpStatsLossPercent = _JnxWxWpStatsLossPercent_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 8),
    _JnxWxWpStatsLossPercent_Type()
)
jnxWxWpStatsLossPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLossPercent.setStatus("current")
_JnxWxWpStatsLossCount_Type = Unsigned32
_JnxWxWpStatsLossCount_Object = MibTableColumn
jnxWxWpStatsLossCount = _JnxWxWpStatsLossCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 9),
    _JnxWxWpStatsLossCount_Type()
)
jnxWxWpStatsLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLossCount.setStatus("current")
_JnxWxWpStatsEventCount_Type = Unsigned32
_JnxWxWpStatsEventCount_Object = MibTableColumn
jnxWxWpStatsEventCount = _JnxWxWpStatsEventCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 10),
    _JnxWxWpStatsEventCount_Type()
)
jnxWxWpStatsEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsEventCount.setStatus("current")
_JnxWxWpStatsDiversionCount_Type = Unsigned32
_JnxWxWpStatsDiversionCount_Object = MibTableColumn
jnxWxWpStatsDiversionCount = _JnxWxWpStatsDiversionCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 11),
    _JnxWxWpStatsDiversionCount_Type()
)
jnxWxWpStatsDiversionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsDiversionCount.setStatus("current")
_JnxWxWpStatsReturnCount_Type = Unsigned32
_JnxWxWpStatsReturnCount_Object = MibTableColumn
jnxWxWpStatsReturnCount = _JnxWxWpStatsReturnCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 12),
    _JnxWxWpStatsReturnCount_Type()
)
jnxWxWpStatsReturnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsReturnCount.setStatus("current")
_JnxWxWpStatsLastDown_Type = Unsigned32
_JnxWxWpStatsLastDown_Object = MibTableColumn
jnxWxWpStatsLastDown = _JnxWxWpStatsLastDown_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 13),
    _JnxWxWpStatsLastDown_Type()
)
jnxWxWpStatsLastDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsLastDown.setStatus("current")
_JnxWxWpStatsUnavailableCount_Type = Unsigned32
_JnxWxWpStatsUnavailableCount_Object = MibTableColumn
jnxWxWpStatsUnavailableCount = _JnxWxWpStatsUnavailableCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 14),
    _JnxWxWpStatsUnavailableCount_Type()
)
jnxWxWpStatsUnavailableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsUnavailableCount.setStatus("current")
_JnxWxWpStatsMinuteCount_Type = Unsigned32
_JnxWxWpStatsMinuteCount_Object = MibTableColumn
jnxWxWpStatsMinuteCount = _JnxWxWpStatsMinuteCount_Object(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 2, 14, 2, 1, 15),
    _JnxWxWpStatsMinuteCount_Type()
)
jnxWxWpStatsMinuteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxWxWpStatsMinuteCount.setStatus("current")
_JnxWxEvents_ObjectIdentity = ObjectIdentity
jnxWxEvents = _JnxWxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jnxWxEvents.setStatus("current")
_JnxWxEventObjs_ObjectIdentity = ObjectIdentity
jnxWxEventObjs = _JnxWxEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxWxEventObjs.setStatus("current")
_JnxWxEventEvents_ObjectIdentity = ObjectIdentity
jnxWxEventEvents = _JnxWxEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxWxEventEvents.setStatus("current")
_JnxWxEventEventsV2_ObjectIdentity = ObjectIdentity
jnxWxEventEventsV2 = _JnxWxEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    jnxWxEventEventsV2.setStatus("current")
jnxWxAsmEntry.registerAugmentions(
    ("JUNIPER-WX-MIB",
     "jnxWxAsmStatsEntry")
)
jnxWxAsmStatsEntry.setIndexNames(*jnxWxAsmEntry.getIndexNames())
jnxWxAppEntry.registerAugmentions(
    ("JUNIPER-WX-MIB",
     "jnxWxAppAggrStatsEntry")
)
jnxWxAppAggrStatsEntry.setIndexNames(*jnxWxAppEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxWxEventRipAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 1)
)
jnxWxEventRipAuthFailure.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventRipAuthFailure.setStatus(
        "current"
    )

jnxWxEventCompressionBufferOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 2)
)
jnxWxEventCompressionBufferOverflow.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventCompressionBufferOverflow.setStatus(
        "current"
    )

jnxWxEventCompressionSessionClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 3)
)
jnxWxEventCompressionSessionClosed.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventCompressionSessionClosed.setStatus(
        "current"
    )

jnxWxEventDecompressionSessionClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 4)
)
jnxWxEventDecompressionSessionClosed.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventDecompressionSessionClosed.setStatus(
        "current"
    )

jnxWxEventCompressionSessionOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 5)
)
jnxWxEventCompressionSessionOpened.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventCompressionSessionOpened.setStatus(
        "current"
    )

jnxWxEventDecompressionSessionOpened = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 6)
)
jnxWxEventDecompressionSessionOpened.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventDecompressionSessionOpened.setStatus(
        "current"
    )

jnxWxEventPrimaryRegServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 7)
)
jnxWxEventPrimaryRegServerUnreachable.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventPrimaryRegServerUnreachable.setStatus(
        "current"
    )

jnxWxEventSecondaryRegServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 8)
)
jnxWxEventSecondaryRegServerUnreachable.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventSecondaryRegServerUnreachable.setStatus(
        "current"
    )

jnxWxEventMultiNodeMasterUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 9)
)
jnxWxEventMultiNodeMasterUp.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventMultiNodeMasterUp.setStatus(
        "current"
    )

jnxWxEventMultiNodeMasterDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 10)
)
jnxWxEventMultiNodeMasterDown.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventMultiNodeMasterDown.setStatus(
        "current"
    )

jnxWxEventMultiNodeLastUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 11)
)
jnxWxEventMultiNodeLastUp.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventMultiNodeLastUp.setStatus(
        "current"
    )

jnxWxEventMultiNodeLastDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 12)
)
jnxWxEventMultiNodeLastDown.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventMultiNodeLastDown.setStatus(
        "current"
    )

jnxWxEventPrimaryDownBackupEngaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 13)
)
jnxWxEventPrimaryDownBackupEngaged.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventPrimaryDownBackupEngaged.setStatus(
        "current"
    )

jnxWxEventPrimaryDownBackupEngageFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 14)
)
jnxWxEventPrimaryDownBackupEngageFailed.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventPrimaryDownBackupEngageFailed.setStatus(
        "current"
    )

jnxWxEventPrimaryUpBackupDisengaged = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 15)
)
jnxWxEventPrimaryUpBackupDisengaged.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventPrimaryUpBackupDisengaged.setStatus(
        "current"
    )

jnxWxEventMultiPathStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 16)
)
jnxWxEventMultiPathStatusChange.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventMultiPathStatusChange.setStatus(
        "current"
    )

jnxWxEventDiskFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 17)
)
jnxWxEventDiskFailure.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventDiskFailure.setStatus(
        "current"
    )

jnxWxEventWanPerfStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 18)
)
jnxWxEventWanPerfStatusChange.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventWanPerfStatusChange.setStatus(
        "current"
    )

jnxWxEventDCQAboveHiWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 19)
)
jnxWxEventDCQAboveHiWatermark.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventDCQAboveHiWatermark.setStatus(
        "current"
    )

jnxWxEventDCQBelowHiWatermark = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 20)
)
jnxWxEventDCQBelowHiWatermark.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventDCQBelowHiWatermark.setStatus(
        "current"
    )

jnxWxEventPerformanceThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 21)
)
jnxWxEventPerformanceThreshCrossed.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventPerformanceThreshCrossed.setStatus(
        "current"
    )

jnxWxEventClientLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 22)
)
jnxWxEventClientLinkDown.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventClientLinkDown.setStatus(
        "current"
    )

jnxWxEventClientLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8239, 2, 2, 1, 3, 2, 0, 23)
)
jnxWxEventClientLinkUp.setObjects(
    ("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr")
)
if mibBuilder.loadTexts:
    jnxWxEventClientLinkUp.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-WX-MIB",
    **{"jnxWxMibModule": jnxWxMibModule,
       "jnxWxMib": jnxWxMib,
       "jnxWxConfMib": jnxWxConfMib,
       "jnxWxObjs": jnxWxObjs,
       "jnxWxStatsUpdateTime": jnxWxStatsUpdateTime,
       "jnxWxStatsAsmCount": jnxWxStatsAsmCount,
       "jnxWxStatsAppCount": jnxWxStatsAppCount,
       "jnxWxSysStats": jnxWxSysStats,
       "jnxWxSysStatsBytesInAe": jnxWxSysStatsBytesInAe,
       "jnxWxSysStatsBytesOutAe": jnxWxSysStatsBytesOutAe,
       "jnxWxSysStatsPktsInAe": jnxWxSysStatsPktsInAe,
       "jnxWxSysStatsPktsOutAe": jnxWxSysStatsPktsOutAe,
       "jnxWxSysStatsBytesOutOob": jnxWxSysStatsBytesOutOob,
       "jnxWxSysStatsBytesPtNoAe": jnxWxSysStatsBytesPtNoAe,
       "jnxWxSysStatsPktsPtNoAe": jnxWxSysStatsPktsPtNoAe,
       "jnxWxSysStatsBytesPtFilter": jnxWxSysStatsBytesPtFilter,
       "jnxWxSysStatsPktsPtFilter": jnxWxSysStatsPktsPtFilter,
       "jnxWxSysStatsBytesOfPt": jnxWxSysStatsBytesOfPt,
       "jnxWxSysStatsPktsOfPt": jnxWxSysStatsPktsOfPt,
       "jnxWxSysStatsBytesTpIn": jnxWxSysStatsBytesTpIn,
       "jnxWxSysStatsPktsTpIn": jnxWxSysStatsPktsTpIn,
       "jnxWxSysStatsBytesTpOut": jnxWxSysStatsBytesTpOut,
       "jnxWxSysStatsPktsTpOut": jnxWxSysStatsPktsTpOut,
       "jnxWxSysStatsBytesTpPt": jnxWxSysStatsBytesTpPt,
       "jnxWxSysStatsPktsTpPt": jnxWxSysStatsPktsTpPt,
       "jnxWxSysStatsPeakRdn": jnxWxSysStatsPeakRdn,
       "jnxWxSysStatsThruputIn": jnxWxSysStatsThruputIn,
       "jnxWxSysStatsThruputOut": jnxWxSysStatsThruputOut,
       "jnxWxSysStatsBytesInRe": jnxWxSysStatsBytesInRe,
       "jnxWxSysStatsBytesOutRe": jnxWxSysStatsBytesOutRe,
       "jnxWxSysStatsPktsInRe": jnxWxSysStatsPktsInRe,
       "jnxWxSysStatsPktsOutRe": jnxWxSysStatsPktsOutRe,
       "jnxWxSysStatsPktSizeIn1": jnxWxSysStatsPktSizeIn1,
       "jnxWxSysStatsPktSizeIn2": jnxWxSysStatsPktSizeIn2,
       "jnxWxSysStatsPktSizeIn3": jnxWxSysStatsPktSizeIn3,
       "jnxWxSysStatsPktSizeIn4": jnxWxSysStatsPktSizeIn4,
       "jnxWxSysStatsPktSizeIn5": jnxWxSysStatsPktSizeIn5,
       "jnxWxSysStatsPktSizeIn6": jnxWxSysStatsPktSizeIn6,
       "jnxWxSysStatsPktSizeOut1": jnxWxSysStatsPktSizeOut1,
       "jnxWxSysStatsPktSizeOut2": jnxWxSysStatsPktSizeOut2,
       "jnxWxSysStatsPktSizeOut3": jnxWxSysStatsPktSizeOut3,
       "jnxWxSysStatsPktSizeOut4": jnxWxSysStatsPktSizeOut4,
       "jnxWxSysStatsPktSizeOut5": jnxWxSysStatsPktSizeOut5,
       "jnxWxSysStatsPktSizeOut6": jnxWxSysStatsPktSizeOut6,
       "jnxWxAsm": jnxWxAsm,
       "jnxWxAsmTable": jnxWxAsmTable,
       "jnxWxAsmEntry": jnxWxAsmEntry,
       "jnxWxAsmIndex": jnxWxAsmIndex,
       "jnxWxAsmIpAddress": jnxWxAsmIpAddress,
       "jnxWxAsmStatsTable": jnxWxAsmStatsTable,
       "jnxWxAsmStatsEntry": jnxWxAsmStatsEntry,
       "jnxWxAsmStatsPktsIn": jnxWxAsmStatsPktsIn,
       "jnxWxAsmStatsPktsOut": jnxWxAsmStatsPktsOut,
       "jnxWxAsmStatsBytesIn": jnxWxAsmStatsBytesIn,
       "jnxWxAsmStatsBytesOut": jnxWxAsmStatsBytesOut,
       "jnxWxVirtEndptTable": jnxWxVirtEndptTable,
       "jnxWxVirtEndptEntry": jnxWxVirtEndptEntry,
       "jnxWxVirtEndptIndex": jnxWxVirtEndptIndex,
       "jnxWxVirtEndptName": jnxWxVirtEndptName,
       "jnxWxVirtEndptSubnetCount": jnxWxVirtEndptSubnetCount,
       "jnxWxApp": jnxWxApp,
       "jnxWxAppTable": jnxWxAppTable,
       "jnxWxAppEntry": jnxWxAppEntry,
       "jnxWxAppIndex": jnxWxAppIndex,
       "jnxWxAppAppName": jnxWxAppAppName,
       "jnxWxAppStatsTable": jnxWxAppStatsTable,
       "jnxWxAppStatsEntry": jnxWxAppStatsEntry,
       "jnxWxAppStatsBytesIn": jnxWxAppStatsBytesIn,
       "jnxWxAppStatsBytesOut": jnxWxAppStatsBytesOut,
       "jnxWxAppStatsBytesInPercent": jnxWxAppStatsBytesInPercent,
       "jnxWxAppStatsAppName": jnxWxAppStatsAppName,
       "jnxWxAppStatsAccelBytesIn": jnxWxAppStatsAccelBytesIn,
       "jnxWxAppStatsActiveSessionTime": jnxWxAppStatsActiveSessionTime,
       "jnxWxAppStatsEstBoostBytes": jnxWxAppStatsEstBoostBytes,
       "jnxWxAppStatsBytesOutWxc": jnxWxAppStatsBytesOutWxc,
       "jnxWxAppAggrStatsTable": jnxWxAppAggrStatsTable,
       "jnxWxAppAggrStatsEntry": jnxWxAppAggrStatsEntry,
       "jnxWxAppAggrStatsBytesInRe": jnxWxAppAggrStatsBytesInRe,
       "jnxWxAppAggrStatsBytesOutRe": jnxWxAppAggrStatsBytesOutRe,
       "jnxWxAppAggrStatsBytesInPercent": jnxWxAppAggrStatsBytesInPercent,
       "jnxWxWanStatsTable": jnxWxWanStatsTable,
       "jnxWxWanStatsEntry": jnxWxWanStatsEntry,
       "jnxWxWanStatsBytesToWan": jnxWxWanStatsBytesToWan,
       "jnxWxWanStatsBytesFromWan": jnxWxWanStatsBytesFromWan,
       "jnxWxAccelAppNameTable": jnxWxAccelAppNameTable,
       "jnxWxAccelAppNameEntry": jnxWxAccelAppNameEntry,
       "jnxWxAccelAppIndex": jnxWxAccelAppIndex,
       "jnxWxAccelAppName": jnxWxAccelAppName,
       "jnxWxAccelAppStatsTable": jnxWxAccelAppStatsTable,
       "jnxWxAccelAppStatsEntry": jnxWxAccelAppStatsEntry,
       "jnxWxAccelAppTimeWithAccel": jnxWxAccelAppTimeWithAccel,
       "jnxWxAccelAppTimeWithoutAccel": jnxWxAccelAppTimeWithoutAccel,
       "jnxWxBurstStats": jnxWxBurstStats,
       "jnxWxBurstStatsStartTime": jnxWxBurstStatsStartTime,
       "jnxWxBurstStatsBpsIn": jnxWxBurstStatsBpsIn,
       "jnxWxBurstStatsBpsOut": jnxWxBurstStatsBpsOut,
       "jnxWxBurstStatsBpsPt": jnxWxBurstStatsBpsPt,
       "jnxWxStatsAccelAppCount": jnxWxStatsAccelAppCount,
       "jnxWxStatsVirtEndptCount": jnxWxStatsVirtEndptCount,
       "jnxWxQos": jnxWxQos,
       "jnxWxQosEndptTable": jnxWxQosEndptTable,
       "jnxWxQosEndptEntry": jnxWxQosEndptEntry,
       "jnxWxQosEndptIndex": jnxWxQosEndptIndex,
       "jnxWxQosEndptIdentifier": jnxWxQosEndptIdentifier,
       "jnxWxQosClassTable": jnxWxQosClassTable,
       "jnxWxQosClassEntry": jnxWxQosClassEntry,
       "jnxWxQosClassIndex": jnxWxQosClassIndex,
       "jnxWxQosClassName": jnxWxQosClassName,
       "jnxWxQosStatsTable": jnxWxQosStatsTable,
       "jnxWxQosStatsEntry": jnxWxQosStatsEntry,
       "jnxWxQosStatsBytesIn": jnxWxQosStatsBytesIn,
       "jnxWxQosStatsBytesOut": jnxWxQosStatsBytesOut,
       "jnxWxQosStatsBytesDropped": jnxWxQosStatsBytesDropped,
       "jnxWxQosStatsPktsIn": jnxWxQosStatsPktsIn,
       "jnxWxQosStatsPktsOut": jnxWxQosStatsPktsOut,
       "jnxWxQosStatsPktsDropped": jnxWxQosStatsPktsDropped,
       "jnxWxStatsQosClassCount": jnxWxStatsQosClassCount,
       "jnxWxStatsQosEndptCount": jnxWxStatsQosEndptCount,
       "jnxWxStatsWpEndptCount": jnxWxStatsWpEndptCount,
       "jnxWxWanPerf": jnxWxWanPerf,
       "jnxWxWpEndptTable": jnxWxWpEndptTable,
       "jnxWxWpEndptEntry": jnxWxWpEndptEntry,
       "jnxWxWpEndptIndex": jnxWxWpEndptIndex,
       "jnxWxWpEndptIp": jnxWxWpEndptIp,
       "jnxWxWpStatsTable": jnxWxWpStatsTable,
       "jnxWxWpStatsEntry": jnxWxWpStatsEntry,
       "jnxWxWpStatsLatencyThresh": jnxWxWpStatsLatencyThresh,
       "jnxWxWpStatsAvgLatency": jnxWxWpStatsAvgLatency,
       "jnxWxWpStatsLatencyCount": jnxWxWpStatsLatencyCount,
       "jnxWxWpStatsLatencyAboveThresh": jnxWxWpStatsLatencyAboveThresh,
       "jnxWxWpStatsLatencyAboveThreshCount": jnxWxWpStatsLatencyAboveThreshCount,
       "jnxWxWpStatsLossPercent": jnxWxWpStatsLossPercent,
       "jnxWxWpStatsLossCount": jnxWxWpStatsLossCount,
       "jnxWxWpStatsEventCount": jnxWxWpStatsEventCount,
       "jnxWxWpStatsDiversionCount": jnxWxWpStatsDiversionCount,
       "jnxWxWpStatsReturnCount": jnxWxWpStatsReturnCount,
       "jnxWxWpStatsLastDown": jnxWxWpStatsLastDown,
       "jnxWxWpStatsUnavailableCount": jnxWxWpStatsUnavailableCount,
       "jnxWxWpStatsMinuteCount": jnxWxWpStatsMinuteCount,
       "jnxWxEvents": jnxWxEvents,
       "jnxWxEventObjs": jnxWxEventObjs,
       "jnxWxEventEvents": jnxWxEventEvents,
       "jnxWxEventEventsV2": jnxWxEventEventsV2,
       "jnxWxEventRipAuthFailure": jnxWxEventRipAuthFailure,
       "jnxWxEventCompressionBufferOverflow": jnxWxEventCompressionBufferOverflow,
       "jnxWxEventCompressionSessionClosed": jnxWxEventCompressionSessionClosed,
       "jnxWxEventDecompressionSessionClosed": jnxWxEventDecompressionSessionClosed,
       "jnxWxEventCompressionSessionOpened": jnxWxEventCompressionSessionOpened,
       "jnxWxEventDecompressionSessionOpened": jnxWxEventDecompressionSessionOpened,
       "jnxWxEventPrimaryRegServerUnreachable": jnxWxEventPrimaryRegServerUnreachable,
       "jnxWxEventSecondaryRegServerUnreachable": jnxWxEventSecondaryRegServerUnreachable,
       "jnxWxEventMultiNodeMasterUp": jnxWxEventMultiNodeMasterUp,
       "jnxWxEventMultiNodeMasterDown": jnxWxEventMultiNodeMasterDown,
       "jnxWxEventMultiNodeLastUp": jnxWxEventMultiNodeLastUp,
       "jnxWxEventMultiNodeLastDown": jnxWxEventMultiNodeLastDown,
       "jnxWxEventPrimaryDownBackupEngaged": jnxWxEventPrimaryDownBackupEngaged,
       "jnxWxEventPrimaryDownBackupEngageFailed": jnxWxEventPrimaryDownBackupEngageFailed,
       "jnxWxEventPrimaryUpBackupDisengaged": jnxWxEventPrimaryUpBackupDisengaged,
       "jnxWxEventMultiPathStatusChange": jnxWxEventMultiPathStatusChange,
       "jnxWxEventDiskFailure": jnxWxEventDiskFailure,
       "jnxWxEventWanPerfStatusChange": jnxWxEventWanPerfStatusChange,
       "jnxWxEventDCQAboveHiWatermark": jnxWxEventDCQAboveHiWatermark,
       "jnxWxEventDCQBelowHiWatermark": jnxWxEventDCQBelowHiWatermark,
       "jnxWxEventPerformanceThreshCrossed": jnxWxEventPerformanceThreshCrossed,
       "jnxWxEventClientLinkDown": jnxWxEventClientLinkDown,
       "jnxWxEventClientLinkUp": jnxWxEventClientLinkUp}
)
