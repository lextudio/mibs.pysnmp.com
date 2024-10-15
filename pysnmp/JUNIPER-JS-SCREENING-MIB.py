# SNMP MIB module (JUNIPER-JS-SCREENING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-JS-SCREENING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:13:21 2024
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

(ifName,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifName")

(jnxJsScreening,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsScreening")

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

jnxJsScreenMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1)
)
jnxJsScreenMIB.setRevisions(
        ("2014-04-02 00:00",
         "2013-11-07 00:00",
         "2013-06-06 00:00",
         "2012-04-06 10:30",
         "2009-02-04 00:00",
         "2007-09-24 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsScreenNotifications_ObjectIdentity = ObjectIdentity
jnxJsScreenNotifications = _JnxJsScreenNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 0)
)
_JnxJsScreenObjects_ObjectIdentity = ObjectIdentity
jnxJsScreenObjects = _JnxJsScreenObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1)
)
_JnxJsScreenMonTable_Object = MibTable
jnxJsScreenMonTable = _JnxJsScreenMonTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJsScreenMonTable.setStatus("current")
_JnxJsScreenMonEntry_Object = MibTableRow
jnxJsScreenMonEntry = _JnxJsScreenMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1)
)
jnxJsScreenMonEntry.setIndexNames(
    (1, "JUNIPER-JS-SCREENING-MIB", "jnxJsScreenZoneName"),
)
if mibBuilder.loadTexts:
    jnxJsScreenMonEntry.setStatus("current")


class _JnxJsScreenZoneName_Type(DisplayString):
    """Custom type jnxJsScreenZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsScreenZoneName_Type.__name__ = "DisplayString"
_JnxJsScreenZoneName_Object = MibTableColumn
jnxJsScreenZoneName = _JnxJsScreenZoneName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 1),
    _JnxJsScreenZoneName_Type()
)
jnxJsScreenZoneName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsScreenZoneName.setStatus("current")
_JnxJsScreenNumOfIf_Type = Integer32
_JnxJsScreenNumOfIf_Object = MibTableColumn
jnxJsScreenNumOfIf = _JnxJsScreenNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 2),
    _JnxJsScreenNumOfIf_Type()
)
jnxJsScreenNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenNumOfIf.setStatus("current")
_JnxJsScreenMonSynAttk_Type = Counter64
_JnxJsScreenMonSynAttk_Object = MibTableColumn
jnxJsScreenMonSynAttk = _JnxJsScreenMonSynAttk_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 3),
    _JnxJsScreenMonSynAttk_Type()
)
jnxJsScreenMonSynAttk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSynAttk.setStatus("current")
_JnxJsScreenMonTearDrop_Type = Counter64
_JnxJsScreenMonTearDrop_Object = MibTableColumn
jnxJsScreenMonTearDrop = _JnxJsScreenMonTearDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 4),
    _JnxJsScreenMonTearDrop_Type()
)
jnxJsScreenMonTearDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonTearDrop.setStatus("current")
_JnxJsScreenMonSrcRoute_Type = Counter64
_JnxJsScreenMonSrcRoute_Object = MibTableColumn
jnxJsScreenMonSrcRoute = _JnxJsScreenMonSrcRoute_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 5),
    _JnxJsScreenMonSrcRoute_Type()
)
jnxJsScreenMonSrcRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSrcRoute.setStatus("current")
_JnxJsScreenMonPingDeath_Type = Counter64
_JnxJsScreenMonPingDeath_Object = MibTableColumn
jnxJsScreenMonPingDeath = _JnxJsScreenMonPingDeath_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 6),
    _JnxJsScreenMonPingDeath_Type()
)
jnxJsScreenMonPingDeath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonPingDeath.setStatus("current")
_JnxJsScreenMonAddrSpoof_Type = Counter64
_JnxJsScreenMonAddrSpoof_Object = MibTableColumn
jnxJsScreenMonAddrSpoof = _JnxJsScreenMonAddrSpoof_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 7),
    _JnxJsScreenMonAddrSpoof_Type()
)
jnxJsScreenMonAddrSpoof.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonAddrSpoof.setStatus("current")
_JnxJsScreenMonLand_Type = Counter64
_JnxJsScreenMonLand_Object = MibTableColumn
jnxJsScreenMonLand = _JnxJsScreenMonLand_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 8),
    _JnxJsScreenMonLand_Type()
)
jnxJsScreenMonLand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonLand.setStatus("current")
_JnxJsScreenMonIcmpFlood_Type = Counter64
_JnxJsScreenMonIcmpFlood_Object = MibTableColumn
jnxJsScreenMonIcmpFlood = _JnxJsScreenMonIcmpFlood_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 9),
    _JnxJsScreenMonIcmpFlood_Type()
)
jnxJsScreenMonIcmpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIcmpFlood.setStatus("current")
_JnxJsScreenMonUdpFlood_Type = Counter64
_JnxJsScreenMonUdpFlood_Object = MibTableColumn
jnxJsScreenMonUdpFlood = _JnxJsScreenMonUdpFlood_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 10),
    _JnxJsScreenMonUdpFlood_Type()
)
jnxJsScreenMonUdpFlood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonUdpFlood.setStatus("current")
_JnxJsScreenMonWinnuke_Type = Counter64
_JnxJsScreenMonWinnuke_Object = MibTableColumn
jnxJsScreenMonWinnuke = _JnxJsScreenMonWinnuke_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 11),
    _JnxJsScreenMonWinnuke_Type()
)
jnxJsScreenMonWinnuke.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonWinnuke.setStatus("current")
_JnxJsScreenMonPortScan_Type = Counter64
_JnxJsScreenMonPortScan_Object = MibTableColumn
jnxJsScreenMonPortScan = _JnxJsScreenMonPortScan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 12),
    _JnxJsScreenMonPortScan_Type()
)
jnxJsScreenMonPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonPortScan.setStatus("current")
_JnxJsScreenMonIpSweep_Type = Counter64
_JnxJsScreenMonIpSweep_Object = MibTableColumn
jnxJsScreenMonIpSweep = _JnxJsScreenMonIpSweep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 13),
    _JnxJsScreenMonIpSweep_Type()
)
jnxJsScreenMonIpSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpSweep.setStatus("current")
_JnxJsScreenMonSynFrag_Type = Counter64
_JnxJsScreenMonSynFrag_Object = MibTableColumn
jnxJsScreenMonSynFrag = _JnxJsScreenMonSynFrag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 14),
    _JnxJsScreenMonSynFrag_Type()
)
jnxJsScreenMonSynFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSynFrag.setStatus("current")
_JnxJsScreenMonTcpNoFlag_Type = Counter64
_JnxJsScreenMonTcpNoFlag_Object = MibTableColumn
jnxJsScreenMonTcpNoFlag = _JnxJsScreenMonTcpNoFlag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 15),
    _JnxJsScreenMonTcpNoFlag_Type()
)
jnxJsScreenMonTcpNoFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonTcpNoFlag.setStatus("current")
_JnxJsScreenMonIpUnknownProt_Type = Counter64
_JnxJsScreenMonIpUnknownProt_Object = MibTableColumn
jnxJsScreenMonIpUnknownProt = _JnxJsScreenMonIpUnknownProt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 16),
    _JnxJsScreenMonIpUnknownProt_Type()
)
jnxJsScreenMonIpUnknownProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpUnknownProt.setStatus("current")
_JnxJsScreenMonIpOptBad_Type = Counter64
_JnxJsScreenMonIpOptBad_Object = MibTableColumn
jnxJsScreenMonIpOptBad = _JnxJsScreenMonIpOptBad_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 17),
    _JnxJsScreenMonIpOptBad_Type()
)
jnxJsScreenMonIpOptBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptBad.setStatus("current")
_JnxJsScreenMonIpOptRecRt_Type = Counter64
_JnxJsScreenMonIpOptRecRt_Object = MibTableColumn
jnxJsScreenMonIpOptRecRt = _JnxJsScreenMonIpOptRecRt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 18),
    _JnxJsScreenMonIpOptRecRt_Type()
)
jnxJsScreenMonIpOptRecRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptRecRt.setStatus("current")
_JnxJsScreenMonIpOptTimestamp_Type = Counter64
_JnxJsScreenMonIpOptTimestamp_Object = MibTableColumn
jnxJsScreenMonIpOptTimestamp = _JnxJsScreenMonIpOptTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 19),
    _JnxJsScreenMonIpOptTimestamp_Type()
)
jnxJsScreenMonIpOptTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptTimestamp.setStatus("current")
_JnxJsScreenMonIpOptSecurity_Type = Counter64
_JnxJsScreenMonIpOptSecurity_Object = MibTableColumn
jnxJsScreenMonIpOptSecurity = _JnxJsScreenMonIpOptSecurity_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 20),
    _JnxJsScreenMonIpOptSecurity_Type()
)
jnxJsScreenMonIpOptSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptSecurity.setStatus("current")
_JnxJsScreenMonIpOptLSR_Type = Counter64
_JnxJsScreenMonIpOptLSR_Object = MibTableColumn
jnxJsScreenMonIpOptLSR = _JnxJsScreenMonIpOptLSR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 21),
    _JnxJsScreenMonIpOptLSR_Type()
)
jnxJsScreenMonIpOptLSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptLSR.setStatus("current")
_JnxJsScreenMonIpOptSSR_Type = Counter64
_JnxJsScreenMonIpOptSSR_Object = MibTableColumn
jnxJsScreenMonIpOptSSR = _JnxJsScreenMonIpOptSSR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 22),
    _JnxJsScreenMonIpOptSSR_Type()
)
jnxJsScreenMonIpOptSSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptSSR.setStatus("current")
_JnxJsScreenMonIpOptStream_Type = Counter64
_JnxJsScreenMonIpOptStream_Object = MibTableColumn
jnxJsScreenMonIpOptStream = _JnxJsScreenMonIpOptStream_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 23),
    _JnxJsScreenMonIpOptStream_Type()
)
jnxJsScreenMonIpOptStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpOptStream.setStatus("current")
_JnxJsScreenMonIcmpFrag_Type = Counter64
_JnxJsScreenMonIcmpFrag_Object = MibTableColumn
jnxJsScreenMonIcmpFrag = _JnxJsScreenMonIcmpFrag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 24),
    _JnxJsScreenMonIcmpFrag_Type()
)
jnxJsScreenMonIcmpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIcmpFrag.setStatus("current")
_JnxJsScreenMonIcmpLarge_Type = Counter64
_JnxJsScreenMonIcmpLarge_Object = MibTableColumn
jnxJsScreenMonIcmpLarge = _JnxJsScreenMonIcmpLarge_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 25),
    _JnxJsScreenMonIcmpLarge_Type()
)
jnxJsScreenMonIcmpLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIcmpLarge.setStatus("current")
_JnxJsScreenMonTcpSynFin_Type = Counter64
_JnxJsScreenMonTcpSynFin_Object = MibTableColumn
jnxJsScreenMonTcpSynFin = _JnxJsScreenMonTcpSynFin_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 26),
    _JnxJsScreenMonTcpSynFin_Type()
)
jnxJsScreenMonTcpSynFin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonTcpSynFin.setStatus("current")
_JnxJsScreenMonTcpFinNoAck_Type = Counter64
_JnxJsScreenMonTcpFinNoAck_Object = MibTableColumn
jnxJsScreenMonTcpFinNoAck = _JnxJsScreenMonTcpFinNoAck_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 27),
    _JnxJsScreenMonTcpFinNoAck_Type()
)
jnxJsScreenMonTcpFinNoAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonTcpFinNoAck.setStatus("current")
_JnxJsScreenMonLimitSessSrc_Type = Counter64
_JnxJsScreenMonLimitSessSrc_Object = MibTableColumn
jnxJsScreenMonLimitSessSrc = _JnxJsScreenMonLimitSessSrc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 28),
    _JnxJsScreenMonLimitSessSrc_Type()
)
jnxJsScreenMonLimitSessSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonLimitSessSrc.setStatus("current")
_JnxJsScreenMonLimitSessDest_Type = Counter64
_JnxJsScreenMonLimitSessDest_Object = MibTableColumn
jnxJsScreenMonLimitSessDest = _JnxJsScreenMonLimitSessDest_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 29),
    _JnxJsScreenMonLimitSessDest_Type()
)
jnxJsScreenMonLimitSessDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonLimitSessDest.setStatus("current")
_JnxJsScreenMonSynAckAck_Type = Counter64
_JnxJsScreenMonSynAckAck_Object = MibTableColumn
jnxJsScreenMonSynAckAck = _JnxJsScreenMonSynAckAck_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 30),
    _JnxJsScreenMonSynAckAck_Type()
)
jnxJsScreenMonSynAckAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSynAckAck.setStatus("current")
_JnxJsScreenMonIpFrag_Type = Counter64
_JnxJsScreenMonIpFrag_Object = MibTableColumn
jnxJsScreenMonIpFrag = _JnxJsScreenMonIpFrag_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 31),
    _JnxJsScreenMonIpFrag_Type()
)
jnxJsScreenMonIpFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpFrag.setStatus("current")
_JnxJsScreenSynAttackThresh_Type = Integer32
_JnxJsScreenSynAttackThresh_Object = MibTableColumn
jnxJsScreenSynAttackThresh = _JnxJsScreenSynAttackThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 32),
    _JnxJsScreenSynAttackThresh_Type()
)
jnxJsScreenSynAttackThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAttackThresh.setStatus("current")
_JnxJsScreenSynAttackTimeout_Type = Integer32
_JnxJsScreenSynAttackTimeout_Object = MibTableColumn
jnxJsScreenSynAttackTimeout = _JnxJsScreenSynAttackTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 33),
    _JnxJsScreenSynAttackTimeout_Type()
)
jnxJsScreenSynAttackTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAttackTimeout.setStatus("current")
_JnxJsScreenSynAttackAlmTh_Type = Integer32
_JnxJsScreenSynAttackAlmTh_Object = MibTableColumn
jnxJsScreenSynAttackAlmTh = _JnxJsScreenSynAttackAlmTh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 34),
    _JnxJsScreenSynAttackAlmTh_Type()
)
jnxJsScreenSynAttackAlmTh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAttackAlmTh.setStatus("current")
_JnxJsScreenSynAttackQueSize_Type = Integer32
_JnxJsScreenSynAttackQueSize_Object = MibTableColumn
jnxJsScreenSynAttackQueSize = _JnxJsScreenSynAttackQueSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 35),
    _JnxJsScreenSynAttackQueSize_Type()
)
jnxJsScreenSynAttackQueSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAttackQueSize.setStatus("deprecated")
_JnxJsScreenSynAttackAgeTime_Type = Integer32
_JnxJsScreenSynAttackAgeTime_Object = MibTableColumn
jnxJsScreenSynAttackAgeTime = _JnxJsScreenSynAttackAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 36),
    _JnxJsScreenSynAttackAgeTime_Type()
)
jnxJsScreenSynAttackAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAttackAgeTime.setStatus("deprecated")
_JnxJsScreenIcmpFloodThresh_Type = Integer32
_JnxJsScreenIcmpFloodThresh_Object = MibTableColumn
jnxJsScreenIcmpFloodThresh = _JnxJsScreenIcmpFloodThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 37),
    _JnxJsScreenIcmpFloodThresh_Type()
)
jnxJsScreenIcmpFloodThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenIcmpFloodThresh.setStatus("current")
_JnxJsScreenUdpFloodThresh_Type = Integer32
_JnxJsScreenUdpFloodThresh_Object = MibTableColumn
jnxJsScreenUdpFloodThresh = _JnxJsScreenUdpFloodThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 38),
    _JnxJsScreenUdpFloodThresh_Type()
)
jnxJsScreenUdpFloodThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenUdpFloodThresh.setStatus("current")
_JnxJsScreenPortScanThresh_Type = Integer32
_JnxJsScreenPortScanThresh_Object = MibTableColumn
jnxJsScreenPortScanThresh = _JnxJsScreenPortScanThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 39),
    _JnxJsScreenPortScanThresh_Type()
)
jnxJsScreenPortScanThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenPortScanThresh.setStatus("current")
_JnxJsScreenIpSweepThresh_Type = Integer32
_JnxJsScreenIpSweepThresh_Object = MibTableColumn
jnxJsScreenIpSweepThresh = _JnxJsScreenIpSweepThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 40),
    _JnxJsScreenIpSweepThresh_Type()
)
jnxJsScreenIpSweepThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenIpSweepThresh.setStatus("current")
_JnxJsScreenSynAckAckThres_Type = Integer32
_JnxJsScreenSynAckAckThres_Object = MibTableColumn
jnxJsScreenSynAckAckThres = _JnxJsScreenSynAckAckThres_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 41),
    _JnxJsScreenSynAckAckThres_Type()
)
jnxJsScreenSynAckAckThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynAckAckThres.setStatus("current")
_JnxJsScreenMonIpv6ExtHdr_Type = Counter64
_JnxJsScreenMonIpv6ExtHdr_Object = MibTableColumn
jnxJsScreenMonIpv6ExtHdr = _JnxJsScreenMonIpv6ExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 42),
    _JnxJsScreenMonIpv6ExtHdr_Type()
)
jnxJsScreenMonIpv6ExtHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpv6ExtHdr.setStatus("current")
_JnxJsScreenMonIpv6HopOpt_Type = Counter64
_JnxJsScreenMonIpv6HopOpt_Object = MibTableColumn
jnxJsScreenMonIpv6HopOpt = _JnxJsScreenMonIpv6HopOpt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 43),
    _JnxJsScreenMonIpv6HopOpt_Type()
)
jnxJsScreenMonIpv6HopOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpv6HopOpt.setStatus("current")
_JnxJsScreenMonIpv6DstOpt_Type = Counter64
_JnxJsScreenMonIpv6DstOpt_Object = MibTableColumn
jnxJsScreenMonIpv6DstOpt = _JnxJsScreenMonIpv6DstOpt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 44),
    _JnxJsScreenMonIpv6DstOpt_Type()
)
jnxJsScreenMonIpv6DstOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpv6DstOpt.setStatus("current")
_JnxJsScreenMonIpv6ExtLimit_Type = Counter64
_JnxJsScreenMonIpv6ExtLimit_Object = MibTableColumn
jnxJsScreenMonIpv6ExtLimit = _JnxJsScreenMonIpv6ExtLimit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 45),
    _JnxJsScreenMonIpv6ExtLimit_Type()
)
jnxJsScreenMonIpv6ExtLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpv6ExtLimit.setStatus("current")
_JnxJsScreenMonIpMalIpv6_Type = Counter64
_JnxJsScreenMonIpMalIpv6_Object = MibTableColumn
jnxJsScreenMonIpMalIpv6 = _JnxJsScreenMonIpMalIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 46),
    _JnxJsScreenMonIpMalIpv6_Type()
)
jnxJsScreenMonIpMalIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpMalIpv6.setStatus("current")
_JnxJsScreenMonIcmpMalIcmpv6_Type = Counter64
_JnxJsScreenMonIcmpMalIcmpv6_Object = MibTableColumn
jnxJsScreenMonIcmpMalIcmpv6 = _JnxJsScreenMonIcmpMalIcmpv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 47),
    _JnxJsScreenMonIcmpMalIcmpv6_Type()
)
jnxJsScreenMonIcmpMalIcmpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIcmpMalIcmpv6.setStatus("current")
_JnxJsScreenIpv6ExtNumLim_Type = Integer32
_JnxJsScreenIpv6ExtNumLim_Object = MibTableColumn
jnxJsScreenIpv6ExtNumLim = _JnxJsScreenIpv6ExtNumLim_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 48),
    _JnxJsScreenIpv6ExtNumLim_Type()
)
jnxJsScreenIpv6ExtNumLim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenIpv6ExtNumLim.setStatus("current")
_JnxJsScreenUdpPortScanThresh_Type = Integer32
_JnxJsScreenUdpPortScanThresh_Object = MibTableColumn
jnxJsScreenUdpPortScanThresh = _JnxJsScreenUdpPortScanThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 49),
    _JnxJsScreenUdpPortScanThresh_Type()
)
jnxJsScreenUdpPortScanThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenUdpPortScanThresh.setStatus("current")
_JnxJsScreenMonUdpPortScan_Type = Counter64
_JnxJsScreenMonUdpPortScan_Object = MibTableColumn
jnxJsScreenMonUdpPortScan = _JnxJsScreenMonUdpPortScan_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 50),
    _JnxJsScreenMonUdpPortScan_Type()
)
jnxJsScreenMonUdpPortScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonUdpPortScan.setStatus("current")
_JnxJsScreenMonIpTunnelGre6in4_Type = Counter64
_JnxJsScreenMonIpTunnelGre6in4_Object = MibTableColumn
jnxJsScreenMonIpTunnelGre6in4 = _JnxJsScreenMonIpTunnelGre6in4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 51),
    _JnxJsScreenMonIpTunnelGre6in4_Type()
)
jnxJsScreenMonIpTunnelGre6in4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelGre6in4.setStatus("current")
_JnxJsScreenMonIpTunnelGre4in6_Type = Counter64
_JnxJsScreenMonIpTunnelGre4in6_Object = MibTableColumn
jnxJsScreenMonIpTunnelGre4in6 = _JnxJsScreenMonIpTunnelGre4in6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 52),
    _JnxJsScreenMonIpTunnelGre4in6_Type()
)
jnxJsScreenMonIpTunnelGre4in6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelGre4in6.setStatus("current")
_JnxJsScreenMonIpTunnelGre6in6_Type = Counter64
_JnxJsScreenMonIpTunnelGre6in6_Object = MibTableColumn
jnxJsScreenMonIpTunnelGre6in6 = _JnxJsScreenMonIpTunnelGre6in6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 53),
    _JnxJsScreenMonIpTunnelGre6in6_Type()
)
jnxJsScreenMonIpTunnelGre6in6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelGre6in6.setStatus("current")
_JnxJsScreenMonIpTunnelGre4in4_Type = Counter64
_JnxJsScreenMonIpTunnelGre4in4_Object = MibTableColumn
jnxJsScreenMonIpTunnelGre4in4 = _JnxJsScreenMonIpTunnelGre4in4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 54),
    _JnxJsScreenMonIpTunnelGre4in4_Type()
)
jnxJsScreenMonIpTunnelGre4in4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelGre4in4.setStatus("current")
_JnxJsScreenMonIpTunnelIpInUdpTeredo_Type = Counter64
_JnxJsScreenMonIpTunnelIpInUdpTeredo_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpInUdpTeredo = _JnxJsScreenMonIpTunnelIpInUdpTeredo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 55),
    _JnxJsScreenMonIpTunnelIpInUdpTeredo_Type()
)
jnxJsScreenMonIpTunnelIpInUdpTeredo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpInUdpTeredo.setStatus("current")
_JnxJsScreenMonIpTunnelBadInnerHeader_Type = Counter64
_JnxJsScreenMonIpTunnelBadInnerHeader_Object = MibTableColumn
jnxJsScreenMonIpTunnelBadInnerHeader = _JnxJsScreenMonIpTunnelBadInnerHeader_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 56),
    _JnxJsScreenMonIpTunnelBadInnerHeader_Type()
)
jnxJsScreenMonIpTunnelBadInnerHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelBadInnerHeader.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp6to4relay_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp6to4relay_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp6to4relay = _JnxJsScreenMonIpTunnelIpIp6to4relay_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 57),
    _JnxJsScreenMonIpTunnelIpIp6to4relay_Type()
)
jnxJsScreenMonIpTunnelIpIp6to4relay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp6to4relay.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp6in4_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp6in4_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp6in4 = _JnxJsScreenMonIpTunnelIpIp6in4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 58),
    _JnxJsScreenMonIpTunnelIpIp6in4_Type()
)
jnxJsScreenMonIpTunnelIpIp6in4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp6in4.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp6over4_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp6over4_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp6over4 = _JnxJsScreenMonIpTunnelIpIp6over4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 59),
    _JnxJsScreenMonIpTunnelIpIp6over4_Type()
)
jnxJsScreenMonIpTunnelIpIp6over4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp6over4.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp4in6_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp4in6_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp4in6 = _JnxJsScreenMonIpTunnelIpIp4in6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 60),
    _JnxJsScreenMonIpTunnelIpIp4in6_Type()
)
jnxJsScreenMonIpTunnelIpIp4in6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp4in6.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp4in4_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp4in4_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp4in4 = _JnxJsScreenMonIpTunnelIpIp4in4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 61),
    _JnxJsScreenMonIpTunnelIpIp4in4_Type()
)
jnxJsScreenMonIpTunnelIpIp4in4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp4in4.setStatus("current")
_JnxJsScreenMonIpTunnelIpIp6in6_Type = Counter64
_JnxJsScreenMonIpTunnelIpIp6in6_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIp6in6 = _JnxJsScreenMonIpTunnelIpIp6in6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 62),
    _JnxJsScreenMonIpTunnelIpIp6in6_Type()
)
jnxJsScreenMonIpTunnelIpIp6in6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIp6in6.setStatus("current")
_JnxJsScreenMonIpTunnelIpIpIsatap_Type = Counter64
_JnxJsScreenMonIpTunnelIpIpIsatap_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIpIsatap = _JnxJsScreenMonIpTunnelIpIpIsatap_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 63),
    _JnxJsScreenMonIpTunnelIpIpIsatap_Type()
)
jnxJsScreenMonIpTunnelIpIpIsatap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIpIsatap.setStatus("current")
_JnxJsScreenMonIpTunnelIpIpDsLite_Type = Counter64
_JnxJsScreenMonIpTunnelIpIpDsLite_Object = MibTableColumn
jnxJsScreenMonIpTunnelIpIpDsLite = _JnxJsScreenMonIpTunnelIpIpDsLite_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 1, 1, 64),
    _JnxJsScreenMonIpTunnelIpIpDsLite_Type()
)
jnxJsScreenMonIpTunnelIpIpDsLite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonIpTunnelIpIpDsLite.setStatus("current")
_JnxJsScreenMonThreshTable_Object = MibTable
jnxJsScreenMonThreshTable = _JnxJsScreenMonThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxJsScreenMonThreshTable.setStatus("current")
_JnxJsScreenMonThreshEntry_Object = MibTableRow
jnxJsScreenMonThreshEntry = _JnxJsScreenMonThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    jnxJsScreenMonThreshEntry.setStatus("current")
_JnxJsScreenSynFloodSrcThresh_Type = Integer32
_JnxJsScreenSynFloodSrcThresh_Object = MibTableColumn
jnxJsScreenSynFloodSrcThresh = _JnxJsScreenSynFloodSrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 1),
    _JnxJsScreenSynFloodSrcThresh_Type()
)
jnxJsScreenSynFloodSrcThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynFloodSrcThresh.setStatus("current")
_JnxJsScreenSynFloodDstThresh_Type = Integer32
_JnxJsScreenSynFloodDstThresh_Object = MibTableColumn
jnxJsScreenSynFloodDstThresh = _JnxJsScreenSynFloodDstThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 2),
    _JnxJsScreenSynFloodDstThresh_Type()
)
jnxJsScreenSynFloodDstThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSynFloodDstThresh.setStatus("current")
_JnxJsScreenSessLimitSrcThresh_Type = Integer32
_JnxJsScreenSessLimitSrcThresh_Object = MibTableColumn
jnxJsScreenSessLimitSrcThresh = _JnxJsScreenSessLimitSrcThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 3),
    _JnxJsScreenSessLimitSrcThresh_Type()
)
jnxJsScreenSessLimitSrcThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSessLimitSrcThresh.setStatus("current")
_JnxJsScreenSessLimitDstThresh_Type = Integer32
_JnxJsScreenSessLimitDstThresh_Object = MibTableColumn
jnxJsScreenSessLimitDstThresh = _JnxJsScreenSessLimitDstThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 4),
    _JnxJsScreenSessLimitDstThresh_Type()
)
jnxJsScreenSessLimitDstThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenSessLimitDstThresh.setStatus("current")
_JnxJsScreenMonSynFloodSrc_Type = Counter64
_JnxJsScreenMonSynFloodSrc_Object = MibTableColumn
jnxJsScreenMonSynFloodSrc = _JnxJsScreenMonSynFloodSrc_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 5),
    _JnxJsScreenMonSynFloodSrc_Type()
)
jnxJsScreenMonSynFloodSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSynFloodSrc.setStatus("current")
_JnxJsScreenMonSynFloodDst_Type = Counter64
_JnxJsScreenMonSynFloodDst_Object = MibTableColumn
jnxJsScreenMonSynFloodDst = _JnxJsScreenMonSynFloodDst_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 2, 1, 6),
    _JnxJsScreenMonSynFloodDst_Type()
)
jnxJsScreenMonSynFloodDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonSynFloodDst.setStatus("current")
_JnxJsScreenSweepTable_Object = MibTable
jnxJsScreenSweepTable = _JnxJsScreenSweepTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3)
)
if mibBuilder.loadTexts:
    jnxJsScreenSweepTable.setStatus("current")
_JnxJsScreenSweepEntry_Object = MibTableRow
jnxJsScreenSweepEntry = _JnxJsScreenSweepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxJsScreenSweepEntry.setStatus("current")
_JnxJsScreenTcpSweepThresh_Type = Integer32
_JnxJsScreenTcpSweepThresh_Object = MibTableColumn
jnxJsScreenTcpSweepThresh = _JnxJsScreenTcpSweepThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3, 1, 1),
    _JnxJsScreenTcpSweepThresh_Type()
)
jnxJsScreenTcpSweepThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenTcpSweepThresh.setStatus("current")
_JnxJsScreenUdpSweepThresh_Type = Integer32
_JnxJsScreenUdpSweepThresh_Object = MibTableColumn
jnxJsScreenUdpSweepThresh = _JnxJsScreenUdpSweepThresh_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3, 1, 2),
    _JnxJsScreenUdpSweepThresh_Type()
)
jnxJsScreenUdpSweepThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenUdpSweepThresh.setStatus("current")
_JnxJsScreenMonTcpSweep_Type = Counter64
_JnxJsScreenMonTcpSweep_Object = MibTableColumn
jnxJsScreenMonTcpSweep = _JnxJsScreenMonTcpSweep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3, 1, 3),
    _JnxJsScreenMonTcpSweep_Type()
)
jnxJsScreenMonTcpSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonTcpSweep.setStatus("current")
_JnxJsScreenMonUdpSweep_Type = Counter64
_JnxJsScreenMonUdpSweep_Object = MibTableColumn
jnxJsScreenMonUdpSweep = _JnxJsScreenMonUdpSweep_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 1, 3, 1, 4),
    _JnxJsScreenMonUdpSweep_Type()
)
jnxJsScreenMonUdpSweep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsScreenMonUdpSweep.setStatus("current")
_JnxJsScreenTrapVars_ObjectIdentity = ObjectIdentity
jnxJsScreenTrapVars = _JnxJsScreenTrapVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 2)
)


class _JnxJsScreenAttackType_Type(Integer32):
    """Custom type jnxJsScreenAttackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54)
        )
    )
    namedValues = NamedValues(
        *(("icmpFlood", 1),
          ("icmpFragmentation", 27),
          ("icmpLarge", 28),
          ("icmpv6malpkt", 39),
          ("ipAddressSpoof", 13),
          ("ipFragmentation", 31),
          ("ipOptionBad", 20),
          ("ipOptionLSR", 24),
          ("ipOptionRecRt", 21),
          ("ipOptionSRR", 25),
          ("ipOptionSecurity", 23),
          ("ipOptionStream", 26),
          ("ipOptionTimeStamp", 22),
          ("ipSweeping", 4),
          ("ipTunnelBadInnerHeader", 46),
          ("ipTunnelGre4in4", 44),
          ("ipTunnelGre4in6", 42),
          ("ipTunnelGre6in4", 41),
          ("ipTunnelGre6in6", 43),
          ("ipTunnelIpInUdpTeredo", 45),
          ("ipTunnelIpIp4in4", 51),
          ("ipTunnelIpIp4in6", 50),
          ("ipTunnelIpIp6in4", 48),
          ("ipTunnelIpIp6in6", 52),
          ("ipTunnelIpIp6over4", 49),
          ("ipTunnelIpIp6to4relay", 47),
          ("ipTunnelIpIpDsLite", 54),
          ("ipTunnelIpIpIsatap", 53),
          ("ipUnknownProtocol", 19),
          ("ipv6dstopt", 36),
          ("ipv6exthdr", 34),
          ("ipv6extlim", 37),
          ("ipv6hbyhopt", 35),
          ("ipv6malhdr", 38),
          ("landAttack", 16),
          ("pingDeath", 14),
          ("portScanning", 3),
          ("sessLimitDestBased", 8),
          ("sessLimitSrcBased", 7),
          ("sourceRoute", 15),
          ("synAckAck", 9),
          ("synAttack", 10),
          ("synFragmentation", 17),
          ("synfloodDstIP", 6),
          ("synfloodSrcIP", 5),
          ("tcpFinNoAck", 30),
          ("tcpNoFlag", 18),
          ("tcpSweeping", 32),
          ("tcpSynFin", 29),
          ("tearDrop", 12),
          ("udpFlood", 2),
          ("udpSweeping", 33),
          ("udpportScanning", 40),
          ("winNuke", 11))
    )


_JnxJsScreenAttackType_Type.__name__ = "Integer32"
_JnxJsScreenAttackType_Object = MibScalar
jnxJsScreenAttackType = _JnxJsScreenAttackType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 2, 1),
    _JnxJsScreenAttackType_Type()
)
jnxJsScreenAttackType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsScreenAttackType.setStatus("current")
_JnxJsScreenAttackCounter_Type = Integer32
_JnxJsScreenAttackCounter_Object = MibScalar
jnxJsScreenAttackCounter = _JnxJsScreenAttackCounter_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 2, 2),
    _JnxJsScreenAttackCounter_Type()
)
jnxJsScreenAttackCounter.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsScreenAttackCounter.setStatus("current")


class _JnxJsScreenAttackDescr_Type(DisplayString):
    """Custom type jnxJsScreenAttackDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsScreenAttackDescr_Type.__name__ = "DisplayString"
_JnxJsScreenAttackDescr_Object = MibScalar
jnxJsScreenAttackDescr = _JnxJsScreenAttackDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 2, 3),
    _JnxJsScreenAttackDescr_Type()
)
jnxJsScreenAttackDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsScreenAttackDescr.setStatus("current")


class _JnxJsScreenCfgStatus_Type(Integer32):
    """Custom type jnxJsScreenCfgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_JnxJsScreenCfgStatus_Type.__name__ = "Integer32"
_JnxJsScreenCfgStatus_Object = MibScalar
jnxJsScreenCfgStatus = _JnxJsScreenCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 2, 4),
    _JnxJsScreenCfgStatus_Type()
)
jnxJsScreenCfgStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    jnxJsScreenCfgStatus.setStatus("current")
jnxJsScreenMonEntry.registerAugmentions(
    ("JUNIPER-JS-SCREENING-MIB",
     "jnxJsScreenMonThreshEntry")
)
jnxJsScreenMonThreshEntry.setIndexNames(*jnxJsScreenMonEntry.getIndexNames())
jnxJsScreenMonEntry.registerAugmentions(
    ("JUNIPER-JS-SCREENING-MIB",
     "jnxJsScreenSweepEntry")
)
jnxJsScreenSweepEntry.setIndexNames(*jnxJsScreenMonEntry.getIndexNames())

# Managed Objects groups


# Notification objects

jnxJsScreenAttack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 0, 1)
)
jnxJsScreenAttack.setObjects(
      *(("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenZoneName"),
        ("IF-MIB", "ifName"),
        ("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenAttackType"),
        ("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenAttackCounter"),
        ("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenAttackDescr"))
)
if mibBuilder.loadTexts:
    jnxJsScreenAttack.setStatus(
        "current"
    )

jnxJsScreenCfgChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 8, 1, 0, 2)
)
jnxJsScreenCfgChange.setObjects(
      *(("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenZoneName"),
        ("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenAttackType"),
        ("JUNIPER-JS-SCREENING-MIB", "jnxJsScreenCfgStatus"))
)
if mibBuilder.loadTexts:
    jnxJsScreenCfgChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-JS-SCREENING-MIB",
    **{"jnxJsScreenMIB": jnxJsScreenMIB,
       "jnxJsScreenNotifications": jnxJsScreenNotifications,
       "jnxJsScreenAttack": jnxJsScreenAttack,
       "jnxJsScreenCfgChange": jnxJsScreenCfgChange,
       "jnxJsScreenObjects": jnxJsScreenObjects,
       "jnxJsScreenMonTable": jnxJsScreenMonTable,
       "jnxJsScreenMonEntry": jnxJsScreenMonEntry,
       "jnxJsScreenZoneName": jnxJsScreenZoneName,
       "jnxJsScreenNumOfIf": jnxJsScreenNumOfIf,
       "jnxJsScreenMonSynAttk": jnxJsScreenMonSynAttk,
       "jnxJsScreenMonTearDrop": jnxJsScreenMonTearDrop,
       "jnxJsScreenMonSrcRoute": jnxJsScreenMonSrcRoute,
       "jnxJsScreenMonPingDeath": jnxJsScreenMonPingDeath,
       "jnxJsScreenMonAddrSpoof": jnxJsScreenMonAddrSpoof,
       "jnxJsScreenMonLand": jnxJsScreenMonLand,
       "jnxJsScreenMonIcmpFlood": jnxJsScreenMonIcmpFlood,
       "jnxJsScreenMonUdpFlood": jnxJsScreenMonUdpFlood,
       "jnxJsScreenMonWinnuke": jnxJsScreenMonWinnuke,
       "jnxJsScreenMonPortScan": jnxJsScreenMonPortScan,
       "jnxJsScreenMonIpSweep": jnxJsScreenMonIpSweep,
       "jnxJsScreenMonSynFrag": jnxJsScreenMonSynFrag,
       "jnxJsScreenMonTcpNoFlag": jnxJsScreenMonTcpNoFlag,
       "jnxJsScreenMonIpUnknownProt": jnxJsScreenMonIpUnknownProt,
       "jnxJsScreenMonIpOptBad": jnxJsScreenMonIpOptBad,
       "jnxJsScreenMonIpOptRecRt": jnxJsScreenMonIpOptRecRt,
       "jnxJsScreenMonIpOptTimestamp": jnxJsScreenMonIpOptTimestamp,
       "jnxJsScreenMonIpOptSecurity": jnxJsScreenMonIpOptSecurity,
       "jnxJsScreenMonIpOptLSR": jnxJsScreenMonIpOptLSR,
       "jnxJsScreenMonIpOptSSR": jnxJsScreenMonIpOptSSR,
       "jnxJsScreenMonIpOptStream": jnxJsScreenMonIpOptStream,
       "jnxJsScreenMonIcmpFrag": jnxJsScreenMonIcmpFrag,
       "jnxJsScreenMonIcmpLarge": jnxJsScreenMonIcmpLarge,
       "jnxJsScreenMonTcpSynFin": jnxJsScreenMonTcpSynFin,
       "jnxJsScreenMonTcpFinNoAck": jnxJsScreenMonTcpFinNoAck,
       "jnxJsScreenMonLimitSessSrc": jnxJsScreenMonLimitSessSrc,
       "jnxJsScreenMonLimitSessDest": jnxJsScreenMonLimitSessDest,
       "jnxJsScreenMonSynAckAck": jnxJsScreenMonSynAckAck,
       "jnxJsScreenMonIpFrag": jnxJsScreenMonIpFrag,
       "jnxJsScreenSynAttackThresh": jnxJsScreenSynAttackThresh,
       "jnxJsScreenSynAttackTimeout": jnxJsScreenSynAttackTimeout,
       "jnxJsScreenSynAttackAlmTh": jnxJsScreenSynAttackAlmTh,
       "jnxJsScreenSynAttackQueSize": jnxJsScreenSynAttackQueSize,
       "jnxJsScreenSynAttackAgeTime": jnxJsScreenSynAttackAgeTime,
       "jnxJsScreenIcmpFloodThresh": jnxJsScreenIcmpFloodThresh,
       "jnxJsScreenUdpFloodThresh": jnxJsScreenUdpFloodThresh,
       "jnxJsScreenPortScanThresh": jnxJsScreenPortScanThresh,
       "jnxJsScreenIpSweepThresh": jnxJsScreenIpSweepThresh,
       "jnxJsScreenSynAckAckThres": jnxJsScreenSynAckAckThres,
       "jnxJsScreenMonIpv6ExtHdr": jnxJsScreenMonIpv6ExtHdr,
       "jnxJsScreenMonIpv6HopOpt": jnxJsScreenMonIpv6HopOpt,
       "jnxJsScreenMonIpv6DstOpt": jnxJsScreenMonIpv6DstOpt,
       "jnxJsScreenMonIpv6ExtLimit": jnxJsScreenMonIpv6ExtLimit,
       "jnxJsScreenMonIpMalIpv6": jnxJsScreenMonIpMalIpv6,
       "jnxJsScreenMonIcmpMalIcmpv6": jnxJsScreenMonIcmpMalIcmpv6,
       "jnxJsScreenIpv6ExtNumLim": jnxJsScreenIpv6ExtNumLim,
       "jnxJsScreenUdpPortScanThresh": jnxJsScreenUdpPortScanThresh,
       "jnxJsScreenMonUdpPortScan": jnxJsScreenMonUdpPortScan,
       "jnxJsScreenMonIpTunnelGre6in4": jnxJsScreenMonIpTunnelGre6in4,
       "jnxJsScreenMonIpTunnelGre4in6": jnxJsScreenMonIpTunnelGre4in6,
       "jnxJsScreenMonIpTunnelGre6in6": jnxJsScreenMonIpTunnelGre6in6,
       "jnxJsScreenMonIpTunnelGre4in4": jnxJsScreenMonIpTunnelGre4in4,
       "jnxJsScreenMonIpTunnelIpInUdpTeredo": jnxJsScreenMonIpTunnelIpInUdpTeredo,
       "jnxJsScreenMonIpTunnelBadInnerHeader": jnxJsScreenMonIpTunnelBadInnerHeader,
       "jnxJsScreenMonIpTunnelIpIp6to4relay": jnxJsScreenMonIpTunnelIpIp6to4relay,
       "jnxJsScreenMonIpTunnelIpIp6in4": jnxJsScreenMonIpTunnelIpIp6in4,
       "jnxJsScreenMonIpTunnelIpIp6over4": jnxJsScreenMonIpTunnelIpIp6over4,
       "jnxJsScreenMonIpTunnelIpIp4in6": jnxJsScreenMonIpTunnelIpIp4in6,
       "jnxJsScreenMonIpTunnelIpIp4in4": jnxJsScreenMonIpTunnelIpIp4in4,
       "jnxJsScreenMonIpTunnelIpIp6in6": jnxJsScreenMonIpTunnelIpIp6in6,
       "jnxJsScreenMonIpTunnelIpIpIsatap": jnxJsScreenMonIpTunnelIpIpIsatap,
       "jnxJsScreenMonIpTunnelIpIpDsLite": jnxJsScreenMonIpTunnelIpIpDsLite,
       "jnxJsScreenMonThreshTable": jnxJsScreenMonThreshTable,
       "jnxJsScreenMonThreshEntry": jnxJsScreenMonThreshEntry,
       "jnxJsScreenSynFloodSrcThresh": jnxJsScreenSynFloodSrcThresh,
       "jnxJsScreenSynFloodDstThresh": jnxJsScreenSynFloodDstThresh,
       "jnxJsScreenSessLimitSrcThresh": jnxJsScreenSessLimitSrcThresh,
       "jnxJsScreenSessLimitDstThresh": jnxJsScreenSessLimitDstThresh,
       "jnxJsScreenMonSynFloodSrc": jnxJsScreenMonSynFloodSrc,
       "jnxJsScreenMonSynFloodDst": jnxJsScreenMonSynFloodDst,
       "jnxJsScreenSweepTable": jnxJsScreenSweepTable,
       "jnxJsScreenSweepEntry": jnxJsScreenSweepEntry,
       "jnxJsScreenTcpSweepThresh": jnxJsScreenTcpSweepThresh,
       "jnxJsScreenUdpSweepThresh": jnxJsScreenUdpSweepThresh,
       "jnxJsScreenMonTcpSweep": jnxJsScreenMonTcpSweep,
       "jnxJsScreenMonUdpSweep": jnxJsScreenMonUdpSweep,
       "jnxJsScreenTrapVars": jnxJsScreenTrapVars,
       "jnxJsScreenAttackType": jnxJsScreenAttackType,
       "jnxJsScreenAttackCounter": jnxJsScreenAttackCounter,
       "jnxJsScreenAttackDescr": jnxJsScreenAttackDescr,
       "jnxJsScreenCfgStatus": jnxJsScreenCfgStatus}
)
