# SNMP MIB module (OLD-CISCO-SYS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-SYS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:05 2024
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

(local,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "local")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

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
    ping.setStatus("obsolete")
_FreeMem_Type = Integer32
_FreeMem_Object = MibScalar
freeMem = _FreeMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 8),
    _FreeMem_Type()
)
freeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMem.setStatus("obsolete")
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
    hostConfigAddr.setStatus("obsolete")
_HostConfigName_Type = DisplayString
_HostConfigName_Object = MibScalar
hostConfigName = _HostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 52),
    _HostConfigName_Type()
)
hostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostConfigName.setStatus("obsolete")
_HostConfigSet_Type = DisplayString
_HostConfigSet_Object = MibScalar
hostConfigSet = _HostConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 2, 1, 53),
    _HostConfigSet_Type()
)
hostConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    hostConfigSet.setStatus("obsolete")
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

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-SYS-MIB",
    **{"lsystem": lsystem,
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
       "envSerialNumber": envSerialNumber}
)
