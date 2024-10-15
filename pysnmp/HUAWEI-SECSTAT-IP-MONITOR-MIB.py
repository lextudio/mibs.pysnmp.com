# SNMP MIB module (HUAWEI-SECSTAT-IP-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SECSTAT-IP-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:50 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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

hwSecStatIPMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwSECSTAT_ObjectIdentity = ObjectIdentity
hwSECSTAT = _HwSECSTAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11)
)
_HwSecStatMonitorObjects_ObjectIdentity = ObjectIdentity
hwSecStatMonitorObjects = _HwSecStatMonitorObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1)
)


class _HwSecStatClearAllIPInfo_Type(Integer32):
    """Custom type hwSecStatClearAllIPInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearAllIPInfo_Type.__name__ = "Integer32"
_HwSecStatClearAllIPInfo_Object = MibScalar
hwSecStatClearAllIPInfo = _HwSecStatClearAllIPInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 1),
    _HwSecStatClearAllIPInfo_Type()
)
hwSecStatClearAllIPInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearAllIPInfo.setStatus("current")
_HwSecStatIPInInfoTable_Object = MibTable
hwSecStatIPInInfoTable = _HwSecStatIPInInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2)
)
if mibBuilder.loadTexts:
    hwSecStatIPInInfoTable.setStatus("current")
_HwSecStatIPInInfoEntry_Object = MibTableRow
hwSecStatIPInInfoEntry = _HwSecStatIPInInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1)
)
hwSecStatIPInInfoEntry.setIndexNames(
    (0, "HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPInInfoIpAddress"),
)
if mibBuilder.loadTexts:
    hwSecStatIPInInfoEntry.setStatus("current")
_HwSecStatIPInInfoIpAddress_Type = IpAddress
_HwSecStatIPInInfoIpAddress_Object = MibTableColumn
hwSecStatIPInInfoIpAddress = _HwSecStatIPInInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 1),
    _HwSecStatIPInInfoIpAddress_Type()
)
hwSecStatIPInInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPInInfoIpAddress.setStatus("current")
_HwSecStatIPTcpSessTo_Type = Counter64
_HwSecStatIPTcpSessTo_Object = MibTableColumn
hwSecStatIPTcpSessTo = _HwSecStatIPTcpSessTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 2),
    _HwSecStatIPTcpSessTo_Type()
)
hwSecStatIPTcpSessTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPTcpSessTo.setStatus("current")
_HwSecStatIPUdpSessTo_Type = Counter64
_HwSecStatIPUdpSessTo_Object = MibTableColumn
hwSecStatIPUdpSessTo = _HwSecStatIPUdpSessTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 3),
    _HwSecStatIPUdpSessTo_Type()
)
hwSecStatIPUdpSessTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPUdpSessTo.setStatus("current")
_HwSecStatIPIcmpSessTo_Type = Counter64
_HwSecStatIPIcmpSessTo_Object = MibTableColumn
hwSecStatIPIcmpSessTo = _HwSecStatIPIcmpSessTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 4),
    _HwSecStatIPIcmpSessTo_Type()
)
hwSecStatIPIcmpSessTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPIcmpSessTo.setStatus("current")
_HwSecStatIPConnTo_Type = Counter64
_HwSecStatIPConnTo_Object = MibTableColumn
hwSecStatIPConnTo = _HwSecStatIPConnTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 5),
    _HwSecStatIPConnTo_Type()
)
hwSecStatIPConnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPConnTo.setStatus("current")
_HwSecStatIPHalfConnTo_Type = Counter64
_HwSecStatIPHalfConnTo_Object = MibTableColumn
hwSecStatIPHalfConnTo = _HwSecStatIPHalfConnTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 6),
    _HwSecStatIPHalfConnTo_Type()
)
hwSecStatIPHalfConnTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHalfConnTo.setStatus("current")
_HwSecStatIPTcpSessSpeedTo_Type = Counter64
_HwSecStatIPTcpSessSpeedTo_Object = MibTableColumn
hwSecStatIPTcpSessSpeedTo = _HwSecStatIPTcpSessSpeedTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 7),
    _HwSecStatIPTcpSessSpeedTo_Type()
)
hwSecStatIPTcpSessSpeedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPTcpSessSpeedTo.setStatus("current")
_HwSecStatIPUdpSessSpeedTo_Type = Counter64
_HwSecStatIPUdpSessSpeedTo_Object = MibTableColumn
hwSecStatIPUdpSessSpeedTo = _HwSecStatIPUdpSessSpeedTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 8),
    _HwSecStatIPUdpSessSpeedTo_Type()
)
hwSecStatIPUdpSessSpeedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPUdpSessSpeedTo.setStatus("current")
_HwSecStatIPIcmpSessSpeedTo_Type = Counter64
_HwSecStatIPIcmpSessSpeedTo_Object = MibTableColumn
hwSecStatIPIcmpSessSpeedTo = _HwSecStatIPIcmpSessSpeedTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 9),
    _HwSecStatIPIcmpSessSpeedTo_Type()
)
hwSecStatIPIcmpSessSpeedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPIcmpSessSpeedTo.setStatus("current")
_HwSecStatIPConnSpeedTo_Type = Counter64
_HwSecStatIPConnSpeedTo_Object = MibTableColumn
hwSecStatIPConnSpeedTo = _HwSecStatIPConnSpeedTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 10),
    _HwSecStatIPConnSpeedTo_Type()
)
hwSecStatIPConnSpeedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPConnSpeedTo.setStatus("current")
_HwSecStatIPHalfConnSpeedTo_Type = Counter64
_HwSecStatIPHalfConnSpeedTo_Object = MibTableColumn
hwSecStatIPHalfConnSpeedTo = _HwSecStatIPHalfConnSpeedTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 11),
    _HwSecStatIPHalfConnSpeedTo_Type()
)
hwSecStatIPHalfConnSpeedTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHalfConnSpeedTo.setStatus("current")
_HwSecStatIPAclDenyIcmpPktsTo_Type = Counter64
_HwSecStatIPAclDenyIcmpPktsTo_Object = MibTableColumn
hwSecStatIPAclDenyIcmpPktsTo = _HwSecStatIPAclDenyIcmpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 12),
    _HwSecStatIPAclDenyIcmpPktsTo_Type()
)
hwSecStatIPAclDenyIcmpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyIcmpPktsTo.setStatus("current")
_HwSecStatIPAclDenyIcmpOctsTo_Type = Counter64
_HwSecStatIPAclDenyIcmpOctsTo_Object = MibTableColumn
hwSecStatIPAclDenyIcmpOctsTo = _HwSecStatIPAclDenyIcmpOctsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 13),
    _HwSecStatIPAclDenyIcmpOctsTo_Type()
)
hwSecStatIPAclDenyIcmpOctsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyIcmpOctsTo.setStatus("current")
_HwSecStatIPAclDenyNonIcmpPktsTo_Type = Counter64
_HwSecStatIPAclDenyNonIcmpPktsTo_Object = MibTableColumn
hwSecStatIPAclDenyNonIcmpPktsTo = _HwSecStatIPAclDenyNonIcmpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 14),
    _HwSecStatIPAclDenyNonIcmpPktsTo_Type()
)
hwSecStatIPAclDenyNonIcmpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyNonIcmpPktsTo.setStatus("current")
_HwSecStatIPAclDenyNonIcmpOctsTo_Type = Counter64
_HwSecStatIPAclDenyNonIcmpOctsTo_Object = MibTableColumn
hwSecStatIPAclDenyNonIcmpOctsTo = _HwSecStatIPAclDenyNonIcmpOctsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 15),
    _HwSecStatIPAclDenyNonIcmpOctsTo_Type()
)
hwSecStatIPAclDenyNonIcmpOctsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyNonIcmpOctsTo.setStatus("current")
_HwSecStatIPBlsDenyPktsTo_Type = Counter64
_HwSecStatIPBlsDenyPktsTo_Object = MibTableColumn
hwSecStatIPBlsDenyPktsTo = _HwSecStatIPBlsDenyPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 16),
    _HwSecStatIPBlsDenyPktsTo_Type()
)
hwSecStatIPBlsDenyPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPBlsDenyPktsTo.setStatus("current")
_HwSecStatIPAclDftDenyPktsTo_Type = Counter64
_HwSecStatIPAclDftDenyPktsTo_Object = MibTableColumn
hwSecStatIPAclDftDenyPktsTo = _HwSecStatIPAclDftDenyPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 17),
    _HwSecStatIPAclDftDenyPktsTo_Type()
)
hwSecStatIPAclDftDenyPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDftDenyPktsTo.setStatus("current")
_HwSecStatIPAclDftDenyIcmpPktsTo_Type = Counter64
_HwSecStatIPAclDftDenyIcmpPktsTo_Object = MibTableColumn
hwSecStatIPAclDftDenyIcmpPktsTo = _HwSecStatIPAclDftDenyIcmpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 18),
    _HwSecStatIPAclDftDenyIcmpPktsTo_Type()
)
hwSecStatIPAclDftDenyIcmpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDftDenyIcmpPktsTo.setStatus("current")
_HwSecStatIPIcmpFloodDropPktsTo_Type = Counter64
_HwSecStatIPIcmpFloodDropPktsTo_Object = MibTableColumn
hwSecStatIPIcmpFloodDropPktsTo = _HwSecStatIPIcmpFloodDropPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 19),
    _HwSecStatIPIcmpFloodDropPktsTo_Type()
)
hwSecStatIPIcmpFloodDropPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPIcmpFloodDropPktsTo.setStatus("current")
_HwSecStatIPUdpFloodDropPktsTo_Type = Counter64
_HwSecStatIPUdpFloodDropPktsTo_Object = MibTableColumn
hwSecStatIPUdpFloodDropPktsTo = _HwSecStatIPUdpFloodDropPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 20),
    _HwSecStatIPUdpFloodDropPktsTo_Type()
)
hwSecStatIPUdpFloodDropPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPUdpFloodDropPktsTo.setStatus("current")
_HwSecStatIPFtpPktsTo_Type = Counter64
_HwSecStatIPFtpPktsTo_Object = MibTableColumn
hwSecStatIPFtpPktsTo = _HwSecStatIPFtpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 21),
    _HwSecStatIPFtpPktsTo_Type()
)
hwSecStatIPFtpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPFtpPktsTo.setStatus("current")
_HwSecStatIPSmtpPktsTo_Type = Counter64
_HwSecStatIPSmtpPktsTo_Object = MibTableColumn
hwSecStatIPSmtpPktsTo = _HwSecStatIPSmtpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 22),
    _HwSecStatIPSmtpPktsTo_Type()
)
hwSecStatIPSmtpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPSmtpPktsTo.setStatus("current")
_HwSecStatIPHttpPktsTo_Type = Counter64
_HwSecStatIPHttpPktsTo_Object = MibTableColumn
hwSecStatIPHttpPktsTo = _HwSecStatIPHttpPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 23),
    _HwSecStatIPHttpPktsTo_Type()
)
hwSecStatIPHttpPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHttpPktsTo.setStatus("current")
_HwSecStatIPH323PktsTo_Type = Counter64
_HwSecStatIPH323PktsTo_Object = MibTableColumn
hwSecStatIPH323PktsTo = _HwSecStatIPH323PktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 24),
    _HwSecStatIPH323PktsTo_Type()
)
hwSecStatIPH323PktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPH323PktsTo.setStatus("current")
_HwSecStatIPRtspPktsTo_Type = Counter64
_HwSecStatIPRtspPktsTo_Object = MibTableColumn
hwSecStatIPRtspPktsTo = _HwSecStatIPRtspPktsTo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 25),
    _HwSecStatIPRtspPktsTo_Type()
)
hwSecStatIPRtspPktsTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPRtspPktsTo.setStatus("current")


class _HwSecStatClearIPInInfo_Type(Integer32):
    """Custom type hwSecStatClearIPInInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearIPInInfo_Type.__name__ = "Integer32"
_HwSecStatClearIPInInfo_Object = MibTableColumn
hwSecStatClearIPInInfo = _HwSecStatClearIPInInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 2, 1, 26),
    _HwSecStatClearIPInInfo_Type()
)
hwSecStatClearIPInInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearIPInInfo.setStatus("current")
_HwSecStatIPOutInfoTable_Object = MibTable
hwSecStatIPOutInfoTable = _HwSecStatIPOutInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3)
)
if mibBuilder.loadTexts:
    hwSecStatIPOutInfoTable.setStatus("current")
_HwSecStatIPOutInfoEntry_Object = MibTableRow
hwSecStatIPOutInfoEntry = _HwSecStatIPOutInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1)
)
hwSecStatIPOutInfoEntry.setIndexNames(
    (0, "HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPOutInfoIpAddress"),
)
if mibBuilder.loadTexts:
    hwSecStatIPOutInfoEntry.setStatus("current")
_HwSecStatIPOutInfoIpAddress_Type = IpAddress
_HwSecStatIPOutInfoIpAddress_Object = MibTableColumn
hwSecStatIPOutInfoIpAddress = _HwSecStatIPOutInfoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 1),
    _HwSecStatIPOutInfoIpAddress_Type()
)
hwSecStatIPOutInfoIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPOutInfoIpAddress.setStatus("current")
_HwSecStatIPTcpSessFrom_Type = Counter64
_HwSecStatIPTcpSessFrom_Object = MibTableColumn
hwSecStatIPTcpSessFrom = _HwSecStatIPTcpSessFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 2),
    _HwSecStatIPTcpSessFrom_Type()
)
hwSecStatIPTcpSessFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPTcpSessFrom.setStatus("current")
_HwSecStatIPUdpSessFrom_Type = Counter64
_HwSecStatIPUdpSessFrom_Object = MibTableColumn
hwSecStatIPUdpSessFrom = _HwSecStatIPUdpSessFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 3),
    _HwSecStatIPUdpSessFrom_Type()
)
hwSecStatIPUdpSessFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPUdpSessFrom.setStatus("current")
_HwSecStatIPIcmpSessFrom_Type = Counter64
_HwSecStatIPIcmpSessFrom_Object = MibTableColumn
hwSecStatIPIcmpSessFrom = _HwSecStatIPIcmpSessFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 4),
    _HwSecStatIPIcmpSessFrom_Type()
)
hwSecStatIPIcmpSessFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPIcmpSessFrom.setStatus("current")
_HwSecStatIPConnFrom_Type = Counter64
_HwSecStatIPConnFrom_Object = MibTableColumn
hwSecStatIPConnFrom = _HwSecStatIPConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 5),
    _HwSecStatIPConnFrom_Type()
)
hwSecStatIPConnFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPConnFrom.setStatus("current")
_HwSecStatIPHalfConnFrom_Type = Counter64
_HwSecStatIPHalfConnFrom_Object = MibTableColumn
hwSecStatIPHalfConnFrom = _HwSecStatIPHalfConnFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 6),
    _HwSecStatIPHalfConnFrom_Type()
)
hwSecStatIPHalfConnFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHalfConnFrom.setStatus("current")
_HwSecStatIPTcpSessSpeedFrom_Type = Counter64
_HwSecStatIPTcpSessSpeedFrom_Object = MibTableColumn
hwSecStatIPTcpSessSpeedFrom = _HwSecStatIPTcpSessSpeedFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 7),
    _HwSecStatIPTcpSessSpeedFrom_Type()
)
hwSecStatIPTcpSessSpeedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPTcpSessSpeedFrom.setStatus("current")
_HwSecStatIPUdpSessSpeedFrom_Type = Counter64
_HwSecStatIPUdpSessSpeedFrom_Object = MibTableColumn
hwSecStatIPUdpSessSpeedFrom = _HwSecStatIPUdpSessSpeedFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 8),
    _HwSecStatIPUdpSessSpeedFrom_Type()
)
hwSecStatIPUdpSessSpeedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPUdpSessSpeedFrom.setStatus("current")
_HwSecStatIPIcmpSessSpeedFrom_Type = Counter64
_HwSecStatIPIcmpSessSpeedFrom_Object = MibTableColumn
hwSecStatIPIcmpSessSpeedFrom = _HwSecStatIPIcmpSessSpeedFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 9),
    _HwSecStatIPIcmpSessSpeedFrom_Type()
)
hwSecStatIPIcmpSessSpeedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPIcmpSessSpeedFrom.setStatus("current")
_HwSecStatIPConnSpeedFrom_Type = Counter64
_HwSecStatIPConnSpeedFrom_Object = MibTableColumn
hwSecStatIPConnSpeedFrom = _HwSecStatIPConnSpeedFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 10),
    _HwSecStatIPConnSpeedFrom_Type()
)
hwSecStatIPConnSpeedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPConnSpeedFrom.setStatus("current")
_HwSecStatIPHalfConnSpeedFrom_Type = Counter64
_HwSecStatIPHalfConnSpeedFrom_Object = MibTableColumn
hwSecStatIPHalfConnSpeedFrom = _HwSecStatIPHalfConnSpeedFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 11),
    _HwSecStatIPHalfConnSpeedFrom_Type()
)
hwSecStatIPHalfConnSpeedFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHalfConnSpeedFrom.setStatus("current")
_HwSecStatIPAclDenyIcmpPktsFrom_Type = Counter64
_HwSecStatIPAclDenyIcmpPktsFrom_Object = MibTableColumn
hwSecStatIPAclDenyIcmpPktsFrom = _HwSecStatIPAclDenyIcmpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 12),
    _HwSecStatIPAclDenyIcmpPktsFrom_Type()
)
hwSecStatIPAclDenyIcmpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyIcmpPktsFrom.setStatus("current")
_HwSecStatIPAclDenyIcmpOctsFrom_Type = Counter64
_HwSecStatIPAclDenyIcmpOctsFrom_Object = MibTableColumn
hwSecStatIPAclDenyIcmpOctsFrom = _HwSecStatIPAclDenyIcmpOctsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 13),
    _HwSecStatIPAclDenyIcmpOctsFrom_Type()
)
hwSecStatIPAclDenyIcmpOctsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyIcmpOctsFrom.setStatus("current")
_HwSecStatIPAclDenyNonIcmpPktsFrom_Type = Counter64
_HwSecStatIPAclDenyNonIcmpPktsFrom_Object = MibTableColumn
hwSecStatIPAclDenyNonIcmpPktsFrom = _HwSecStatIPAclDenyNonIcmpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 14),
    _HwSecStatIPAclDenyNonIcmpPktsFrom_Type()
)
hwSecStatIPAclDenyNonIcmpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyNonIcmpPktsFrom.setStatus("current")
_HwSecStatIPAclDenyNonIcmpOctsFrom_Type = Counter64
_HwSecStatIPAclDenyNonIcmpOctsFrom_Object = MibTableColumn
hwSecStatIPAclDenyNonIcmpOctsFrom = _HwSecStatIPAclDenyNonIcmpOctsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 15),
    _HwSecStatIPAclDenyNonIcmpOctsFrom_Type()
)
hwSecStatIPAclDenyNonIcmpOctsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDenyNonIcmpOctsFrom.setStatus("current")
_HwSecStatIPBlsDenyPktsFrom_Type = Counter64
_HwSecStatIPBlsDenyPktsFrom_Object = MibTableColumn
hwSecStatIPBlsDenyPktsFrom = _HwSecStatIPBlsDenyPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 16),
    _HwSecStatIPBlsDenyPktsFrom_Type()
)
hwSecStatIPBlsDenyPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPBlsDenyPktsFrom.setStatus("current")
_HwSecStatIPAclDftDenyPktsFrom_Type = Counter64
_HwSecStatIPAclDftDenyPktsFrom_Object = MibTableColumn
hwSecStatIPAclDftDenyPktsFrom = _HwSecStatIPAclDftDenyPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 17),
    _HwSecStatIPAclDftDenyPktsFrom_Type()
)
hwSecStatIPAclDftDenyPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDftDenyPktsFrom.setStatus("current")
_HwSecStatIPAclDftDenyIcmpPktsFrom_Type = Counter64
_HwSecStatIPAclDftDenyIcmpPktsFrom_Object = MibTableColumn
hwSecStatIPAclDftDenyIcmpPktsFrom = _HwSecStatIPAclDftDenyIcmpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 18),
    _HwSecStatIPAclDftDenyIcmpPktsFrom_Type()
)
hwSecStatIPAclDftDenyIcmpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPAclDftDenyIcmpPktsFrom.setStatus("current")
_HwSecStatIPFtpPktsFrom_Type = Counter64
_HwSecStatIPFtpPktsFrom_Object = MibTableColumn
hwSecStatIPFtpPktsFrom = _HwSecStatIPFtpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 19),
    _HwSecStatIPFtpPktsFrom_Type()
)
hwSecStatIPFtpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPFtpPktsFrom.setStatus("current")
_HwSecStatIPSmtpPktsFrom_Type = Counter64
_HwSecStatIPSmtpPktsFrom_Object = MibTableColumn
hwSecStatIPSmtpPktsFrom = _HwSecStatIPSmtpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 20),
    _HwSecStatIPSmtpPktsFrom_Type()
)
hwSecStatIPSmtpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPSmtpPktsFrom.setStatus("current")
_HwSecStatIPHttpPktsFrom_Type = Counter64
_HwSecStatIPHttpPktsFrom_Object = MibTableColumn
hwSecStatIPHttpPktsFrom = _HwSecStatIPHttpPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 21),
    _HwSecStatIPHttpPktsFrom_Type()
)
hwSecStatIPHttpPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPHttpPktsFrom.setStatus("current")
_HwSecStatIPH323PktsFrom_Type = Counter64
_HwSecStatIPH323PktsFrom_Object = MibTableColumn
hwSecStatIPH323PktsFrom = _HwSecStatIPH323PktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 22),
    _HwSecStatIPH323PktsFrom_Type()
)
hwSecStatIPH323PktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPH323PktsFrom.setStatus("current")
_HwSecStatIPRtspPktsFrom_Type = Counter64
_HwSecStatIPRtspPktsFrom_Object = MibTableColumn
hwSecStatIPRtspPktsFrom = _HwSecStatIPRtspPktsFrom_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 23),
    _HwSecStatIPRtspPktsFrom_Type()
)
hwSecStatIPRtspPktsFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecStatIPRtspPktsFrom.setStatus("current")


class _HwSecStatClearIPOutInfo_Type(Integer32):
    """Custom type hwSecStatClearIPOutInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_HwSecStatClearIPOutInfo_Type.__name__ = "Integer32"
_HwSecStatClearIPOutInfo_Object = MibTableColumn
hwSecStatClearIPOutInfo = _HwSecStatClearIPOutInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 1, 3, 1, 24),
    _HwSecStatClearIPOutInfo_Type()
)
hwSecStatClearIPOutInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSecStatClearIPOutInfo.setStatus("current")
_HwSecStatConformance_ObjectIdentity = ObjectIdentity
hwSecStatConformance = _HwSecStatConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 3)
)
_HwSecStatCompliance_ObjectIdentity = ObjectIdentity
hwSecStatCompliance = _HwSecStatCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 3, 1)
)
_HwSecStatMibGroups_ObjectIdentity = ObjectIdentity
hwSecStatMibGroups = _HwSecStatMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 3, 2)
)

# Managed Objects groups

hwSecStatIPMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 11, 4, 3, 2, 5)
)
hwSecStatIPMonitorGroup.setObjects(
      *(("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPTcpSessTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPUdpSessTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPIcmpSessTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPConnTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHalfConnTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPTcpSessSpeedTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPUdpSessSpeedTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPIcmpSessSpeedTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPConnSpeedTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHalfConnSpeedTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyIcmpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyIcmpOctsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyNonIcmpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyNonIcmpOctsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDftDenyIcmpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPIcmpFloodDropPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPUdpFloodDropPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPFtpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPSmtpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHttpPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPH323PktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPRtspPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPTcpSessFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPUdpSessFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPIcmpSessFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPConnFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHalfConnFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPTcpSessSpeedFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPUdpSessSpeedFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPIcmpSessSpeedFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPConnSpeedFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHalfConnSpeedFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyIcmpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyIcmpOctsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyNonIcmpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDenyNonIcmpOctsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDftDenyIcmpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPFtpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPSmtpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPHttpPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPH323PktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPOutInfoIpAddress"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPInInfoIpAddress"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatClearIPOutInfo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatClearIPInInfo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatClearAllIPInfo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPRtspPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPBlsDenyPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDftDenyPktsTo"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPBlsDenyPktsFrom"),
        ("HUAWEI-SECSTAT-IP-MONITOR-MIB", "hwSecStatIPAclDftDenyPktsFrom"))
)
if mibBuilder.loadTexts:
    hwSecStatIPMonitorGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECSTAT-IP-MONITOR-MIB",
    **{"hwSECSTAT": hwSECSTAT,
       "hwSecStatIPMonitor": hwSecStatIPMonitor,
       "hwSecStatMonitorObjects": hwSecStatMonitorObjects,
       "hwSecStatClearAllIPInfo": hwSecStatClearAllIPInfo,
       "hwSecStatIPInInfoTable": hwSecStatIPInInfoTable,
       "hwSecStatIPInInfoEntry": hwSecStatIPInInfoEntry,
       "hwSecStatIPInInfoIpAddress": hwSecStatIPInInfoIpAddress,
       "hwSecStatIPTcpSessTo": hwSecStatIPTcpSessTo,
       "hwSecStatIPUdpSessTo": hwSecStatIPUdpSessTo,
       "hwSecStatIPIcmpSessTo": hwSecStatIPIcmpSessTo,
       "hwSecStatIPConnTo": hwSecStatIPConnTo,
       "hwSecStatIPHalfConnTo": hwSecStatIPHalfConnTo,
       "hwSecStatIPTcpSessSpeedTo": hwSecStatIPTcpSessSpeedTo,
       "hwSecStatIPUdpSessSpeedTo": hwSecStatIPUdpSessSpeedTo,
       "hwSecStatIPIcmpSessSpeedTo": hwSecStatIPIcmpSessSpeedTo,
       "hwSecStatIPConnSpeedTo": hwSecStatIPConnSpeedTo,
       "hwSecStatIPHalfConnSpeedTo": hwSecStatIPHalfConnSpeedTo,
       "hwSecStatIPAclDenyIcmpPktsTo": hwSecStatIPAclDenyIcmpPktsTo,
       "hwSecStatIPAclDenyIcmpOctsTo": hwSecStatIPAclDenyIcmpOctsTo,
       "hwSecStatIPAclDenyNonIcmpPktsTo": hwSecStatIPAclDenyNonIcmpPktsTo,
       "hwSecStatIPAclDenyNonIcmpOctsTo": hwSecStatIPAclDenyNonIcmpOctsTo,
       "hwSecStatIPBlsDenyPktsTo": hwSecStatIPBlsDenyPktsTo,
       "hwSecStatIPAclDftDenyPktsTo": hwSecStatIPAclDftDenyPktsTo,
       "hwSecStatIPAclDftDenyIcmpPktsTo": hwSecStatIPAclDftDenyIcmpPktsTo,
       "hwSecStatIPIcmpFloodDropPktsTo": hwSecStatIPIcmpFloodDropPktsTo,
       "hwSecStatIPUdpFloodDropPktsTo": hwSecStatIPUdpFloodDropPktsTo,
       "hwSecStatIPFtpPktsTo": hwSecStatIPFtpPktsTo,
       "hwSecStatIPSmtpPktsTo": hwSecStatIPSmtpPktsTo,
       "hwSecStatIPHttpPktsTo": hwSecStatIPHttpPktsTo,
       "hwSecStatIPH323PktsTo": hwSecStatIPH323PktsTo,
       "hwSecStatIPRtspPktsTo": hwSecStatIPRtspPktsTo,
       "hwSecStatClearIPInInfo": hwSecStatClearIPInInfo,
       "hwSecStatIPOutInfoTable": hwSecStatIPOutInfoTable,
       "hwSecStatIPOutInfoEntry": hwSecStatIPOutInfoEntry,
       "hwSecStatIPOutInfoIpAddress": hwSecStatIPOutInfoIpAddress,
       "hwSecStatIPTcpSessFrom": hwSecStatIPTcpSessFrom,
       "hwSecStatIPUdpSessFrom": hwSecStatIPUdpSessFrom,
       "hwSecStatIPIcmpSessFrom": hwSecStatIPIcmpSessFrom,
       "hwSecStatIPConnFrom": hwSecStatIPConnFrom,
       "hwSecStatIPHalfConnFrom": hwSecStatIPHalfConnFrom,
       "hwSecStatIPTcpSessSpeedFrom": hwSecStatIPTcpSessSpeedFrom,
       "hwSecStatIPUdpSessSpeedFrom": hwSecStatIPUdpSessSpeedFrom,
       "hwSecStatIPIcmpSessSpeedFrom": hwSecStatIPIcmpSessSpeedFrom,
       "hwSecStatIPConnSpeedFrom": hwSecStatIPConnSpeedFrom,
       "hwSecStatIPHalfConnSpeedFrom": hwSecStatIPHalfConnSpeedFrom,
       "hwSecStatIPAclDenyIcmpPktsFrom": hwSecStatIPAclDenyIcmpPktsFrom,
       "hwSecStatIPAclDenyIcmpOctsFrom": hwSecStatIPAclDenyIcmpOctsFrom,
       "hwSecStatIPAclDenyNonIcmpPktsFrom": hwSecStatIPAclDenyNonIcmpPktsFrom,
       "hwSecStatIPAclDenyNonIcmpOctsFrom": hwSecStatIPAclDenyNonIcmpOctsFrom,
       "hwSecStatIPBlsDenyPktsFrom": hwSecStatIPBlsDenyPktsFrom,
       "hwSecStatIPAclDftDenyPktsFrom": hwSecStatIPAclDftDenyPktsFrom,
       "hwSecStatIPAclDftDenyIcmpPktsFrom": hwSecStatIPAclDftDenyIcmpPktsFrom,
       "hwSecStatIPFtpPktsFrom": hwSecStatIPFtpPktsFrom,
       "hwSecStatIPSmtpPktsFrom": hwSecStatIPSmtpPktsFrom,
       "hwSecStatIPHttpPktsFrom": hwSecStatIPHttpPktsFrom,
       "hwSecStatIPH323PktsFrom": hwSecStatIPH323PktsFrom,
       "hwSecStatIPRtspPktsFrom": hwSecStatIPRtspPktsFrom,
       "hwSecStatClearIPOutInfo": hwSecStatClearIPOutInfo,
       "hwSecStatConformance": hwSecStatConformance,
       "hwSecStatCompliance": hwSecStatCompliance,
       "hwSecStatMibGroups": hwSecStatMibGroups,
       "hwSecStatIPMonitorGroup": hwSecStatIPMonitorGroup}
)
