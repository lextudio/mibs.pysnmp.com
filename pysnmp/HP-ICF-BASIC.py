# SNMP MIB module (HP-ICF-BASIC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-BASIC
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:06 2024
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

(entLogicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalIndex")

(hpicfCommon,
 hpicfCommonTrapsPrefix,
 hpicfObjectModules) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpicfCommon",
    "hpicfCommonTrapsPrefix",
    "hpicfObjectModules")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(alarmEntry,
 eventEntry) = mibBuilder.importSymbols(
    "RMON-MIB",
    "alarmEntry",
    "eventEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(snmpTargetAddrEntry,) = mibBuilder.importSymbols(
    "SNMP-TARGET-MIB",
    "snmpTargetAddrEntry")

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
 StorageType,
 TAddress,
 TDomain,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

hpicfBasicMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5)
)
hpicfBasicMib.setRevisions(
        ("2017-07-03 00:00",
         "2016-09-16 00:00",
         "2015-01-31 00:00",
         "2013-06-12 14:41",
         "2013-05-29 21:00",
         "2013-02-10 13:57",
         "2012-10-11 00:00",
         "2012-07-10 13:57",
         "2012-03-27 13:00",
         "2011-08-30 13:57",
         "2010-11-11 13:57",
         "2009-11-02 13:57",
         "2009-02-23 00:00",
         "2009-02-10 15:39",
         "2009-02-03 00:00",
         "2008-12-04 00:00",
         "2008-04-04 00:00",
         "2007-09-13 00:00",
         "2007-06-07 00:00",
         "2007-05-30 09:54",
         "2005-11-17 00:00",
         "2004-04-12 00:00",
         "2003-01-09 01:08",
         "2002-10-10 04:01",
         "2000-11-14 04:01",
         "2000-11-03 05:11",
         "1997-10-21 03:00",
         "1997-03-06 03:31",
         "1996-09-10 02:21",
         "1995-07-13 00:00",
         "1995-01-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfBasicConformance_ObjectIdentity = ObjectIdentity
hpicfBasicConformance = _HpicfBasicConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1)
)
_HpicfBasicCompliances_ObjectIdentity = ObjectIdentity
hpicfBasicCompliances = _HpicfBasicCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1)
)
_HpicfBasicGroups_ObjectIdentity = ObjectIdentity
hpicfBasicGroups = _HpicfBasicGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2)
)
_HpicfBasic_ObjectIdentity = ObjectIdentity
hpicfBasic = _HpicfBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4)
)


class _HpicfReset_Type(Integer32):
    """Custom type hpicfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("agentReset", 4),
          ("noReset", 1),
          ("normalReset", 2))
    )


_HpicfReset_Type.__name__ = "Integer32"
_HpicfReset_Object = MibScalar
hpicfReset = _HpicfReset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 1),
    _HpicfReset_Type()
)
hpicfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfReset.setStatus("current")


class _HpicfSelfTest_Type(Integer32):
    """Custom type hpicfSelfTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stExecute", 2),
          ("stSuccess", 1))
    )


_HpicfSelfTest_Type.__name__ = "Integer32"
_HpicfSelfTest_Object = MibScalar
hpicfSelfTest = _HpicfSelfTest_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 2),
    _HpicfSelfTest_Type()
)
hpicfSelfTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSelfTest.setStatus("current")


class _HpicfTelnetEnable_Type(Integer32):
    """Custom type hpicfTelnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfTelnetEnable_Type.__name__ = "Integer32"
_HpicfTelnetEnable_Object = MibScalar
hpicfTelnetEnable = _HpicfTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 3),
    _HpicfTelnetEnable_Type()
)
hpicfTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTelnetEnable.setStatus("current")


class _HpicfConfigClear_Type(Integer32):
    """Custom type hpicfConfigClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configClear", 2),
          ("running", 1))
    )


_HpicfConfigClear_Type.__name__ = "Integer32"
_HpicfConfigClear_Object = MibScalar
hpicfConfigClear = _HpicfConfigClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 4),
    _HpicfConfigClear_Type()
)
hpicfConfigClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfConfigClear.setStatus("current")
_HpicfSelfTestResult_ObjectIdentity = ObjectIdentity
hpicfSelfTestResult = _HpicfSelfTestResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 5)
)


class _HpicfSelfTestResultCode_Type(Integer32):
    """Custom type hpicfSelfTestResultCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("softFailure", 2))
    )


_HpicfSelfTestResultCode_Type.__name__ = "Integer32"
_HpicfSelfTestResultCode_Object = MibScalar
hpicfSelfTestResultCode = _HpicfSelfTestResultCode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 5, 1),
    _HpicfSelfTestResultCode_Type()
)
hpicfSelfTestResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSelfTestResultCode.setStatus("current")


class _HpicfSelfTestResultText_Type(DisplayString):
    """Custom type hpicfSelfTestResultText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfSelfTestResultText_Type.__name__ = "DisplayString"
_HpicfSelfTestResultText_Object = MibScalar
hpicfSelfTestResultText = _HpicfSelfTestResultText_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 5, 2),
    _HpicfSelfTestResultText_Type()
)
hpicfSelfTestResultText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSelfTestResultText.setStatus("current")
_HpicfSelfTestResultTime_Type = TimeStamp
_HpicfSelfTestResultTime_Object = MibScalar
hpicfSelfTestResultTime = _HpicfSelfTestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 5, 3),
    _HpicfSelfTestResultTime_Type()
)
hpicfSelfTestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfSelfTestResultTime.setStatus("current")


class _HpicfWebAgentEnable_Type(Integer32):
    """Custom type hpicfWebAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfWebAgentEnable_Type.__name__ = "Integer32"
_HpicfWebAgentEnable_Object = MibScalar
hpicfWebAgentEnable = _HpicfWebAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 6),
    _HpicfWebAgentEnable_Type()
)
hpicfWebAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfWebAgentEnable.setStatus("current")
_HpicfBasicDiscovery_ObjectIdentity = ObjectIdentity
hpicfBasicDiscovery = _HpicfBasicDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7)
)
_HpicfAnnounceTable_Object = MibTable
hpicfAnnounceTable = _HpicfAnnounceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 1)
)
if mibBuilder.loadTexts:
    hpicfAnnounceTable.setStatus("deprecated")
_HpicfAnnounceEntry_Object = MibTableRow
hpicfAnnounceEntry = _HpicfAnnounceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 1, 1)
)
hpicfAnnounceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    hpicfAnnounceEntry.setStatus("deprecated")
_HpicfAnnounceAddress_Type = MacAddress
_HpicfAnnounceAddress_Object = MibTableColumn
hpicfAnnounceAddress = _HpicfAnnounceAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 1, 1, 1),
    _HpicfAnnounceAddress_Type()
)
hpicfAnnounceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAnnounceAddress.setStatus("deprecated")
_HpicfIfToEntityTable_Object = MibTable
hpicfIfToEntityTable = _HpicfIfToEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 2)
)
if mibBuilder.loadTexts:
    hpicfIfToEntityTable.setStatus("deprecated")
_HpicfIfToEntityEntry_Object = MibTableRow
hpicfIfToEntityEntry = _HpicfIfToEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 2, 1)
)
hpicfIfToEntityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfIfToEntityEntry.setStatus("deprecated")


class _HpicfIfEntLogicalIndex_Type(Integer32):
    """Custom type hpicfIfEntLogicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfIfEntLogicalIndex_Type.__name__ = "Integer32"
_HpicfIfEntLogicalIndex_Object = MibTableColumn
hpicfIfEntLogicalIndex = _HpicfIfEntLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 2, 1, 1),
    _HpicfIfEntLogicalIndex_Type()
)
hpicfIfEntLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIfEntLogicalIndex.setStatus("deprecated")
_HpicfAnnounceDiscoveryTable_Object = MibTable
hpicfAnnounceDiscoveryTable = _HpicfAnnounceDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 3)
)
if mibBuilder.loadTexts:
    hpicfAnnounceDiscoveryTable.setStatus("current")
_HpicfAnnounceDiscoveryEntry_Object = MibTableRow
hpicfAnnounceDiscoveryEntry = _HpicfAnnounceDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 3, 1)
)
hpicfAnnounceDiscoveryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfAnnounceDiscoveryEntry.setStatus("current")
_HpicfAnnounceDiscoveryAddress_Type = MacAddress
_HpicfAnnounceDiscoveryAddress_Object = MibTableColumn
hpicfAnnounceDiscoveryAddress = _HpicfAnnounceDiscoveryAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 7, 3, 1, 1),
    _HpicfAnnounceDiscoveryAddress_Type()
)
hpicfAnnounceDiscoveryAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfAnnounceDiscoveryAddress.setStatus("current")
_HpicfBasicIpConfig_ObjectIdentity = ObjectIdentity
hpicfBasicIpConfig = _HpicfBasicIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8)
)
_HpicfIpConfigTable_Object = MibTable
hpicfIpConfigTable = _HpicfIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1)
)
if mibBuilder.loadTexts:
    hpicfIpConfigTable.setStatus("deprecated")
_HpicfIpConfigEntry_Object = MibTableRow
hpicfIpConfigEntry = _HpicfIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1)
)
hpicfIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpConfigEntry.setStatus("deprecated")
_HpicfIpConfigAddress_Type = IpAddress
_HpicfIpConfigAddress_Object = MibTableColumn
hpicfIpConfigAddress = _HpicfIpConfigAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 1),
    _HpicfIpConfigAddress_Type()
)
hpicfIpConfigAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigAddress.setStatus("deprecated")
_HpicfIpConfigAddrMask_Type = IpAddress
_HpicfIpConfigAddrMask_Object = MibTableColumn
hpicfIpConfigAddrMask = _HpicfIpConfigAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 2),
    _HpicfIpConfigAddrMask_Type()
)
hpicfIpConfigAddrMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigAddrMask.setStatus("deprecated")
_HpicfIpConfigDefaultRouter_Type = IpAddress
_HpicfIpConfigDefaultRouter_Object = MibTableColumn
hpicfIpConfigDefaultRouter = _HpicfIpConfigDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 3),
    _HpicfIpConfigDefaultRouter_Type()
)
hpicfIpConfigDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigDefaultRouter.setStatus("deprecated")
_HpicfIpConfigPingRouter_Type = TruthValue
_HpicfIpConfigPingRouter_Object = MibTableColumn
hpicfIpConfigPingRouter = _HpicfIpConfigPingRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 4),
    _HpicfIpConfigPingRouter_Type()
)
hpicfIpConfigPingRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigPingRouter.setStatus("deprecated")


class _HpicfIpConfigMtu_Type(Integer32):
    """Custom type hpicfIpConfigMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(68, 65535),
    )


_HpicfIpConfigMtu_Type.__name__ = "Integer32"
_HpicfIpConfigMtu_Object = MibTableColumn
hpicfIpConfigMtu = _HpicfIpConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 5),
    _HpicfIpConfigMtu_Type()
)
hpicfIpConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigMtu.setStatus("deprecated")


class _HpicfIpConfigAdminStatus_Type(Integer32):
    """Custom type hpicfIpConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("learn", 3),
          ("useConfigured", 2))
    )


_HpicfIpConfigAdminStatus_Type.__name__ = "Integer32"
_HpicfIpConfigAdminStatus_Object = MibTableColumn
hpicfIpConfigAdminStatus = _HpicfIpConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 6),
    _HpicfIpConfigAdminStatus_Type()
)
hpicfIpConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigAdminStatus.setStatus("deprecated")


class _HpicfIpConfigProxyArp_Type(Integer32):
    """Custom type hpicfIpConfigProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfIpConfigProxyArp_Type.__name__ = "Integer32"
_HpicfIpConfigProxyArp_Object = MibTableColumn
hpicfIpConfigProxyArp = _HpicfIpConfigProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 7),
    _HpicfIpConfigProxyArp_Type()
)
hpicfIpConfigProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigProxyArp.setStatus("deprecated")


class _HpicfIpConfigLocalProxyArp_Type(Integer32):
    """Custom type hpicfIpConfigLocalProxyArp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfIpConfigLocalProxyArp_Type.__name__ = "Integer32"
_HpicfIpConfigLocalProxyArp_Object = MibTableColumn
hpicfIpConfigLocalProxyArp = _HpicfIpConfigLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 1, 1, 8),
    _HpicfIpConfigLocalProxyArp_Type()
)
hpicfIpConfigLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpConfigLocalProxyArp.setStatus("deprecated")
_HpicfIpAddrTable_Object = MibTable
hpicfIpAddrTable = _HpicfIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 2)
)
if mibBuilder.loadTexts:
    hpicfIpAddrTable.setStatus("deprecated")
_HpicfIpAddrEntry_Object = MibTableRow
hpicfIpAddrEntry = _HpicfIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 2, 1)
)
hpicfIpAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-BASIC", "hpicfIpAddrAddr"),
)
if mibBuilder.loadTexts:
    hpicfIpAddrEntry.setStatus("deprecated")
_HpicfIpAddrAddr_Type = IpAddress
_HpicfIpAddrAddr_Object = MibTableColumn
hpicfIpAddrAddr = _HpicfIpAddrAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 2, 1, 1),
    _HpicfIpAddrAddr_Type()
)
hpicfIpAddrAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpAddrAddr.setStatus("deprecated")
_HpicfIpAddrMask_Type = IpAddress
_HpicfIpAddrMask_Object = MibTableColumn
hpicfIpAddrMask = _HpicfIpAddrMask_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 2, 1, 2),
    _HpicfIpAddrMask_Type()
)
hpicfIpAddrMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddrMask.setStatus("deprecated")
_HpicfIpAddrStatus_Type = RowStatus
_HpicfIpAddrStatus_Object = MibTableColumn
hpicfIpAddrStatus = _HpicfIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 2, 1, 3),
    _HpicfIpAddrStatus_Type()
)
hpicfIpAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfIpAddrStatus.setStatus("deprecated")
_HpicfIpGlobalDefaultRouter_Type = IpAddress
_HpicfIpGlobalDefaultRouter_Object = MibScalar
hpicfIpGlobalDefaultRouter = _HpicfIpGlobalDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 3),
    _HpicfIpGlobalDefaultRouter_Type()
)
hpicfIpGlobalDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpGlobalDefaultRouter.setStatus("current")
_HpicfIpGlobalPingRouter_Type = TruthValue
_HpicfIpGlobalPingRouter_Object = MibScalar
hpicfIpGlobalPingRouter = _HpicfIpGlobalPingRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 4),
    _HpicfIpGlobalPingRouter_Type()
)
hpicfIpGlobalPingRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpGlobalPingRouter.setStatus("current")
_HpicfIpZeroBroadcastEnable_Type = TruthValue
_HpicfIpZeroBroadcastEnable_Object = MibScalar
hpicfIpZeroBroadcastEnable = _HpicfIpZeroBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 8, 5),
    _HpicfIpZeroBroadcastEnable_Type()
)
hpicfIpZeroBroadcastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpZeroBroadcastEnable.setStatus("current")
_HpicfBasicIpxConfig_ObjectIdentity = ObjectIdentity
hpicfBasicIpxConfig = _HpicfBasicIpxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9)
)
_HpicfIpxConfigTable_Object = MibTable
hpicfIpxConfigTable = _HpicfIpxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1)
)
if mibBuilder.loadTexts:
    hpicfIpxConfigTable.setStatus("current")
_HpicfIpxConfigEntry_Object = MibTableRow
hpicfIpxConfigEntry = _HpicfIpxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1, 1)
)
hpicfIpxConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfIpxConfigEntry.setStatus("current")
_HpicfIpxConfigNodeAddress_Type = MacAddress
_HpicfIpxConfigNodeAddress_Object = MibTableColumn
hpicfIpxConfigNodeAddress = _HpicfIpxConfigNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1, 1, 1),
    _HpicfIpxConfigNodeAddress_Type()
)
hpicfIpxConfigNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpxConfigNodeAddress.setStatus("current")
_HpicfIpxConfigDefaultRouter_Type = MacAddress
_HpicfIpxConfigDefaultRouter_Object = MibTableColumn
hpicfIpxConfigDefaultRouter = _HpicfIpxConfigDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1, 1, 2),
    _HpicfIpxConfigDefaultRouter_Type()
)
hpicfIpxConfigDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpxConfigDefaultRouter.setStatus("current")


class _HpicfIpxConfigRouterEncaps_Type(Integer32):
    """Custom type hpicfIpxConfigRouterEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee8022", 2),
          ("ieee8023Raw", 4),
          ("learn", 6),
          ("noGateway", 5),
          ("snap", 3))
    )


_HpicfIpxConfigRouterEncaps_Type.__name__ = "Integer32"
_HpicfIpxConfigRouterEncaps_Object = MibTableColumn
hpicfIpxConfigRouterEncaps = _HpicfIpxConfigRouterEncaps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1, 1, 3),
    _HpicfIpxConfigRouterEncaps_Type()
)
hpicfIpxConfigRouterEncaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpxConfigRouterEncaps.setStatus("current")


class _HpicfIpxConfigAdminStatus_Type(Integer32):
    """Custom type hpicfIpxConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpicfIpxConfigAdminStatus_Type.__name__ = "Integer32"
_HpicfIpxConfigAdminStatus_Object = MibTableColumn
hpicfIpxConfigAdminStatus = _HpicfIpxConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 1, 1, 4),
    _HpicfIpxConfigAdminStatus_Type()
)
hpicfIpxConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIpxConfigAdminStatus.setStatus("current")
_HpicfIpxNetTable_Object = MibTable
hpicfIpxNetTable = _HpicfIpxNetTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 2)
)
if mibBuilder.loadTexts:
    hpicfIpxNetTable.setStatus("current")
_HpicfIpxNetEntry_Object = MibTableRow
hpicfIpxNetEntry = _HpicfIpxNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 2, 1)
)
hpicfIpxNetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-BASIC", "hpicfIpxNetEncaps"),
)
if mibBuilder.loadTexts:
    hpicfIpxNetEntry.setStatus("current")


class _HpicfIpxNetEncaps_Type(Integer32):
    """Custom type hpicfIpxNetEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ethernetII", 1),
          ("ieee8022", 2),
          ("ieee8023Raw", 4),
          ("snap", 3))
    )


_HpicfIpxNetEncaps_Type.__name__ = "Integer32"
_HpicfIpxNetEncaps_Object = MibTableColumn
hpicfIpxNetEncaps = _HpicfIpxNetEncaps_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 2, 1, 1),
    _HpicfIpxNetEncaps_Type()
)
hpicfIpxNetEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfIpxNetEncaps.setStatus("current")


class _HpicfIpxNetNumber_Type(OctetString):
    """Custom type hpicfIpxNetNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpicfIpxNetNumber_Type.__name__ = "OctetString"
_HpicfIpxNetNumber_Object = MibTableColumn
hpicfIpxNetNumber = _HpicfIpxNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 9, 2, 1, 2),
    _HpicfIpxNetNumber_Type()
)
hpicfIpxNetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfIpxNetNumber.setStatus("current")
_HpicfBasicTraps_ObjectIdentity = ObjectIdentity
hpicfBasicTraps = _HpicfBasicTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10)
)
_HpicfFixedTrapTable_Object = MibTable
hpicfFixedTrapTable = _HpicfFixedTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 1)
)
if mibBuilder.loadTexts:
    hpicfFixedTrapTable.setStatus("current")
_HpicfFixedTrapEntry_Object = MibTableRow
hpicfFixedTrapEntry = _HpicfFixedTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 1, 1)
)
hpicfFixedTrapEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfFixedTrapID"),
)
if mibBuilder.loadTexts:
    hpicfFixedTrapEntry.setStatus("current")
_HpicfFixedTrapID_Type = ObjectIdentifier
_HpicfFixedTrapID_Object = MibTableColumn
hpicfFixedTrapID = _HpicfFixedTrapID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 1, 1, 1),
    _HpicfFixedTrapID_Type()
)
hpicfFixedTrapID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfFixedTrapID.setStatus("current")


class _HpicfFixedTrapEventIndex_Type(Integer32):
    """Custom type hpicfFixedTrapEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpicfFixedTrapEventIndex_Type.__name__ = "Integer32"
_HpicfFixedTrapEventIndex_Object = MibTableColumn
hpicfFixedTrapEventIndex = _HpicfFixedTrapEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 1, 1, 2),
    _HpicfFixedTrapEventIndex_Type()
)
hpicfFixedTrapEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfFixedTrapEventIndex.setStatus("current")
_HpicfTrapDestTable_Object = MibTable
hpicfTrapDestTable = _HpicfTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2)
)
if mibBuilder.loadTexts:
    hpicfTrapDestTable.setStatus("deprecated")
_HpicfTrapDestEntry_Object = MibTableRow
hpicfTrapDestEntry = _HpicfTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1)
)
hpicfTrapDestEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfTrapDestIndex"),
)
if mibBuilder.loadTexts:
    hpicfTrapDestEntry.setStatus("current")


class _HpicfTrapDestIndex_Type(Integer32):
    """Custom type hpicfTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfTrapDestIndex_Type.__name__ = "Integer32"
_HpicfTrapDestIndex_Object = MibTableColumn
hpicfTrapDestIndex = _HpicfTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 1),
    _HpicfTrapDestIndex_Type()
)
hpicfTrapDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTrapDestIndex.setStatus("deprecated")


class _HpicfTrapDestVersion_Type(Integer32):
    """Custom type hpicfTrapDestVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2))
    )


_HpicfTrapDestVersion_Type.__name__ = "Integer32"
_HpicfTrapDestVersion_Object = MibTableColumn
hpicfTrapDestVersion = _HpicfTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 2),
    _HpicfTrapDestVersion_Type()
)
hpicfTrapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestVersion.setStatus("deprecated")


class _HpicfTrapDestCommunity_Type(OctetString):
    """Custom type hpicfTrapDestCommunity based on OctetString"""
    defaultHexValue = "7075626C6963"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfTrapDestCommunity_Type.__name__ = "OctetString"
_HpicfTrapDestCommunity_Object = MibTableColumn
hpicfTrapDestCommunity = _HpicfTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 3),
    _HpicfTrapDestCommunity_Type()
)
hpicfTrapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestCommunity.setStatus("deprecated")
_HpicfTrapDestTDomain_Type = TDomain
_HpicfTrapDestTDomain_Object = MibTableColumn
hpicfTrapDestTDomain = _HpicfTrapDestTDomain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 4),
    _HpicfTrapDestTDomain_Type()
)
hpicfTrapDestTDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestTDomain.setStatus("deprecated")
_HpicfTrapDestTAddress_Type = TAddress
_HpicfTrapDestTAddress_Object = MibTableColumn
hpicfTrapDestTAddress = _HpicfTrapDestTAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 5),
    _HpicfTrapDestTAddress_Type()
)
hpicfTrapDestTAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestTAddress.setStatus("deprecated")


class _HpicfTrapDestFilter_Type(Integer32):
    """Custom type hpicfTrapDestFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpicfTrapDestFilter_Type.__name__ = "Integer32"
_HpicfTrapDestFilter_Object = MibTableColumn
hpicfTrapDestFilter = _HpicfTrapDestFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 6),
    _HpicfTrapDestFilter_Type()
)
hpicfTrapDestFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestFilter.setStatus("deprecated")
_HpicfTrapDestStatus_Type = RowStatus
_HpicfTrapDestStatus_Object = MibTableColumn
hpicfTrapDestStatus = _HpicfTrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 7),
    _HpicfTrapDestStatus_Type()
)
hpicfTrapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestStatus.setStatus("deprecated")


class _HpicfTrapDestNotifyType_Type(Integer32):
    """Custom type hpicfTrapDestNotifyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inform", 2),
          ("trap", 1))
    )


_HpicfTrapDestNotifyType_Type.__name__ = "Integer32"
_HpicfTrapDestNotifyType_Object = MibTableColumn
hpicfTrapDestNotifyType = _HpicfTrapDestNotifyType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 8),
    _HpicfTrapDestNotifyType_Type()
)
hpicfTrapDestNotifyType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestNotifyType.setStatus("deprecated")


class _HpicfTrapDestRetries_Type(Integer32):
    """Custom type hpicfTrapDestRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfTrapDestRetries_Type.__name__ = "Integer32"
_HpicfTrapDestRetries_Object = MibTableColumn
hpicfTrapDestRetries = _HpicfTrapDestRetries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 9),
    _HpicfTrapDestRetries_Type()
)
hpicfTrapDestRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestRetries.setStatus("deprecated")


class _HpicfTrapDestTimeout_Type(TimeInterval):
    """Custom type hpicfTrapDestTimeout based on TimeInterval"""
    defaultValue = 1500


_HpicfTrapDestTimeout_Object = MibTableColumn
hpicfTrapDestTimeout = _HpicfTrapDestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 10, 2, 1, 10),
    _HpicfTrapDestTimeout_Type()
)
hpicfTrapDestTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTrapDestTimeout.setStatus("deprecated")
_HpicfBasicRmon_ObjectIdentity = ObjectIdentity
hpicfBasicRmon = _HpicfBasicRmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11)
)
_HpicfBasicAlarm_ObjectIdentity = ObjectIdentity
hpicfBasicAlarm = _HpicfBasicAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 3)
)
_HpicfBasicAlarmNVCapacity_Type = Integer32
_HpicfBasicAlarmNVCapacity_Object = MibScalar
hpicfBasicAlarmNVCapacity = _HpicfBasicAlarmNVCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 3, 1),
    _HpicfBasicAlarmNVCapacity_Type()
)
hpicfBasicAlarmNVCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBasicAlarmNVCapacity.setStatus("current")
_HpicfBasicAlarmTable_Object = MibTable
hpicfBasicAlarmTable = _HpicfBasicAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 3, 2)
)
if mibBuilder.loadTexts:
    hpicfBasicAlarmTable.setStatus("current")
_HpicfBasicAlarmEntry_Object = MibTableRow
hpicfBasicAlarmEntry = _HpicfBasicAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBasicAlarmEntry.setStatus("current")


class _HpicfBasicAlarmStorageType_Type(StorageType):
    """Custom type hpicfBasicAlarmStorageType based on StorageType"""


_HpicfBasicAlarmStorageType_Object = MibTableColumn
hpicfBasicAlarmStorageType = _HpicfBasicAlarmStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 3, 2, 1, 1),
    _HpicfBasicAlarmStorageType_Type()
)
hpicfBasicAlarmStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicAlarmStorageType.setStatus("current")
_HpicfBasicEvent_ObjectIdentity = ObjectIdentity
hpicfBasicEvent = _HpicfBasicEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 9)
)
_HpicfBasicEventNVCapacity_Type = Integer32
_HpicfBasicEventNVCapacity_Object = MibScalar
hpicfBasicEventNVCapacity = _HpicfBasicEventNVCapacity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 9, 1),
    _HpicfBasicEventNVCapacity_Type()
)
hpicfBasicEventNVCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBasicEventNVCapacity.setStatus("current")
_HpicfBasicEventTable_Object = MibTable
hpicfBasicEventTable = _HpicfBasicEventTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 9, 2)
)
if mibBuilder.loadTexts:
    hpicfBasicEventTable.setStatus("current")
_HpicfBasicEventEntry_Object = MibTableRow
hpicfBasicEventEntry = _HpicfBasicEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 9, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfBasicEventEntry.setStatus("current")


class _HpicfBasicEventStorageType_Type(StorageType):
    """Custom type hpicfBasicEventStorageType based on StorageType"""


_HpicfBasicEventStorageType_Object = MibTableColumn
hpicfBasicEventStorageType = _HpicfBasicEventStorageType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 11, 9, 2, 1, 1),
    _HpicfBasicEventStorageType_Type()
)
hpicfBasicEventStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicEventStorageType.setStatus("current")
_HpicfBasicSnmpTargetAddrLogFilter_ObjectIdentity = ObjectIdentity
hpicfBasicSnmpTargetAddrLogFilter = _HpicfBasicSnmpTargetAddrLogFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 12)
)
_HpicfSnmpTargetAddrLogFilterTable_Object = MibTable
hpicfSnmpTargetAddrLogFilterTable = _HpicfSnmpTargetAddrLogFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 12, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrLogFilterTable.setStatus("current")
_HpicfSnmpTargetAddrLogFilterEntry_Object = MibTableRow
hpicfSnmpTargetAddrLogFilterEntry = _HpicfSnmpTargetAddrLogFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 12, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrLogFilterEntry.setStatus("current")


class _HpicfSnmpTargetAddrLogFilter_Type(Integer32):
    """Custom type hpicfSnmpTargetAddrLogFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_HpicfSnmpTargetAddrLogFilter_Type.__name__ = "Integer32"
_HpicfSnmpTargetAddrLogFilter_Object = MibTableColumn
hpicfSnmpTargetAddrLogFilter = _HpicfSnmpTargetAddrLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 12, 1, 1, 1),
    _HpicfSnmpTargetAddrLogFilter_Type()
)
hpicfSnmpTargetAddrLogFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrLogFilter.setStatus("current")


class _HpicfBannerStatus_Type(Integer32):
    """Custom type hpicfBannerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfBannerStatus_Type.__name__ = "Integer32"
_HpicfBannerStatus_Object = MibScalar
hpicfBannerStatus = _HpicfBannerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 13),
    _HpicfBannerStatus_Type()
)
hpicfBannerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBannerStatus.setStatus("current")
_HpicfBanner_ObjectIdentity = ObjectIdentity
hpicfBanner = _HpicfBanner_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14)
)


class _HpicfBannerMOTD_Type(OctetString):
    """Custom type hpicfBannerMOTD based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1300),
    )


_HpicfBannerMOTD_Type.__name__ = "OctetString"
_HpicfBannerMOTD_Object = MibScalar
hpicfBannerMOTD = _HpicfBannerMOTD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14, 1),
    _HpicfBannerMOTD_Type()
)
hpicfBannerMOTD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBannerMOTD.setStatus("current")


class _HpicfExecBannerStatus_Type(Integer32):
    """Custom type hpicfExecBannerStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfExecBannerStatus_Type.__name__ = "Integer32"
_HpicfExecBannerStatus_Object = MibScalar
hpicfExecBannerStatus = _HpicfExecBannerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14, 2),
    _HpicfExecBannerStatus_Type()
)
hpicfExecBannerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfExecBannerStatus.setStatus("current")


class _HpicfBannerExec_Type(OctetString):
    """Custom type hpicfBannerExec based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_HpicfBannerExec_Type.__name__ = "OctetString"
_HpicfBannerExec_Object = MibScalar
hpicfBannerExec = _HpicfBannerExec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14, 3),
    _HpicfBannerExec_Type()
)
hpicfBannerExec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBannerExec.setStatus("deprecated")


class _HpicfLastLoginBannerStatus_Type(Integer32):
    """Custom type hpicfLastLoginBannerStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfLastLoginBannerStatus_Type.__name__ = "Integer32"
_HpicfLastLoginBannerStatus_Object = MibScalar
hpicfLastLoginBannerStatus = _HpicfLastLoginBannerStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14, 4),
    _HpicfLastLoginBannerStatus_Type()
)
hpicfLastLoginBannerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfLastLoginBannerStatus.setStatus("current")


class _HpicfBannerExec1_Type(OctetString):
    """Custom type hpicfBannerExec1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_HpicfBannerExec1_Type.__name__ = "OctetString"
_HpicfBannerExec1_Object = MibScalar
hpicfBannerExec1 = _HpicfBannerExec1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 14, 5),
    _HpicfBannerExec1_Type()
)
hpicfBannerExec1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBannerExec1.setStatus("deprecated")
_HpicfBasicDNSConfig_ObjectIdentity = ObjectIdentity
hpicfBasicDNSConfig = _HpicfBasicDNSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15)
)


class _HpicfDNSDefaultDomainSuffix_Type(DisplayString):
    """Custom type hpicfDNSDefaultDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDNSDefaultDomainSuffix_Type.__name__ = "DisplayString"
_HpicfDNSDefaultDomainSuffix_Object = MibScalar
hpicfDNSDefaultDomainSuffix = _HpicfDNSDefaultDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 1),
    _HpicfDNSDefaultDomainSuffix_Type()
)
hpicfDNSDefaultDomainSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDNSDefaultDomainSuffix.setStatus("deprecated")
_HpicfDNSNameServerTable_Object = MibTable
hpicfDNSNameServerTable = _HpicfDNSNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 2)
)
if mibBuilder.loadTexts:
    hpicfDNSNameServerTable.setStatus("deprecated")
_HpicfDNSNameServerEntry_Object = MibTableRow
hpicfDNSNameServerEntry = _HpicfDNSNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 2, 1)
)
hpicfDNSNameServerEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfDNSNameServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfDNSNameServerEntry.setStatus("deprecated")
_HpicfDNSNameServerAddress_Type = IpAddress
_HpicfDNSNameServerAddress_Object = MibTableColumn
hpicfDNSNameServerAddress = _HpicfDNSNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 2, 1, 1),
    _HpicfDNSNameServerAddress_Type()
)
hpicfDNSNameServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDNSNameServerAddress.setStatus("deprecated")
_HpicfDNSNameServerEntryStatus_Type = RowStatus
_HpicfDNSNameServerEntryStatus_Object = MibTableColumn
hpicfDNSNameServerEntryStatus = _HpicfDNSNameServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 2, 1, 2),
    _HpicfDNSNameServerEntryStatus_Type()
)
hpicfDNSNameServerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDNSNameServerEntryStatus.setStatus("deprecated")
_HpicfInetDNSNameServerTable_Object = MibTable
hpicfInetDNSNameServerTable = _HpicfInetDNSNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3)
)
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerTable.setStatus("current")
_HpicfInetDNSNameServerEntry_Object = MibTableRow
hpicfInetDNSNameServerEntry = _HpicfInetDNSNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1)
)
hpicfInetDNSNameServerEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfInetDNSNameServerAddrIndex"),
    (0, "HP-ICF-BASIC", "hpicfInetDNSNameServerAddrType"),
    (0, "HP-ICF-BASIC", "hpicfInetDNSNameServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerEntry.setStatus("current")


class _HpicfInetDNSNameServerAddrIndex_Type(Integer32):
    """Custom type hpicfInetDNSNameServerAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfInetDNSNameServerAddrIndex_Type.__name__ = "Integer32"
_HpicfInetDNSNameServerAddrIndex_Object = MibTableColumn
hpicfInetDNSNameServerAddrIndex = _HpicfInetDNSNameServerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1, 1),
    _HpicfInetDNSNameServerAddrIndex_Type()
)
hpicfInetDNSNameServerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerAddrIndex.setStatus("current")
_HpicfInetDNSNameServerAddrType_Type = InetAddressType
_HpicfInetDNSNameServerAddrType_Object = MibTableColumn
hpicfInetDNSNameServerAddrType = _HpicfInetDNSNameServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1, 2),
    _HpicfInetDNSNameServerAddrType_Type()
)
hpicfInetDNSNameServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerAddrType.setStatus("current")
_HpicfInetDNSNameServerAddress_Type = InetAddress
_HpicfInetDNSNameServerAddress_Object = MibTableColumn
hpicfInetDNSNameServerAddress = _HpicfInetDNSNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1, 3),
    _HpicfInetDNSNameServerAddress_Type()
)
hpicfInetDNSNameServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerAddress.setStatus("current")
_HpicfInetDNSNameServerEntryStatus_Type = RowStatus
_HpicfInetDNSNameServerEntryStatus_Object = MibTableColumn
hpicfInetDNSNameServerEntryStatus = _HpicfInetDNSNameServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1, 4),
    _HpicfInetDNSNameServerEntryStatus_Type()
)
hpicfInetDNSNameServerEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerEntryStatus.setStatus("current")


class _HpicfInetDNSNameServerEntryIsOobm_Type(TruthValue):
    """Custom type hpicfInetDNSNameServerEntryIsOobm based on TruthValue"""


_HpicfInetDNSNameServerEntryIsOobm_Object = MibTableColumn
hpicfInetDNSNameServerEntryIsOobm = _HpicfInetDNSNameServerEntryIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 3, 1, 5),
    _HpicfInetDNSNameServerEntryIsOobm_Type()
)
hpicfInetDNSNameServerEntryIsOobm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerEntryIsOobm.setStatus("current")


class _HpicfDNSDefaultDomainSuffixIsOobm_Type(DisplayString):
    """Custom type hpicfDNSDefaultDomainSuffixIsOobm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDNSDefaultDomainSuffixIsOobm_Type.__name__ = "DisplayString"
_HpicfDNSDefaultDomainSuffixIsOobm_Object = MibScalar
hpicfDNSDefaultDomainSuffixIsOobm = _HpicfDNSDefaultDomainSuffixIsOobm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 4),
    _HpicfDNSDefaultDomainSuffixIsOobm_Type()
)
hpicfDNSDefaultDomainSuffixIsOobm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDNSDefaultDomainSuffixIsOobm.setStatus("current")


class _HpicfDNSConfigMode_Type(Integer32):
    """Custom type hpicfDNSConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 1),
          ("disabled", 3),
          ("manual", 2))
    )


_HpicfDNSConfigMode_Type.__name__ = "Integer32"
_HpicfDNSConfigMode_Object = MibScalar
hpicfDNSConfigMode = _HpicfDNSConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 5),
    _HpicfDNSConfigMode_Type()
)
hpicfDNSConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDNSConfigMode.setStatus("current")
_HpicfCurDNSConfig_ObjectIdentity = ObjectIdentity
hpicfCurDNSConfig = _HpicfCurDNSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6)
)


class _HpicfCurDNSDefaultDomainSuffix_Type(DisplayString):
    """Custom type hpicfCurDNSDefaultDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfCurDNSDefaultDomainSuffix_Type.__name__ = "DisplayString"
_HpicfCurDNSDefaultDomainSuffix_Object = MibScalar
hpicfCurDNSDefaultDomainSuffix = _HpicfCurDNSDefaultDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 1),
    _HpicfCurDNSDefaultDomainSuffix_Type()
)
hpicfCurDNSDefaultDomainSuffix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfCurDNSDefaultDomainSuffix.setStatus("deprecated")
_HpicfCurDNSNameServerTable_Object = MibTable
hpicfCurDNSNameServerTable = _HpicfCurDNSNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2)
)
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerTable.setStatus("current")
_HpicfCurDNSNameServerEntry_Object = MibTableRow
hpicfCurDNSNameServerEntry = _HpicfCurDNSNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2, 1)
)
hpicfCurDNSNameServerEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfCurDNSNameServerAddrIndex"),
    (0, "HP-ICF-BASIC", "hpicfCurDNSNameServerAddrType"),
    (0, "HP-ICF-BASIC", "hpicfCurDNSNameServerAddress"),
)
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerEntry.setStatus("current")


class _HpicfCurDNSNameServerAddrIndex_Type(Integer32):
    """Custom type hpicfCurDNSNameServerAddrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfCurDNSNameServerAddrIndex_Type.__name__ = "Integer32"
_HpicfCurDNSNameServerAddrIndex_Object = MibTableColumn
hpicfCurDNSNameServerAddrIndex = _HpicfCurDNSNameServerAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2, 1, 1),
    _HpicfCurDNSNameServerAddrIndex_Type()
)
hpicfCurDNSNameServerAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerAddrIndex.setStatus("current")
_HpicfCurDNSNameServerAddrType_Type = InetAddressType
_HpicfCurDNSNameServerAddrType_Object = MibTableColumn
hpicfCurDNSNameServerAddrType = _HpicfCurDNSNameServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2, 1, 2),
    _HpicfCurDNSNameServerAddrType_Type()
)
hpicfCurDNSNameServerAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerAddrType.setStatus("current")
_HpicfCurDNSNameServerAddress_Type = InetAddress
_HpicfCurDNSNameServerAddress_Object = MibTableColumn
hpicfCurDNSNameServerAddress = _HpicfCurDNSNameServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2, 1, 3),
    _HpicfCurDNSNameServerAddress_Type()
)
hpicfCurDNSNameServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerAddress.setStatus("current")
_HpicfCurDNSNameServerEntryStatus_Type = RowStatus
_HpicfCurDNSNameServerEntryStatus_Object = MibTableColumn
hpicfCurDNSNameServerEntryStatus = _HpicfCurDNSNameServerEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 6, 2, 1, 4),
    _HpicfCurDNSNameServerEntryStatus_Type()
)
hpicfCurDNSNameServerEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfCurDNSNameServerEntryStatus.setStatus("current")
_HpicfDNSDomainSuffixTable_Object = MibTable
hpicfDNSDomainSuffixTable = _HpicfDNSDomainSuffixTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 7)
)
if mibBuilder.loadTexts:
    hpicfDNSDomainSuffixTable.setStatus("current")
_HpicfDNSDomainSuffixEntry_Object = MibTableRow
hpicfDNSDomainSuffixEntry = _HpicfDNSDomainSuffixEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 7, 1)
)
hpicfDNSDomainSuffixEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfDNSDomainSuffixIndex"),
)
if mibBuilder.loadTexts:
    hpicfDNSDomainSuffixEntry.setStatus("current")


class _HpicfDNSDomainSuffixIndex_Type(Integer32):
    """Custom type hpicfDNSDomainSuffixIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpicfDNSDomainSuffixIndex_Type.__name__ = "Integer32"
_HpicfDNSDomainSuffixIndex_Object = MibTableColumn
hpicfDNSDomainSuffixIndex = _HpicfDNSDomainSuffixIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 7, 1, 1),
    _HpicfDNSDomainSuffixIndex_Type()
)
hpicfDNSDomainSuffixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDNSDomainSuffixIndex.setStatus("current")


class _HpicfDNSDomainSuffix_Type(DisplayString):
    """Custom type hpicfDNSDomainSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfDNSDomainSuffix_Type.__name__ = "DisplayString"
_HpicfDNSDomainSuffix_Object = MibTableColumn
hpicfDNSDomainSuffix = _HpicfDNSDomainSuffix_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 15, 7, 1, 2),
    _HpicfDNSDomainSuffix_Type()
)
hpicfDNSDomainSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDNSDomainSuffix.setStatus("current")


class _HpicfResetDefault_Type(Integer32):
    """Custom type hpicfResetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_HpicfResetDefault_Type.__name__ = "Integer32"
_HpicfResetDefault_Object = MibScalar
hpicfResetDefault = _HpicfResetDefault_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 16),
    _HpicfResetDefault_Type()
)
hpicfResetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfResetDefault.setStatus("current")


class _HpicfTelnet6Enable_Type(Integer32):
    """Custom type hpicfTelnet6Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfTelnet6Enable_Type.__name__ = "Integer32"
_HpicfTelnet6Enable_Object = MibScalar
hpicfTelnet6Enable = _HpicfTelnet6Enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 17),
    _HpicfTelnet6Enable_Type()
)
hpicfTelnet6Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTelnet6Enable.setStatus("deprecated")
_HpicfBasicSNMPConfig_ObjectIdentity = ObjectIdentity
hpicfBasicSNMPConfig = _HpicfBasicSNMPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 18)
)


class _HpSwitchSnmpViewConfig_Type(Integer32):
    """Custom type hpSwitchSnmpViewConfig based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpSwitchSnmpViewConfig_Type.__name__ = "Integer32"
_HpSwitchSnmpViewConfig_Object = MibScalar
hpSwitchSnmpViewConfig = _HpSwitchSnmpViewConfig_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 18, 1),
    _HpSwitchSnmpViewConfig_Type()
)
hpSwitchSnmpViewConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchSnmpViewConfig.setStatus("current")


class _HpicfSnmpV2Enable_Type(Integer32):
    """Custom type hpicfSnmpV2Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfSnmpV2Enable_Type.__name__ = "Integer32"
_HpicfSnmpV2Enable_Object = MibScalar
hpicfSnmpV2Enable = _HpicfSnmpV2Enable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 18, 2),
    _HpicfSnmpV2Enable_Type()
)
hpicfSnmpV2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSnmpV2Enable.setStatus("current")


class _HpicfSwitchSnmpAllowUnsecuredAccessToMACsec_Type(Integer32):
    """Custom type hpicfSwitchSnmpAllowUnsecuredAccessToMACsec based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfSwitchSnmpAllowUnsecuredAccessToMACsec_Type.__name__ = "Integer32"
_HpicfSwitchSnmpAllowUnsecuredAccessToMACsec_Object = MibScalar
hpicfSwitchSnmpAllowUnsecuredAccessToMACsec = _HpicfSwitchSnmpAllowUnsecuredAccessToMACsec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 18, 3),
    _HpicfSwitchSnmpAllowUnsecuredAccessToMACsec_Type()
)
hpicfSwitchSnmpAllowUnsecuredAccessToMACsec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSwitchSnmpAllowUnsecuredAccessToMACsec.setStatus("current")


class _HpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy_Type(Integer32):
    """Custom type hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy_Type.__name__ = "Integer32"
_HpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy_Object = MibScalar
hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy = _HpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 18, 4),
    _HpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy_Type()
)
hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy.setStatus("current")
_HpicfBasicConfig_ObjectIdentity = ObjectIdentity
hpicfBasicConfig = _HpicfBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 19)
)


class _HpicfDisplayLogNumbers_Type(TruthValue):
    """Custom type hpicfDisplayLogNumbers based on TruthValue"""


_HpicfDisplayLogNumbers_Object = MibScalar
hpicfDisplayLogNumbers = _HpicfDisplayLogNumbers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 19, 1),
    _HpicfDisplayLogNumbers_Type()
)
hpicfDisplayLogNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDisplayLogNumbers.setStatus("current")


class _HpicfIncludeCredentials_Type(Integer32):
    """Custom type hpicfIncludeCredentials based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("radiusTacacsOnly", 3))
    )


_HpicfIncludeCredentials_Type.__name__ = "Integer32"
_HpicfIncludeCredentials_Object = MibScalar
hpicfIncludeCredentials = _HpicfIncludeCredentials_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 19, 2),
    _HpicfIncludeCredentials_Type()
)
hpicfIncludeCredentials.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfIncludeCredentials.setStatus("current")
_HpicfBasicLogFilters_ObjectIdentity = ObjectIdentity
hpicfBasicLogFilters = _HpicfBasicLogFilters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23)
)
_HpicfBasicLogFiltersTable_Object = MibTable
hpicfBasicLogFiltersTable = _HpicfBasicLogFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1)
)
if mibBuilder.loadTexts:
    hpicfBasicLogFiltersTable.setStatus("current")
_HpicfBasicLogFiltersEntry_Object = MibTableRow
hpicfBasicLogFiltersEntry = _HpicfBasicLogFiltersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1, 1)
)
hpicfBasicLogFiltersEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfBasicLogFilterName"),
)
if mibBuilder.loadTexts:
    hpicfBasicLogFiltersEntry.setStatus("current")


class _HpicfBasicLogFilterName_Type(SnmpAdminString):
    """Custom type hpicfBasicLogFilterName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfBasicLogFilterName_Type.__name__ = "SnmpAdminString"
_HpicfBasicLogFilterName_Object = MibTableColumn
hpicfBasicLogFilterName = _HpicfBasicLogFilterName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1, 1, 1),
    _HpicfBasicLogFilterName_Type()
)
hpicfBasicLogFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBasicLogFilterName.setStatus("current")


class _HpicfBasicLogFilterEnable_Type(Integer32):
    """Custom type hpicfBasicLogFilterEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HpicfBasicLogFilterEnable_Type.__name__ = "Integer32"
_HpicfBasicLogFilterEnable_Object = MibTableColumn
hpicfBasicLogFilterEnable = _HpicfBasicLogFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1, 1, 2),
    _HpicfBasicLogFilterEnable_Type()
)
hpicfBasicLogFilterEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogFilterEnable.setStatus("current")
_HpicfBasicLogFilterDropCounter_Type = Counter32
_HpicfBasicLogFilterDropCounter_Object = MibTableColumn
hpicfBasicLogFilterDropCounter = _HpicfBasicLogFilterDropCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1, 1, 3),
    _HpicfBasicLogFilterDropCounter_Type()
)
hpicfBasicLogFilterDropCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBasicLogFilterDropCounter.setStatus("current")
_HpicfBasicLogFilterRowStatus_Type = RowStatus
_HpicfBasicLogFilterRowStatus_Object = MibTableColumn
hpicfBasicLogFilterRowStatus = _HpicfBasicLogFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 1, 1, 4),
    _HpicfBasicLogFilterRowStatus_Type()
)
hpicfBasicLogFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogFilterRowStatus.setStatus("current")
_HpicfBasicLogSubFiltersTable_Object = MibTable
hpicfBasicLogSubFiltersTable = _HpicfBasicLogSubFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2)
)
if mibBuilder.loadTexts:
    hpicfBasicLogSubFiltersTable.setStatus("current")
_HpicfBasicLogSubFilterEntry_Object = MibTableRow
hpicfBasicLogSubFilterEntry = _HpicfBasicLogSubFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1)
)
hpicfBasicLogSubFilterEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfBasicLogFilterName"),
    (0, "HP-ICF-BASIC", "hpicfBasicLogSubFilterSeqNum"),
)
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterEntry.setStatus("current")


class _HpicfBasicLogSubFilterSeqNum_Type(Integer32):
    """Custom type hpicfBasicLogSubFilterSeqNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_HpicfBasicLogSubFilterSeqNum_Type.__name__ = "Integer32"
_HpicfBasicLogSubFilterSeqNum_Object = MibTableColumn
hpicfBasicLogSubFilterSeqNum = _HpicfBasicLogSubFilterSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 1),
    _HpicfBasicLogSubFilterSeqNum_Type()
)
hpicfBasicLogSubFilterSeqNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterSeqNum.setStatus("current")


class _HpicfBasicLogSubFilterType_Type(Integer32):
    """Custom type hpicfBasicLogSubFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eventNum", 2),
          ("regExp", 3),
          ("severity", 1))
    )


_HpicfBasicLogSubFilterType_Type.__name__ = "Integer32"
_HpicfBasicLogSubFilterType_Object = MibTableColumn
hpicfBasicLogSubFilterType = _HpicfBasicLogSubFilterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 2),
    _HpicfBasicLogSubFilterType_Type()
)
hpicfBasicLogSubFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterType.setStatus("current")


class _HpicfBasicLogSubFilterSeverity_Type(Integer32):
    """Custom type hpicfBasicLogSubFilterSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("fatal", 1),
          ("info", 3),
          ("standard", 5),
          ("warn", 2))
    )


_HpicfBasicLogSubFilterSeverity_Type.__name__ = "Integer32"
_HpicfBasicLogSubFilterSeverity_Object = MibTableColumn
hpicfBasicLogSubFilterSeverity = _HpicfBasicLogSubFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 3),
    _HpicfBasicLogSubFilterSeverity_Type()
)
hpicfBasicLogSubFilterSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterSeverity.setStatus("current")


class _HpicfBasicLogSubFilterEventNum_Type(Integer32):
    """Custom type hpicfBasicLogSubFilterEventNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfBasicLogSubFilterEventNum_Type.__name__ = "Integer32"
_HpicfBasicLogSubFilterEventNum_Object = MibTableColumn
hpicfBasicLogSubFilterEventNum = _HpicfBasicLogSubFilterEventNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 4),
    _HpicfBasicLogSubFilterEventNum_Type()
)
hpicfBasicLogSubFilterEventNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterEventNum.setStatus("current")


class _HpicfBasicLogSubFilterRegExp_Type(SnmpAdminString):
    """Custom type hpicfBasicLogSubFilterRegExp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpicfBasicLogSubFilterRegExp_Type.__name__ = "SnmpAdminString"
_HpicfBasicLogSubFilterRegExp_Object = MibTableColumn
hpicfBasicLogSubFilterRegExp = _HpicfBasicLogSubFilterRegExp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 5),
    _HpicfBasicLogSubFilterRegExp_Type()
)
hpicfBasicLogSubFilterRegExp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterRegExp.setStatus("current")


class _HpicfBasicLogSubFilterAction_Type(Integer32):
    """Custom type hpicfBasicLogSubFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_HpicfBasicLogSubFilterAction_Type.__name__ = "Integer32"
_HpicfBasicLogSubFilterAction_Object = MibTableColumn
hpicfBasicLogSubFilterAction = _HpicfBasicLogSubFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 6),
    _HpicfBasicLogSubFilterAction_Type()
)
hpicfBasicLogSubFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterAction.setStatus("current")
_HpicfBasicLogSubFilterMatchCounter_Type = Counter32
_HpicfBasicLogSubFilterMatchCounter_Object = MibTableColumn
hpicfBasicLogSubFilterMatchCounter = _HpicfBasicLogSubFilterMatchCounter_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 7),
    _HpicfBasicLogSubFilterMatchCounter_Type()
)
hpicfBasicLogSubFilterMatchCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterMatchCounter.setStatus("current")
_HpicfBasicLogSubFilterRowStatus_Type = RowStatus
_HpicfBasicLogSubFilterRowStatus_Object = MibTableColumn
hpicfBasicLogSubFilterRowStatus = _HpicfBasicLogSubFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 2, 1, 8),
    _HpicfBasicLogSubFilterRowStatus_Type()
)
hpicfBasicLogSubFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogSubFilterRowStatus.setStatus("current")


class _HpicfBasicLogFiltersClearCounters_Type(SnmpAdminString):
    """Custom type hpicfBasicLogFiltersClearCounters based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfBasicLogFiltersClearCounters_Type.__name__ = "SnmpAdminString"
_HpicfBasicLogFiltersClearCounters_Object = MibScalar
hpicfBasicLogFiltersClearCounters = _HpicfBasicLogFiltersClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 3),
    _HpicfBasicLogFiltersClearCounters_Type()
)
hpicfBasicLogFiltersClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBasicLogFiltersClearCounters.setStatus("current")
_HpicfBasicLogPerIpFiltersTable_Object = MibTable
hpicfBasicLogPerIpFiltersTable = _HpicfBasicLogPerIpFiltersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4)
)
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFiltersTable.setStatus("current")
_HpicfBasicLogPerIpFilterEntry_Object = MibTableRow
hpicfBasicLogPerIpFilterEntry = _HpicfBasicLogPerIpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1)
)
hpicfBasicLogPerIpFilterEntry.setIndexNames(
    (0, "HP-ICF-BASIC", "hpicfBasicLogFilterName"),
    (0, "HP-ICF-BASIC", "hpicfBasicLogPerIpIndex"),
)
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterEntry.setStatus("current")


class _HpicfBasicLogPerIpIndex_Type(Unsigned32):
    """Custom type hpicfBasicLogPerIpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfBasicLogPerIpIndex_Type.__name__ = "Unsigned32"
_HpicfBasicLogPerIpIndex_Object = MibTableColumn
hpicfBasicLogPerIpIndex = _HpicfBasicLogPerIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 1),
    _HpicfBasicLogPerIpIndex_Type()
)
hpicfBasicLogPerIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpIndex.setStatus("current")


class _HpicfBasicLogPerIpFilterType_Type(Integer32):
    """Custom type hpicfBasicLogPerIpFilterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eventNum", 2),
          ("severity", 1),
          ("sysMod", 3))
    )


_HpicfBasicLogPerIpFilterType_Type.__name__ = "Integer32"
_HpicfBasicLogPerIpFilterType_Object = MibTableColumn
hpicfBasicLogPerIpFilterType = _HpicfBasicLogPerIpFilterType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 2),
    _HpicfBasicLogPerIpFilterType_Type()
)
hpicfBasicLogPerIpFilterType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterType.setStatus("current")


class _HpicfBasicLogPerIpFilterSeverity_Type(Integer32):
    """Custom type hpicfBasicLogPerIpFilterSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("debug", 4),
          ("fatal", 1),
          ("info", 3),
          ("standard", 5),
          ("warn", 2))
    )


_HpicfBasicLogPerIpFilterSeverity_Type.__name__ = "Integer32"
_HpicfBasicLogPerIpFilterSeverity_Object = MibTableColumn
hpicfBasicLogPerIpFilterSeverity = _HpicfBasicLogPerIpFilterSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 3),
    _HpicfBasicLogPerIpFilterSeverity_Type()
)
hpicfBasicLogPerIpFilterSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterSeverity.setStatus("current")


class _HpicfBasicLogPerIpFilterEventList_Type(OctetString):
    """Custom type hpicfBasicLogPerIpFilterEventList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(876, 876),
    )


_HpicfBasicLogPerIpFilterEventList_Type.__name__ = "OctetString"
_HpicfBasicLogPerIpFilterEventList_Object = MibTableColumn
hpicfBasicLogPerIpFilterEventList = _HpicfBasicLogPerIpFilterEventList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 4),
    _HpicfBasicLogPerIpFilterEventList_Type()
)
hpicfBasicLogPerIpFilterEventList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterEventList.setStatus("current")


class _HpicfBasicLogPerIpFilterAction_Type(Integer32):
    """Custom type hpicfBasicLogPerIpFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_HpicfBasicLogPerIpFilterAction_Type.__name__ = "Integer32"
_HpicfBasicLogPerIpFilterAction_Object = MibTableColumn
hpicfBasicLogPerIpFilterAction = _HpicfBasicLogPerIpFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 5),
    _HpicfBasicLogPerIpFilterAction_Type()
)
hpicfBasicLogPerIpFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterAction.setStatus("current")


class _HpicfBasicLogPerIpFilterSysModule_Type(OctetString):
    """Custom type hpicfBasicLogPerIpFilterSysModule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HpicfBasicLogPerIpFilterSysModule_Type.__name__ = "OctetString"
_HpicfBasicLogPerIpFilterSysModule_Object = MibTableColumn
hpicfBasicLogPerIpFilterSysModule = _HpicfBasicLogPerIpFilterSysModule_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 6),
    _HpicfBasicLogPerIpFilterSysModule_Type()
)
hpicfBasicLogPerIpFilterSysModule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterSysModule.setStatus("current")
_HpicfBasicLogPerIpFilterRowStatus_Type = RowStatus
_HpicfBasicLogPerIpFilterRowStatus_Object = MibTableColumn
hpicfBasicLogPerIpFilterRowStatus = _HpicfBasicLogPerIpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 23, 4, 1, 7),
    _HpicfBasicLogPerIpFilterRowStatus_Type()
)
hpicfBasicLogPerIpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfBasicLogPerIpFilterRowStatus.setStatus("current")
_HpicfBasicWebMgmtObjects_ObjectIdentity = ObjectIdentity
hpicfBasicWebMgmtObjects = _HpicfBasicWebMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 24)
)


class _HpicfBasicWebAgentIdleTime_Type(Integer32):
    """Custom type hpicfBasicWebAgentIdleTime based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_HpicfBasicWebAgentIdleTime_Type.__name__ = "Integer32"
_HpicfBasicWebAgentIdleTime_Object = MibScalar
hpicfBasicWebAgentIdleTime = _HpicfBasicWebAgentIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 24, 1),
    _HpicfBasicWebAgentIdleTime_Type()
)
hpicfBasicWebAgentIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBasicWebAgentIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    hpicfBasicWebAgentIdleTime.setUnits("seconds")


class _HpicfBasicWebAgentInterface_Type(Integer32):
    """Custom type hpicfBasicWebAgentInterface based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("improved", 2),
          ("traditional", 1))
    )


_HpicfBasicWebAgentInterface_Type.__name__ = "Integer32"
_HpicfBasicWebAgentInterface_Object = MibScalar
hpicfBasicWebAgentInterface = _HpicfBasicWebAgentInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 1, 4, 24, 2),
    _HpicfBasicWebAgentInterface_Type()
)
hpicfBasicWebAgentInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfBasicWebAgentInterface.setStatus("current")
alarmEntry.registerAugmentions(
    ("HP-ICF-BASIC",
     "hpicfBasicAlarmEntry")
)
hpicfBasicAlarmEntry.setIndexNames(*alarmEntry.getIndexNames())
eventEntry.registerAugmentions(
    ("HP-ICF-BASIC",
     "hpicfBasicEventEntry")
)
hpicfBasicEventEntry.setIndexNames(*eventEntry.getIndexNames())
snmpTargetAddrEntry.registerAugmentions(
    ("HP-ICF-BASIC",
     "hpicfSnmpTargetAddrLogFilterEntry")
)
hpicfSnmpTargetAddrLogFilterEntry.setIndexNames(*snmpTargetAddrEntry.getIndexNames())

# Managed Objects groups

hpicfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 1)
)
hpicfBasicGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfReset"),
        ("HP-ICF-BASIC", "hpicfSelfTest"))
)
if mibBuilder.loadTexts:
    hpicfBasicGroup.setStatus("deprecated")

hpicfTelnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 2)
)
hpicfTelnetGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfTelnetEnable")
)
if mibBuilder.loadTexts:
    hpicfTelnetGroup.setStatus("deprecated")

hpicfNewBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 3)
)
hpicfNewBasicGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfReset"),
        ("HP-ICF-BASIC", "hpicfSelfTest"),
        ("HP-ICF-BASIC", "hpicfTelnetEnable"),
        ("HP-ICF-BASIC", "hpicfConfigClear"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultCode"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultText"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultTime"),
        ("HP-ICF-BASIC", "hpicfBannerStatus"))
)
if mibBuilder.loadTexts:
    hpicfNewBasicGroup.setStatus("deprecated")

hpicfDiscoverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 4)
)
hpicfDiscoverGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfAnnounceAddress"),
        ("HP-ICF-BASIC", "hpicfIfEntLogicalIndex"))
)
if mibBuilder.loadTexts:
    hpicfDiscoverGroup.setStatus("deprecated")

hpicfBasicIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 5)
)
hpicfBasicIpConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpConfigAddress"),
        ("HP-ICF-BASIC", "hpicfIpConfigAddrMask"),
        ("HP-ICF-BASIC", "hpicfIpConfigDefaultRouter"),
        ("HP-ICF-BASIC", "hpicfIpConfigPingRouter"),
        ("HP-ICF-BASIC", "hpicfIpConfigMtu"),
        ("HP-ICF-BASIC", "hpicfIpConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    hpicfBasicIpConfigGroup.setStatus("deprecated")

hpicfBasicIpxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 6)
)
hpicfBasicIpxConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpxConfigNodeAddress"),
        ("HP-ICF-BASIC", "hpicfIpxConfigDefaultRouter"),
        ("HP-ICF-BASIC", "hpicfIpxConfigRouterEncaps"),
        ("HP-ICF-BASIC", "hpicfIpxConfigAdminStatus"),
        ("HP-ICF-BASIC", "hpicfIpxNetNumber"))
)
if mibBuilder.loadTexts:
    hpicfBasicIpxConfigGroup.setStatus("current")

hpicfBasicFixedTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 7)
)
hpicfBasicFixedTrapGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfFixedTrapEventIndex")
)
if mibBuilder.loadTexts:
    hpicfBasicFixedTrapGroup.setStatus("current")

hpicfBasicTrapDestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 8)
)
hpicfBasicTrapDestGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfTrapDestVersion"),
        ("HP-ICF-BASIC", "hpicfTrapDestCommunity"),
        ("HP-ICF-BASIC", "hpicfTrapDestTDomain"),
        ("HP-ICF-BASIC", "hpicfTrapDestTAddress"),
        ("HP-ICF-BASIC", "hpicfTrapDestFilter"),
        ("HP-ICF-BASIC", "hpicfTrapDestStatus"))
)
if mibBuilder.loadTexts:
    hpicfBasicTrapDestGroup.setStatus("deprecated")

hpicfBasicRmonNVGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 9)
)
hpicfBasicRmonNVGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfBasicAlarmNVCapacity"),
        ("HP-ICF-BASIC", "hpicfBasicAlarmStorageType"),
        ("HP-ICF-BASIC", "hpicfBasicEventNVCapacity"),
        ("HP-ICF-BASIC", "hpicfBasicEventStorageType"))
)
if mibBuilder.loadTexts:
    hpicfBasicRmonNVGroup.setStatus("current")

hpicfBasicWebAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 11)
)
hpicfBasicWebAgentGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfWebAgentEnable")
)
if mibBuilder.loadTexts:
    hpicfBasicWebAgentGroup.setStatus("deprecated")

hpicfAnnounceDiscoveryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 12)
)
hpicfAnnounceDiscoveryGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfAnnounceDiscoveryAddress")
)
if mibBuilder.loadTexts:
    hpicfAnnounceDiscoveryGroup.setStatus("current")

hpicfBasicIpConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 13)
)
hpicfBasicIpConfigGroup2.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpConfigAddress"),
        ("HP-ICF-BASIC", "hpicfIpConfigAddrMask"),
        ("HP-ICF-BASIC", "hpicfIpConfigMtu"),
        ("HP-ICF-BASIC", "hpicfIpConfigAdminStatus"),
        ("HP-ICF-BASIC", "hpicfIpGlobalDefaultRouter"),
        ("HP-ICF-BASIC", "hpicfIpGlobalPingRouter"))
)
if mibBuilder.loadTexts:
    hpicfBasicIpConfigGroup2.setStatus("deprecated")

hpicfBasicProxyArpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 14)
)
hpicfBasicProxyArpGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfIpConfigProxyArp")
)
if mibBuilder.loadTexts:
    hpicfBasicProxyArpGroup.setStatus("current")

hpicfBasicIpSecondaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 15)
)
hpicfBasicIpSecondaryGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpAddrMask"),
        ("HP-ICF-BASIC", "hpicfIpAddrStatus"))
)
if mibBuilder.loadTexts:
    hpicfBasicIpSecondaryGroup.setStatus("current")

hpicfSnmpTargetAddrLogFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 16)
)
hpicfSnmpTargetAddrLogFilterGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfSnmpTargetAddrLogFilter")
)
if mibBuilder.loadTexts:
    hpicfSnmpTargetAddrLogFilterGroup.setStatus("current")

hpicfBasicIpConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 17)
)
hpicfBasicIpConfigGroup3.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpConfigAddress"),
        ("HP-ICF-BASIC", "hpicfIpConfigAddrMask"),
        ("HP-ICF-BASIC", "hpicfIpConfigMtu"),
        ("HP-ICF-BASIC", "hpicfIpConfigAdminStatus"),
        ("HP-ICF-BASIC", "hpicfIpGlobalDefaultRouter"),
        ("HP-ICF-BASIC", "hpicfIpGlobalPingRouter"),
        ("HP-ICF-BASIC", "hpicfIpZeroBroadcastEnable"))
)
if mibBuilder.loadTexts:
    hpicfBasicIpConfigGroup3.setStatus("current")

hpicfBasicBannerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 18)
)
hpicfBasicBannerGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfBannerMOTD"),
        ("HP-ICF-BASIC", "hpicfExecBannerStatus"),
        ("HP-ICF-BASIC", "hpicfBannerExec"))
)
if mibBuilder.loadTexts:
    hpicfBasicBannerGroup.setStatus("current")

hpicfBasicDNSConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 19)
)
hpicfBasicDNSConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfDNSDefaultDomainSuffix"),
        ("HP-ICF-BASIC", "hpicfDNSNameServerEntryStatus"))
)
if mibBuilder.loadTexts:
    hpicfBasicDNSConfigGroup.setStatus("deprecated")

hpicfBasicGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 20)
)
hpicfBasicGroup1.setObjects(
      *(("HP-ICF-BASIC", "hpicfReset"),
        ("HP-ICF-BASIC", "hpicfSelfTest"),
        ("HP-ICF-BASIC", "hpicfTelnetEnable"),
        ("HP-ICF-BASIC", "hpicfConfigClear"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultCode"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultText"),
        ("HP-ICF-BASIC", "hpicfSelfTestResultTime"),
        ("HP-ICF-BASIC", "hpicfBannerStatus"),
        ("HP-ICF-BASIC", "hpicfResetDefault"))
)
if mibBuilder.loadTexts:
    hpicfBasicGroup1.setStatus("current")

hpicfSNMPConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 21)
)
hpicfSNMPConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfSnmpV2Enable"),
        ("HP-ICF-BASIC", "hpSwitchSnmpViewConfig"))
)
if mibBuilder.loadTexts:
    hpicfSNMPConfigGroup.setStatus("deprecated")

hpicfBasicConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 22)
)
hpicfBasicConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfDisplayLogNumbers"),
        ("HP-ICF-BASIC", "hpicfIncludeCredentials"))
)
if mibBuilder.loadTexts:
    hpicfBasicConfigGroup.setStatus("current")

hpicfInetDNSNameServerOobmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 23)
)
hpicfInetDNSNameServerOobmGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfInetDNSNameServerEntryIsOobm")
)
if mibBuilder.loadTexts:
    hpicfInetDNSNameServerOobmGroup.setStatus("current")

hpicfBasicObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 24)
)
hpicfBasicObjectsGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpConfigLocalProxyArp"),
        ("HP-ICF-BASIC", "hpicfTrapDestNotifyType"),
        ("HP-ICF-BASIC", "hpicfTrapDestRetries"),
        ("HP-ICF-BASIC", "hpicfTrapDestTimeout"),
        ("HP-ICF-BASIC", "hpicfInetDNSNameServerEntryStatus"),
        ("HP-ICF-BASIC", "hpicfExecBannerStatus"),
        ("HP-ICF-BASIC", "hpicfBannerExec"),
        ("HP-ICF-BASIC", "hpicfTelnet6Enable"))
)
if mibBuilder.loadTexts:
    hpicfBasicObjectsGroup.setStatus("deprecated")

hpicfBasicDNSGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 25)
)
hpicfBasicDNSGroup1.setObjects(
      *(("HP-ICF-BASIC", "hpicfDNSDefaultDomainSuffixIsOobm"),
        ("HP-ICF-BASIC", "hpicfDNSConfigMode"),
        ("HP-ICF-BASIC", "hpicfCurDNSDefaultDomainSuffix"))
)
if mibBuilder.loadTexts:
    hpicfBasicDNSGroup1.setStatus("deprecated")

hpicfBasicDNSConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 26)
)
hpicfBasicDNSConfigGroup1.setObjects(
    ("HP-ICF-BASIC", "hpicfDNSDomainSuffix")
)
if mibBuilder.loadTexts:
    hpicfBasicDNSConfigGroup1.setStatus("current")

hpicfBasicObjectsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 27)
)
hpicfBasicObjectsGroup1.setObjects(
      *(("HP-ICF-BASIC", "hpicfIpConfigLocalProxyArp"),
        ("HP-ICF-BASIC", "hpicfTrapDestNotifyType"),
        ("HP-ICF-BASIC", "hpicfTrapDestRetries"),
        ("HP-ICF-BASIC", "hpicfTrapDestTimeout"),
        ("HP-ICF-BASIC", "hpicfInetDNSNameServerEntryStatus"),
        ("HP-ICF-BASIC", "hpicfExecBannerStatus"),
        ("HP-ICF-BASIC", "hpicfBannerExec"),
        ("HP-ICF-BASIC", "hpicfLastLoginBannerStatus"),
        ("HP-ICF-BASIC", "hpicfTelnet6Enable"),
        ("HP-ICF-BASIC", "hpicfBannerExec1"))
)
if mibBuilder.loadTexts:
    hpicfBasicObjectsGroup1.setStatus("current")

hpicfBasicDNSConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 28)
)
hpicfBasicDNSConfigGroup2.setObjects(
    ("HP-ICF-BASIC", "hpicfDNSNameServerEntryStatus")
)
if mibBuilder.loadTexts:
    hpicfBasicDNSConfigGroup2.setStatus("current")

hpicfBasicDNSGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 29)
)
hpicfBasicDNSGroup2.setObjects(
      *(("HP-ICF-BASIC", "hpicfDNSDefaultDomainSuffixIsOobm"),
        ("HP-ICF-BASIC", "hpicfDNSConfigMode"))
)
if mibBuilder.loadTexts:
    hpicfBasicDNSGroup2.setStatus("current")

hpicfBasicLogFilterConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 30)
)
hpicfBasicLogFilterConfigGroup.setObjects(
      *(("HP-ICF-BASIC", "hpicfBasicLogFilterName"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterEnable"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterDropCounter"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterSeqNum"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterType"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterSeverity"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterEventNum"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterRegExp"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterAction"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterMatchCounter"))
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigGroup.setStatus("deprecated")

hpicfBasicWebAgentGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 31)
)
hpicfBasicWebAgentGroup1.setObjects(
      *(("HP-ICF-BASIC", "hpicfWebAgentEnable"),
        ("HP-ICF-BASIC", "hpicfBasicWebAgentIdleTime"))
)
if mibBuilder.loadTexts:
    hpicfBasicWebAgentGroup1.setStatus("deprecated")

hpicfSNMPConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 32)
)
hpicfSNMPConfigGroup1.setObjects(
      *(("HP-ICF-BASIC", "hpicfSnmpV2Enable"),
        ("HP-ICF-BASIC", "hpSwitchSnmpViewConfig"),
        ("HP-ICF-BASIC", "hpicfSwitchSnmpAllowUnsecuredAccessToMACsec"),
        ("HP-ICF-BASIC", "hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy"))
)
if mibBuilder.loadTexts:
    hpicfSNMPConfigGroup1.setStatus("current")

hpicfBasicLogFilterConfigGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 33)
)
hpicfBasicLogFilterConfigGroup2.setObjects(
      *(("HP-ICF-BASIC", "hpicfBasicLogFilterEnable"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterDropCounter"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterRowStatus"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterType"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterSeverity"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterEventNum"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterRegExp"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterAction"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterMatchCounter"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterRowStatus"),
        ("HP-ICF-BASIC", "hpicfBasicLogFiltersClearCounters"))
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigGroup2.setStatus("deprecated")

hpicfBasicWebAgentGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 34)
)
hpicfBasicWebAgentGroup2.setObjects(
      *(("HP-ICF-BASIC", "hpicfWebAgentEnable"),
        ("HP-ICF-BASIC", "hpicfBasicWebAgentIdleTime"),
        ("HP-ICF-BASIC", "hpicfBasicWebAgentInterface"))
)
if mibBuilder.loadTexts:
    hpicfBasicWebAgentGroup2.setStatus("current")

hpicfBasicCurDNSNameServerGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 35)
)
hpicfBasicCurDNSNameServerGroup1.setObjects(
    ("HP-ICF-BASIC", "hpicfCurDNSNameServerEntryStatus")
)
if mibBuilder.loadTexts:
    hpicfBasicCurDNSNameServerGroup1.setStatus("current")

hpicfBasicLogFilterConfigGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 36)
)
hpicfBasicLogFilterConfigGroup3.setObjects(
      *(("HP-ICF-BASIC", "hpicfBasicLogFilterEnable"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterDropCounter"),
        ("HP-ICF-BASIC", "hpicfBasicLogFilterRowStatus"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterType"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterSeverity"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterEventNum"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterRegExp"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterAction"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterMatchCounter"),
        ("HP-ICF-BASIC", "hpicfBasicLogSubFilterRowStatus"),
        ("HP-ICF-BASIC", "hpicfBasicLogFiltersClearCounters"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterType"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterSeverity"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterEventList"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterAction"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterSysModule"),
        ("HP-ICF-BASIC", "hpicfBasicLogPerIpFilterRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigGroup3.setStatus("current")


# Notification objects

hpicfSelfTestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 12, 1, 0, 4)
)
hpicfSelfTestTrap.setObjects(
    ("HP-ICF-BASIC", "hpicfSelfTestResultText")
)
if mibBuilder.loadTexts:
    hpicfSelfTestTrap.setStatus(
        "current"
    )


# Notifications groups

hpicfBasicSelfTestNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 2, 10)
)
hpicfBasicSelfTestNotifyGroup.setObjects(
    ("HP-ICF-BASIC", "hpicfSelfTestTrap")
)
if mibBuilder.loadTexts:
    hpicfBasicSelfTestNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance.setStatus(
        "deprecated"
    )

hpicfNewBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfNewBasicCompliance.setStatus(
        "deprecated"
    )

hpicfBasicCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance3.setStatus(
        "deprecated"
    )

hpicfBasicCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance4.setStatus(
        "deprecated"
    )

hpicfBasicCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance5.setStatus(
        "deprecated"
    )

hpicfBasicCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance6.setStatus(
        "deprecated"
    )

hpicfBasicCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance7.setStatus(
        "deprecated"
    )

hpicfBasicSNMPConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfBasicSNMPConfigCompliance.setStatus(
        "deprecated"
    )

hpicfBasicConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfBasicConfigCompliance.setStatus(
        "current"
    )

hpicfBasicComplianceOobm = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 10)
)
if mibBuilder.loadTexts:
    hpicfBasicComplianceOobm.setStatus(
        "current"
    )

hpicfBasicCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance8.setStatus(
        "deprecated"
    )

hpicfBasicCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance9.setStatus(
        "deprecated"
    )

hpicfBasicCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance10.setStatus(
        "current"
    )

hpicfBasicCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance11.setStatus(
        "current"
    )

hpicfBasicCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 15)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance12.setStatus(
        "deprecated"
    )

hpicfBasicLogFilterConfigCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 16)
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigCompliance.setStatus(
        "deprecated"
    )

hpicfBasicCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 17)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance13.setStatus(
        "deprecated"
    )

hpicfBasicSNMPConfigCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 18)
)
if mibBuilder.loadTexts:
    hpicfBasicSNMPConfigCompliance1.setStatus(
        "current"
    )

hpicfBasicCompliance19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 19)
)
if mibBuilder.loadTexts:
    hpicfBasicCompliance19.setStatus(
        "current"
    )

hpicfBasicLogFilterConfigCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 20)
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigCompliance2.setStatus(
        "deprecated"
    )

hpicfBasicWebAgentCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 21)
)
if mibBuilder.loadTexts:
    hpicfBasicWebAgentCompliance1.setStatus(
        "current"
    )

hpicfBasicCurDNSNameServerCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 22)
)
if mibBuilder.loadTexts:
    hpicfBasicCurDNSNameServerCompliance1.setStatus(
        "current"
    )

hpicfBasicLogFilterConfigCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 10, 2, 5, 1, 1, 23)
)
if mibBuilder.loadTexts:
    hpicfBasicLogFilterConfigCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-BASIC",
    **{"hpicfBasicMib": hpicfBasicMib,
       "hpicfBasicConformance": hpicfBasicConformance,
       "hpicfBasicCompliances": hpicfBasicCompliances,
       "hpicfBasicCompliance": hpicfBasicCompliance,
       "hpicfNewBasicCompliance": hpicfNewBasicCompliance,
       "hpicfBasicCompliance3": hpicfBasicCompliance3,
       "hpicfBasicCompliance4": hpicfBasicCompliance4,
       "hpicfBasicCompliance5": hpicfBasicCompliance5,
       "hpicfBasicCompliance6": hpicfBasicCompliance6,
       "hpicfBasicCompliance7": hpicfBasicCompliance7,
       "hpicfBasicSNMPConfigCompliance": hpicfBasicSNMPConfigCompliance,
       "hpicfBasicConfigCompliance": hpicfBasicConfigCompliance,
       "hpicfBasicComplianceOobm": hpicfBasicComplianceOobm,
       "hpicfBasicCompliance8": hpicfBasicCompliance8,
       "hpicfBasicCompliance9": hpicfBasicCompliance9,
       "hpicfBasicCompliance10": hpicfBasicCompliance10,
       "hpicfBasicCompliance11": hpicfBasicCompliance11,
       "hpicfBasicCompliance12": hpicfBasicCompliance12,
       "hpicfBasicLogFilterConfigCompliance": hpicfBasicLogFilterConfigCompliance,
       "hpicfBasicCompliance13": hpicfBasicCompliance13,
       "hpicfBasicSNMPConfigCompliance1": hpicfBasicSNMPConfigCompliance1,
       "hpicfBasicCompliance19": hpicfBasicCompliance19,
       "hpicfBasicLogFilterConfigCompliance2": hpicfBasicLogFilterConfigCompliance2,
       "hpicfBasicWebAgentCompliance1": hpicfBasicWebAgentCompliance1,
       "hpicfBasicCurDNSNameServerCompliance1": hpicfBasicCurDNSNameServerCompliance1,
       "hpicfBasicLogFilterConfigCompliance3": hpicfBasicLogFilterConfigCompliance3,
       "hpicfBasicGroups": hpicfBasicGroups,
       "hpicfBasicGroup": hpicfBasicGroup,
       "hpicfTelnetGroup": hpicfTelnetGroup,
       "hpicfNewBasicGroup": hpicfNewBasicGroup,
       "hpicfDiscoverGroup": hpicfDiscoverGroup,
       "hpicfBasicIpConfigGroup": hpicfBasicIpConfigGroup,
       "hpicfBasicIpxConfigGroup": hpicfBasicIpxConfigGroup,
       "hpicfBasicFixedTrapGroup": hpicfBasicFixedTrapGroup,
       "hpicfBasicTrapDestGroup": hpicfBasicTrapDestGroup,
       "hpicfBasicRmonNVGroup": hpicfBasicRmonNVGroup,
       "hpicfBasicSelfTestNotifyGroup": hpicfBasicSelfTestNotifyGroup,
       "hpicfBasicWebAgentGroup": hpicfBasicWebAgentGroup,
       "hpicfAnnounceDiscoveryGroup": hpicfAnnounceDiscoveryGroup,
       "hpicfBasicIpConfigGroup2": hpicfBasicIpConfigGroup2,
       "hpicfBasicProxyArpGroup": hpicfBasicProxyArpGroup,
       "hpicfBasicIpSecondaryGroup": hpicfBasicIpSecondaryGroup,
       "hpicfSnmpTargetAddrLogFilterGroup": hpicfSnmpTargetAddrLogFilterGroup,
       "hpicfBasicIpConfigGroup3": hpicfBasicIpConfigGroup3,
       "hpicfBasicBannerGroup": hpicfBasicBannerGroup,
       "hpicfBasicDNSConfigGroup": hpicfBasicDNSConfigGroup,
       "hpicfBasicGroup1": hpicfBasicGroup1,
       "hpicfSNMPConfigGroup": hpicfSNMPConfigGroup,
       "hpicfBasicConfigGroup": hpicfBasicConfigGroup,
       "hpicfInetDNSNameServerOobmGroup": hpicfInetDNSNameServerOobmGroup,
       "hpicfBasicObjectsGroup": hpicfBasicObjectsGroup,
       "hpicfBasicDNSGroup1": hpicfBasicDNSGroup1,
       "hpicfBasicDNSConfigGroup1": hpicfBasicDNSConfigGroup1,
       "hpicfBasicObjectsGroup1": hpicfBasicObjectsGroup1,
       "hpicfBasicDNSConfigGroup2": hpicfBasicDNSConfigGroup2,
       "hpicfBasicDNSGroup2": hpicfBasicDNSGroup2,
       "hpicfBasicLogFilterConfigGroup": hpicfBasicLogFilterConfigGroup,
       "hpicfBasicWebAgentGroup1": hpicfBasicWebAgentGroup1,
       "hpicfSNMPConfigGroup1": hpicfSNMPConfigGroup1,
       "hpicfBasicLogFilterConfigGroup2": hpicfBasicLogFilterConfigGroup2,
       "hpicfBasicWebAgentGroup2": hpicfBasicWebAgentGroup2,
       "hpicfBasicCurDNSNameServerGroup1": hpicfBasicCurDNSNameServerGroup1,
       "hpicfBasicLogFilterConfigGroup3": hpicfBasicLogFilterConfigGroup3,
       "hpicfBasic": hpicfBasic,
       "hpicfReset": hpicfReset,
       "hpicfSelfTest": hpicfSelfTest,
       "hpicfTelnetEnable": hpicfTelnetEnable,
       "hpicfConfigClear": hpicfConfigClear,
       "hpicfSelfTestResult": hpicfSelfTestResult,
       "hpicfSelfTestResultCode": hpicfSelfTestResultCode,
       "hpicfSelfTestResultText": hpicfSelfTestResultText,
       "hpicfSelfTestResultTime": hpicfSelfTestResultTime,
       "hpicfWebAgentEnable": hpicfWebAgentEnable,
       "hpicfBasicDiscovery": hpicfBasicDiscovery,
       "hpicfAnnounceTable": hpicfAnnounceTable,
       "hpicfAnnounceEntry": hpicfAnnounceEntry,
       "hpicfAnnounceAddress": hpicfAnnounceAddress,
       "hpicfIfToEntityTable": hpicfIfToEntityTable,
       "hpicfIfToEntityEntry": hpicfIfToEntityEntry,
       "hpicfIfEntLogicalIndex": hpicfIfEntLogicalIndex,
       "hpicfAnnounceDiscoveryTable": hpicfAnnounceDiscoveryTable,
       "hpicfAnnounceDiscoveryEntry": hpicfAnnounceDiscoveryEntry,
       "hpicfAnnounceDiscoveryAddress": hpicfAnnounceDiscoveryAddress,
       "hpicfBasicIpConfig": hpicfBasicIpConfig,
       "hpicfIpConfigTable": hpicfIpConfigTable,
       "hpicfIpConfigEntry": hpicfIpConfigEntry,
       "hpicfIpConfigAddress": hpicfIpConfigAddress,
       "hpicfIpConfigAddrMask": hpicfIpConfigAddrMask,
       "hpicfIpConfigDefaultRouter": hpicfIpConfigDefaultRouter,
       "hpicfIpConfigPingRouter": hpicfIpConfigPingRouter,
       "hpicfIpConfigMtu": hpicfIpConfigMtu,
       "hpicfIpConfigAdminStatus": hpicfIpConfigAdminStatus,
       "hpicfIpConfigProxyArp": hpicfIpConfigProxyArp,
       "hpicfIpConfigLocalProxyArp": hpicfIpConfigLocalProxyArp,
       "hpicfIpAddrTable": hpicfIpAddrTable,
       "hpicfIpAddrEntry": hpicfIpAddrEntry,
       "hpicfIpAddrAddr": hpicfIpAddrAddr,
       "hpicfIpAddrMask": hpicfIpAddrMask,
       "hpicfIpAddrStatus": hpicfIpAddrStatus,
       "hpicfIpGlobalDefaultRouter": hpicfIpGlobalDefaultRouter,
       "hpicfIpGlobalPingRouter": hpicfIpGlobalPingRouter,
       "hpicfIpZeroBroadcastEnable": hpicfIpZeroBroadcastEnable,
       "hpicfBasicIpxConfig": hpicfBasicIpxConfig,
       "hpicfIpxConfigTable": hpicfIpxConfigTable,
       "hpicfIpxConfigEntry": hpicfIpxConfigEntry,
       "hpicfIpxConfigNodeAddress": hpicfIpxConfigNodeAddress,
       "hpicfIpxConfigDefaultRouter": hpicfIpxConfigDefaultRouter,
       "hpicfIpxConfigRouterEncaps": hpicfIpxConfigRouterEncaps,
       "hpicfIpxConfigAdminStatus": hpicfIpxConfigAdminStatus,
       "hpicfIpxNetTable": hpicfIpxNetTable,
       "hpicfIpxNetEntry": hpicfIpxNetEntry,
       "hpicfIpxNetEncaps": hpicfIpxNetEncaps,
       "hpicfIpxNetNumber": hpicfIpxNetNumber,
       "hpicfBasicTraps": hpicfBasicTraps,
       "hpicfFixedTrapTable": hpicfFixedTrapTable,
       "hpicfFixedTrapEntry": hpicfFixedTrapEntry,
       "hpicfFixedTrapID": hpicfFixedTrapID,
       "hpicfFixedTrapEventIndex": hpicfFixedTrapEventIndex,
       "hpicfTrapDestTable": hpicfTrapDestTable,
       "hpicfTrapDestEntry": hpicfTrapDestEntry,
       "hpicfTrapDestIndex": hpicfTrapDestIndex,
       "hpicfTrapDestVersion": hpicfTrapDestVersion,
       "hpicfTrapDestCommunity": hpicfTrapDestCommunity,
       "hpicfTrapDestTDomain": hpicfTrapDestTDomain,
       "hpicfTrapDestTAddress": hpicfTrapDestTAddress,
       "hpicfTrapDestFilter": hpicfTrapDestFilter,
       "hpicfTrapDestStatus": hpicfTrapDestStatus,
       "hpicfTrapDestNotifyType": hpicfTrapDestNotifyType,
       "hpicfTrapDestRetries": hpicfTrapDestRetries,
       "hpicfTrapDestTimeout": hpicfTrapDestTimeout,
       "hpicfBasicRmon": hpicfBasicRmon,
       "hpicfBasicAlarm": hpicfBasicAlarm,
       "hpicfBasicAlarmNVCapacity": hpicfBasicAlarmNVCapacity,
       "hpicfBasicAlarmTable": hpicfBasicAlarmTable,
       "hpicfBasicAlarmEntry": hpicfBasicAlarmEntry,
       "hpicfBasicAlarmStorageType": hpicfBasicAlarmStorageType,
       "hpicfBasicEvent": hpicfBasicEvent,
       "hpicfBasicEventNVCapacity": hpicfBasicEventNVCapacity,
       "hpicfBasicEventTable": hpicfBasicEventTable,
       "hpicfBasicEventEntry": hpicfBasicEventEntry,
       "hpicfBasicEventStorageType": hpicfBasicEventStorageType,
       "hpicfBasicSnmpTargetAddrLogFilter": hpicfBasicSnmpTargetAddrLogFilter,
       "hpicfSnmpTargetAddrLogFilterTable": hpicfSnmpTargetAddrLogFilterTable,
       "hpicfSnmpTargetAddrLogFilterEntry": hpicfSnmpTargetAddrLogFilterEntry,
       "hpicfSnmpTargetAddrLogFilter": hpicfSnmpTargetAddrLogFilter,
       "hpicfBannerStatus": hpicfBannerStatus,
       "hpicfBanner": hpicfBanner,
       "hpicfBannerMOTD": hpicfBannerMOTD,
       "hpicfExecBannerStatus": hpicfExecBannerStatus,
       "hpicfBannerExec": hpicfBannerExec,
       "hpicfLastLoginBannerStatus": hpicfLastLoginBannerStatus,
       "hpicfBannerExec1": hpicfBannerExec1,
       "hpicfBasicDNSConfig": hpicfBasicDNSConfig,
       "hpicfDNSDefaultDomainSuffix": hpicfDNSDefaultDomainSuffix,
       "hpicfDNSNameServerTable": hpicfDNSNameServerTable,
       "hpicfDNSNameServerEntry": hpicfDNSNameServerEntry,
       "hpicfDNSNameServerAddress": hpicfDNSNameServerAddress,
       "hpicfDNSNameServerEntryStatus": hpicfDNSNameServerEntryStatus,
       "hpicfInetDNSNameServerTable": hpicfInetDNSNameServerTable,
       "hpicfInetDNSNameServerEntry": hpicfInetDNSNameServerEntry,
       "hpicfInetDNSNameServerAddrIndex": hpicfInetDNSNameServerAddrIndex,
       "hpicfInetDNSNameServerAddrType": hpicfInetDNSNameServerAddrType,
       "hpicfInetDNSNameServerAddress": hpicfInetDNSNameServerAddress,
       "hpicfInetDNSNameServerEntryStatus": hpicfInetDNSNameServerEntryStatus,
       "hpicfInetDNSNameServerEntryIsOobm": hpicfInetDNSNameServerEntryIsOobm,
       "hpicfDNSDefaultDomainSuffixIsOobm": hpicfDNSDefaultDomainSuffixIsOobm,
       "hpicfDNSConfigMode": hpicfDNSConfigMode,
       "hpicfCurDNSConfig": hpicfCurDNSConfig,
       "hpicfCurDNSDefaultDomainSuffix": hpicfCurDNSDefaultDomainSuffix,
       "hpicfCurDNSNameServerTable": hpicfCurDNSNameServerTable,
       "hpicfCurDNSNameServerEntry": hpicfCurDNSNameServerEntry,
       "hpicfCurDNSNameServerAddrIndex": hpicfCurDNSNameServerAddrIndex,
       "hpicfCurDNSNameServerAddrType": hpicfCurDNSNameServerAddrType,
       "hpicfCurDNSNameServerAddress": hpicfCurDNSNameServerAddress,
       "hpicfCurDNSNameServerEntryStatus": hpicfCurDNSNameServerEntryStatus,
       "hpicfDNSDomainSuffixTable": hpicfDNSDomainSuffixTable,
       "hpicfDNSDomainSuffixEntry": hpicfDNSDomainSuffixEntry,
       "hpicfDNSDomainSuffixIndex": hpicfDNSDomainSuffixIndex,
       "hpicfDNSDomainSuffix": hpicfDNSDomainSuffix,
       "hpicfResetDefault": hpicfResetDefault,
       "hpicfTelnet6Enable": hpicfTelnet6Enable,
       "hpicfBasicSNMPConfig": hpicfBasicSNMPConfig,
       "hpSwitchSnmpViewConfig": hpSwitchSnmpViewConfig,
       "hpicfSnmpV2Enable": hpicfSnmpV2Enable,
       "hpicfSwitchSnmpAllowUnsecuredAccessToMACsec": hpicfSwitchSnmpAllowUnsecuredAccessToMACsec,
       "hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy": hpicfSwitchSnmpAllowUnsecuredAccessToIeee8021Secy,
       "hpicfBasicConfig": hpicfBasicConfig,
       "hpicfDisplayLogNumbers": hpicfDisplayLogNumbers,
       "hpicfIncludeCredentials": hpicfIncludeCredentials,
       "hpicfBasicLogFilters": hpicfBasicLogFilters,
       "hpicfBasicLogFiltersTable": hpicfBasicLogFiltersTable,
       "hpicfBasicLogFiltersEntry": hpicfBasicLogFiltersEntry,
       "hpicfBasicLogFilterName": hpicfBasicLogFilterName,
       "hpicfBasicLogFilterEnable": hpicfBasicLogFilterEnable,
       "hpicfBasicLogFilterDropCounter": hpicfBasicLogFilterDropCounter,
       "hpicfBasicLogFilterRowStatus": hpicfBasicLogFilterRowStatus,
       "hpicfBasicLogSubFiltersTable": hpicfBasicLogSubFiltersTable,
       "hpicfBasicLogSubFilterEntry": hpicfBasicLogSubFilterEntry,
       "hpicfBasicLogSubFilterSeqNum": hpicfBasicLogSubFilterSeqNum,
       "hpicfBasicLogSubFilterType": hpicfBasicLogSubFilterType,
       "hpicfBasicLogSubFilterSeverity": hpicfBasicLogSubFilterSeverity,
       "hpicfBasicLogSubFilterEventNum": hpicfBasicLogSubFilterEventNum,
       "hpicfBasicLogSubFilterRegExp": hpicfBasicLogSubFilterRegExp,
       "hpicfBasicLogSubFilterAction": hpicfBasicLogSubFilterAction,
       "hpicfBasicLogSubFilterMatchCounter": hpicfBasicLogSubFilterMatchCounter,
       "hpicfBasicLogSubFilterRowStatus": hpicfBasicLogSubFilterRowStatus,
       "hpicfBasicLogFiltersClearCounters": hpicfBasicLogFiltersClearCounters,
       "hpicfBasicLogPerIpFiltersTable": hpicfBasicLogPerIpFiltersTable,
       "hpicfBasicLogPerIpFilterEntry": hpicfBasicLogPerIpFilterEntry,
       "hpicfBasicLogPerIpIndex": hpicfBasicLogPerIpIndex,
       "hpicfBasicLogPerIpFilterType": hpicfBasicLogPerIpFilterType,
       "hpicfBasicLogPerIpFilterSeverity": hpicfBasicLogPerIpFilterSeverity,
       "hpicfBasicLogPerIpFilterEventList": hpicfBasicLogPerIpFilterEventList,
       "hpicfBasicLogPerIpFilterAction": hpicfBasicLogPerIpFilterAction,
       "hpicfBasicLogPerIpFilterSysModule": hpicfBasicLogPerIpFilterSysModule,
       "hpicfBasicLogPerIpFilterRowStatus": hpicfBasicLogPerIpFilterRowStatus,
       "hpicfBasicWebMgmtObjects": hpicfBasicWebMgmtObjects,
       "hpicfBasicWebAgentIdleTime": hpicfBasicWebAgentIdleTime,
       "hpicfBasicWebAgentInterface": hpicfBasicWebAgentInterface,
       "hpicfSelfTestTrap": hpicfSelfTestTrap}
)
