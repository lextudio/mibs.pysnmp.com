# SNMP MIB module (BDCOM-SYS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BDCOM-SYS
# Produced by pysmi-1.5.4 at Mon Oct 14 20:46:38 2024
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

(bdlocal,) = mibBuilder.importSymbols(
    "BDCOM-SMI",
    "bdlocal")

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

_Bdlsystem_ObjectIdentity = ObjectIdentity
bdlsystem = _Bdlsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1)
)
_BdromId_Type = DisplayString
_BdromId_Object = MibScalar
bdromId = _BdromId_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 1),
    _BdromId_Type()
)
bdromId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdromId.setStatus("mandatory")
_BdwhyReload_Type = DisplayString
_BdwhyReload_Object = MibScalar
bdwhyReload = _BdwhyReload_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 2),
    _BdwhyReload_Type()
)
bdwhyReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdwhyReload.setStatus("mandatory")
_BdhostName_Type = DisplayString
_BdhostName_Object = MibScalar
bdhostName = _BdhostName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 3),
    _BdhostName_Type()
)
bdhostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdhostName.setStatus("mandatory")
_BddomainName_Type = DisplayString
_BddomainName_Object = MibScalar
bddomainName = _BddomainName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 4),
    _BddomainName_Type()
)
bddomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bddomainName.setStatus("mandatory")
_BdauthAddr_Type = IpAddress
_BdauthAddr_Object = MibScalar
bdauthAddr = _BdauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 5),
    _BdauthAddr_Type()
)
bdauthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdauthAddr.setStatus("mandatory")
_BdbootHost_Type = IpAddress
_BdbootHost_Object = MibScalar
bdbootHost = _BdbootHost_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 6),
    _BdbootHost_Type()
)
bdbootHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbootHost.setStatus("mandatory")
_Bdping_Type = Integer32
_Bdping_Object = MibScalar
bdping = _Bdping_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 7),
    _Bdping_Type()
)
bdping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdping.setStatus("obsolete")
_BdfreeMem_Type = Integer32
_BdfreeMem_Object = MibScalar
bdfreeMem = _BdfreeMem_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 8),
    _BdfreeMem_Type()
)
bdfreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdfreeMem.setStatus("obsolete")
_BdbufferElFree_Type = Integer32
_BdbufferElFree_Object = MibScalar
bdbufferElFree = _BdbufferElFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 9),
    _BdbufferElFree_Type()
)
bdbufferElFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferElFree.setStatus("mandatory")
_BdbufferElMax_Type = Integer32
_BdbufferElMax_Object = MibScalar
bdbufferElMax = _BdbufferElMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 10),
    _BdbufferElMax_Type()
)
bdbufferElMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferElMax.setStatus("mandatory")
_BdbufferElHit_Type = Integer32
_BdbufferElHit_Object = MibScalar
bdbufferElHit = _BdbufferElHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 11),
    _BdbufferElHit_Type()
)
bdbufferElHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferElHit.setStatus("mandatory")
_BdbufferElMiss_Type = Integer32
_BdbufferElMiss_Object = MibScalar
bdbufferElMiss = _BdbufferElMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 12),
    _BdbufferElMiss_Type()
)
bdbufferElMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferElMiss.setStatus("mandatory")
_BdbufferElCreate_Type = Integer32
_BdbufferElCreate_Object = MibScalar
bdbufferElCreate = _BdbufferElCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 13),
    _BdbufferElCreate_Type()
)
bdbufferElCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferElCreate.setStatus("mandatory")
_BdbufferSmSize_Type = Integer32
_BdbufferSmSize_Object = MibScalar
bdbufferSmSize = _BdbufferSmSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 14),
    _BdbufferSmSize_Type()
)
bdbufferSmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmSize.setStatus("mandatory")
_BdbufferSmTotal_Type = Integer32
_BdbufferSmTotal_Object = MibScalar
bdbufferSmTotal = _BdbufferSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 15),
    _BdbufferSmTotal_Type()
)
bdbufferSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmTotal.setStatus("mandatory")
_BdbufferSmFree_Type = Integer32
_BdbufferSmFree_Object = MibScalar
bdbufferSmFree = _BdbufferSmFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 16),
    _BdbufferSmFree_Type()
)
bdbufferSmFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmFree.setStatus("mandatory")
_BdbufferSmMax_Type = Integer32
_BdbufferSmMax_Object = MibScalar
bdbufferSmMax = _BdbufferSmMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 17),
    _BdbufferSmMax_Type()
)
bdbufferSmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmMax.setStatus("mandatory")
_BdbufferSmHit_Type = Integer32
_BdbufferSmHit_Object = MibScalar
bdbufferSmHit = _BdbufferSmHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 18),
    _BdbufferSmHit_Type()
)
bdbufferSmHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmHit.setStatus("mandatory")
_BdbufferSmMiss_Type = Integer32
_BdbufferSmMiss_Object = MibScalar
bdbufferSmMiss = _BdbufferSmMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 19),
    _BdbufferSmMiss_Type()
)
bdbufferSmMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmMiss.setStatus("mandatory")
_BdbufferSmTrim_Type = Integer32
_BdbufferSmTrim_Object = MibScalar
bdbufferSmTrim = _BdbufferSmTrim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 20),
    _BdbufferSmTrim_Type()
)
bdbufferSmTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmTrim.setStatus("mandatory")
_BdbufferSmCreate_Type = Integer32
_BdbufferSmCreate_Object = MibScalar
bdbufferSmCreate = _BdbufferSmCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 21),
    _BdbufferSmCreate_Type()
)
bdbufferSmCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferSmCreate.setStatus("mandatory")
_BdbufferMdSize_Type = Integer32
_BdbufferMdSize_Object = MibScalar
bdbufferMdSize = _BdbufferMdSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 22),
    _BdbufferMdSize_Type()
)
bdbufferMdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdSize.setStatus("mandatory")
_BdbufferMdTotal_Type = Integer32
_BdbufferMdTotal_Object = MibScalar
bdbufferMdTotal = _BdbufferMdTotal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 23),
    _BdbufferMdTotal_Type()
)
bdbufferMdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdTotal.setStatus("mandatory")
_BdbufferMdFree_Type = Integer32
_BdbufferMdFree_Object = MibScalar
bdbufferMdFree = _BdbufferMdFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 24),
    _BdbufferMdFree_Type()
)
bdbufferMdFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdFree.setStatus("mandatory")
_BdbufferMdMax_Type = Integer32
_BdbufferMdMax_Object = MibScalar
bdbufferMdMax = _BdbufferMdMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 25),
    _BdbufferMdMax_Type()
)
bdbufferMdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdMax.setStatus("mandatory")
_BdbufferMdHit_Type = Integer32
_BdbufferMdHit_Object = MibScalar
bdbufferMdHit = _BdbufferMdHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 26),
    _BdbufferMdHit_Type()
)
bdbufferMdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdHit.setStatus("mandatory")
_BdbufferMdMiss_Type = Integer32
_BdbufferMdMiss_Object = MibScalar
bdbufferMdMiss = _BdbufferMdMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 27),
    _BdbufferMdMiss_Type()
)
bdbufferMdMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdMiss.setStatus("mandatory")
_BdbufferMdTrim_Type = Integer32
_BdbufferMdTrim_Object = MibScalar
bdbufferMdTrim = _BdbufferMdTrim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 28),
    _BdbufferMdTrim_Type()
)
bdbufferMdTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdTrim.setStatus("mandatory")
_BdbufferMdCreate_Type = Integer32
_BdbufferMdCreate_Object = MibScalar
bdbufferMdCreate = _BdbufferMdCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 29),
    _BdbufferMdCreate_Type()
)
bdbufferMdCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferMdCreate.setStatus("mandatory")
_BdbufferBgSize_Type = Integer32
_BdbufferBgSize_Object = MibScalar
bdbufferBgSize = _BdbufferBgSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 30),
    _BdbufferBgSize_Type()
)
bdbufferBgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgSize.setStatus("mandatory")
_BdbufferBgTotal_Type = Integer32
_BdbufferBgTotal_Object = MibScalar
bdbufferBgTotal = _BdbufferBgTotal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 31),
    _BdbufferBgTotal_Type()
)
bdbufferBgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgTotal.setStatus("mandatory")
_BdbufferBgFree_Type = Integer32
_BdbufferBgFree_Object = MibScalar
bdbufferBgFree = _BdbufferBgFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 32),
    _BdbufferBgFree_Type()
)
bdbufferBgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgFree.setStatus("mandatory")
_BdbufferBgMax_Type = Integer32
_BdbufferBgMax_Object = MibScalar
bdbufferBgMax = _BdbufferBgMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 33),
    _BdbufferBgMax_Type()
)
bdbufferBgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgMax.setStatus("mandatory")
_BdbufferBgHit_Type = Integer32
_BdbufferBgHit_Object = MibScalar
bdbufferBgHit = _BdbufferBgHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 34),
    _BdbufferBgHit_Type()
)
bdbufferBgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgHit.setStatus("mandatory")
_BdbufferBgMiss_Type = Integer32
_BdbufferBgMiss_Object = MibScalar
bdbufferBgMiss = _BdbufferBgMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 35),
    _BdbufferBgMiss_Type()
)
bdbufferBgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgMiss.setStatus("mandatory")
_BdbufferBgTrim_Type = Integer32
_BdbufferBgTrim_Object = MibScalar
bdbufferBgTrim = _BdbufferBgTrim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 36),
    _BdbufferBgTrim_Type()
)
bdbufferBgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgTrim.setStatus("mandatory")
_BdbufferBgCreate_Type = Integer32
_BdbufferBgCreate_Object = MibScalar
bdbufferBgCreate = _BdbufferBgCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 37),
    _BdbufferBgCreate_Type()
)
bdbufferBgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferBgCreate.setStatus("mandatory")
_BdbufferLgSize_Type = Integer32
_BdbufferLgSize_Object = MibScalar
bdbufferLgSize = _BdbufferLgSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 38),
    _BdbufferLgSize_Type()
)
bdbufferLgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgSize.setStatus("mandatory")
_BdbufferLgTotal_Type = Integer32
_BdbufferLgTotal_Object = MibScalar
bdbufferLgTotal = _BdbufferLgTotal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 39),
    _BdbufferLgTotal_Type()
)
bdbufferLgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgTotal.setStatus("mandatory")
_BdbufferLgFree_Type = Integer32
_BdbufferLgFree_Object = MibScalar
bdbufferLgFree = _BdbufferLgFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 40),
    _BdbufferLgFree_Type()
)
bdbufferLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgFree.setStatus("mandatory")
_BdbufferLgMax_Type = Integer32
_BdbufferLgMax_Object = MibScalar
bdbufferLgMax = _BdbufferLgMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 41),
    _BdbufferLgMax_Type()
)
bdbufferLgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgMax.setStatus("mandatory")
_BdbufferLgHit_Type = Integer32
_BdbufferLgHit_Object = MibScalar
bdbufferLgHit = _BdbufferLgHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 42),
    _BdbufferLgHit_Type()
)
bdbufferLgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgHit.setStatus("mandatory")
_BdbufferLgMiss_Type = Integer32
_BdbufferLgMiss_Object = MibScalar
bdbufferLgMiss = _BdbufferLgMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 43),
    _BdbufferLgMiss_Type()
)
bdbufferLgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgMiss.setStatus("mandatory")
_BdbufferLgTrim_Type = Integer32
_BdbufferLgTrim_Object = MibScalar
bdbufferLgTrim = _BdbufferLgTrim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 44),
    _BdbufferLgTrim_Type()
)
bdbufferLgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgTrim.setStatus("mandatory")
_BdbufferLgCreate_Type = Integer32
_BdbufferLgCreate_Object = MibScalar
bdbufferLgCreate = _BdbufferLgCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 45),
    _BdbufferLgCreate_Type()
)
bdbufferLgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferLgCreate.setStatus("mandatory")
_BdbufferFail_Type = Integer32
_BdbufferFail_Object = MibScalar
bdbufferFail = _BdbufferFail_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 46),
    _BdbufferFail_Type()
)
bdbufferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferFail.setStatus("mandatory")
_BdbufferNoMem_Type = Integer32
_BdbufferNoMem_Object = MibScalar
bdbufferNoMem = _BdbufferNoMem_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 47),
    _BdbufferNoMem_Type()
)
bdbufferNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferNoMem.setStatus("mandatory")
_BdnetConfigAddr_Type = IpAddress
_BdnetConfigAddr_Object = MibScalar
bdnetConfigAddr = _BdnetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 48),
    _BdnetConfigAddr_Type()
)
bdnetConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdnetConfigAddr.setStatus("mandatory")
_BdnetConfigName_Type = DisplayString
_BdnetConfigName_Object = MibScalar
bdnetConfigName = _BdnetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 49),
    _BdnetConfigName_Type()
)
bdnetConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdnetConfigName.setStatus("mandatory")
_BdnetConfigSet_Type = DisplayString
_BdnetConfigSet_Object = MibScalar
bdnetConfigSet = _BdnetConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 50),
    _BdnetConfigSet_Type()
)
bdnetConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdnetConfigSet.setStatus("mandatory")
_BdhostConfigAddr_Type = IpAddress
_BdhostConfigAddr_Object = MibScalar
bdhostConfigAddr = _BdhostConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 51),
    _BdhostConfigAddr_Type()
)
bdhostConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdhostConfigAddr.setStatus("obsolete")
_BdhostConfigName_Type = DisplayString
_BdhostConfigName_Object = MibScalar
bdhostConfigName = _BdhostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 52),
    _BdhostConfigName_Type()
)
bdhostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdhostConfigName.setStatus("obsolete")
_BdhostConfigSet_Type = DisplayString
_BdhostConfigSet_Object = MibScalar
bdhostConfigSet = _BdhostConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 53),
    _BdhostConfigSet_Type()
)
bdhostConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdhostConfigSet.setStatus("obsolete")
_BdwriteMem_Type = Integer32
_BdwriteMem_Object = MibScalar
bdwriteMem = _BdwriteMem_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 54),
    _BdwriteMem_Type()
)
bdwriteMem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdwriteMem.setStatus("mandatory")
_BdwriteNet_Type = DisplayString
_BdwriteNet_Object = MibScalar
bdwriteNet = _BdwriteNet_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 55),
    _BdwriteNet_Type()
)
bdwriteNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdwriteNet.setStatus("mandatory")
_BdbusyPer_Type = Integer32
_BdbusyPer_Object = MibScalar
bdbusyPer = _BdbusyPer_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 56),
    _BdbusyPer_Type()
)
bdbusyPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbusyPer.setStatus("mandatory")
_BdavgBusy1_Type = Integer32
_BdavgBusy1_Object = MibScalar
bdavgBusy1 = _BdavgBusy1_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 57),
    _BdavgBusy1_Type()
)
bdavgBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdavgBusy1.setStatus("mandatory")
_BdavgBusy5_Type = Integer32
_BdavgBusy5_Object = MibScalar
bdavgBusy5 = _BdavgBusy5_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 58),
    _BdavgBusy5_Type()
)
bdavgBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdavgBusy5.setStatus("mandatory")
_BdidleCount_Type = Integer32
_BdidleCount_Object = MibScalar
bdidleCount = _BdidleCount_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 59),
    _BdidleCount_Type()
)
bdidleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdidleCount.setStatus("mandatory")
_BdidleWired_Type = Integer32
_BdidleWired_Object = MibScalar
bdidleWired = _BdidleWired_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 60),
    _BdidleWired_Type()
)
bdidleWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bdidleWired.setStatus("mandatory")
_BdContactInfo_Type = DisplayString
_BdContactInfo_Object = MibScalar
bdContactInfo = _BdContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 61),
    _BdContactInfo_Type()
)
bdContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdContactInfo.setStatus("mandatory")
_BdbufferHgSize_Type = Integer32
_BdbufferHgSize_Object = MibScalar
bdbufferHgSize = _BdbufferHgSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 62),
    _BdbufferHgSize_Type()
)
bdbufferHgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgSize.setStatus("mandatory")
_BdbufferHgTotal_Type = Integer32
_BdbufferHgTotal_Object = MibScalar
bdbufferHgTotal = _BdbufferHgTotal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 63),
    _BdbufferHgTotal_Type()
)
bdbufferHgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgTotal.setStatus("mandatory")
_BdbufferHgFree_Type = Integer32
_BdbufferHgFree_Object = MibScalar
bdbufferHgFree = _BdbufferHgFree_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 64),
    _BdbufferHgFree_Type()
)
bdbufferHgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgFree.setStatus("mandatory")
_BdbufferHgMax_Type = Integer32
_BdbufferHgMax_Object = MibScalar
bdbufferHgMax = _BdbufferHgMax_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 65),
    _BdbufferHgMax_Type()
)
bdbufferHgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgMax.setStatus("mandatory")
_BdbufferHgHit_Type = Integer32
_BdbufferHgHit_Object = MibScalar
bdbufferHgHit = _BdbufferHgHit_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 66),
    _BdbufferHgHit_Type()
)
bdbufferHgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgHit.setStatus("mandatory")
_BdbufferHgMiss_Type = Integer32
_BdbufferHgMiss_Object = MibScalar
bdbufferHgMiss = _BdbufferHgMiss_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 67),
    _BdbufferHgMiss_Type()
)
bdbufferHgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgMiss.setStatus("mandatory")
_BdbufferHgTrim_Type = Integer32
_BdbufferHgTrim_Object = MibScalar
bdbufferHgTrim = _BdbufferHgTrim_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 68),
    _BdbufferHgTrim_Type()
)
bdbufferHgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgTrim.setStatus("mandatory")
_BdbufferHgCreate_Type = Integer32
_BdbufferHgCreate_Object = MibScalar
bdbufferHgCreate = _BdbufferHgCreate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 69),
    _BdbufferHgCreate_Type()
)
bdbufferHgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdbufferHgCreate.setStatus("mandatory")
_BdnetConfigProto_Type = Integer32
_BdnetConfigProto_Object = MibScalar
bdnetConfigProto = _BdnetConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 70),
    _BdnetConfigProto_Type()
)
bdnetConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdnetConfigProto.setStatus("mandatory")
_BdhostConfigProto_Type = Integer32
_BdhostConfigProto_Object = MibScalar
bdhostConfigProto = _BdhostConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 71),
    _BdhostConfigProto_Type()
)
bdhostConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdhostConfigProto.setStatus("mandatory")
_BdsysConfigAddr_Type = IpAddress
_BdsysConfigAddr_Object = MibScalar
bdsysConfigAddr = _BdsysConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 72),
    _BdsysConfigAddr_Type()
)
bdsysConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdsysConfigAddr.setStatus("mandatory")
_BdsysConfigName_Type = DisplayString
_BdsysConfigName_Object = MibScalar
bdsysConfigName = _BdsysConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 73),
    _BdsysConfigName_Type()
)
bdsysConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdsysConfigName.setStatus("mandatory")
_BdsysConfigProto_Type = Integer32
_BdsysConfigProto_Object = MibScalar
bdsysConfigProto = _BdsysConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 74),
    _BdsysConfigProto_Type()
)
bdsysConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdsysConfigProto.setStatus("mandatory")
_BdsysClearARP_Type = Integer32
_BdsysClearARP_Object = MibScalar
bdsysClearARP = _BdsysClearARP_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 75),
    _BdsysClearARP_Type()
)
bdsysClearARP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdsysClearARP.setStatus("mandatory")
_BdsysClearInt_Type = Integer32
_BdsysClearInt_Object = MibScalar
bdsysClearInt = _BdsysClearInt_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 76),
    _BdsysClearInt_Type()
)
bdsysClearInt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    bdsysClearInt.setStatus("mandatory")
_BdenvPresent_Type = Integer32
_BdenvPresent_Object = MibScalar
bdenvPresent = _BdenvPresent_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 77),
    _BdenvPresent_Type()
)
bdenvPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvPresent.setStatus("mandatory")
_BdenvTestPt1Descr_Type = DisplayString
_BdenvTestPt1Descr_Object = MibScalar
bdenvTestPt1Descr = _BdenvTestPt1Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 78),
    _BdenvTestPt1Descr_Type()
)
bdenvTestPt1Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt1Descr.setStatus("mandatory")
_BdenvTestPt1Measure_Type = Integer32
_BdenvTestPt1Measure_Object = MibScalar
bdenvTestPt1Measure = _BdenvTestPt1Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 79),
    _BdenvTestPt1Measure_Type()
)
bdenvTestPt1Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt1Measure.setStatus("mandatory")
_BdenvTestPt2Descr_Type = DisplayString
_BdenvTestPt2Descr_Object = MibScalar
bdenvTestPt2Descr = _BdenvTestPt2Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 80),
    _BdenvTestPt2Descr_Type()
)
bdenvTestPt2Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt2Descr.setStatus("mandatory")
_BdenvTestPt2Measure_Type = Integer32
_BdenvTestPt2Measure_Object = MibScalar
bdenvTestPt2Measure = _BdenvTestPt2Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 81),
    _BdenvTestPt2Measure_Type()
)
bdenvTestPt2Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt2Measure.setStatus("mandatory")
_BdenvTestPt3Descr_Type = DisplayString
_BdenvTestPt3Descr_Object = MibScalar
bdenvTestPt3Descr = _BdenvTestPt3Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 82),
    _BdenvTestPt3Descr_Type()
)
bdenvTestPt3Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt3Descr.setStatus("mandatory")
_BdenvTestPt3Measure_Type = Integer32
_BdenvTestPt3Measure_Object = MibScalar
bdenvTestPt3Measure = _BdenvTestPt3Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 83),
    _BdenvTestPt3Measure_Type()
)
bdenvTestPt3Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt3Measure.setStatus("mandatory")
_BdenvTestPt4Descr_Type = DisplayString
_BdenvTestPt4Descr_Object = MibScalar
bdenvTestPt4Descr = _BdenvTestPt4Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 84),
    _BdenvTestPt4Descr_Type()
)
bdenvTestPt4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt4Descr.setStatus("mandatory")
_BdenvTestPt4Measure_Type = Integer32
_BdenvTestPt4Measure_Object = MibScalar
bdenvTestPt4Measure = _BdenvTestPt4Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 85),
    _BdenvTestPt4Measure_Type()
)
bdenvTestPt4Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt4Measure.setStatus("mandatory")
_BdenvTestPt5Descr_Type = DisplayString
_BdenvTestPt5Descr_Object = MibScalar
bdenvTestPt5Descr = _BdenvTestPt5Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 86),
    _BdenvTestPt5Descr_Type()
)
bdenvTestPt5Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt5Descr.setStatus("mandatory")
_BdenvTestPt5Measure_Type = Integer32
_BdenvTestPt5Measure_Object = MibScalar
bdenvTestPt5Measure = _BdenvTestPt5Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 87),
    _BdenvTestPt5Measure_Type()
)
bdenvTestPt5Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt5Measure.setStatus("mandatory")
_BdenvTestPt6Descr_Type = DisplayString
_BdenvTestPt6Descr_Object = MibScalar
bdenvTestPt6Descr = _BdenvTestPt6Descr_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 88),
    _BdenvTestPt6Descr_Type()
)
bdenvTestPt6Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt6Descr.setStatus("mandatory")
_BdenvTestPt6Measure_Type = Integer32
_BdenvTestPt6Measure_Object = MibScalar
bdenvTestPt6Measure = _BdenvTestPt6Measure_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 89),
    _BdenvTestPt6Measure_Type()
)
bdenvTestPt6Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt6Measure.setStatus("mandatory")
_BdenvTestPt1MarginVal_Type = Integer32
_BdenvTestPt1MarginVal_Object = MibScalar
bdenvTestPt1MarginVal = _BdenvTestPt1MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 90),
    _BdenvTestPt1MarginVal_Type()
)
bdenvTestPt1MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt1MarginVal.setStatus("mandatory")
_BdenvTestPt2MarginVal_Type = Integer32
_BdenvTestPt2MarginVal_Object = MibScalar
bdenvTestPt2MarginVal = _BdenvTestPt2MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 91),
    _BdenvTestPt2MarginVal_Type()
)
bdenvTestPt2MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt2MarginVal.setStatus("mandatory")
_BdenvTestPt3MarginPercent_Type = Integer32
_BdenvTestPt3MarginPercent_Object = MibScalar
bdenvTestPt3MarginPercent = _BdenvTestPt3MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 92),
    _BdenvTestPt3MarginPercent_Type()
)
bdenvTestPt3MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt3MarginPercent.setStatus("mandatory")
_BdenvTestPt4MarginPercent_Type = Integer32
_BdenvTestPt4MarginPercent_Object = MibScalar
bdenvTestPt4MarginPercent = _BdenvTestPt4MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 93),
    _BdenvTestPt4MarginPercent_Type()
)
bdenvTestPt4MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt4MarginPercent.setStatus("mandatory")
_BdenvTestPt5MarginPercent_Type = Integer32
_BdenvTestPt5MarginPercent_Object = MibScalar
bdenvTestPt5MarginPercent = _BdenvTestPt5MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 94),
    _BdenvTestPt5MarginPercent_Type()
)
bdenvTestPt5MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt5MarginPercent.setStatus("mandatory")
_BdenvTestPt6MarginPercent_Type = Integer32
_BdenvTestPt6MarginPercent_Object = MibScalar
bdenvTestPt6MarginPercent = _BdenvTestPt6MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 95),
    _BdenvTestPt6MarginPercent_Type()
)
bdenvTestPt6MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt6MarginPercent.setStatus("mandatory")
_BdenvTestPt1last_Type = Integer32
_BdenvTestPt1last_Object = MibScalar
bdenvTestPt1last = _BdenvTestPt1last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 96),
    _BdenvTestPt1last_Type()
)
bdenvTestPt1last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt1last.setStatus("mandatory")
_BdenvTestPt2last_Type = Integer32
_BdenvTestPt2last_Object = MibScalar
bdenvTestPt2last = _BdenvTestPt2last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 97),
    _BdenvTestPt2last_Type()
)
bdenvTestPt2last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt2last.setStatus("mandatory")
_BdenvTestPt3last_Type = Integer32
_BdenvTestPt3last_Object = MibScalar
bdenvTestPt3last = _BdenvTestPt3last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 98),
    _BdenvTestPt3last_Type()
)
bdenvTestPt3last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt3last.setStatus("mandatory")
_BdenvTestPt4last_Type = Integer32
_BdenvTestPt4last_Object = MibScalar
bdenvTestPt4last = _BdenvTestPt4last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 99),
    _BdenvTestPt4last_Type()
)
bdenvTestPt4last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt4last.setStatus("mandatory")
_BdenvTestPt5last_Type = Integer32
_BdenvTestPt5last_Object = MibScalar
bdenvTestPt5last = _BdenvTestPt5last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 100),
    _BdenvTestPt5last_Type()
)
bdenvTestPt5last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt5last.setStatus("mandatory")
_BdenvTestPt6last_Type = Integer32
_BdenvTestPt6last_Object = MibScalar
bdenvTestPt6last = _BdenvTestPt6last_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 101),
    _BdenvTestPt6last_Type()
)
bdenvTestPt6last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt6last.setStatus("mandatory")


class _BdenvTestPt1warn_Type(Integer32):
    """Custom type bdenvTestPt1warn based on Integer32"""
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


_BdenvTestPt1warn_Type.__name__ = "Integer32"
_BdenvTestPt1warn_Object = MibScalar
bdenvTestPt1warn = _BdenvTestPt1warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 102),
    _BdenvTestPt1warn_Type()
)
bdenvTestPt1warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt1warn.setStatus("mandatory")


class _BdenvTestPt2warn_Type(Integer32):
    """Custom type bdenvTestPt2warn based on Integer32"""
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


_BdenvTestPt2warn_Type.__name__ = "Integer32"
_BdenvTestPt2warn_Object = MibScalar
bdenvTestPt2warn = _BdenvTestPt2warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 103),
    _BdenvTestPt2warn_Type()
)
bdenvTestPt2warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt2warn.setStatus("mandatory")


class _BdenvTestPt3warn_Type(Integer32):
    """Custom type bdenvTestPt3warn based on Integer32"""
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


_BdenvTestPt3warn_Type.__name__ = "Integer32"
_BdenvTestPt3warn_Object = MibScalar
bdenvTestPt3warn = _BdenvTestPt3warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 104),
    _BdenvTestPt3warn_Type()
)
bdenvTestPt3warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt3warn.setStatus("mandatory")


class _BdenvTestPt4warn_Type(Integer32):
    """Custom type bdenvTestPt4warn based on Integer32"""
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


_BdenvTestPt4warn_Type.__name__ = "Integer32"
_BdenvTestPt4warn_Object = MibScalar
bdenvTestPt4warn = _BdenvTestPt4warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 105),
    _BdenvTestPt4warn_Type()
)
bdenvTestPt4warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt4warn.setStatus("mandatory")


class _BdenvTestPt5warn_Type(Integer32):
    """Custom type bdenvTestPt5warn based on Integer32"""
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


_BdenvTestPt5warn_Type.__name__ = "Integer32"
_BdenvTestPt5warn_Object = MibScalar
bdenvTestPt5warn = _BdenvTestPt5warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 106),
    _BdenvTestPt5warn_Type()
)
bdenvTestPt5warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt5warn.setStatus("mandatory")


class _BdenvTestPt6warn_Type(Integer32):
    """Custom type bdenvTestPt6warn based on Integer32"""
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


_BdenvTestPt6warn_Type.__name__ = "Integer32"
_BdenvTestPt6warn_Object = MibScalar
bdenvTestPt6warn = _BdenvTestPt6warn_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 107),
    _BdenvTestPt6warn_Type()
)
bdenvTestPt6warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTestPt6warn.setStatus("mandatory")
_BdenvFirmVersion_Type = DisplayString
_BdenvFirmVersion_Object = MibScalar
bdenvFirmVersion = _BdenvFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 108),
    _BdenvFirmVersion_Type()
)
bdenvFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvFirmVersion.setStatus("mandatory")
_BdenvTechnicianID_Type = DisplayString
_BdenvTechnicianID_Object = MibScalar
bdenvTechnicianID = _BdenvTechnicianID_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 109),
    _BdenvTechnicianID_Type()
)
bdenvTechnicianID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvTechnicianID.setStatus("mandatory")
_BdenvType_Type = DisplayString
_BdenvType_Object = MibScalar
bdenvType = _BdenvType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 110),
    _BdenvType_Type()
)
bdenvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvType.setStatus("mandatory")
_BdenvBurnDate_Type = DisplayString
_BdenvBurnDate_Object = MibScalar
bdenvBurnDate = _BdenvBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 111),
    _BdenvBurnDate_Type()
)
bdenvBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvBurnDate.setStatus("mandatory")
_BdenvSerialNumber_Type = DisplayString
_BdenvSerialNumber_Object = MibScalar
bdenvSerialNumber = _BdenvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3320, 2, 1, 112),
    _BdenvSerialNumber_Type()
)
bdenvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bdenvSerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BDCOM-SYS",
    **{"bdlsystem": bdlsystem,
       "bdromId": bdromId,
       "bdwhyReload": bdwhyReload,
       "bdhostName": bdhostName,
       "bddomainName": bddomainName,
       "bdauthAddr": bdauthAddr,
       "bdbootHost": bdbootHost,
       "bdping": bdping,
       "bdfreeMem": bdfreeMem,
       "bdbufferElFree": bdbufferElFree,
       "bdbufferElMax": bdbufferElMax,
       "bdbufferElHit": bdbufferElHit,
       "bdbufferElMiss": bdbufferElMiss,
       "bdbufferElCreate": bdbufferElCreate,
       "bdbufferSmSize": bdbufferSmSize,
       "bdbufferSmTotal": bdbufferSmTotal,
       "bdbufferSmFree": bdbufferSmFree,
       "bdbufferSmMax": bdbufferSmMax,
       "bdbufferSmHit": bdbufferSmHit,
       "bdbufferSmMiss": bdbufferSmMiss,
       "bdbufferSmTrim": bdbufferSmTrim,
       "bdbufferSmCreate": bdbufferSmCreate,
       "bdbufferMdSize": bdbufferMdSize,
       "bdbufferMdTotal": bdbufferMdTotal,
       "bdbufferMdFree": bdbufferMdFree,
       "bdbufferMdMax": bdbufferMdMax,
       "bdbufferMdHit": bdbufferMdHit,
       "bdbufferMdMiss": bdbufferMdMiss,
       "bdbufferMdTrim": bdbufferMdTrim,
       "bdbufferMdCreate": bdbufferMdCreate,
       "bdbufferBgSize": bdbufferBgSize,
       "bdbufferBgTotal": bdbufferBgTotal,
       "bdbufferBgFree": bdbufferBgFree,
       "bdbufferBgMax": bdbufferBgMax,
       "bdbufferBgHit": bdbufferBgHit,
       "bdbufferBgMiss": bdbufferBgMiss,
       "bdbufferBgTrim": bdbufferBgTrim,
       "bdbufferBgCreate": bdbufferBgCreate,
       "bdbufferLgSize": bdbufferLgSize,
       "bdbufferLgTotal": bdbufferLgTotal,
       "bdbufferLgFree": bdbufferLgFree,
       "bdbufferLgMax": bdbufferLgMax,
       "bdbufferLgHit": bdbufferLgHit,
       "bdbufferLgMiss": bdbufferLgMiss,
       "bdbufferLgTrim": bdbufferLgTrim,
       "bdbufferLgCreate": bdbufferLgCreate,
       "bdbufferFail": bdbufferFail,
       "bdbufferNoMem": bdbufferNoMem,
       "bdnetConfigAddr": bdnetConfigAddr,
       "bdnetConfigName": bdnetConfigName,
       "bdnetConfigSet": bdnetConfigSet,
       "bdhostConfigAddr": bdhostConfigAddr,
       "bdhostConfigName": bdhostConfigName,
       "bdhostConfigSet": bdhostConfigSet,
       "bdwriteMem": bdwriteMem,
       "bdwriteNet": bdwriteNet,
       "bdbusyPer": bdbusyPer,
       "bdavgBusy1": bdavgBusy1,
       "bdavgBusy5": bdavgBusy5,
       "bdidleCount": bdidleCount,
       "bdidleWired": bdidleWired,
       "bdContactInfo": bdContactInfo,
       "bdbufferHgSize": bdbufferHgSize,
       "bdbufferHgTotal": bdbufferHgTotal,
       "bdbufferHgFree": bdbufferHgFree,
       "bdbufferHgMax": bdbufferHgMax,
       "bdbufferHgHit": bdbufferHgHit,
       "bdbufferHgMiss": bdbufferHgMiss,
       "bdbufferHgTrim": bdbufferHgTrim,
       "bdbufferHgCreate": bdbufferHgCreate,
       "bdnetConfigProto": bdnetConfigProto,
       "bdhostConfigProto": bdhostConfigProto,
       "bdsysConfigAddr": bdsysConfigAddr,
       "bdsysConfigName": bdsysConfigName,
       "bdsysConfigProto": bdsysConfigProto,
       "bdsysClearARP": bdsysClearARP,
       "bdsysClearInt": bdsysClearInt,
       "bdenvPresent": bdenvPresent,
       "bdenvTestPt1Descr": bdenvTestPt1Descr,
       "bdenvTestPt1Measure": bdenvTestPt1Measure,
       "bdenvTestPt2Descr": bdenvTestPt2Descr,
       "bdenvTestPt2Measure": bdenvTestPt2Measure,
       "bdenvTestPt3Descr": bdenvTestPt3Descr,
       "bdenvTestPt3Measure": bdenvTestPt3Measure,
       "bdenvTestPt4Descr": bdenvTestPt4Descr,
       "bdenvTestPt4Measure": bdenvTestPt4Measure,
       "bdenvTestPt5Descr": bdenvTestPt5Descr,
       "bdenvTestPt5Measure": bdenvTestPt5Measure,
       "bdenvTestPt6Descr": bdenvTestPt6Descr,
       "bdenvTestPt6Measure": bdenvTestPt6Measure,
       "bdenvTestPt1MarginVal": bdenvTestPt1MarginVal,
       "bdenvTestPt2MarginVal": bdenvTestPt2MarginVal,
       "bdenvTestPt3MarginPercent": bdenvTestPt3MarginPercent,
       "bdenvTestPt4MarginPercent": bdenvTestPt4MarginPercent,
       "bdenvTestPt5MarginPercent": bdenvTestPt5MarginPercent,
       "bdenvTestPt6MarginPercent": bdenvTestPt6MarginPercent,
       "bdenvTestPt1last": bdenvTestPt1last,
       "bdenvTestPt2last": bdenvTestPt2last,
       "bdenvTestPt3last": bdenvTestPt3last,
       "bdenvTestPt4last": bdenvTestPt4last,
       "bdenvTestPt5last": bdenvTestPt5last,
       "bdenvTestPt6last": bdenvTestPt6last,
       "bdenvTestPt1warn": bdenvTestPt1warn,
       "bdenvTestPt2warn": bdenvTestPt2warn,
       "bdenvTestPt3warn": bdenvTestPt3warn,
       "bdenvTestPt4warn": bdenvTestPt4warn,
       "bdenvTestPt5warn": bdenvTestPt5warn,
       "bdenvTestPt6warn": bdenvTestPt6warn,
       "bdenvFirmVersion": bdenvFirmVersion,
       "bdenvTechnicianID": bdenvTechnicianID,
       "bdenvType": bdenvType,
       "bdenvBurnDate": bdenvBurnDate,
       "bdenvSerialNumber": bdenvSerialNumber}
)
