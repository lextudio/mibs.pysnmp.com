# SNMP MIB module (SONICWALL-FIREWALL-IP-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONICWALL-FIREWALL-IP-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:56:33 2024
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(sonicwallFw,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallFw")


# MODULE-IDENTITY

sonicwallFwStatsModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3)
)
sonicwallFwStatsModule.setRevisions(
        ("2015-01-08 00:00",
         "2014-02-28 00:00",
         "2014-02-18 00:00",
         "2005-11-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SyslogFacility(Integer32, TextualConvention):
    status = "current"
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("alert", 14),
          ("audit", 13),
          ("auth", 4),
          ("authpriv", 10),
          ("cron", 9),
          ("cron2", 15),
          ("daemon", 3),
          ("ftp", 11),
          ("kern", 0),
          ("local0", 16),
          ("local1", 17),
          ("local2", 18),
          ("local3", 19),
          ("local4", 20),
          ("local5", 21),
          ("local6", 22),
          ("local7", 23),
          ("lpr", 6),
          ("mail", 2),
          ("news", 7),
          ("ntp", 12),
          ("syslog", 5),
          ("user", 1),
          ("uucp", 8))
    )



# MIB Managed Objects in the order of their OIDs

_SonicwallFwStats_ObjectIdentity = ObjectIdentity
sonicwallFwStats = _SonicwallFwStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1)
)


class _SonicMaxConnCacheEntries_Type(Integer32):
    """Custom type sonicMaxConnCacheEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SonicMaxConnCacheEntries_Type.__name__ = "Integer32"
_SonicMaxConnCacheEntries_Object = MibScalar
sonicMaxConnCacheEntries = _SonicMaxConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 1),
    _SonicMaxConnCacheEntries_Type()
)
sonicMaxConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicMaxConnCacheEntries.setStatus("current")
_SonicCurrentConnCacheEntries_Type = Gauge32
_SonicCurrentConnCacheEntries_Object = MibScalar
sonicCurrentConnCacheEntries = _SonicCurrentConnCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 2),
    _SonicCurrentConnCacheEntries_Type()
)
sonicCurrentConnCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentConnCacheEntries.setStatus("current")
_SonicCurrentCPUUtil_Type = Gauge32
_SonicCurrentCPUUtil_Object = MibScalar
sonicCurrentCPUUtil = _SonicCurrentCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 3),
    _SonicCurrentCPUUtil_Type()
)
sonicCurrentCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentCPUUtil.setStatus("current")
_SonicCurrentRAMUtil_Type = Gauge32
_SonicCurrentRAMUtil_Object = MibScalar
sonicCurrentRAMUtil = _SonicCurrentRAMUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 4),
    _SonicCurrentRAMUtil_Type()
)
sonicCurrentRAMUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentRAMUtil.setStatus("current")
_SonicNatTranslationCount_Type = Gauge32
_SonicNatTranslationCount_Object = MibScalar
sonicNatTranslationCount = _SonicNatTranslationCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 5),
    _SonicNatTranslationCount_Type()
)
sonicNatTranslationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicNatTranslationCount.setStatus("current")
_SonicCurrentManagementCPUUtil_Type = Gauge32
_SonicCurrentManagementCPUUtil_Object = MibScalar
sonicCurrentManagementCPUUtil = _SonicCurrentManagementCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 6),
    _SonicCurrentManagementCPUUtil_Type()
)
sonicCurrentManagementCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentManagementCPUUtil.setStatus("current")
_SonicCurrentFwdAndInspectCPUUtil_Type = Gauge32
_SonicCurrentFwdAndInspectCPUUtil_Object = MibScalar
sonicCurrentFwdAndInspectCPUUtil = _SonicCurrentFwdAndInspectCPUUtil_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 7),
    _SonicCurrentFwdAndInspectCPUUtil_Type()
)
sonicCurrentFwdAndInspectCPUUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicCurrentFwdAndInspectCPUUtil.setStatus("current")
_SonicIfStatTable_Object = MibTable
sonicIfStatTable = _SonicIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    sonicIfStatTable.setStatus("current")
_SonicIfStatEntry_Object = MibTableRow
sonicIfStatEntry = _SonicIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1)
)
sonicIfStatEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIfIndex"),
)
if mibBuilder.loadTexts:
    sonicIfStatEntry.setStatus("current")
_SonicIfIndex_Type = Integer32
_SonicIfIndex_Object = MibTableColumn
sonicIfIndex = _SonicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 1),
    _SonicIfIndex_Type()
)
sonicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfIndex.setStatus("current")
_SonicIfUsage_Type = Integer32
_SonicIfUsage_Object = MibTableColumn
sonicIfUsage = _SonicIfUsage_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 2),
    _SonicIfUsage_Type()
)
sonicIfUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfUsage.setStatus("current")
_SonicIfThroughput_Type = Integer32
_SonicIfThroughput_Object = MibTableColumn
sonicIfThroughput = _SonicIfThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 1, 8, 1, 3),
    _SonicIfThroughput_Type()
)
sonicIfThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIfThroughput.setStatus("current")
_SonicwallFwVPNStats_ObjectIdentity = ObjectIdentity
sonicwallFwVPNStats = _SonicwallFwVPNStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2)
)
_SonicwallFwVpnIPSecStats_ObjectIdentity = ObjectIdentity
sonicwallFwVpnIPSecStats = _SonicwallFwVpnIPSecStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1)
)
_SonicSAStatTable_Object = MibTable
sonicSAStatTable = _SonicSAStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sonicSAStatTable.setStatus("current")
_SonicSAStatEntry_Object = MibTableRow
sonicSAStatEntry = _SonicSAStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1)
)
sonicSAStatEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicIpsecSaIndex"),
)
if mibBuilder.loadTexts:
    sonicSAStatEntry.setStatus("current")
_SonicIpsecSaIndex_Type = Counter32
_SonicIpsecSaIndex_Object = MibTableColumn
sonicIpsecSaIndex = _SonicIpsecSaIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 1),
    _SonicIpsecSaIndex_Type()
)
sonicIpsecSaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicIpsecSaIndex.setStatus("current")
_SonicSAStatPeerGateway_Type = IpAddress
_SonicSAStatPeerGateway_Object = MibTableColumn
sonicSAStatPeerGateway = _SonicSAStatPeerGateway_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 2),
    _SonicSAStatPeerGateway_Type()
)
sonicSAStatPeerGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatPeerGateway.setStatus("current")
_SonicSAStatSrcAddrBegin_Type = IpAddress
_SonicSAStatSrcAddrBegin_Object = MibTableColumn
sonicSAStatSrcAddrBegin = _SonicSAStatSrcAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 3),
    _SonicSAStatSrcAddrBegin_Type()
)
sonicSAStatSrcAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrBegin.setStatus("current")
_SonicSAStatSrcAddrEnd_Type = IpAddress
_SonicSAStatSrcAddrEnd_Object = MibTableColumn
sonicSAStatSrcAddrEnd = _SonicSAStatSrcAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 4),
    _SonicSAStatSrcAddrEnd_Type()
)
sonicSAStatSrcAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatSrcAddrEnd.setStatus("current")
_SonicSAStatDstAddrBegin_Type = IpAddress
_SonicSAStatDstAddrBegin_Object = MibTableColumn
sonicSAStatDstAddrBegin = _SonicSAStatDstAddrBegin_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 5),
    _SonicSAStatDstAddrBegin_Type()
)
sonicSAStatDstAddrBegin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrBegin.setStatus("current")
_SonicSAStatDstAddrEnd_Type = IpAddress
_SonicSAStatDstAddrEnd_Object = MibTableColumn
sonicSAStatDstAddrEnd = _SonicSAStatDstAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 6),
    _SonicSAStatDstAddrEnd_Type()
)
sonicSAStatDstAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDstAddrEnd.setStatus("current")
_SonicSAStatCreateTime_Type = DisplayString
_SonicSAStatCreateTime_Object = MibTableColumn
sonicSAStatCreateTime = _SonicSAStatCreateTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 7),
    _SonicSAStatCreateTime_Type()
)
sonicSAStatCreateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatCreateTime.setStatus("current")
_SonicSAStatEncryptPktCount_Type = Counter32
_SonicSAStatEncryptPktCount_Object = MibTableColumn
sonicSAStatEncryptPktCount = _SonicSAStatEncryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 8),
    _SonicSAStatEncryptPktCount_Type()
)
sonicSAStatEncryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptPktCount.setStatus("current")
_SonicSAStatEncryptByteCount_Type = Counter32
_SonicSAStatEncryptByteCount_Object = MibTableColumn
sonicSAStatEncryptByteCount = _SonicSAStatEncryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 9),
    _SonicSAStatEncryptByteCount_Type()
)
sonicSAStatEncryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatEncryptByteCount.setStatus("current")
_SonicSAStatDecryptPktCount_Type = Counter32
_SonicSAStatDecryptPktCount_Object = MibTableColumn
sonicSAStatDecryptPktCount = _SonicSAStatDecryptPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 10),
    _SonicSAStatDecryptPktCount_Type()
)
sonicSAStatDecryptPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptPktCount.setStatus("current")
_SonicSAStatDecryptByteCount_Type = Counter32
_SonicSAStatDecryptByteCount_Object = MibTableColumn
sonicSAStatDecryptByteCount = _SonicSAStatDecryptByteCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 11),
    _SonicSAStatDecryptByteCount_Type()
)
sonicSAStatDecryptByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatDecryptByteCount.setStatus("current")
_SonicSAStatInFragPktCount_Type = Counter32
_SonicSAStatInFragPktCount_Object = MibTableColumn
sonicSAStatInFragPktCount = _SonicSAStatInFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 12),
    _SonicSAStatInFragPktCount_Type()
)
sonicSAStatInFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatInFragPktCount.setStatus("current")
_SonicSAStatOutFragPktCount_Type = Counter32
_SonicSAStatOutFragPktCount_Object = MibTableColumn
sonicSAStatOutFragPktCount = _SonicSAStatOutFragPktCount_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 13),
    _SonicSAStatOutFragPktCount_Type()
)
sonicSAStatOutFragPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatOutFragPktCount.setStatus("current")
_SonicSAStatUserName_Type = DisplayString
_SonicSAStatUserName_Object = MibTableColumn
sonicSAStatUserName = _SonicSAStatUserName_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 2, 1, 1, 1, 14),
    _SonicSAStatUserName_Type()
)
sonicSAStatUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSAStatUserName.setStatus("current")
_SonicwallFwHWStats_ObjectIdentity = ObjectIdentity
sonicwallFwHWStats = _SonicwallFwHWStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3)
)
_SonicwallFwHWSensorStats_ObjectIdentity = ObjectIdentity
sonicwallFwHWSensorStats = _SonicwallFwHWSensorStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3)
)
_SonicwallSensorsTable_Object = MibTable
sonicwallSensorsTable = _SonicwallSensorsTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    sonicwallSensorsTable.setStatus("current")
_SonicwallSensorsEntry_Object = MibTableRow
sonicwallSensorsEntry = _SonicwallSensorsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1)
)
sonicwallSensorsEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicwallSensorsIndex"),
)
if mibBuilder.loadTexts:
    sonicwallSensorsEntry.setStatus("current")


class _SonicwallSensorsIndex_Type(Integer32):
    """Custom type sonicwallSensorsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicwallSensorsIndex_Type.__name__ = "Integer32"
_SonicwallSensorsIndex_Object = MibTableColumn
sonicwallSensorsIndex = _SonicwallSensorsIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 1),
    _SonicwallSensorsIndex_Type()
)
sonicwallSensorsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsIndex.setStatus("current")


class _SonicwallSensorsId_Type(Integer32):
    """Custom type sonicwallSensorsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicwallSensorsId_Type.__name__ = "Integer32"
_SonicwallSensorsId_Object = MibTableColumn
sonicwallSensorsId = _SonicwallSensorsId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 2),
    _SonicwallSensorsId_Type()
)
sonicwallSensorsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsId.setStatus("current")


class _SonicwallSensorsDevice_Type(DisplayString):
    """Custom type sonicwallSensorsDevice based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SonicwallSensorsDevice_Type.__name__ = "DisplayString"
_SonicwallSensorsDevice_Object = MibTableColumn
sonicwallSensorsDevice = _SonicwallSensorsDevice_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 3),
    _SonicwallSensorsDevice_Type()
)
sonicwallSensorsDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsDevice.setStatus("current")
_SonicwallSensorsValue_Type = Integer32
_SonicwallSensorsValue_Object = MibTableColumn
sonicwallSensorsValue = _SonicwallSensorsValue_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 4),
    _SonicwallSensorsValue_Type()
)
sonicwallSensorsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsValue.setStatus("current")


class _SonicwallSensorsUnit_Type(DisplayString):
    """Custom type sonicwallSensorsUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SonicwallSensorsUnit_Type.__name__ = "DisplayString"
_SonicwallSensorsUnit_Object = MibTableColumn
sonicwallSensorsUnit = _SonicwallSensorsUnit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 3, 3, 1, 1, 5),
    _SonicwallSensorsUnit_Type()
)
sonicwallSensorsUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicwallSensorsUnit.setStatus("current")
_SonicwallFwSyslogStats_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogStats = _SonicwallFwSyslogStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4)
)
_SonicwallFwSyslogSetting_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogSetting = _SonicwallFwSyslogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1)
)
_SonicSyslogFacility_Type = SyslogFacility
_SonicSyslogFacility_Object = MibScalar
sonicSyslogFacility = _SonicSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 1),
    _SonicSyslogFacility_Type()
)
sonicSyslogFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogFacility.setStatus("current")
_SonicSyslogOverrideSetting_Type = TruthValue
_SonicSyslogOverrideSetting_Object = MibScalar
sonicSyslogOverrideSetting = _SonicSyslogOverrideSetting_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 2),
    _SonicSyslogOverrideSetting_Type()
)
sonicSyslogOverrideSetting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogOverrideSetting.setStatus("current")


class _SonicSyslogFormat_Type(Integer32):
    """Custom type sonicSyslogFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("arcSight", 3),
          ("default", 0),
          ("enhSyslog", 2),
          ("webTrends", 1))
    )


_SonicSyslogFormat_Type.__name__ = "Integer32"
_SonicSyslogFormat_Object = MibScalar
sonicSyslogFormat = _SonicSyslogFormat_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 3),
    _SonicSyslogFormat_Type()
)
sonicSyslogFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogFormat.setStatus("current")


class _SonicSyslogID_Type(DisplayString):
    """Custom type sonicSyslogID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SonicSyslogID_Type.__name__ = "DisplayString"
_SonicSyslogID_Object = MibScalar
sonicSyslogID = _SonicSyslogID_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 4),
    _SonicSyslogID_Type()
)
sonicSyslogID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogID.setStatus("current")
_SonicSyslogEventRateLimitEnable_Type = TruthValue
_SonicSyslogEventRateLimitEnable_Object = MibScalar
sonicSyslogEventRateLimitEnable = _SonicSyslogEventRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 5),
    _SonicSyslogEventRateLimitEnable_Type()
)
sonicSyslogEventRateLimitEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogEventRateLimitEnable.setStatus("current")
_SonicSyslogEventRateLimit_Type = Gauge32
_SonicSyslogEventRateLimit_Object = MibScalar
sonicSyslogEventRateLimit = _SonicSyslogEventRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 6),
    _SonicSyslogEventRateLimit_Type()
)
sonicSyslogEventRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogEventRateLimit.setStatus("current")
_SonicSyslogDataRateLimitEnable_Type = TruthValue
_SonicSyslogDataRateLimitEnable_Object = MibScalar
sonicSyslogDataRateLimitEnable = _SonicSyslogDataRateLimitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 7),
    _SonicSyslogDataRateLimitEnable_Type()
)
sonicSyslogDataRateLimitEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogDataRateLimitEnable.setStatus("current")
_SonicSyslogDataRateLimit_Type = Gauge32
_SonicSyslogDataRateLimit_Object = MibScalar
sonicSyslogDataRateLimit = _SonicSyslogDataRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 8),
    _SonicSyslogDataRateLimit_Type()
)
sonicSyslogDataRateLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogDataRateLimit.setStatus("current")
_SonicSyslogNDPPEnable_Type = TruthValue
_SonicSyslogNDPPEnable_Object = MibScalar
sonicSyslogNDPPEnable = _SonicSyslogNDPPEnable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 1, 9),
    _SonicSyslogNDPPEnable_Type()
)
sonicSyslogNDPPEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogNDPPEnable.setStatus("current")
_SonicwallFwSyslogServer_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogServer = _SonicwallFwSyslogServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2)
)
_SonicSyslogMaxServers_Type = Unsigned32
_SonicSyslogMaxServers_Object = MibScalar
sonicSyslogMaxServers = _SonicSyslogMaxServers_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 1),
    _SonicSyslogMaxServers_Type()
)
sonicSyslogMaxServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogMaxServers.setStatus("current")
_SonicSyslogServerTable_Object = MibTable
sonicSyslogServerTable = _SonicSyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    sonicSyslogServerTable.setStatus("current")
_SonicSyslogServerEntry_Object = MibTableRow
sonicSyslogServerEntry = _SonicSyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1)
)
sonicSyslogServerEntry.setIndexNames(
    (0, "SONICWALL-FIREWALL-IP-STATISTICS-MIB", "sonicSyslogServerIndex"),
)
if mibBuilder.loadTexts:
    sonicSyslogServerEntry.setStatus("current")
_SonicSyslogServerIndex_Type = Integer32
_SonicSyslogServerIndex_Object = MibTableColumn
sonicSyslogServerIndex = _SonicSyslogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 1),
    _SonicSyslogServerIndex_Type()
)
sonicSyslogServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerIndex.setStatus("current")
_SonicSyslogServerAddr_Type = IpAddress
_SonicSyslogServerAddr_Object = MibTableColumn
sonicSyslogServerAddr = _SonicSyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 2),
    _SonicSyslogServerAddr_Type()
)
sonicSyslogServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerAddr.setStatus("current")


class _SonicSyslogServerPort_Type(Integer32):
    """Custom type sonicSyslogServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonicSyslogServerPort_Type.__name__ = "Integer32"
_SonicSyslogServerPort_Object = MibTableColumn
sonicSyslogServerPort = _SonicSyslogServerPort_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 2, 2, 1, 3),
    _SonicSyslogServerPort_Type()
)
sonicSyslogServerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogServerPort.setStatus("current")
_SonicwallFwSyslogStatistic_ObjectIdentity = ObjectIdentity
sonicwallFwSyslogStatistic = _SonicwallFwSyslogStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3)
)
_SonicSyslogMessage_Type = Counter32
_SonicSyslogMessage_Object = MibScalar
sonicSyslogMessage = _SonicSyslogMessage_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 1),
    _SonicSyslogMessage_Type()
)
sonicSyslogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogMessage.setStatus("current")
_SonicSyslogStreamData_Type = Counter32
_SonicSyslogStreamData_Object = MibScalar
sonicSyslogStreamData = _SonicSyslogStreamData_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 4, 3, 2),
    _SonicSyslogStreamData_Type()
)
sonicSyslogStreamData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicSyslogStreamData.setStatus("current")
_SonicwallFwDpiSslStats_ObjectIdentity = ObjectIdentity
sonicwallFwDpiSslStats = _SonicwallFwDpiSslStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5)
)
_SonicDpiSslConnCountCur_Type = Gauge32
_SonicDpiSslConnCountCur_Object = MibScalar
sonicDpiSslConnCountCur = _SonicDpiSslConnCountCur_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 1),
    _SonicDpiSslConnCountCur_Type()
)
sonicDpiSslConnCountCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountCur.setStatus("current")
_SonicDpiSslConnCountHighWater_Type = Gauge32
_SonicDpiSslConnCountHighWater_Object = MibScalar
sonicDpiSslConnCountHighWater = _SonicDpiSslConnCountHighWater_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 2),
    _SonicDpiSslConnCountHighWater_Type()
)
sonicDpiSslConnCountHighWater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountHighWater.setStatus("current")
_SonicDpiSslConnCountMax_Type = Gauge32
_SonicDpiSslConnCountMax_Object = MibScalar
sonicDpiSslConnCountMax = _SonicDpiSslConnCountMax_Object(
    (1, 3, 6, 1, 4, 1, 8741, 1, 3, 5, 3),
    _SonicDpiSslConnCountMax_Type()
)
sonicDpiSslConnCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonicDpiSslConnCountMax.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-FIREWALL-IP-STATISTICS-MIB",
    **{"SyslogFacility": SyslogFacility,
       "sonicwallFwStatsModule": sonicwallFwStatsModule,
       "sonicwallFwStats": sonicwallFwStats,
       "sonicMaxConnCacheEntries": sonicMaxConnCacheEntries,
       "sonicCurrentConnCacheEntries": sonicCurrentConnCacheEntries,
       "sonicCurrentCPUUtil": sonicCurrentCPUUtil,
       "sonicCurrentRAMUtil": sonicCurrentRAMUtil,
       "sonicNatTranslationCount": sonicNatTranslationCount,
       "sonicCurrentManagementCPUUtil": sonicCurrentManagementCPUUtil,
       "sonicCurrentFwdAndInspectCPUUtil": sonicCurrentFwdAndInspectCPUUtil,
       "sonicIfStatTable": sonicIfStatTable,
       "sonicIfStatEntry": sonicIfStatEntry,
       "sonicIfIndex": sonicIfIndex,
       "sonicIfUsage": sonicIfUsage,
       "sonicIfThroughput": sonicIfThroughput,
       "sonicwallFwVPNStats": sonicwallFwVPNStats,
       "sonicwallFwVpnIPSecStats": sonicwallFwVpnIPSecStats,
       "sonicSAStatTable": sonicSAStatTable,
       "sonicSAStatEntry": sonicSAStatEntry,
       "sonicIpsecSaIndex": sonicIpsecSaIndex,
       "sonicSAStatPeerGateway": sonicSAStatPeerGateway,
       "sonicSAStatSrcAddrBegin": sonicSAStatSrcAddrBegin,
       "sonicSAStatSrcAddrEnd": sonicSAStatSrcAddrEnd,
       "sonicSAStatDstAddrBegin": sonicSAStatDstAddrBegin,
       "sonicSAStatDstAddrEnd": sonicSAStatDstAddrEnd,
       "sonicSAStatCreateTime": sonicSAStatCreateTime,
       "sonicSAStatEncryptPktCount": sonicSAStatEncryptPktCount,
       "sonicSAStatEncryptByteCount": sonicSAStatEncryptByteCount,
       "sonicSAStatDecryptPktCount": sonicSAStatDecryptPktCount,
       "sonicSAStatDecryptByteCount": sonicSAStatDecryptByteCount,
       "sonicSAStatInFragPktCount": sonicSAStatInFragPktCount,
       "sonicSAStatOutFragPktCount": sonicSAStatOutFragPktCount,
       "sonicSAStatUserName": sonicSAStatUserName,
       "sonicwallFwHWStats": sonicwallFwHWStats,
       "sonicwallFwHWSensorStats": sonicwallFwHWSensorStats,
       "sonicwallSensorsTable": sonicwallSensorsTable,
       "sonicwallSensorsEntry": sonicwallSensorsEntry,
       "sonicwallSensorsIndex": sonicwallSensorsIndex,
       "sonicwallSensorsId": sonicwallSensorsId,
       "sonicwallSensorsDevice": sonicwallSensorsDevice,
       "sonicwallSensorsValue": sonicwallSensorsValue,
       "sonicwallSensorsUnit": sonicwallSensorsUnit,
       "sonicwallFwSyslogStats": sonicwallFwSyslogStats,
       "sonicwallFwSyslogSetting": sonicwallFwSyslogSetting,
       "sonicSyslogFacility": sonicSyslogFacility,
       "sonicSyslogOverrideSetting": sonicSyslogOverrideSetting,
       "sonicSyslogFormat": sonicSyslogFormat,
       "sonicSyslogID": sonicSyslogID,
       "sonicSyslogEventRateLimitEnable": sonicSyslogEventRateLimitEnable,
       "sonicSyslogEventRateLimit": sonicSyslogEventRateLimit,
       "sonicSyslogDataRateLimitEnable": sonicSyslogDataRateLimitEnable,
       "sonicSyslogDataRateLimit": sonicSyslogDataRateLimit,
       "sonicSyslogNDPPEnable": sonicSyslogNDPPEnable,
       "sonicwallFwSyslogServer": sonicwallFwSyslogServer,
       "sonicSyslogMaxServers": sonicSyslogMaxServers,
       "sonicSyslogServerTable": sonicSyslogServerTable,
       "sonicSyslogServerEntry": sonicSyslogServerEntry,
       "sonicSyslogServerIndex": sonicSyslogServerIndex,
       "sonicSyslogServerAddr": sonicSyslogServerAddr,
       "sonicSyslogServerPort": sonicSyslogServerPort,
       "sonicwallFwSyslogStatistic": sonicwallFwSyslogStatistic,
       "sonicSyslogMessage": sonicSyslogMessage,
       "sonicSyslogStreamData": sonicSyslogStreamData,
       "sonicwallFwDpiSslStats": sonicwallFwDpiSslStats,
       "sonicDpiSslConnCountCur": sonicDpiSslConnCountCur,
       "sonicDpiSslConnCountHighWater": sonicDpiSslConnCountHighWater,
       "sonicDpiSslConnCountMax": sonicDpiSslConnCountMax}
)
