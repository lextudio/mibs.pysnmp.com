# SNMP MIB module (CISCO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:05:41 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(ipRouteDest,) = mibBuilder.importSymbols(
    "RFC1213-MIB",
    "ipRouteDest")

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

(tcpConnLocalAddress,
 tcpConnLocalPort,
 tcpConnRemAddress,
 tcpConnRemPort) = mibBuilder.importSymbols(
    "TCP-MIB",
    "tcpConnLocalAddress",
    "tcpConnLocalPort",
    "tcpConnRemAddress",
    "tcpConnRemPort")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cisco_ObjectIdentity = ObjectIdentity
cisco = _Cisco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1)
)
_Gateway_server_ObjectIdentity = ObjectIdentity
gateway_server = _Gateway_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 1)
)
_Terminal_server_ObjectIdentity = ObjectIdentity
terminal_server = _Terminal_server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 2)
)
_Trouter_ObjectIdentity = ObjectIdentity
trouter = _Trouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 3)
)
_Protocol_translator_ObjectIdentity = ObjectIdentity
protocol_translator = _Protocol_translator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 4)
)
_Igs_sysID_ObjectIdentity = ObjectIdentity
igs_sysID = _Igs_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 5)
)
_C3000_sysID_ObjectIdentity = ObjectIdentity
c3000_sysID = _C3000_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 6)
)
_C4000_sysID_ObjectIdentity = ObjectIdentity
c4000_sysID = _C4000_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 7)
)
_C7000_sysID_ObjectIdentity = ObjectIdentity
c7000_sysID = _C7000_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 8)
)
_Cs_500_sysID_ObjectIdentity = ObjectIdentity
cs_500_sysID = _Cs_500_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 9)
)
_C2000_sysID_ObjectIdentity = ObjectIdentity
c2000_sysID = _C2000_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 10)
)
_Agsplus_sysID_ObjectIdentity = ObjectIdentity
agsplus_sysID = _Agsplus_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 11)
)
_C7010_sysID_ObjectIdentity = ObjectIdentity
c7010_sysID = _C7010_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 12)
)
_C2500_sysID_ObjectIdentity = ObjectIdentity
c2500_sysID = _C2500_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 13)
)
_C4500_sysID_ObjectIdentity = ObjectIdentity
c4500_sysID = _C4500_sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 1, 14)
)
_Local_ObjectIdentity = ObjectIdentity
local = _Local_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2)
)
_Lsystem_ObjectIdentity = ObjectIdentity
lsystem = _Lsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 1)
)
_RomId_Type = DisplayString
_RomId_Object = MibScalar
romId = _RomId_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 1),
    _RomId_Type()
)
romId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romId.setStatus("mandatory")
_WhyReload_Type = DisplayString
_WhyReload_Object = MibScalar
whyReload = _WhyReload_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 2),
    _WhyReload_Type()
)
whyReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    whyReload.setStatus("mandatory")
_HostName_Type = DisplayString
_HostName_Object = MibScalar
hostName = _HostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 3),
    _HostName_Type()
)
hostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostName.setStatus("mandatory")
_DomainName_Type = DisplayString
_DomainName_Object = MibScalar
domainName = _DomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 4),
    _DomainName_Type()
)
domainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    domainName.setStatus("mandatory")
_AuthAddr_Type = IpAddress
_AuthAddr_Object = MibScalar
authAddr = _AuthAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 5),
    _AuthAddr_Type()
)
authAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    authAddr.setStatus("mandatory")
_BootHost_Type = IpAddress
_BootHost_Object = MibScalar
bootHost = _BootHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 6),
    _BootHost_Type()
)
bootHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootHost.setStatus("mandatory")
_Ping_Type = Integer32
_Ping_Object = MibScalar
ping = _Ping_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 7),
    _Ping_Type()
)
ping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ping.setStatus("mandatory")
_FreeMem_Type = Integer32
_FreeMem_Object = MibScalar
freeMem = _FreeMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 8),
    _FreeMem_Type()
)
freeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMem.setStatus("mandatory")
_BufferElFree_Type = Integer32
_BufferElFree_Object = MibScalar
bufferElFree = _BufferElFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 9),
    _BufferElFree_Type()
)
bufferElFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElFree.setStatus("mandatory")
_BufferElMax_Type = Integer32
_BufferElMax_Object = MibScalar
bufferElMax = _BufferElMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 10),
    _BufferElMax_Type()
)
bufferElMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElMax.setStatus("mandatory")
_BufferElHit_Type = Integer32
_BufferElHit_Object = MibScalar
bufferElHit = _BufferElHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 11),
    _BufferElHit_Type()
)
bufferElHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElHit.setStatus("mandatory")
_BufferElMiss_Type = Integer32
_BufferElMiss_Object = MibScalar
bufferElMiss = _BufferElMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 12),
    _BufferElMiss_Type()
)
bufferElMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElMiss.setStatus("mandatory")
_BufferElCreate_Type = Integer32
_BufferElCreate_Object = MibScalar
bufferElCreate = _BufferElCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 13),
    _BufferElCreate_Type()
)
bufferElCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferElCreate.setStatus("mandatory")
_BufferSmSize_Type = Integer32
_BufferSmSize_Object = MibScalar
bufferSmSize = _BufferSmSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 14),
    _BufferSmSize_Type()
)
bufferSmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmSize.setStatus("mandatory")
_BufferSmTotal_Type = Integer32
_BufferSmTotal_Object = MibScalar
bufferSmTotal = _BufferSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 15),
    _BufferSmTotal_Type()
)
bufferSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmTotal.setStatus("mandatory")
_BufferSmFree_Type = Integer32
_BufferSmFree_Object = MibScalar
bufferSmFree = _BufferSmFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 16),
    _BufferSmFree_Type()
)
bufferSmFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmFree.setStatus("mandatory")
_BufferSmMax_Type = Integer32
_BufferSmMax_Object = MibScalar
bufferSmMax = _BufferSmMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 17),
    _BufferSmMax_Type()
)
bufferSmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmMax.setStatus("mandatory")
_BufferSmHit_Type = Integer32
_BufferSmHit_Object = MibScalar
bufferSmHit = _BufferSmHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 18),
    _BufferSmHit_Type()
)
bufferSmHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmHit.setStatus("mandatory")
_BufferSmMiss_Type = Integer32
_BufferSmMiss_Object = MibScalar
bufferSmMiss = _BufferSmMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 19),
    _BufferSmMiss_Type()
)
bufferSmMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmMiss.setStatus("mandatory")
_BufferSmTrim_Type = Integer32
_BufferSmTrim_Object = MibScalar
bufferSmTrim = _BufferSmTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 20),
    _BufferSmTrim_Type()
)
bufferSmTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmTrim.setStatus("mandatory")
_BufferSmCreate_Type = Integer32
_BufferSmCreate_Object = MibScalar
bufferSmCreate = _BufferSmCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 21),
    _BufferSmCreate_Type()
)
bufferSmCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferSmCreate.setStatus("mandatory")
_BufferMdSize_Type = Integer32
_BufferMdSize_Object = MibScalar
bufferMdSize = _BufferMdSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 22),
    _BufferMdSize_Type()
)
bufferMdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdSize.setStatus("mandatory")
_BufferMdTotal_Type = Integer32
_BufferMdTotal_Object = MibScalar
bufferMdTotal = _BufferMdTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 23),
    _BufferMdTotal_Type()
)
bufferMdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdTotal.setStatus("mandatory")
_BufferMdFree_Type = Integer32
_BufferMdFree_Object = MibScalar
bufferMdFree = _BufferMdFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 24),
    _BufferMdFree_Type()
)
bufferMdFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdFree.setStatus("mandatory")
_BufferMdMax_Type = Integer32
_BufferMdMax_Object = MibScalar
bufferMdMax = _BufferMdMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 25),
    _BufferMdMax_Type()
)
bufferMdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdMax.setStatus("mandatory")
_BufferMdHit_Type = Integer32
_BufferMdHit_Object = MibScalar
bufferMdHit = _BufferMdHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 26),
    _BufferMdHit_Type()
)
bufferMdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdHit.setStatus("mandatory")
_BufferMdMiss_Type = Integer32
_BufferMdMiss_Object = MibScalar
bufferMdMiss = _BufferMdMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 27),
    _BufferMdMiss_Type()
)
bufferMdMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdMiss.setStatus("mandatory")
_BufferMdTrim_Type = Integer32
_BufferMdTrim_Object = MibScalar
bufferMdTrim = _BufferMdTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 28),
    _BufferMdTrim_Type()
)
bufferMdTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdTrim.setStatus("mandatory")
_BufferMdCreate_Type = Integer32
_BufferMdCreate_Object = MibScalar
bufferMdCreate = _BufferMdCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 29),
    _BufferMdCreate_Type()
)
bufferMdCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferMdCreate.setStatus("mandatory")
_BufferBgSize_Type = Integer32
_BufferBgSize_Object = MibScalar
bufferBgSize = _BufferBgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 30),
    _BufferBgSize_Type()
)
bufferBgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgSize.setStatus("mandatory")
_BufferBgTotal_Type = Integer32
_BufferBgTotal_Object = MibScalar
bufferBgTotal = _BufferBgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 31),
    _BufferBgTotal_Type()
)
bufferBgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgTotal.setStatus("mandatory")
_BufferBgFree_Type = Integer32
_BufferBgFree_Object = MibScalar
bufferBgFree = _BufferBgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 32),
    _BufferBgFree_Type()
)
bufferBgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgFree.setStatus("mandatory")
_BufferBgMax_Type = Integer32
_BufferBgMax_Object = MibScalar
bufferBgMax = _BufferBgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 33),
    _BufferBgMax_Type()
)
bufferBgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgMax.setStatus("mandatory")
_BufferBgHit_Type = Integer32
_BufferBgHit_Object = MibScalar
bufferBgHit = _BufferBgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 34),
    _BufferBgHit_Type()
)
bufferBgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgHit.setStatus("mandatory")
_BufferBgMiss_Type = Integer32
_BufferBgMiss_Object = MibScalar
bufferBgMiss = _BufferBgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 35),
    _BufferBgMiss_Type()
)
bufferBgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgMiss.setStatus("mandatory")
_BufferBgTrim_Type = Integer32
_BufferBgTrim_Object = MibScalar
bufferBgTrim = _BufferBgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 36),
    _BufferBgTrim_Type()
)
bufferBgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgTrim.setStatus("mandatory")
_BufferBgCreate_Type = Integer32
_BufferBgCreate_Object = MibScalar
bufferBgCreate = _BufferBgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 37),
    _BufferBgCreate_Type()
)
bufferBgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferBgCreate.setStatus("mandatory")
_BufferLgSize_Type = Integer32
_BufferLgSize_Object = MibScalar
bufferLgSize = _BufferLgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 38),
    _BufferLgSize_Type()
)
bufferLgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgSize.setStatus("mandatory")
_BufferLgTotal_Type = Integer32
_BufferLgTotal_Object = MibScalar
bufferLgTotal = _BufferLgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 39),
    _BufferLgTotal_Type()
)
bufferLgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgTotal.setStatus("mandatory")
_BufferLgFree_Type = Integer32
_BufferLgFree_Object = MibScalar
bufferLgFree = _BufferLgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 40),
    _BufferLgFree_Type()
)
bufferLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgFree.setStatus("mandatory")
_BufferLgMax_Type = Integer32
_BufferLgMax_Object = MibScalar
bufferLgMax = _BufferLgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 41),
    _BufferLgMax_Type()
)
bufferLgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgMax.setStatus("mandatory")
_BufferLgHit_Type = Integer32
_BufferLgHit_Object = MibScalar
bufferLgHit = _BufferLgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 42),
    _BufferLgHit_Type()
)
bufferLgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgHit.setStatus("mandatory")
_BufferLgMiss_Type = Integer32
_BufferLgMiss_Object = MibScalar
bufferLgMiss = _BufferLgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 43),
    _BufferLgMiss_Type()
)
bufferLgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgMiss.setStatus("mandatory")
_BufferLgTrim_Type = Integer32
_BufferLgTrim_Object = MibScalar
bufferLgTrim = _BufferLgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 44),
    _BufferLgTrim_Type()
)
bufferLgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgTrim.setStatus("mandatory")
_BufferLgCreate_Type = Integer32
_BufferLgCreate_Object = MibScalar
bufferLgCreate = _BufferLgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 45),
    _BufferLgCreate_Type()
)
bufferLgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferLgCreate.setStatus("mandatory")
_BufferFail_Type = Integer32
_BufferFail_Object = MibScalar
bufferFail = _BufferFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 46),
    _BufferFail_Type()
)
bufferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferFail.setStatus("mandatory")
_BufferNoMem_Type = Integer32
_BufferNoMem_Object = MibScalar
bufferNoMem = _BufferNoMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 47),
    _BufferNoMem_Type()
)
bufferNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferNoMem.setStatus("mandatory")
_NetConfigAddr_Type = IpAddress
_NetConfigAddr_Object = MibScalar
netConfigAddr = _NetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 48),
    _NetConfigAddr_Type()
)
netConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigAddr.setStatus("mandatory")
_NetConfigName_Type = DisplayString
_NetConfigName_Object = MibScalar
netConfigName = _NetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 49),
    _NetConfigName_Type()
)
netConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigName.setStatus("mandatory")
_NetConfigSet_Type = DisplayString
_NetConfigSet_Object = MibScalar
netConfigSet = _NetConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 50),
    _NetConfigSet_Type()
)
netConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    netConfigSet.setStatus("mandatory")
_HostConfigAddr_Type = IpAddress
_HostConfigAddr_Object = MibScalar
hostConfigAddr = _HostConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 51),
    _HostConfigAddr_Type()
)
hostConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigAddr.setStatus("mandatory")
_HostConfigName_Type = DisplayString
_HostConfigName_Object = MibScalar
hostConfigName = _HostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 52),
    _HostConfigName_Type()
)
hostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigName.setStatus("mandatory")
_HostConfigSet_Type = DisplayString
_HostConfigSet_Object = MibScalar
hostConfigSet = _HostConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 53),
    _HostConfigSet_Type()
)
hostConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hostConfigSet.setStatus("mandatory")
_WriteMem_Type = Integer32
_WriteMem_Object = MibScalar
writeMem = _WriteMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 54),
    _WriteMem_Type()
)
writeMem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeMem.setStatus("mandatory")
_WriteNet_Type = DisplayString
_WriteNet_Object = MibScalar
writeNet = _WriteNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 55),
    _WriteNet_Type()
)
writeNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    writeNet.setStatus("mandatory")
_BusyPer_Type = Integer32
_BusyPer_Object = MibScalar
busyPer = _BusyPer_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 56),
    _BusyPer_Type()
)
busyPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    busyPer.setStatus("mandatory")
_AvgBusy1_Type = Integer32
_AvgBusy1_Object = MibScalar
avgBusy1 = _AvgBusy1_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 57),
    _AvgBusy1_Type()
)
avgBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBusy1.setStatus("mandatory")
_AvgBusy5_Type = Integer32
_AvgBusy5_Object = MibScalar
avgBusy5 = _AvgBusy5_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 58),
    _AvgBusy5_Type()
)
avgBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBusy5.setStatus("mandatory")
_IdleCount_Type = Integer32
_IdleCount_Object = MibScalar
idleCount = _IdleCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 59),
    _IdleCount_Type()
)
idleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleCount.setStatus("mandatory")
_IdleWired_Type = Integer32
_IdleWired_Object = MibScalar
idleWired = _IdleWired_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 60),
    _IdleWired_Type()
)
idleWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    idleWired.setStatus("mandatory")
_CiscoContactInfo_Type = DisplayString
_CiscoContactInfo_Object = MibScalar
ciscoContactInfo = _CiscoContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 61),
    _CiscoContactInfo_Type()
)
ciscoContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoContactInfo.setStatus("mandatory")
_BufferHgSize_Type = Integer32
_BufferHgSize_Object = MibScalar
bufferHgSize = _BufferHgSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 62),
    _BufferHgSize_Type()
)
bufferHgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgSize.setStatus("mandatory")
_BufferHgTotal_Type = Integer32
_BufferHgTotal_Object = MibScalar
bufferHgTotal = _BufferHgTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 63),
    _BufferHgTotal_Type()
)
bufferHgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgTotal.setStatus("mandatory")
_BufferHgFree_Type = Integer32
_BufferHgFree_Object = MibScalar
bufferHgFree = _BufferHgFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 64),
    _BufferHgFree_Type()
)
bufferHgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgFree.setStatus("mandatory")
_BufferHgMax_Type = Integer32
_BufferHgMax_Object = MibScalar
bufferHgMax = _BufferHgMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 65),
    _BufferHgMax_Type()
)
bufferHgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgMax.setStatus("mandatory")
_BufferHgHit_Type = Integer32
_BufferHgHit_Object = MibScalar
bufferHgHit = _BufferHgHit_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 66),
    _BufferHgHit_Type()
)
bufferHgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgHit.setStatus("mandatory")
_BufferHgMiss_Type = Integer32
_BufferHgMiss_Object = MibScalar
bufferHgMiss = _BufferHgMiss_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 67),
    _BufferHgMiss_Type()
)
bufferHgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgMiss.setStatus("mandatory")
_BufferHgTrim_Type = Integer32
_BufferHgTrim_Object = MibScalar
bufferHgTrim = _BufferHgTrim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 68),
    _BufferHgTrim_Type()
)
bufferHgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgTrim.setStatus("mandatory")
_BufferHgCreate_Type = Integer32
_BufferHgCreate_Object = MibScalar
bufferHgCreate = _BufferHgCreate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 69),
    _BufferHgCreate_Type()
)
bufferHgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bufferHgCreate.setStatus("mandatory")
_NetConfigProto_Type = Integer32
_NetConfigProto_Object = MibScalar
netConfigProto = _NetConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 70),
    _NetConfigProto_Type()
)
netConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigProto.setStatus("mandatory")
_HostConfigProto_Type = Integer32
_HostConfigProto_Object = MibScalar
hostConfigProto = _HostConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 71),
    _HostConfigProto_Type()
)
hostConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigProto.setStatus("mandatory")
_SysConfigAddr_Type = IpAddress
_SysConfigAddr_Object = MibScalar
sysConfigAddr = _SysConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 72),
    _SysConfigAddr_Type()
)
sysConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigAddr.setStatus("mandatory")
_SysConfigName_Type = DisplayString
_SysConfigName_Object = MibScalar
sysConfigName = _SysConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 73),
    _SysConfigName_Type()
)
sysConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigName.setStatus("mandatory")
_SysConfigProto_Type = Integer32
_SysConfigProto_Object = MibScalar
sysConfigProto = _SysConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 74),
    _SysConfigProto_Type()
)
sysConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigProto.setStatus("mandatory")
_SysClearARP_Type = Integer32
_SysClearARP_Object = MibScalar
sysClearARP = _SysClearARP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 75),
    _SysClearARP_Type()
)
sysClearARP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysClearARP.setStatus("mandatory")
_SysClearInt_Type = Integer32
_SysClearInt_Object = MibScalar
sysClearInt = _SysClearInt_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 76),
    _SysClearInt_Type()
)
sysClearInt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    sysClearInt.setStatus("mandatory")
_EnvPresent_Type = Integer32
_EnvPresent_Object = MibScalar
envPresent = _EnvPresent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 77),
    _EnvPresent_Type()
)
envPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envPresent.setStatus("mandatory")
_EnvTestPt1Descr_Type = DisplayString
_EnvTestPt1Descr_Object = MibScalar
envTestPt1Descr = _EnvTestPt1Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 78),
    _EnvTestPt1Descr_Type()
)
envTestPt1Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1Descr.setStatus("mandatory")
_EnvTestPt1Measure_Type = Integer32
_EnvTestPt1Measure_Object = MibScalar
envTestPt1Measure = _EnvTestPt1Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 79),
    _EnvTestPt1Measure_Type()
)
envTestPt1Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1Measure.setStatus("mandatory")
_EnvTestPt2Descr_Type = DisplayString
_EnvTestPt2Descr_Object = MibScalar
envTestPt2Descr = _EnvTestPt2Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 80),
    _EnvTestPt2Descr_Type()
)
envTestPt2Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2Descr.setStatus("mandatory")
_EnvTestPt2Measure_Type = Integer32
_EnvTestPt2Measure_Object = MibScalar
envTestPt2Measure = _EnvTestPt2Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 81),
    _EnvTestPt2Measure_Type()
)
envTestPt2Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2Measure.setStatus("mandatory")
_EnvTestPt3Descr_Type = DisplayString
_EnvTestPt3Descr_Object = MibScalar
envTestPt3Descr = _EnvTestPt3Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 82),
    _EnvTestPt3Descr_Type()
)
envTestPt3Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3Descr.setStatus("mandatory")
_EnvTestPt3Measure_Type = Integer32
_EnvTestPt3Measure_Object = MibScalar
envTestPt3Measure = _EnvTestPt3Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 83),
    _EnvTestPt3Measure_Type()
)
envTestPt3Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3Measure.setStatus("mandatory")
_EnvTestPt4Descr_Type = DisplayString
_EnvTestPt4Descr_Object = MibScalar
envTestPt4Descr = _EnvTestPt4Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 84),
    _EnvTestPt4Descr_Type()
)
envTestPt4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4Descr.setStatus("mandatory")
_EnvTestPt4Measure_Type = Integer32
_EnvTestPt4Measure_Object = MibScalar
envTestPt4Measure = _EnvTestPt4Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 85),
    _EnvTestPt4Measure_Type()
)
envTestPt4Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4Measure.setStatus("mandatory")
_EnvTestPt5Descr_Type = DisplayString
_EnvTestPt5Descr_Object = MibScalar
envTestPt5Descr = _EnvTestPt5Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 86),
    _EnvTestPt5Descr_Type()
)
envTestPt5Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5Descr.setStatus("mandatory")
_EnvTestPt5Measure_Type = Integer32
_EnvTestPt5Measure_Object = MibScalar
envTestPt5Measure = _EnvTestPt5Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 87),
    _EnvTestPt5Measure_Type()
)
envTestPt5Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5Measure.setStatus("mandatory")
_EnvTestPt6Descr_Type = DisplayString
_EnvTestPt6Descr_Object = MibScalar
envTestPt6Descr = _EnvTestPt6Descr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 88),
    _EnvTestPt6Descr_Type()
)
envTestPt6Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6Descr.setStatus("mandatory")
_EnvTestPt6Measure_Type = Integer32
_EnvTestPt6Measure_Object = MibScalar
envTestPt6Measure = _EnvTestPt6Measure_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 89),
    _EnvTestPt6Measure_Type()
)
envTestPt6Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6Measure.setStatus("mandatory")
_EnvTestPt1MarginVal_Type = Integer32
_EnvTestPt1MarginVal_Object = MibScalar
envTestPt1MarginVal = _EnvTestPt1MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 90),
    _EnvTestPt1MarginVal_Type()
)
envTestPt1MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1MarginVal.setStatus("mandatory")
_EnvTestPt2MarginVal_Type = Integer32
_EnvTestPt2MarginVal_Object = MibScalar
envTestPt2MarginVal = _EnvTestPt2MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 91),
    _EnvTestPt2MarginVal_Type()
)
envTestPt2MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2MarginVal.setStatus("mandatory")
_EnvTestPt3MarginPercent_Type = Integer32
_EnvTestPt3MarginPercent_Object = MibScalar
envTestPt3MarginPercent = _EnvTestPt3MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 92),
    _EnvTestPt3MarginPercent_Type()
)
envTestPt3MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3MarginPercent.setStatus("mandatory")
_EnvTestPt4MarginPercent_Type = Integer32
_EnvTestPt4MarginPercent_Object = MibScalar
envTestPt4MarginPercent = _EnvTestPt4MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 93),
    _EnvTestPt4MarginPercent_Type()
)
envTestPt4MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4MarginPercent.setStatus("mandatory")
_EnvTestPt5MarginPercent_Type = Integer32
_EnvTestPt5MarginPercent_Object = MibScalar
envTestPt5MarginPercent = _EnvTestPt5MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 94),
    _EnvTestPt5MarginPercent_Type()
)
envTestPt5MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5MarginPercent.setStatus("mandatory")
_EnvTestPt6MarginPercent_Type = Integer32
_EnvTestPt6MarginPercent_Object = MibScalar
envTestPt6MarginPercent = _EnvTestPt6MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 95),
    _EnvTestPt6MarginPercent_Type()
)
envTestPt6MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6MarginPercent.setStatus("mandatory")
_EnvTestPt1last_Type = Integer32
_EnvTestPt1last_Object = MibScalar
envTestPt1last = _EnvTestPt1last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 96),
    _EnvTestPt1last_Type()
)
envTestPt1last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1last.setStatus("mandatory")
_EnvTestPt2last_Type = Integer32
_EnvTestPt2last_Object = MibScalar
envTestPt2last = _EnvTestPt2last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 97),
    _EnvTestPt2last_Type()
)
envTestPt2last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2last.setStatus("mandatory")
_EnvTestPt3last_Type = Integer32
_EnvTestPt3last_Object = MibScalar
envTestPt3last = _EnvTestPt3last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 98),
    _EnvTestPt3last_Type()
)
envTestPt3last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3last.setStatus("mandatory")
_EnvTestPt4last_Type = Integer32
_EnvTestPt4last_Object = MibScalar
envTestPt4last = _EnvTestPt4last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 99),
    _EnvTestPt4last_Type()
)
envTestPt4last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4last.setStatus("mandatory")
_EnvTestPt5last_Type = Integer32
_EnvTestPt5last_Object = MibScalar
envTestPt5last = _EnvTestPt5last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 100),
    _EnvTestPt5last_Type()
)
envTestPt5last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5last.setStatus("mandatory")
_EnvTestPt6last_Type = Integer32
_EnvTestPt6last_Object = MibScalar
envTestPt6last = _EnvTestPt6last_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 101),
    _EnvTestPt6last_Type()
)
envTestPt6last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6last.setStatus("mandatory")


class _EnvTestPt1warn_Type(Integer32):
    """Custom type envTestPt1warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt1warn_Type.__name__ = "Integer32"
_EnvTestPt1warn_Object = MibScalar
envTestPt1warn = _EnvTestPt1warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 102),
    _EnvTestPt1warn_Type()
)
envTestPt1warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt1warn.setStatus("mandatory")


class _EnvTestPt2warn_Type(Integer32):
    """Custom type envTestPt2warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt2warn_Type.__name__ = "Integer32"
_EnvTestPt2warn_Object = MibScalar
envTestPt2warn = _EnvTestPt2warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 103),
    _EnvTestPt2warn_Type()
)
envTestPt2warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt2warn.setStatus("mandatory")


class _EnvTestPt3warn_Type(Integer32):
    """Custom type envTestPt3warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt3warn_Type.__name__ = "Integer32"
_EnvTestPt3warn_Object = MibScalar
envTestPt3warn = _EnvTestPt3warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 104),
    _EnvTestPt3warn_Type()
)
envTestPt3warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt3warn.setStatus("mandatory")


class _EnvTestPt4warn_Type(Integer32):
    """Custom type envTestPt4warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt4warn_Type.__name__ = "Integer32"
_EnvTestPt4warn_Object = MibScalar
envTestPt4warn = _EnvTestPt4warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 105),
    _EnvTestPt4warn_Type()
)
envTestPt4warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt4warn.setStatus("mandatory")


class _EnvTestPt5warn_Type(Integer32):
    """Custom type envTestPt5warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt5warn_Type.__name__ = "Integer32"
_EnvTestPt5warn_Object = MibScalar
envTestPt5warn = _EnvTestPt5warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 106),
    _EnvTestPt5warn_Type()
)
envTestPt5warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt5warn.setStatus("mandatory")


class _EnvTestPt6warn_Type(Integer32):
    """Custom type envTestPt6warn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noWarning", 2),
          ("warning", 1))
    )


_EnvTestPt6warn_Type.__name__ = "Integer32"
_EnvTestPt6warn_Object = MibScalar
envTestPt6warn = _EnvTestPt6warn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 107),
    _EnvTestPt6warn_Type()
)
envTestPt6warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTestPt6warn.setStatus("mandatory")
_EnvFirmVersion_Type = DisplayString
_EnvFirmVersion_Object = MibScalar
envFirmVersion = _EnvFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 108),
    _EnvFirmVersion_Type()
)
envFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envFirmVersion.setStatus("mandatory")
_EnvTechnicianID_Type = DisplayString
_EnvTechnicianID_Object = MibScalar
envTechnicianID = _EnvTechnicianID_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 109),
    _EnvTechnicianID_Type()
)
envTechnicianID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTechnicianID.setStatus("mandatory")
_EnvType_Type = DisplayString
_EnvType_Object = MibScalar
envType = _EnvType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 110),
    _EnvType_Type()
)
envType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envType.setStatus("mandatory")
_EnvBurnDate_Type = DisplayString
_EnvBurnDate_Object = MibScalar
envBurnDate = _EnvBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 111),
    _EnvBurnDate_Type()
)
envBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envBurnDate.setStatus("mandatory")
_EnvSerialNumber_Type = DisplayString
_EnvSerialNumber_Object = MibScalar
envSerialNumber = _EnvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 112),
    _EnvSerialNumber_Type()
)
envSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envSerialNumber.setStatus("mandatory")
_Linterfaces_ObjectIdentity = ObjectIdentity
linterfaces = _Linterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 2)
)
_LifTable_Object = MibTable
lifTable = _LifTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lifTable.setStatus("mandatory")
_LifEntry_Object = MibTableRow
lifEntry = _LifEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1)
)
lifEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lifEntry.setStatus("mandatory")
_LocIfHardType_Type = DisplayString
_LocIfHardType_Object = MibTableColumn
locIfHardType = _LocIfHardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 1),
    _LocIfHardType_Type()
)
locIfHardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfHardType.setStatus("mandatory")
_LocIfLineProt_Type = Integer32
_LocIfLineProt_Object = MibTableColumn
locIfLineProt = _LocIfLineProt_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 2),
    _LocIfLineProt_Type()
)
locIfLineProt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLineProt.setStatus("mandatory")
_LocIfLastIn_Type = Integer32
_LocIfLastIn_Object = MibTableColumn
locIfLastIn = _LocIfLastIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 3),
    _LocIfLastIn_Type()
)
locIfLastIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastIn.setStatus("mandatory")
_LocIfLastOut_Type = Integer32
_LocIfLastOut_Object = MibTableColumn
locIfLastOut = _LocIfLastOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 4),
    _LocIfLastOut_Type()
)
locIfLastOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastOut.setStatus("mandatory")
_LocIfLastOutHang_Type = Integer32
_LocIfLastOutHang_Object = MibTableColumn
locIfLastOutHang = _LocIfLastOutHang_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 5),
    _LocIfLastOutHang_Type()
)
locIfLastOutHang.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLastOutHang.setStatus("mandatory")
_LocIfInBitsSec_Type = Integer32
_LocIfInBitsSec_Object = MibTableColumn
locIfInBitsSec = _LocIfInBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 6),
    _LocIfInBitsSec_Type()
)
locIfInBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInBitsSec.setStatus("mandatory")
_LocIfInPktsSec_Type = Integer32
_LocIfInPktsSec_Object = MibTableColumn
locIfInPktsSec = _LocIfInPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 7),
    _LocIfInPktsSec_Type()
)
locIfInPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInPktsSec.setStatus("mandatory")
_LocIfOutBitsSec_Type = Integer32
_LocIfOutBitsSec_Object = MibTableColumn
locIfOutBitsSec = _LocIfOutBitsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 8),
    _LocIfOutBitsSec_Type()
)
locIfOutBitsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutBitsSec.setStatus("mandatory")
_LocIfOutPktsSec_Type = Integer32
_LocIfOutPktsSec_Object = MibTableColumn
locIfOutPktsSec = _LocIfOutPktsSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 9),
    _LocIfOutPktsSec_Type()
)
locIfOutPktsSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutPktsSec.setStatus("mandatory")
_LocIfInRunts_Type = Integer32
_LocIfInRunts_Object = MibTableColumn
locIfInRunts = _LocIfInRunts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 10),
    _LocIfInRunts_Type()
)
locIfInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInRunts.setStatus("mandatory")
_LocIfInGiants_Type = Integer32
_LocIfInGiants_Object = MibTableColumn
locIfInGiants = _LocIfInGiants_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 11),
    _LocIfInGiants_Type()
)
locIfInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInGiants.setStatus("mandatory")
_LocIfInCRC_Type = Integer32
_LocIfInCRC_Object = MibTableColumn
locIfInCRC = _LocIfInCRC_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 12),
    _LocIfInCRC_Type()
)
locIfInCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInCRC.setStatus("mandatory")
_LocIfInFrame_Type = Integer32
_LocIfInFrame_Object = MibTableColumn
locIfInFrame = _LocIfInFrame_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 13),
    _LocIfInFrame_Type()
)
locIfInFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInFrame.setStatus("mandatory")
_LocIfInOverrun_Type = Integer32
_LocIfInOverrun_Object = MibTableColumn
locIfInOverrun = _LocIfInOverrun_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 14),
    _LocIfInOverrun_Type()
)
locIfInOverrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInOverrun.setStatus("mandatory")
_LocIfInIgnored_Type = Integer32
_LocIfInIgnored_Object = MibTableColumn
locIfInIgnored = _LocIfInIgnored_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 15),
    _LocIfInIgnored_Type()
)
locIfInIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInIgnored.setStatus("mandatory")
_LocIfInAbort_Type = Integer32
_LocIfInAbort_Object = MibTableColumn
locIfInAbort = _LocIfInAbort_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 16),
    _LocIfInAbort_Type()
)
locIfInAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInAbort.setStatus("mandatory")
_LocIfResets_Type = Integer32
_LocIfResets_Object = MibTableColumn
locIfResets = _LocIfResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 17),
    _LocIfResets_Type()
)
locIfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfResets.setStatus("mandatory")
_LocIfRestarts_Type = Integer32
_LocIfRestarts_Object = MibTableColumn
locIfRestarts = _LocIfRestarts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 18),
    _LocIfRestarts_Type()
)
locIfRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfRestarts.setStatus("mandatory")
_LocIfKeep_Type = Integer32
_LocIfKeep_Object = MibTableColumn
locIfKeep = _LocIfKeep_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 19),
    _LocIfKeep_Type()
)
locIfKeep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfKeep.setStatus("mandatory")
_LocIfReason_Type = DisplayString
_LocIfReason_Object = MibTableColumn
locIfReason = _LocIfReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 20),
    _LocIfReason_Type()
)
locIfReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfReason.setStatus("mandatory")
_LocIfCarTrans_Type = Integer32
_LocIfCarTrans_Object = MibTableColumn
locIfCarTrans = _LocIfCarTrans_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 21),
    _LocIfCarTrans_Type()
)
locIfCarTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfCarTrans.setStatus("mandatory")
_LocIfReliab_Type = Integer32
_LocIfReliab_Object = MibTableColumn
locIfReliab = _LocIfReliab_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 22),
    _LocIfReliab_Type()
)
locIfReliab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfReliab.setStatus("mandatory")
_LocIfDelay_Type = Integer32
_LocIfDelay_Object = MibTableColumn
locIfDelay = _LocIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 23),
    _LocIfDelay_Type()
)
locIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfDelay.setStatus("mandatory")
_LocIfLoad_Type = Integer32
_LocIfLoad_Object = MibTableColumn
locIfLoad = _LocIfLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 24),
    _LocIfLoad_Type()
)
locIfLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfLoad.setStatus("mandatory")
_LocIfCollisions_Type = Integer32
_LocIfCollisions_Object = MibTableColumn
locIfCollisions = _LocIfCollisions_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 25),
    _LocIfCollisions_Type()
)
locIfCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfCollisions.setStatus("mandatory")
_LocIfInputQueueDrops_Type = Integer32
_LocIfInputQueueDrops_Object = MibTableColumn
locIfInputQueueDrops = _LocIfInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 26),
    _LocIfInputQueueDrops_Type()
)
locIfInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfInputQueueDrops.setStatus("mandatory")
_LocIfOutputQueueDrops_Type = Integer32
_LocIfOutputQueueDrops_Object = MibTableColumn
locIfOutputQueueDrops = _LocIfOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 27),
    _LocIfOutputQueueDrops_Type()
)
locIfOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfOutputQueueDrops.setStatus("mandatory")
_LocIfDescr_Type = DisplayString
_LocIfDescr_Object = MibTableColumn
locIfDescr = _LocIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 28),
    _LocIfDescr_Type()
)
locIfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    locIfDescr.setStatus("mandatory")
_LocIfSlowInPkts_Type = Counter32
_LocIfSlowInPkts_Object = MibTableColumn
locIfSlowInPkts = _LocIfSlowInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 30),
    _LocIfSlowInPkts_Type()
)
locIfSlowInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowInPkts.setStatus("mandatory")
_LocIfSlowOutPkts_Type = Counter32
_LocIfSlowOutPkts_Object = MibTableColumn
locIfSlowOutPkts = _LocIfSlowOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 31),
    _LocIfSlowOutPkts_Type()
)
locIfSlowOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowOutPkts.setStatus("mandatory")
_LocIfSlowInOctets_Type = Counter32
_LocIfSlowInOctets_Object = MibTableColumn
locIfSlowInOctets = _LocIfSlowInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 32),
    _LocIfSlowInOctets_Type()
)
locIfSlowInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowInOctets.setStatus("mandatory")
_LocIfSlowOutOctets_Type = Counter32
_LocIfSlowOutOctets_Object = MibTableColumn
locIfSlowOutOctets = _LocIfSlowOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 33),
    _LocIfSlowOutOctets_Type()
)
locIfSlowOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfSlowOutOctets.setStatus("mandatory")
_LocIfFastInPkts_Type = Counter32
_LocIfFastInPkts_Object = MibTableColumn
locIfFastInPkts = _LocIfFastInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 34),
    _LocIfFastInPkts_Type()
)
locIfFastInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastInPkts.setStatus("mandatory")
_LocIfFastOutPkts_Type = Counter32
_LocIfFastOutPkts_Object = MibTableColumn
locIfFastOutPkts = _LocIfFastOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 35),
    _LocIfFastOutPkts_Type()
)
locIfFastOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastOutPkts.setStatus("mandatory")
_LocIfFastInOctets_Type = Counter32
_LocIfFastInOctets_Object = MibTableColumn
locIfFastInOctets = _LocIfFastInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 36),
    _LocIfFastInOctets_Type()
)
locIfFastInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastInOctets.setStatus("mandatory")
_LocIfFastOutOctets_Type = Counter32
_LocIfFastOutOctets_Object = MibTableColumn
locIfFastOutOctets = _LocIfFastOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 37),
    _LocIfFastOutOctets_Type()
)
locIfFastOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFastOutOctets.setStatus("mandatory")
_LocIfotherInPkts_Type = Counter32
_LocIfotherInPkts_Object = MibTableColumn
locIfotherInPkts = _LocIfotherInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 38),
    _LocIfotherInPkts_Type()
)
locIfotherInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherInPkts.setStatus("mandatory")
_LocIfotherOutPkts_Type = Counter32
_LocIfotherOutPkts_Object = MibTableColumn
locIfotherOutPkts = _LocIfotherOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 39),
    _LocIfotherOutPkts_Type()
)
locIfotherOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherOutPkts.setStatus("mandatory")
_LocIfotherInOctets_Type = Counter32
_LocIfotherInOctets_Object = MibTableColumn
locIfotherInOctets = _LocIfotherInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 40),
    _LocIfotherInOctets_Type()
)
locIfotherInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherInOctets.setStatus("mandatory")
_LocIfotherOutOctets_Type = Counter32
_LocIfotherOutOctets_Object = MibTableColumn
locIfotherOutOctets = _LocIfotherOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 41),
    _LocIfotherOutOctets_Type()
)
locIfotherOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfotherOutOctets.setStatus("mandatory")
_LocIfipInPkts_Type = Counter32
_LocIfipInPkts_Object = MibTableColumn
locIfipInPkts = _LocIfipInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 42),
    _LocIfipInPkts_Type()
)
locIfipInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipInPkts.setStatus("mandatory")
_LocIfipOutPkts_Type = Counter32
_LocIfipOutPkts_Object = MibTableColumn
locIfipOutPkts = _LocIfipOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 43),
    _LocIfipOutPkts_Type()
)
locIfipOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipOutPkts.setStatus("mandatory")
_LocIfipInOctets_Type = Counter32
_LocIfipInOctets_Object = MibTableColumn
locIfipInOctets = _LocIfipInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 44),
    _LocIfipInOctets_Type()
)
locIfipInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipInOctets.setStatus("mandatory")
_LocIfipOutOctets_Type = Counter32
_LocIfipOutOctets_Object = MibTableColumn
locIfipOutOctets = _LocIfipOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 45),
    _LocIfipOutOctets_Type()
)
locIfipOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfipOutOctets.setStatus("mandatory")
_LocIfdecnetInPkts_Type = Counter32
_LocIfdecnetInPkts_Object = MibTableColumn
locIfdecnetInPkts = _LocIfdecnetInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 46),
    _LocIfdecnetInPkts_Type()
)
locIfdecnetInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetInPkts.setStatus("mandatory")
_LocIfdecnetOutPkts_Type = Counter32
_LocIfdecnetOutPkts_Object = MibTableColumn
locIfdecnetOutPkts = _LocIfdecnetOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 47),
    _LocIfdecnetOutPkts_Type()
)
locIfdecnetOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetOutPkts.setStatus("mandatory")
_LocIfdecnetInOctets_Type = Counter32
_LocIfdecnetInOctets_Object = MibTableColumn
locIfdecnetInOctets = _LocIfdecnetInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 48),
    _LocIfdecnetInOctets_Type()
)
locIfdecnetInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetInOctets.setStatus("mandatory")
_LocIfdecnetOutOctets_Type = Counter32
_LocIfdecnetOutOctets_Object = MibTableColumn
locIfdecnetOutOctets = _LocIfdecnetOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 49),
    _LocIfdecnetOutOctets_Type()
)
locIfdecnetOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfdecnetOutOctets.setStatus("mandatory")
_LocIfxnsInPkts_Type = Counter32
_LocIfxnsInPkts_Object = MibTableColumn
locIfxnsInPkts = _LocIfxnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 50),
    _LocIfxnsInPkts_Type()
)
locIfxnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsInPkts.setStatus("mandatory")
_LocIfxnsOutPkts_Type = Counter32
_LocIfxnsOutPkts_Object = MibTableColumn
locIfxnsOutPkts = _LocIfxnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 51),
    _LocIfxnsOutPkts_Type()
)
locIfxnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsOutPkts.setStatus("mandatory")
_LocIfxnsInOctets_Type = Counter32
_LocIfxnsInOctets_Object = MibTableColumn
locIfxnsInOctets = _LocIfxnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 52),
    _LocIfxnsInOctets_Type()
)
locIfxnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsInOctets.setStatus("mandatory")
_LocIfxnsOutOctets_Type = Counter32
_LocIfxnsOutOctets_Object = MibTableColumn
locIfxnsOutOctets = _LocIfxnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 53),
    _LocIfxnsOutOctets_Type()
)
locIfxnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfxnsOutOctets.setStatus("mandatory")
_LocIfclnsInPkts_Type = Counter32
_LocIfclnsInPkts_Object = MibTableColumn
locIfclnsInPkts = _LocIfclnsInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 54),
    _LocIfclnsInPkts_Type()
)
locIfclnsInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsInPkts.setStatus("mandatory")
_LocIfclnsOutPkts_Type = Counter32
_LocIfclnsOutPkts_Object = MibTableColumn
locIfclnsOutPkts = _LocIfclnsOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 55),
    _LocIfclnsOutPkts_Type()
)
locIfclnsOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsOutPkts.setStatus("mandatory")
_LocIfclnsInOctets_Type = Counter32
_LocIfclnsInOctets_Object = MibTableColumn
locIfclnsInOctets = _LocIfclnsInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 56),
    _LocIfclnsInOctets_Type()
)
locIfclnsInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsInOctets.setStatus("mandatory")
_LocIfclnsOutOctets_Type = Counter32
_LocIfclnsOutOctets_Object = MibTableColumn
locIfclnsOutOctets = _LocIfclnsOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 57),
    _LocIfclnsOutOctets_Type()
)
locIfclnsOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfclnsOutOctets.setStatus("mandatory")
_LocIfappletalkInPkts_Type = Counter32
_LocIfappletalkInPkts_Object = MibTableColumn
locIfappletalkInPkts = _LocIfappletalkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 58),
    _LocIfappletalkInPkts_Type()
)
locIfappletalkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkInPkts.setStatus("mandatory")
_LocIfappletalkOutPkts_Type = Counter32
_LocIfappletalkOutPkts_Object = MibTableColumn
locIfappletalkOutPkts = _LocIfappletalkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 59),
    _LocIfappletalkOutPkts_Type()
)
locIfappletalkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkOutPkts.setStatus("mandatory")
_LocIfappletalkInOctets_Type = Counter32
_LocIfappletalkInOctets_Object = MibTableColumn
locIfappletalkInOctets = _LocIfappletalkInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 60),
    _LocIfappletalkInOctets_Type()
)
locIfappletalkInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkInOctets.setStatus("mandatory")
_LocIfappletalkOutOctets_Type = Counter32
_LocIfappletalkOutOctets_Object = MibTableColumn
locIfappletalkOutOctets = _LocIfappletalkOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 61),
    _LocIfappletalkOutOctets_Type()
)
locIfappletalkOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfappletalkOutOctets.setStatus("mandatory")
_LocIfnovellInPkts_Type = Counter32
_LocIfnovellInPkts_Object = MibTableColumn
locIfnovellInPkts = _LocIfnovellInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 62),
    _LocIfnovellInPkts_Type()
)
locIfnovellInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellInPkts.setStatus("mandatory")
_LocIfnovellOutPkts_Type = Counter32
_LocIfnovellOutPkts_Object = MibTableColumn
locIfnovellOutPkts = _LocIfnovellOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 63),
    _LocIfnovellOutPkts_Type()
)
locIfnovellOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellOutPkts.setStatus("mandatory")
_LocIfnovellInOctets_Type = Counter32
_LocIfnovellInOctets_Object = MibTableColumn
locIfnovellInOctets = _LocIfnovellInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 64),
    _LocIfnovellInOctets_Type()
)
locIfnovellInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellInOctets.setStatus("mandatory")
_LocIfnovellOutOctets_Type = Counter32
_LocIfnovellOutOctets_Object = MibTableColumn
locIfnovellOutOctets = _LocIfnovellOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 65),
    _LocIfnovellOutOctets_Type()
)
locIfnovellOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfnovellOutOctets.setStatus("mandatory")
_LocIfapolloInPkts_Type = Counter32
_LocIfapolloInPkts_Object = MibTableColumn
locIfapolloInPkts = _LocIfapolloInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 66),
    _LocIfapolloInPkts_Type()
)
locIfapolloInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloInPkts.setStatus("mandatory")
_LocIfapolloOutPkts_Type = Counter32
_LocIfapolloOutPkts_Object = MibTableColumn
locIfapolloOutPkts = _LocIfapolloOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 67),
    _LocIfapolloOutPkts_Type()
)
locIfapolloOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloOutPkts.setStatus("mandatory")
_LocIfapolloInOctets_Type = Counter32
_LocIfapolloInOctets_Object = MibTableColumn
locIfapolloInOctets = _LocIfapolloInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 68),
    _LocIfapolloInOctets_Type()
)
locIfapolloInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloInOctets.setStatus("mandatory")
_LocIfapolloOutOctets_Type = Counter32
_LocIfapolloOutOctets_Object = MibTableColumn
locIfapolloOutOctets = _LocIfapolloOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 69),
    _LocIfapolloOutOctets_Type()
)
locIfapolloOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfapolloOutOctets.setStatus("mandatory")
_LocIfvinesInPkts_Type = Counter32
_LocIfvinesInPkts_Object = MibTableColumn
locIfvinesInPkts = _LocIfvinesInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 70),
    _LocIfvinesInPkts_Type()
)
locIfvinesInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesInPkts.setStatus("mandatory")
_LocIfvinesOutPkts_Type = Counter32
_LocIfvinesOutPkts_Object = MibTableColumn
locIfvinesOutPkts = _LocIfvinesOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 71),
    _LocIfvinesOutPkts_Type()
)
locIfvinesOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesOutPkts.setStatus("mandatory")
_LocIfvinesInOctets_Type = Counter32
_LocIfvinesInOctets_Object = MibTableColumn
locIfvinesInOctets = _LocIfvinesInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 72),
    _LocIfvinesInOctets_Type()
)
locIfvinesInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesInOctets.setStatus("mandatory")
_LocIfvinesOutOctets_Type = Counter32
_LocIfvinesOutOctets_Object = MibTableColumn
locIfvinesOutOctets = _LocIfvinesOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 73),
    _LocIfvinesOutOctets_Type()
)
locIfvinesOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfvinesOutOctets.setStatus("mandatory")
_LocIfbridgedInPkts_Type = Counter32
_LocIfbridgedInPkts_Object = MibTableColumn
locIfbridgedInPkts = _LocIfbridgedInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 74),
    _LocIfbridgedInPkts_Type()
)
locIfbridgedInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedInPkts.setStatus("mandatory")
_LocIfbridgedOutPkts_Type = Counter32
_LocIfbridgedOutPkts_Object = MibTableColumn
locIfbridgedOutPkts = _LocIfbridgedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 75),
    _LocIfbridgedOutPkts_Type()
)
locIfbridgedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedOutPkts.setStatus("mandatory")
_LocIfbridgedInOctets_Type = Counter32
_LocIfbridgedInOctets_Object = MibTableColumn
locIfbridgedInOctets = _LocIfbridgedInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 76),
    _LocIfbridgedInOctets_Type()
)
locIfbridgedInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedInOctets.setStatus("mandatory")
_LocIfbridgedOutOctets_Type = Counter32
_LocIfbridgedOutOctets_Object = MibTableColumn
locIfbridgedOutOctets = _LocIfbridgedOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 77),
    _LocIfbridgedOutOctets_Type()
)
locIfbridgedOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfbridgedOutOctets.setStatus("mandatory")
_LocIfsrbInPkts_Type = Counter32
_LocIfsrbInPkts_Object = MibTableColumn
locIfsrbInPkts = _LocIfsrbInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 78),
    _LocIfsrbInPkts_Type()
)
locIfsrbInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbInPkts.setStatus("mandatory")
_LocIfsrbOutPkts_Type = Counter32
_LocIfsrbOutPkts_Object = MibTableColumn
locIfsrbOutPkts = _LocIfsrbOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 79),
    _LocIfsrbOutPkts_Type()
)
locIfsrbOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbOutPkts.setStatus("mandatory")
_LocIfsrbInOctets_Type = Counter32
_LocIfsrbInOctets_Object = MibTableColumn
locIfsrbInOctets = _LocIfsrbInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 80),
    _LocIfsrbInOctets_Type()
)
locIfsrbInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbInOctets.setStatus("mandatory")
_LocIfsrbOutOctets_Type = Counter32
_LocIfsrbOutOctets_Object = MibTableColumn
locIfsrbOutOctets = _LocIfsrbOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 81),
    _LocIfsrbOutOctets_Type()
)
locIfsrbOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfsrbOutOctets.setStatus("mandatory")
_LocIfchaosInPkts_Type = Counter32
_LocIfchaosInPkts_Object = MibTableColumn
locIfchaosInPkts = _LocIfchaosInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 82),
    _LocIfchaosInPkts_Type()
)
locIfchaosInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosInPkts.setStatus("mandatory")
_LocIfchaosOutPkts_Type = Counter32
_LocIfchaosOutPkts_Object = MibTableColumn
locIfchaosOutPkts = _LocIfchaosOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 83),
    _LocIfchaosOutPkts_Type()
)
locIfchaosOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosOutPkts.setStatus("mandatory")
_LocIfchaosInOctets_Type = Counter32
_LocIfchaosInOctets_Object = MibTableColumn
locIfchaosInOctets = _LocIfchaosInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 84),
    _LocIfchaosInOctets_Type()
)
locIfchaosInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosInOctets.setStatus("mandatory")
_LocIfchaosOutOctets_Type = Counter32
_LocIfchaosOutOctets_Object = MibTableColumn
locIfchaosOutOctets = _LocIfchaosOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 85),
    _LocIfchaosOutOctets_Type()
)
locIfchaosOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfchaosOutOctets.setStatus("mandatory")
_LocIfpupInPkts_Type = Counter32
_LocIfpupInPkts_Object = MibTableColumn
locIfpupInPkts = _LocIfpupInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 86),
    _LocIfpupInPkts_Type()
)
locIfpupInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupInPkts.setStatus("mandatory")
_LocIfpupOutPkts_Type = Counter32
_LocIfpupOutPkts_Object = MibTableColumn
locIfpupOutPkts = _LocIfpupOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 87),
    _LocIfpupOutPkts_Type()
)
locIfpupOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupOutPkts.setStatus("mandatory")
_LocIfpupInOctets_Type = Counter32
_LocIfpupInOctets_Object = MibTableColumn
locIfpupInOctets = _LocIfpupInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 88),
    _LocIfpupInOctets_Type()
)
locIfpupInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupInOctets.setStatus("mandatory")
_LocIfpupOutOctets_Type = Counter32
_LocIfpupOutOctets_Object = MibTableColumn
locIfpupOutOctets = _LocIfpupOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 89),
    _LocIfpupOutOctets_Type()
)
locIfpupOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfpupOutOctets.setStatus("mandatory")
_LocIfmopInPkts_Type = Counter32
_LocIfmopInPkts_Object = MibTableColumn
locIfmopInPkts = _LocIfmopInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 90),
    _LocIfmopInPkts_Type()
)
locIfmopInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopInPkts.setStatus("mandatory")
_LocIfmopOutPkts_Type = Counter32
_LocIfmopOutPkts_Object = MibTableColumn
locIfmopOutPkts = _LocIfmopOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 91),
    _LocIfmopOutPkts_Type()
)
locIfmopOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopOutPkts.setStatus("mandatory")
_LocIfmopInOctets_Type = Counter32
_LocIfmopInOctets_Object = MibTableColumn
locIfmopInOctets = _LocIfmopInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 92),
    _LocIfmopInOctets_Type()
)
locIfmopInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopInOctets.setStatus("mandatory")
_LocIfmopOutOctets_Type = Counter32
_LocIfmopOutOctets_Object = MibTableColumn
locIfmopOutOctets = _LocIfmopOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 93),
    _LocIfmopOutOctets_Type()
)
locIfmopOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfmopOutOctets.setStatus("mandatory")
_LocIflanmanInPkts_Type = Counter32
_LocIflanmanInPkts_Object = MibTableColumn
locIflanmanInPkts = _LocIflanmanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 94),
    _LocIflanmanInPkts_Type()
)
locIflanmanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanInPkts.setStatus("mandatory")
_LocIflanmanOutPkts_Type = Counter32
_LocIflanmanOutPkts_Object = MibTableColumn
locIflanmanOutPkts = _LocIflanmanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 95),
    _LocIflanmanOutPkts_Type()
)
locIflanmanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanOutPkts.setStatus("mandatory")
_LocIflanmanInOctets_Type = Counter32
_LocIflanmanInOctets_Object = MibTableColumn
locIflanmanInOctets = _LocIflanmanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 96),
    _LocIflanmanInOctets_Type()
)
locIflanmanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanInOctets.setStatus("mandatory")
_LocIflanmanOutOctets_Type = Counter32
_LocIflanmanOutOctets_Object = MibTableColumn
locIflanmanOutOctets = _LocIflanmanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 97),
    _LocIflanmanOutOctets_Type()
)
locIflanmanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIflanmanOutOctets.setStatus("mandatory")
_LocIfstunInPkts_Type = Counter32
_LocIfstunInPkts_Object = MibTableColumn
locIfstunInPkts = _LocIfstunInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 98),
    _LocIfstunInPkts_Type()
)
locIfstunInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunInPkts.setStatus("mandatory")
_LocIfstunOutPkts_Type = Counter32
_LocIfstunOutPkts_Object = MibTableColumn
locIfstunOutPkts = _LocIfstunOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 99),
    _LocIfstunOutPkts_Type()
)
locIfstunOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunOutPkts.setStatus("mandatory")
_LocIfstunInOctets_Type = Counter32
_LocIfstunInOctets_Object = MibTableColumn
locIfstunInOctets = _LocIfstunInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 100),
    _LocIfstunInOctets_Type()
)
locIfstunInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunInOctets.setStatus("mandatory")
_LocIfstunOutOctets_Type = Counter32
_LocIfstunOutOctets_Object = MibTableColumn
locIfstunOutOctets = _LocIfstunOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 101),
    _LocIfstunOutOctets_Type()
)
locIfstunOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfstunOutOctets.setStatus("mandatory")
_LocIfspanInPkts_Type = Counter32
_LocIfspanInPkts_Object = MibTableColumn
locIfspanInPkts = _LocIfspanInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 102),
    _LocIfspanInPkts_Type()
)
locIfspanInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanInPkts.setStatus("mandatory")
_LocIfspanOutPkts_Type = Counter32
_LocIfspanOutPkts_Object = MibTableColumn
locIfspanOutPkts = _LocIfspanOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 103),
    _LocIfspanOutPkts_Type()
)
locIfspanOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanOutPkts.setStatus("mandatory")
_LocIfspanInOctets_Type = Counter32
_LocIfspanInOctets_Object = MibTableColumn
locIfspanInOctets = _LocIfspanInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 104),
    _LocIfspanInOctets_Type()
)
locIfspanInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanInOctets.setStatus("mandatory")
_LocIfspanOutOctets_Type = Counter32
_LocIfspanOutOctets_Object = MibTableColumn
locIfspanOutOctets = _LocIfspanOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 105),
    _LocIfspanOutOctets_Type()
)
locIfspanOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfspanOutOctets.setStatus("mandatory")
_LocIfarpInPkts_Type = Counter32
_LocIfarpInPkts_Object = MibTableColumn
locIfarpInPkts = _LocIfarpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 106),
    _LocIfarpInPkts_Type()
)
locIfarpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpInPkts.setStatus("mandatory")
_LocIfarpOutPkts_Type = Counter32
_LocIfarpOutPkts_Object = MibTableColumn
locIfarpOutPkts = _LocIfarpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 107),
    _LocIfarpOutPkts_Type()
)
locIfarpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpOutPkts.setStatus("mandatory")
_LocIfarpInOctets_Type = Counter32
_LocIfarpInOctets_Object = MibTableColumn
locIfarpInOctets = _LocIfarpInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 108),
    _LocIfarpInOctets_Type()
)
locIfarpInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpInOctets.setStatus("mandatory")
_LocIfarpOutOctets_Type = Counter32
_LocIfarpOutOctets_Object = MibTableColumn
locIfarpOutOctets = _LocIfarpOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 109),
    _LocIfarpOutOctets_Type()
)
locIfarpOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfarpOutOctets.setStatus("mandatory")
_LocIfprobeInPkts_Type = Counter32
_LocIfprobeInPkts_Object = MibTableColumn
locIfprobeInPkts = _LocIfprobeInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 110),
    _LocIfprobeInPkts_Type()
)
locIfprobeInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeInPkts.setStatus("mandatory")
_LocIfprobeOutPkts_Type = Counter32
_LocIfprobeOutPkts_Object = MibTableColumn
locIfprobeOutPkts = _LocIfprobeOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 111),
    _LocIfprobeOutPkts_Type()
)
locIfprobeOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeOutPkts.setStatus("mandatory")
_LocIfprobeInOctets_Type = Counter32
_LocIfprobeInOctets_Object = MibTableColumn
locIfprobeInOctets = _LocIfprobeInOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 112),
    _LocIfprobeInOctets_Type()
)
locIfprobeInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeInOctets.setStatus("mandatory")
_LocIfprobeOutOctets_Type = Counter32
_LocIfprobeOutOctets_Object = MibTableColumn
locIfprobeOutOctets = _LocIfprobeOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 113),
    _LocIfprobeOutOctets_Type()
)
locIfprobeOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfprobeOutOctets.setStatus("mandatory")
_LocIfDribbleInputs_Type = Counter32
_LocIfDribbleInputs_Object = MibTableColumn
locIfDribbleInputs = _LocIfDribbleInputs_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 1, 1, 114),
    _LocIfDribbleInputs_Type()
)
locIfDribbleInputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfDribbleInputs.setStatus("mandatory")
_LfsipTable_Object = MibTable
lfsipTable = _LfsipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2)
)
if mibBuilder.loadTexts:
    lfsipTable.setStatus("mandatory")
_LFSIPEntry_Object = MibTableRow
lFSIPEntry = _LFSIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1)
)
lFSIPEntry.setIndexNames(
    (0, "CISCO-MIB", "locIfFSIPIndex"),
)
if mibBuilder.loadTexts:
    lFSIPEntry.setStatus("mandatory")
_LocIfFSIPIndex_Type = Integer32
_LocIfFSIPIndex_Object = MibTableColumn
locIfFSIPIndex = _LocIfFSIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 1),
    _LocIfFSIPIndex_Type()
)
locIfFSIPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPIndex.setStatus("mandatory")


class _LocIfFSIPtype_Type(Integer32):
    """Custom type locIfFSIPtype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("notAvailable", 1))
    )


_LocIfFSIPtype_Type.__name__ = "Integer32"
_LocIfFSIPtype_Object = MibTableColumn
locIfFSIPtype = _LocIfFSIPtype_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 2),
    _LocIfFSIPtype_Type()
)
locIfFSIPtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPtype.setStatus("mandatory")


class _LocIfFSIPrts_Type(Integer32):
    """Custom type locIfFSIPrts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPrts_Type.__name__ = "Integer32"
_LocIfFSIPrts_Object = MibTableColumn
locIfFSIPrts = _LocIfFSIPrts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 3),
    _LocIfFSIPrts_Type()
)
locIfFSIPrts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPrts.setStatus("mandatory")


class _LocIfFSIPcts_Type(Integer32):
    """Custom type locIfFSIPcts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPcts_Type.__name__ = "Integer32"
_LocIfFSIPcts_Object = MibTableColumn
locIfFSIPcts = _LocIfFSIPcts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 4),
    _LocIfFSIPcts_Type()
)
locIfFSIPcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPcts.setStatus("mandatory")


class _LocIfFSIPdtr_Type(Integer32):
    """Custom type locIfFSIPdtr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdtr_Type.__name__ = "Integer32"
_LocIfFSIPdtr_Object = MibTableColumn
locIfFSIPdtr = _LocIfFSIPdtr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 5),
    _LocIfFSIPdtr_Type()
)
locIfFSIPdtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdtr.setStatus("mandatory")


class _LocIfFSIPdcd_Type(Integer32):
    """Custom type locIfFSIPdcd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdcd_Type.__name__ = "Integer32"
_LocIfFSIPdcd_Object = MibTableColumn
locIfFSIPdcd = _LocIfFSIPdcd_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 6),
    _LocIfFSIPdcd_Type()
)
locIfFSIPdcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdcd.setStatus("mandatory")


class _LocIfFSIPdsr_Type(Integer32):
    """Custom type locIfFSIPdsr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("notAvailable", 1),
          ("up", 2))
    )


_LocIfFSIPdsr_Type.__name__ = "Integer32"
_LocIfFSIPdsr_Object = MibTableColumn
locIfFSIPdsr = _LocIfFSIPdsr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 2, 2, 1, 7),
    _LocIfFSIPdsr_Type()
)
locIfFSIPdsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIfFSIPdsr.setStatus("mandatory")
_Lat_ObjectIdentity = ObjectIdentity
lat = _Lat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 3)
)
_Lip_ObjectIdentity = ObjectIdentity
lip = _Lip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 4)
)
_LipAddrTable_Object = MibTable
lipAddrTable = _LipAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1)
)
if mibBuilder.loadTexts:
    lipAddrTable.setStatus("mandatory")
_LipAddrEntry_Object = MibTableRow
lipAddrEntry = _LipAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1)
)
lipAddrEntry.setIndexNames(
    (0, "IP-MIB", "ipAdEntAddr"),
)
if mibBuilder.loadTexts:
    lipAddrEntry.setStatus("mandatory")
_LocIPHow_Type = DisplayString
_LocIPHow_Object = MibTableColumn
locIPHow = _LocIPHow_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 1),
    _LocIPHow_Type()
)
locIPHow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPHow.setStatus("mandatory")
_LocIPWho_Type = IpAddress
_LocIPWho_Object = MibTableColumn
locIPWho = _LocIPWho_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 2),
    _LocIPWho_Type()
)
locIPWho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPWho.setStatus("mandatory")
_LocIPHelper_Type = IpAddress
_LocIPHelper_Object = MibTableColumn
locIPHelper = _LocIPHelper_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 3),
    _LocIPHelper_Type()
)
locIPHelper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPHelper.setStatus("mandatory")
_LocIPSecurity_Type = Integer32
_LocIPSecurity_Object = MibTableColumn
locIPSecurity = _LocIPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 4),
    _LocIPSecurity_Type()
)
locIPSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPSecurity.setStatus("mandatory")
_LocIPRedirects_Type = Integer32
_LocIPRedirects_Object = MibTableColumn
locIPRedirects = _LocIPRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 5),
    _LocIPRedirects_Type()
)
locIPRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPRedirects.setStatus("mandatory")
_LocIPUnreach_Type = Integer32
_LocIPUnreach_Object = MibTableColumn
locIPUnreach = _LocIPUnreach_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 1, 1, 6),
    _LocIPUnreach_Type()
)
locIPUnreach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locIPUnreach.setStatus("mandatory")
_LipRoutingTable_Object = MibTable
lipRoutingTable = _LipRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2)
)
if mibBuilder.loadTexts:
    lipRoutingTable.setStatus("mandatory")
_LipRouteEntry_Object = MibTableRow
lipRouteEntry = _LipRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1)
)
lipRouteEntry.setIndexNames(
    (0, "RFC1213-MIB", "ipRouteDest"),
)
if mibBuilder.loadTexts:
    lipRouteEntry.setStatus("mandatory")
_LocRtMask_Type = IpAddress
_LocRtMask_Object = MibTableColumn
locRtMask = _LocRtMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 1),
    _LocRtMask_Type()
)
locRtMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtMask.setStatus("mandatory")
_LocRtCount_Type = Integer32
_LocRtCount_Object = MibTableColumn
locRtCount = _LocRtCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 2),
    _LocRtCount_Type()
)
locRtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtCount.setStatus("mandatory")
_LocRtUses_Type = Integer32
_LocRtUses_Object = MibTableColumn
locRtUses = _LocRtUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 2, 1, 3),
    _LocRtUses_Type()
)
locRtUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locRtUses.setStatus("mandatory")
_ActThresh_Type = Integer32
_ActThresh_Object = MibScalar
actThresh = _ActThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 4),
    _ActThresh_Type()
)
actThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actThresh.setStatus("mandatory")
_ActLostPkts_Type = Integer32
_ActLostPkts_Object = MibScalar
actLostPkts = _ActLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 5),
    _ActLostPkts_Type()
)
actLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actLostPkts.setStatus("mandatory")
_ActLostByts_Type = Integer32
_ActLostByts_Object = MibScalar
actLostByts = _ActLostByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 6),
    _ActLostByts_Type()
)
actLostByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actLostByts.setStatus("mandatory")
_LipAccountingTable_Object = MibTable
lipAccountingTable = _LipAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7)
)
if mibBuilder.loadTexts:
    lipAccountingTable.setStatus("mandatory")
_LipAccountEntry_Object = MibTableRow
lipAccountEntry = _LipAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1)
)
lipAccountEntry.setIndexNames(
    (0, "CISCO-MIB", "actSrc"),
    (0, "CISCO-MIB", "actDst"),
)
if mibBuilder.loadTexts:
    lipAccountEntry.setStatus("mandatory")
_ActSrc_Type = IpAddress
_ActSrc_Object = MibTableColumn
actSrc = _ActSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 1),
    _ActSrc_Type()
)
actSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actSrc.setStatus("mandatory")
_ActDst_Type = IpAddress
_ActDst_Object = MibTableColumn
actDst = _ActDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 2),
    _ActDst_Type()
)
actDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actDst.setStatus("mandatory")
_ActPkts_Type = Integer32
_ActPkts_Object = MibTableColumn
actPkts = _ActPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 3),
    _ActPkts_Type()
)
actPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actPkts.setStatus("mandatory")
_ActByts_Type = Integer32
_ActByts_Object = MibTableColumn
actByts = _ActByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 7, 1, 4),
    _ActByts_Type()
)
actByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actByts.setStatus("mandatory")
_ActAge_Type = TimeTicks
_ActAge_Object = MibScalar
actAge = _ActAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 8),
    _ActAge_Type()
)
actAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actAge.setStatus("mandatory")
_LipCkAccountingTable_Object = MibTable
lipCkAccountingTable = _LipCkAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9)
)
if mibBuilder.loadTexts:
    lipCkAccountingTable.setStatus("mandatory")
_LipCkAccountEntry_Object = MibTableRow
lipCkAccountEntry = _LipCkAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1)
)
lipCkAccountEntry.setIndexNames(
    (0, "CISCO-MIB", "ckactSrc"),
    (0, "CISCO-MIB", "ckactDst"),
)
if mibBuilder.loadTexts:
    lipCkAccountEntry.setStatus("mandatory")
_CkactSrc_Type = IpAddress
_CkactSrc_Object = MibTableColumn
ckactSrc = _CkactSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 1),
    _CkactSrc_Type()
)
ckactSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactSrc.setStatus("mandatory")
_CkactDst_Type = IpAddress
_CkactDst_Object = MibTableColumn
ckactDst = _CkactDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 2),
    _CkactDst_Type()
)
ckactDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactDst.setStatus("mandatory")
_CkactPkts_Type = Integer32
_CkactPkts_Object = MibTableColumn
ckactPkts = _CkactPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 3),
    _CkactPkts_Type()
)
ckactPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactPkts.setStatus("mandatory")
_CkactByts_Type = Integer32
_CkactByts_Object = MibTableColumn
ckactByts = _CkactByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 9, 1, 4),
    _CkactByts_Type()
)
ckactByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactByts.setStatus("mandatory")
_CkactAge_Type = TimeTicks
_CkactAge_Object = MibScalar
ckactAge = _CkactAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 10),
    _CkactAge_Type()
)
ckactAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ckactAge.setStatus("mandatory")
_ActCheckPoint_Type = Integer32
_ActCheckPoint_Object = MibScalar
actCheckPoint = _ActCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 11),
    _ActCheckPoint_Type()
)
actCheckPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actCheckPoint.setStatus("mandatory")
_IpNoaccess_Type = Counter32
_IpNoaccess_Object = MibScalar
ipNoaccess = _IpNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 4, 12),
    _IpNoaccess_Type()
)
ipNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNoaccess.setStatus("mandatory")
_Licmp_ObjectIdentity = ObjectIdentity
licmp = _Licmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 5)
)
_Ltcp_ObjectIdentity = ObjectIdentity
ltcp = _Ltcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 6)
)
_LtcpConnTable_Object = MibTable
ltcpConnTable = _LtcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ltcpConnTable.setStatus("mandatory")
_LtcpConnEntry_Object = MibTableRow
ltcpConnEntry = _LtcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1)
)
ltcpConnEntry.setIndexNames(
    (0, "TCP-MIB", "tcpConnLocalAddress"),
    (0, "TCP-MIB", "tcpConnLocalPort"),
    (0, "TCP-MIB", "tcpConnRemAddress"),
    (0, "TCP-MIB", "tcpConnRemPort"),
)
if mibBuilder.loadTexts:
    ltcpConnEntry.setStatus("mandatory")
_LoctcpConnInBytes_Type = Integer32
_LoctcpConnInBytes_Object = MibTableColumn
loctcpConnInBytes = _LoctcpConnInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 1),
    _LoctcpConnInBytes_Type()
)
loctcpConnInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnInBytes.setStatus("mandatory")
_LoctcpConnOutBytes_Type = Integer32
_LoctcpConnOutBytes_Object = MibTableColumn
loctcpConnOutBytes = _LoctcpConnOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 2),
    _LoctcpConnOutBytes_Type()
)
loctcpConnOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnOutBytes.setStatus("mandatory")
_LoctcpConnInPkts_Type = Integer32
_LoctcpConnInPkts_Object = MibTableColumn
loctcpConnInPkts = _LoctcpConnInPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 3),
    _LoctcpConnInPkts_Type()
)
loctcpConnInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnInPkts.setStatus("mandatory")
_LoctcpConnOutPkts_Type = Integer32
_LoctcpConnOutPkts_Object = MibTableColumn
loctcpConnOutPkts = _LoctcpConnOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 4),
    _LoctcpConnOutPkts_Type()
)
loctcpConnOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnOutPkts.setStatus("mandatory")
_LoctcpConnElapsed_Type = TimeTicks
_LoctcpConnElapsed_Object = MibTableColumn
loctcpConnElapsed = _LoctcpConnElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 6, 1, 1, 5),
    _LoctcpConnElapsed_Type()
)
loctcpConnElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    loctcpConnElapsed.setStatus("mandatory")
_Ludp_ObjectIdentity = ObjectIdentity
ludp = _Ludp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 7)
)
_Legp_ObjectIdentity = ObjectIdentity
legp = _Legp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 8)
)
_Lts_ObjectIdentity = ObjectIdentity
lts = _Lts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 9)
)
_TsLines_Type = Integer32
_TsLines_Object = MibScalar
tsLines = _TsLines_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 1),
    _TsLines_Type()
)
tsLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLines.setStatus("mandatory")
_LtsLineTable_Object = MibTable
ltsLineTable = _LtsLineTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2)
)
if mibBuilder.loadTexts:
    ltsLineTable.setStatus("mandatory")
_LtsLineEntry_Object = MibTableRow
ltsLineEntry = _LtsLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1)
)
ltsLineEntry.setIndexNames(
    (0, "CISCO-MIB", "tsLineNum"),
)
if mibBuilder.loadTexts:
    ltsLineEntry.setStatus("mandatory")
_TsLineActive_Type = Integer32
_TsLineActive_Object = MibTableColumn
tsLineActive = _TsLineActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 1),
    _TsLineActive_Type()
)
tsLineActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineActive.setStatus("mandatory")


class _TsLineType_Type(Integer32):
    """Custom type tsLineType based on Integer32"""
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
        *(("auxiliary", 6),
          ("console", 2),
          ("line-printer", 4),
          ("terminal", 3),
          ("unknown", 1),
          ("virtual-terminal", 5))
    )


_TsLineType_Type.__name__ = "Integer32"
_TsLineType_Object = MibTableColumn
tsLineType = _TsLineType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 2),
    _TsLineType_Type()
)
tsLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineType.setStatus("mandatory")
_TsLineAutobaud_Type = Integer32
_TsLineAutobaud_Object = MibTableColumn
tsLineAutobaud = _TsLineAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 3),
    _TsLineAutobaud_Type()
)
tsLineAutobaud.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineAutobaud.setStatus("mandatory")
_TsLineSpeedin_Type = Integer32
_TsLineSpeedin_Object = MibTableColumn
tsLineSpeedin = _TsLineSpeedin_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 4),
    _TsLineSpeedin_Type()
)
tsLineSpeedin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSpeedin.setStatus("mandatory")
_TsLineSpeedout_Type = Integer32
_TsLineSpeedout_Object = MibTableColumn
tsLineSpeedout = _TsLineSpeedout_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 5),
    _TsLineSpeedout_Type()
)
tsLineSpeedout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSpeedout.setStatus("mandatory")


class _TsLineFlow_Type(Integer32):
    """Custom type tsLineFlow based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("hardware-both", 8),
          ("hardware-input", 6),
          ("hardware-output", 7),
          ("none", 2),
          ("software-both", 5),
          ("software-input", 3),
          ("software-output", 4),
          ("unknown", 1))
    )


_TsLineFlow_Type.__name__ = "Integer32"
_TsLineFlow_Object = MibTableColumn
tsLineFlow = _TsLineFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 6),
    _TsLineFlow_Type()
)
tsLineFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineFlow.setStatus("mandatory")


class _TsLineModem_Type(Integer32):
    """Custom type tsLineModem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("call-in", 3),
          ("call-out", 4),
          ("cts-required", 5),
          ("inout", 7),
          ("none", 2),
          ("ri-is-cd", 6),
          ("unknown", 1))
    )


_TsLineModem_Type.__name__ = "Integer32"
_TsLineModem_Object = MibTableColumn
tsLineModem = _TsLineModem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 7),
    _TsLineModem_Type()
)
tsLineModem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineModem.setStatus("mandatory")
_TsLineLoc_Type = DisplayString
_TsLineLoc_Object = MibTableColumn
tsLineLoc = _TsLineLoc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 8),
    _TsLineLoc_Type()
)
tsLineLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineLoc.setStatus("mandatory")
_TsLineTerm_Type = DisplayString
_TsLineTerm_Object = MibTableColumn
tsLineTerm = _TsLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 9),
    _TsLineTerm_Type()
)
tsLineTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineTerm.setStatus("mandatory")
_TsLineScrlen_Type = Integer32
_TsLineScrlen_Object = MibTableColumn
tsLineScrlen = _TsLineScrlen_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 10),
    _TsLineScrlen_Type()
)
tsLineScrlen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineScrlen.setStatus("mandatory")
_TsLineScrwid_Type = Integer32
_TsLineScrwid_Object = MibTableColumn
tsLineScrwid = _TsLineScrwid_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 11),
    _TsLineScrwid_Type()
)
tsLineScrwid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineScrwid.setStatus("mandatory")
_TsLineEsc_Type = DisplayString
_TsLineEsc_Object = MibTableColumn
tsLineEsc = _TsLineEsc_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 12),
    _TsLineEsc_Type()
)
tsLineEsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineEsc.setStatus("mandatory")
_TsLineTmo_Type = Integer32
_TsLineTmo_Object = MibTableColumn
tsLineTmo = _TsLineTmo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 13),
    _TsLineTmo_Type()
)
tsLineTmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineTmo.setStatus("mandatory")
_TsLineSestmo_Type = Integer32
_TsLineSestmo_Object = MibTableColumn
tsLineSestmo = _TsLineSestmo_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 14),
    _TsLineSestmo_Type()
)
tsLineSestmo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineSestmo.setStatus("mandatory")
_TsLineRotary_Type = Integer32
_TsLineRotary_Object = MibTableColumn
tsLineRotary = _TsLineRotary_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 15),
    _TsLineRotary_Type()
)
tsLineRotary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineRotary.setStatus("mandatory")
_TsLineUses_Type = Integer32
_TsLineUses_Object = MibTableColumn
tsLineUses = _TsLineUses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 16),
    _TsLineUses_Type()
)
tsLineUses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineUses.setStatus("mandatory")
_TsLineNses_Type = Integer32
_TsLineNses_Object = MibTableColumn
tsLineNses = _TsLineNses_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 17),
    _TsLineNses_Type()
)
tsLineNses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineNses.setStatus("mandatory")
_TsLineUser_Type = DisplayString
_TsLineUser_Object = MibTableColumn
tsLineUser = _TsLineUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 18),
    _TsLineUser_Type()
)
tsLineUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineUser.setStatus("mandatory")
_TsLineNoise_Type = Integer32
_TsLineNoise_Object = MibTableColumn
tsLineNoise = _TsLineNoise_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 19),
    _TsLineNoise_Type()
)
tsLineNoise.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tsLineNoise.setStatus("mandatory")
_TsLineNum_Type = Integer32
_TsLineNum_Object = MibTableColumn
tsLineNum = _TsLineNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 2, 1, 20),
    _TsLineNum_Type()
)
tsLineNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tsLineNum.setStatus("mandatory")
_LtsLineSessionTable_Object = MibTable
ltsLineSessionTable = _LtsLineSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3)
)
if mibBuilder.loadTexts:
    ltsLineSessionTable.setStatus("mandatory")
_LtsLineSessionEntry_Object = MibTableRow
ltsLineSessionEntry = _LtsLineSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1)
)
ltsLineSessionEntry.setIndexNames(
    (0, "CISCO-MIB", "tslineSesLine"),
    (0, "CISCO-MIB", "tslineSesSession"),
)
if mibBuilder.loadTexts:
    ltsLineSessionEntry.setStatus("mandatory")


class _TslineSesType_Type(Integer32):
    """Custom type tslineSesType based on Integer32"""
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
        *(("lat", 7),
          ("mop", 8),
          ("pad", 2),
          ("rlogin", 4),
          ("rshell", 11),
          ("slip", 9),
          ("stream", 3),
          ("tcp", 6),
          ("telnet", 5),
          ("unknown", 1),
          ("xremote", 10))
    )


_TslineSesType_Type.__name__ = "Integer32"
_TslineSesType_Object = MibTableColumn
tslineSesType = _TslineSesType_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 1),
    _TslineSesType_Type()
)
tslineSesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesType.setStatus("mandatory")


class _TslineSesDir_Type(Integer32):
    """Custom type tslineSesDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("outgoing", 3),
          ("unknown", 1))
    )


_TslineSesDir_Type.__name__ = "Integer32"
_TslineSesDir_Object = MibTableColumn
tslineSesDir = _TslineSesDir_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 2),
    _TslineSesDir_Type()
)
tslineSesDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesDir.setStatus("mandatory")
_TslineSesAddr_Type = IpAddress
_TslineSesAddr_Object = MibTableColumn
tslineSesAddr = _TslineSesAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 3),
    _TslineSesAddr_Type()
)
tslineSesAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesAddr.setStatus("mandatory")
_TslineSesName_Type = DisplayString
_TslineSesName_Object = MibTableColumn
tslineSesName = _TslineSesName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 4),
    _TslineSesName_Type()
)
tslineSesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesName.setStatus("mandatory")
_TslineSesCur_Type = Integer32
_TslineSesCur_Object = MibTableColumn
tslineSesCur = _TslineSesCur_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 5),
    _TslineSesCur_Type()
)
tslineSesCur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesCur.setStatus("mandatory")
_TslineSesIdle_Type = Integer32
_TslineSesIdle_Object = MibTableColumn
tslineSesIdle = _TslineSesIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 6),
    _TslineSesIdle_Type()
)
tslineSesIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tslineSesIdle.setStatus("mandatory")
_TslineSesLine_Type = Integer32
_TslineSesLine_Object = MibTableColumn
tslineSesLine = _TslineSesLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 7),
    _TslineSesLine_Type()
)
tslineSesLine.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tslineSesLine.setStatus("mandatory")
_TslineSesSession_Type = Integer32
_TslineSesSession_Object = MibTableColumn
tslineSesSession = _TslineSesSession_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 3, 1, 8),
    _TslineSesSession_Type()
)
tslineSesSession.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tslineSesSession.setStatus("mandatory")
_TsMsgTtyLine_Type = Integer32
_TsMsgTtyLine_Object = MibScalar
tsMsgTtyLine = _TsMsgTtyLine_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 4),
    _TsMsgTtyLine_Type()
)
tsMsgTtyLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgTtyLine.setStatus("mandatory")
_TsMsgIntervaltim_Type = Integer32
_TsMsgIntervaltim_Object = MibScalar
tsMsgIntervaltim = _TsMsgIntervaltim_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 5),
    _TsMsgIntervaltim_Type()
)
tsMsgIntervaltim.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgIntervaltim.setStatus("mandatory")
_TsMsgDuration_Type = Integer32
_TsMsgDuration_Object = MibScalar
tsMsgDuration = _TsMsgDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 6),
    _TsMsgDuration_Type()
)
tsMsgDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgDuration.setStatus("mandatory")
_TsMsgText_Type = DisplayString
_TsMsgText_Object = MibScalar
tsMsgText = _TsMsgText_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 7),
    _TsMsgText_Type()
)
tsMsgText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgText.setStatus("mandatory")


class _TsMsgTmpBanner_Type(Integer32):
    """Custom type tsMsgTmpBanner based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("additive", 2),
          ("no", 1))
    )


_TsMsgTmpBanner_Type.__name__ = "Integer32"
_TsMsgTmpBanner_Object = MibScalar
tsMsgTmpBanner = _TsMsgTmpBanner_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 8),
    _TsMsgTmpBanner_Type()
)
tsMsgTmpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgTmpBanner.setStatus("mandatory")


class _TsMsgSend_Type(Integer32):
    """Custom type tsMsgSend based on Integer32"""
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
        *(("abort", 4),
          ("messagedone", 3),
          ("nothing", 1),
          ("reload", 2))
    )


_TsMsgSend_Type.__name__ = "Integer32"
_TsMsgSend_Object = MibScalar
tsMsgSend = _TsMsgSend_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 9, 9),
    _TsMsgSend_Type()
)
tsMsgSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tsMsgSend.setStatus("mandatory")
_Lflash_ObjectIdentity = ObjectIdentity
lflash = _Lflash_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 2, 10)
)
_FlashSize_Type = Integer32
_FlashSize_Object = MibScalar
flashSize = _FlashSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 1),
    _FlashSize_Type()
)
flashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashSize.setStatus("mandatory")
_FlashFree_Type = Integer32
_FlashFree_Object = MibScalar
flashFree = _FlashFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 2),
    _FlashFree_Type()
)
flashFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashFree.setStatus("mandatory")
_FlashController_Type = DisplayString
_FlashController_Object = MibScalar
flashController = _FlashController_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 3),
    _FlashController_Type()
)
flashController.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashController.setStatus("mandatory")
_FlashCard_Type = DisplayString
_FlashCard_Object = MibScalar
flashCard = _FlashCard_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 4),
    _FlashCard_Type()
)
flashCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashCard.setStatus("mandatory")


class _FlashVPP_Type(Integer32):
    """Custom type flashVPP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("installed", 1),
          ("missing", 2))
    )


_FlashVPP_Type.__name__ = "Integer32"
_FlashVPP_Object = MibScalar
flashVPP = _FlashVPP_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 5),
    _FlashVPP_Type()
)
flashVPP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashVPP.setStatus("mandatory")
_FlashErase_Type = Integer32
_FlashErase_Object = MibScalar
flashErase = _FlashErase_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 6),
    _FlashErase_Type()
)
flashErase.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashErase.setStatus("mandatory")
_FlashEraseTime_Type = TimeTicks
_FlashEraseTime_Object = MibScalar
flashEraseTime = _FlashEraseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 7),
    _FlashEraseTime_Type()
)
flashEraseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseTime.setStatus("mandatory")


class _FlashEraseStatus_Type(Integer32):
    """Custom type flashEraseStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4))
    )


_FlashEraseStatus_Type.__name__ = "Integer32"
_FlashEraseStatus_Object = MibScalar
flashEraseStatus = _FlashEraseStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 8),
    _FlashEraseStatus_Type()
)
flashEraseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEraseStatus.setStatus("mandatory")
_FlashToNet_Type = DisplayString
_FlashToNet_Object = MibScalar
flashToNet = _FlashToNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 9),
    _FlashToNet_Type()
)
flashToNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    flashToNet.setStatus("mandatory")
_FlashToNetTime_Type = TimeTicks
_FlashToNetTime_Object = MibScalar
flashToNetTime = _FlashToNetTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 10),
    _FlashToNetTime_Type()
)
flashToNetTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetTime.setStatus("mandatory")


class _FlashToNetStatus_Type(Integer32):
    """Custom type flashToNetStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4))
    )


_FlashToNetStatus_Type.__name__ = "Integer32"
_FlashToNetStatus_Object = MibScalar
flashToNetStatus = _FlashToNetStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 11),
    _FlashToNetStatus_Type()
)
flashToNetStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashToNetStatus.setStatus("mandatory")
_NetToFlash_Type = DisplayString
_NetToFlash_Object = MibScalar
netToFlash = _NetToFlash_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 12),
    _NetToFlash_Type()
)
netToFlash.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    netToFlash.setStatus("mandatory")
_NetToFlashTime_Type = TimeTicks
_NetToFlashTime_Object = MibScalar
netToFlashTime = _NetToFlashTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 13),
    _NetToFlashTime_Type()
)
netToFlashTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashTime.setStatus("mandatory")


class _NetToFlashStatus_Type(Integer32):
    """Custom type netToFlashStatus based on Integer32"""
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
        *(("bufferAllocationFailure", 6),
          ("flashOpFailure", 3),
          ("flashOpInProgress", 1),
          ("flashOpSuccess", 2),
          ("flashOpenFailure", 5),
          ("flashReadOnly", 4))
    )


_NetToFlashStatus_Type.__name__ = "Integer32"
_NetToFlashStatus_Object = MibScalar
netToFlashStatus = _NetToFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 14),
    _NetToFlashStatus_Type()
)
netToFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netToFlashStatus.setStatus("mandatory")


class _FlashStatus_Type(Integer32):
    """Custom type flashStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("available", 2),
          ("busy", 1))
    )


_FlashStatus_Type.__name__ = "Integer32"
_FlashStatus_Object = MibScalar
flashStatus = _FlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 15),
    _FlashStatus_Type()
)
flashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashStatus.setStatus("mandatory")
_FlashEntries_Type = Integer32
_FlashEntries_Object = MibScalar
flashEntries = _FlashEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 16),
    _FlashEntries_Type()
)
flashEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashEntries.setStatus("mandatory")
_LflashFileDirTable_Object = MibTable
lflashFileDirTable = _LflashFileDirTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17)
)
if mibBuilder.loadTexts:
    lflashFileDirTable.setStatus("mandatory")
_LflashFileDirEntry_Object = MibTableRow
lflashFileDirEntry = _LflashFileDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1)
)
lflashFileDirEntry.setIndexNames(
    (0, "CISCO-MIB", "flashEntries"),
)
if mibBuilder.loadTexts:
    lflashFileDirEntry.setStatus("mandatory")
_FlashDirName_Type = DisplayString
_FlashDirName_Object = MibTableColumn
flashDirName = _FlashDirName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 1),
    _FlashDirName_Type()
)
flashDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirName.setStatus("mandatory")
_FlashDirSize_Type = Integer32
_FlashDirSize_Object = MibTableColumn
flashDirSize = _FlashDirSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 2),
    _FlashDirSize_Type()
)
flashDirSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirSize.setStatus("mandatory")


class _FlashDirStatus_Type(Integer32):
    """Custom type flashDirStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 2),
          ("valid", 1))
    )


_FlashDirStatus_Type.__name__ = "Integer32"
_FlashDirStatus_Object = MibTableColumn
flashDirStatus = _FlashDirStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 10, 17, 1, 3),
    _FlashDirStatus_Type()
)
flashDirStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flashDirStatus.setStatus("mandatory")
_Temporary_ObjectIdentity = ObjectIdentity
temporary = _Temporary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3)
)
_Tmpdecnet_ObjectIdentity = ObjectIdentity
tmpdecnet = _Tmpdecnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 1)
)
_DnForward_Type = Integer32
_DnForward_Object = MibScalar
dnForward = _DnForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 1),
    _DnForward_Type()
)
dnForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnForward.setStatus("mandatory")
_DnReceived_Type = Integer32
_DnReceived_Object = MibScalar
dnReceived = _DnReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 2),
    _DnReceived_Type()
)
dnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnReceived.setStatus("mandatory")
_DnFormaterr_Type = Integer32
_DnFormaterr_Object = MibScalar
dnFormaterr = _DnFormaterr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 3),
    _DnFormaterr_Type()
)
dnFormaterr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnFormaterr.setStatus("mandatory")
_DnNotgateway_Type = Integer32
_DnNotgateway_Object = MibScalar
dnNotgateway = _DnNotgateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 4),
    _DnNotgateway_Type()
)
dnNotgateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotgateway.setStatus("mandatory")
_DnNotimp_Type = Integer32
_DnNotimp_Object = MibScalar
dnNotimp = _DnNotimp_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 5),
    _DnNotimp_Type()
)
dnNotimp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotimp.setStatus("mandatory")
_DnHellos_Type = Integer32
_DnHellos_Object = MibScalar
dnHellos = _DnHellos_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 6),
    _DnHellos_Type()
)
dnHellos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHellos.setStatus("mandatory")
_DnBadhello_Type = Integer32
_DnBadhello_Object = MibScalar
dnBadhello = _DnBadhello_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 7),
    _DnBadhello_Type()
)
dnBadhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBadhello.setStatus("mandatory")
_DnNotlong_Type = Integer32
_DnNotlong_Object = MibScalar
dnNotlong = _DnNotlong_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 8),
    _DnNotlong_Type()
)
dnNotlong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNotlong.setStatus("mandatory")
_DnDatas_Type = Integer32
_DnDatas_Object = MibScalar
dnDatas = _DnDatas_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 9),
    _DnDatas_Type()
)
dnDatas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnDatas.setStatus("mandatory")
_DnBigaddr_Type = Integer32
_DnBigaddr_Object = MibScalar
dnBigaddr = _DnBigaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 10),
    _DnBigaddr_Type()
)
dnBigaddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBigaddr.setStatus("mandatory")
_DnNoroute_Type = Integer32
_DnNoroute_Object = MibScalar
dnNoroute = _DnNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 11),
    _DnNoroute_Type()
)
dnNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoroute.setStatus("mandatory")
_DnNoencap_Type = Integer32
_DnNoencap_Object = MibScalar
dnNoencap = _DnNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 12),
    _DnNoencap_Type()
)
dnNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoencap.setStatus("mandatory")
_DnLevel1s_Type = Integer32
_DnLevel1s_Object = MibScalar
dnLevel1s = _DnLevel1s_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 13),
    _DnLevel1s_Type()
)
dnLevel1s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel1s.setStatus("mandatory")
_DnBadlevel1_Type = Integer32
_DnBadlevel1_Object = MibScalar
dnBadlevel1 = _DnBadlevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 14),
    _DnBadlevel1_Type()
)
dnBadlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnBadlevel1.setStatus("mandatory")
_DnToomanyhops_Type = Integer32
_DnToomanyhops_Object = MibScalar
dnToomanyhops = _DnToomanyhops_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 15),
    _DnToomanyhops_Type()
)
dnToomanyhops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnToomanyhops.setStatus("mandatory")
_DnHellosent_Type = Integer32
_DnHellosent_Object = MibScalar
dnHellosent = _DnHellosent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 16),
    _DnHellosent_Type()
)
dnHellosent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHellosent.setStatus("mandatory")
_DnLevel1sent_Type = Integer32
_DnLevel1sent_Object = MibScalar
dnLevel1sent = _DnLevel1sent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 17),
    _DnLevel1sent_Type()
)
dnLevel1sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel1sent.setStatus("mandatory")
_DnNomemory_Type = Integer32
_DnNomemory_Object = MibScalar
dnNomemory = _DnNomemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 18),
    _DnNomemory_Type()
)
dnNomemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNomemory.setStatus("mandatory")
_DnOtherhello_Type = Integer32
_DnOtherhello_Object = MibScalar
dnOtherhello = _DnOtherhello_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 19),
    _DnOtherhello_Type()
)
dnOtherhello.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherhello.setStatus("mandatory")
_DnOtherlevel1_Type = Integer32
_DnOtherlevel1_Object = MibScalar
dnOtherlevel1 = _DnOtherlevel1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 20),
    _DnOtherlevel1_Type()
)
dnOtherlevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherlevel1.setStatus("mandatory")
_DnLevel2s_Type = Integer32
_DnLevel2s_Object = MibScalar
dnLevel2s = _DnLevel2s_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 21),
    _DnLevel2s_Type()
)
dnLevel2s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel2s.setStatus("mandatory")
_DnLevel2sent_Type = Integer32
_DnLevel2sent_Object = MibScalar
dnLevel2sent = _DnLevel2sent_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 22),
    _DnLevel2sent_Type()
)
dnLevel2sent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnLevel2sent.setStatus("mandatory")
_DnNovector_Type = Integer32
_DnNovector_Object = MibScalar
dnNovector = _DnNovector_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 23),
    _DnNovector_Type()
)
dnNovector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNovector.setStatus("mandatory")
_DnOtherlevel2_Type = Integer32
_DnOtherlevel2_Object = MibScalar
dnOtherlevel2 = _DnOtherlevel2_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 24),
    _DnOtherlevel2_Type()
)
dnOtherlevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnOtherlevel2.setStatus("mandatory")
_DnNoaccess_Type = Integer32
_DnNoaccess_Object = MibScalar
dnNoaccess = _DnNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 25),
    _DnNoaccess_Type()
)
dnNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnNoaccess.setStatus("mandatory")
_DnAreaTable_Object = MibTable
dnAreaTable = _DnAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26)
)
if mibBuilder.loadTexts:
    dnAreaTable.setStatus("mandatory")
_DnAreaTableEntry_Object = MibTableRow
dnAreaTableEntry = _DnAreaTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1)
)
dnAreaTableEntry.setIndexNames(
    (0, "CISCO-MIB", "dnArea"),
)
if mibBuilder.loadTexts:
    dnAreaTableEntry.setStatus("mandatory")
_DnArea_Type = Integer32
_DnArea_Object = MibTableColumn
dnArea = _DnArea_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 1),
    _DnArea_Type()
)
dnArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnArea.setStatus("mandatory")
_DnACost_Type = Integer32
_DnACost_Object = MibTableColumn
dnACost = _DnACost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 2),
    _DnACost_Type()
)
dnACost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnACost.setStatus("mandatory")
_DnAHop_Type = Integer32
_DnAHop_Object = MibTableColumn
dnAHop = _DnAHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 3),
    _DnAHop_Type()
)
dnAHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAHop.setStatus("mandatory")
_DnAIfIndex_Type = Integer32
_DnAIfIndex_Object = MibTableColumn
dnAIfIndex = _DnAIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 4),
    _DnAIfIndex_Type()
)
dnAIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAIfIndex.setStatus("mandatory")
_DnANextHop_Type = OctetString
_DnANextHop_Object = MibTableColumn
dnANextHop = _DnANextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 5),
    _DnANextHop_Type()
)
dnANextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnANextHop.setStatus("mandatory")
_DnAAge_Type = Integer32
_DnAAge_Object = MibTableColumn
dnAAge = _DnAAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 6),
    _DnAAge_Type()
)
dnAAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAAge.setStatus("mandatory")
_DnAPrio_Type = Integer32
_DnAPrio_Object = MibTableColumn
dnAPrio = _DnAPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 26, 1, 7),
    _DnAPrio_Type()
)
dnAPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnAPrio.setStatus("mandatory")
_DnHostTable_Object = MibTable
dnHostTable = _DnHostTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27)
)
if mibBuilder.loadTexts:
    dnHostTable.setStatus("mandatory")
_DnHostTableEntry_Object = MibTableRow
dnHostTableEntry = _DnHostTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1)
)
dnHostTableEntry.setIndexNames(
    (0, "CISCO-MIB", "dnHIdx1"),
    (0, "CISCO-MIB", "dnHIdx2"),
)
if mibBuilder.loadTexts:
    dnHostTableEntry.setStatus("mandatory")
_DnHost_Type = Integer32
_DnHost_Object = MibTableColumn
dnHost = _DnHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 1),
    _DnHost_Type()
)
dnHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHost.setStatus("mandatory")
_DnHCost_Type = Integer32
_DnHCost_Object = MibTableColumn
dnHCost = _DnHCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 2),
    _DnHCost_Type()
)
dnHCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHCost.setStatus("mandatory")
_DnHHop_Type = Integer32
_DnHHop_Object = MibTableColumn
dnHHop = _DnHHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 3),
    _DnHHop_Type()
)
dnHHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHHop.setStatus("mandatory")
_DnHIfIndex_Type = Integer32
_DnHIfIndex_Object = MibTableColumn
dnHIfIndex = _DnHIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 4),
    _DnHIfIndex_Type()
)
dnHIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHIfIndex.setStatus("mandatory")
_DnHNextHop_Type = OctetString
_DnHNextHop_Object = MibTableColumn
dnHNextHop = _DnHNextHop_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 5),
    _DnHNextHop_Type()
)
dnHNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHNextHop.setStatus("mandatory")
_DnHAge_Type = Integer32
_DnHAge_Object = MibTableColumn
dnHAge = _DnHAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 6),
    _DnHAge_Type()
)
dnHAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHAge.setStatus("mandatory")
_DnHPrio_Type = Integer32
_DnHPrio_Object = MibTableColumn
dnHPrio = _DnHPrio_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 7),
    _DnHPrio_Type()
)
dnHPrio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnHPrio.setStatus("mandatory")
_DnHIdx1_Type = Integer32
_DnHIdx1_Object = MibTableColumn
dnHIdx1 = _DnHIdx1_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 8),
    _DnHIdx1_Type()
)
dnHIdx1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnHIdx1.setStatus("mandatory")
_DnHIdx2_Type = Integer32
_DnHIdx2_Object = MibTableColumn
dnHIdx2 = _DnHIdx2_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 27, 1, 9),
    _DnHIdx2_Type()
)
dnHIdx2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnHIdx2.setStatus("mandatory")
_DnIfTable_Object = MibTable
dnIfTable = _DnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28)
)
if mibBuilder.loadTexts:
    dnIfTable.setStatus("mandatory")
_DnIfTableEntry_Object = MibTableRow
dnIfTableEntry = _DnIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28, 1)
)
dnIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dnIfTableEntry.setStatus("mandatory")
_DnIfCost_Type = Integer32
_DnIfCost_Object = MibTableColumn
dnIfCost = _DnIfCost_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 1, 28, 1, 1),
    _DnIfCost_Type()
)
dnIfCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnIfCost.setStatus("mandatory")
_Tmpxns_ObjectIdentity = ObjectIdentity
tmpxns = _Tmpxns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 2)
)
_XnsInput_Type = Integer32
_XnsInput_Object = MibScalar
xnsInput = _XnsInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 1),
    _XnsInput_Type()
)
xnsInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsInput.setStatus("mandatory")
_XnsLocal_Type = Integer32
_XnsLocal_Object = MibScalar
xnsLocal = _XnsLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 2),
    _XnsLocal_Type()
)
xnsLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsLocal.setStatus("mandatory")
_XnsBcastin_Type = Integer32
_XnsBcastin_Object = MibScalar
xnsBcastin = _XnsBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 3),
    _XnsBcastin_Type()
)
xnsBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsBcastin.setStatus("mandatory")
_XnsForward_Type = Integer32
_XnsForward_Object = MibScalar
xnsForward = _XnsForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 4),
    _XnsForward_Type()
)
xnsForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsForward.setStatus("mandatory")
_XnsBcastout_Type = Integer32
_XnsBcastout_Object = MibScalar
xnsBcastout = _XnsBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 5),
    _XnsBcastout_Type()
)
xnsBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsBcastout.setStatus("mandatory")
_XnsErrin_Type = Integer32
_XnsErrin_Object = MibScalar
xnsErrin = _XnsErrin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 6),
    _XnsErrin_Type()
)
xnsErrin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsErrin.setStatus("mandatory")
_XnsErrout_Type = Integer32
_XnsErrout_Object = MibScalar
xnsErrout = _XnsErrout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 7),
    _XnsErrout_Type()
)
xnsErrout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsErrout.setStatus("mandatory")
_XnsFormerr_Type = Integer32
_XnsFormerr_Object = MibScalar
xnsFormerr = _XnsFormerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 8),
    _XnsFormerr_Type()
)
xnsFormerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsFormerr.setStatus("mandatory")
_XnsChksum_Type = Integer32
_XnsChksum_Object = MibScalar
xnsChksum = _XnsChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 9),
    _XnsChksum_Type()
)
xnsChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsChksum.setStatus("mandatory")
_XnsNotgate_Type = Integer32
_XnsNotgate_Object = MibScalar
xnsNotgate = _XnsNotgate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 10),
    _XnsNotgate_Type()
)
xnsNotgate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNotgate.setStatus("mandatory")
_XnsHopcnt_Type = Integer32
_XnsHopcnt_Object = MibScalar
xnsHopcnt = _XnsHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 11),
    _XnsHopcnt_Type()
)
xnsHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsHopcnt.setStatus("mandatory")
_XnsNoroute_Type = Integer32
_XnsNoroute_Object = MibScalar
xnsNoroute = _XnsNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 12),
    _XnsNoroute_Type()
)
xnsNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNoroute.setStatus("mandatory")
_XnsNoencap_Type = Integer32
_XnsNoencap_Object = MibScalar
xnsNoencap = _XnsNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 13),
    _XnsNoencap_Type()
)
xnsNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsNoencap.setStatus("mandatory")
_XnsOutput_Type = Integer32
_XnsOutput_Object = MibScalar
xnsOutput = _XnsOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 14),
    _XnsOutput_Type()
)
xnsOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsOutput.setStatus("mandatory")
_XnsInmult_Type = Integer32
_XnsInmult_Object = MibScalar
xnsInmult = _XnsInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 15),
    _XnsInmult_Type()
)
xnsInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsInmult.setStatus("mandatory")
_XnsUnknown_Type = Integer32
_XnsUnknown_Object = MibScalar
xnsUnknown = _XnsUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 16),
    _XnsUnknown_Type()
)
xnsUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsUnknown.setStatus("mandatory")
_XnsFwdbrd_Type = Integer32
_XnsFwdbrd_Object = MibScalar
xnsFwdbrd = _XnsFwdbrd_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 17),
    _XnsFwdbrd_Type()
)
xnsFwdbrd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsFwdbrd.setStatus("mandatory")
_XnsEchoreqin_Type = Integer32
_XnsEchoreqin_Object = MibScalar
xnsEchoreqin = _XnsEchoreqin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 18),
    _XnsEchoreqin_Type()
)
xnsEchoreqin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchoreqin.setStatus("mandatory")
_XnsEchoreqout_Type = Integer32
_XnsEchoreqout_Object = MibScalar
xnsEchoreqout = _XnsEchoreqout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 19),
    _XnsEchoreqout_Type()
)
xnsEchoreqout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchoreqout.setStatus("mandatory")
_XnsEchorepin_Type = Integer32
_XnsEchorepin_Object = MibScalar
xnsEchorepin = _XnsEchorepin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 20),
    _XnsEchorepin_Type()
)
xnsEchorepin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchorepin.setStatus("mandatory")
_XnsEchorepout_Type = Integer32
_XnsEchorepout_Object = MibScalar
xnsEchorepout = _XnsEchorepout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 2, 21),
    _XnsEchorepout_Type()
)
xnsEchorepout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xnsEchorepout.setStatus("mandatory")
_Tmpappletalk_ObjectIdentity = ObjectIdentity
tmpappletalk = _Tmpappletalk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 3)
)
_AtInput_Type = Integer32
_AtInput_Object = MibScalar
atInput = _AtInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 1),
    _AtInput_Type()
)
atInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atInput.setStatus("mandatory")
_AtLocal_Type = Integer32
_AtLocal_Object = MibScalar
atLocal = _AtLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 2),
    _AtLocal_Type()
)
atLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atLocal.setStatus("mandatory")
_AtBcastin_Type = Integer32
_AtBcastin_Object = MibScalar
atBcastin = _AtBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 3),
    _AtBcastin_Type()
)
atBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBcastin.setStatus("mandatory")
_AtForward_Type = Integer32
_AtForward_Object = MibScalar
atForward = _AtForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 4),
    _AtForward_Type()
)
atForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atForward.setStatus("mandatory")
_AtBcastout_Type = Integer32
_AtBcastout_Object = MibScalar
atBcastout = _AtBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 5),
    _AtBcastout_Type()
)
atBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atBcastout.setStatus("mandatory")
_AtChksum_Type = Integer32
_AtChksum_Object = MibScalar
atChksum = _AtChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 7),
    _AtChksum_Type()
)
atChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atChksum.setStatus("mandatory")
_AtNotgate_Type = Integer32
_AtNotgate_Object = MibScalar
atNotgate = _AtNotgate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 8),
    _AtNotgate_Type()
)
atNotgate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNotgate.setStatus("mandatory")
_AtHopcnt_Type = Integer32
_AtHopcnt_Object = MibScalar
atHopcnt = _AtHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 9),
    _AtHopcnt_Type()
)
atHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atHopcnt.setStatus("mandatory")
_AtNoaccess_Type = Integer32
_AtNoaccess_Object = MibScalar
atNoaccess = _AtNoaccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 10),
    _AtNoaccess_Type()
)
atNoaccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoaccess.setStatus("mandatory")
_AtNoroute_Type = Integer32
_AtNoroute_Object = MibScalar
atNoroute = _AtNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 11),
    _AtNoroute_Type()
)
atNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoroute.setStatus("mandatory")
_AtNoencap_Type = Integer32
_AtNoencap_Object = MibScalar
atNoencap = _AtNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 12),
    _AtNoencap_Type()
)
atNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNoencap.setStatus("mandatory")
_AtOutput_Type = Integer32
_AtOutput_Object = MibScalar
atOutput = _AtOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 13),
    _AtOutput_Type()
)
atOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atOutput.setStatus("mandatory")
_AtInmult_Type = Integer32
_AtInmult_Object = MibScalar
atInmult = _AtInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 14),
    _AtInmult_Type()
)
atInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atInmult.setStatus("mandatory")
_AtRtmpin_Type = Integer32
_AtRtmpin_Object = MibScalar
atRtmpin = _AtRtmpin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 15),
    _AtRtmpin_Type()
)
atRtmpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtmpin.setStatus("mandatory")
_AtRtmpout_Type = Integer32
_AtRtmpout_Object = MibScalar
atRtmpout = _AtRtmpout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 16),
    _AtRtmpout_Type()
)
atRtmpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atRtmpout.setStatus("mandatory")
_AtNbpin_Type = Integer32
_AtNbpin_Object = MibScalar
atNbpin = _AtNbpin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 17),
    _AtNbpin_Type()
)
atNbpin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNbpin.setStatus("mandatory")
_AtNbpout_Type = Integer32
_AtNbpout_Object = MibScalar
atNbpout = _AtNbpout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 18),
    _AtNbpout_Type()
)
atNbpout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNbpout.setStatus("mandatory")
_AtAtp_Type = Integer32
_AtAtp_Object = MibScalar
atAtp = _AtAtp_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 19),
    _AtAtp_Type()
)
atAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtp.setStatus("mandatory")
_AtZipin_Type = Integer32
_AtZipin_Object = MibScalar
atZipin = _AtZipin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 20),
    _AtZipin_Type()
)
atZipin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atZipin.setStatus("mandatory")
_AtZipout_Type = Integer32
_AtZipout_Object = MibScalar
atZipout = _AtZipout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 21),
    _AtZipout_Type()
)
atZipout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atZipout.setStatus("mandatory")
_AtEcho_Type = Integer32
_AtEcho_Object = MibScalar
atEcho = _AtEcho_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 22),
    _AtEcho_Type()
)
atEcho.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEcho.setStatus("mandatory")
_AtEchoill_Type = Integer32
_AtEchoill_Object = MibScalar
atEchoill = _AtEchoill_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 23),
    _AtEchoill_Type()
)
atEchoill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atEchoill.setStatus("mandatory")
_AtDdpshort_Type = Integer32
_AtDdpshort_Object = MibScalar
atDdpshort = _AtDdpshort_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 24),
    _AtDdpshort_Type()
)
atDdpshort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdpshort.setStatus("mandatory")
_AtDdplong_Type = Integer32
_AtDdplong_Object = MibScalar
atDdplong = _AtDdplong_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 25),
    _AtDdplong_Type()
)
atDdplong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdplong.setStatus("mandatory")
_AtDdpbad_Type = Integer32
_AtDdpbad_Object = MibScalar
atDdpbad = _AtDdpbad_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 26),
    _AtDdpbad_Type()
)
atDdpbad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atDdpbad.setStatus("mandatory")
_AtNobuffer_Type = Integer32
_AtNobuffer_Object = MibScalar
atNobuffer = _AtNobuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 27),
    _AtNobuffer_Type()
)
atNobuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atNobuffer.setStatus("mandatory")
_AtArpreq_Type = Integer32
_AtArpreq_Object = MibScalar
atArpreq = _AtArpreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 28),
    _AtArpreq_Type()
)
atArpreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpreq.setStatus("mandatory")
_AtArpreply_Type = Integer32
_AtArpreply_Object = MibScalar
atArpreply = _AtArpreply_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 29),
    _AtArpreply_Type()
)
atArpreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpreply.setStatus("mandatory")
_AtArpprobe_Type = Integer32
_AtArpprobe_Object = MibScalar
atArpprobe = _AtArpprobe_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 30),
    _AtArpprobe_Type()
)
atArpprobe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atArpprobe.setStatus("mandatory")
_AtUnknown_Type = Integer32
_AtUnknown_Object = MibScalar
atUnknown = _AtUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 3, 31),
    _AtUnknown_Type()
)
atUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atUnknown.setStatus("mandatory")
_Tmpnovell_ObjectIdentity = ObjectIdentity
tmpnovell = _Tmpnovell_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 4)
)
_NovellInput_Type = Integer32
_NovellInput_Object = MibScalar
novellInput = _NovellInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 1),
    _NovellInput_Type()
)
novellInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellInput.setStatus("mandatory")
_NovellBcastin_Type = Integer32
_NovellBcastin_Object = MibScalar
novellBcastin = _NovellBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 2),
    _NovellBcastin_Type()
)
novellBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellBcastin.setStatus("mandatory")
_NovellForward_Type = Integer32
_NovellForward_Object = MibScalar
novellForward = _NovellForward_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 3),
    _NovellForward_Type()
)
novellForward.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellForward.setStatus("mandatory")
_NovellBcastout_Type = Integer32
_NovellBcastout_Object = MibScalar
novellBcastout = _NovellBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 4),
    _NovellBcastout_Type()
)
novellBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellBcastout.setStatus("mandatory")
_NovellFormerr_Type = Integer32
_NovellFormerr_Object = MibScalar
novellFormerr = _NovellFormerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 5),
    _NovellFormerr_Type()
)
novellFormerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellFormerr.setStatus("mandatory")
_NovellChksum_Type = Integer32
_NovellChksum_Object = MibScalar
novellChksum = _NovellChksum_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 6),
    _NovellChksum_Type()
)
novellChksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellChksum.setStatus("mandatory")
_NovellHopcnt_Type = Integer32
_NovellHopcnt_Object = MibScalar
novellHopcnt = _NovellHopcnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 7),
    _NovellHopcnt_Type()
)
novellHopcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellHopcnt.setStatus("mandatory")
_NovellNoroute_Type = Integer32
_NovellNoroute_Object = MibScalar
novellNoroute = _NovellNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 8),
    _NovellNoroute_Type()
)
novellNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellNoroute.setStatus("mandatory")
_NovellNoencap_Type = Integer32
_NovellNoencap_Object = MibScalar
novellNoencap = _NovellNoencap_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 9),
    _NovellNoencap_Type()
)
novellNoencap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellNoencap.setStatus("mandatory")
_NovellOutput_Type = Integer32
_NovellOutput_Object = MibScalar
novellOutput = _NovellOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 10),
    _NovellOutput_Type()
)
novellOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellOutput.setStatus("mandatory")
_NovellInmult_Type = Integer32
_NovellInmult_Object = MibScalar
novellInmult = _NovellInmult_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 11),
    _NovellInmult_Type()
)
novellInmult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellInmult.setStatus("mandatory")
_NovellLocal_Type = Integer32
_NovellLocal_Object = MibScalar
novellLocal = _NovellLocal_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 12),
    _NovellLocal_Type()
)
novellLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellLocal.setStatus("mandatory")
_NovellUnknown_Type = Integer32
_NovellUnknown_Object = MibScalar
novellUnknown = _NovellUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 13),
    _NovellUnknown_Type()
)
novellUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellUnknown.setStatus("mandatory")
_NovellSapreqin_Type = Integer32
_NovellSapreqin_Object = MibScalar
novellSapreqin = _NovellSapreqin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 14),
    _NovellSapreqin_Type()
)
novellSapreqin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapreqin.setStatus("mandatory")
_NovellSapresin_Type = Integer32
_NovellSapresin_Object = MibScalar
novellSapresin = _NovellSapresin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 15),
    _NovellSapresin_Type()
)
novellSapresin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapresin.setStatus("mandatory")
_NovellSapout_Type = Integer32
_NovellSapout_Object = MibScalar
novellSapout = _NovellSapout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 16),
    _NovellSapout_Type()
)
novellSapout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapout.setStatus("mandatory")
_NovellSapreply_Type = Integer32
_NovellSapreply_Object = MibScalar
novellSapreply = _NovellSapreply_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 17),
    _NovellSapreply_Type()
)
novellSapreply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    novellSapreply.setStatus("mandatory")
_IpxActThresh_Type = Integer32
_IpxActThresh_Object = MibScalar
ipxActThresh = _IpxActThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 18),
    _IpxActThresh_Type()
)
ipxActThresh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActThresh.setStatus("mandatory")
_IpxActLostPkts_Type = Integer32
_IpxActLostPkts_Object = MibScalar
ipxActLostPkts = _IpxActLostPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 19),
    _IpxActLostPkts_Type()
)
ipxActLostPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActLostPkts.setStatus("mandatory")
_IpxActLostByts_Type = Integer32
_IpxActLostByts_Object = MibScalar
ipxActLostByts = _IpxActLostByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 20),
    _IpxActLostByts_Type()
)
ipxActLostByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActLostByts.setStatus("mandatory")
_LipxAccountingTable_Object = MibTable
lipxAccountingTable = _LipxAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21)
)
if mibBuilder.loadTexts:
    lipxAccountingTable.setStatus("mandatory")
_LipxAccountingEntry_Object = MibTableRow
lipxAccountingEntry = _LipxAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1)
)
lipxAccountingEntry.setIndexNames(
    (0, "CISCO-MIB", "ipxActSrc"),
    (0, "CISCO-MIB", "ipxActDst"),
)
if mibBuilder.loadTexts:
    lipxAccountingEntry.setStatus("mandatory")
_IpxActSrc_Type = OctetString
_IpxActSrc_Object = MibTableColumn
ipxActSrc = _IpxActSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 1),
    _IpxActSrc_Type()
)
ipxActSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActSrc.setStatus("mandatory")
_IpxActDst_Type = OctetString
_IpxActDst_Object = MibTableColumn
ipxActDst = _IpxActDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 2),
    _IpxActDst_Type()
)
ipxActDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActDst.setStatus("mandatory")
_IpxActPkts_Type = Integer32
_IpxActPkts_Object = MibTableColumn
ipxActPkts = _IpxActPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 3),
    _IpxActPkts_Type()
)
ipxActPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActPkts.setStatus("mandatory")
_IpxActByts_Type = Integer32
_IpxActByts_Object = MibTableColumn
ipxActByts = _IpxActByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 21, 1, 4),
    _IpxActByts_Type()
)
ipxActByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActByts.setStatus("mandatory")
_IpxActAge_Type = TimeTicks
_IpxActAge_Object = MibScalar
ipxActAge = _IpxActAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 22),
    _IpxActAge_Type()
)
ipxActAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxActAge.setStatus("mandatory")
_LipxCkAccountingTable_Object = MibTable
lipxCkAccountingTable = _LipxCkAccountingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23)
)
if mibBuilder.loadTexts:
    lipxCkAccountingTable.setStatus("mandatory")
_LipxCkAccountingEntry_Object = MibTableRow
lipxCkAccountingEntry = _LipxCkAccountingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1)
)
lipxCkAccountingEntry.setIndexNames(
    (0, "CISCO-MIB", "ipxCkactSrc"),
    (0, "CISCO-MIB", "ipxCkactDst"),
)
if mibBuilder.loadTexts:
    lipxCkAccountingEntry.setStatus("mandatory")
_IpxCkactSrc_Type = OctetString
_IpxCkactSrc_Object = MibTableColumn
ipxCkactSrc = _IpxCkactSrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 1),
    _IpxCkactSrc_Type()
)
ipxCkactSrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactSrc.setStatus("mandatory")
_IpxCkactDst_Type = OctetString
_IpxCkactDst_Object = MibTableColumn
ipxCkactDst = _IpxCkactDst_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 2),
    _IpxCkactDst_Type()
)
ipxCkactDst.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactDst.setStatus("mandatory")
_IpxCkactPkts_Type = Integer32
_IpxCkactPkts_Object = MibTableColumn
ipxCkactPkts = _IpxCkactPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 3),
    _IpxCkactPkts_Type()
)
ipxCkactPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactPkts.setStatus("mandatory")
_IpxCkactByts_Type = Counter32
_IpxCkactByts_Object = MibTableColumn
ipxCkactByts = _IpxCkactByts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 23, 1, 4),
    _IpxCkactByts_Type()
)
ipxCkactByts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactByts.setStatus("mandatory")
_IpxCkactAge_Type = TimeTicks
_IpxCkactAge_Object = MibScalar
ipxCkactAge = _IpxCkactAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 24),
    _IpxCkactAge_Type()
)
ipxCkactAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCkactAge.setStatus("mandatory")
_IpxActCheckPoint_Type = Integer32
_IpxActCheckPoint_Object = MibScalar
ipxActCheckPoint = _IpxActCheckPoint_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 4, 25),
    _IpxActCheckPoint_Type()
)
ipxActCheckPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxActCheckPoint.setStatus("mandatory")
_Tmpvines_ObjectIdentity = ObjectIdentity
tmpvines = _Tmpvines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 5)
)
_VinesInput_Type = Integer32
_VinesInput_Object = MibScalar
vinesInput = _VinesInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 1),
    _VinesInput_Type()
)
vinesInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesInput.setStatus("mandatory")
_VinesOutput_Type = Integer32
_VinesOutput_Object = MibScalar
vinesOutput = _VinesOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 2),
    _VinesOutput_Type()
)
vinesOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesOutput.setStatus("mandatory")
_VinesLocaldest_Type = Integer32
_VinesLocaldest_Object = MibScalar
vinesLocaldest = _VinesLocaldest_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 3),
    _VinesLocaldest_Type()
)
vinesLocaldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesLocaldest.setStatus("mandatory")
_VinesForwarded_Type = Integer32
_VinesForwarded_Object = MibScalar
vinesForwarded = _VinesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 4),
    _VinesForwarded_Type()
)
vinesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesForwarded.setStatus("mandatory")
_VinesBcastin_Type = Integer32
_VinesBcastin_Object = MibScalar
vinesBcastin = _VinesBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 5),
    _VinesBcastin_Type()
)
vinesBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastin.setStatus("mandatory")
_VinesBcastout_Type = Integer32
_VinesBcastout_Object = MibScalar
vinesBcastout = _VinesBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 6),
    _VinesBcastout_Type()
)
vinesBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastout.setStatus("mandatory")
_VinesBcastfwd_Type = Integer32
_VinesBcastfwd_Object = MibScalar
vinesBcastfwd = _VinesBcastfwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 7),
    _VinesBcastfwd_Type()
)
vinesBcastfwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastfwd.setStatus("mandatory")
_VinesNotlan_Type = Integer32
_VinesNotlan_Object = MibScalar
vinesNotlan = _VinesNotlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 8),
    _VinesNotlan_Type()
)
vinesNotlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNotlan.setStatus("mandatory")
_VinesNotgt4800_Type = Integer32
_VinesNotgt4800_Object = MibScalar
vinesNotgt4800 = _VinesNotgt4800_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 9),
    _VinesNotgt4800_Type()
)
vinesNotgt4800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNotgt4800.setStatus("mandatory")
_VinesNocharges_Type = Integer32
_VinesNocharges_Object = MibScalar
vinesNocharges = _VinesNocharges_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 10),
    _VinesNocharges_Type()
)
vinesNocharges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNocharges.setStatus("mandatory")
_VinesFormaterror_Type = Integer32
_VinesFormaterror_Object = MibScalar
vinesFormaterror = _VinesFormaterror_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 11),
    _VinesFormaterror_Type()
)
vinesFormaterror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesFormaterror.setStatus("mandatory")
_VinesCksumerr_Type = Integer32
_VinesCksumerr_Object = MibScalar
vinesCksumerr = _VinesCksumerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 12),
    _VinesCksumerr_Type()
)
vinesCksumerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesCksumerr.setStatus("mandatory")
_VinesHopcount_Type = Integer32
_VinesHopcount_Object = MibScalar
vinesHopcount = _VinesHopcount_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 13),
    _VinesHopcount_Type()
)
vinesHopcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesHopcount.setStatus("mandatory")
_VinesNoroute_Type = Integer32
_VinesNoroute_Object = MibScalar
vinesNoroute = _VinesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 14),
    _VinesNoroute_Type()
)
vinesNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNoroute.setStatus("mandatory")
_VinesEncapsfailed_Type = Integer32
_VinesEncapsfailed_Object = MibScalar
vinesEncapsfailed = _VinesEncapsfailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 15),
    _VinesEncapsfailed_Type()
)
vinesEncapsfailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEncapsfailed.setStatus("mandatory")
_VinesUnknown_Type = Integer32
_VinesUnknown_Object = MibScalar
vinesUnknown = _VinesUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 16),
    _VinesUnknown_Type()
)
vinesUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesUnknown.setStatus("mandatory")
_VinesIcpIn_Type = Integer32
_VinesIcpIn_Object = MibScalar
vinesIcpIn = _VinesIcpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 17),
    _VinesIcpIn_Type()
)
vinesIcpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIcpIn.setStatus("mandatory")
_VinesIcpOut_Type = Integer32
_VinesIcpOut_Object = MibScalar
vinesIcpOut = _VinesIcpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 18),
    _VinesIcpOut_Type()
)
vinesIcpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIcpOut.setStatus("mandatory")
_VinesMetricOut_Type = Integer32
_VinesMetricOut_Object = MibScalar
vinesMetricOut = _VinesMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 19),
    _VinesMetricOut_Type()
)
vinesMetricOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMetricOut.setStatus("mandatory")
_VinesMacEchoIn_Type = Integer32
_VinesMacEchoIn_Object = MibScalar
vinesMacEchoIn = _VinesMacEchoIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 20),
    _VinesMacEchoIn_Type()
)
vinesMacEchoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMacEchoIn.setStatus("mandatory")
_VinesMacEchoOut_Type = Integer32
_VinesMacEchoOut_Object = MibScalar
vinesMacEchoOut = _VinesMacEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 21),
    _VinesMacEchoOut_Type()
)
vinesMacEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMacEchoOut.setStatus("mandatory")
_VinesEchoIn_Type = Integer32
_VinesEchoIn_Object = MibScalar
vinesEchoIn = _VinesEchoIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 22),
    _VinesEchoIn_Type()
)
vinesEchoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEchoIn.setStatus("mandatory")
_VinesEchoOut_Type = Integer32
_VinesEchoOut_Object = MibScalar
vinesEchoOut = _VinesEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 23),
    _VinesEchoOut_Type()
)
vinesEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEchoOut.setStatus("mandatory")
_VinesProxyCnt_Type = Counter32
_VinesProxyCnt_Object = MibScalar
vinesProxyCnt = _VinesProxyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 24),
    _VinesProxyCnt_Type()
)
vinesProxyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesProxyCnt.setStatus("mandatory")
_VinesProxyReplyCnt_Type = Counter32
_VinesProxyReplyCnt_Object = MibScalar
vinesProxyReplyCnt = _VinesProxyReplyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 25),
    _VinesProxyReplyCnt_Type()
)
vinesProxyReplyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesProxyReplyCnt.setStatus("mandatory")
_VinesNet_Type = Integer32
_VinesNet_Object = MibScalar
vinesNet = _VinesNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 26),
    _VinesNet_Type()
)
vinesNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNet.setStatus("mandatory")
_VinesSubNet_Type = Integer32
_VinesSubNet_Object = MibScalar
vinesSubNet = _VinesSubNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 27),
    _VinesSubNet_Type()
)
vinesSubNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesSubNet.setStatus("mandatory")
_VinesClient_Type = Integer32
_VinesClient_Object = MibScalar
vinesClient = _VinesClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 28),
    _VinesClient_Type()
)
vinesClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesClient.setStatus("mandatory")
_TmpvinesIfTable_Object = MibTable
tmpvinesIfTable = _TmpvinesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29)
)
if mibBuilder.loadTexts:
    tmpvinesIfTable.setStatus("mandatory")
_TmpvinesIfTableEntry_Object = MibTableRow
tmpvinesIfTableEntry = _TmpvinesIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1)
)
tmpvinesIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tmpvinesIfTableEntry.setStatus("mandatory")
_VinesIfMetric_Type = Integer32
_VinesIfMetric_Object = MibTableColumn
vinesIfMetric = _VinesIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 1),
    _VinesIfMetric_Type()
)
vinesIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfMetric.setStatus("mandatory")
_VinesIfEnctype_Type = Integer32
_VinesIfEnctype_Object = MibTableColumn
vinesIfEnctype = _VinesIfEnctype_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 2),
    _VinesIfEnctype_Type()
)
vinesIfEnctype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfEnctype.setStatus("mandatory")
_VinesIfAccesslist_Type = Integer32
_VinesIfAccesslist_Object = MibTableColumn
vinesIfAccesslist = _VinesIfAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 3),
    _VinesIfAccesslist_Type()
)
vinesIfAccesslist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfAccesslist.setStatus("mandatory")
_VinesIfPropagate_Type = Integer32
_VinesIfPropagate_Object = MibTableColumn
vinesIfPropagate = _VinesIfPropagate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 4),
    _VinesIfPropagate_Type()
)
vinesIfPropagate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfPropagate.setStatus("mandatory")
_VinesIfArpEnabled_Type = Integer32
_VinesIfArpEnabled_Object = MibTableColumn
vinesIfArpEnabled = _VinesIfArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 5),
    _VinesIfArpEnabled_Type()
)
vinesIfArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfArpEnabled.setStatus("mandatory")
_VinesIfServerless_Type = Integer32
_VinesIfServerless_Object = MibTableColumn
vinesIfServerless = _VinesIfServerless_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 6),
    _VinesIfServerless_Type()
)
vinesIfServerless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfServerless.setStatus("mandatory")
_VinesIfServerlessBcast_Type = Integer32
_VinesIfServerlessBcast_Object = MibTableColumn
vinesIfServerlessBcast = _VinesIfServerlessBcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 7),
    _VinesIfServerlessBcast_Type()
)
vinesIfServerlessBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfServerlessBcast.setStatus("mandatory")
_VinesIfRedirectInterval_Type = Integer32
_VinesIfRedirectInterval_Object = MibTableColumn
vinesIfRedirectInterval = _VinesIfRedirectInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 8),
    _VinesIfRedirectInterval_Type()
)
vinesIfRedirectInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRedirectInterval.setStatus("mandatory")
_VinesIfSplitDisabled_Type = Integer32
_VinesIfSplitDisabled_Object = MibTableColumn
vinesIfSplitDisabled = _VinesIfSplitDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 9),
    _VinesIfSplitDisabled_Type()
)
vinesIfSplitDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfSplitDisabled.setStatus("mandatory")
_VinesIfLineup_Type = Integer32
_VinesIfLineup_Object = MibTableColumn
vinesIfLineup = _VinesIfLineup_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 10),
    _VinesIfLineup_Type()
)
vinesIfLineup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfLineup.setStatus("mandatory")
_VinesIfFastokay_Type = Integer32
_VinesIfFastokay_Object = MibTableColumn
vinesIfFastokay = _VinesIfFastokay_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 11),
    _VinesIfFastokay_Type()
)
vinesIfFastokay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfFastokay.setStatus("mandatory")
_VinesIfRouteCache_Type = Integer32
_VinesIfRouteCache_Object = MibTableColumn
vinesIfRouteCache = _VinesIfRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 12),
    _VinesIfRouteCache_Type()
)
vinesIfRouteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRouteCache.setStatus("mandatory")
_VinesIfIns_Type = Counter32
_VinesIfIns_Object = MibTableColumn
vinesIfIns = _VinesIfIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 13),
    _VinesIfIns_Type()
)
vinesIfIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfIns.setStatus("mandatory")
_VinesIfOuts_Type = Counter32
_VinesIfOuts_Object = MibTableColumn
vinesIfOuts = _VinesIfOuts_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 14),
    _VinesIfOuts_Type()
)
vinesIfOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfOuts.setStatus("mandatory")
_VinesIfInBytes_Type = Counter32
_VinesIfInBytes_Object = MibTableColumn
vinesIfInBytes = _VinesIfInBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 15),
    _VinesIfInBytes_Type()
)
vinesIfInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfInBytes.setStatus("mandatory")
_VinesIfOutBytes_Type = Counter32
_VinesIfOutBytes_Object = MibTableColumn
vinesIfOutBytes = _VinesIfOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 16),
    _VinesIfOutBytes_Type()
)
vinesIfOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfOutBytes.setStatus("mandatory")
_VinesIfRxNotEnabledCnt_Type = Counter32
_VinesIfRxNotEnabledCnt_Object = MibTableColumn
vinesIfRxNotEnabledCnt = _VinesIfRxNotEnabledCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 17),
    _VinesIfRxNotEnabledCnt_Type()
)
vinesIfRxNotEnabledCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxNotEnabledCnt.setStatus("mandatory")
_VinesIfRxFormatErrorCnt_Type = Counter32
_VinesIfRxFormatErrorCnt_Object = MibTableColumn
vinesIfRxFormatErrorCnt = _VinesIfRxFormatErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 18),
    _VinesIfRxFormatErrorCnt_Type()
)
vinesIfRxFormatErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxFormatErrorCnt.setStatus("mandatory")
_VinesIfRxLocalDestCnt_Type = Counter32
_VinesIfRxLocalDestCnt_Object = MibTableColumn
vinesIfRxLocalDestCnt = _VinesIfRxLocalDestCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 19),
    _VinesIfRxLocalDestCnt_Type()
)
vinesIfRxLocalDestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxLocalDestCnt.setStatus("mandatory")
_VinesIfRxBcastinCnt_Type = Counter32
_VinesIfRxBcastinCnt_Object = MibTableColumn
vinesIfRxBcastinCnt = _VinesIfRxBcastinCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 20),
    _VinesIfRxBcastinCnt_Type()
)
vinesIfRxBcastinCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastinCnt.setStatus("mandatory")
_VinesIfRxForwardedCnt_Type = Counter32
_VinesIfRxForwardedCnt_Object = MibTableColumn
vinesIfRxForwardedCnt = _VinesIfRxForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 21),
    _VinesIfRxForwardedCnt_Type()
)
vinesIfRxForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxForwardedCnt.setStatus("mandatory")
_VinesIfRxNoRouteCnt_Type = Counter32
_VinesIfRxNoRouteCnt_Object = MibTableColumn
vinesIfRxNoRouteCnt = _VinesIfRxNoRouteCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 22),
    _VinesIfRxNoRouteCnt_Type()
)
vinesIfRxNoRouteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxNoRouteCnt.setStatus("mandatory")
_VinesIfRxZeroHopCountCnt_Type = Counter32
_VinesIfRxZeroHopCountCnt_Object = MibTableColumn
vinesIfRxZeroHopCountCnt = _VinesIfRxZeroHopCountCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 23),
    _VinesIfRxZeroHopCountCnt_Type()
)
vinesIfRxZeroHopCountCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxZeroHopCountCnt.setStatus("mandatory")
_VinesIfRxChecksumErrorCnt_Type = Counter32
_VinesIfRxChecksumErrorCnt_Object = MibTableColumn
vinesIfRxChecksumErrorCnt = _VinesIfRxChecksumErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 24),
    _VinesIfRxChecksumErrorCnt_Type()
)
vinesIfRxChecksumErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxChecksumErrorCnt.setStatus("mandatory")
_VinesIfRxArp0Cnt_Type = Counter32
_VinesIfRxArp0Cnt_Object = MibTableColumn
vinesIfRxArp0Cnt = _VinesIfRxArp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 25),
    _VinesIfRxArp0Cnt_Type()
)
vinesIfRxArp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp0Cnt.setStatus("mandatory")
_VinesIfRxArp1Cnt_Type = Counter32
_VinesIfRxArp1Cnt_Object = MibTableColumn
vinesIfRxArp1Cnt = _VinesIfRxArp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 26),
    _VinesIfRxArp1Cnt_Type()
)
vinesIfRxArp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp1Cnt.setStatus("mandatory")
_VinesIfRxArp2Cnt_Type = Counter32
_VinesIfRxArp2Cnt_Object = MibTableColumn
vinesIfRxArp2Cnt = _VinesIfRxArp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 27),
    _VinesIfRxArp2Cnt_Type()
)
vinesIfRxArp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp2Cnt.setStatus("mandatory")
_VinesIfRxArp3Cnt_Type = Counter32
_VinesIfRxArp3Cnt_Object = MibTableColumn
vinesIfRxArp3Cnt = _VinesIfRxArp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 28),
    _VinesIfRxArp3Cnt_Type()
)
vinesIfRxArp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp3Cnt.setStatus("mandatory")
_VinesIfRxArpIllegalCnt_Type = Counter32
_VinesIfRxArpIllegalCnt_Object = MibTableColumn
vinesIfRxArpIllegalCnt = _VinesIfRxArpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 29),
    _VinesIfRxArpIllegalCnt_Type()
)
vinesIfRxArpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArpIllegalCnt.setStatus("mandatory")
_VinesIfRxIcpErrorCnt_Type = Counter32
_VinesIfRxIcpErrorCnt_Object = MibTableColumn
vinesIfRxIcpErrorCnt = _VinesIfRxIcpErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 30),
    _VinesIfRxIcpErrorCnt_Type()
)
vinesIfRxIcpErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpErrorCnt.setStatus("mandatory")
_VinesIfRxIcpMetricCnt_Type = Counter32
_VinesIfRxIcpMetricCnt_Object = MibTableColumn
vinesIfRxIcpMetricCnt = _VinesIfRxIcpMetricCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 31),
    _VinesIfRxIcpMetricCnt_Type()
)
vinesIfRxIcpMetricCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpMetricCnt.setStatus("mandatory")
_VinesIfRxIcpIllegalCnt_Type = Counter32
_VinesIfRxIcpIllegalCnt_Object = MibTableColumn
vinesIfRxIcpIllegalCnt = _VinesIfRxIcpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 32),
    _VinesIfRxIcpIllegalCnt_Type()
)
vinesIfRxIcpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpIllegalCnt.setStatus("mandatory")
_VinesIfRxIpcCnt_Type = Counter32
_VinesIfRxIpcCnt_Object = MibTableColumn
vinesIfRxIpcCnt = _VinesIfRxIpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 33),
    _VinesIfRxIpcCnt_Type()
)
vinesIfRxIpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpcCnt.setStatus("mandatory")
_VinesIfRxRtp0Cnt_Type = Counter32
_VinesIfRxRtp0Cnt_Object = MibTableColumn
vinesIfRxRtp0Cnt = _VinesIfRxRtp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 34),
    _VinesIfRxRtp0Cnt_Type()
)
vinesIfRxRtp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp0Cnt.setStatus("mandatory")
_VinesIfRxRtp1Cnt_Type = Counter32
_VinesIfRxRtp1Cnt_Object = MibTableColumn
vinesIfRxRtp1Cnt = _VinesIfRxRtp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 35),
    _VinesIfRxRtp1Cnt_Type()
)
vinesIfRxRtp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp1Cnt.setStatus("mandatory")
_VinesIfRxRtp2Cnt_Type = Counter32
_VinesIfRxRtp2Cnt_Object = MibTableColumn
vinesIfRxRtp2Cnt = _VinesIfRxRtp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 36),
    _VinesIfRxRtp2Cnt_Type()
)
vinesIfRxRtp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp2Cnt.setStatus("mandatory")
_VinesIfRxRtp3Cnt_Type = Counter32
_VinesIfRxRtp3Cnt_Object = MibTableColumn
vinesIfRxRtp3Cnt = _VinesIfRxRtp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 37),
    _VinesIfRxRtp3Cnt_Type()
)
vinesIfRxRtp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp3Cnt.setStatus("mandatory")
_VinesIfRxRtp4Cnt_Type = Counter32
_VinesIfRxRtp4Cnt_Object = MibTableColumn
vinesIfRxRtp4Cnt = _VinesIfRxRtp4Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 38),
    _VinesIfRxRtp4Cnt_Type()
)
vinesIfRxRtp4Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp4Cnt.setStatus("mandatory")
_VinesIfRxRtp5Cnt_Type = Counter32
_VinesIfRxRtp5Cnt_Object = MibTableColumn
vinesIfRxRtp5Cnt = _VinesIfRxRtp5Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 39),
    _VinesIfRxRtp5Cnt_Type()
)
vinesIfRxRtp5Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp5Cnt.setStatus("mandatory")
_VinesIfRxRtp6Cnt_Type = Counter32
_VinesIfRxRtp6Cnt_Object = MibTableColumn
vinesIfRxRtp6Cnt = _VinesIfRxRtp6Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 40),
    _VinesIfRxRtp6Cnt_Type()
)
vinesIfRxRtp6Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp6Cnt.setStatus("mandatory")
_VinesIfRxRtpIllegalCnt_Type = Counter32
_VinesIfRxRtpIllegalCnt_Object = MibTableColumn
vinesIfRxRtpIllegalCnt = _VinesIfRxRtpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 41),
    _VinesIfRxRtpIllegalCnt_Type()
)
vinesIfRxRtpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtpIllegalCnt.setStatus("mandatory")
_VinesIfRxSppCnt_Type = Counter32
_VinesIfRxSppCnt_Object = MibTableColumn
vinesIfRxSppCnt = _VinesIfRxSppCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 42),
    _VinesIfRxSppCnt_Type()
)
vinesIfRxSppCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxSppCnt.setStatus("mandatory")
_VinesIfRxIpUnknownCnt_Type = Counter32
_VinesIfRxIpUnknownCnt_Object = MibTableColumn
vinesIfRxIpUnknownCnt = _VinesIfRxIpUnknownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 43),
    _VinesIfRxIpUnknownCnt_Type()
)
vinesIfRxIpUnknownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpUnknownCnt.setStatus("mandatory")
_VinesIfRxIpcUnknownCnt_Type = Counter32
_VinesIfRxIpcUnknownCnt_Object = MibTableColumn
vinesIfRxIpcUnknownCnt = _VinesIfRxIpcUnknownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 44),
    _VinesIfRxIpcUnknownCnt_Type()
)
vinesIfRxIpcUnknownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpcUnknownCnt.setStatus("mandatory")
_VinesIfRxBcastHelperedCnt_Type = Counter32
_VinesIfRxBcastHelperedCnt_Object = MibTableColumn
vinesIfRxBcastHelperedCnt = _VinesIfRxBcastHelperedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 45),
    _VinesIfRxBcastHelperedCnt_Type()
)
vinesIfRxBcastHelperedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastHelperedCnt.setStatus("mandatory")
_VinesIfRxBcastForwardedCnt_Type = Counter32
_VinesIfRxBcastForwardedCnt_Object = MibTableColumn
vinesIfRxBcastForwardedCnt = _VinesIfRxBcastForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 46),
    _VinesIfRxBcastForwardedCnt_Type()
)
vinesIfRxBcastForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastForwardedCnt.setStatus("mandatory")
_VinesIfRxBcastDuplicateCnt_Type = Counter32
_VinesIfRxBcastDuplicateCnt_Object = MibTableColumn
vinesIfRxBcastDuplicateCnt = _VinesIfRxBcastDuplicateCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 47),
    _VinesIfRxBcastDuplicateCnt_Type()
)
vinesIfRxBcastDuplicateCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastDuplicateCnt.setStatus("mandatory")
_VinesIfRxEchoCnt_Type = Counter32
_VinesIfRxEchoCnt_Object = MibTableColumn
vinesIfRxEchoCnt = _VinesIfRxEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 48),
    _VinesIfRxEchoCnt_Type()
)
vinesIfRxEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxEchoCnt.setStatus("mandatory")
_VinesIfRxMacEchoCnt_Type = Counter32
_VinesIfRxMacEchoCnt_Object = MibTableColumn
vinesIfRxMacEchoCnt = _VinesIfRxMacEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 49),
    _VinesIfRxMacEchoCnt_Type()
)
vinesIfRxMacEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxMacEchoCnt.setStatus("mandatory")
_VinesIfRxProxyReplyCnt_Type = Counter32
_VinesIfRxProxyReplyCnt_Object = MibTableColumn
vinesIfRxProxyReplyCnt = _VinesIfRxProxyReplyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 50),
    _VinesIfRxProxyReplyCnt_Type()
)
vinesIfRxProxyReplyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxProxyReplyCnt.setStatus("mandatory")
_VinesIfTxUnicastCnt_Type = Counter32
_VinesIfTxUnicastCnt_Object = MibTableColumn
vinesIfTxUnicastCnt = _VinesIfTxUnicastCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 51),
    _VinesIfTxUnicastCnt_Type()
)
vinesIfTxUnicastCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxUnicastCnt.setStatus("mandatory")
_VinesIfTxBcastCnt_Type = Counter32
_VinesIfTxBcastCnt_Object = MibTableColumn
vinesIfTxBcastCnt = _VinesIfTxBcastCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 52),
    _VinesIfTxBcastCnt_Type()
)
vinesIfTxBcastCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastCnt.setStatus("mandatory")
_VinesIfTxForwardedCnt_Type = Counter32
_VinesIfTxForwardedCnt_Object = MibTableColumn
vinesIfTxForwardedCnt = _VinesIfTxForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 53),
    _VinesIfTxForwardedCnt_Type()
)
vinesIfTxForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxForwardedCnt.setStatus("mandatory")
_VinesIfTxFailedEncapsCnt_Type = Counter32
_VinesIfTxFailedEncapsCnt_Object = MibTableColumn
vinesIfTxFailedEncapsCnt = _VinesIfTxFailedEncapsCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 54),
    _VinesIfTxFailedEncapsCnt_Type()
)
vinesIfTxFailedEncapsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedEncapsCnt.setStatus("mandatory")
_VinesIfTxFailedAccessCnt_Type = Counter32
_VinesIfTxFailedAccessCnt_Object = MibTableColumn
vinesIfTxFailedAccessCnt = _VinesIfTxFailedAccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 55),
    _VinesIfTxFailedAccessCnt_Type()
)
vinesIfTxFailedAccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedAccessCnt.setStatus("mandatory")
_VinesIfTxFailedDownCnt_Type = Counter32
_VinesIfTxFailedDownCnt_Object = MibTableColumn
vinesIfTxFailedDownCnt = _VinesIfTxFailedDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 56),
    _VinesIfTxFailedDownCnt_Type()
)
vinesIfTxFailedDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedDownCnt.setStatus("mandatory")
_VinesIfTxNotBcastToSourceCnt_Type = Counter32
_VinesIfTxNotBcastToSourceCnt_Object = MibTableColumn
vinesIfTxNotBcastToSourceCnt = _VinesIfTxNotBcastToSourceCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 57),
    _VinesIfTxNotBcastToSourceCnt_Type()
)
vinesIfTxNotBcastToSourceCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastToSourceCnt.setStatus("mandatory")
_VinesIfTxNotBcastNotlanCnt_Type = Counter32
_VinesIfTxNotBcastNotlanCnt_Object = MibTableColumn
vinesIfTxNotBcastNotlanCnt = _VinesIfTxNotBcastNotlanCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 58),
    _VinesIfTxNotBcastNotlanCnt_Type()
)
vinesIfTxNotBcastNotlanCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastNotlanCnt.setStatus("mandatory")
_VinesIfTxNotBcastNotgt4800Cnt_Type = Counter32
_VinesIfTxNotBcastNotgt4800Cnt_Object = MibTableColumn
vinesIfTxNotBcastNotgt4800Cnt = _VinesIfTxNotBcastNotgt4800Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 59),
    _VinesIfTxNotBcastNotgt4800Cnt_Type()
)
vinesIfTxNotBcastNotgt4800Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastNotgt4800Cnt.setStatus("mandatory")
_VinesIfTxNotBcastPpchargeCnt_Type = Counter32
_VinesIfTxNotBcastPpchargeCnt_Object = MibTableColumn
vinesIfTxNotBcastPpchargeCnt = _VinesIfTxNotBcastPpchargeCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 60),
    _VinesIfTxNotBcastPpchargeCnt_Type()
)
vinesIfTxNotBcastPpchargeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastPpchargeCnt.setStatus("mandatory")
_VinesIfTxBcastForwardedCnt_Type = Counter32
_VinesIfTxBcastForwardedCnt_Object = MibTableColumn
vinesIfTxBcastForwardedCnt = _VinesIfTxBcastForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 61),
    _VinesIfTxBcastForwardedCnt_Type()
)
vinesIfTxBcastForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastForwardedCnt.setStatus("mandatory")
_VinesIfTxBcastHelperedCnt_Type = Counter32
_VinesIfTxBcastHelperedCnt_Object = MibTableColumn
vinesIfTxBcastHelperedCnt = _VinesIfTxBcastHelperedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 62),
    _VinesIfTxBcastHelperedCnt_Type()
)
vinesIfTxBcastHelperedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastHelperedCnt.setStatus("mandatory")
_VinesIfTxArp0Cnt_Type = Counter32
_VinesIfTxArp0Cnt_Object = MibTableColumn
vinesIfTxArp0Cnt = _VinesIfTxArp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 63),
    _VinesIfTxArp0Cnt_Type()
)
vinesIfTxArp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp0Cnt.setStatus("mandatory")
_VinesIfTxArp1Cnt_Type = Counter32
_VinesIfTxArp1Cnt_Object = MibTableColumn
vinesIfTxArp1Cnt = _VinesIfTxArp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 64),
    _VinesIfTxArp1Cnt_Type()
)
vinesIfTxArp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp1Cnt.setStatus("mandatory")
_VinesIfTxArp2Cnt_Type = Counter32
_VinesIfTxArp2Cnt_Object = MibTableColumn
vinesIfTxArp2Cnt = _VinesIfTxArp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 65),
    _VinesIfTxArp2Cnt_Type()
)
vinesIfTxArp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp2Cnt.setStatus("mandatory")
_VinesIfTxArp3Cnt_Type = Counter32
_VinesIfTxArp3Cnt_Object = MibTableColumn
vinesIfTxArp3Cnt = _VinesIfTxArp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 66),
    _VinesIfTxArp3Cnt_Type()
)
vinesIfTxArp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp3Cnt.setStatus("mandatory")
_VinesIfTxIcpErrorCnt_Type = Counter32
_VinesIfTxIcpErrorCnt_Object = MibTableColumn
vinesIfTxIcpErrorCnt = _VinesIfTxIcpErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 67),
    _VinesIfTxIcpErrorCnt_Type()
)
vinesIfTxIcpErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIcpErrorCnt.setStatus("mandatory")
_VinesIfTxIcpMetricCnt_Type = Counter32
_VinesIfTxIcpMetricCnt_Object = MibTableColumn
vinesIfTxIcpMetricCnt = _VinesIfTxIcpMetricCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 68),
    _VinesIfTxIcpMetricCnt_Type()
)
vinesIfTxIcpMetricCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIcpMetricCnt.setStatus("mandatory")
_VinesIfTxIpcCnt_Type = Counter32
_VinesIfTxIpcCnt_Object = MibTableColumn
vinesIfTxIpcCnt = _VinesIfTxIpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 69),
    _VinesIfTxIpcCnt_Type()
)
vinesIfTxIpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIpcCnt.setStatus("mandatory")
_VinesIfTxRtp0Cnt_Type = Counter32
_VinesIfTxRtp0Cnt_Object = MibTableColumn
vinesIfTxRtp0Cnt = _VinesIfTxRtp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 70),
    _VinesIfTxRtp0Cnt_Type()
)
vinesIfTxRtp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp0Cnt.setStatus("mandatory")
_VinesIfTxRtp1Cnt_Type = Counter32
_VinesIfTxRtp1Cnt_Object = MibTableColumn
vinesIfTxRtp1Cnt = _VinesIfTxRtp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 71),
    _VinesIfTxRtp1Cnt_Type()
)
vinesIfTxRtp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp1Cnt.setStatus("mandatory")
_VinesIfTxRtp2Cnt_Type = Counter32
_VinesIfTxRtp2Cnt_Object = MibTableColumn
vinesIfTxRtp2Cnt = _VinesIfTxRtp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 72),
    _VinesIfTxRtp2Cnt_Type()
)
vinesIfTxRtp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp2Cnt.setStatus("mandatory")
_VinesIfTxRtp3Cnt_Type = Counter32
_VinesIfTxRtp3Cnt_Object = MibTableColumn
vinesIfTxRtp3Cnt = _VinesIfTxRtp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 73),
    _VinesIfTxRtp3Cnt_Type()
)
vinesIfTxRtp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp3Cnt.setStatus("mandatory")
_VinesIfTxRtp4Cnt_Type = Counter32
_VinesIfTxRtp4Cnt_Object = MibTableColumn
vinesIfTxRtp4Cnt = _VinesIfTxRtp4Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 74),
    _VinesIfTxRtp4Cnt_Type()
)
vinesIfTxRtp4Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp4Cnt.setStatus("mandatory")
_VinesIfTxRtp5Cnt_Type = Counter32
_VinesIfTxRtp5Cnt_Object = MibTableColumn
vinesIfTxRtp5Cnt = _VinesIfTxRtp5Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 75),
    _VinesIfTxRtp5Cnt_Type()
)
vinesIfTxRtp5Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp5Cnt.setStatus("mandatory")
_VinesIfTxRtp6Cnt_Type = Counter32
_VinesIfTxRtp6Cnt_Object = MibTableColumn
vinesIfTxRtp6Cnt = _VinesIfTxRtp6Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 76),
    _VinesIfTxRtp6Cnt_Type()
)
vinesIfTxRtp6Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp6Cnt.setStatus("mandatory")
_VinesIfTxSppCnt_Type = Counter32
_VinesIfTxSppCnt_Object = MibTableColumn
vinesIfTxSppCnt = _VinesIfTxSppCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 77),
    _VinesIfTxSppCnt_Type()
)
vinesIfTxSppCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxSppCnt.setStatus("mandatory")
_VinesIfTxEchoCnt_Type = Counter32
_VinesIfTxEchoCnt_Object = MibTableColumn
vinesIfTxEchoCnt = _VinesIfTxEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 78),
    _VinesIfTxEchoCnt_Type()
)
vinesIfTxEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxEchoCnt.setStatus("mandatory")
_VinesIfTxMacEchoCnt_Type = Counter32
_VinesIfTxMacEchoCnt_Object = MibTableColumn
vinesIfTxMacEchoCnt = _VinesIfTxMacEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 79),
    _VinesIfTxMacEchoCnt_Type()
)
vinesIfTxMacEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxMacEchoCnt.setStatus("mandatory")
_VinesIfTxProxyCnt_Type = Counter32
_VinesIfTxProxyCnt_Object = MibTableColumn
vinesIfTxProxyCnt = _VinesIfTxProxyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 80),
    _VinesIfTxProxyCnt_Type()
)
vinesIfTxProxyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxProxyCnt.setStatus("mandatory")
_VinesIfInputRouterFilter_Type = Integer32
_VinesIfInputRouterFilter_Object = MibTableColumn
vinesIfInputRouterFilter = _VinesIfInputRouterFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 81),
    _VinesIfInputRouterFilter_Type()
)
vinesIfInputRouterFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfInputRouterFilter.setStatus("mandatory")
_VinesIfInputNetworkFilter_Type = Integer32
_VinesIfInputNetworkFilter_Object = MibTableColumn
vinesIfInputNetworkFilter = _VinesIfInputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 82),
    _VinesIfInputNetworkFilter_Type()
)
vinesIfInputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfInputNetworkFilter.setStatus("mandatory")
_VinesIfOutputNetworkFilter_Type = Integer32
_VinesIfOutputNetworkFilter_Object = MibTableColumn
vinesIfOutputNetworkFilter = _VinesIfOutputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 83),
    _VinesIfOutputNetworkFilter_Type()
)
vinesIfOutputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfOutputNetworkFilter.setStatus("mandatory")
_Tmpchassis_ObjectIdentity = ObjectIdentity
tmpchassis = _Tmpchassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 6)
)


class _ChassisType_Type(Integer32):
    """Custom type chassisType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("agsplus", 3),
          ("c2000", 5),
          ("c2500", 11),
          ("c3000", 6),
          ("c4000", 7),
          ("c4500", 12),
          ("c7000", 8),
          ("c7010", 10),
          ("cs-500", 9),
          ("igs", 4),
          ("multibus", 2),
          ("unknown", 1))
    )


_ChassisType_Type.__name__ = "Integer32"
_ChassisType_Object = MibScalar
chassisType = _ChassisType_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 1),
    _ChassisType_Type()
)
chassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisType.setStatus("mandatory")
_ChassisVersion_Type = DisplayString
_ChassisVersion_Object = MibScalar
chassisVersion = _ChassisVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 2),
    _ChassisVersion_Type()
)
chassisVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisVersion.setStatus("mandatory")
_ChassisId_Type = DisplayString
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 3),
    _ChassisId_Type()
)
chassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisId.setStatus("mandatory")
_RomVersion_Type = DisplayString
_RomVersion_Object = MibScalar
romVersion = _RomVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 4),
    _RomVersion_Type()
)
romVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romVersion.setStatus("mandatory")
_RomSysVersion_Type = DisplayString
_RomSysVersion_Object = MibScalar
romSysVersion = _RomSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 5),
    _RomSysVersion_Type()
)
romSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    romSysVersion.setStatus("mandatory")
_ProcessorRam_Type = Integer32
_ProcessorRam_Object = MibScalar
processorRam = _ProcessorRam_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 6),
    _ProcessorRam_Type()
)
processorRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    processorRam.setStatus("mandatory")
_NvRAMSize_Type = Integer32
_NvRAMSize_Object = MibScalar
nvRAMSize = _NvRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 7),
    _NvRAMSize_Type()
)
nvRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvRAMSize.setStatus("mandatory")
_NvRAMUsed_Type = Integer32
_NvRAMUsed_Object = MibScalar
nvRAMUsed = _NvRAMUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 8),
    _NvRAMUsed_Type()
)
nvRAMUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvRAMUsed.setStatus("mandatory")
_ConfigRegister_Type = Integer32
_ConfigRegister_Object = MibScalar
configRegister = _ConfigRegister_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 9),
    _ConfigRegister_Type()
)
configRegister.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRegister.setStatus("mandatory")
_ConfigRegNext_Type = Integer32
_ConfigRegNext_Object = MibScalar
configRegNext = _ConfigRegNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 10),
    _ConfigRegNext_Type()
)
configRegNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRegNext.setStatus("mandatory")
_CardTable_Object = MibTable
cardTable = _CardTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11)
)
if mibBuilder.loadTexts:
    cardTable.setStatus("mandatory")
_CardTableEntry_Object = MibTableRow
cardTableEntry = _CardTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1)
)
cardTableEntry.setIndexNames(
    (0, "CISCO-MIB", "cardIndex"),
)
if mibBuilder.loadTexts:
    cardTableEntry.setStatus("mandatory")
_CardIndex_Type = Integer32
_CardIndex_Object = MibTableColumn
cardIndex = _CardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 1),
    _CardIndex_Type()
)
cardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardIndex.setStatus("mandatory")


class _CardType_Type(Integer32):
    """Custom type cardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              20,
              21,
              22,
              23,
              24,
              40,
              41,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              80,
              81,
              82,
              83,
              84,
              100,
              101,
              110,
              111,
              112,
              113,
              114,
              115,
              116,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209)
        )
    )
    namedValues = NamedValues(
        *(("aip", 157),
          ("csc-16", 40),
          ("csc-1r", 83),
          ("csc-2r", 84),
          ("csc-a", 50),
          ("csc-cctl1", 100),
          ("csc-cctl2", 101),
          ("csc-ctr", 116),
          ("csc-e1", 51),
          ("csc-e2", 52),
          ("csc-envm", 24),
          ("csc-fci", 113),
          ("csc-fcit", 114),
          ("csc-hsci", 115),
          ("csc-m", 20),
          ("csc-mc", 22),
          ("csc-mcplus", 23),
          ("csc-mec2", 110),
          ("csc-mec4", 111),
          ("csc-mec6", 112),
          ("csc-mt", 21),
          ("csc-p", 41),
          ("csc-r", 80),
          ("csc-r16", 81),
          ("csc-r16m", 82),
          ("csc-s", 54),
          ("csc-t", 55),
          ("csc-y", 53),
          ("csc1", 2),
          ("csc2", 3),
          ("csc3", 4),
          ("csc4", 5),
          ("eip", 151),
          ("fip", 152),
          ("fsip", 156),
          ("hip", 153),
          ("mci1e", 64),
          ("mci1e1s", 67),
          ("mci1e1s1t", 68),
          ("mci1e1t", 65),
          ("mci1e2s", 69),
          ("mci1e2t", 66),
          ("mci1s", 61),
          ("mci1s1t", 62),
          ("mci1t", 59),
          ("mci2e", 70),
          ("mci2e1s", 73),
          ("mci2e1s1t", 74),
          ("mci2e1t", 71),
          ("mci2e2s", 75),
          ("mci2e2t", 72),
          ("mci2s", 63),
          ("mci2t", 60),
          ("mip", 158),
          ("npm-4000-1e", 202),
          ("npm-4000-1r", 203),
          ("npm-4000-2e", 206),
          ("npm-4000-2e1", 205),
          ("npm-4000-2r", 208),
          ("npm-4000-2r1", 207),
          ("npm-4000-2s", 204),
          ("npm-4000-4t", 209),
          ("npm-4000-fddi-das", 201),
          ("npm-4000-fddi-sas", 200),
          ("rp", 6),
          ("sci2s2t", 57),
          ("sci4s", 56),
          ("sci4t", 58),
          ("sip", 154),
          ("sp", 150),
          ("ssp", 159),
          ("trip", 155),
          ("unknown", 1))
    )


_CardType_Type.__name__ = "Integer32"
_CardType_Object = MibTableColumn
cardType = _CardType_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 2),
    _CardType_Type()
)
cardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardType.setStatus("mandatory")
_CardDescr_Type = DisplayString
_CardDescr_Object = MibTableColumn
cardDescr = _CardDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 3),
    _CardDescr_Type()
)
cardDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardDescr.setStatus("mandatory")
_CardSerial_Type = Integer32
_CardSerial_Object = MibTableColumn
cardSerial = _CardSerial_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 4),
    _CardSerial_Type()
)
cardSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSerial.setStatus("mandatory")
_CardHwVersion_Type = DisplayString
_CardHwVersion_Object = MibTableColumn
cardHwVersion = _CardHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 5),
    _CardHwVersion_Type()
)
cardHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardHwVersion.setStatus("mandatory")
_CardSwVersion_Type = DisplayString
_CardSwVersion_Object = MibTableColumn
cardSwVersion = _CardSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 6),
    _CardSwVersion_Type()
)
cardSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSwVersion.setStatus("mandatory")
_CardSlotNumber_Type = Integer32
_CardSlotNumber_Object = MibTableColumn
cardSlotNumber = _CardSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 11, 1, 7),
    _CardSlotNumber_Type()
)
cardSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardSlotNumber.setStatus("mandatory")
_ChassisSlots_Type = Integer32
_ChassisSlots_Object = MibScalar
chassisSlots = _ChassisSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 6, 12),
    _ChassisSlots_Type()
)
chassisSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlots.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-MIB",
    **{"cisco": cisco,
       "products": products,
       "gateway-server": gateway_server,
       "terminal-server": terminal_server,
       "trouter": trouter,
       "protocol-translator": protocol_translator,
       "igs-sysID": igs_sysID,
       "c3000-sysID": c3000_sysID,
       "c4000-sysID": c4000_sysID,
       "c7000-sysID": c7000_sysID,
       "cs-500-sysID": cs_500_sysID,
       "c2000-sysID": c2000_sysID,
       "agsplus-sysID": agsplus_sysID,
       "c7010-sysID": c7010_sysID,
       "c2500-sysID": c2500_sysID,
       "c4500-sysID": c4500_sysID,
       "local": local,
       "lsystem": lsystem,
       "romId": romId,
       "whyReload": whyReload,
       "hostName": hostName,
       "domainName": domainName,
       "authAddr": authAddr,
       "bootHost": bootHost,
       "ping": ping,
       "freeMem": freeMem,
       "bufferElFree": bufferElFree,
       "bufferElMax": bufferElMax,
       "bufferElHit": bufferElHit,
       "bufferElMiss": bufferElMiss,
       "bufferElCreate": bufferElCreate,
       "bufferSmSize": bufferSmSize,
       "bufferSmTotal": bufferSmTotal,
       "bufferSmFree": bufferSmFree,
       "bufferSmMax": bufferSmMax,
       "bufferSmHit": bufferSmHit,
       "bufferSmMiss": bufferSmMiss,
       "bufferSmTrim": bufferSmTrim,
       "bufferSmCreate": bufferSmCreate,
       "bufferMdSize": bufferMdSize,
       "bufferMdTotal": bufferMdTotal,
       "bufferMdFree": bufferMdFree,
       "bufferMdMax": bufferMdMax,
       "bufferMdHit": bufferMdHit,
       "bufferMdMiss": bufferMdMiss,
       "bufferMdTrim": bufferMdTrim,
       "bufferMdCreate": bufferMdCreate,
       "bufferBgSize": bufferBgSize,
       "bufferBgTotal": bufferBgTotal,
       "bufferBgFree": bufferBgFree,
       "bufferBgMax": bufferBgMax,
       "bufferBgHit": bufferBgHit,
       "bufferBgMiss": bufferBgMiss,
       "bufferBgTrim": bufferBgTrim,
       "bufferBgCreate": bufferBgCreate,
       "bufferLgSize": bufferLgSize,
       "bufferLgTotal": bufferLgTotal,
       "bufferLgFree": bufferLgFree,
       "bufferLgMax": bufferLgMax,
       "bufferLgHit": bufferLgHit,
       "bufferLgMiss": bufferLgMiss,
       "bufferLgTrim": bufferLgTrim,
       "bufferLgCreate": bufferLgCreate,
       "bufferFail": bufferFail,
       "bufferNoMem": bufferNoMem,
       "netConfigAddr": netConfigAddr,
       "netConfigName": netConfigName,
       "netConfigSet": netConfigSet,
       "hostConfigAddr": hostConfigAddr,
       "hostConfigName": hostConfigName,
       "hostConfigSet": hostConfigSet,
       "writeMem": writeMem,
       "writeNet": writeNet,
       "busyPer": busyPer,
       "avgBusy1": avgBusy1,
       "avgBusy5": avgBusy5,
       "idleCount": idleCount,
       "idleWired": idleWired,
       "ciscoContactInfo": ciscoContactInfo,
       "bufferHgSize": bufferHgSize,
       "bufferHgTotal": bufferHgTotal,
       "bufferHgFree": bufferHgFree,
       "bufferHgMax": bufferHgMax,
       "bufferHgHit": bufferHgHit,
       "bufferHgMiss": bufferHgMiss,
       "bufferHgTrim": bufferHgTrim,
       "bufferHgCreate": bufferHgCreate,
       "netConfigProto": netConfigProto,
       "hostConfigProto": hostConfigProto,
       "sysConfigAddr": sysConfigAddr,
       "sysConfigName": sysConfigName,
       "sysConfigProto": sysConfigProto,
       "sysClearARP": sysClearARP,
       "sysClearInt": sysClearInt,
       "envPresent": envPresent,
       "envTestPt1Descr": envTestPt1Descr,
       "envTestPt1Measure": envTestPt1Measure,
       "envTestPt2Descr": envTestPt2Descr,
       "envTestPt2Measure": envTestPt2Measure,
       "envTestPt3Descr": envTestPt3Descr,
       "envTestPt3Measure": envTestPt3Measure,
       "envTestPt4Descr": envTestPt4Descr,
       "envTestPt4Measure": envTestPt4Measure,
       "envTestPt5Descr": envTestPt5Descr,
       "envTestPt5Measure": envTestPt5Measure,
       "envTestPt6Descr": envTestPt6Descr,
       "envTestPt6Measure": envTestPt6Measure,
       "envTestPt1MarginVal": envTestPt1MarginVal,
       "envTestPt2MarginVal": envTestPt2MarginVal,
       "envTestPt3MarginPercent": envTestPt3MarginPercent,
       "envTestPt4MarginPercent": envTestPt4MarginPercent,
       "envTestPt5MarginPercent": envTestPt5MarginPercent,
       "envTestPt6MarginPercent": envTestPt6MarginPercent,
       "envTestPt1last": envTestPt1last,
       "envTestPt2last": envTestPt2last,
       "envTestPt3last": envTestPt3last,
       "envTestPt4last": envTestPt4last,
       "envTestPt5last": envTestPt5last,
       "envTestPt6last": envTestPt6last,
       "envTestPt1warn": envTestPt1warn,
       "envTestPt2warn": envTestPt2warn,
       "envTestPt3warn": envTestPt3warn,
       "envTestPt4warn": envTestPt4warn,
       "envTestPt5warn": envTestPt5warn,
       "envTestPt6warn": envTestPt6warn,
       "envFirmVersion": envFirmVersion,
       "envTechnicianID": envTechnicianID,
       "envType": envType,
       "envBurnDate": envBurnDate,
       "envSerialNumber": envSerialNumber,
       "linterfaces": linterfaces,
       "lifTable": lifTable,
       "lifEntry": lifEntry,
       "locIfHardType": locIfHardType,
       "locIfLineProt": locIfLineProt,
       "locIfLastIn": locIfLastIn,
       "locIfLastOut": locIfLastOut,
       "locIfLastOutHang": locIfLastOutHang,
       "locIfInBitsSec": locIfInBitsSec,
       "locIfInPktsSec": locIfInPktsSec,
       "locIfOutBitsSec": locIfOutBitsSec,
       "locIfOutPktsSec": locIfOutPktsSec,
       "locIfInRunts": locIfInRunts,
       "locIfInGiants": locIfInGiants,
       "locIfInCRC": locIfInCRC,
       "locIfInFrame": locIfInFrame,
       "locIfInOverrun": locIfInOverrun,
       "locIfInIgnored": locIfInIgnored,
       "locIfInAbort": locIfInAbort,
       "locIfResets": locIfResets,
       "locIfRestarts": locIfRestarts,
       "locIfKeep": locIfKeep,
       "locIfReason": locIfReason,
       "locIfCarTrans": locIfCarTrans,
       "locIfReliab": locIfReliab,
       "locIfDelay": locIfDelay,
       "locIfLoad": locIfLoad,
       "locIfCollisions": locIfCollisions,
       "locIfInputQueueDrops": locIfInputQueueDrops,
       "locIfOutputQueueDrops": locIfOutputQueueDrops,
       "locIfDescr": locIfDescr,
       "locIfSlowInPkts": locIfSlowInPkts,
       "locIfSlowOutPkts": locIfSlowOutPkts,
       "locIfSlowInOctets": locIfSlowInOctets,
       "locIfSlowOutOctets": locIfSlowOutOctets,
       "locIfFastInPkts": locIfFastInPkts,
       "locIfFastOutPkts": locIfFastOutPkts,
       "locIfFastInOctets": locIfFastInOctets,
       "locIfFastOutOctets": locIfFastOutOctets,
       "locIfotherInPkts": locIfotherInPkts,
       "locIfotherOutPkts": locIfotherOutPkts,
       "locIfotherInOctets": locIfotherInOctets,
       "locIfotherOutOctets": locIfotherOutOctets,
       "locIfipInPkts": locIfipInPkts,
       "locIfipOutPkts": locIfipOutPkts,
       "locIfipInOctets": locIfipInOctets,
       "locIfipOutOctets": locIfipOutOctets,
       "locIfdecnetInPkts": locIfdecnetInPkts,
       "locIfdecnetOutPkts": locIfdecnetOutPkts,
       "locIfdecnetInOctets": locIfdecnetInOctets,
       "locIfdecnetOutOctets": locIfdecnetOutOctets,
       "locIfxnsInPkts": locIfxnsInPkts,
       "locIfxnsOutPkts": locIfxnsOutPkts,
       "locIfxnsInOctets": locIfxnsInOctets,
       "locIfxnsOutOctets": locIfxnsOutOctets,
       "locIfclnsInPkts": locIfclnsInPkts,
       "locIfclnsOutPkts": locIfclnsOutPkts,
       "locIfclnsInOctets": locIfclnsInOctets,
       "locIfclnsOutOctets": locIfclnsOutOctets,
       "locIfappletalkInPkts": locIfappletalkInPkts,
       "locIfappletalkOutPkts": locIfappletalkOutPkts,
       "locIfappletalkInOctets": locIfappletalkInOctets,
       "locIfappletalkOutOctets": locIfappletalkOutOctets,
       "locIfnovellInPkts": locIfnovellInPkts,
       "locIfnovellOutPkts": locIfnovellOutPkts,
       "locIfnovellInOctets": locIfnovellInOctets,
       "locIfnovellOutOctets": locIfnovellOutOctets,
       "locIfapolloInPkts": locIfapolloInPkts,
       "locIfapolloOutPkts": locIfapolloOutPkts,
       "locIfapolloInOctets": locIfapolloInOctets,
       "locIfapolloOutOctets": locIfapolloOutOctets,
       "locIfvinesInPkts": locIfvinesInPkts,
       "locIfvinesOutPkts": locIfvinesOutPkts,
       "locIfvinesInOctets": locIfvinesInOctets,
       "locIfvinesOutOctets": locIfvinesOutOctets,
       "locIfbridgedInPkts": locIfbridgedInPkts,
       "locIfbridgedOutPkts": locIfbridgedOutPkts,
       "locIfbridgedInOctets": locIfbridgedInOctets,
       "locIfbridgedOutOctets": locIfbridgedOutOctets,
       "locIfsrbInPkts": locIfsrbInPkts,
       "locIfsrbOutPkts": locIfsrbOutPkts,
       "locIfsrbInOctets": locIfsrbInOctets,
       "locIfsrbOutOctets": locIfsrbOutOctets,
       "locIfchaosInPkts": locIfchaosInPkts,
       "locIfchaosOutPkts": locIfchaosOutPkts,
       "locIfchaosInOctets": locIfchaosInOctets,
       "locIfchaosOutOctets": locIfchaosOutOctets,
       "locIfpupInPkts": locIfpupInPkts,
       "locIfpupOutPkts": locIfpupOutPkts,
       "locIfpupInOctets": locIfpupInOctets,
       "locIfpupOutOctets": locIfpupOutOctets,
       "locIfmopInPkts": locIfmopInPkts,
       "locIfmopOutPkts": locIfmopOutPkts,
       "locIfmopInOctets": locIfmopInOctets,
       "locIfmopOutOctets": locIfmopOutOctets,
       "locIflanmanInPkts": locIflanmanInPkts,
       "locIflanmanOutPkts": locIflanmanOutPkts,
       "locIflanmanInOctets": locIflanmanInOctets,
       "locIflanmanOutOctets": locIflanmanOutOctets,
       "locIfstunInPkts": locIfstunInPkts,
       "locIfstunOutPkts": locIfstunOutPkts,
       "locIfstunInOctets": locIfstunInOctets,
       "locIfstunOutOctets": locIfstunOutOctets,
       "locIfspanInPkts": locIfspanInPkts,
       "locIfspanOutPkts": locIfspanOutPkts,
       "locIfspanInOctets": locIfspanInOctets,
       "locIfspanOutOctets": locIfspanOutOctets,
       "locIfarpInPkts": locIfarpInPkts,
       "locIfarpOutPkts": locIfarpOutPkts,
       "locIfarpInOctets": locIfarpInOctets,
       "locIfarpOutOctets": locIfarpOutOctets,
       "locIfprobeInPkts": locIfprobeInPkts,
       "locIfprobeOutPkts": locIfprobeOutPkts,
       "locIfprobeInOctets": locIfprobeInOctets,
       "locIfprobeOutOctets": locIfprobeOutOctets,
       "locIfDribbleInputs": locIfDribbleInputs,
       "lfsipTable": lfsipTable,
       "lFSIPEntry": lFSIPEntry,
       "locIfFSIPIndex": locIfFSIPIndex,
       "locIfFSIPtype": locIfFSIPtype,
       "locIfFSIPrts": locIfFSIPrts,
       "locIfFSIPcts": locIfFSIPcts,
       "locIfFSIPdtr": locIfFSIPdtr,
       "locIfFSIPdcd": locIfFSIPdcd,
       "locIfFSIPdsr": locIfFSIPdsr,
       "lat": lat,
       "lip": lip,
       "lipAddrTable": lipAddrTable,
       "lipAddrEntry": lipAddrEntry,
       "locIPHow": locIPHow,
       "locIPWho": locIPWho,
       "locIPHelper": locIPHelper,
       "locIPSecurity": locIPSecurity,
       "locIPRedirects": locIPRedirects,
       "locIPUnreach": locIPUnreach,
       "lipRoutingTable": lipRoutingTable,
       "lipRouteEntry": lipRouteEntry,
       "locRtMask": locRtMask,
       "locRtCount": locRtCount,
       "locRtUses": locRtUses,
       "actThresh": actThresh,
       "actLostPkts": actLostPkts,
       "actLostByts": actLostByts,
       "lipAccountingTable": lipAccountingTable,
       "lipAccountEntry": lipAccountEntry,
       "actSrc": actSrc,
       "actDst": actDst,
       "actPkts": actPkts,
       "actByts": actByts,
       "actAge": actAge,
       "lipCkAccountingTable": lipCkAccountingTable,
       "lipCkAccountEntry": lipCkAccountEntry,
       "ckactSrc": ckactSrc,
       "ckactDst": ckactDst,
       "ckactPkts": ckactPkts,
       "ckactByts": ckactByts,
       "ckactAge": ckactAge,
       "actCheckPoint": actCheckPoint,
       "ipNoaccess": ipNoaccess,
       "licmp": licmp,
       "ltcp": ltcp,
       "ltcpConnTable": ltcpConnTable,
       "ltcpConnEntry": ltcpConnEntry,
       "loctcpConnInBytes": loctcpConnInBytes,
       "loctcpConnOutBytes": loctcpConnOutBytes,
       "loctcpConnInPkts": loctcpConnInPkts,
       "loctcpConnOutPkts": loctcpConnOutPkts,
       "loctcpConnElapsed": loctcpConnElapsed,
       "ludp": ludp,
       "legp": legp,
       "lts": lts,
       "tsLines": tsLines,
       "ltsLineTable": ltsLineTable,
       "ltsLineEntry": ltsLineEntry,
       "tsLineActive": tsLineActive,
       "tsLineType": tsLineType,
       "tsLineAutobaud": tsLineAutobaud,
       "tsLineSpeedin": tsLineSpeedin,
       "tsLineSpeedout": tsLineSpeedout,
       "tsLineFlow": tsLineFlow,
       "tsLineModem": tsLineModem,
       "tsLineLoc": tsLineLoc,
       "tsLineTerm": tsLineTerm,
       "tsLineScrlen": tsLineScrlen,
       "tsLineScrwid": tsLineScrwid,
       "tsLineEsc": tsLineEsc,
       "tsLineTmo": tsLineTmo,
       "tsLineSestmo": tsLineSestmo,
       "tsLineRotary": tsLineRotary,
       "tsLineUses": tsLineUses,
       "tsLineNses": tsLineNses,
       "tsLineUser": tsLineUser,
       "tsLineNoise": tsLineNoise,
       "tsLineNum": tsLineNum,
       "ltsLineSessionTable": ltsLineSessionTable,
       "ltsLineSessionEntry": ltsLineSessionEntry,
       "tslineSesType": tslineSesType,
       "tslineSesDir": tslineSesDir,
       "tslineSesAddr": tslineSesAddr,
       "tslineSesName": tslineSesName,
       "tslineSesCur": tslineSesCur,
       "tslineSesIdle": tslineSesIdle,
       "tslineSesLine": tslineSesLine,
       "tslineSesSession": tslineSesSession,
       "tsMsgTtyLine": tsMsgTtyLine,
       "tsMsgIntervaltim": tsMsgIntervaltim,
       "tsMsgDuration": tsMsgDuration,
       "tsMsgText": tsMsgText,
       "tsMsgTmpBanner": tsMsgTmpBanner,
       "tsMsgSend": tsMsgSend,
       "lflash": lflash,
       "flashSize": flashSize,
       "flashFree": flashFree,
       "flashController": flashController,
       "flashCard": flashCard,
       "flashVPP": flashVPP,
       "flashErase": flashErase,
       "flashEraseTime": flashEraseTime,
       "flashEraseStatus": flashEraseStatus,
       "flashToNet": flashToNet,
       "flashToNetTime": flashToNetTime,
       "flashToNetStatus": flashToNetStatus,
       "netToFlash": netToFlash,
       "netToFlashTime": netToFlashTime,
       "netToFlashStatus": netToFlashStatus,
       "flashStatus": flashStatus,
       "flashEntries": flashEntries,
       "lflashFileDirTable": lflashFileDirTable,
       "lflashFileDirEntry": lflashFileDirEntry,
       "flashDirName": flashDirName,
       "flashDirSize": flashDirSize,
       "flashDirStatus": flashDirStatus,
       "temporary": temporary,
       "tmpdecnet": tmpdecnet,
       "dnForward": dnForward,
       "dnReceived": dnReceived,
       "dnFormaterr": dnFormaterr,
       "dnNotgateway": dnNotgateway,
       "dnNotimp": dnNotimp,
       "dnHellos": dnHellos,
       "dnBadhello": dnBadhello,
       "dnNotlong": dnNotlong,
       "dnDatas": dnDatas,
       "dnBigaddr": dnBigaddr,
       "dnNoroute": dnNoroute,
       "dnNoencap": dnNoencap,
       "dnLevel1s": dnLevel1s,
       "dnBadlevel1": dnBadlevel1,
       "dnToomanyhops": dnToomanyhops,
       "dnHellosent": dnHellosent,
       "dnLevel1sent": dnLevel1sent,
       "dnNomemory": dnNomemory,
       "dnOtherhello": dnOtherhello,
       "dnOtherlevel1": dnOtherlevel1,
       "dnLevel2s": dnLevel2s,
       "dnLevel2sent": dnLevel2sent,
       "dnNovector": dnNovector,
       "dnOtherlevel2": dnOtherlevel2,
       "dnNoaccess": dnNoaccess,
       "dnAreaTable": dnAreaTable,
       "dnAreaTableEntry": dnAreaTableEntry,
       "dnArea": dnArea,
       "dnACost": dnACost,
       "dnAHop": dnAHop,
       "dnAIfIndex": dnAIfIndex,
       "dnANextHop": dnANextHop,
       "dnAAge": dnAAge,
       "dnAPrio": dnAPrio,
       "dnHostTable": dnHostTable,
       "dnHostTableEntry": dnHostTableEntry,
       "dnHost": dnHost,
       "dnHCost": dnHCost,
       "dnHHop": dnHHop,
       "dnHIfIndex": dnHIfIndex,
       "dnHNextHop": dnHNextHop,
       "dnHAge": dnHAge,
       "dnHPrio": dnHPrio,
       "dnHIdx1": dnHIdx1,
       "dnHIdx2": dnHIdx2,
       "dnIfTable": dnIfTable,
       "dnIfTableEntry": dnIfTableEntry,
       "dnIfCost": dnIfCost,
       "tmpxns": tmpxns,
       "xnsInput": xnsInput,
       "xnsLocal": xnsLocal,
       "xnsBcastin": xnsBcastin,
       "xnsForward": xnsForward,
       "xnsBcastout": xnsBcastout,
       "xnsErrin": xnsErrin,
       "xnsErrout": xnsErrout,
       "xnsFormerr": xnsFormerr,
       "xnsChksum": xnsChksum,
       "xnsNotgate": xnsNotgate,
       "xnsHopcnt": xnsHopcnt,
       "xnsNoroute": xnsNoroute,
       "xnsNoencap": xnsNoencap,
       "xnsOutput": xnsOutput,
       "xnsInmult": xnsInmult,
       "xnsUnknown": xnsUnknown,
       "xnsFwdbrd": xnsFwdbrd,
       "xnsEchoreqin": xnsEchoreqin,
       "xnsEchoreqout": xnsEchoreqout,
       "xnsEchorepin": xnsEchorepin,
       "xnsEchorepout": xnsEchorepout,
       "tmpappletalk": tmpappletalk,
       "atInput": atInput,
       "atLocal": atLocal,
       "atBcastin": atBcastin,
       "atForward": atForward,
       "atBcastout": atBcastout,
       "atChksum": atChksum,
       "atNotgate": atNotgate,
       "atHopcnt": atHopcnt,
       "atNoaccess": atNoaccess,
       "atNoroute": atNoroute,
       "atNoencap": atNoencap,
       "atOutput": atOutput,
       "atInmult": atInmult,
       "atRtmpin": atRtmpin,
       "atRtmpout": atRtmpout,
       "atNbpin": atNbpin,
       "atNbpout": atNbpout,
       "atAtp": atAtp,
       "atZipin": atZipin,
       "atZipout": atZipout,
       "atEcho": atEcho,
       "atEchoill": atEchoill,
       "atDdpshort": atDdpshort,
       "atDdplong": atDdplong,
       "atDdpbad": atDdpbad,
       "atNobuffer": atNobuffer,
       "atArpreq": atArpreq,
       "atArpreply": atArpreply,
       "atArpprobe": atArpprobe,
       "atUnknown": atUnknown,
       "tmpnovell": tmpnovell,
       "novellInput": novellInput,
       "novellBcastin": novellBcastin,
       "novellForward": novellForward,
       "novellBcastout": novellBcastout,
       "novellFormerr": novellFormerr,
       "novellChksum": novellChksum,
       "novellHopcnt": novellHopcnt,
       "novellNoroute": novellNoroute,
       "novellNoencap": novellNoencap,
       "novellOutput": novellOutput,
       "novellInmult": novellInmult,
       "novellLocal": novellLocal,
       "novellUnknown": novellUnknown,
       "novellSapreqin": novellSapreqin,
       "novellSapresin": novellSapresin,
       "novellSapout": novellSapout,
       "novellSapreply": novellSapreply,
       "ipxActThresh": ipxActThresh,
       "ipxActLostPkts": ipxActLostPkts,
       "ipxActLostByts": ipxActLostByts,
       "lipxAccountingTable": lipxAccountingTable,
       "lipxAccountingEntry": lipxAccountingEntry,
       "ipxActSrc": ipxActSrc,
       "ipxActDst": ipxActDst,
       "ipxActPkts": ipxActPkts,
       "ipxActByts": ipxActByts,
       "ipxActAge": ipxActAge,
       "lipxCkAccountingTable": lipxCkAccountingTable,
       "lipxCkAccountingEntry": lipxCkAccountingEntry,
       "ipxCkactSrc": ipxCkactSrc,
       "ipxCkactDst": ipxCkactDst,
       "ipxCkactPkts": ipxCkactPkts,
       "ipxCkactByts": ipxCkactByts,
       "ipxCkactAge": ipxCkactAge,
       "ipxActCheckPoint": ipxActCheckPoint,
       "tmpvines": tmpvines,
       "vinesInput": vinesInput,
       "vinesOutput": vinesOutput,
       "vinesLocaldest": vinesLocaldest,
       "vinesForwarded": vinesForwarded,
       "vinesBcastin": vinesBcastin,
       "vinesBcastout": vinesBcastout,
       "vinesBcastfwd": vinesBcastfwd,
       "vinesNotlan": vinesNotlan,
       "vinesNotgt4800": vinesNotgt4800,
       "vinesNocharges": vinesNocharges,
       "vinesFormaterror": vinesFormaterror,
       "vinesCksumerr": vinesCksumerr,
       "vinesHopcount": vinesHopcount,
       "vinesNoroute": vinesNoroute,
       "vinesEncapsfailed": vinesEncapsfailed,
       "vinesUnknown": vinesUnknown,
       "vinesIcpIn": vinesIcpIn,
       "vinesIcpOut": vinesIcpOut,
       "vinesMetricOut": vinesMetricOut,
       "vinesMacEchoIn": vinesMacEchoIn,
       "vinesMacEchoOut": vinesMacEchoOut,
       "vinesEchoIn": vinesEchoIn,
       "vinesEchoOut": vinesEchoOut,
       "vinesProxyCnt": vinesProxyCnt,
       "vinesProxyReplyCnt": vinesProxyReplyCnt,
       "vinesNet": vinesNet,
       "vinesSubNet": vinesSubNet,
       "vinesClient": vinesClient,
       "tmpvinesIfTable": tmpvinesIfTable,
       "tmpvinesIfTableEntry": tmpvinesIfTableEntry,
       "vinesIfMetric": vinesIfMetric,
       "vinesIfEnctype": vinesIfEnctype,
       "vinesIfAccesslist": vinesIfAccesslist,
       "vinesIfPropagate": vinesIfPropagate,
       "vinesIfArpEnabled": vinesIfArpEnabled,
       "vinesIfServerless": vinesIfServerless,
       "vinesIfServerlessBcast": vinesIfServerlessBcast,
       "vinesIfRedirectInterval": vinesIfRedirectInterval,
       "vinesIfSplitDisabled": vinesIfSplitDisabled,
       "vinesIfLineup": vinesIfLineup,
       "vinesIfFastokay": vinesIfFastokay,
       "vinesIfRouteCache": vinesIfRouteCache,
       "vinesIfIns": vinesIfIns,
       "vinesIfOuts": vinesIfOuts,
       "vinesIfInBytes": vinesIfInBytes,
       "vinesIfOutBytes": vinesIfOutBytes,
       "vinesIfRxNotEnabledCnt": vinesIfRxNotEnabledCnt,
       "vinesIfRxFormatErrorCnt": vinesIfRxFormatErrorCnt,
       "vinesIfRxLocalDestCnt": vinesIfRxLocalDestCnt,
       "vinesIfRxBcastinCnt": vinesIfRxBcastinCnt,
       "vinesIfRxForwardedCnt": vinesIfRxForwardedCnt,
       "vinesIfRxNoRouteCnt": vinesIfRxNoRouteCnt,
       "vinesIfRxZeroHopCountCnt": vinesIfRxZeroHopCountCnt,
       "vinesIfRxChecksumErrorCnt": vinesIfRxChecksumErrorCnt,
       "vinesIfRxArp0Cnt": vinesIfRxArp0Cnt,
       "vinesIfRxArp1Cnt": vinesIfRxArp1Cnt,
       "vinesIfRxArp2Cnt": vinesIfRxArp2Cnt,
       "vinesIfRxArp3Cnt": vinesIfRxArp3Cnt,
       "vinesIfRxArpIllegalCnt": vinesIfRxArpIllegalCnt,
       "vinesIfRxIcpErrorCnt": vinesIfRxIcpErrorCnt,
       "vinesIfRxIcpMetricCnt": vinesIfRxIcpMetricCnt,
       "vinesIfRxIcpIllegalCnt": vinesIfRxIcpIllegalCnt,
       "vinesIfRxIpcCnt": vinesIfRxIpcCnt,
       "vinesIfRxRtp0Cnt": vinesIfRxRtp0Cnt,
       "vinesIfRxRtp1Cnt": vinesIfRxRtp1Cnt,
       "vinesIfRxRtp2Cnt": vinesIfRxRtp2Cnt,
       "vinesIfRxRtp3Cnt": vinesIfRxRtp3Cnt,
       "vinesIfRxRtp4Cnt": vinesIfRxRtp4Cnt,
       "vinesIfRxRtp5Cnt": vinesIfRxRtp5Cnt,
       "vinesIfRxRtp6Cnt": vinesIfRxRtp6Cnt,
       "vinesIfRxRtpIllegalCnt": vinesIfRxRtpIllegalCnt,
       "vinesIfRxSppCnt": vinesIfRxSppCnt,
       "vinesIfRxIpUnknownCnt": vinesIfRxIpUnknownCnt,
       "vinesIfRxIpcUnknownCnt": vinesIfRxIpcUnknownCnt,
       "vinesIfRxBcastHelperedCnt": vinesIfRxBcastHelperedCnt,
       "vinesIfRxBcastForwardedCnt": vinesIfRxBcastForwardedCnt,
       "vinesIfRxBcastDuplicateCnt": vinesIfRxBcastDuplicateCnt,
       "vinesIfRxEchoCnt": vinesIfRxEchoCnt,
       "vinesIfRxMacEchoCnt": vinesIfRxMacEchoCnt,
       "vinesIfRxProxyReplyCnt": vinesIfRxProxyReplyCnt,
       "vinesIfTxUnicastCnt": vinesIfTxUnicastCnt,
       "vinesIfTxBcastCnt": vinesIfTxBcastCnt,
       "vinesIfTxForwardedCnt": vinesIfTxForwardedCnt,
       "vinesIfTxFailedEncapsCnt": vinesIfTxFailedEncapsCnt,
       "vinesIfTxFailedAccessCnt": vinesIfTxFailedAccessCnt,
       "vinesIfTxFailedDownCnt": vinesIfTxFailedDownCnt,
       "vinesIfTxNotBcastToSourceCnt": vinesIfTxNotBcastToSourceCnt,
       "vinesIfTxNotBcastNotlanCnt": vinesIfTxNotBcastNotlanCnt,
       "vinesIfTxNotBcastNotgt4800Cnt": vinesIfTxNotBcastNotgt4800Cnt,
       "vinesIfTxNotBcastPpchargeCnt": vinesIfTxNotBcastPpchargeCnt,
       "vinesIfTxBcastForwardedCnt": vinesIfTxBcastForwardedCnt,
       "vinesIfTxBcastHelperedCnt": vinesIfTxBcastHelperedCnt,
       "vinesIfTxArp0Cnt": vinesIfTxArp0Cnt,
       "vinesIfTxArp1Cnt": vinesIfTxArp1Cnt,
       "vinesIfTxArp2Cnt": vinesIfTxArp2Cnt,
       "vinesIfTxArp3Cnt": vinesIfTxArp3Cnt,
       "vinesIfTxIcpErrorCnt": vinesIfTxIcpErrorCnt,
       "vinesIfTxIcpMetricCnt": vinesIfTxIcpMetricCnt,
       "vinesIfTxIpcCnt": vinesIfTxIpcCnt,
       "vinesIfTxRtp0Cnt": vinesIfTxRtp0Cnt,
       "vinesIfTxRtp1Cnt": vinesIfTxRtp1Cnt,
       "vinesIfTxRtp2Cnt": vinesIfTxRtp2Cnt,
       "vinesIfTxRtp3Cnt": vinesIfTxRtp3Cnt,
       "vinesIfTxRtp4Cnt": vinesIfTxRtp4Cnt,
       "vinesIfTxRtp5Cnt": vinesIfTxRtp5Cnt,
       "vinesIfTxRtp6Cnt": vinesIfTxRtp6Cnt,
       "vinesIfTxSppCnt": vinesIfTxSppCnt,
       "vinesIfTxEchoCnt": vinesIfTxEchoCnt,
       "vinesIfTxMacEchoCnt": vinesIfTxMacEchoCnt,
       "vinesIfTxProxyCnt": vinesIfTxProxyCnt,
       "vinesIfInputRouterFilter": vinesIfInputRouterFilter,
       "vinesIfInputNetworkFilter": vinesIfInputNetworkFilter,
       "vinesIfOutputNetworkFilter": vinesIfOutputNetworkFilter,
       "tmpchassis": tmpchassis,
       "chassisType": chassisType,
       "chassisVersion": chassisVersion,
       "chassisId": chassisId,
       "romVersion": romVersion,
       "romSysVersion": romSysVersion,
       "processorRam": processorRam,
       "nvRAMSize": nvRAMSize,
       "nvRAMUsed": nvRAMUsed,
       "configRegister": configRegister,
       "configRegNext": configRegNext,
       "cardTable": cardTable,
       "cardTableEntry": cardTableEntry,
       "cardIndex": cardIndex,
       "cardType": cardType,
       "cardDescr": cardDescr,
       "cardSerial": cardSerial,
       "cardHwVersion": cardHwVersion,
       "cardSwVersion": cardSwVersion,
       "cardSlotNumber": cardSlotNumber,
       "chassisSlots": chassisSlots}
)
