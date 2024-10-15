# SNMP MIB module (F5-BIGIP-WAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F5-BIGIP-WAM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:38 2024
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

(LongDisplayString,
 bigipCompliances,
 bigipGroups,
 bigipTrafficMgmt) = mibBuilder.importSymbols(
    "F5-BIGIP-COMMON-MIB",
    "LongDisplayString",
    "bigipCompliances",
    "bigipGroups",
    "bigipTrafficMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

bigipWAM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BigipWAMGroups_ObjectIdentity = ObjectIdentity
bigipWAMGroups = _BigipWAMGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7)
)
_WamAppStat_ObjectIdentity = ObjectIdentity
wamAppStat = _WamAppStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1)
)
_WamAppStatResetStats_Type = Integer32
_WamAppStatResetStats_Object = MibScalar
wamAppStatResetStats = _WamAppStatResetStats_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 1),
    _WamAppStatResetStats_Type()
)
wamAppStatResetStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wamAppStatResetStats.setStatus("current")
_WamAppStatNumber_Type = Integer32
_WamAppStatNumber_Object = MibScalar
wamAppStatNumber = _WamAppStatNumber_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 2),
    _WamAppStatNumber_Type()
)
wamAppStatNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatNumber.setStatus("current")
_WamAppStatTable_Object = MibTable
wamAppStatTable = _WamAppStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    wamAppStatTable.setStatus("current")
_WamAppStatEntry_Object = MibTableRow
wamAppStatEntry = _WamAppStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1)
)
wamAppStatEntry.setIndexNames(
    (0, "F5-BIGIP-WAM-MIB", "wamAppStatName"),
)
if mibBuilder.loadTexts:
    wamAppStatEntry.setStatus("current")
_WamAppStatName_Type = LongDisplayString
_WamAppStatName_Object = MibTableColumn
wamAppStatName = _WamAppStatName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 1),
    _WamAppStatName_Type()
)
wamAppStatName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatName.setStatus("current")
_WamAppStatVsName_Type = LongDisplayString
_WamAppStatVsName_Object = MibTableColumn
wamAppStatVsName = _WamAppStatVsName_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 2),
    _WamAppStatVsName_Type()
)
wamAppStatVsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatVsName.setStatus("current")
_WamAppStatRqstTotal_Type = Counter64
_WamAppStatRqstTotal_Object = MibTableColumn
wamAppStatRqstTotal = _WamAppStatRqstTotal_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 3),
    _WamAppStatRqstTotal_Type()
)
wamAppStatRqstTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatRqstTotal.setStatus("current")
_WamAppStatProxied_Type = Counter64
_WamAppStatProxied_Object = MibTableColumn
wamAppStatProxied = _WamAppStatProxied_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 4),
    _WamAppStatProxied_Type()
)
wamAppStatProxied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied.setStatus("current")
_WamAppStatProxiedBytes_Type = Counter64
_WamAppStatProxiedBytes_Object = MibTableColumn
wamAppStatProxiedBytes = _WamAppStatProxiedBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 5),
    _WamAppStatProxiedBytes_Type()
)
wamAppStatProxiedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedBytes.setStatus("current")
_WamAppStatProxied1500_Type = Counter64
_WamAppStatProxied1500_Object = MibTableColumn
wamAppStatProxied1500 = _WamAppStatProxied1500_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 6),
    _WamAppStatProxied1500_Type()
)
wamAppStatProxied1500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied1500.setStatus("current")
_WamAppStatProxied10k_Type = Counter64
_WamAppStatProxied10k_Object = MibTableColumn
wamAppStatProxied10k = _WamAppStatProxied10k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 7),
    _WamAppStatProxied10k_Type()
)
wamAppStatProxied10k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied10k.setStatus("current")
_WamAppStatProxied50k_Type = Counter64
_WamAppStatProxied50k_Object = MibTableColumn
wamAppStatProxied50k = _WamAppStatProxied50k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 8),
    _WamAppStatProxied50k_Type()
)
wamAppStatProxied50k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied50k.setStatus("current")
_WamAppStatProxied100k_Type = Counter64
_WamAppStatProxied100k_Object = MibTableColumn
wamAppStatProxied100k = _WamAppStatProxied100k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 9),
    _WamAppStatProxied100k_Type()
)
wamAppStatProxied100k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied100k.setStatus("current")
_WamAppStatProxied500k_Type = Counter64
_WamAppStatProxied500k_Object = MibTableColumn
wamAppStatProxied500k = _WamAppStatProxied500k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 10),
    _WamAppStatProxied500k_Type()
)
wamAppStatProxied500k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied500k.setStatus("current")
_WamAppStatProxied1m_Type = Counter64
_WamAppStatProxied1m_Object = MibTableColumn
wamAppStatProxied1m = _WamAppStatProxied1m_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 11),
    _WamAppStatProxied1m_Type()
)
wamAppStatProxied1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied1m.setStatus("current")
_WamAppStatProxied5m_Type = Counter64
_WamAppStatProxied5m_Object = MibTableColumn
wamAppStatProxied5m = _WamAppStatProxied5m_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 12),
    _WamAppStatProxied5m_Type()
)
wamAppStatProxied5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxied5m.setStatus("current")
_WamAppStatProxiedLarge_Type = Counter64
_WamAppStatProxiedLarge_Object = MibTableColumn
wamAppStatProxiedLarge = _WamAppStatProxiedLarge_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 13),
    _WamAppStatProxiedLarge_Type()
)
wamAppStatProxiedLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedLarge.setStatus("current")
_WamAppStatProxiedNew_Type = Counter64
_WamAppStatProxiedNew_Object = MibTableColumn
wamAppStatProxiedNew = _WamAppStatProxiedNew_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 14),
    _WamAppStatProxiedNew_Type()
)
wamAppStatProxiedNew.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedNew.setStatus("current")
_WamAppStatProxiedExpired_Type = Counter64
_WamAppStatProxiedExpired_Object = MibTableColumn
wamAppStatProxiedExpired = _WamAppStatProxiedExpired_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 15),
    _WamAppStatProxiedExpired_Type()
)
wamAppStatProxiedExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedExpired.setStatus("current")
_WamAppStatProxiedPerPolicy_Type = Counter64
_WamAppStatProxiedPerPolicy_Object = MibTableColumn
wamAppStatProxiedPerPolicy = _WamAppStatProxiedPerPolicy_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 16),
    _WamAppStatProxiedPerPolicy_Type()
)
wamAppStatProxiedPerPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedPerPolicy.setStatus("current")
_WamAppStatProxiedPerIrule_Type = Counter64
_WamAppStatProxiedPerIrule_Object = MibTableColumn
wamAppStatProxiedPerIrule = _WamAppStatProxiedPerIrule_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 17),
    _WamAppStatProxiedPerIrule_Type()
)
wamAppStatProxiedPerIrule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedPerIrule.setStatus("current")
_WamAppStatProxiedPerInvalidation_Type = Counter64
_WamAppStatProxiedPerInvalidation_Object = MibTableColumn
wamAppStatProxiedPerInvalidation = _WamAppStatProxiedPerInvalidation_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 18),
    _WamAppStatProxiedPerInvalidation_Type()
)
wamAppStatProxiedPerInvalidation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedPerInvalidation.setStatus("current")
_WamAppStatProxiedPerClientRequest_Type = Counter64
_WamAppStatProxiedPerClientRequest_Object = MibTableColumn
wamAppStatProxiedPerClientRequest = _WamAppStatProxiedPerClientRequest_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 19),
    _WamAppStatProxiedPerClientRequest_Type()
)
wamAppStatProxiedPerClientRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedPerClientRequest.setStatus("current")
_WamAppStatProxiedBypass_Type = Counter64
_WamAppStatProxiedBypass_Object = MibTableColumn
wamAppStatProxiedBypass = _WamAppStatProxiedBypass_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 20),
    _WamAppStatProxiedBypass_Type()
)
wamAppStatProxiedBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatProxiedBypass.setStatus("current")
_WamAppStatFromCache_Type = Counter64
_WamAppStatFromCache_Object = MibTableColumn
wamAppStatFromCache = _WamAppStatFromCache_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 21),
    _WamAppStatFromCache_Type()
)
wamAppStatFromCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache.setStatus("current")
_WamAppStatFromCacheBytes_Type = Counter64
_WamAppStatFromCacheBytes_Object = MibTableColumn
wamAppStatFromCacheBytes = _WamAppStatFromCacheBytes_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 22),
    _WamAppStatFromCacheBytes_Type()
)
wamAppStatFromCacheBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCacheBytes.setStatus("current")
_WamAppStatFromCache1500_Type = Counter64
_WamAppStatFromCache1500_Object = MibTableColumn
wamAppStatFromCache1500 = _WamAppStatFromCache1500_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 23),
    _WamAppStatFromCache1500_Type()
)
wamAppStatFromCache1500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache1500.setStatus("current")
_WamAppStatFromCache10k_Type = Counter64
_WamAppStatFromCache10k_Object = MibTableColumn
wamAppStatFromCache10k = _WamAppStatFromCache10k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 24),
    _WamAppStatFromCache10k_Type()
)
wamAppStatFromCache10k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache10k.setStatus("current")
_WamAppStatFromCache50k_Type = Counter64
_WamAppStatFromCache50k_Object = MibTableColumn
wamAppStatFromCache50k = _WamAppStatFromCache50k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 25),
    _WamAppStatFromCache50k_Type()
)
wamAppStatFromCache50k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache50k.setStatus("current")
_WamAppStatFromCache100k_Type = Counter64
_WamAppStatFromCache100k_Object = MibTableColumn
wamAppStatFromCache100k = _WamAppStatFromCache100k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 26),
    _WamAppStatFromCache100k_Type()
)
wamAppStatFromCache100k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache100k.setStatus("current")
_WamAppStatFromCache500k_Type = Counter64
_WamAppStatFromCache500k_Object = MibTableColumn
wamAppStatFromCache500k = _WamAppStatFromCache500k_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 27),
    _WamAppStatFromCache500k_Type()
)
wamAppStatFromCache500k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache500k.setStatus("current")
_WamAppStatFromCache1m_Type = Counter64
_WamAppStatFromCache1m_Object = MibTableColumn
wamAppStatFromCache1m = _WamAppStatFromCache1m_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 28),
    _WamAppStatFromCache1m_Type()
)
wamAppStatFromCache1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache1m.setStatus("current")
_WamAppStatFromCache5m_Type = Counter64
_WamAppStatFromCache5m_Object = MibTableColumn
wamAppStatFromCache5m = _WamAppStatFromCache5m_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 29),
    _WamAppStatFromCache5m_Type()
)
wamAppStatFromCache5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCache5m.setStatus("current")
_WamAppStatFromCacheLarge_Type = Counter64
_WamAppStatFromCacheLarge_Object = MibTableColumn
wamAppStatFromCacheLarge = _WamAppStatFromCacheLarge_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 30),
    _WamAppStatFromCacheLarge_Type()
)
wamAppStatFromCacheLarge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatFromCacheLarge.setStatus("current")
_WamAppStatOws2xx_Type = Counter64
_WamAppStatOws2xx_Object = MibTableColumn
wamAppStatOws2xx = _WamAppStatOws2xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 31),
    _WamAppStatOws2xx_Type()
)
wamAppStatOws2xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOws2xx.setStatus("current")
_WamAppStatOws3xx_Type = Counter64
_WamAppStatOws3xx_Object = MibTableColumn
wamAppStatOws3xx = _WamAppStatOws3xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 32),
    _WamAppStatOws3xx_Type()
)
wamAppStatOws3xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOws3xx.setStatus("current")
_WamAppStatOws4xx_Type = Counter64
_WamAppStatOws4xx_Object = MibTableColumn
wamAppStatOws4xx = _WamAppStatOws4xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 33),
    _WamAppStatOws4xx_Type()
)
wamAppStatOws4xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOws4xx.setStatus("current")
_WamAppStatOws5xx_Type = Counter64
_WamAppStatOws5xx_Object = MibTableColumn
wamAppStatOws5xx = _WamAppStatOws5xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 34),
    _WamAppStatOws5xx_Type()
)
wamAppStatOws5xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOws5xx.setStatus("current")
_WamAppStatOwsDropped_Type = Counter64
_WamAppStatOwsDropped_Object = MibTableColumn
wamAppStatOwsDropped = _WamAppStatOwsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 35),
    _WamAppStatOwsDropped_Type()
)
wamAppStatOwsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOwsDropped.setStatus("current")
_WamAppStatOwsRejected_Type = Counter64
_WamAppStatOwsRejected_Object = MibTableColumn
wamAppStatOwsRejected = _WamAppStatOwsRejected_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 36),
    _WamAppStatOwsRejected_Type()
)
wamAppStatOwsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatOwsRejected.setStatus("current")
_WamAppStatWam2xx_Type = Counter64
_WamAppStatWam2xx_Object = MibTableColumn
wamAppStatWam2xx = _WamAppStatWam2xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 37),
    _WamAppStatWam2xx_Type()
)
wamAppStatWam2xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWam2xx.setStatus("current")
_WamAppStatWam3xx_Type = Counter64
_WamAppStatWam3xx_Object = MibTableColumn
wamAppStatWam3xx = _WamAppStatWam3xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 38),
    _WamAppStatWam3xx_Type()
)
wamAppStatWam3xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWam3xx.setStatus("current")
_WamAppStatWam4xx_Type = Counter64
_WamAppStatWam4xx_Object = MibTableColumn
wamAppStatWam4xx = _WamAppStatWam4xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 39),
    _WamAppStatWam4xx_Type()
)
wamAppStatWam4xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWam4xx.setStatus("current")
_WamAppStatWam5xx_Type = Counter64
_WamAppStatWam5xx_Object = MibTableColumn
wamAppStatWam5xx = _WamAppStatWam5xx_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 40),
    _WamAppStatWam5xx_Type()
)
wamAppStatWam5xx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWam5xx.setStatus("current")
_WamAppStatWam503_Type = Counter64
_WamAppStatWam503_Object = MibTableColumn
wamAppStatWam503 = _WamAppStatWam503_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 41),
    _WamAppStatWam503_Type()
)
wamAppStatWam503.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWam503.setStatus("current")
_WamAppStatWamDropped_Type = Counter64
_WamAppStatWamDropped_Object = MibTableColumn
wamAppStatWamDropped = _WamAppStatWamDropped_Object(
    (1, 3, 6, 1, 4, 1, 3375, 2, 7, 1, 3, 1, 42),
    _WamAppStatWamDropped_Type()
)
wamAppStatWamDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wamAppStatWamDropped.setStatus("current")

# Managed Objects groups

wamAppStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 2, 7, 1)
)
wamAppStatGroup.setObjects(
      *(("F5-BIGIP-WAM-MIB", "wamAppStatResetStats"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatNumber"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatName"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatVsName"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatRqstTotal"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBytes"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1500"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied10k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied50k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied100k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied500k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied1m"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxied5m"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedLarge"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedNew"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedExpired"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerPolicy"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerIrule"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerInvalidation"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedPerClientRequest"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatProxiedBypass"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheBytes"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1500"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache10k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache50k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache100k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache500k"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache1m"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCache5m"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatFromCacheLarge"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOws2xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOws3xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOws4xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOws5xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOwsDropped"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatOwsRejected"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWam2xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWam3xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWam4xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWam5xx"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWam503"),
        ("F5-BIGIP-WAM-MIB", "wamAppStatWamDropped"))
)
if mibBuilder.loadTexts:
    wamAppStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bigipWAMCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3375, 2, 5, 1, 7)
)
if mibBuilder.loadTexts:
    bigipWAMCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F5-BIGIP-WAM-MIB",
    **{"bigipWAMCompliance": bigipWAMCompliance,
       "bigipWAMGroups": bigipWAMGroups,
       "wamAppStatGroup": wamAppStatGroup,
       "bigipWAM": bigipWAM,
       "wamAppStat": wamAppStat,
       "wamAppStatResetStats": wamAppStatResetStats,
       "wamAppStatNumber": wamAppStatNumber,
       "wamAppStatTable": wamAppStatTable,
       "wamAppStatEntry": wamAppStatEntry,
       "wamAppStatName": wamAppStatName,
       "wamAppStatVsName": wamAppStatVsName,
       "wamAppStatRqstTotal": wamAppStatRqstTotal,
       "wamAppStatProxied": wamAppStatProxied,
       "wamAppStatProxiedBytes": wamAppStatProxiedBytes,
       "wamAppStatProxied1500": wamAppStatProxied1500,
       "wamAppStatProxied10k": wamAppStatProxied10k,
       "wamAppStatProxied50k": wamAppStatProxied50k,
       "wamAppStatProxied100k": wamAppStatProxied100k,
       "wamAppStatProxied500k": wamAppStatProxied500k,
       "wamAppStatProxied1m": wamAppStatProxied1m,
       "wamAppStatProxied5m": wamAppStatProxied5m,
       "wamAppStatProxiedLarge": wamAppStatProxiedLarge,
       "wamAppStatProxiedNew": wamAppStatProxiedNew,
       "wamAppStatProxiedExpired": wamAppStatProxiedExpired,
       "wamAppStatProxiedPerPolicy": wamAppStatProxiedPerPolicy,
       "wamAppStatProxiedPerIrule": wamAppStatProxiedPerIrule,
       "wamAppStatProxiedPerInvalidation": wamAppStatProxiedPerInvalidation,
       "wamAppStatProxiedPerClientRequest": wamAppStatProxiedPerClientRequest,
       "wamAppStatProxiedBypass": wamAppStatProxiedBypass,
       "wamAppStatFromCache": wamAppStatFromCache,
       "wamAppStatFromCacheBytes": wamAppStatFromCacheBytes,
       "wamAppStatFromCache1500": wamAppStatFromCache1500,
       "wamAppStatFromCache10k": wamAppStatFromCache10k,
       "wamAppStatFromCache50k": wamAppStatFromCache50k,
       "wamAppStatFromCache100k": wamAppStatFromCache100k,
       "wamAppStatFromCache500k": wamAppStatFromCache500k,
       "wamAppStatFromCache1m": wamAppStatFromCache1m,
       "wamAppStatFromCache5m": wamAppStatFromCache5m,
       "wamAppStatFromCacheLarge": wamAppStatFromCacheLarge,
       "wamAppStatOws2xx": wamAppStatOws2xx,
       "wamAppStatOws3xx": wamAppStatOws3xx,
       "wamAppStatOws4xx": wamAppStatOws4xx,
       "wamAppStatOws5xx": wamAppStatOws5xx,
       "wamAppStatOwsDropped": wamAppStatOwsDropped,
       "wamAppStatOwsRejected": wamAppStatOwsRejected,
       "wamAppStatWam2xx": wamAppStatWam2xx,
       "wamAppStatWam3xx": wamAppStatWam3xx,
       "wamAppStatWam4xx": wamAppStatWam4xx,
       "wamAppStatWam5xx": wamAppStatWam5xx,
       "wamAppStatWam503": wamAppStatWam503,
       "wamAppStatWamDropped": wamAppStatWamDropped}
)
