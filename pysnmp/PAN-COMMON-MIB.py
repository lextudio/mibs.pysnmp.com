# SNMP MIB module (PAN-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAN-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:26 2024
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

(panCommonMib,
 panModules) = mibBuilder.importSymbols(
    "PAN-GLOBAL-REG",
    "panCommonMib",
    "panModules")

(TcChassisType,) = mibBuilder.importSymbols(
    "PAN-GLOBAL-TC",
    "TcChassisType")

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


# MODULE-IDENTITY

panCommonMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 1, 1, 3)
)
panCommonMibModule.setRevisions(
        ("2014-06-30 00:00",
         "2014-09-04 00:00",
         "2014-03-06 00:00",
         "2013-03-01 00:00",
         "2011-02-09 16:10")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PanCommonConfMib_ObjectIdentity = ObjectIdentity
panCommonConfMib = _PanCommonConfMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 1)
)
if mibBuilder.loadTexts:
    panCommonConfMib.setStatus("current")
_PanCommonObjs_ObjectIdentity = ObjectIdentity
panCommonObjs = _PanCommonObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2)
)
if mibBuilder.loadTexts:
    panCommonObjs.setStatus("current")
_PanSys_ObjectIdentity = ObjectIdentity
panSys = _PanSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    panSys.setStatus("current")
_PanSysSwVersion_Type = DisplayString
_PanSysSwVersion_Object = MibScalar
panSysSwVersion = _PanSysSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 1),
    _PanSysSwVersion_Type()
)
panSysSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysSwVersion.setStatus("current")
_PanSysHwVersion_Type = DisplayString
_PanSysHwVersion_Object = MibScalar
panSysHwVersion = _PanSysHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 2),
    _PanSysHwVersion_Type()
)
panSysHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHwVersion.setStatus("current")
_PanSysSerialNumber_Type = DisplayString
_PanSysSerialNumber_Object = MibScalar
panSysSerialNumber = _PanSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 3),
    _PanSysSerialNumber_Type()
)
panSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysSerialNumber.setStatus("current")
_PanSysTimeZoneOffset_Type = Integer32
_PanSysTimeZoneOffset_Object = MibScalar
panSysTimeZoneOffset = _PanSysTimeZoneOffset_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 4),
    _PanSysTimeZoneOffset_Type()
)
panSysTimeZoneOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysTimeZoneOffset.setStatus("current")
_PanSysDaylightSaving_Type = TruthValue
_PanSysDaylightSaving_Object = MibScalar
panSysDaylightSaving = _PanSysDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 5),
    _PanSysDaylightSaving_Type()
)
panSysDaylightSaving.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysDaylightSaving.setStatus("current")
_PanSysVpnClientVersion_Type = DisplayString
_PanSysVpnClientVersion_Object = MibScalar
panSysVpnClientVersion = _PanSysVpnClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 6),
    _PanSysVpnClientVersion_Type()
)
panSysVpnClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysVpnClientVersion.setStatus("current")
_PanSysAppVersion_Type = DisplayString
_PanSysAppVersion_Object = MibScalar
panSysAppVersion = _PanSysAppVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 7),
    _PanSysAppVersion_Type()
)
panSysAppVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAppVersion.setStatus("current")
_PanSysAvVersion_Type = DisplayString
_PanSysAvVersion_Object = MibScalar
panSysAvVersion = _PanSysAvVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 8),
    _PanSysAvVersion_Type()
)
panSysAvVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysAvVersion.setStatus("current")
_PanSysThreatVersion_Type = DisplayString
_PanSysThreatVersion_Object = MibScalar
panSysThreatVersion = _PanSysThreatVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 9),
    _PanSysThreatVersion_Type()
)
panSysThreatVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysThreatVersion.setStatus("current")
_PanSysUrlFilteringVersion_Type = DisplayString
_PanSysUrlFilteringVersion_Object = MibScalar
panSysUrlFilteringVersion = _PanSysUrlFilteringVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 10),
    _PanSysUrlFilteringVersion_Type()
)
panSysUrlFilteringVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysUrlFilteringVersion.setStatus("current")
_PanSysHAState_Type = DisplayString
_PanSysHAState_Object = MibScalar
panSysHAState = _PanSysHAState_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 11),
    _PanSysHAState_Type()
)
panSysHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAState.setStatus("current")
_PanSysHAPeerState_Type = DisplayString
_PanSysHAPeerState_Object = MibScalar
panSysHAPeerState = _PanSysHAPeerState_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 12),
    _PanSysHAPeerState_Type()
)
panSysHAPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAPeerState.setStatus("current")
_PanSysHAMode_Type = DisplayString
_PanSysHAMode_Object = MibScalar
panSysHAMode = _PanSysHAMode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 13),
    _PanSysHAMode_Type()
)
panSysHAMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysHAMode.setStatus("current")
_PanSysUrlFilteringDatabase_Type = DisplayString
_PanSysUrlFilteringDatabase_Object = MibScalar
panSysUrlFilteringDatabase = _PanSysUrlFilteringDatabase_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 14),
    _PanSysUrlFilteringDatabase_Type()
)
panSysUrlFilteringDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysUrlFilteringDatabase.setStatus("current")
_PanSysGlobalProtectClientVersion_Type = DisplayString
_PanSysGlobalProtectClientVersion_Object = MibScalar
panSysGlobalProtectClientVersion = _PanSysGlobalProtectClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 15),
    _PanSysGlobalProtectClientVersion_Type()
)
panSysGlobalProtectClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysGlobalProtectClientVersion.setStatus("current")
_PanSysOpswatDatafileVersion_Type = DisplayString
_PanSysOpswatDatafileVersion_Object = MibScalar
panSysOpswatDatafileVersion = _PanSysOpswatDatafileVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 16),
    _PanSysOpswatDatafileVersion_Type()
)
panSysOpswatDatafileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysOpswatDatafileVersion.setStatus("current")
_PanSysWildfireVersion_Type = DisplayString
_PanSysWildfireVersion_Object = MibScalar
panSysWildfireVersion = _PanSysWildfireVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 17),
    _PanSysWildfireVersion_Type()
)
panSysWildfireVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysWildfireVersion.setStatus("current")
_PanSysWildfirePrivateCloudVersion_Type = DisplayString
_PanSysWildfirePrivateCloudVersion_Object = MibScalar
panSysWildfirePrivateCloudVersion = _PanSysWildfirePrivateCloudVersion_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 18),
    _PanSysWildfirePrivateCloudVersion_Type()
)
panSysWildfirePrivateCloudVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSysWildfirePrivateCloudVersion.setStatus("current")
_PanGlobalCounters_ObjectIdentity = ObjectIdentity
panGlobalCounters = _PanGlobalCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19)
)
if mibBuilder.loadTexts:
    panGlobalCounters.setStatus("current")
_PanAhoSw_Type = Counter64
_PanAhoSw_Object = MibScalar
panAhoSw = _PanAhoSw_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 1),
    _PanAhoSw_Type()
)
panAhoSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panAhoSw.setStatus("current")
_PanDfaSw_Type = Counter64
_PanDfaSw_Object = MibScalar
panDfaSw = _PanDfaSw_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 2),
    _PanDfaSw_Type()
)
panDfaSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDfaSw.setStatus("current")
_PanFlowHostServiceAllow_Type = Counter64
_PanFlowHostServiceAllow_Object = MibScalar
panFlowHostServiceAllow = _PanFlowHostServiceAllow_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 3),
    _PanFlowHostServiceAllow_Type()
)
panFlowHostServiceAllow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceAllow.setStatus("current")
_PanHaPathmonSent_Type = Counter64
_PanHaPathmonSent_Object = MibScalar
panHaPathmonSent = _PanHaPathmonSent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 4),
    _PanHaPathmonSent_Type()
)
panHaPathmonSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panHaPathmonSent.setStatus("current")
_PanAhoFpga_Type = Counter64
_PanAhoFpga_Object = MibScalar
panAhoFpga = _PanAhoFpga_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 5),
    _PanAhoFpga_Type()
)
panAhoFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panAhoFpga.setStatus("current")
_PanDfaFpga_Type = Counter64
_PanDfaFpga_Object = MibScalar
panDfaFpga = _PanDfaFpga_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 6),
    _PanDfaFpga_Type()
)
panDfaFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panDfaFpga.setStatus("current")
_PanFpgaPkt_Type = Counter64
_PanFpgaPkt_Object = MibScalar
panFpgaPkt = _PanFpgaPkt_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 7),
    _PanFpgaPkt_Type()
)
panFpgaPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFpgaPkt.setStatus("current")
_PanGlobalCountersDOSCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersDOSCounters = _PanGlobalCountersDOSCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8)
)
if mibBuilder.loadTexts:
    panGlobalCountersDOSCounters.setStatus("current")
_PanFlowDosAgMaxSessLimit_Type = Counter64
_PanFlowDosAgMaxSessLimit_Object = MibScalar
panFlowDosAgMaxSessLimit = _PanFlowDosAgMaxSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 1),
    _PanFlowDosAgMaxSessLimit_Type()
)
panFlowDosAgMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosAgMaxSessLimit.setStatus("current")
_PanFlowDosBlkNumEntries_Type = Counter64
_PanFlowDosBlkNumEntries_Object = MibScalar
panFlowDosBlkNumEntries = _PanFlowDosBlkNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 2),
    _PanFlowDosBlkNumEntries_Type()
)
panFlowDosBlkNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosBlkNumEntries.setStatus("current")
_PanFlowDosClMaxSessLimit_Type = Counter64
_PanFlowDosClMaxSessLimit_Object = MibScalar
panFlowDosClMaxSessLimit = _PanFlowDosClMaxSessLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 3),
    _PanFlowDosClMaxSessLimit_Type()
)
panFlowDosClMaxSessLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClMaxSessLimit.setStatus("current")
_PanFlowDosClSyncookieAckErr_Type = Counter64
_PanFlowDosClSyncookieAckErr_Object = MibScalar
panFlowDosClSyncookieAckErr = _PanFlowDosClSyncookieAckErr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 4),
    _PanFlowDosClSyncookieAckErr_Type()
)
panFlowDosClSyncookieAckErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieAckErr.setStatus("current")
_PanFlowDosClSyncookieAckRcv_Type = Counter64
_PanFlowDosClSyncookieAckRcv_Object = MibScalar
panFlowDosClSyncookieAckRcv = _PanFlowDosClSyncookieAckRcv_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 5),
    _PanFlowDosClSyncookieAckRcv_Type()
)
panFlowDosClSyncookieAckRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieAckRcv.setStatus("current")
_PanFlowDosClSyncookieBlkDur_Type = Counter64
_PanFlowDosClSyncookieBlkDur_Object = MibScalar
panFlowDosClSyncookieBlkDur = _PanFlowDosClSyncookieBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 6),
    _PanFlowDosClSyncookieBlkDur_Type()
)
panFlowDosClSyncookieBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieBlkDur.setStatus("current")
_PanFlowDosClSyncookieMax_Type = Counter64
_PanFlowDosClSyncookieMax_Object = MibScalar
panFlowDosClSyncookieMax = _PanFlowDosClSyncookieMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 7),
    _PanFlowDosClSyncookieMax_Type()
)
panFlowDosClSyncookieMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieMax.setStatus("current")
_PanFlowDosClSyncookieSent_Type = Counter64
_PanFlowDosClSyncookieSent_Object = MibScalar
panFlowDosClSyncookieSent = _PanFlowDosClSyncookieSent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 8),
    _PanFlowDosClSyncookieSent_Type()
)
panFlowDosClSyncookieSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosClSyncookieSent.setStatus("current")
_PanFlowMeterVsysThrottle_Type = Counter64
_PanFlowMeterVsysThrottle_Object = MibScalar
panFlowMeterVsysThrottle = _PanFlowMeterVsysThrottle_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 9),
    _PanFlowMeterVsysThrottle_Type()
)
panFlowMeterVsysThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowMeterVsysThrottle.setStatus("current")
_PanFlowPolicyDeny_Type = Counter64
_PanFlowPolicyDeny_Object = MibScalar
panFlowPolicyDeny = _PanFlowPolicyDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 10),
    _PanFlowPolicyDeny_Type()
)
panFlowPolicyDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowPolicyDeny.setStatus("current")
_PanFlowPolicyNat_Type = Counter64
_PanFlowPolicyNat_Object = MibScalar
panFlowPolicyNat = _PanFlowPolicyNat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 11),
    _PanFlowPolicyNat_Type()
)
panFlowPolicyNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowPolicyNat.setStatus("current")
_PanFlowScanDrop_Type = Counter64
_PanFlowScanDrop_Object = MibScalar
panFlowScanDrop = _PanFlowScanDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 12),
    _PanFlowScanDrop_Type()
)
panFlowScanDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowScanDrop.setStatus("current")
_PanFlowDosDropIpBlocked_Type = Counter64
_PanFlowDosDropIpBlocked_Object = MibScalar
panFlowDosDropIpBlocked = _PanFlowDosDropIpBlocked_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 13),
    _PanFlowDosDropIpBlocked_Type()
)
panFlowDosDropIpBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosDropIpBlocked.setStatus("current")
_PanFlowDosRedIcmp_Type = Counter64
_PanFlowDosRedIcmp_Object = MibScalar
panFlowDosRedIcmp = _PanFlowDosRedIcmp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 14),
    _PanFlowDosRedIcmp_Type()
)
panFlowDosRedIcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIcmp.setStatus("current")
_PanFlowDosRedIcmp6_Type = Counter64
_PanFlowDosRedIcmp6_Object = MibScalar
panFlowDosRedIcmp6 = _PanFlowDosRedIcmp6_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 15),
    _PanFlowDosRedIcmp6_Type()
)
panFlowDosRedIcmp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIcmp6.setStatus("current")
_PanFlowDosRedIp_Type = Counter64
_PanFlowDosRedIp_Object = MibScalar
panFlowDosRedIp = _PanFlowDosRedIp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 16),
    _PanFlowDosRedIp_Type()
)
panFlowDosRedIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedIp.setStatus("current")
_PanFlowDosRedTcp_Type = Counter64
_PanFlowDosRedTcp_Object = MibScalar
panFlowDosRedTcp = _PanFlowDosRedTcp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 17),
    _PanFlowDosRedTcp_Type()
)
panFlowDosRedTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedTcp.setStatus("current")
_PanFlowDosRedUdp_Type = Counter64
_PanFlowDosRedUdp_Object = MibScalar
panFlowDosRedUdp = _PanFlowDosRedUdp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 18),
    _PanFlowDosRedUdp_Type()
)
panFlowDosRedUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRedUdp.setStatus("current")
_PanFlowDosRuleAgBlkDur_Type = Counter64
_PanFlowDosRuleAgBlkDur_Object = MibScalar
panFlowDosRuleAgBlkDur = _PanFlowDosRuleAgBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 19),
    _PanFlowDosRuleAgBlkDur_Type()
)
panFlowDosRuleAgBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgBlkDur.setStatus("current")
_PanFlowDosRuleAgRedAct_Type = Counter64
_PanFlowDosRuleAgRedAct_Object = MibScalar
panFlowDosRuleAgRedAct = _PanFlowDosRuleAgRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 20),
    _PanFlowDosRuleAgRedAct_Type()
)
panFlowDosRuleAgRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgRedAct.setStatus("current")
_PanFlowDosRuleAgRedMax_Type = Counter64
_PanFlowDosRuleAgRedMax_Object = MibScalar
panFlowDosRuleAgRedMax = _PanFlowDosRuleAgRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 21),
    _PanFlowDosRuleAgRedMax_Type()
)
panFlowDosRuleAgRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleAgRedMax.setStatus("current")
_PanFlowDosRuleDeny_Type = Counter64
_PanFlowDosRuleDeny_Object = MibScalar
panFlowDosRuleDeny = _PanFlowDosRuleDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 22),
    _PanFlowDosRuleDeny_Type()
)
panFlowDosRuleDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDeny.setStatus("current")
_PanFlowDosRuleDrop_Type = Counter64
_PanFlowDosRuleDrop_Object = MibScalar
panFlowDosRuleDrop = _PanFlowDosRuleDrop_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 23),
    _PanFlowDosRuleDrop_Type()
)
panFlowDosRuleDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDrop.setStatus("current")
_PanFlowDosRuleDropAggr_Type = Counter64
_PanFlowDosRuleDropAggr_Object = MibScalar
panFlowDosRuleDropAggr = _PanFlowDosRuleDropAggr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 24),
    _PanFlowDosRuleDropAggr_Type()
)
panFlowDosRuleDropAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropAggr.setStatus("current")
_PanFlowDosRuleDropClBlkDur_Type = Counter64
_PanFlowDosRuleDropClBlkDur_Object = MibScalar
panFlowDosRuleDropClBlkDur = _PanFlowDosRuleDropClBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 25),
    _PanFlowDosRuleDropClBlkDur_Type()
)
panFlowDosRuleDropClBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClBlkDur.setStatus("current")
_PanFlowDosRuleDropClRedAct_Type = Counter64
_PanFlowDosRuleDropClRedAct_Object = MibScalar
panFlowDosRuleDropClRedAct = _PanFlowDosRuleDropClRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 26),
    _PanFlowDosRuleDropClRedAct_Type()
)
panFlowDosRuleDropClRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClRedAct.setStatus("current")
_PanFlowDosRuleDropClRedMax_Type = Counter64
_PanFlowDosRuleDropClRedMax_Object = MibScalar
panFlowDosRuleDropClRedMax = _PanFlowDosRuleDropClRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 27),
    _PanFlowDosRuleDropClRedMax_Type()
)
panFlowDosRuleDropClRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClRedMax.setStatus("current")
_PanFlowDosRuleDropClassified_Type = Counter64
_PanFlowDosRuleDropClassified_Object = MibScalar
panFlowDosRuleDropClassified = _PanFlowDosRuleDropClassified_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 28),
    _PanFlowDosRuleDropClassified_Type()
)
panFlowDosRuleDropClassified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosRuleDropClassified.setStatus("current")
_PanFlowDosSyncookieBlkDur_Type = Counter64
_PanFlowDosSyncookieBlkDur_Object = MibScalar
panFlowDosSyncookieBlkDur = _PanFlowDosSyncookieBlkDur_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 29),
    _PanFlowDosSyncookieBlkDur_Type()
)
panFlowDosSyncookieBlkDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieBlkDur.setStatus("current")
_PanFlowDosSyncookieMax_Type = Counter64
_PanFlowDosSyncookieMax_Object = MibScalar
panFlowDosSyncookieMax = _PanFlowDosSyncookieMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 30),
    _PanFlowDosSyncookieMax_Type()
)
panFlowDosSyncookieMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosSyncookieMax.setStatus("current")
_PanFlowDosZoneRedAct_Type = Counter64
_PanFlowDosZoneRedAct_Object = MibScalar
panFlowDosZoneRedAct = _PanFlowDosZoneRedAct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 31),
    _PanFlowDosZoneRedAct_Type()
)
panFlowDosZoneRedAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosZoneRedAct.setStatus("current")
_PanFlowDosZoneRedMax_Type = Counter64
_PanFlowDosZoneRedMax_Object = MibScalar
panFlowDosZoneRedMax = _PanFlowDosZoneRedMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 8, 32),
    _PanFlowDosZoneRedMax_Type()
)
panFlowDosZoneRedMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowDosZoneRedMax.setStatus("current")
_PanGlobalCountersDropCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersDropCounters = _PanGlobalCountersDropCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9)
)
if mibBuilder.loadTexts:
    panGlobalCountersDropCounters.setStatus("current")
_PanFlowFwdL3TtlZero_Type = Counter64
_PanFlowFwdL3TtlZero_Object = MibScalar
panFlowFwdL3TtlZero = _PanFlowFwdL3TtlZero_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 1),
    _PanFlowFwdL3TtlZero_Type()
)
panFlowFwdL3TtlZero.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowFwdL3TtlZero.setStatus("current")
_PanFlowMeterHostThrottle_Type = Counter64
_PanFlowMeterHostThrottle_Object = MibScalar
panFlowMeterHostThrottle = _PanFlowMeterHostThrottle_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 2),
    _PanFlowMeterHostThrottle_Type()
)
panFlowMeterHostThrottle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowMeterHostThrottle.setStatus("current")
_PanFlowHostServiceDeny_Type = Counter64
_PanFlowHostServiceDeny_Object = MibScalar
panFlowHostServiceDeny = _PanFlowHostServiceDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 3),
    _PanFlowHostServiceDeny_Type()
)
panFlowHostServiceDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceDeny.setStatus("current")
_PanFlowHostServiceUnknown_Type = Counter64
_PanFlowHostServiceUnknown_Object = MibScalar
panFlowHostServiceUnknown = _PanFlowHostServiceUnknown_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 4),
    _PanFlowHostServiceUnknown_Type()
)
panFlowHostServiceUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowHostServiceUnknown.setStatus("current")
_PanPktAllocFailure_Type = Counter64
_PanPktAllocFailure_Object = MibScalar
panPktAllocFailure = _PanPktAllocFailure_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 5),
    _PanPktAllocFailure_Type()
)
panPktAllocFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panPktAllocFailure.setStatus("current")
_PanPktAllocFailureCos_Type = Counter64
_PanPktAllocFailureCos_Object = MibScalar
panPktAllocFailureCos = _PanPktAllocFailureCos_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 6),
    _PanPktAllocFailureCos_Type()
)
panPktAllocFailureCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panPktAllocFailureCos.setStatus("current")
_PanSessionDiscard_Type = Counter64
_PanSessionDiscard_Object = MibScalar
panSessionDiscard = _PanSessionDiscard_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 9, 7),
    _PanSessionDiscard_Type()
)
panSessionDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionDiscard.setStatus("current")
_PanGlobalCountersIPFragmentationCounters_ObjectIdentity = ObjectIdentity
panGlobalCountersIPFragmentationCounters = _PanGlobalCountersIPFragmentationCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10)
)
if mibBuilder.loadTexts:
    panGlobalCountersIPFragmentationCounters.setStatus("current")
_PanFlowIpfragFragErr_Type = Counter64
_PanFlowIpfragFragErr_Object = MibScalar
panFlowIpfragFragErr = _PanFlowIpfragFragErr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10, 1),
    _PanFlowIpfragFragErr_Type()
)
panFlowIpfragFragErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowIpfragFragErr.setStatus("current")
_PanFlowIpfragRecv_Type = Counter64
_PanFlowIpfragRecv_Object = MibScalar
panFlowIpfragRecv = _PanFlowIpfragRecv_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 10, 2),
    _PanFlowIpfragRecv_Type()
)
panFlowIpfragRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowIpfragRecv.setStatus("current")
_PanGlobalCountersTCPState_ObjectIdentity = ObjectIdentity
panGlobalCountersTCPState = _PanGlobalCountersTCPState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11)
)
if mibBuilder.loadTexts:
    panGlobalCountersTCPState.setStatus("current")
_PanTcpAllocWqeFailed_Type = Counter64
_PanTcpAllocWqeFailed_Object = MibScalar
panTcpAllocWqeFailed = _PanTcpAllocWqeFailed_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 1),
    _PanTcpAllocWqeFailed_Type()
)
panTcpAllocWqeFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpAllocWqeFailed.setStatus("current")
_PanTcpDeny_Type = Counter64
_PanTcpDeny_Object = MibScalar
panTcpDeny = _PanTcpDeny_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 2),
    _PanTcpDeny_Type()
)
panTcpDeny.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDeny.setStatus("current")
_PanTcpDropOutOfWnd_Type = Counter64
_PanTcpDropOutOfWnd_Object = MibScalar
panTcpDropOutOfWnd = _PanTcpDropOutOfWnd_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 3),
    _PanTcpDropOutOfWnd_Type()
)
panTcpDropOutOfWnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDropOutOfWnd.setStatus("current")
_PanTcpDropPacket_Type = Counter64
_PanTcpDropPacket_Object = MibScalar
panTcpDropPacket = _PanTcpDropPacket_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 4),
    _PanTcpDropPacket_Type()
)
panTcpDropPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpDropPacket.setStatus("current")
_PanFlowActionClose_Type = Counter64
_PanFlowActionClose_Object = MibScalar
panFlowActionClose = _PanFlowActionClose_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 5),
    _PanFlowActionClose_Type()
)
panFlowActionClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowActionClose.setStatus("current")
_PanFlowActionReset_Type = Counter64
_PanFlowActionReset_Object = MibScalar
panFlowActionReset = _PanFlowActionReset_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 6),
    _PanFlowActionReset_Type()
)
panFlowActionReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowActionReset.setStatus("current")
_PanFlowTcpNonSyn_Type = Counter64
_PanFlowTcpNonSyn_Object = MibScalar
panFlowTcpNonSyn = _PanFlowTcpNonSyn_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 7),
    _PanFlowTcpNonSyn_Type()
)
panFlowTcpNonSyn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panFlowTcpNonSyn.setStatus("current")
_PanTcpExceedSegLimit_Type = Counter64
_PanTcpExceedSegLimit_Object = MibScalar
panTcpExceedSegLimit = _PanTcpExceedSegLimit_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 1, 19, 11, 8),
    _PanTcpExceedSegLimit_Type()
)
panTcpExceedSegLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panTcpExceedSegLimit.setStatus("current")
_PanChassis_ObjectIdentity = ObjectIdentity
panChassis = _PanChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    panChassis.setStatus("current")
_PanChassisType_Type = DisplayString
_PanChassisType_Object = MibScalar
panChassisType = _PanChassisType_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2, 1),
    _PanChassisType_Type()
)
panChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panChassisType.setStatus("current")
_PanMSeriesMode_Type = DisplayString
_PanMSeriesMode_Object = MibScalar
panMSeriesMode = _PanMSeriesMode_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 2, 2),
    _PanMSeriesMode_Type()
)
panMSeriesMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMSeriesMode.setStatus("current")
_PanSession_ObjectIdentity = ObjectIdentity
panSession = _PanSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    panSession.setStatus("current")
_PanSessionUtilization_Type = Integer32
_PanSessionUtilization_Object = MibScalar
panSessionUtilization = _PanSessionUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 1),
    _PanSessionUtilization_Type()
)
panSessionUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionUtilization.setStatus("current")
_PanSessionMax_Type = Integer32
_PanSessionMax_Object = MibScalar
panSessionMax = _PanSessionMax_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 2),
    _PanSessionMax_Type()
)
panSessionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionMax.setStatus("current")
_PanSessionActive_Type = Integer32
_PanSessionActive_Object = MibScalar
panSessionActive = _PanSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 3),
    _PanSessionActive_Type()
)
panSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActive.setStatus("current")
_PanSessionActiveTcp_Type = Integer32
_PanSessionActiveTcp_Object = MibScalar
panSessionActiveTcp = _PanSessionActiveTcp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 4),
    _PanSessionActiveTcp_Type()
)
panSessionActiveTcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveTcp.setStatus("current")
_PanSessionActiveUdp_Type = Integer32
_PanSessionActiveUdp_Object = MibScalar
panSessionActiveUdp = _PanSessionActiveUdp_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 5),
    _PanSessionActiveUdp_Type()
)
panSessionActiveUdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveUdp.setStatus("current")
_PanSessionActiveICMP_Type = Integer32
_PanSessionActiveICMP_Object = MibScalar
panSessionActiveICMP = _PanSessionActiveICMP_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 6),
    _PanSessionActiveICMP_Type()
)
panSessionActiveICMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveICMP.setStatus("current")
_PanSessionActiveSslProxy_Type = Integer32
_PanSessionActiveSslProxy_Object = MibScalar
panSessionActiveSslProxy = _PanSessionActiveSslProxy_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 7),
    _PanSessionActiveSslProxy_Type()
)
panSessionActiveSslProxy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionActiveSslProxy.setStatus("current")
_PanSessionSslProxyUtilization_Type = Integer32
_PanSessionSslProxyUtilization_Object = MibScalar
panSessionSslProxyUtilization = _PanSessionSslProxyUtilization_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 8),
    _PanSessionSslProxyUtilization_Type()
)
panSessionSslProxyUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panSessionSslProxyUtilization.setStatus("current")
_PanVsysTable_Object = MibTable
panVsysTable = _PanVsysTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9)
)
if mibBuilder.loadTexts:
    panVsysTable.setStatus("current")
_PanVsysEntry_Object = MibTableRow
panVsysEntry = _PanVsysEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1)
)
panVsysEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panVsysId"),
)
if mibBuilder.loadTexts:
    panVsysEntry.setStatus("current")
_PanVsysId_Type = Integer32
_PanVsysId_Object = MibTableColumn
panVsysId = _PanVsysId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 1),
    _PanVsysId_Type()
)
panVsysId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysId.setStatus("current")
_PanVsysName_Type = DisplayString
_PanVsysName_Object = MibTableColumn
panVsysName = _PanVsysName_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 2),
    _PanVsysName_Type()
)
panVsysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysName.setStatus("current")
_PanVsysSessionUtilizationPct_Type = Integer32
_PanVsysSessionUtilizationPct_Object = MibTableColumn
panVsysSessionUtilizationPct = _PanVsysSessionUtilizationPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 3),
    _PanVsysSessionUtilizationPct_Type()
)
panVsysSessionUtilizationPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysSessionUtilizationPct.setStatus("current")
_PanVsysActiveSessions_Type = Integer32
_PanVsysActiveSessions_Object = MibTableColumn
panVsysActiveSessions = _PanVsysActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 4),
    _PanVsysActiveSessions_Type()
)
panVsysActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysActiveSessions.setStatus("current")
_PanVsysMaxSessions_Type = Integer32
_PanVsysMaxSessions_Object = MibTableColumn
panVsysMaxSessions = _PanVsysMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 3, 9, 1, 5),
    _PanVsysMaxSessions_Type()
)
panVsysMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panVsysMaxSessions.setStatus("current")
_PanMgmt_ObjectIdentity = ObjectIdentity
panMgmt = _PanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    panMgmt.setStatus("current")
_PanMgmtPanoramaConnected_Type = DisplayString
_PanMgmtPanoramaConnected_Object = MibScalar
panMgmtPanoramaConnected = _PanMgmtPanoramaConnected_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4, 1),
    _PanMgmtPanoramaConnected_Type()
)
panMgmtPanoramaConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMgmtPanoramaConnected.setStatus("current")
_PanMgmtPanorama2Connected_Type = DisplayString
_PanMgmtPanorama2Connected_Object = MibScalar
panMgmtPanorama2Connected = _PanMgmtPanorama2Connected_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 4, 2),
    _PanMgmtPanorama2Connected_Type()
)
panMgmtPanorama2Connected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panMgmtPanorama2Connected.setStatus("current")
_PanGlobalProtect_ObjectIdentity = ObjectIdentity
panGlobalProtect = _PanGlobalProtect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    panGlobalProtect.setStatus("current")
_PanGPGatewayUtilization_ObjectIdentity = ObjectIdentity
panGPGatewayUtilization = _PanGPGatewayUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    panGPGatewayUtilization.setStatus("current")
_PanGPGWUtilizationPct_Type = Integer32
_PanGPGWUtilizationPct_Object = MibScalar
panGPGWUtilizationPct = _PanGPGWUtilizationPct_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 1),
    _PanGPGWUtilizationPct_Type()
)
panGPGWUtilizationPct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationPct.setStatus("current")
_PanGPGWUtilizationMaxTunnels_Type = Integer32
_PanGPGWUtilizationMaxTunnels_Object = MibScalar
panGPGWUtilizationMaxTunnels = _PanGPGWUtilizationMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 2),
    _PanGPGWUtilizationMaxTunnels_Type()
)
panGPGWUtilizationMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationMaxTunnels.setStatus("current")
_PanGPGWUtilizationActiveTunnels_Type = Integer32
_PanGPGWUtilizationActiveTunnels_Object = MibScalar
panGPGWUtilizationActiveTunnels = _PanGPGWUtilizationActiveTunnels_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 5, 1, 3),
    _PanGPGWUtilizationActiveTunnels_Type()
)
panGPGWUtilizationActiveTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panGPGWUtilizationActiveTunnels.setStatus("current")
_PanLogCollector_ObjectIdentity = ObjectIdentity
panLogCollector = _PanLogCollector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6)
)
if mibBuilder.loadTexts:
    panLogCollector.setStatus("current")
_PanLcStat_ObjectIdentity = ObjectIdentity
panLcStat = _PanLcStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    panLcStat.setStatus("current")
_PanLcLogRate_Type = Unsigned32
_PanLcLogRate_Object = MibScalar
panLcLogRate = _PanLcLogRate_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 1),
    _PanLcLogRate_Type()
)
panLcLogRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogRate.setStatus("current")
_PanLcLogDuration_ObjectIdentity = ObjectIdentity
panLcLogDuration = _PanLcLogDuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    panLcLogDuration.setStatus("current")
_PanLcLogDurationTraffic_Type = Unsigned32
_PanLcLogDurationTraffic_Object = MibScalar
panLcLogDurationTraffic = _PanLcLogDurationTraffic_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 1),
    _PanLcLogDurationTraffic_Type()
)
panLcLogDurationTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTraffic.setStatus("current")
_PanLcLogDurationConfig_Type = Unsigned32
_PanLcLogDurationConfig_Object = MibScalar
panLcLogDurationConfig = _PanLcLogDurationConfig_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 2),
    _PanLcLogDurationConfig_Type()
)
panLcLogDurationConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationConfig.setStatus("current")
_PanLcLogDurationSystem_Type = Unsigned32
_PanLcLogDurationSystem_Object = MibScalar
panLcLogDurationSystem = _PanLcLogDurationSystem_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 3),
    _PanLcLogDurationSystem_Type()
)
panLcLogDurationSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationSystem.setStatus("current")
_PanLcLogDurationThreat_Type = Unsigned32
_PanLcLogDurationThreat_Object = MibScalar
panLcLogDurationThreat = _PanLcLogDurationThreat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 4),
    _PanLcLogDurationThreat_Type()
)
panLcLogDurationThreat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThreat.setStatus("current")
_PanLcLogDurationAppstat_Type = Unsigned32
_PanLcLogDurationAppstat_Object = MibScalar
panLcLogDurationAppstat = _PanLcLogDurationAppstat_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 5),
    _PanLcLogDurationAppstat_Type()
)
panLcLogDurationAppstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAppstat.setStatus("current")
_PanLcLogDurationTrsum_Type = Unsigned32
_PanLcLogDurationTrsum_Object = MibScalar
panLcLogDurationTrsum = _PanLcLogDurationTrsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 6),
    _PanLcLogDurationTrsum_Type()
)
panLcLogDurationTrsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationTrsum.setStatus("current")
_PanLcLogDurationThsum_Type = Unsigned32
_PanLcLogDurationThsum_Object = MibScalar
panLcLogDurationThsum = _PanLcLogDurationThsum_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 7),
    _PanLcLogDurationThsum_Type()
)
panLcLogDurationThsum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationThsum.setStatus("current")
_PanLcLogDurationEvent_Type = Unsigned32
_PanLcLogDurationEvent_Object = MibScalar
panLcLogDurationEvent = _PanLcLogDurationEvent_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 8),
    _PanLcLogDurationEvent_Type()
)
panLcLogDurationEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationEvent.setStatus("current")
_PanLcLogDurationAlarm_Type = Unsigned32
_PanLcLogDurationAlarm_Object = MibScalar
panLcLogDurationAlarm = _PanLcLogDurationAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 9),
    _PanLcLogDurationAlarm_Type()
)
panLcLogDurationAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationAlarm.setStatus("current")
_PanLcLogDurationHipmatch_Type = Unsigned32
_PanLcLogDurationHipmatch_Object = MibScalar
panLcLogDurationHipmatch = _PanLcLogDurationHipmatch_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 10),
    _PanLcLogDurationHipmatch_Type()
)
panLcLogDurationHipmatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationHipmatch.setStatus("current")
_PanLcLogDurationUserid_Type = Unsigned32
_PanLcLogDurationUserid_Object = MibScalar
panLcLogDurationUserid = _PanLcLogDurationUserid_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 2, 11),
    _PanLcLogDurationUserid_Type()
)
panLcLogDurationUserid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcLogDurationUserid.setStatus("current")
_PanLcDiskUsageTable_Object = MibTable
panLcDiskUsageTable = _PanLcDiskUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3)
)
if mibBuilder.loadTexts:
    panLcDiskUsageTable.setStatus("current")
_PanLcDiskUsageEntry_Object = MibTableRow
panLcDiskUsageEntry = _PanLcDiskUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1)
)
panLcDiskUsageEntry.setIndexNames(
    (0, "PAN-COMMON-MIB", "panLcDiskUsageId"),
)
if mibBuilder.loadTexts:
    panLcDiskUsageEntry.setStatus("current")
_PanLcDiskUsageId_Type = Integer32
_PanLcDiskUsageId_Object = MibTableColumn
panLcDiskUsageId = _PanLcDiskUsageId_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1, 1),
    _PanLcDiskUsageId_Type()
)
panLcDiskUsageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsageId.setStatus("current")
_PanLcDiskUsage_Type = Unsigned32
_PanLcDiskUsage_Object = MibTableColumn
panLcDiskUsage = _PanLcDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 1, 3, 1, 2),
    _PanLcDiskUsage_Type()
)
panLcDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcDiskUsage.setStatus("current")
_PanLcIsRedundancyMember_Type = TruthValue
_PanLcIsRedundancyMember_Object = MibScalar
panLcIsRedundancyMember = _PanLcIsRedundancyMember_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 2, 6, 2),
    _PanLcIsRedundancyMember_Type()
)
panLcIsRedundancyMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    panLcIsRedundancyMember.setStatus("current")
_PanCommonEvents_ObjectIdentity = ObjectIdentity
panCommonEvents = _PanCommonEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3)
)
if mibBuilder.loadTexts:
    panCommonEvents.setStatus("current")
_PanCommonEventObjs_ObjectIdentity = ObjectIdentity
panCommonEventObjs = _PanCommonEventObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    panCommonEventObjs.setStatus("current")
_PanCommonEventDescr_Type = DisplayString
_PanCommonEventDescr_Object = MibScalar
panCommonEventDescr = _PanCommonEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 1, 1),
    _PanCommonEventDescr_Type()
)
panCommonEventDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    panCommonEventDescr.setStatus("current")
_PanCommonEventEvents_ObjectIdentity = ObjectIdentity
panCommonEventEvents = _PanCommonEventEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    panCommonEventEvents.setStatus("current")
_PanCommonEventEventsV2_ObjectIdentity = ObjectIdentity
panCommonEventEventsV2 = _PanCommonEventEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    panCommonEventEventsV2.setStatus("current")

# Managed Objects groups


# Notification objects

panCommonEventLog = NotificationType(
    (1, 3, 6, 1, 4, 1, 25461, 2, 1, 3, 2, 0, 1)
)
panCommonEventLog.setObjects(
    ("PAN-COMMON-MIB", "panCommonEventDescr")
)
if mibBuilder.loadTexts:
    panCommonEventLog.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAN-COMMON-MIB",
    **{"panCommonMibModule": panCommonMibModule,
       "panCommonConfMib": panCommonConfMib,
       "panCommonObjs": panCommonObjs,
       "panSys": panSys,
       "panSysSwVersion": panSysSwVersion,
       "panSysHwVersion": panSysHwVersion,
       "panSysSerialNumber": panSysSerialNumber,
       "panSysTimeZoneOffset": panSysTimeZoneOffset,
       "panSysDaylightSaving": panSysDaylightSaving,
       "panSysVpnClientVersion": panSysVpnClientVersion,
       "panSysAppVersion": panSysAppVersion,
       "panSysAvVersion": panSysAvVersion,
       "panSysThreatVersion": panSysThreatVersion,
       "panSysUrlFilteringVersion": panSysUrlFilteringVersion,
       "panSysHAState": panSysHAState,
       "panSysHAPeerState": panSysHAPeerState,
       "panSysHAMode": panSysHAMode,
       "panSysUrlFilteringDatabase": panSysUrlFilteringDatabase,
       "panSysGlobalProtectClientVersion": panSysGlobalProtectClientVersion,
       "panSysOpswatDatafileVersion": panSysOpswatDatafileVersion,
       "panSysWildfireVersion": panSysWildfireVersion,
       "panSysWildfirePrivateCloudVersion": panSysWildfirePrivateCloudVersion,
       "panGlobalCounters": panGlobalCounters,
       "panAhoSw": panAhoSw,
       "panDfaSw": panDfaSw,
       "panFlowHostServiceAllow": panFlowHostServiceAllow,
       "panHaPathmonSent": panHaPathmonSent,
       "panAhoFpga": panAhoFpga,
       "panDfaFpga": panDfaFpga,
       "panFpgaPkt": panFpgaPkt,
       "panGlobalCountersDOSCounters": panGlobalCountersDOSCounters,
       "panFlowDosAgMaxSessLimit": panFlowDosAgMaxSessLimit,
       "panFlowDosBlkNumEntries": panFlowDosBlkNumEntries,
       "panFlowDosClMaxSessLimit": panFlowDosClMaxSessLimit,
       "panFlowDosClSyncookieAckErr": panFlowDosClSyncookieAckErr,
       "panFlowDosClSyncookieAckRcv": panFlowDosClSyncookieAckRcv,
       "panFlowDosClSyncookieBlkDur": panFlowDosClSyncookieBlkDur,
       "panFlowDosClSyncookieMax": panFlowDosClSyncookieMax,
       "panFlowDosClSyncookieSent": panFlowDosClSyncookieSent,
       "panFlowMeterVsysThrottle": panFlowMeterVsysThrottle,
       "panFlowPolicyDeny": panFlowPolicyDeny,
       "panFlowPolicyNat": panFlowPolicyNat,
       "panFlowScanDrop": panFlowScanDrop,
       "panFlowDosDropIpBlocked": panFlowDosDropIpBlocked,
       "panFlowDosRedIcmp": panFlowDosRedIcmp,
       "panFlowDosRedIcmp6": panFlowDosRedIcmp6,
       "panFlowDosRedIp": panFlowDosRedIp,
       "panFlowDosRedTcp": panFlowDosRedTcp,
       "panFlowDosRedUdp": panFlowDosRedUdp,
       "panFlowDosRuleAgBlkDur": panFlowDosRuleAgBlkDur,
       "panFlowDosRuleAgRedAct": panFlowDosRuleAgRedAct,
       "panFlowDosRuleAgRedMax": panFlowDosRuleAgRedMax,
       "panFlowDosRuleDeny": panFlowDosRuleDeny,
       "panFlowDosRuleDrop": panFlowDosRuleDrop,
       "panFlowDosRuleDropAggr": panFlowDosRuleDropAggr,
       "panFlowDosRuleDropClBlkDur": panFlowDosRuleDropClBlkDur,
       "panFlowDosRuleDropClRedAct": panFlowDosRuleDropClRedAct,
       "panFlowDosRuleDropClRedMax": panFlowDosRuleDropClRedMax,
       "panFlowDosRuleDropClassified": panFlowDosRuleDropClassified,
       "panFlowDosSyncookieBlkDur": panFlowDosSyncookieBlkDur,
       "panFlowDosSyncookieMax": panFlowDosSyncookieMax,
       "panFlowDosZoneRedAct": panFlowDosZoneRedAct,
       "panFlowDosZoneRedMax": panFlowDosZoneRedMax,
       "panGlobalCountersDropCounters": panGlobalCountersDropCounters,
       "panFlowFwdL3TtlZero": panFlowFwdL3TtlZero,
       "panFlowMeterHostThrottle": panFlowMeterHostThrottle,
       "panFlowHostServiceDeny": panFlowHostServiceDeny,
       "panFlowHostServiceUnknown": panFlowHostServiceUnknown,
       "panPktAllocFailure": panPktAllocFailure,
       "panPktAllocFailureCos": panPktAllocFailureCos,
       "panSessionDiscard": panSessionDiscard,
       "panGlobalCountersIPFragmentationCounters": panGlobalCountersIPFragmentationCounters,
       "panFlowIpfragFragErr": panFlowIpfragFragErr,
       "panFlowIpfragRecv": panFlowIpfragRecv,
       "panGlobalCountersTCPState": panGlobalCountersTCPState,
       "panTcpAllocWqeFailed": panTcpAllocWqeFailed,
       "panTcpDeny": panTcpDeny,
       "panTcpDropOutOfWnd": panTcpDropOutOfWnd,
       "panTcpDropPacket": panTcpDropPacket,
       "panFlowActionClose": panFlowActionClose,
       "panFlowActionReset": panFlowActionReset,
       "panFlowTcpNonSyn": panFlowTcpNonSyn,
       "panTcpExceedSegLimit": panTcpExceedSegLimit,
       "panChassis": panChassis,
       "panChassisType": panChassisType,
       "panMSeriesMode": panMSeriesMode,
       "panSession": panSession,
       "panSessionUtilization": panSessionUtilization,
       "panSessionMax": panSessionMax,
       "panSessionActive": panSessionActive,
       "panSessionActiveTcp": panSessionActiveTcp,
       "panSessionActiveUdp": panSessionActiveUdp,
       "panSessionActiveICMP": panSessionActiveICMP,
       "panSessionActiveSslProxy": panSessionActiveSslProxy,
       "panSessionSslProxyUtilization": panSessionSslProxyUtilization,
       "panVsysTable": panVsysTable,
       "panVsysEntry": panVsysEntry,
       "panVsysId": panVsysId,
       "panVsysName": panVsysName,
       "panVsysSessionUtilizationPct": panVsysSessionUtilizationPct,
       "panVsysActiveSessions": panVsysActiveSessions,
       "panVsysMaxSessions": panVsysMaxSessions,
       "panMgmt": panMgmt,
       "panMgmtPanoramaConnected": panMgmtPanoramaConnected,
       "panMgmtPanorama2Connected": panMgmtPanorama2Connected,
       "panGlobalProtect": panGlobalProtect,
       "panGPGatewayUtilization": panGPGatewayUtilization,
       "panGPGWUtilizationPct": panGPGWUtilizationPct,
       "panGPGWUtilizationMaxTunnels": panGPGWUtilizationMaxTunnels,
       "panGPGWUtilizationActiveTunnels": panGPGWUtilizationActiveTunnels,
       "panLogCollector": panLogCollector,
       "panLcStat": panLcStat,
       "panLcLogRate": panLcLogRate,
       "panLcLogDuration": panLcLogDuration,
       "panLcLogDurationTraffic": panLcLogDurationTraffic,
       "panLcLogDurationConfig": panLcLogDurationConfig,
       "panLcLogDurationSystem": panLcLogDurationSystem,
       "panLcLogDurationThreat": panLcLogDurationThreat,
       "panLcLogDurationAppstat": panLcLogDurationAppstat,
       "panLcLogDurationTrsum": panLcLogDurationTrsum,
       "panLcLogDurationThsum": panLcLogDurationThsum,
       "panLcLogDurationEvent": panLcLogDurationEvent,
       "panLcLogDurationAlarm": panLcLogDurationAlarm,
       "panLcLogDurationHipmatch": panLcLogDurationHipmatch,
       "panLcLogDurationUserid": panLcLogDurationUserid,
       "panLcDiskUsageTable": panLcDiskUsageTable,
       "panLcDiskUsageEntry": panLcDiskUsageEntry,
       "panLcDiskUsageId": panLcDiskUsageId,
       "panLcDiskUsage": panLcDiskUsage,
       "panLcIsRedundancyMember": panLcIsRedundancyMember,
       "panCommonEvents": panCommonEvents,
       "panCommonEventObjs": panCommonEventObjs,
       "panCommonEventDescr": panCommonEventDescr,
       "panCommonEventEvents": panCommonEventEvents,
       "panCommonEventEventsV2": panCommonEventEventsV2,
       "panCommonEventLog": panCommonEventLog}
)
