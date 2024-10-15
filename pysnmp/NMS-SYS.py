# SNMP MIB module (NMS-SYS) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-SYS
# Produced by pysmi-1.5.4 at Mon Oct 14 22:28:05 2024
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

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

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

_Nmslsystem_ObjectIdentity = ObjectIdentity
nmslsystem = _Nmslsystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1)
)
_NmsromId_Type = DisplayString
_NmsromId_Object = MibScalar
nmsromId = _NmsromId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 1),
    _NmsromId_Type()
)
nmsromId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsromId.setStatus("mandatory")
_NmswhyReload_Type = DisplayString
_NmswhyReload_Object = MibScalar
nmswhyReload = _NmswhyReload_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 2),
    _NmswhyReload_Type()
)
nmswhyReload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmswhyReload.setStatus("mandatory")
_NmshostName_Type = DisplayString
_NmshostName_Object = MibScalar
nmshostName = _NmshostName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 3),
    _NmshostName_Type()
)
nmshostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmshostName.setStatus("mandatory")
_NmsdomainName_Type = DisplayString
_NmsdomainName_Object = MibScalar
nmsdomainName = _NmsdomainName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 4),
    _NmsdomainName_Type()
)
nmsdomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsdomainName.setStatus("mandatory")
_NmsauthAddr_Type = IpAddress
_NmsauthAddr_Object = MibScalar
nmsauthAddr = _NmsauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 5),
    _NmsauthAddr_Type()
)
nmsauthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsauthAddr.setStatus("mandatory")
_NmsbootHost_Type = IpAddress
_NmsbootHost_Object = MibScalar
nmsbootHost = _NmsbootHost_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 6),
    _NmsbootHost_Type()
)
nmsbootHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbootHost.setStatus("mandatory")
_Nmsping_Type = Integer32
_Nmsping_Object = MibScalar
nmsping = _Nmsping_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 7),
    _Nmsping_Type()
)
nmsping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsping.setStatus("obsolete")
_NmsfreeMem_Type = Integer32
_NmsfreeMem_Object = MibScalar
nmsfreeMem = _NmsfreeMem_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 8),
    _NmsfreeMem_Type()
)
nmsfreeMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsfreeMem.setStatus("obsolete")
_NmsbufferElFree_Type = Integer32
_NmsbufferElFree_Object = MibScalar
nmsbufferElFree = _NmsbufferElFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 9),
    _NmsbufferElFree_Type()
)
nmsbufferElFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferElFree.setStatus("mandatory")
_NmsbufferElMax_Type = Integer32
_NmsbufferElMax_Object = MibScalar
nmsbufferElMax = _NmsbufferElMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 10),
    _NmsbufferElMax_Type()
)
nmsbufferElMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferElMax.setStatus("mandatory")
_NmsbufferElHit_Type = Integer32
_NmsbufferElHit_Object = MibScalar
nmsbufferElHit = _NmsbufferElHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 11),
    _NmsbufferElHit_Type()
)
nmsbufferElHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferElHit.setStatus("mandatory")
_NmsbufferElMiss_Type = Integer32
_NmsbufferElMiss_Object = MibScalar
nmsbufferElMiss = _NmsbufferElMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 12),
    _NmsbufferElMiss_Type()
)
nmsbufferElMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferElMiss.setStatus("mandatory")
_NmsbufferElCreate_Type = Integer32
_NmsbufferElCreate_Object = MibScalar
nmsbufferElCreate = _NmsbufferElCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 13),
    _NmsbufferElCreate_Type()
)
nmsbufferElCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferElCreate.setStatus("mandatory")
_NmsbufferSmSize_Type = Integer32
_NmsbufferSmSize_Object = MibScalar
nmsbufferSmSize = _NmsbufferSmSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 14),
    _NmsbufferSmSize_Type()
)
nmsbufferSmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmSize.setStatus("mandatory")
_NmsbufferSmTotal_Type = Integer32
_NmsbufferSmTotal_Object = MibScalar
nmsbufferSmTotal = _NmsbufferSmTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 15),
    _NmsbufferSmTotal_Type()
)
nmsbufferSmTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmTotal.setStatus("mandatory")
_NmsbufferSmFree_Type = Integer32
_NmsbufferSmFree_Object = MibScalar
nmsbufferSmFree = _NmsbufferSmFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 16),
    _NmsbufferSmFree_Type()
)
nmsbufferSmFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmFree.setStatus("mandatory")
_NmsbufferSmMax_Type = Integer32
_NmsbufferSmMax_Object = MibScalar
nmsbufferSmMax = _NmsbufferSmMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 17),
    _NmsbufferSmMax_Type()
)
nmsbufferSmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmMax.setStatus("mandatory")
_NmsbufferSmHit_Type = Integer32
_NmsbufferSmHit_Object = MibScalar
nmsbufferSmHit = _NmsbufferSmHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 18),
    _NmsbufferSmHit_Type()
)
nmsbufferSmHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmHit.setStatus("mandatory")
_NmsbufferSmMiss_Type = Integer32
_NmsbufferSmMiss_Object = MibScalar
nmsbufferSmMiss = _NmsbufferSmMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 19),
    _NmsbufferSmMiss_Type()
)
nmsbufferSmMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmMiss.setStatus("mandatory")
_NmsbufferSmTrim_Type = Integer32
_NmsbufferSmTrim_Object = MibScalar
nmsbufferSmTrim = _NmsbufferSmTrim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 20),
    _NmsbufferSmTrim_Type()
)
nmsbufferSmTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmTrim.setStatus("mandatory")
_NmsbufferSmCreate_Type = Integer32
_NmsbufferSmCreate_Object = MibScalar
nmsbufferSmCreate = _NmsbufferSmCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 21),
    _NmsbufferSmCreate_Type()
)
nmsbufferSmCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferSmCreate.setStatus("mandatory")
_NmsbufferMdSize_Type = Integer32
_NmsbufferMdSize_Object = MibScalar
nmsbufferMdSize = _NmsbufferMdSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 22),
    _NmsbufferMdSize_Type()
)
nmsbufferMdSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdSize.setStatus("mandatory")
_NmsbufferMdTotal_Type = Integer32
_NmsbufferMdTotal_Object = MibScalar
nmsbufferMdTotal = _NmsbufferMdTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 23),
    _NmsbufferMdTotal_Type()
)
nmsbufferMdTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdTotal.setStatus("mandatory")
_NmsbufferMdFree_Type = Integer32
_NmsbufferMdFree_Object = MibScalar
nmsbufferMdFree = _NmsbufferMdFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 24),
    _NmsbufferMdFree_Type()
)
nmsbufferMdFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdFree.setStatus("mandatory")
_NmsbufferMdMax_Type = Integer32
_NmsbufferMdMax_Object = MibScalar
nmsbufferMdMax = _NmsbufferMdMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 25),
    _NmsbufferMdMax_Type()
)
nmsbufferMdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdMax.setStatus("mandatory")
_NmsbufferMdHit_Type = Integer32
_NmsbufferMdHit_Object = MibScalar
nmsbufferMdHit = _NmsbufferMdHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 26),
    _NmsbufferMdHit_Type()
)
nmsbufferMdHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdHit.setStatus("mandatory")
_NmsbufferMdMiss_Type = Integer32
_NmsbufferMdMiss_Object = MibScalar
nmsbufferMdMiss = _NmsbufferMdMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 27),
    _NmsbufferMdMiss_Type()
)
nmsbufferMdMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdMiss.setStatus("mandatory")
_NmsbufferMdTrim_Type = Integer32
_NmsbufferMdTrim_Object = MibScalar
nmsbufferMdTrim = _NmsbufferMdTrim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 28),
    _NmsbufferMdTrim_Type()
)
nmsbufferMdTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdTrim.setStatus("mandatory")
_NmsbufferMdCreate_Type = Integer32
_NmsbufferMdCreate_Object = MibScalar
nmsbufferMdCreate = _NmsbufferMdCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 29),
    _NmsbufferMdCreate_Type()
)
nmsbufferMdCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferMdCreate.setStatus("mandatory")
_NmsbufferBgSize_Type = Integer32
_NmsbufferBgSize_Object = MibScalar
nmsbufferBgSize = _NmsbufferBgSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 30),
    _NmsbufferBgSize_Type()
)
nmsbufferBgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgSize.setStatus("mandatory")
_NmsbufferBgTotal_Type = Integer32
_NmsbufferBgTotal_Object = MibScalar
nmsbufferBgTotal = _NmsbufferBgTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 31),
    _NmsbufferBgTotal_Type()
)
nmsbufferBgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgTotal.setStatus("mandatory")
_NmsbufferBgFree_Type = Integer32
_NmsbufferBgFree_Object = MibScalar
nmsbufferBgFree = _NmsbufferBgFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 32),
    _NmsbufferBgFree_Type()
)
nmsbufferBgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgFree.setStatus("mandatory")
_NmsbufferBgMax_Type = Integer32
_NmsbufferBgMax_Object = MibScalar
nmsbufferBgMax = _NmsbufferBgMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 33),
    _NmsbufferBgMax_Type()
)
nmsbufferBgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgMax.setStatus("mandatory")
_NmsbufferBgHit_Type = Integer32
_NmsbufferBgHit_Object = MibScalar
nmsbufferBgHit = _NmsbufferBgHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 34),
    _NmsbufferBgHit_Type()
)
nmsbufferBgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgHit.setStatus("mandatory")
_NmsbufferBgMiss_Type = Integer32
_NmsbufferBgMiss_Object = MibScalar
nmsbufferBgMiss = _NmsbufferBgMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 35),
    _NmsbufferBgMiss_Type()
)
nmsbufferBgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgMiss.setStatus("mandatory")
_NmsbufferBgTrim_Type = Integer32
_NmsbufferBgTrim_Object = MibScalar
nmsbufferBgTrim = _NmsbufferBgTrim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 36),
    _NmsbufferBgTrim_Type()
)
nmsbufferBgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgTrim.setStatus("mandatory")
_NmsbufferBgCreate_Type = Integer32
_NmsbufferBgCreate_Object = MibScalar
nmsbufferBgCreate = _NmsbufferBgCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 37),
    _NmsbufferBgCreate_Type()
)
nmsbufferBgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferBgCreate.setStatus("mandatory")
_NmsbufferLgSize_Type = Integer32
_NmsbufferLgSize_Object = MibScalar
nmsbufferLgSize = _NmsbufferLgSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 38),
    _NmsbufferLgSize_Type()
)
nmsbufferLgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgSize.setStatus("mandatory")
_NmsbufferLgTotal_Type = Integer32
_NmsbufferLgTotal_Object = MibScalar
nmsbufferLgTotal = _NmsbufferLgTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 39),
    _NmsbufferLgTotal_Type()
)
nmsbufferLgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgTotal.setStatus("mandatory")
_NmsbufferLgFree_Type = Integer32
_NmsbufferLgFree_Object = MibScalar
nmsbufferLgFree = _NmsbufferLgFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 40),
    _NmsbufferLgFree_Type()
)
nmsbufferLgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgFree.setStatus("mandatory")
_NmsbufferLgMax_Type = Integer32
_NmsbufferLgMax_Object = MibScalar
nmsbufferLgMax = _NmsbufferLgMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 41),
    _NmsbufferLgMax_Type()
)
nmsbufferLgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgMax.setStatus("mandatory")
_NmsbufferLgHit_Type = Integer32
_NmsbufferLgHit_Object = MibScalar
nmsbufferLgHit = _NmsbufferLgHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 42),
    _NmsbufferLgHit_Type()
)
nmsbufferLgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgHit.setStatus("mandatory")
_NmsbufferLgMiss_Type = Integer32
_NmsbufferLgMiss_Object = MibScalar
nmsbufferLgMiss = _NmsbufferLgMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 43),
    _NmsbufferLgMiss_Type()
)
nmsbufferLgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgMiss.setStatus("mandatory")
_NmsbufferLgTrim_Type = Integer32
_NmsbufferLgTrim_Object = MibScalar
nmsbufferLgTrim = _NmsbufferLgTrim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 44),
    _NmsbufferLgTrim_Type()
)
nmsbufferLgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgTrim.setStatus("mandatory")
_NmsbufferLgCreate_Type = Integer32
_NmsbufferLgCreate_Object = MibScalar
nmsbufferLgCreate = _NmsbufferLgCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 45),
    _NmsbufferLgCreate_Type()
)
nmsbufferLgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferLgCreate.setStatus("mandatory")
_NmsbufferFail_Type = Integer32
_NmsbufferFail_Object = MibScalar
nmsbufferFail = _NmsbufferFail_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 46),
    _NmsbufferFail_Type()
)
nmsbufferFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferFail.setStatus("mandatory")
_NmsbufferNoMem_Type = Integer32
_NmsbufferNoMem_Object = MibScalar
nmsbufferNoMem = _NmsbufferNoMem_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 47),
    _NmsbufferNoMem_Type()
)
nmsbufferNoMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferNoMem.setStatus("mandatory")
_NmsnetConfigAddr_Type = IpAddress
_NmsnetConfigAddr_Object = MibScalar
nmsnetConfigAddr = _NmsnetConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 48),
    _NmsnetConfigAddr_Type()
)
nmsnetConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsnetConfigAddr.setStatus("mandatory")
_NmsnetConfigName_Type = DisplayString
_NmsnetConfigName_Object = MibScalar
nmsnetConfigName = _NmsnetConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 49),
    _NmsnetConfigName_Type()
)
nmsnetConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsnetConfigName.setStatus("mandatory")
_NmsnetConfigSet_Type = DisplayString
_NmsnetConfigSet_Object = MibScalar
nmsnetConfigSet = _NmsnetConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 50),
    _NmsnetConfigSet_Type()
)
nmsnetConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmsnetConfigSet.setStatus("mandatory")
_NmshostConfigAddr_Type = IpAddress
_NmshostConfigAddr_Object = MibScalar
nmshostConfigAddr = _NmshostConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 51),
    _NmshostConfigAddr_Type()
)
nmshostConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmshostConfigAddr.setStatus("obsolete")
_NmshostConfigName_Type = DisplayString
_NmshostConfigName_Object = MibScalar
nmshostConfigName = _NmshostConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 52),
    _NmshostConfigName_Type()
)
nmshostConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmshostConfigName.setStatus("obsolete")
_NmshostConfigSet_Type = DisplayString
_NmshostConfigSet_Object = MibScalar
nmshostConfigSet = _NmshostConfigSet_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 53),
    _NmshostConfigSet_Type()
)
nmshostConfigSet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmshostConfigSet.setStatus("obsolete")
_NmswriteMem_Type = Integer32
_NmswriteMem_Object = MibScalar
nmswriteMem = _NmswriteMem_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 54),
    _NmswriteMem_Type()
)
nmswriteMem.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmswriteMem.setStatus("mandatory")
_NmswriteNet_Type = DisplayString
_NmswriteNet_Object = MibScalar
nmswriteNet = _NmswriteNet_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 55),
    _NmswriteNet_Type()
)
nmswriteNet.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmswriteNet.setStatus("mandatory")
_NmsbusyPer_Type = Integer32
_NmsbusyPer_Object = MibScalar
nmsbusyPer = _NmsbusyPer_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 56),
    _NmsbusyPer_Type()
)
nmsbusyPer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbusyPer.setStatus("mandatory")
_NmsavgBusy1_Type = Integer32
_NmsavgBusy1_Object = MibScalar
nmsavgBusy1 = _NmsavgBusy1_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 57),
    _NmsavgBusy1_Type()
)
nmsavgBusy1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsavgBusy1.setStatus("mandatory")
_NmsavgBusy5_Type = Integer32
_NmsavgBusy5_Object = MibScalar
nmsavgBusy5 = _NmsavgBusy5_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 58),
    _NmsavgBusy5_Type()
)
nmsavgBusy5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsavgBusy5.setStatus("mandatory")
_NmsidleCount_Type = Integer32
_NmsidleCount_Object = MibScalar
nmsidleCount = _NmsidleCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 59),
    _NmsidleCount_Type()
)
nmsidleCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsidleCount.setStatus("mandatory")
_NmsidleWired_Type = Integer32
_NmsidleWired_Object = MibScalar
nmsidleWired = _NmsidleWired_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 60),
    _NmsidleWired_Type()
)
nmsidleWired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nmsidleWired.setStatus("mandatory")
_NmsContactInfo_Type = DisplayString
_NmsContactInfo_Object = MibScalar
nmsContactInfo = _NmsContactInfo_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 61),
    _NmsContactInfo_Type()
)
nmsContactInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsContactInfo.setStatus("mandatory")
_NmsbufferHgSize_Type = Integer32
_NmsbufferHgSize_Object = MibScalar
nmsbufferHgSize = _NmsbufferHgSize_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 62),
    _NmsbufferHgSize_Type()
)
nmsbufferHgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgSize.setStatus("mandatory")
_NmsbufferHgTotal_Type = Integer32
_NmsbufferHgTotal_Object = MibScalar
nmsbufferHgTotal = _NmsbufferHgTotal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 63),
    _NmsbufferHgTotal_Type()
)
nmsbufferHgTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgTotal.setStatus("mandatory")
_NmsbufferHgFree_Type = Integer32
_NmsbufferHgFree_Object = MibScalar
nmsbufferHgFree = _NmsbufferHgFree_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 64),
    _NmsbufferHgFree_Type()
)
nmsbufferHgFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgFree.setStatus("mandatory")
_NmsbufferHgMax_Type = Integer32
_NmsbufferHgMax_Object = MibScalar
nmsbufferHgMax = _NmsbufferHgMax_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 65),
    _NmsbufferHgMax_Type()
)
nmsbufferHgMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgMax.setStatus("mandatory")
_NmsbufferHgHit_Type = Integer32
_NmsbufferHgHit_Object = MibScalar
nmsbufferHgHit = _NmsbufferHgHit_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 66),
    _NmsbufferHgHit_Type()
)
nmsbufferHgHit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgHit.setStatus("mandatory")
_NmsbufferHgMiss_Type = Integer32
_NmsbufferHgMiss_Object = MibScalar
nmsbufferHgMiss = _NmsbufferHgMiss_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 67),
    _NmsbufferHgMiss_Type()
)
nmsbufferHgMiss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgMiss.setStatus("mandatory")
_NmsbufferHgTrim_Type = Integer32
_NmsbufferHgTrim_Object = MibScalar
nmsbufferHgTrim = _NmsbufferHgTrim_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 68),
    _NmsbufferHgTrim_Type()
)
nmsbufferHgTrim.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgTrim.setStatus("mandatory")
_NmsbufferHgCreate_Type = Integer32
_NmsbufferHgCreate_Object = MibScalar
nmsbufferHgCreate = _NmsbufferHgCreate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 69),
    _NmsbufferHgCreate_Type()
)
nmsbufferHgCreate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsbufferHgCreate.setStatus("mandatory")
_NmsnetConfigProto_Type = Integer32
_NmsnetConfigProto_Object = MibScalar
nmsnetConfigProto = _NmsnetConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 70),
    _NmsnetConfigProto_Type()
)
nmsnetConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsnetConfigProto.setStatus("mandatory")
_NmshostConfigProto_Type = Integer32
_NmshostConfigProto_Object = MibScalar
nmshostConfigProto = _NmshostConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 71),
    _NmshostConfigProto_Type()
)
nmshostConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmshostConfigProto.setStatus("mandatory")
_NmssysConfigAddr_Type = IpAddress
_NmssysConfigAddr_Object = MibScalar
nmssysConfigAddr = _NmssysConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 72),
    _NmssysConfigAddr_Type()
)
nmssysConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmssysConfigAddr.setStatus("mandatory")
_NmssysConfigName_Type = DisplayString
_NmssysConfigName_Object = MibScalar
nmssysConfigName = _NmssysConfigName_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 73),
    _NmssysConfigName_Type()
)
nmssysConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmssysConfigName.setStatus("mandatory")
_NmssysConfigProto_Type = Integer32
_NmssysConfigProto_Object = MibScalar
nmssysConfigProto = _NmssysConfigProto_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 74),
    _NmssysConfigProto_Type()
)
nmssysConfigProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmssysConfigProto.setStatus("mandatory")
_NmssysClearARP_Type = Integer32
_NmssysClearARP_Object = MibScalar
nmssysClearARP = _NmssysClearARP_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 75),
    _NmssysClearARP_Type()
)
nmssysClearARP.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmssysClearARP.setStatus("mandatory")
_NmssysClearInt_Type = Integer32
_NmssysClearInt_Object = MibScalar
nmssysClearInt = _NmssysClearInt_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 76),
    _NmssysClearInt_Type()
)
nmssysClearInt.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    nmssysClearInt.setStatus("mandatory")
_NmsenvPresent_Type = Integer32
_NmsenvPresent_Object = MibScalar
nmsenvPresent = _NmsenvPresent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 77),
    _NmsenvPresent_Type()
)
nmsenvPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvPresent.setStatus("mandatory")
_NmsenvTestPt1Descr_Type = DisplayString
_NmsenvTestPt1Descr_Object = MibScalar
nmsenvTestPt1Descr = _NmsenvTestPt1Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 78),
    _NmsenvTestPt1Descr_Type()
)
nmsenvTestPt1Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt1Descr.setStatus("mandatory")
_NmsenvTestPt1Measure_Type = Integer32
_NmsenvTestPt1Measure_Object = MibScalar
nmsenvTestPt1Measure = _NmsenvTestPt1Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 79),
    _NmsenvTestPt1Measure_Type()
)
nmsenvTestPt1Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt1Measure.setStatus("mandatory")
_NmsenvTestPt2Descr_Type = DisplayString
_NmsenvTestPt2Descr_Object = MibScalar
nmsenvTestPt2Descr = _NmsenvTestPt2Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 80),
    _NmsenvTestPt2Descr_Type()
)
nmsenvTestPt2Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt2Descr.setStatus("mandatory")
_NmsenvTestPt2Measure_Type = Integer32
_NmsenvTestPt2Measure_Object = MibScalar
nmsenvTestPt2Measure = _NmsenvTestPt2Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 81),
    _NmsenvTestPt2Measure_Type()
)
nmsenvTestPt2Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt2Measure.setStatus("mandatory")
_NmsenvTestPt3Descr_Type = DisplayString
_NmsenvTestPt3Descr_Object = MibScalar
nmsenvTestPt3Descr = _NmsenvTestPt3Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 82),
    _NmsenvTestPt3Descr_Type()
)
nmsenvTestPt3Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt3Descr.setStatus("mandatory")
_NmsenvTestPt3Measure_Type = Integer32
_NmsenvTestPt3Measure_Object = MibScalar
nmsenvTestPt3Measure = _NmsenvTestPt3Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 83),
    _NmsenvTestPt3Measure_Type()
)
nmsenvTestPt3Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt3Measure.setStatus("mandatory")
_NmsenvTestPt4Descr_Type = DisplayString
_NmsenvTestPt4Descr_Object = MibScalar
nmsenvTestPt4Descr = _NmsenvTestPt4Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 84),
    _NmsenvTestPt4Descr_Type()
)
nmsenvTestPt4Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt4Descr.setStatus("mandatory")
_NmsenvTestPt4Measure_Type = Integer32
_NmsenvTestPt4Measure_Object = MibScalar
nmsenvTestPt4Measure = _NmsenvTestPt4Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 85),
    _NmsenvTestPt4Measure_Type()
)
nmsenvTestPt4Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt4Measure.setStatus("mandatory")
_NmsenvTestPt5Descr_Type = DisplayString
_NmsenvTestPt5Descr_Object = MibScalar
nmsenvTestPt5Descr = _NmsenvTestPt5Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 86),
    _NmsenvTestPt5Descr_Type()
)
nmsenvTestPt5Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt5Descr.setStatus("mandatory")
_NmsenvTestPt5Measure_Type = Integer32
_NmsenvTestPt5Measure_Object = MibScalar
nmsenvTestPt5Measure = _NmsenvTestPt5Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 87),
    _NmsenvTestPt5Measure_Type()
)
nmsenvTestPt5Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt5Measure.setStatus("mandatory")
_NmsenvTestPt6Descr_Type = DisplayString
_NmsenvTestPt6Descr_Object = MibScalar
nmsenvTestPt6Descr = _NmsenvTestPt6Descr_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 88),
    _NmsenvTestPt6Descr_Type()
)
nmsenvTestPt6Descr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt6Descr.setStatus("mandatory")
_NmsenvTestPt6Measure_Type = Integer32
_NmsenvTestPt6Measure_Object = MibScalar
nmsenvTestPt6Measure = _NmsenvTestPt6Measure_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 89),
    _NmsenvTestPt6Measure_Type()
)
nmsenvTestPt6Measure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt6Measure.setStatus("mandatory")
_NmsenvTestPt1MarginVal_Type = Integer32
_NmsenvTestPt1MarginVal_Object = MibScalar
nmsenvTestPt1MarginVal = _NmsenvTestPt1MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 90),
    _NmsenvTestPt1MarginVal_Type()
)
nmsenvTestPt1MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt1MarginVal.setStatus("mandatory")
_NmsenvTestPt2MarginVal_Type = Integer32
_NmsenvTestPt2MarginVal_Object = MibScalar
nmsenvTestPt2MarginVal = _NmsenvTestPt2MarginVal_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 91),
    _NmsenvTestPt2MarginVal_Type()
)
nmsenvTestPt2MarginVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt2MarginVal.setStatus("mandatory")
_NmsenvTestPt3MarginPercent_Type = Integer32
_NmsenvTestPt3MarginPercent_Object = MibScalar
nmsenvTestPt3MarginPercent = _NmsenvTestPt3MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 92),
    _NmsenvTestPt3MarginPercent_Type()
)
nmsenvTestPt3MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt3MarginPercent.setStatus("mandatory")
_NmsenvTestPt4MarginPercent_Type = Integer32
_NmsenvTestPt4MarginPercent_Object = MibScalar
nmsenvTestPt4MarginPercent = _NmsenvTestPt4MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 93),
    _NmsenvTestPt4MarginPercent_Type()
)
nmsenvTestPt4MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt4MarginPercent.setStatus("mandatory")
_NmsenvTestPt5MarginPercent_Type = Integer32
_NmsenvTestPt5MarginPercent_Object = MibScalar
nmsenvTestPt5MarginPercent = _NmsenvTestPt5MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 94),
    _NmsenvTestPt5MarginPercent_Type()
)
nmsenvTestPt5MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt5MarginPercent.setStatus("mandatory")
_NmsenvTestPt6MarginPercent_Type = Integer32
_NmsenvTestPt6MarginPercent_Object = MibScalar
nmsenvTestPt6MarginPercent = _NmsenvTestPt6MarginPercent_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 95),
    _NmsenvTestPt6MarginPercent_Type()
)
nmsenvTestPt6MarginPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt6MarginPercent.setStatus("mandatory")
_NmsenvTestPt1last_Type = Integer32
_NmsenvTestPt1last_Object = MibScalar
nmsenvTestPt1last = _NmsenvTestPt1last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 96),
    _NmsenvTestPt1last_Type()
)
nmsenvTestPt1last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt1last.setStatus("mandatory")
_NmsenvTestPt2last_Type = Integer32
_NmsenvTestPt2last_Object = MibScalar
nmsenvTestPt2last = _NmsenvTestPt2last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 97),
    _NmsenvTestPt2last_Type()
)
nmsenvTestPt2last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt2last.setStatus("mandatory")
_NmsenvTestPt3last_Type = Integer32
_NmsenvTestPt3last_Object = MibScalar
nmsenvTestPt3last = _NmsenvTestPt3last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 98),
    _NmsenvTestPt3last_Type()
)
nmsenvTestPt3last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt3last.setStatus("mandatory")
_NmsenvTestPt4last_Type = Integer32
_NmsenvTestPt4last_Object = MibScalar
nmsenvTestPt4last = _NmsenvTestPt4last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 99),
    _NmsenvTestPt4last_Type()
)
nmsenvTestPt4last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt4last.setStatus("mandatory")
_NmsenvTestPt5last_Type = Integer32
_NmsenvTestPt5last_Object = MibScalar
nmsenvTestPt5last = _NmsenvTestPt5last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 100),
    _NmsenvTestPt5last_Type()
)
nmsenvTestPt5last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt5last.setStatus("mandatory")
_NmsenvTestPt6last_Type = Integer32
_NmsenvTestPt6last_Object = MibScalar
nmsenvTestPt6last = _NmsenvTestPt6last_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 101),
    _NmsenvTestPt6last_Type()
)
nmsenvTestPt6last.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt6last.setStatus("mandatory")


class _NmsenvTestPt1warn_Type(Integer32):
    """Custom type nmsenvTestPt1warn based on Integer32"""
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


_NmsenvTestPt1warn_Type.__name__ = "Integer32"
_NmsenvTestPt1warn_Object = MibScalar
nmsenvTestPt1warn = _NmsenvTestPt1warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 102),
    _NmsenvTestPt1warn_Type()
)
nmsenvTestPt1warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt1warn.setStatus("mandatory")


class _NmsenvTestPt2warn_Type(Integer32):
    """Custom type nmsenvTestPt2warn based on Integer32"""
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


_NmsenvTestPt2warn_Type.__name__ = "Integer32"
_NmsenvTestPt2warn_Object = MibScalar
nmsenvTestPt2warn = _NmsenvTestPt2warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 103),
    _NmsenvTestPt2warn_Type()
)
nmsenvTestPt2warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt2warn.setStatus("mandatory")


class _NmsenvTestPt3warn_Type(Integer32):
    """Custom type nmsenvTestPt3warn based on Integer32"""
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


_NmsenvTestPt3warn_Type.__name__ = "Integer32"
_NmsenvTestPt3warn_Object = MibScalar
nmsenvTestPt3warn = _NmsenvTestPt3warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 104),
    _NmsenvTestPt3warn_Type()
)
nmsenvTestPt3warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt3warn.setStatus("mandatory")


class _NmsenvTestPt4warn_Type(Integer32):
    """Custom type nmsenvTestPt4warn based on Integer32"""
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


_NmsenvTestPt4warn_Type.__name__ = "Integer32"
_NmsenvTestPt4warn_Object = MibScalar
nmsenvTestPt4warn = _NmsenvTestPt4warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 105),
    _NmsenvTestPt4warn_Type()
)
nmsenvTestPt4warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt4warn.setStatus("mandatory")


class _NmsenvTestPt5warn_Type(Integer32):
    """Custom type nmsenvTestPt5warn based on Integer32"""
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


_NmsenvTestPt5warn_Type.__name__ = "Integer32"
_NmsenvTestPt5warn_Object = MibScalar
nmsenvTestPt5warn = _NmsenvTestPt5warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 106),
    _NmsenvTestPt5warn_Type()
)
nmsenvTestPt5warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt5warn.setStatus("mandatory")


class _NmsenvTestPt6warn_Type(Integer32):
    """Custom type nmsenvTestPt6warn based on Integer32"""
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


_NmsenvTestPt6warn_Type.__name__ = "Integer32"
_NmsenvTestPt6warn_Object = MibScalar
nmsenvTestPt6warn = _NmsenvTestPt6warn_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 107),
    _NmsenvTestPt6warn_Type()
)
nmsenvTestPt6warn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTestPt6warn.setStatus("mandatory")
_NmsenvFirmVersion_Type = DisplayString
_NmsenvFirmVersion_Object = MibScalar
nmsenvFirmVersion = _NmsenvFirmVersion_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 108),
    _NmsenvFirmVersion_Type()
)
nmsenvFirmVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvFirmVersion.setStatus("mandatory")
_NmsenvTechnicianID_Type = DisplayString
_NmsenvTechnicianID_Object = MibScalar
nmsenvTechnicianID = _NmsenvTechnicianID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 109),
    _NmsenvTechnicianID_Type()
)
nmsenvTechnicianID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvTechnicianID.setStatus("mandatory")
_NmsenvType_Type = DisplayString
_NmsenvType_Object = MibScalar
nmsenvType = _NmsenvType_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 110),
    _NmsenvType_Type()
)
nmsenvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvType.setStatus("mandatory")
_NmsenvBurnDate_Type = DisplayString
_NmsenvBurnDate_Object = MibScalar
nmsenvBurnDate = _NmsenvBurnDate_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 111),
    _NmsenvBurnDate_Type()
)
nmsenvBurnDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvBurnDate.setStatus("mandatory")
_NmsenvSerialNumber_Type = DisplayString
_NmsenvSerialNumber_Object = MibScalar
nmsenvSerialNumber = _NmsenvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 1, 112),
    _NmsenvSerialNumber_Type()
)
nmsenvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsenvSerialNumber.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-SYS",
    **{"nmslsystem": nmslsystem,
       "nmsromId": nmsromId,
       "nmswhyReload": nmswhyReload,
       "nmshostName": nmshostName,
       "nmsdomainName": nmsdomainName,
       "nmsauthAddr": nmsauthAddr,
       "nmsbootHost": nmsbootHost,
       "nmsping": nmsping,
       "nmsfreeMem": nmsfreeMem,
       "nmsbufferElFree": nmsbufferElFree,
       "nmsbufferElMax": nmsbufferElMax,
       "nmsbufferElHit": nmsbufferElHit,
       "nmsbufferElMiss": nmsbufferElMiss,
       "nmsbufferElCreate": nmsbufferElCreate,
       "nmsbufferSmSize": nmsbufferSmSize,
       "nmsbufferSmTotal": nmsbufferSmTotal,
       "nmsbufferSmFree": nmsbufferSmFree,
       "nmsbufferSmMax": nmsbufferSmMax,
       "nmsbufferSmHit": nmsbufferSmHit,
       "nmsbufferSmMiss": nmsbufferSmMiss,
       "nmsbufferSmTrim": nmsbufferSmTrim,
       "nmsbufferSmCreate": nmsbufferSmCreate,
       "nmsbufferMdSize": nmsbufferMdSize,
       "nmsbufferMdTotal": nmsbufferMdTotal,
       "nmsbufferMdFree": nmsbufferMdFree,
       "nmsbufferMdMax": nmsbufferMdMax,
       "nmsbufferMdHit": nmsbufferMdHit,
       "nmsbufferMdMiss": nmsbufferMdMiss,
       "nmsbufferMdTrim": nmsbufferMdTrim,
       "nmsbufferMdCreate": nmsbufferMdCreate,
       "nmsbufferBgSize": nmsbufferBgSize,
       "nmsbufferBgTotal": nmsbufferBgTotal,
       "nmsbufferBgFree": nmsbufferBgFree,
       "nmsbufferBgMax": nmsbufferBgMax,
       "nmsbufferBgHit": nmsbufferBgHit,
       "nmsbufferBgMiss": nmsbufferBgMiss,
       "nmsbufferBgTrim": nmsbufferBgTrim,
       "nmsbufferBgCreate": nmsbufferBgCreate,
       "nmsbufferLgSize": nmsbufferLgSize,
       "nmsbufferLgTotal": nmsbufferLgTotal,
       "nmsbufferLgFree": nmsbufferLgFree,
       "nmsbufferLgMax": nmsbufferLgMax,
       "nmsbufferLgHit": nmsbufferLgHit,
       "nmsbufferLgMiss": nmsbufferLgMiss,
       "nmsbufferLgTrim": nmsbufferLgTrim,
       "nmsbufferLgCreate": nmsbufferLgCreate,
       "nmsbufferFail": nmsbufferFail,
       "nmsbufferNoMem": nmsbufferNoMem,
       "nmsnetConfigAddr": nmsnetConfigAddr,
       "nmsnetConfigName": nmsnetConfigName,
       "nmsnetConfigSet": nmsnetConfigSet,
       "nmshostConfigAddr": nmshostConfigAddr,
       "nmshostConfigName": nmshostConfigName,
       "nmshostConfigSet": nmshostConfigSet,
       "nmswriteMem": nmswriteMem,
       "nmswriteNet": nmswriteNet,
       "nmsbusyPer": nmsbusyPer,
       "nmsavgBusy1": nmsavgBusy1,
       "nmsavgBusy5": nmsavgBusy5,
       "nmsidleCount": nmsidleCount,
       "nmsidleWired": nmsidleWired,
       "nmsContactInfo": nmsContactInfo,
       "nmsbufferHgSize": nmsbufferHgSize,
       "nmsbufferHgTotal": nmsbufferHgTotal,
       "nmsbufferHgFree": nmsbufferHgFree,
       "nmsbufferHgMax": nmsbufferHgMax,
       "nmsbufferHgHit": nmsbufferHgHit,
       "nmsbufferHgMiss": nmsbufferHgMiss,
       "nmsbufferHgTrim": nmsbufferHgTrim,
       "nmsbufferHgCreate": nmsbufferHgCreate,
       "nmsnetConfigProto": nmsnetConfigProto,
       "nmshostConfigProto": nmshostConfigProto,
       "nmssysConfigAddr": nmssysConfigAddr,
       "nmssysConfigName": nmssysConfigName,
       "nmssysConfigProto": nmssysConfigProto,
       "nmssysClearARP": nmssysClearARP,
       "nmssysClearInt": nmssysClearInt,
       "nmsenvPresent": nmsenvPresent,
       "nmsenvTestPt1Descr": nmsenvTestPt1Descr,
       "nmsenvTestPt1Measure": nmsenvTestPt1Measure,
       "nmsenvTestPt2Descr": nmsenvTestPt2Descr,
       "nmsenvTestPt2Measure": nmsenvTestPt2Measure,
       "nmsenvTestPt3Descr": nmsenvTestPt3Descr,
       "nmsenvTestPt3Measure": nmsenvTestPt3Measure,
       "nmsenvTestPt4Descr": nmsenvTestPt4Descr,
       "nmsenvTestPt4Measure": nmsenvTestPt4Measure,
       "nmsenvTestPt5Descr": nmsenvTestPt5Descr,
       "nmsenvTestPt5Measure": nmsenvTestPt5Measure,
       "nmsenvTestPt6Descr": nmsenvTestPt6Descr,
       "nmsenvTestPt6Measure": nmsenvTestPt6Measure,
       "nmsenvTestPt1MarginVal": nmsenvTestPt1MarginVal,
       "nmsenvTestPt2MarginVal": nmsenvTestPt2MarginVal,
       "nmsenvTestPt3MarginPercent": nmsenvTestPt3MarginPercent,
       "nmsenvTestPt4MarginPercent": nmsenvTestPt4MarginPercent,
       "nmsenvTestPt5MarginPercent": nmsenvTestPt5MarginPercent,
       "nmsenvTestPt6MarginPercent": nmsenvTestPt6MarginPercent,
       "nmsenvTestPt1last": nmsenvTestPt1last,
       "nmsenvTestPt2last": nmsenvTestPt2last,
       "nmsenvTestPt3last": nmsenvTestPt3last,
       "nmsenvTestPt4last": nmsenvTestPt4last,
       "nmsenvTestPt5last": nmsenvTestPt5last,
       "nmsenvTestPt6last": nmsenvTestPt6last,
       "nmsenvTestPt1warn": nmsenvTestPt1warn,
       "nmsenvTestPt2warn": nmsenvTestPt2warn,
       "nmsenvTestPt3warn": nmsenvTestPt3warn,
       "nmsenvTestPt4warn": nmsenvTestPt4warn,
       "nmsenvTestPt5warn": nmsenvTestPt5warn,
       "nmsenvTestPt6warn": nmsenvTestPt6warn,
       "nmsenvFirmVersion": nmsenvFirmVersion,
       "nmsenvTechnicianID": nmsenvTechnicianID,
       "nmsenvType": nmsenvType,
       "nmsenvBurnDate": nmsenvBurnDate,
       "nmsenvSerialNumber": nmsenvSerialNumber}
)
