# SNMP MIB module (PROXY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PROXY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:55 2024
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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

proxy = ModuleIdentity(
    (1, 3, 6, 1, 3, 25, 17)
)
proxy.setRevisions(
        ("1998-08-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nsfnet_ObjectIdentity = ObjectIdentity
nsfnet = _Nsfnet_ObjectIdentity(
    (1, 3, 6, 1, 3, 25)
)
_ProxySystem_ObjectIdentity = ObjectIdentity
proxySystem = _ProxySystem_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 1)
)
_ProxyMemUsage_Type = Unsigned32
_ProxyMemUsage_Object = MibScalar
proxyMemUsage = _ProxyMemUsage_Object(
    (1, 3, 6, 1, 3, 25, 17, 1, 1),
    _ProxyMemUsage_Type()
)
proxyMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyMemUsage.setStatus("current")
_ProxyStorage_Type = Unsigned32
_ProxyStorage_Object = MibScalar
proxyStorage = _ProxyStorage_Object(
    (1, 3, 6, 1, 3, 25, 17, 1, 2),
    _ProxyStorage_Type()
)
proxyStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyStorage.setStatus("current")
_ProxyCpuUsage_Type = Unsigned32
_ProxyCpuUsage_Object = MibScalar
proxyCpuUsage = _ProxyCpuUsage_Object(
    (1, 3, 6, 1, 3, 25, 17, 1, 3),
    _ProxyCpuUsage_Type()
)
proxyCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyCpuUsage.setStatus("current")
_ProxyUpTime_Type = TimeTicks
_ProxyUpTime_Object = MibScalar
proxyUpTime = _ProxyUpTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 1, 4),
    _ProxyUpTime_Type()
)
proxyUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyUpTime.setStatus("current")
_ProxyConfig_ObjectIdentity = ObjectIdentity
proxyConfig = _ProxyConfig_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 2)
)
_ProxyAdmin_Type = DisplayString
_ProxyAdmin_Object = MibScalar
proxyAdmin = _ProxyAdmin_Object(
    (1, 3, 6, 1, 3, 25, 17, 2, 1),
    _ProxyAdmin_Type()
)
proxyAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyAdmin.setStatus("current")
_ProxySoftware_Type = DisplayString
_ProxySoftware_Object = MibScalar
proxySoftware = _ProxySoftware_Object(
    (1, 3, 6, 1, 3, 25, 17, 2, 2),
    _ProxySoftware_Type()
)
proxySoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxySoftware.setStatus("current")
_ProxyVersion_Type = DisplayString
_ProxyVersion_Object = MibScalar
proxyVersion = _ProxyVersion_Object(
    (1, 3, 6, 1, 3, 25, 17, 2, 3),
    _ProxyVersion_Type()
)
proxyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyVersion.setStatus("current")
_ProxyPerf_ObjectIdentity = ObjectIdentity
proxyPerf = _ProxyPerf_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 3)
)
_ProxySysPerf_ObjectIdentity = ObjectIdentity
proxySysPerf = _ProxySysPerf_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 3, 1)
)
_ProxyCpuLoad_Type = Gauge32
_ProxyCpuLoad_Object = MibScalar
proxyCpuLoad = _ProxyCpuLoad_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 1, 1),
    _ProxyCpuLoad_Type()
)
proxyCpuLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyCpuLoad.setStatus("current")
_ProxyNumObjects_Type = Counter32
_ProxyNumObjects_Object = MibScalar
proxyNumObjects = _ProxyNumObjects_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 1, 2),
    _ProxyNumObjects_Type()
)
proxyNumObjects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyNumObjects.setStatus("current")
_ProxyProtoPerf_ObjectIdentity = ObjectIdentity
proxyProtoPerf = _ProxyProtoPerf_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 3, 2)
)
_ProxyProtoClient_ObjectIdentity = ObjectIdentity
proxyProtoClient = _ProxyProtoClient_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1)
)
_ProxyClientHttpRequests_Type = Counter32
_ProxyClientHttpRequests_Object = MibScalar
proxyClientHttpRequests = _ProxyClientHttpRequests_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1, 1),
    _ProxyClientHttpRequests_Type()
)
proxyClientHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyClientHttpRequests.setStatus("current")
_ProxyClientHttpHits_Type = Counter32
_ProxyClientHttpHits_Object = MibScalar
proxyClientHttpHits = _ProxyClientHttpHits_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1, 2),
    _ProxyClientHttpHits_Type()
)
proxyClientHttpHits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyClientHttpHits.setStatus("current")
_ProxyClientHttpErrors_Type = Counter32
_ProxyClientHttpErrors_Object = MibScalar
proxyClientHttpErrors = _ProxyClientHttpErrors_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1, 3),
    _ProxyClientHttpErrors_Type()
)
proxyClientHttpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyClientHttpErrors.setStatus("current")
_ProxyClientHttpInKbs_Type = Counter32
_ProxyClientHttpInKbs_Object = MibScalar
proxyClientHttpInKbs = _ProxyClientHttpInKbs_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1, 4),
    _ProxyClientHttpInKbs_Type()
)
proxyClientHttpInKbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyClientHttpInKbs.setStatus("current")
_ProxyClientHttpOutKbs_Type = Counter32
_ProxyClientHttpOutKbs_Object = MibScalar
proxyClientHttpOutKbs = _ProxyClientHttpOutKbs_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 1, 5),
    _ProxyClientHttpOutKbs_Type()
)
proxyClientHttpOutKbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyClientHttpOutKbs.setStatus("current")
_ProxyProtoServer_ObjectIdentity = ObjectIdentity
proxyProtoServer = _ProxyProtoServer_ObjectIdentity(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 2)
)
_ProxyServerHttpRequests_Type = Counter32
_ProxyServerHttpRequests_Object = MibScalar
proxyServerHttpRequests = _ProxyServerHttpRequests_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 2, 1),
    _ProxyServerHttpRequests_Type()
)
proxyServerHttpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyServerHttpRequests.setStatus("current")
_ProxyServerHttpErrors_Type = Counter32
_ProxyServerHttpErrors_Object = MibScalar
proxyServerHttpErrors = _ProxyServerHttpErrors_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 2, 2),
    _ProxyServerHttpErrors_Type()
)
proxyServerHttpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyServerHttpErrors.setStatus("current")
_ProxyServerHttpInKbs_Type = Counter32
_ProxyServerHttpInKbs_Object = MibScalar
proxyServerHttpInKbs = _ProxyServerHttpInKbs_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 2, 3),
    _ProxyServerHttpInKbs_Type()
)
proxyServerHttpInKbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyServerHttpInKbs.setStatus("current")
_ProxyServerHttpOutKbs_Type = Counter32
_ProxyServerHttpOutKbs_Object = MibScalar
proxyServerHttpOutKbs = _ProxyServerHttpOutKbs_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 2, 2, 4),
    _ProxyServerHttpOutKbs_Type()
)
proxyServerHttpOutKbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyServerHttpOutKbs.setStatus("current")
_ProxyMedianSvcTable_Object = MibTable
proxyMedianSvcTable = _ProxyMedianSvcTable_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3)
)
if mibBuilder.loadTexts:
    proxyMedianSvcTable.setStatus("current")
_ProxyMedianSvcEntry_Object = MibTableRow
proxyMedianSvcEntry = _ProxyMedianSvcEntry_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1)
)
proxyMedianSvcEntry.setIndexNames(
    (0, "PROXY-MIB", "proxyMedianTime"),
)
if mibBuilder.loadTexts:
    proxyMedianSvcEntry.setStatus("current")
_ProxyMedianTime_Type = Integer32
_ProxyMedianTime_Object = MibTableColumn
proxyMedianTime = _ProxyMedianTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 1),
    _ProxyMedianTime_Type()
)
proxyMedianTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyMedianTime.setStatus("current")
_ProxyHTTPAllSvcTime_Type = Integer32
_ProxyHTTPAllSvcTime_Object = MibTableColumn
proxyHTTPAllSvcTime = _ProxyHTTPAllSvcTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 2),
    _ProxyHTTPAllSvcTime_Type()
)
proxyHTTPAllSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyHTTPAllSvcTime.setStatus("current")
_ProxyHTTPMissSvcTime_Type = Integer32
_ProxyHTTPMissSvcTime_Object = MibTableColumn
proxyHTTPMissSvcTime = _ProxyHTTPMissSvcTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 3),
    _ProxyHTTPMissSvcTime_Type()
)
proxyHTTPMissSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyHTTPMissSvcTime.setStatus("current")
_ProxyHTTPHitSvcTime_Type = Integer32
_ProxyHTTPHitSvcTime_Object = MibTableColumn
proxyHTTPHitSvcTime = _ProxyHTTPHitSvcTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 4),
    _ProxyHTTPHitSvcTime_Type()
)
proxyHTTPHitSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyHTTPHitSvcTime.setStatus("current")
_ProxyHTTPNhSvcTime_Type = Integer32
_ProxyHTTPNhSvcTime_Object = MibTableColumn
proxyHTTPNhSvcTime = _ProxyHTTPNhSvcTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 5),
    _ProxyHTTPNhSvcTime_Type()
)
proxyHTTPNhSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyHTTPNhSvcTime.setStatus("current")
_ProxyDnsSvcTime_Type = Integer32
_ProxyDnsSvcTime_Object = MibTableColumn
proxyDnsSvcTime = _ProxyDnsSvcTime_Object(
    (1, 3, 6, 1, 3, 25, 17, 3, 3, 1, 6),
    _ProxyDnsSvcTime_Type()
)
proxyDnsSvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    proxyDnsSvcTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PROXY-MIB",
    **{"nsfnet": nsfnet,
       "proxy": proxy,
       "proxySystem": proxySystem,
       "proxyMemUsage": proxyMemUsage,
       "proxyStorage": proxyStorage,
       "proxyCpuUsage": proxyCpuUsage,
       "proxyUpTime": proxyUpTime,
       "proxyConfig": proxyConfig,
       "proxyAdmin": proxyAdmin,
       "proxySoftware": proxySoftware,
       "proxyVersion": proxyVersion,
       "proxyPerf": proxyPerf,
       "proxySysPerf": proxySysPerf,
       "proxyCpuLoad": proxyCpuLoad,
       "proxyNumObjects": proxyNumObjects,
       "proxyProtoPerf": proxyProtoPerf,
       "proxyProtoClient": proxyProtoClient,
       "proxyClientHttpRequests": proxyClientHttpRequests,
       "proxyClientHttpHits": proxyClientHttpHits,
       "proxyClientHttpErrors": proxyClientHttpErrors,
       "proxyClientHttpInKbs": proxyClientHttpInKbs,
       "proxyClientHttpOutKbs": proxyClientHttpOutKbs,
       "proxyProtoServer": proxyProtoServer,
       "proxyServerHttpRequests": proxyServerHttpRequests,
       "proxyServerHttpErrors": proxyServerHttpErrors,
       "proxyServerHttpInKbs": proxyServerHttpInKbs,
       "proxyServerHttpOutKbs": proxyServerHttpOutKbs,
       "proxyMedianSvcTable": proxyMedianSvcTable,
       "proxyMedianSvcEntry": proxyMedianSvcEntry,
       "proxyMedianTime": proxyMedianTime,
       "proxyHTTPAllSvcTime": proxyHTTPAllSvcTime,
       "proxyHTTPMissSvcTime": proxyHTTPMissSvcTime,
       "proxyHTTPHitSvcTime": proxyHTTPHitSvcTime,
       "proxyHTTPNhSvcTime": proxyHTTPNhSvcTime,
       "proxyDnsSvcTime": proxyDnsSvcTime}
)
