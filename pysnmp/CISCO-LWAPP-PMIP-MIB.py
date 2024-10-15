# SNMP MIB module (CISCO-LWAPP-PMIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-PMIP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:51 2024
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

(cldcClientMacAddress,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-DOT11-CLIENT-MIB",
    "cldcClientMacAddress")

(cLWlanIndex,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-WLAN-MIB",
    "cLWlanIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappPmipMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 888)
)
ciscoLwappPmipMIB.setRevisions(
        ("1970-01-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappPmipMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappPmipMIBObjects = _CiscoLwappPmipMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0)
)
_CiscoLwappPmipGlobal_ObjectIdentity = ObjectIdentity
ciscoLwappPmipGlobal = _CiscoLwappPmipGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1)
)
_CLPmipDomainName_Type = SnmpAdminString
_CLPmipDomainName_Object = MibScalar
cLPmipDomainName = _CLPmipDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 1),
    _CLPmipDomainName_Type()
)
cLPmipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipDomainName.setStatus("current")


class _CLPmipMAGInterface_Type(SnmpAdminString):
    """Custom type cLPmipMAGInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLPmipMAGInterface_Type.__name__ = "SnmpAdminString"
_CLPmipMAGInterface_Object = MibScalar
cLPmipMAGInterface = _CLPmipMAGInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 2),
    _CLPmipMAGInterface_Type()
)
cLPmipMAGInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipMAGInterface.setStatus("current")
_CLPmipMaxBindings_Type = Unsigned32
_CLPmipMaxBindings_Object = MibScalar
cLPmipMaxBindings = _CLPmipMaxBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 3),
    _CLPmipMaxBindings_Type()
)
cLPmipMaxBindings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipMaxBindings.setStatus("current")
_CLPmipBindingLifeTime_Type = TimeTicks
_CLPmipBindingLifeTime_Object = MibScalar
cLPmipBindingLifeTime = _CLPmipBindingLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 4),
    _CLPmipBindingLifeTime_Type()
)
cLPmipBindingLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBindingLifeTime.setStatus("current")
_CLPmipBindingRefreshTime_Type = TimeTicks
_CLPmipBindingRefreshTime_Object = MibScalar
cLPmipBindingRefreshTime = _CLPmipBindingRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 5),
    _CLPmipBindingRefreshTime_Type()
)
cLPmipBindingRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBindingRefreshTime.setStatus("current")
_CLPmipBindingInitRetxTime_Type = TimeTicks
_CLPmipBindingInitRetxTime_Object = MibScalar
cLPmipBindingInitRetxTime = _CLPmipBindingInitRetxTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 6),
    _CLPmipBindingInitRetxTime_Type()
)
cLPmipBindingInitRetxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBindingInitRetxTime.setStatus("current")
_CLPmipBindingMaxRetxTime_Type = TimeTicks
_CLPmipBindingMaxRetxTime_Object = MibScalar
cLPmipBindingMaxRetxTime = _CLPmipBindingMaxRetxTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 7),
    _CLPmipBindingMaxRetxTime_Type()
)
cLPmipBindingMaxRetxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBindingMaxRetxTime.setStatus("current")
_CLPmipReplayProtectionTimestamp_Type = TimeStamp
_CLPmipReplayProtectionTimestamp_Object = MibScalar
cLPmipReplayProtectionTimestamp = _CLPmipReplayProtectionTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 8),
    _CLPmipReplayProtectionTimestamp_Type()
)
cLPmipReplayProtectionTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipReplayProtectionTimestamp.setStatus("current")
_CLPmipBriMinDelayTime_Type = TimeTicks
_CLPmipBriMinDelayTime_Object = MibScalar
cLPmipBriMinDelayTime = _CLPmipBriMinDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 9),
    _CLPmipBriMinDelayTime_Type()
)
cLPmipBriMinDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBriMinDelayTime.setStatus("current")
_CLPmipBriMaxDelayTime_Type = TimeTicks
_CLPmipBriMaxDelayTime_Object = MibScalar
cLPmipBriMaxDelayTime = _CLPmipBriMaxDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 10),
    _CLPmipBriMaxDelayTime_Type()
)
cLPmipBriMaxDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBriMaxDelayTime.setStatus("current")
_CLPmipBriRetries_Type = Unsigned32
_CLPmipBriRetries_Object = MibScalar
cLPmipBriRetries = _CLPmipBriRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 11),
    _CLPmipBriRetries_Type()
)
cLPmipBriRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipBriRetries.setStatus("current")
_CLPmipMagApnName_Type = SnmpAdminString
_CLPmipMagApnName_Object = MibScalar
cLPmipMagApnName = _CLPmipMagApnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 1, 12),
    _CLPmipMagApnName_Type()
)
cLPmipMagApnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipMagApnName.setStatus("current")
_CiscoLwappPmipConfig_ObjectIdentity = ObjectIdentity
ciscoLwappPmipConfig = _CiscoLwappPmipConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2)
)
_CLPmipLmaTable_Object = MibTable
cLPmipLmaTable = _CLPmipLmaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1)
)
if mibBuilder.loadTexts:
    cLPmipLmaTable.setStatus("current")
_CLPmipLmaEntry_Object = MibTableRow
cLPmipLmaEntry = _CLPmipLmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1)
)
cLPmipLmaEntry.setIndexNames(
    (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"),
)
if mibBuilder.loadTexts:
    cLPmipLmaEntry.setStatus("current")
_CLPmipLmaName_Type = SnmpAdminString
_CLPmipLmaName_Object = MibTableColumn
cLPmipLmaName = _CLPmipLmaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 1),
    _CLPmipLmaName_Type()
)
cLPmipLmaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipLmaName.setStatus("current")
_CLPmipLmaIPAddrType_Type = InetAddressType
_CLPmipLmaIPAddrType_Object = MibTableColumn
cLPmipLmaIPAddrType = _CLPmipLmaIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 2),
    _CLPmipLmaIPAddrType_Type()
)
cLPmipLmaIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipLmaIPAddrType.setStatus("current")
_CLPmipLmaIPAddr_Type = InetAddress
_CLPmipLmaIPAddr_Object = MibTableColumn
cLPmipLmaIPAddr = _CLPmipLmaIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 3),
    _CLPmipLmaIPAddr_Type()
)
cLPmipLmaIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipLmaIPAddr.setStatus("current")
_CLPmipLmaRowStatus_Type = RowStatus
_CLPmipLmaRowStatus_Object = MibTableColumn
cLPmipLmaRowStatus = _CLPmipLmaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 1, 1, 4),
    _CLPmipLmaRowStatus_Type()
)
cLPmipLmaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipLmaRowStatus.setStatus("current")
_CLPmipProfileTable_Object = MibTable
cLPmipProfileTable = _CLPmipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2)
)
if mibBuilder.loadTexts:
    cLPmipProfileTable.setStatus("current")
_CLPmipProfileEntry_Object = MibTableRow
cLPmipProfileEntry = _CLPmipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1)
)
cLPmipProfileEntry.setIndexNames(
    (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"),
)
if mibBuilder.loadTexts:
    cLPmipProfileEntry.setStatus("current")
_CLPmipProfileName_Type = SnmpAdminString
_CLPmipProfileName_Object = MibTableColumn
cLPmipProfileName = _CLPmipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 2, 1, 1),
    _CLPmipProfileName_Type()
)
cLPmipProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipProfileName.setStatus("current")
_CLPmipProfileNaiTable_Object = MibTable
cLPmipProfileNaiTable = _CLPmipProfileNaiTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3)
)
if mibBuilder.loadTexts:
    cLPmipProfileNaiTable.setStatus("current")
_CLPmipProfileNaiEntry_Object = MibTableRow
cLPmipProfileNaiEntry = _CLPmipProfileNaiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1)
)
cLPmipProfileNaiEntry.setIndexNames(
    (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileName"),
    (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipProfileNai"),
)
if mibBuilder.loadTexts:
    cLPmipProfileNaiEntry.setStatus("current")
_CLPmipProfileNai_Type = SnmpAdminString
_CLPmipProfileNai_Object = MibTableColumn
cLPmipProfileNai = _CLPmipProfileNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 1),
    _CLPmipProfileNai_Type()
)
cLPmipProfileNai.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipProfileNai.setStatus("current")
_CLPmipProfileApn_Type = SnmpAdminString
_CLPmipProfileApn_Object = MibTableColumn
cLPmipProfileApn = _CLPmipProfileApn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 2),
    _CLPmipProfileApn_Type()
)
cLPmipProfileApn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipProfileApn.setStatus("current")
_CLPmipProfileLmaName_Type = SnmpAdminString
_CLPmipProfileLmaName_Object = MibTableColumn
cLPmipProfileLmaName = _CLPmipProfileLmaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 3),
    _CLPmipProfileLmaName_Type()
)
cLPmipProfileLmaName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipProfileLmaName.setStatus("current")
_CLPmipProfileNaiRowStatus_Type = RowStatus
_CLPmipProfileNaiRowStatus_Object = MibTableColumn
cLPmipProfileNaiRowStatus = _CLPmipProfileNaiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 3, 1, 4),
    _CLPmipProfileNaiRowStatus_Type()
)
cLPmipProfileNaiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cLPmipProfileNaiRowStatus.setStatus("current")
_CLPmipWlanTable_Object = MibTable
cLPmipWlanTable = _CLPmipWlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4)
)
if mibBuilder.loadTexts:
    cLPmipWlanTable.setStatus("current")
_CLPmipWlanEntry_Object = MibTableRow
cLPmipWlanEntry = _CLPmipWlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1)
)
cLPmipWlanEntry.setIndexNames(
    (0, "CISCO-LWAPP-WLAN-MIB", "cLWlanIndex"),
)
if mibBuilder.loadTexts:
    cLPmipWlanEntry.setStatus("current")
_CLPmipWlanProfileName_Type = SnmpAdminString
_CLPmipWlanProfileName_Object = MibTableColumn
cLPmipWlanProfileName = _CLPmipWlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 1),
    _CLPmipWlanProfileName_Type()
)
cLPmipWlanProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipWlanProfileName.setStatus("current")


class _CLPmipWlanMobilityType_Type(Integer32):
    """Custom type cLPmipWlanMobilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("pmipv6", 2))
    )


_CLPmipWlanMobilityType_Type.__name__ = "Integer32"
_CLPmipWlanMobilityType_Object = MibTableColumn
cLPmipWlanMobilityType = _CLPmipWlanMobilityType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 2),
    _CLPmipWlanMobilityType_Type()
)
cLPmipWlanMobilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipWlanMobilityType.setStatus("current")
_CLPmipWlanDefaultRealm_Type = SnmpAdminString
_CLPmipWlanDefaultRealm_Object = MibTableColumn
cLPmipWlanDefaultRealm = _CLPmipWlanDefaultRealm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 2, 4, 1, 3),
    _CLPmipWlanDefaultRealm_Type()
)
cLPmipWlanDefaultRealm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cLPmipWlanDefaultRealm.setStatus("current")
_CiscoLwappPmipStatistics_ObjectIdentity = ObjectIdentity
ciscoLwappPmipStatistics = _CiscoLwappPmipStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3)
)
_CLPmipLmaStatsTable_Object = MibTable
cLPmipLmaStatsTable = _CLPmipLmaStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1)
)
if mibBuilder.loadTexts:
    cLPmipLmaStatsTable.setStatus("current")
_CLPmipLmaStatsEntry_Object = MibTableRow
cLPmipLmaStatsEntry = _CLPmipLmaStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1)
)
cLPmipLmaStatsEntry.setIndexNames(
    (0, "CISCO-LWAPP-PMIP-MIB", "cLPmipLmaName"),
)
if mibBuilder.loadTexts:
    cLPmipLmaStatsEntry.setStatus("current")
_CLPmipLmaTotalBindings_Type = Counter32
_CLPmipLmaTotalBindings_Object = MibTableColumn
cLPmipLmaTotalBindings = _CLPmipLmaTotalBindings_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 1),
    _CLPmipLmaTotalBindings_Type()
)
cLPmipLmaTotalBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaTotalBindings.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaTotalBindings.setUnits("packets")
_CLPmipLmaPbuSent_Type = Counter32
_CLPmipLmaPbuSent_Object = MibTableColumn
cLPmipLmaPbuSent = _CLPmipLmaPbuSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 2),
    _CLPmipLmaPbuSent_Type()
)
cLPmipLmaPbuSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbuSent.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbuSent.setUnits("packets")
_CLPmipLmaPbaReceived_Type = Counter32
_CLPmipLmaPbaReceived_Object = MibTableColumn
cLPmipLmaPbaReceived = _CLPmipLmaPbaReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 3),
    _CLPmipLmaPbaReceived_Type()
)
cLPmipLmaPbaReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbaReceived.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbaReceived.setUnits("packets")
_CLPmipLmaPbriSent_Type = Counter32
_CLPmipLmaPbriSent_Object = MibTableColumn
cLPmipLmaPbriSent = _CLPmipLmaPbriSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 4),
    _CLPmipLmaPbriSent_Type()
)
cLPmipLmaPbriSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbriSent.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbriSent.setUnits("packets")
_CLPmipLmaPbriReceived_Type = Counter32
_CLPmipLmaPbriReceived_Object = MibTableColumn
cLPmipLmaPbriReceived = _CLPmipLmaPbriReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 5),
    _CLPmipLmaPbriReceived_Type()
)
cLPmipLmaPbriReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbriReceived.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbriReceived.setUnits("packets")
_CLPmipLmaPbraSent_Type = Counter32
_CLPmipLmaPbraSent_Object = MibTableColumn
cLPmipLmaPbraSent = _CLPmipLmaPbraSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 6),
    _CLPmipLmaPbraSent_Type()
)
cLPmipLmaPbraSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbraSent.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbraSent.setUnits("packets")
_CLPmipLmaPbraReceived_Type = Counter32
_CLPmipLmaPbraReceived_Object = MibTableColumn
cLPmipLmaPbraReceived = _CLPmipLmaPbraReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 7),
    _CLPmipLmaPbraReceived_Type()
)
cLPmipLmaPbraReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbraReceived.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbraReceived.setUnits("packets")
_CLPmipLmaNoOfHandoff_Type = Counter32
_CLPmipLmaNoOfHandoff_Object = MibTableColumn
cLPmipLmaNoOfHandoff = _CLPmipLmaNoOfHandoff_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 8),
    _CLPmipLmaNoOfHandoff_Type()
)
cLPmipLmaNoOfHandoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaNoOfHandoff.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaNoOfHandoff.setUnits("packets")
_CLPmipLmaPbuDropped_Type = Counter32
_CLPmipLmaPbuDropped_Object = MibTableColumn
cLPmipLmaPbuDropped = _CLPmipLmaPbuDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 1, 1, 9),
    _CLPmipLmaPbuDropped_Type()
)
cLPmipLmaPbuDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipLmaPbuDropped.setStatus("current")
if mibBuilder.loadTexts:
    cLPmipLmaPbuDropped.setUnits("packets")
_CLPmipClientInfoTable_Object = MibTable
cLPmipClientInfoTable = _CLPmipClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2)
)
if mibBuilder.loadTexts:
    cLPmipClientInfoTable.setStatus("current")
_CLPmipClientInfoEntry_Object = MibTableRow
cLPmipClientInfoEntry = _CLPmipClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1)
)
cLPmipClientInfoEntry.setIndexNames(
    (0, "CISCO-LWAPP-DOT11-CLIENT-MIB", "cldcClientMacAddress"),
)
if mibBuilder.loadTexts:
    cLPmipClientInfoEntry.setStatus("current")
_CLPmipClientNai_Type = SnmpAdminString
_CLPmipClientNai_Object = MibTableColumn
cLPmipClientNai = _CLPmipClientNai_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 1),
    _CLPmipClientNai_Type()
)
cLPmipClientNai.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientNai.setStatus("current")
_CLPmipClientState_Type = SnmpAdminString
_CLPmipClientState_Object = MibTableColumn
cLPmipClientState = _CLPmipClientState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 2),
    _CLPmipClientState_Type()
)
cLPmipClientState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientState.setStatus("current")


class _CLPmipClientInterface_Type(SnmpAdminString):
    """Custom type cLPmipClientInterface based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CLPmipClientInterface_Type.__name__ = "SnmpAdminString"
_CLPmipClientInterface_Object = MibTableColumn
cLPmipClientInterface = _CLPmipClientInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 3),
    _CLPmipClientInterface_Type()
)
cLPmipClientInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientInterface.setStatus("current")
_CLPmipClientHomeAddressType_Type = InetAddressType
_CLPmipClientHomeAddressType_Object = MibTableColumn
cLPmipClientHomeAddressType = _CLPmipClientHomeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 4),
    _CLPmipClientHomeAddressType_Type()
)
cLPmipClientHomeAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientHomeAddressType.setStatus("current")
_CLPmipClientHomeAddress_Type = InetAddress
_CLPmipClientHomeAddress_Object = MibTableColumn
cLPmipClientHomeAddress = _CLPmipClientHomeAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 5),
    _CLPmipClientHomeAddress_Type()
)
cLPmipClientHomeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientHomeAddress.setStatus("current")


class _CLPmipClientAtt_Type(Integer32):
    """Custom type cLPmipClientAtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 3),
          ("logicalNetworkInterface", 1),
          ("pointToPointInterface", 2),
          ("reserved", 0),
          ("threeGPP21xRTT", 11),
          ("threeGPP2HRPD", 10),
          ("threeGPP2UMB", 12),
          ("threeGPP2eHRPD", 9),
          ("threeGPPETRAN", 8),
          ("threeGPPGERAN", 6),
          ("threeGPPUTRAN", 7),
          ("wimax", 5),
          ("wirelessLan", 4))
    )


_CLPmipClientAtt_Type.__name__ = "Integer32"
_CLPmipClientAtt_Object = MibTableColumn
cLPmipClientAtt = _CLPmipClientAtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 6),
    _CLPmipClientAtt_Type()
)
cLPmipClientAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientAtt.setStatus("current")
_CLPmipClientLocalLinkId_Type = MacAddress
_CLPmipClientLocalLinkId_Object = MibTableColumn
cLPmipClientLocalLinkId = _CLPmipClientLocalLinkId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 7),
    _CLPmipClientLocalLinkId_Type()
)
cLPmipClientLocalLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientLocalLinkId.setStatus("current")
_CLPmipClientLmaName_Type = SnmpAdminString
_CLPmipClientLmaName_Object = MibTableColumn
cLPmipClientLmaName = _CLPmipClientLmaName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 8),
    _CLPmipClientLmaName_Type()
)
cLPmipClientLmaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientLmaName.setStatus("current")
_CLPmipClientLifeTime_Type = TimeTicks
_CLPmipClientLifeTime_Object = MibTableColumn
cLPmipClientLifeTime = _CLPmipClientLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 9),
    _CLPmipClientLifeTime_Type()
)
cLPmipClientLifeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientLifeTime.setStatus("current")
_CLPmipClientDomainName_Type = SnmpAdminString
_CLPmipClientDomainName_Object = MibTableColumn
cLPmipClientDomainName = _CLPmipClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 10),
    _CLPmipClientDomainName_Type()
)
cLPmipClientDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientDomainName.setStatus("current")
_CLPmipClientUpKey_Type = Unsigned32
_CLPmipClientUpKey_Object = MibTableColumn
cLPmipClientUpKey = _CLPmipClientUpKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 11),
    _CLPmipClientUpKey_Type()
)
cLPmipClientUpKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientUpKey.setStatus("current")
_CLPmipClientDownKey_Type = Unsigned32
_CLPmipClientDownKey_Object = MibTableColumn
cLPmipClientDownKey = _CLPmipClientDownKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 888, 0, 3, 2, 1, 12),
    _CLPmipClientDownKey_Type()
)
cLPmipClientDownKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cLPmipClientDownKey.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-PMIP-MIB",
    **{"ciscoLwappPmipMIB": ciscoLwappPmipMIB,
       "ciscoLwappPmipMIBObjects": ciscoLwappPmipMIBObjects,
       "ciscoLwappPmipGlobal": ciscoLwappPmipGlobal,
       "cLPmipDomainName": cLPmipDomainName,
       "cLPmipMAGInterface": cLPmipMAGInterface,
       "cLPmipMaxBindings": cLPmipMaxBindings,
       "cLPmipBindingLifeTime": cLPmipBindingLifeTime,
       "cLPmipBindingRefreshTime": cLPmipBindingRefreshTime,
       "cLPmipBindingInitRetxTime": cLPmipBindingInitRetxTime,
       "cLPmipBindingMaxRetxTime": cLPmipBindingMaxRetxTime,
       "cLPmipReplayProtectionTimestamp": cLPmipReplayProtectionTimestamp,
       "cLPmipBriMinDelayTime": cLPmipBriMinDelayTime,
       "cLPmipBriMaxDelayTime": cLPmipBriMaxDelayTime,
       "cLPmipBriRetries": cLPmipBriRetries,
       "cLPmipMagApnName": cLPmipMagApnName,
       "ciscoLwappPmipConfig": ciscoLwappPmipConfig,
       "cLPmipLmaTable": cLPmipLmaTable,
       "cLPmipLmaEntry": cLPmipLmaEntry,
       "cLPmipLmaName": cLPmipLmaName,
       "cLPmipLmaIPAddrType": cLPmipLmaIPAddrType,
       "cLPmipLmaIPAddr": cLPmipLmaIPAddr,
       "cLPmipLmaRowStatus": cLPmipLmaRowStatus,
       "cLPmipProfileTable": cLPmipProfileTable,
       "cLPmipProfileEntry": cLPmipProfileEntry,
       "cLPmipProfileName": cLPmipProfileName,
       "cLPmipProfileNaiTable": cLPmipProfileNaiTable,
       "cLPmipProfileNaiEntry": cLPmipProfileNaiEntry,
       "cLPmipProfileNai": cLPmipProfileNai,
       "cLPmipProfileApn": cLPmipProfileApn,
       "cLPmipProfileLmaName": cLPmipProfileLmaName,
       "cLPmipProfileNaiRowStatus": cLPmipProfileNaiRowStatus,
       "cLPmipWlanTable": cLPmipWlanTable,
       "cLPmipWlanEntry": cLPmipWlanEntry,
       "cLPmipWlanProfileName": cLPmipWlanProfileName,
       "cLPmipWlanMobilityType": cLPmipWlanMobilityType,
       "cLPmipWlanDefaultRealm": cLPmipWlanDefaultRealm,
       "ciscoLwappPmipStatistics": ciscoLwappPmipStatistics,
       "cLPmipLmaStatsTable": cLPmipLmaStatsTable,
       "cLPmipLmaStatsEntry": cLPmipLmaStatsEntry,
       "cLPmipLmaTotalBindings": cLPmipLmaTotalBindings,
       "cLPmipLmaPbuSent": cLPmipLmaPbuSent,
       "cLPmipLmaPbaReceived": cLPmipLmaPbaReceived,
       "cLPmipLmaPbriSent": cLPmipLmaPbriSent,
       "cLPmipLmaPbriReceived": cLPmipLmaPbriReceived,
       "cLPmipLmaPbraSent": cLPmipLmaPbraSent,
       "cLPmipLmaPbraReceived": cLPmipLmaPbraReceived,
       "cLPmipLmaNoOfHandoff": cLPmipLmaNoOfHandoff,
       "cLPmipLmaPbuDropped": cLPmipLmaPbuDropped,
       "cLPmipClientInfoTable": cLPmipClientInfoTable,
       "cLPmipClientInfoEntry": cLPmipClientInfoEntry,
       "cLPmipClientNai": cLPmipClientNai,
       "cLPmipClientState": cLPmipClientState,
       "cLPmipClientInterface": cLPmipClientInterface,
       "cLPmipClientHomeAddressType": cLPmipClientHomeAddressType,
       "cLPmipClientHomeAddress": cLPmipClientHomeAddress,
       "cLPmipClientAtt": cLPmipClientAtt,
       "cLPmipClientLocalLinkId": cLPmipClientLocalLinkId,
       "cLPmipClientLmaName": cLPmipClientLmaName,
       "cLPmipClientLifeTime": cLPmipClientLifeTime,
       "cLPmipClientDomainName": cLPmipClientDomainName,
       "cLPmipClientUpKey": cLPmipClientUpKey,
       "cLPmipClientDownKey": cLPmipClientDownKey}
)
