# SNMP MIB module (CONTIVITY-TRAPS-V1-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CONTIVITY-TRAPS-V1-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:01 2024
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

(ifAdminStatus,
 ifDescr,
 ifIndex,
 ifOperStatus,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifOperStatus",
    "ifType")

(contivity,) = mibBuilder.importSymbols(
    "NEWOAK-MIB",
    "contivity")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,
 sysName,
 sysObjectID) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp",
    "sysName",
    "sysObjectID")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

contivityTrapsV1 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 0)
)
contivityTrapsV1.setRevisions(
        ("1900-05-12 20:00",
         "1900-06-28 18:00",
         "1900-06-28 21:00",
         "1900-08-10 15:00",
         "1900-06-18 22:00",
         "1901-02-27 23:00",
         "1901-03-26 23:00",
         "1901-05-10 23:00")
)


# Types definitions



class PortLocation_ces(Integer32):
    """Custom type PortLocation_ces based on Integer32"""
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
        *(("motherBoardOrSlot0", 1),
          ("slot1", 2),
          ("slot2", 3),
          ("slot3", 4),
          ("slot4", 5),
          ("slot5", 6))
    )





class IfReasonForStatus_ces(Integer32):
    """Custom type IfReasonForStatus_ces based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("idle-time-out", 2),
          ("ip-addr-chg", 3),
          ("link-down", 10),
          ("link-up", 11),
          ("no-response", 4),
          ("test-complete-failure", 9),
          ("test-complete-success", 8),
          ("testing", 7),
          ("time-limit", 6),
          ("unknown", 1),
          ("user-interaction", 5))
    )





class FirewallPolicyType_ces(Integer32):
    """Custom type FirewallPolicyType_ces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firewall", 1),
          ("nat", 2))
    )





class FirewallRuleType_ces(Integer32):
    """Custom type FirewallRuleType_ces based on Integer32"""
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
        *(("default", 4),
          ("destinationInterface", 3),
          ("over-ride", 1),
          ("sourceInterface", 2))
    )





class FirewallRuleAction_ces(Integer32):
    """Custom type FirewallRuleAction_ces based on Integer32"""
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
        *(("allow", 2),
          ("drop", 4),
          ("reject", 3),
          ("unknown", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HardwareCESTrapInfo_ObjectIdentity = ObjectIdentity
hardwareCESTrapInfo = _HardwareCESTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1)
)
_HardDisk1Status_Type = DisplayString
_HardDisk1Status_Object = MibScalar
hardDisk1Status = _HardDisk1Status_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 1),
    _HardDisk1Status_Type()
)
hardDisk1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardDisk1Status.setStatus("mandatory")
_HardDisk0Status_Type = DisplayString
_HardDisk0Status_Object = MibScalar
hardDisk0Status = _HardDisk0Status_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 2),
    _HardDisk0Status_Type()
)
hardDisk0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hardDisk0Status.setStatus("mandatory")
_MemoryUsage_Type = DisplayString
_MemoryUsage_Object = MibScalar
memoryUsage = _MemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 3),
    _MemoryUsage_Type()
)
memoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsage.setStatus("mandatory")
_LanCardStatus_Type = DisplayString
_LanCardStatus_Object = MibScalar
lanCardStatus = _LanCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 4),
    _LanCardStatus_Type()
)
lanCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lanCardStatus.setStatus("mandatory")
_CpuTwoStatus_Type = DisplayString
_CpuTwoStatus_Object = MibScalar
cpuTwoStatus = _CpuTwoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 5),
    _CpuTwoStatus_Type()
)
cpuTwoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuTwoStatus.setStatus("mandatory")
_FanOneStatus_Type = DisplayString
_FanOneStatus_Object = MibScalar
fanOneStatus = _FanOneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 6),
    _FanOneStatus_Type()
)
fanOneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanOneStatus.setStatus("mandatory")
_FanTwoStatus_Type = DisplayString
_FanTwoStatus_Object = MibScalar
fanTwoStatus = _FanTwoStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 7),
    _FanTwoStatus_Type()
)
fanTwoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanTwoStatus.setStatus("mandatory")
_ChassisFanStatus_Type = DisplayString
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 8),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("mandatory")
_FiveVoltsPositive_Type = DisplayString
_FiveVoltsPositive_Object = MibScalar
fiveVoltsPositive = _FiveVoltsPositive_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 9),
    _FiveVoltsPositive_Type()
)
fiveVoltsPositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiveVoltsPositive.setStatus("mandatory")
_FiveVoltsMinus_Type = DisplayString
_FiveVoltsMinus_Object = MibScalar
fiveVoltsMinus = _FiveVoltsMinus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 10),
    _FiveVoltsMinus_Type()
)
fiveVoltsMinus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fiveVoltsMinus.setStatus("mandatory")
_ThreeVoltsPositive_Type = DisplayString
_ThreeVoltsPositive_Object = MibScalar
threeVoltsPositive = _ThreeVoltsPositive_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 11),
    _ThreeVoltsPositive_Type()
)
threeVoltsPositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    threeVoltsPositive.setStatus("mandatory")
_TwoDotFiveVA_Type = DisplayString
_TwoDotFiveVA_Object = MibScalar
twoDotFiveVA = _TwoDotFiveVA_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 12),
    _TwoDotFiveVA_Type()
)
twoDotFiveVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twoDotFiveVA.setStatus("mandatory")
_TwoDotFiveVB_Type = DisplayString
_TwoDotFiveVB_Object = MibScalar
twoDotFiveVB = _TwoDotFiveVB_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 13),
    _TwoDotFiveVB_Type()
)
twoDotFiveVB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twoDotFiveVB.setStatus("mandatory")
_TwelveVoltsPositive_Type = DisplayString
_TwelveVoltsPositive_Object = MibScalar
twelveVoltsPositive = _TwelveVoltsPositive_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 14),
    _TwelveVoltsPositive_Type()
)
twelveVoltsPositive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twelveVoltsPositive.setStatus("mandatory")
_TwelveVoltsMinus_Type = DisplayString
_TwelveVoltsMinus_Object = MibScalar
twelveVoltsMinus = _TwelveVoltsMinus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 15),
    _TwelveVoltsMinus_Type()
)
twelveVoltsMinus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    twelveVoltsMinus.setStatus("mandatory")
_NormalTemperature_Type = DisplayString
_NormalTemperature_Object = MibScalar
normalTemperature = _NormalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 16),
    _NormalTemperature_Type()
)
normalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    normalTemperature.setStatus("mandatory")
_CriticalTemperature_Type = DisplayString
_CriticalTemperature_Object = MibScalar
criticalTemperature = _CriticalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 17),
    _CriticalTemperature_Type()
)
criticalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    criticalTemperature.setStatus("mandatory")
_ChassisIntrusion_Type = DisplayString
_ChassisIntrusion_Object = MibScalar
chassisIntrusion = _ChassisIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 18),
    _ChassisIntrusion_Type()
)
chassisIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisIntrusion.setStatus("mandatory")
_DualPowerSupply_Type = DisplayString
_DualPowerSupply_Object = MibScalar
dualPowerSupply = _DualPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 19),
    _DualPowerSupply_Type()
)
dualPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dualPowerSupply.setStatus("mandatory")
_T1WANStatus_Type = DisplayString
_T1WANStatus_Object = MibScalar
t1WANStatus = _T1WANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 20),
    _T1WANStatus_Type()
)
t1WANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t1WANStatus.setStatus("mandatory")
_T3WANStatus_Type = DisplayString
_T3WANStatus_Object = MibScalar
t3WANStatus = _T3WANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 21),
    _T3WANStatus_Type()
)
t3WANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t3WANStatus.setStatus("mandatory")
_HwAccelStatus_Type = DisplayString
_HwAccelStatus_Object = MibScalar
hwAccelStatus = _HwAccelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 22),
    _HwAccelStatus_Type()
)
hwAccelStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwAccelStatus.setStatus("mandatory")
_V90WANStatus_Type = DisplayString
_V90WANStatus_Object = MibScalar
v90WANStatus = _V90WANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 24),
    _V90WANStatus_Type()
)
v90WANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    v90WANStatus.setStatus("mandatory")
_BriWANStatus_Type = DisplayString
_BriWANStatus_Object = MibScalar
briWANStatus = _BriWANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 25),
    _BriWANStatus_Type()
)
briWANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    briWANStatus.setStatus("mandatory")
_SerUartStatus_Type = DisplayString
_SerUartStatus_Object = MibScalar
serUartStatus = _SerUartStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 26),
    _SerUartStatus_Type()
)
serUartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serUartStatus.setStatus("mandatory")
_AdslWANStatus_Type = DisplayString
_AdslWANStatus_Object = MibScalar
adslWANStatus = _AdslWANStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 27),
    _AdslWANStatus_Type()
)
adslWANStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adslWANStatus.setStatus("mandatory")
_ServerCESTrapInfo_ObjectIdentity = ObjectIdentity
serverCESTrapInfo = _ServerCESTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2)
)
_RadiusAcctServer_Type = DisplayString
_RadiusAcctServer_Object = MibScalar
radiusAcctServer = _RadiusAcctServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 1),
    _RadiusAcctServer_Type()
)
radiusAcctServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAcctServer.setStatus("mandatory")
_BackupServer_Type = DisplayString
_BackupServer_Object = MibScalar
backupServer = _BackupServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 2),
    _BackupServer_Type()
)
backupServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupServer.setStatus("mandatory")
_DiskRedundency_Type = DisplayString
_DiskRedundency_Object = MibScalar
diskRedundency = _DiskRedundency_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 3),
    _DiskRedundency_Type()
)
diskRedundency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diskRedundency.setStatus("mandatory")
_IntLDAPServer_Type = DisplayString
_IntLDAPServer_Object = MibScalar
intLDAPServer = _IntLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 4),
    _IntLDAPServer_Type()
)
intLDAPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intLDAPServer.setStatus("mandatory")
_LoadBalancingServer_Type = DisplayString
_LoadBalancingServer_Object = MibScalar
loadBalancingServer = _LoadBalancingServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 5),
    _LoadBalancingServer_Type()
)
loadBalancingServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loadBalancingServer.setStatus("mandatory")
_DnsServer_Type = DisplayString
_DnsServer_Object = MibScalar
dnsServer = _DnsServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 6),
    _DnsServer_Type()
)
dnsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServer.setStatus("mandatory")
_SnmpServer_Type = DisplayString
_SnmpServer_Object = MibScalar
snmpServer = _SnmpServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 7),
    _SnmpServer_Type()
)
snmpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpServer.setStatus("mandatory")
_IpAddressPool_Type = DisplayString
_IpAddressPool_Object = MibScalar
ipAddressPool = _IpAddressPool_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 8),
    _IpAddressPool_Type()
)
ipAddressPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAddressPool.setStatus("mandatory")
_ExtLDAPServer_Type = DisplayString
_ExtLDAPServer_Object = MibScalar
extLDAPServer = _ExtLDAPServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 9),
    _ExtLDAPServer_Type()
)
extLDAPServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLDAPServer.setStatus("mandatory")
_RadiusAuthServer_Type = DisplayString
_RadiusAuthServer_Object = MibScalar
radiusAuthServer = _RadiusAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 10),
    _RadiusAuthServer_Type()
)
radiusAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusAuthServer.setStatus("mandatory")
_CertificateServer_Type = DisplayString
_CertificateServer_Object = MibScalar
certificateServer = _CertificateServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 11),
    _CertificateServer_Type()
)
certificateServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    certificateServer.setStatus("mandatory")
_ExtLDAPAuthServer_Type = DisplayString
_ExtLDAPAuthServer_Object = MibScalar
extLDAPAuthServer = _ExtLDAPAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 12),
    _ExtLDAPAuthServer_Type()
)
extLDAPAuthServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extLDAPAuthServer.setStatus("mandatory")
_CmpServer_Type = DisplayString
_CmpServer_Object = MibScalar
cmpServer = _CmpServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 13),
    _CmpServer_Type()
)
cmpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cmpServer.setStatus("mandatory")
_DhcpServer_Type = DisplayString
_DhcpServer_Object = MibScalar
dhcpServer = _DhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 14),
    _DhcpServer_Type()
)
dhcpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpServer.setStatus("mandatory")
_SshServer_Type = DisplayString
_SshServer_Object = MibScalar
sshServer = _SshServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 15),
    _SshServer_Type()
)
sshServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServer.setStatus("mandatory")
_NtpServer_Type = DisplayString
_NtpServer_Object = MibScalar
ntpServer = _NtpServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 16),
    _NtpServer_Type()
)
ntpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServer.setStatus("mandatory")
_OspfServer_Type = DisplayString
_OspfServer_Object = MibScalar
ospfServer = _OspfServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 17),
    _OspfServer_Type()
)
ospfServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfServer.setStatus("mandatory")
_ClipServer_Type = DisplayString
_ClipServer_Object = MibScalar
clipServer = _ClipServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 18),
    _ClipServer_Type()
)
clipServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clipServer.setStatus("mandatory")
_DhcprelayServer_Type = DisplayString
_DhcprelayServer_Object = MibScalar
dhcprelayServer = _DhcprelayServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 19),
    _DhcprelayServer_Type()
)
dhcprelayServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcprelayServer.setStatus("mandatory")
_GdsServer_Type = DisplayString
_GdsServer_Object = MibScalar
gdsServer = _GdsServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 20),
    _GdsServer_Type()
)
gdsServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gdsServer.setStatus("mandatory")
_DemandintfServer_Type = DisplayString
_DemandintfServer_Object = MibScalar
demandintfServer = _DemandintfServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 21),
    _DemandintfServer_Type()
)
demandintfServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    demandintfServer.setStatus("mandatory")
_CrlServer_Type = DisplayString
_CrlServer_Object = MibScalar
crlServer = _CrlServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 22),
    _CrlServer_Type()
)
crlServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crlServer.setStatus("mandatory")
_OcspServer_Type = DisplayString
_OcspServer_Object = MibScalar
ocspServer = _OcspServer_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 23),
    _OcspServer_Type()
)
ocspServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ocspServer.setStatus("mandatory")
_ServiceCESTrapInfo_ObjectIdentity = ObjectIdentity
serviceCESTrapInfo = _ServiceCESTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3)
)
_NetBuffers_Type = DisplayString
_NetBuffers_Object = MibScalar
netBuffers = _NetBuffers_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 1),
    _NetBuffers_Type()
)
netBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netBuffers.setStatus("mandatory")
_FireWall_Type = DisplayString
_FireWall_Object = MibScalar
fireWall = _FireWall_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 2),
    _FireWall_Type()
)
fireWall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fireWall.setStatus("mandatory")
_FipsStatus_Type = DisplayString
_FipsStatus_Object = MibScalar
fipsStatus = _FipsStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 3),
    _FipsStatus_Type()
)
fipsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fipsStatus.setStatus("mandatory")
_LicensingStatus_Type = DisplayString
_LicensingStatus_Object = MibScalar
licensingStatus = _LicensingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 4),
    _LicensingStatus_Type()
)
licensingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    licensingStatus.setStatus("mandatory")
_NatStatus_Type = DisplayString
_NatStatus_Object = MibScalar
natStatus = _NatStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 5),
    _NatStatus_Type()
)
natStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    natStatus.setStatus("mandatory")
_AntiSpoofingStatus_Type = DisplayString
_AntiSpoofingStatus_Object = MibScalar
antiSpoofingStatus = _AntiSpoofingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 6),
    _AntiSpoofingStatus_Type()
)
antiSpoofingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    antiSpoofingStatus.setStatus("mandatory")
_SslVpnStatus_Type = DisplayString
_SslVpnStatus_Object = MibScalar
sslVpnStatus = _SslVpnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 7),
    _SslVpnStatus_Type()
)
sslVpnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sslVpnStatus.setStatus("mandatory")
_UsrIpAddrStatus_Type = DisplayString
_UsrIpAddrStatus_Object = MibScalar
usrIpAddrStatus = _UsrIpAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 8),
    _UsrIpAddrStatus_Type()
)
usrIpAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usrIpAddrStatus.setStatus("mandatory")
_VrrpStatus_Type = DisplayString
_VrrpStatus_Object = MibScalar
vrrpStatus = _VrrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 9),
    _VrrpStatus_Type()
)
vrrpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrrpStatus.setStatus("mandatory")
_McastRelayStatus_Type = DisplayString
_McastRelayStatus_Object = MibScalar
mcastRelayStatus = _McastRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 10),
    _McastRelayStatus_Type()
)
mcastRelayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastRelayStatus.setStatus("mandatory")
_DlswStatus_Type = DisplayString
_DlswStatus_Object = MibScalar
dlswStatus = _DlswStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 11),
    _DlswStatus_Type()
)
dlswStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dlswStatus.setStatus("mandatory")
_IpsecFailoverStatus_Type = DisplayString
_IpsecFailoverStatus_Object = MibScalar
ipsecFailoverStatus = _IpsecFailoverStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 12),
    _IpsecFailoverStatus_Type()
)
ipsecFailoverStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipsecFailoverStatus.setStatus("mandatory")
_TunnelGuardStatus_Type = DisplayString
_TunnelGuardStatus_Object = MibScalar
tunnelGuardStatus = _TunnelGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 13),
    _TunnelGuardStatus_Type()
)
tunnelGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelGuardStatus.setStatus("mandatory")
_RipStatus_Type = DisplayString
_RipStatus_Object = MibScalar
ripStatus = _RipStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 14),
    _RipStatus_Type()
)
ripStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripStatus.setStatus("mandatory")
_RoutePolicyStatus_Type = DisplayString
_RoutePolicyStatus_Object = MibScalar
routePolicyStatus = _RoutePolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 15),
    _RoutePolicyStatus_Type()
)
routePolicyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routePolicyStatus.setStatus("mandatory")
_CRoutesMStatus_Type = DisplayString
_CRoutesMStatus_Object = MibScalar
cRoutesMStatus = _CRoutesMStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 16),
    _CRoutesMStatus_Type()
)
cRoutesMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cRoutesMStatus.setStatus("mandatory")
_IgmpStatus_Type = DisplayString
_IgmpStatus_Object = MibScalar
igmpStatus = _IgmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 17),
    _IgmpStatus_Type()
)
igmpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpStatus.setStatus("mandatory")
_LoginCESTrapInfo_ObjectIdentity = ObjectIdentity
loginCESTrapInfo = _LoginCESTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 4)
)
_FailedLogin_Type = DisplayString
_FailedLogin_Object = MibScalar
failedLogin = _FailedLogin_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 4, 1),
    _FailedLogin_Type()
)
failedLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    failedLogin.setStatus("mandatory")
_IntrusionCESTrapInfo_ObjectIdentity = ObjectIdentity
intrusionCESTrapInfo = _IntrusionCESTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 5)
)
_SecurityIntrusion_Type = DisplayString
_SecurityIntrusion_Object = MibScalar
securityIntrusion = _SecurityIntrusion_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 5, 1),
    _SecurityIntrusion_Type()
)
securityIntrusion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityIntrusion.setStatus("mandatory")
_PowerUpTrap_Type = DisplayString
_PowerUpTrap_Object = MibScalar
powerUpTrap = _PowerUpTrap_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 6),
    _PowerUpTrap_Type()
)
powerUpTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerUpTrap.setStatus("deprecated")


class _SeverityLevel_Type(Integer32):
    """Custom type severityLevel based on Integer32"""
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
        *(("alert", 1),
          ("disabled", 3),
          ("healthy", 4),
          ("unknown", 5),
          ("warning", 2))
    )


_SeverityLevel_Type.__name__ = "Integer32"
_SeverityLevel_Object = MibScalar
severityLevel = _SeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 7),
    _SeverityLevel_Type()
)
severityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    severityLevel.setStatus("mandatory")
_SystemName_Type = DisplayString
_SystemName_Object = MibScalar
systemName = _SystemName_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 8),
    _SystemName_Type()
)
systemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemName.setStatus("mandatory")
_SystemDate_Type = DisplayString
_SystemDate_Object = MibScalar
systemDate = _SystemDate_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 9),
    _SystemDate_Type()
)
systemDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemDate.setStatus("mandatory")
_SystemTime_Type = DisplayString
_SystemTime_Object = MibScalar
systemTime = _SystemTime_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 10),
    _SystemTime_Type()
)
systemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemTime.setStatus("mandatory")
_SystemUpTime_Type = DisplayString
_SystemUpTime_Object = MibScalar
systemUpTime = _SystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 11),
    _SystemUpTime_Type()
)
systemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemUpTime.setStatus("mandatory")
_PeriodicHeartbeat_Type = DisplayString
_PeriodicHeartbeat_Object = MibScalar
periodicHeartbeat = _PeriodicHeartbeat_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 12),
    _PeriodicHeartbeat_Type()
)
periodicHeartbeat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    periodicHeartbeat.setStatus("mandatory")
_SnmpAgentTrapInfo_ces_ObjectIdentity = ObjectIdentity
snmpAgentTrapInfo_ces = _SnmpAgentTrapInfo_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14)
)
_SnmpAgentAuthTrapInfo_ces_ObjectIdentity = ObjectIdentity
snmpAgentAuthTrapInfo_ces = _SnmpAgentAuthTrapInfo_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 1)
)


class _SnmpAuthenOperation_ces_Type(Integer32):
    """Custom type snmpAuthenOperation_ces based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(160,
              161,
              163,
              165)
        )
    )
    namedValues = NamedValues(
        *(("getBulkRequest", 165),
          ("getNextRequest", 161),
          ("getRequest", 160),
          ("setRequest", 163))
    )


_SnmpAuthenOperation_ces_Type.__name__ = "Integer32"
_SnmpAuthenOperation_ces_Object = MibScalar
snmpAuthenOperation_ces = _SnmpAuthenOperation_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 1, 1),
    _SnmpAuthenOperation_ces_Type()
)
snmpAuthenOperation_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAuthenOperation_ces.setStatus("mandatory")
_SnmpAuthenIpAddress_ces_Type = IpAddress
_SnmpAuthenIpAddress_ces_Object = MibScalar
snmpAuthenIpAddress_ces = _SnmpAuthenIpAddress_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 1, 2),
    _SnmpAuthenIpAddress_ces_Type()
)
snmpAuthenIpAddress_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAuthenIpAddress_ces.setStatus("mandatory")
_SnmpAuthenCommString_ces_Type = DisplayString
_SnmpAuthenCommString_ces_Object = MibScalar
snmpAuthenCommString_ces = _SnmpAuthenCommString_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 1, 3),
    _SnmpAuthenCommString_ces_Type()
)
snmpAuthenCommString_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAuthenCommString_ces.setStatus("mandatory")
_SnmpAgentInterfaceInfo_ces_ObjectIdentity = ObjectIdentity
snmpAgentInterfaceInfo_ces = _SnmpAgentInterfaceInfo_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2)
)
_IfReasonForStatus_ces_Type = IfReasonForStatus_ces
_IfReasonForStatus_ces_Object = MibScalar
ifReasonForStatus_ces = _IfReasonForStatus_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 1),
    _IfReasonForStatus_ces_Type()
)
ifReasonForStatus_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifReasonForStatus_ces.setStatus("mandatory")
_IfPhysLocation_ces_Type = PortLocation_ces
_IfPhysLocation_ces_Object = MibScalar
ifPhysLocation_ces = _IfPhysLocation_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 2),
    _IfPhysLocation_ces_Type()
)
ifPhysLocation_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysLocation_ces.setStatus("mandatory")
_IfPhysRelPos_ces_Type = Integer32
_IfPhysRelPos_ces_Object = MibScalar
ifPhysRelPos_ces = _IfPhysRelPos_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 3),
    _IfPhysRelPos_ces_Type()
)
ifPhysRelPos_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysRelPos_ces.setStatus("mandatory")
_IfIpAddr_ces_Type = IpAddress
_IfIpAddr_ces_Object = MibScalar
ifIpAddr_ces = _IfIpAddr_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 4),
    _IfIpAddr_ces_Type()
)
ifIpAddr_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifIpAddr_ces.setStatus("mandatory")
_IfName_ces_Type = DisplayString
_IfName_ces_Object = MibScalar
ifName_ces = _IfName_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 5),
    _IfName_ces_Type()
)
ifName_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifName_ces.setStatus("mandatory")
_IfTunnelRemoteIpAddr_ces_Type = IpAddress
_IfTunnelRemoteIpAddr_ces_Object = MibScalar
ifTunnelRemoteIpAddr_ces = _IfTunnelRemoteIpAddr_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 2, 6),
    _IfTunnelRemoteIpAddr_ces_Type()
)
ifTunnelRemoteIpAddr_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifTunnelRemoteIpAddr_ces.setStatus("mandatory")
_SnmpAgentFirewallInfo_ces_ObjectIdentity = ObjectIdentity
snmpAgentFirewallInfo_ces = _SnmpAgentFirewallInfo_ces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3)
)
_FirewallPolicyType_ces_Type = FirewallPolicyType_ces
_FirewallPolicyType_ces_Object = MibScalar
firewallPolicyType_ces = _FirewallPolicyType_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 1),
    _FirewallPolicyType_ces_Type()
)
firewallPolicyType_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallPolicyType_ces.setStatus("mandatory")
_FirewallRuleType_ces_Type = FirewallRuleType_ces
_FirewallRuleType_ces_Object = MibScalar
firewallRuleType_ces = _FirewallRuleType_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 2),
    _FirewallRuleType_ces_Type()
)
firewallRuleType_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallRuleType_ces.setStatus("mandatory")
_FirewallRuleNumber_ces_Type = Integer32
_FirewallRuleNumber_ces_Object = MibScalar
firewallRuleNumber_ces = _FirewallRuleNumber_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 3),
    _FirewallRuleNumber_ces_Type()
)
firewallRuleNumber_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallRuleNumber_ces.setStatus("mandatory")
_FirewallSrcAddr_ces_Type = IpAddress
_FirewallSrcAddr_ces_Object = MibScalar
firewallSrcAddr_ces = _FirewallSrcAddr_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 6),
    _FirewallSrcAddr_ces_Type()
)
firewallSrcAddr_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSrcAddr_ces.setStatus("mandatory")
_FirewallSrcPort_ces_Type = Integer32
_FirewallSrcPort_ces_Object = MibScalar
firewallSrcPort_ces = _FirewallSrcPort_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 7),
    _FirewallSrcPort_ces_Type()
)
firewallSrcPort_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallSrcPort_ces.setStatus("mandatory")
_FirewallDestAddr_ces_Type = IpAddress
_FirewallDestAddr_ces_Object = MibScalar
firewallDestAddr_ces = _FirewallDestAddr_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 8),
    _FirewallDestAddr_ces_Type()
)
firewallDestAddr_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDestAddr_ces.setStatus("mandatory")
_FirewallDestPort_ces_Type = Integer32
_FirewallDestPort_ces_Object = MibScalar
firewallDestPort_ces = _FirewallDestPort_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 9),
    _FirewallDestPort_ces_Type()
)
firewallDestPort_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallDestPort_ces.setStatus("mandatory")
_FirewallProtocolID_ces_Type = Integer32
_FirewallProtocolID_ces_Object = MibScalar
firewallProtocolID_ces = _FirewallProtocolID_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 10),
    _FirewallProtocolID_ces_Type()
)
firewallProtocolID_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallProtocolID_ces.setStatus("mandatory")
_FirewallRuleAction_ces_Type = FirewallRuleAction_ces
_FirewallRuleAction_ces_Object = MibScalar
firewallRuleAction_ces = _FirewallRuleAction_ces_Object(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 11),
    _FirewallRuleAction_ces_Type()
)
firewallRuleAction_ces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firewallRuleAction_ces.setStatus("mandatory")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifReasonForStatus_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifPhysLocation_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifPhysRelPos_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifIpAddr_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifName_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifTunnelRemoteIpAddr_ces"),
        ("SNMPv2-MIB", "sysObjectID"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifReasonForStatus_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifPhysLocation_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifPhysRelPos_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifIpAddr_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifName_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifTunnelRemoteIpAddr_ces"),
        ("SNMPv2-MIB", "sysObjectID"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 5)
)
authenticationFailure.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "snmpAuthenOperation_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "snmpAuthenIpAddress_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "snmpAuthenCommString_ces"),
        ("SNMPv2-MIB", "sysObjectID"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

powerUpTrapEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 0, 401)
)
powerUpTrapEntry.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "powerUpTrap"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    powerUpTrapEntry.setStatus(
        ""
    )

periodicHeartbeatTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 0, 601)
)
periodicHeartbeatTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "periodicHeartbeat"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    periodicHeartbeatTrap.setStatus(
        ""
    )

hardDisk1StatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1001)
)
hardDisk1StatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "hardDisk1Status"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    hardDisk1StatusTrap.setStatus(
        ""
    )

hardDisk0StatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1002)
)
hardDisk0StatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "hardDisk0Status"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    hardDisk0StatusTrap.setStatus(
        ""
    )

memoryUsageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1003)
)
memoryUsageTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "memoryUsage"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    memoryUsageTrap.setStatus(
        ""
    )

lanCardStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1004)
)
lanCardStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "lanCardStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    lanCardStatusTrap.setStatus(
        ""
    )

cpuTwoStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1005)
)
cpuTwoStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "cpuTwoStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    cpuTwoStatusTrap.setStatus(
        ""
    )

fanOneStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1006)
)
fanOneStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fanOneStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fanOneStatusTrap.setStatus(
        ""
    )

fanTwoStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1007)
)
fanTwoStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fanTwoStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fanTwoStatusTrap.setStatus(
        ""
    )

chassisFanStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1008)
)
chassisFanStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "chassisFanStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    chassisFanStatusTrap.setStatus(
        ""
    )

fiveVoltsPosStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 1009)
)
fiveVoltsPosStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fiveVoltsPositive"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fiveVoltsPosStatusTrap.setStatus(
        ""
    )

fiveVoltsMinusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10010)
)
fiveVoltsMinusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fiveVoltsMinus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fiveVoltsMinusTrap.setStatus(
        ""
    )

threeVoltsPositiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10011)
)
threeVoltsPositiveTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "threeVoltsPositive"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    threeVoltsPositiveTrap.setStatus(
        ""
    )

twoDotFiveVATrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10012)
)
twoDotFiveVATrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "twoDotFiveVA"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    twoDotFiveVATrap.setStatus(
        ""
    )

twoDotFiveVBTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10013)
)
twoDotFiveVBTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "twoDotFiveVB"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    twoDotFiveVBTrap.setStatus(
        ""
    )

twelveVoltsPositveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10014)
)
twelveVoltsPositveTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "twelveVoltsPositive"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    twelveVoltsPositveTrap.setStatus(
        ""
    )

twelveVoltsMinsTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10015)
)
twelveVoltsMinsTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "twelveVoltsMinus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    twelveVoltsMinsTrap.setStatus(
        ""
    )

normalTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10016)
)
normalTemperatureTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "normalTemperature"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    normalTemperatureTrap.setStatus(
        ""
    )

criticalTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10017)
)
criticalTemperatureTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "criticalTemperature"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    criticalTemperatureTrap.setStatus(
        ""
    )

chassisIntrusionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10018)
)
chassisIntrusionTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "chassisIntrusion"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    chassisIntrusionTrap.setStatus(
        ""
    )

dualPowerSupplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10019)
)
dualPowerSupplyTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "dualPowerSupply"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    dualPowerSupplyTrap.setStatus(
        ""
    )

t1WANStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10020)
)
t1WANStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "t1WANStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    t1WANStatusTrap.setStatus(
        ""
    )

t3WANStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10021)
)
t3WANStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "t3WANStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifType"))
)
if mibBuilder.loadTexts:
    t3WANStatusTrap.setStatus(
        ""
    )

hwAccelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10022)
)
hwAccelTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "hwAccelStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    hwAccelTrap.setStatus(
        ""
    )

v90WANStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10024)
)
v90WANStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "v90WANStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    v90WANStatusTrap.setStatus(
        ""
    )

briWANStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10025)
)
briWANStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "briWANStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    briWANStatusTrap.setStatus(
        ""
    )

serUartStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10026)
)
serUartStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "serUartStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    serUartStatusTrap.setStatus(
        ""
    )

adslWANStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 1, 0, 10027)
)
adslWANStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "adslWANStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    adslWANStatusTrap.setStatus(
        ""
    )

radiusAcctServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3001)
)
radiusAcctServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "radiusAcctServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    radiusAcctServerTrap.setStatus(
        ""
    )

backupServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3002)
)
backupServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "backupServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    backupServerTrap.setStatus(
        ""
    )

diskRedundencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3003)
)
diskRedundencyTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "diskRedundency"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    diskRedundencyTrap.setStatus(
        ""
    )

intLDAPServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3004)
)
intLDAPServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "intLDAPServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    intLDAPServerTrap.setStatus(
        ""
    )

loadBalancingServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3005)
)
loadBalancingServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "loadBalancingServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    loadBalancingServerTrap.setStatus(
        ""
    )

dnsServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3006)
)
dnsServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "dnsServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    dnsServerTrap.setStatus(
        ""
    )

snmpServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3007)
)
snmpServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "snmpServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    snmpServerTrap.setStatus(
        ""
    )

ipAddressPoolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3008)
)
ipAddressPoolTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ipAddressPool"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ipAddressPoolTrap.setStatus(
        ""
    )

extLDAPServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 3009)
)
extLDAPServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "extLDAPServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    extLDAPServerTrap.setStatus(
        ""
    )

radiusAuthServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30010)
)
radiusAuthServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "radiusAuthServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    radiusAuthServerTrap.setStatus(
        ""
    )

certificateServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30011)
)
certificateServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "certificateServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    certificateServerTrap.setStatus(
        ""
    )

extLDAPAuthServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30012)
)
extLDAPAuthServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "certificateServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    extLDAPAuthServerTrap.setStatus(
        ""
    )

cmpServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30013)
)
cmpServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "cmpServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    cmpServerTrap.setStatus(
        ""
    )

dhcpServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30014)
)
dhcpServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "dhcpServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    dhcpServerTrap.setStatus(
        ""
    )

sshServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30015)
)
sshServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "sshServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    sshServerTrap.setStatus(
        ""
    )

ntpServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30016)
)
ntpServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ntpServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ntpServerTrap.setStatus(
        ""
    )

ospfServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30017)
)
ospfServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ospfServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ospfServerTrap.setStatus(
        ""
    )

clipServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30018)
)
clipServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "clipServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    clipServerTrap.setStatus(
        ""
    )

dhcprelayServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30019)
)
dhcprelayServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "dhcprelayServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    dhcprelayServerTrap.setStatus(
        ""
    )

gdsServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30020)
)
gdsServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "gdsServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    gdsServerTrap.setStatus(
        ""
    )

demandintfServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30021)
)
demandintfServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "demandintfServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    demandintfServerTrap.setStatus(
        ""
    )

crlServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30022)
)
crlServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "crlServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    crlServerTrap.setStatus(
        ""
    )

ocspServerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 2, 0, 30023)
)
ocspServerTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ocspServer"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ocspServerTrap.setStatus(
        ""
    )

netBuffersTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5001)
)
netBuffersTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "netBuffers"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    netBuffersTrap.setStatus(
        ""
    )

fireWallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5002)
)
fireWallTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fireWall"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fireWallTrap.setStatus(
        ""
    )

fipsStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5003)
)
fipsStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "fipsStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    fipsStatusTrap.setStatus(
        ""
    )

licensingStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5004)
)
licensingStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "licensingStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    licensingStatusTrap.setStatus(
        ""
    )

natStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5005)
)
natStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "natStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    natStatusTrap.setStatus(
        ""
    )

antiSpoofingStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5006)
)
antiSpoofingStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "antiSpoofingStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    antiSpoofingStatusTrap.setStatus(
        ""
    )

sslVpnStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5007)
)
sslVpnStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "sslVpnStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    sslVpnStatusTrap.setStatus(
        ""
    )

usrIpAddrStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5008)
)
usrIpAddrStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "usrIpAddrStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    usrIpAddrStatusTrap.setStatus(
        ""
    )

vrrpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 5009)
)
vrrpStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "vrrpStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    vrrpStatusTrap.setStatus(
        ""
    )

mcastRelayStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50010)
)
mcastRelayStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "mcastRelayStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    mcastRelayStatusTrap.setStatus(
        ""
    )

dlswStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50011)
)
dlswStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "dlswStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    dlswStatusTrap.setStatus(
        ""
    )

ipsecFailoverStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50012)
)
ipsecFailoverStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ipsecFailoverStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ipsecFailoverStatusTrap.setStatus(
        ""
    )

tunnelGuardStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50013)
)
tunnelGuardStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "tunnelGuardStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    tunnelGuardStatusTrap.setStatus(
        ""
    )

ripStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50014)
)
ripStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "ripStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    ripStatusTrap.setStatus(
        ""
    )

routePolicyStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50015)
)
routePolicyStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "routePolicyStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    routePolicyStatusTrap.setStatus(
        ""
    )

cRoutesMStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50016)
)
cRoutesMStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "cRoutesMStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    cRoutesMStatusTrap.setStatus(
        ""
    )

igmpStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 3, 0, 50017)
)
igmpStatusTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "igmpStatus"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    igmpStatusTrap.setStatus(
        ""
    )

failedLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 4, 0, 101)
)
failedLoginTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "failedLogin"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    failedLoginTrap.setStatus(
        ""
    )

securityIntrusionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 5, 0, 201)
)
securityIntrusionTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "severityLevel"),
        ("CONTIVITY-TRAPS-V1-MIB", "securityIntrusion"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemName"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemDate"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemTime"),
        ("CONTIVITY-TRAPS-V1-MIB", "systemUpTime"))
)
if mibBuilder.loadTexts:
    securityIntrusionTrap.setStatus(
        ""
    )

firewallRuleTriggeredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2505, 1, 14, 3, 0, 1)
)
firewallRuleTriggeredTrap.setObjects(
      *(("CONTIVITY-TRAPS-V1-MIB", "firewallPolicyType_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallRuleType_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallRuleNumber_ces"),
        ("IF-MIB", "ifIndex"),
        ("CONTIVITY-TRAPS-V1-MIB", "ifName_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallSrcAddr_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallSrcPort_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallDestAddr_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallDestPort_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallProtocolID_ces"),
        ("CONTIVITY-TRAPS-V1-MIB", "firewallRuleAction_ces"),
        ("SNMPv2-MIB", "sysObjectID"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    firewallRuleTriggeredTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONTIVITY-TRAPS-V1-MIB",
    **{"PortLocation-ces": PortLocation_ces,
       "IfReasonForStatus-ces": IfReasonForStatus_ces,
       "FirewallPolicyType-ces": FirewallPolicyType_ces,
       "FirewallRuleType-ces": FirewallRuleType_ces,
       "FirewallRuleAction-ces": FirewallRuleAction_ces,
       "coldStart": coldStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "contivityTrapsV1": contivityTrapsV1,
       "powerUpTrapEntry": powerUpTrapEntry,
       "periodicHeartbeatTrap": periodicHeartbeatTrap,
       "hardwareCESTrapInfo": hardwareCESTrapInfo,
       "hardDisk1StatusTrap": hardDisk1StatusTrap,
       "hardDisk0StatusTrap": hardDisk0StatusTrap,
       "memoryUsageTrap": memoryUsageTrap,
       "lanCardStatusTrap": lanCardStatusTrap,
       "cpuTwoStatusTrap": cpuTwoStatusTrap,
       "fanOneStatusTrap": fanOneStatusTrap,
       "fanTwoStatusTrap": fanTwoStatusTrap,
       "chassisFanStatusTrap": chassisFanStatusTrap,
       "fiveVoltsPosStatusTrap": fiveVoltsPosStatusTrap,
       "fiveVoltsMinusTrap": fiveVoltsMinusTrap,
       "threeVoltsPositiveTrap": threeVoltsPositiveTrap,
       "twoDotFiveVATrap": twoDotFiveVATrap,
       "twoDotFiveVBTrap": twoDotFiveVBTrap,
       "twelveVoltsPositveTrap": twelveVoltsPositveTrap,
       "twelveVoltsMinsTrap": twelveVoltsMinsTrap,
       "normalTemperatureTrap": normalTemperatureTrap,
       "criticalTemperatureTrap": criticalTemperatureTrap,
       "chassisIntrusionTrap": chassisIntrusionTrap,
       "dualPowerSupplyTrap": dualPowerSupplyTrap,
       "t1WANStatusTrap": t1WANStatusTrap,
       "t3WANStatusTrap": t3WANStatusTrap,
       "hwAccelTrap": hwAccelTrap,
       "v90WANStatusTrap": v90WANStatusTrap,
       "briWANStatusTrap": briWANStatusTrap,
       "serUartStatusTrap": serUartStatusTrap,
       "adslWANStatusTrap": adslWANStatusTrap,
       "hardDisk1Status": hardDisk1Status,
       "hardDisk0Status": hardDisk0Status,
       "memoryUsage": memoryUsage,
       "lanCardStatus": lanCardStatus,
       "cpuTwoStatus": cpuTwoStatus,
       "fanOneStatus": fanOneStatus,
       "fanTwoStatus": fanTwoStatus,
       "chassisFanStatus": chassisFanStatus,
       "fiveVoltsPositive": fiveVoltsPositive,
       "fiveVoltsMinus": fiveVoltsMinus,
       "threeVoltsPositive": threeVoltsPositive,
       "twoDotFiveVA": twoDotFiveVA,
       "twoDotFiveVB": twoDotFiveVB,
       "twelveVoltsPositive": twelveVoltsPositive,
       "twelveVoltsMinus": twelveVoltsMinus,
       "normalTemperature": normalTemperature,
       "criticalTemperature": criticalTemperature,
       "chassisIntrusion": chassisIntrusion,
       "dualPowerSupply": dualPowerSupply,
       "t1WANStatus": t1WANStatus,
       "t3WANStatus": t3WANStatus,
       "hwAccelStatus": hwAccelStatus,
       "v90WANStatus": v90WANStatus,
       "briWANStatus": briWANStatus,
       "serUartStatus": serUartStatus,
       "adslWANStatus": adslWANStatus,
       "serverCESTrapInfo": serverCESTrapInfo,
       "radiusAcctServerTrap": radiusAcctServerTrap,
       "backupServerTrap": backupServerTrap,
       "diskRedundencyTrap": diskRedundencyTrap,
       "intLDAPServerTrap": intLDAPServerTrap,
       "loadBalancingServerTrap": loadBalancingServerTrap,
       "dnsServerTrap": dnsServerTrap,
       "snmpServerTrap": snmpServerTrap,
       "ipAddressPoolTrap": ipAddressPoolTrap,
       "extLDAPServerTrap": extLDAPServerTrap,
       "radiusAuthServerTrap": radiusAuthServerTrap,
       "certificateServerTrap": certificateServerTrap,
       "extLDAPAuthServerTrap": extLDAPAuthServerTrap,
       "cmpServerTrap": cmpServerTrap,
       "dhcpServerTrap": dhcpServerTrap,
       "sshServerTrap": sshServerTrap,
       "ntpServerTrap": ntpServerTrap,
       "ospfServerTrap": ospfServerTrap,
       "clipServerTrap": clipServerTrap,
       "dhcprelayServerTrap": dhcprelayServerTrap,
       "gdsServerTrap": gdsServerTrap,
       "demandintfServerTrap": demandintfServerTrap,
       "crlServerTrap": crlServerTrap,
       "ocspServerTrap": ocspServerTrap,
       "radiusAcctServer": radiusAcctServer,
       "backupServer": backupServer,
       "diskRedundency": diskRedundency,
       "intLDAPServer": intLDAPServer,
       "loadBalancingServer": loadBalancingServer,
       "dnsServer": dnsServer,
       "snmpServer": snmpServer,
       "ipAddressPool": ipAddressPool,
       "extLDAPServer": extLDAPServer,
       "radiusAuthServer": radiusAuthServer,
       "certificateServer": certificateServer,
       "extLDAPAuthServer": extLDAPAuthServer,
       "cmpServer": cmpServer,
       "dhcpServer": dhcpServer,
       "sshServer": sshServer,
       "ntpServer": ntpServer,
       "ospfServer": ospfServer,
       "clipServer": clipServer,
       "dhcprelayServer": dhcprelayServer,
       "gdsServer": gdsServer,
       "demandintfServer": demandintfServer,
       "crlServer": crlServer,
       "ocspServer": ocspServer,
       "serviceCESTrapInfo": serviceCESTrapInfo,
       "netBuffersTrap": netBuffersTrap,
       "fireWallTrap": fireWallTrap,
       "fipsStatusTrap": fipsStatusTrap,
       "licensingStatusTrap": licensingStatusTrap,
       "natStatusTrap": natStatusTrap,
       "antiSpoofingStatusTrap": antiSpoofingStatusTrap,
       "sslVpnStatusTrap": sslVpnStatusTrap,
       "usrIpAddrStatusTrap": usrIpAddrStatusTrap,
       "vrrpStatusTrap": vrrpStatusTrap,
       "mcastRelayStatusTrap": mcastRelayStatusTrap,
       "dlswStatusTrap": dlswStatusTrap,
       "ipsecFailoverStatusTrap": ipsecFailoverStatusTrap,
       "tunnelGuardStatusTrap": tunnelGuardStatusTrap,
       "ripStatusTrap": ripStatusTrap,
       "routePolicyStatusTrap": routePolicyStatusTrap,
       "cRoutesMStatusTrap": cRoutesMStatusTrap,
       "igmpStatusTrap": igmpStatusTrap,
       "netBuffers": netBuffers,
       "fireWall": fireWall,
       "fipsStatus": fipsStatus,
       "licensingStatus": licensingStatus,
       "natStatus": natStatus,
       "antiSpoofingStatus": antiSpoofingStatus,
       "sslVpnStatus": sslVpnStatus,
       "usrIpAddrStatus": usrIpAddrStatus,
       "vrrpStatus": vrrpStatus,
       "mcastRelayStatus": mcastRelayStatus,
       "dlswStatus": dlswStatus,
       "ipsecFailoverStatus": ipsecFailoverStatus,
       "tunnelGuardStatus": tunnelGuardStatus,
       "ripStatus": ripStatus,
       "routePolicyStatus": routePolicyStatus,
       "cRoutesMStatus": cRoutesMStatus,
       "igmpStatus": igmpStatus,
       "loginCESTrapInfo": loginCESTrapInfo,
       "failedLoginTrap": failedLoginTrap,
       "failedLogin": failedLogin,
       "intrusionCESTrapInfo": intrusionCESTrapInfo,
       "securityIntrusionTrap": securityIntrusionTrap,
       "securityIntrusion": securityIntrusion,
       "powerUpTrap": powerUpTrap,
       "severityLevel": severityLevel,
       "systemName": systemName,
       "systemDate": systemDate,
       "systemTime": systemTime,
       "systemUpTime": systemUpTime,
       "periodicHeartbeat": periodicHeartbeat,
       "snmpAgentTrapInfo-ces": snmpAgentTrapInfo_ces,
       "snmpAgentAuthTrapInfo-ces": snmpAgentAuthTrapInfo_ces,
       "snmpAuthenOperation-ces": snmpAuthenOperation_ces,
       "snmpAuthenIpAddress-ces": snmpAuthenIpAddress_ces,
       "snmpAuthenCommString-ces": snmpAuthenCommString_ces,
       "snmpAgentInterfaceInfo-ces": snmpAgentInterfaceInfo_ces,
       "ifReasonForStatus-ces": ifReasonForStatus_ces,
       "ifPhysLocation-ces": ifPhysLocation_ces,
       "ifPhysRelPos-ces": ifPhysRelPos_ces,
       "ifIpAddr-ces": ifIpAddr_ces,
       "ifName-ces": ifName_ces,
       "ifTunnelRemoteIpAddr-ces": ifTunnelRemoteIpAddr_ces,
       "snmpAgentFirewallInfo-ces": snmpAgentFirewallInfo_ces,
       "firewallRuleTriggeredTrap": firewallRuleTriggeredTrap,
       "firewallPolicyType-ces": firewallPolicyType_ces,
       "firewallRuleType-ces": firewallRuleType_ces,
       "firewallRuleNumber-ces": firewallRuleNumber_ces,
       "firewallSrcAddr-ces": firewallSrcAddr_ces,
       "firewallSrcPort-ces": firewallSrcPort_ces,
       "firewallDestAddr-ces": firewallDestAddr_ces,
       "firewallDestPort-ces": firewallDestPort_ces,
       "firewallProtocolID-ces": firewallProtocolID_ces,
       "firewallRuleAction-ces": firewallRuleAction_ces}
)
