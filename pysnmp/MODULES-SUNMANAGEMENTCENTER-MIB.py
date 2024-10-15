# SNMP MIB module (MODULES-SUNMANAGEMENTCENTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MODULES-SUNMANAGEMENTCENTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:38 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Prod_ObjectIdentity = ObjectIdentity
prod = _Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Sunsymon_ObjectIdentity = ObjectIdentity
sunsymon = _Sunsymon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12)
)
_Agent_ObjectIdentity = ObjectIdentity
agent = _Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2)
)
_Base_ObjectIdentity = ObjectIdentity
base = _Base_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1)
)
_Info_ObjectIdentity = ObjectIdentity
info = _Info_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 1, 2, 1)
)
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1)
)
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1)
)
_Reader4u_ObjectIdentity = ObjectIdentity
reader4u = _Reader4u_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 1)
)
_Reader4udt_ObjectIdentity = ObjectIdentity
reader4udt = _Reader4udt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 2)
)
_Reader4uwg_ObjectIdentity = ObjectIdentity
reader4uwg = _Reader4uwg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 3)
)
_Reader4u1P_ObjectIdentity = ObjectIdentity
reader4u1P = _Reader4u1P_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 4)
)
_Reader4u1D_ObjectIdentity = ObjectIdentity
reader4u1D = _Reader4u1D_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 5)
)
_Reader4unt_ObjectIdentity = ObjectIdentity
reader4unt = _Reader4unt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 6)
)
_ReaderSerengeti_ObjectIdentity = ObjectIdentity
readerSerengeti = _ReaderSerengeti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 7)
)
_Reader4uvh_ObjectIdentity = ObjectIdentity
reader4uvh = _Reader4uvh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 8)
)
_ReaderECP_ObjectIdentity = ObjectIdentity
readerECP = _ReaderECP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 9)
)
_ReaderELP_ObjectIdentity = ObjectIdentity
readerELP = _ReaderELP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 1, 1, 10)
)
_OperatingSystem_ObjectIdentity = ObjectIdentity
operatingSystem = _OperatingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 2)
)
_LocalApplication_ObjectIdentity = ObjectIdentity
localApplication = _LocalApplication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 3)
)
_RemoteSystem_ObjectIdentity = ObjectIdentity
remoteSystem = _RemoteSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 4)
)
_ServerSupport_ObjectIdentity = ObjectIdentity
serverSupport = _ServerSupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 5)
)
_Dr_ObjectIdentity = ObjectIdentity
dr = _Dr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 10)
)
_HealthMonitor_ObjectIdentity = ObjectIdentity
healthMonitor = _HealthMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 11)
)
_KernelReader_ObjectIdentity = ObjectIdentity
kernelReader = _KernelReader_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 12)
)
_ProcessDetails_ObjectIdentity = ObjectIdentity
processDetails = _ProcessDetails_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 13)
)
_Mib2Proxy_ObjectIdentity = ObjectIdentity
mib2Proxy = _Mib2Proxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 14)
)
_Dtable_ObjectIdentity = ObjectIdentity
dtable = _Dtable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 15)
)
_KernelReaderSimple_ObjectIdentity = ObjectIdentity
kernelReaderSimple = _KernelReaderSimple_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 16)
)
_Hdreg_ObjectIdentity = ObjectIdentity
hdreg = _Hdreg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 17)
)
_A5x00_ObjectIdentity = ObjectIdentity
a5x00 = _A5x00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 18)
)
_T300_ObjectIdentity = ObjectIdentity
t300 = _T300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 19)
)
_ProcessTable_ObjectIdentity = ObjectIdentity
processTable = _ProcessTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 20)
)
_DatalogRegistry_ObjectIdentity = ObjectIdentity
datalogRegistry = _DatalogRegistry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 21)
)
_Dirmon_ObjectIdentity = ObjectIdentity
dirmon = _Dirmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 22)
)
_Filemon_ObjectIdentity = ObjectIdentity
filemon = _Filemon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 23)
)
_Fscan_ObjectIdentity = ObjectIdentity
fscan = _Fscan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 24)
)
_HpJetdirect_ObjectIdentity = ObjectIdentity
hpJetdirect = _HpJetdirect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 25)
)
_Nfsmon_ObjectIdentity = ObjectIdentity
nfsmon = _Nfsmon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 27)
)
_Nfsstat_ObjectIdentity = ObjectIdentity
nfsstat = _Nfsstat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28)
)
_PrintSpool_ObjectIdentity = ObjectIdentity
printSpool = _PrintSpool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 29)
)
_AgentStats_ObjectIdentity = ObjectIdentity
agentStats = _AgentStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 30)
)
_DomainControl_ObjectIdentity = ObjectIdentity
domainControl = _DomainControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 31)
)
_TopologyLicense_ObjectIdentity = ObjectIdentity
topologyLicense = _TopologyLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 32)
)
_Topology_ObjectIdentity = ObjectIdentity
topology = _Topology_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 33)
)
_Cfgserver_ObjectIdentity = ObjectIdentity
cfgserver = _Cfgserver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 34)
)
_Eventmgr_ObjectIdentity = ObjectIdentity
eventmgr = _Eventmgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 35)
)
_ToolAdhocs_ObjectIdentity = ObjectIdentity
toolAdhocs = _ToolAdhocs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 36)
)
_PrintSpoolv3_ObjectIdentity = ObjectIdentity
printSpoolv3 = _PrintSpoolv3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 37)
)
_Discovery_ObjectIdentity = ObjectIdentity
discovery = _Discovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 38)
)
_Ipv6_ObjectIdentity = ObjectIdentity
ipv6 = _Ipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 39)
)
_Agent_update_ObjectIdentity = ObjectIdentity
agent_update = _Agent_update_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 40)
)
_Altpath_ObjectIdentity = ObjectIdentity
altpath = _Altpath_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 45)
)
_MetadataManager_ObjectIdentity = ObjectIdentity
metadataManager = _MetadataManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 46)
)
_Logview_ObjectIdentity = ObjectIdentity
logview = _Logview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 47)
)
_Mcp_ObjectIdentity = ObjectIdentity
mcp = _Mcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 48)
)
_Builder_ObjectIdentity = ObjectIdentity
builder = _Builder_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 49)
)
_Dr_serengeti_ObjectIdentity = ObjectIdentity
dr_serengeti = _Dr_serengeti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 51)
)
_Em_ObjectIdentity = ObjectIdentity
em = _Em_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 52)
)
_Crashdump_ObjectIdentity = ObjectIdentity
crashdump = _Crashdump_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 53)
)
_Filewch_ObjectIdentity = ObjectIdentity
filewch = _Filewch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 54)
)
_Patchmgt_ObjectIdentity = ObjectIdentity
patchmgt = _Patchmgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 55)
)
_ScriptLauncher_ObjectIdentity = ObjectIdentity
scriptLauncher = _ScriptLauncher_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 56)
)
_ScriptRepository_ObjectIdentity = ObjectIdentity
scriptRepository = _ScriptRepository_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 57)
)
_HttpST_ObjectIdentity = ObjectIdentity
httpST = _HttpST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 58)
)
_FtpST_ObjectIdentity = ObjectIdentity
ftpST = _FtpST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 59)
)
_TelnetST_ObjectIdentity = ObjectIdentity
telnetST = _TelnetST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 60)
)
_DnsST_ObjectIdentity = ObjectIdentity
dnsST = _DnsST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 61)
)
_NisST_ObjectIdentity = ObjectIdentity
nisST = _NisST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 62)
)
_LdapST_ObjectIdentity = ObjectIdentity
ldapST = _LdapST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 63)
)
_SmtpST_ObjectIdentity = ObjectIdentity
smtpST = _SmtpST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 64)
)
_ImapST_ObjectIdentity = ObjectIdentity
imapST = _ImapST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 65)
)
_PopST_ObjectIdentity = ObjectIdentity
popST = _PopST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 66)
)
_CalendarST_ObjectIdentity = ObjectIdentity
calendarST = _CalendarST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 67)
)
_HttpSE_ObjectIdentity = ObjectIdentity
httpSE = _HttpSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 68)
)
_FtpSE_ObjectIdentity = ObjectIdentity
ftpSE = _FtpSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 69)
)
_TelnetSE_ObjectIdentity = ObjectIdentity
telnetSE = _TelnetSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 70)
)
_DnsSE_ObjectIdentity = ObjectIdentity
dnsSE = _DnsSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 71)
)
_NisSE_ObjectIdentity = ObjectIdentity
nisSE = _NisSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 72)
)
_LdapSE_ObjectIdentity = ObjectIdentity
ldapSE = _LdapSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 73)
)
_SmtpSE_ObjectIdentity = ObjectIdentity
smtpSE = _SmtpSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 74)
)
_ImapSE_ObjectIdentity = ObjectIdentity
imapSE = _ImapSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 75)
)
_PopSE_ObjectIdentity = ObjectIdentity
popSE = _PopSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 76)
)
_CalendarSE_ObjectIdentity = ObjectIdentity
calendarSE = _CalendarSE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 77)
)
_Edot_ObjectIdentity = ObjectIdentity
edot = _Edot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 78)
)
_Pkgchk_ObjectIdentity = ObjectIdentity
pkgchk = _Pkgchk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 81)
)
_Patchadmin_ObjectIdentity = ObjectIdentity
patchadmin = _Patchadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 82)
)
_Perftool_ObjectIdentity = ObjectIdentity
perftool = _Perftool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 88)
)
_Ichange_ObjectIdentity = ObjectIdentity
ichange = _Ichange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 89)
)
_V880_dr_ObjectIdentity = ObjectIdentity
v880_dr = _V880_dr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 90)
)
_Serengeti_platadmin_ObjectIdentity = ObjectIdentity
serengeti_platadmin = _Serengeti_platadmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 100)
)
_Serengeti_rules_ObjectIdentity = ObjectIdentity
serengeti_rules = _Serengeti_rules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 101)
)
_Cod_ObjectIdentity = ObjectIdentity
cod = _Cod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 200)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MODULES-SUNMANAGEMENTCENTER-MIB",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "base": base,
       "info": info,
       "system": system,
       "modules": modules,
       "hardware": hardware,
       "config": config,
       "reader4u": reader4u,
       "reader4udt": reader4udt,
       "reader4uwg": reader4uwg,
       "reader4u1P": reader4u1P,
       "reader4u1D": reader4u1D,
       "reader4unt": reader4unt,
       "readerSerengeti": readerSerengeti,
       "reader4uvh": reader4uvh,
       "readerECP": readerECP,
       "readerELP": readerELP,
       "operatingSystem": operatingSystem,
       "localApplication": localApplication,
       "remoteSystem": remoteSystem,
       "serverSupport": serverSupport,
       "dr": dr,
       "healthMonitor": healthMonitor,
       "kernelReader": kernelReader,
       "processDetails": processDetails,
       "mib2Proxy": mib2Proxy,
       "dtable": dtable,
       "kernelReaderSimple": kernelReaderSimple,
       "hdreg": hdreg,
       "a5x00": a5x00,
       "t300": t300,
       "processTable": processTable,
       "datalogRegistry": datalogRegistry,
       "dirmon": dirmon,
       "filemon": filemon,
       "fscan": fscan,
       "hpJetdirect": hpJetdirect,
       "nfsmon": nfsmon,
       "nfsstat": nfsstat,
       "printSpool": printSpool,
       "agentStats": agentStats,
       "domainControl": domainControl,
       "topologyLicense": topologyLicense,
       "topology": topology,
       "cfgserver": cfgserver,
       "eventmgr": eventmgr,
       "toolAdhocs": toolAdhocs,
       "printSpoolv3": printSpoolv3,
       "discovery": discovery,
       "ipv6": ipv6,
       "agent-update": agent_update,
       "altpath": altpath,
       "metadataManager": metadataManager,
       "logview": logview,
       "mcp": mcp,
       "builder": builder,
       "dr-serengeti": dr_serengeti,
       "em": em,
       "crashdump": crashdump,
       "filewch": filewch,
       "patchmgt": patchmgt,
       "scriptLauncher": scriptLauncher,
       "scriptRepository": scriptRepository,
       "httpST": httpST,
       "ftpST": ftpST,
       "telnetST": telnetST,
       "dnsST": dnsST,
       "nisST": nisST,
       "ldapST": ldapST,
       "smtpST": smtpST,
       "imapST": imapST,
       "popST": popST,
       "calendarST": calendarST,
       "httpSE": httpSE,
       "ftpSE": ftpSE,
       "telnetSE": telnetSE,
       "dnsSE": dnsSE,
       "nisSE": nisSE,
       "ldapSE": ldapSE,
       "smtpSE": smtpSE,
       "imapSE": imapSE,
       "popSE": popSE,
       "calendarSE": calendarSE,
       "edot": edot,
       "pkgchk": pkgchk,
       "patchadmin": patchadmin,
       "perftool": perftool,
       "ichange": ichange,
       "v880-dr": v880_dr,
       "serengeti-platadmin": serengeti_platadmin,
       "serengeti-rules": serengeti_rules,
       "cod": cod}
)
