# SNMP MIB module (JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:50 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxMobileGatewaySgw,) = mibBuilder.importSymbols(
    "JUNIPER-MBG-SMI",
    "jnxMobileGatewaySgw")

(jnxMbgGwIndex,
 jnxMbgGwName) = mibBuilder.importSymbols(
    "JUNIPER-MOBILE-GATEWAYS",
    "jnxMbgGwIndex",
    "jnxMbgGwName")

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

jnxMbgSgwSMMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4)
)
jnxMbgSgwSMMib.setRevisions(
        ("2011-10-03 12:00",
         "2012-03-22 12:00",
         "2012-10-12 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxMbgSgwSMNotifications_ObjectIdentity = ObjectIdentity
jnxMbgSgwSMNotifications = _JnxMbgSgwSMNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0)
)
_JnxMbgSgwSMObjects_ObjectIdentity = ObjectIdentity
jnxMbgSgwSMObjects = _JnxMbgSgwSMObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1)
)
_JnxMbgSgwSMStatsTable_Object = MibTable
jnxMbgSgwSMStatsTable = _JnxMbgSgwSMStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1)
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMStatsTable.setStatus("current")
_JnxMbgSgwSMStatsEntry_Object = MibTableRow
jnxMbgSgwSMStatsEntry = _JnxMbgSgwSMStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1)
)
jnxMbgSgwSMStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMStatsEntry.setStatus("current")
_JnxMbgSgwSessnEstAttmpts_Type = Counter64
_JnxMbgSgwSessnEstAttmpts_Object = MibTableColumn
jnxMbgSgwSessnEstAttmpts = _JnxMbgSgwSessnEstAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 1),
    _JnxMbgSgwSessnEstAttmpts_Type()
)
jnxMbgSgwSessnEstAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSessnEstAttmpts.setStatus("current")
_JnxMbgSgwSuccSessnEst_Type = Counter64
_JnxMbgSgwSuccSessnEst_Object = MibTableColumn
jnxMbgSgwSuccSessnEst = _JnxMbgSgwSuccSessnEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 2),
    _JnxMbgSgwSuccSessnEst_Type()
)
jnxMbgSgwSuccSessnEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccSessnEst.setStatus("current")
_JnxMbgSgwPeerInitDeactv_Type = Counter64
_JnxMbgSgwPeerInitDeactv_Object = MibTableColumn
jnxMbgSgwPeerInitDeactv = _JnxMbgSgwPeerInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 3),
    _JnxMbgSgwPeerInitDeactv_Type()
)
jnxMbgSgwPeerInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPeerInitDeactv.setStatus("deprecated")
_JnxMbgSgwPeerInitSuccDeactv_Type = Counter64
_JnxMbgSgwPeerInitSuccDeactv_Object = MibTableColumn
jnxMbgSgwPeerInitSuccDeactv = _JnxMbgSgwPeerInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 4),
    _JnxMbgSgwPeerInitSuccDeactv_Type()
)
jnxMbgSgwPeerInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwPeerInitSuccDeactv.setStatus("deprecated")
_JnxMbgSgwGwInitDeactv_Type = Counter64
_JnxMbgSgwGwInitDeactv_Object = MibTableColumn
jnxMbgSgwGwInitDeactv = _JnxMbgSgwGwInitDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 5),
    _JnxMbgSgwGwInitDeactv_Type()
)
jnxMbgSgwGwInitDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGwInitDeactv.setStatus("deprecated")
_JnxMbgSgwGwInitSuccDeactv_Type = Counter64
_JnxMbgSgwGwInitSuccDeactv_Object = MibTableColumn
jnxMbgSgwGwInitSuccDeactv = _JnxMbgSgwGwInitSuccDeactv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 6),
    _JnxMbgSgwGwInitSuccDeactv_Type()
)
jnxMbgSgwGwInitSuccDeactv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGwInitSuccDeactv.setStatus("deprecated")
_JnxMbgSgwGtpStatsGnS5S8InpPkt_Type = Counter64
_JnxMbgSgwGtpStatsGnS5S8InpPkt_Object = MibTableColumn
jnxMbgSgwGtpStatsGnS5S8InpPkt = _JnxMbgSgwGtpStatsGnS5S8InpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 7),
    _JnxMbgSgwGtpStatsGnS5S8InpPkt_Type()
)
jnxMbgSgwGtpStatsGnS5S8InpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsGnS5S8InpPkt.setStatus("current")
_JnxMbgSgwGtpStatsGnS5S8InpByt_Type = Counter64
_JnxMbgSgwGtpStatsGnS5S8InpByt_Object = MibTableColumn
jnxMbgSgwGtpStatsGnS5S8InpByt = _JnxMbgSgwGtpStatsGnS5S8InpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 8),
    _JnxMbgSgwGtpStatsGnS5S8InpByt_Type()
)
jnxMbgSgwGtpStatsGnS5S8InpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsGnS5S8InpByt.setStatus("current")
_JnxMbgSgwGtpStatsGnS5S8OutPkt_Type = Counter64
_JnxMbgSgwGtpStatsGnS5S8OutPkt_Object = MibTableColumn
jnxMbgSgwGtpStatsGnS5S8OutPkt = _JnxMbgSgwGtpStatsGnS5S8OutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 9),
    _JnxMbgSgwGtpStatsGnS5S8OutPkt_Type()
)
jnxMbgSgwGtpStatsGnS5S8OutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsGnS5S8OutPkt.setStatus("current")
_JnxMbgSgwGtpStatsGnS5S8OutByt_Type = Counter64
_JnxMbgSgwGtpStatsGnS5S8OutByt_Object = MibTableColumn
jnxMbgSgwGtpStatsGnS5S8OutByt = _JnxMbgSgwGtpStatsGnS5S8OutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 10),
    _JnxMbgSgwGtpStatsGnS5S8OutByt_Type()
)
jnxMbgSgwGtpStatsGnS5S8OutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsGnS5S8OutByt.setStatus("current")
_JnxMbgSgwGtpStatsS1uInpPkt_Type = Counter64
_JnxMbgSgwGtpStatsS1uInpPkt_Object = MibTableColumn
jnxMbgSgwGtpStatsS1uInpPkt = _JnxMbgSgwGtpStatsS1uInpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 11),
    _JnxMbgSgwGtpStatsS1uInpPkt_Type()
)
jnxMbgSgwGtpStatsS1uInpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsS1uInpPkt.setStatus("current")
_JnxMbgSgwGtpStatsS1uInpByt_Type = Counter64
_JnxMbgSgwGtpStatsS1uInpByt_Object = MibTableColumn
jnxMbgSgwGtpStatsS1uInpByt = _JnxMbgSgwGtpStatsS1uInpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 12),
    _JnxMbgSgwGtpStatsS1uInpByt_Type()
)
jnxMbgSgwGtpStatsS1uInpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsS1uInpByt.setStatus("current")
_JnxMbgSgwGtpStatsS1uOutPkt_Type = Counter64
_JnxMbgSgwGtpStatsS1uOutPkt_Object = MibTableColumn
jnxMbgSgwGtpStatsS1uOutPkt = _JnxMbgSgwGtpStatsS1uOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 13),
    _JnxMbgSgwGtpStatsS1uOutPkt_Type()
)
jnxMbgSgwGtpStatsS1uOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsS1uOutPkt.setStatus("current")
_JnxMbgSgwGtpStatsS1uOutByt_Type = Counter64
_JnxMbgSgwGtpStatsS1uOutByt_Object = MibTableColumn
jnxMbgSgwGtpStatsS1uOutByt = _JnxMbgSgwGtpStatsS1uOutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 14),
    _JnxMbgSgwGtpStatsS1uOutByt_Type()
)
jnxMbgSgwGtpStatsS1uOutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwGtpStatsS1uOutByt.setStatus("current")
_JnxMbgSgwDedBrCrtAttmpts_Type = Counter64
_JnxMbgSgwDedBrCrtAttmpts_Object = MibTableColumn
jnxMbgSgwDedBrCrtAttmpts = _JnxMbgSgwDedBrCrtAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 15),
    _JnxMbgSgwDedBrCrtAttmpts_Type()
)
jnxMbgSgwDedBrCrtAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDedBrCrtAttmpts.setStatus("current")
_JnxMbgSgwSuccDedBrCrt_Type = Counter64
_JnxMbgSgwSuccDedBrCrt_Object = MibTableColumn
jnxMbgSgwSuccDedBrCrt = _JnxMbgSgwSuccDedBrCrt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 16),
    _JnxMbgSgwSuccDedBrCrt_Type()
)
jnxMbgSgwSuccDedBrCrt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccDedBrCrt.setStatus("current")
_JnxMbgSgwSessnDeActvAttmpts_Type = Counter64
_JnxMbgSgwSessnDeActvAttmpts_Object = MibTableColumn
jnxMbgSgwSessnDeActvAttmpts = _JnxMbgSgwSessnDeActvAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 17),
    _JnxMbgSgwSessnDeActvAttmpts_Type()
)
jnxMbgSgwSessnDeActvAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSessnDeActvAttmpts.setStatus("current")
_JnxMbgSgwSuccSessnDeActv_Type = Counter64
_JnxMbgSgwSuccSessnDeActv_Object = MibTableColumn
jnxMbgSgwSuccSessnDeActv = _JnxMbgSgwSuccSessnDeActv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 18),
    _JnxMbgSgwSuccSessnDeActv_Type()
)
jnxMbgSgwSuccSessnDeActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccSessnDeActv.setStatus("current")
_JnxMbgSgwDedBrDeActvAttmpts_Type = Counter64
_JnxMbgSgwDedBrDeActvAttmpts_Object = MibTableColumn
jnxMbgSgwDedBrDeActvAttmpts = _JnxMbgSgwDedBrDeActvAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 19),
    _JnxMbgSgwDedBrDeActvAttmpts_Type()
)
jnxMbgSgwDedBrDeActvAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwDedBrDeActvAttmpts.setStatus("current")
_JnxMbgSgwSuccDedBrDeActv_Type = Counter64
_JnxMbgSgwSuccDedBrDeActv_Object = MibTableColumn
jnxMbgSgwSuccDedBrDeActv = _JnxMbgSgwSuccDedBrDeActv_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 20),
    _JnxMbgSgwSuccDedBrDeActv_Type()
)
jnxMbgSgwSuccDedBrDeActv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccDedBrDeActv.setStatus("current")
_JnxMbgSgwIntrRatHoAttmpts_Type = Counter64
_JnxMbgSgwIntrRatHoAttmpts_Object = MibTableColumn
jnxMbgSgwIntrRatHoAttmpts = _JnxMbgSgwIntrRatHoAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 21),
    _JnxMbgSgwIntrRatHoAttmpts_Type()
)
jnxMbgSgwIntrRatHoAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIntrRatHoAttmpts.setStatus("current")
_JnxMbgSgwSuccIntrRatHo_Type = Counter64
_JnxMbgSgwSuccIntrRatHo_Object = MibTableColumn
jnxMbgSgwSuccIntrRatHo = _JnxMbgSgwSuccIntrRatHo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 22),
    _JnxMbgSgwSuccIntrRatHo_Type()
)
jnxMbgSgwSuccIntrRatHo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccIntrRatHo.setStatus("current")
_JnxMbgSgwX2HoAttmpts_Type = Counter64
_JnxMbgSgwX2HoAttmpts_Object = MibTableColumn
jnxMbgSgwX2HoAttmpts = _JnxMbgSgwX2HoAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 23),
    _JnxMbgSgwX2HoAttmpts_Type()
)
jnxMbgSgwX2HoAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwX2HoAttmpts.setStatus("current")
_JnxMbgSgwSuccX2Ho_Type = Counter64
_JnxMbgSgwSuccX2Ho_Object = MibTableColumn
jnxMbgSgwSuccX2Ho = _JnxMbgSgwSuccX2Ho_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 24),
    _JnxMbgSgwSuccX2Ho_Type()
)
jnxMbgSgwSuccX2Ho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccX2Ho.setStatus("current")
_JnxMbgSgwS1HoAttmpts_Type = Counter64
_JnxMbgSgwS1HoAttmpts_Object = MibTableColumn
jnxMbgSgwS1HoAttmpts = _JnxMbgSgwS1HoAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 25),
    _JnxMbgSgwS1HoAttmpts_Type()
)
jnxMbgSgwS1HoAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwS1HoAttmpts.setStatus("current")
_JnxMbgSgwSuccS1Ho_Type = Counter64
_JnxMbgSgwSuccS1Ho_Object = MibTableColumn
jnxMbgSgwSuccS1Ho = _JnxMbgSgwSuccS1Ho_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 26),
    _JnxMbgSgwSuccS1Ho_Type()
)
jnxMbgSgwSuccS1Ho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccS1Ho.setStatus("current")
_JnxMbgSgwIdlMdTauRauAttmpts_Type = Counter64
_JnxMbgSgwIdlMdTauRauAttmpts_Object = MibTableColumn
jnxMbgSgwIdlMdTauRauAttmpts = _JnxMbgSgwIdlMdTauRauAttmpts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 27),
    _JnxMbgSgwIdlMdTauRauAttmpts_Type()
)
jnxMbgSgwIdlMdTauRauAttmpts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIdlMdTauRauAttmpts.setStatus("current")
_JnxMbgSgwSuccIdlMdTauRau_Type = Counter64
_JnxMbgSgwSuccIdlMdTauRau_Object = MibTableColumn
jnxMbgSgwSuccIdlMdTauRau = _JnxMbgSgwSuccIdlMdTauRau_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 28),
    _JnxMbgSgwSuccIdlMdTauRau_Type()
)
jnxMbgSgwSuccIdlMdTauRau.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccIdlMdTauRau.setStatus("current")
_JnxMbgSgwServReqAttmempts_Type = Counter64
_JnxMbgSgwServReqAttmempts_Object = MibTableColumn
jnxMbgSgwServReqAttmempts = _JnxMbgSgwServReqAttmempts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 29),
    _JnxMbgSgwServReqAttmempts_Type()
)
jnxMbgSgwServReqAttmempts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwServReqAttmempts.setStatus("current")
_JnxMbgSgwSuccServReq_Type = Counter64
_JnxMbgSgwSuccServReq_Object = MibTableColumn
jnxMbgSgwSuccServReq = _JnxMbgSgwSuccServReq_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 1, 1, 30),
    _JnxMbgSgwSuccServReq_Type()
)
jnxMbgSgwSuccServReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuccServReq.setStatus("current")
_JnxMbgSgwSMStatusTable_Object = MibTable
jnxMbgSgwSMStatusTable = _JnxMbgSgwSMStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2)
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMStatusTable.setStatus("current")
_JnxMbgSgwSMStatusEntry_Object = MibTableRow
jnxMbgSgwSMStatusEntry = _JnxMbgSgwSMStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1)
)
jnxMbgSgwSMStatusEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMStatusEntry.setStatus("current")
_JnxMbgSgwActvSubscribers_Type = CounterBasedGauge64
_JnxMbgSgwActvSubscribers_Object = MibTableColumn
jnxMbgSgwActvSubscribers = _JnxMbgSgwActvSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 1),
    _JnxMbgSgwActvSubscribers_Type()
)
jnxMbgSgwActvSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwActvSubscribers.setStatus("current")
_JnxMbgSgwActvSessions_Type = CounterBasedGauge64
_JnxMbgSgwActvSessions_Object = MibTableColumn
jnxMbgSgwActvSessions = _JnxMbgSgwActvSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 2),
    _JnxMbgSgwActvSessions_Type()
)
jnxMbgSgwActvSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwActvSessions.setStatus("current")
_JnxMbgSgwActvBearers_Type = CounterBasedGauge64
_JnxMbgSgwActvBearers_Object = MibTableColumn
jnxMbgSgwActvBearers = _JnxMbgSgwActvBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 3),
    _JnxMbgSgwActvBearers_Type()
)
jnxMbgSgwActvBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwActvBearers.setStatus("current")
_JnxMbgSgwIdleSubscribers_Type = CounterBasedGauge64
_JnxMbgSgwIdleSubscribers_Object = MibTableColumn
jnxMbgSgwIdleSubscribers = _JnxMbgSgwIdleSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 4),
    _JnxMbgSgwIdleSubscribers_Type()
)
jnxMbgSgwIdleSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIdleSubscribers.setStatus("current")
_JnxMbgSgwIdleSessions_Type = CounterBasedGauge64
_JnxMbgSgwIdleSessions_Object = MibTableColumn
jnxMbgSgwIdleSessions = _JnxMbgSgwIdleSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 5),
    _JnxMbgSgwIdleSessions_Type()
)
jnxMbgSgwIdleSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIdleSessions.setStatus("current")
_JnxMbgSgwIdleBearers_Type = CounterBasedGauge64
_JnxMbgSgwIdleBearers_Object = MibTableColumn
jnxMbgSgwIdleBearers = _JnxMbgSgwIdleBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 6),
    _JnxMbgSgwIdleBearers_Type()
)
jnxMbgSgwIdleBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwIdleBearers.setStatus("current")
_JnxMbgSgwSuspSubscribers_Type = CounterBasedGauge64
_JnxMbgSgwSuspSubscribers_Object = MibTableColumn
jnxMbgSgwSuspSubscribers = _JnxMbgSgwSuspSubscribers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 7),
    _JnxMbgSgwSuspSubscribers_Type()
)
jnxMbgSgwSuspSubscribers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspSubscribers.setStatus("current")
_JnxMbgSgwSuspSessions_Type = CounterBasedGauge64
_JnxMbgSgwSuspSessions_Object = MibTableColumn
jnxMbgSgwSuspSessions = _JnxMbgSgwSuspSessions_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 8),
    _JnxMbgSgwSuspSessions_Type()
)
jnxMbgSgwSuspSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspSessions.setStatus("current")
_JnxMbgSgwSuspBearers_Type = CounterBasedGauge64
_JnxMbgSgwSuspBearers_Object = MibTableColumn
jnxMbgSgwSuspBearers = _JnxMbgSgwSuspBearers_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 9),
    _JnxMbgSgwSuspBearers_Type()
)
jnxMbgSgwSuspBearers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwSuspBearers.setStatus("current")
_JnxMbgSgwCPUUtil_Type = Gauge32
_JnxMbgSgwCPUUtil_Object = MibTableColumn
jnxMbgSgwCPUUtil = _JnxMbgSgwCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 10),
    _JnxMbgSgwCPUUtil_Type()
)
jnxMbgSgwCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwCPUUtil.setStatus("current")
_JnxMbgSgwMemoryUtil_Type = Gauge32
_JnxMbgSgwMemoryUtil_Object = MibTableColumn
jnxMbgSgwMemoryUtil = _JnxMbgSgwMemoryUtil_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 2, 1, 11),
    _JnxMbgSgwMemoryUtil_Type()
)
jnxMbgSgwMemoryUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwMemoryUtil.setStatus("current")
_JnxMbgSgwSMNotificationVars_ObjectIdentity = ObjectIdentity
jnxMbgSgwSMNotificationVars = _JnxMbgSgwSMNotificationVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3)
)
_JnxMbgGwSpicName_Type = DisplayString
_JnxMbgGwSpicName_Object = MibScalar
jnxMbgGwSpicName = _JnxMbgGwSpicName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 1),
    _JnxMbgGwSpicName_Type()
)
jnxMbgGwSpicName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgGwSpicName.setStatus("current")
_JnxMbgSgwTrapGwIndex_Type = Unsigned32
_JnxMbgSgwTrapGwIndex_Object = MibScalar
jnxMbgSgwTrapGwIndex = _JnxMbgSgwTrapGwIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 2),
    _JnxMbgSgwTrapGwIndex_Type()
)
jnxMbgSgwTrapGwIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwTrapGwIndex.setStatus("current")
_JnxMbgSgwTrapGwName_Type = DisplayString
_JnxMbgSgwTrapGwName_Object = MibScalar
jnxMbgSgwTrapGwName = _JnxMbgSgwTrapGwName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 3),
    _JnxMbgSgwTrapGwName_Type()
)
jnxMbgSgwTrapGwName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwTrapGwName.setStatus("current")
_JnxMbgSgwSMInterfaceName_Type = DisplayString
_JnxMbgSgwSMInterfaceName_Object = MibScalar
jnxMbgSgwSMInterfaceName = _JnxMbgSgwSMInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 4),
    _JnxMbgSgwSMInterfaceName_Type()
)
jnxMbgSgwSMInterfaceName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwSMInterfaceName.setStatus("current")


class _JnxMbgSgwPrevMMState_Type(Integer32):
    """Custom type jnxMbgSgwPrevMMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mmactivephase", 3),
          ("mmdefault", 0),
          ("mminphase", 2),
          ("mmnormalphase", 1),
          ("mmoutphase", 4))
    )


_JnxMbgSgwPrevMMState_Type.__name__ = "Integer32"
_JnxMbgSgwPrevMMState_Object = MibScalar
jnxMbgSgwPrevMMState = _JnxMbgSgwPrevMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 5),
    _JnxMbgSgwPrevMMState_Type()
)
jnxMbgSgwPrevMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwPrevMMState.setStatus("current")


class _JnxMbgSgwNewMMState_Type(Integer32):
    """Custom type jnxMbgSgwNewMMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("mmactivephase", 3),
          ("mmdefault", 0),
          ("mminphase", 2),
          ("mmnormalphase", 1),
          ("mmoutphase", 4))
    )


_JnxMbgSgwNewMMState_Type.__name__ = "Integer32"
_JnxMbgSgwNewMMState_Object = MibScalar
jnxMbgSgwNewMMState = _JnxMbgSgwNewMMState_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 3, 6),
    _JnxMbgSgwNewMMState_Type()
)
jnxMbgSgwNewMMState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxMbgSgwNewMMState.setStatus("current")
_JnxMbgSgwSMClRateStatsTable_Object = MibTable
jnxMbgSgwSMClRateStatsTable = _JnxMbgSgwSMClRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4)
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMClRateStatsTable.setStatus("current")
_JnxMbgSgwSMClRateStatsEntry_Object = MibTableRow
jnxMbgSgwSMClRateStatsEntry = _JnxMbgSgwSMClRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1)
)
jnxMbgSgwSMClRateStatsEntry.setIndexNames(
    (0, "JUNIPER-MOBILE-GATEWAYS", "jnxMbgGwIndex"),
)
if mibBuilder.loadTexts:
    jnxMbgSgwSMClRateStatsEntry.setStatus("current")
_JnxMbgSgwClRateIntervalMin_Type = Unsigned32
_JnxMbgSgwClRateIntervalMin_Object = MibTableColumn
jnxMbgSgwClRateIntervalMin = _JnxMbgSgwClRateIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 1),
    _JnxMbgSgwClRateIntervalMin_Type()
)
jnxMbgSgwClRateIntervalMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateIntervalMin.setStatus("current")
_JnxMbgSgwClRateSuccSessnEst_Type = Counter64
_JnxMbgSgwClRateSuccSessnEst_Object = MibTableColumn
jnxMbgSgwClRateSuccSessnEst = _JnxMbgSgwClRateSuccSessnEst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 2),
    _JnxMbgSgwClRateSuccSessnEst_Type()
)
jnxMbgSgwClRateSuccSessnEst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateSuccSessnEst.setStatus("current")
_JnxMbgSgwClRateSuccSessnDel_Type = Counter64
_JnxMbgSgwClRateSuccSessnDel_Object = MibTableColumn
jnxMbgSgwClRateSuccSessnDel = _JnxMbgSgwClRateSuccSessnDel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 3),
    _JnxMbgSgwClRateSuccSessnDel_Type()
)
jnxMbgSgwClRateSuccSessnDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateSuccSessnDel.setStatus("current")
_JnxMbgSgwClRateStatsGnInpPkt_Type = Counter64
_JnxMbgSgwClRateStatsGnInpPkt_Object = MibTableColumn
jnxMbgSgwClRateStatsGnInpPkt = _JnxMbgSgwClRateStatsGnInpPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 4),
    _JnxMbgSgwClRateStatsGnInpPkt_Type()
)
jnxMbgSgwClRateStatsGnInpPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateStatsGnInpPkt.setStatus("current")
_JnxMbgSgwClRateStatsGnOutPkt_Type = Counter64
_JnxMbgSgwClRateStatsGnOutPkt_Object = MibTableColumn
jnxMbgSgwClRateStatsGnOutPkt = _JnxMbgSgwClRateStatsGnOutPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 5),
    _JnxMbgSgwClRateStatsGnOutPkt_Type()
)
jnxMbgSgwClRateStatsGnOutPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateStatsGnOutPkt.setStatus("current")
_JnxMbgSgwClRateStatsGnInpByt_Type = Counter64
_JnxMbgSgwClRateStatsGnInpByt_Object = MibTableColumn
jnxMbgSgwClRateStatsGnInpByt = _JnxMbgSgwClRateStatsGnInpByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 6),
    _JnxMbgSgwClRateStatsGnInpByt_Type()
)
jnxMbgSgwClRateStatsGnInpByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateStatsGnInpByt.setStatus("current")
_JnxMbgSgwClRateStatsGnOutByt_Type = Counter64
_JnxMbgSgwClRateStatsGnOutByt_Object = MibTableColumn
jnxMbgSgwClRateStatsGnOutByt = _JnxMbgSgwClRateStatsGnOutByt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 1, 4, 1, 7),
    _JnxMbgSgwClRateStatsGnOutByt_Type()
)
jnxMbgSgwClRateStatsGnOutByt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxMbgSgwClRateStatsGnOutByt.setStatus("current")

# Managed Objects groups


# Notification objects

jnxMbgSgwCpuThrStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 1)
)
jnxMbgSgwCpuThrStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCpuThrStatusHi.setStatus(
        "current"
    )

jnxMbgSgwCpuThrStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 2)
)
jnxMbgSgwCpuThrStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCpuThrStatusLow.setStatus(
        "current"
    )

jnxMbgSgwCpuThrStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 3)
)
jnxMbgSgwCpuThrStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwCpuThrStatusClear.setStatus(
        "current"
    )

jnxMbgSgwMemThrStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 4)
)
jnxMbgSgwMemThrStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMemThrStatusHi.setStatus(
        "current"
    )

jnxMbgSgwMemThrStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 5)
)
jnxMbgSgwMemThrStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMemThrStatusLow.setStatus(
        "current"
    )

jnxMbgSgwMemThrStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 6)
)
jnxMbgSgwMemThrStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMemThrStatusClear.setStatus(
        "current"
    )

jnxMbgSgwPFEMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 7)
)
jnxMbgSgwPFEMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwPFEMMStateChange.setStatus(
        "current"
    )

jnxMbgSgwMSMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 8)
)
jnxMbgSgwMSMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwMSMMStateChange.setStatus(
        "current"
    )

jnxMbgSgwAPFEMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 9)
)
jnxMbgSgwAPFEMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwAPFEMMStateChange.setStatus(
        "current"
    )

jnxMbgSgwAMSMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 10)
)
jnxMbgSgwAMSMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwSMInterfaceName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwAMSMMStateChange.setStatus(
        "current"
    )

jnxMbgSgwQosBearerThrStatusHi = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 11)
)
jnxMbgSgwQosBearerThrStatusHi.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwQosBearerThrStatusHi.setStatus(
        "current"
    )

jnxMbgSgwQosBearerThrStatusLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 12)
)
jnxMbgSgwQosBearerThrStatusLow.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwQosBearerThrStatusLow.setStatus(
        "current"
    )

jnxMbgSgwQosBearerThrStatusClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 13)
)
jnxMbgSgwQosBearerThrStatusClear.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwIndex"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwQosBearerThrStatusClear.setStatus(
        "current"
    )

jnxMbgSgwGatewayMMStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 66, 2, 4, 0, 14)
)
jnxMbgSgwGatewayMMStateChange.setObjects(
      *(("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwTrapGwName"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwPrevMMState"),
        ("JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB", "jnxMbgSgwNewMMState"))
)
if mibBuilder.loadTexts:
    jnxMbgSgwGatewayMMStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-MOBILE-GATEWAY-SGW-SM-MIB",
    **{"jnxMbgSgwSMMib": jnxMbgSgwSMMib,
       "jnxMbgSgwSMNotifications": jnxMbgSgwSMNotifications,
       "jnxMbgSgwCpuThrStatusHi": jnxMbgSgwCpuThrStatusHi,
       "jnxMbgSgwCpuThrStatusLow": jnxMbgSgwCpuThrStatusLow,
       "jnxMbgSgwCpuThrStatusClear": jnxMbgSgwCpuThrStatusClear,
       "jnxMbgSgwMemThrStatusHi": jnxMbgSgwMemThrStatusHi,
       "jnxMbgSgwMemThrStatusLow": jnxMbgSgwMemThrStatusLow,
       "jnxMbgSgwMemThrStatusClear": jnxMbgSgwMemThrStatusClear,
       "jnxMbgSgwPFEMMStateChange": jnxMbgSgwPFEMMStateChange,
       "jnxMbgSgwMSMMStateChange": jnxMbgSgwMSMMStateChange,
       "jnxMbgSgwAPFEMMStateChange": jnxMbgSgwAPFEMMStateChange,
       "jnxMbgSgwAMSMMStateChange": jnxMbgSgwAMSMMStateChange,
       "jnxMbgSgwQosBearerThrStatusHi": jnxMbgSgwQosBearerThrStatusHi,
       "jnxMbgSgwQosBearerThrStatusLow": jnxMbgSgwQosBearerThrStatusLow,
       "jnxMbgSgwQosBearerThrStatusClear": jnxMbgSgwQosBearerThrStatusClear,
       "jnxMbgSgwGatewayMMStateChange": jnxMbgSgwGatewayMMStateChange,
       "jnxMbgSgwSMObjects": jnxMbgSgwSMObjects,
       "jnxMbgSgwSMStatsTable": jnxMbgSgwSMStatsTable,
       "jnxMbgSgwSMStatsEntry": jnxMbgSgwSMStatsEntry,
       "jnxMbgSgwSessnEstAttmpts": jnxMbgSgwSessnEstAttmpts,
       "jnxMbgSgwSuccSessnEst": jnxMbgSgwSuccSessnEst,
       "jnxMbgSgwPeerInitDeactv": jnxMbgSgwPeerInitDeactv,
       "jnxMbgSgwPeerInitSuccDeactv": jnxMbgSgwPeerInitSuccDeactv,
       "jnxMbgSgwGwInitDeactv": jnxMbgSgwGwInitDeactv,
       "jnxMbgSgwGwInitSuccDeactv": jnxMbgSgwGwInitSuccDeactv,
       "jnxMbgSgwGtpStatsGnS5S8InpPkt": jnxMbgSgwGtpStatsGnS5S8InpPkt,
       "jnxMbgSgwGtpStatsGnS5S8InpByt": jnxMbgSgwGtpStatsGnS5S8InpByt,
       "jnxMbgSgwGtpStatsGnS5S8OutPkt": jnxMbgSgwGtpStatsGnS5S8OutPkt,
       "jnxMbgSgwGtpStatsGnS5S8OutByt": jnxMbgSgwGtpStatsGnS5S8OutByt,
       "jnxMbgSgwGtpStatsS1uInpPkt": jnxMbgSgwGtpStatsS1uInpPkt,
       "jnxMbgSgwGtpStatsS1uInpByt": jnxMbgSgwGtpStatsS1uInpByt,
       "jnxMbgSgwGtpStatsS1uOutPkt": jnxMbgSgwGtpStatsS1uOutPkt,
       "jnxMbgSgwGtpStatsS1uOutByt": jnxMbgSgwGtpStatsS1uOutByt,
       "jnxMbgSgwDedBrCrtAttmpts": jnxMbgSgwDedBrCrtAttmpts,
       "jnxMbgSgwSuccDedBrCrt": jnxMbgSgwSuccDedBrCrt,
       "jnxMbgSgwSessnDeActvAttmpts": jnxMbgSgwSessnDeActvAttmpts,
       "jnxMbgSgwSuccSessnDeActv": jnxMbgSgwSuccSessnDeActv,
       "jnxMbgSgwDedBrDeActvAttmpts": jnxMbgSgwDedBrDeActvAttmpts,
       "jnxMbgSgwSuccDedBrDeActv": jnxMbgSgwSuccDedBrDeActv,
       "jnxMbgSgwIntrRatHoAttmpts": jnxMbgSgwIntrRatHoAttmpts,
       "jnxMbgSgwSuccIntrRatHo": jnxMbgSgwSuccIntrRatHo,
       "jnxMbgSgwX2HoAttmpts": jnxMbgSgwX2HoAttmpts,
       "jnxMbgSgwSuccX2Ho": jnxMbgSgwSuccX2Ho,
       "jnxMbgSgwS1HoAttmpts": jnxMbgSgwS1HoAttmpts,
       "jnxMbgSgwSuccS1Ho": jnxMbgSgwSuccS1Ho,
       "jnxMbgSgwIdlMdTauRauAttmpts": jnxMbgSgwIdlMdTauRauAttmpts,
       "jnxMbgSgwSuccIdlMdTauRau": jnxMbgSgwSuccIdlMdTauRau,
       "jnxMbgSgwServReqAttmempts": jnxMbgSgwServReqAttmempts,
       "jnxMbgSgwSuccServReq": jnxMbgSgwSuccServReq,
       "jnxMbgSgwSMStatusTable": jnxMbgSgwSMStatusTable,
       "jnxMbgSgwSMStatusEntry": jnxMbgSgwSMStatusEntry,
       "jnxMbgSgwActvSubscribers": jnxMbgSgwActvSubscribers,
       "jnxMbgSgwActvSessions": jnxMbgSgwActvSessions,
       "jnxMbgSgwActvBearers": jnxMbgSgwActvBearers,
       "jnxMbgSgwIdleSubscribers": jnxMbgSgwIdleSubscribers,
       "jnxMbgSgwIdleSessions": jnxMbgSgwIdleSessions,
       "jnxMbgSgwIdleBearers": jnxMbgSgwIdleBearers,
       "jnxMbgSgwSuspSubscribers": jnxMbgSgwSuspSubscribers,
       "jnxMbgSgwSuspSessions": jnxMbgSgwSuspSessions,
       "jnxMbgSgwSuspBearers": jnxMbgSgwSuspBearers,
       "jnxMbgSgwCPUUtil": jnxMbgSgwCPUUtil,
       "jnxMbgSgwMemoryUtil": jnxMbgSgwMemoryUtil,
       "jnxMbgSgwSMNotificationVars": jnxMbgSgwSMNotificationVars,
       "jnxMbgGwSpicName": jnxMbgGwSpicName,
       "jnxMbgSgwTrapGwIndex": jnxMbgSgwTrapGwIndex,
       "jnxMbgSgwTrapGwName": jnxMbgSgwTrapGwName,
       "jnxMbgSgwSMInterfaceName": jnxMbgSgwSMInterfaceName,
       "jnxMbgSgwPrevMMState": jnxMbgSgwPrevMMState,
       "jnxMbgSgwNewMMState": jnxMbgSgwNewMMState,
       "jnxMbgSgwSMClRateStatsTable": jnxMbgSgwSMClRateStatsTable,
       "jnxMbgSgwSMClRateStatsEntry": jnxMbgSgwSMClRateStatsEntry,
       "jnxMbgSgwClRateIntervalMin": jnxMbgSgwClRateIntervalMin,
       "jnxMbgSgwClRateSuccSessnEst": jnxMbgSgwClRateSuccSessnEst,
       "jnxMbgSgwClRateSuccSessnDel": jnxMbgSgwClRateSuccSessnDel,
       "jnxMbgSgwClRateStatsGnInpPkt": jnxMbgSgwClRateStatsGnInpPkt,
       "jnxMbgSgwClRateStatsGnOutPkt": jnxMbgSgwClRateStatsGnOutPkt,
       "jnxMbgSgwClRateStatsGnInpByt": jnxMbgSgwClRateStatsGnInpByt,
       "jnxMbgSgwClRateStatsGnOutByt": jnxMbgSgwClRateStatsGnOutByt}
)
