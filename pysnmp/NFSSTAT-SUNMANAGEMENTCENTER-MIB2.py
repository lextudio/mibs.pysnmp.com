# SNMP MIB module (NFSSTAT-SUNMANAGEMENTCENTER-MIB2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NFSSTAT-SUNMANAGEMENTCENTER-MIB2
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:24 2024
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

nfsstat = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28)
)
nfsstat.setRevisions(
        ("1999-07-20 15:05",)
)


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
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2)
)
_NfsStats_ObjectIdentity = ObjectIdentity
nfsStats = _NfsStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1)
)
_NfssTotServRPCCalls_Type = Integer32
_NfssTotServRPCCalls_Object = MibScalar
nfssTotServRPCCalls = _NfssTotServRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 1),
    _NfssTotServRPCCalls_Type()
)
nfssTotServRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssTotServRPCCalls.setStatus("current")
_NfssServBadRPCCalls_Type = Integer32
_NfssServBadRPCCalls_Object = MibScalar
nfssServBadRPCCalls = _NfssServBadRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 2),
    _NfssServBadRPCCalls_Type()
)
nfssServBadRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServBadRPCCalls.setStatus("current")
_NfssServPcntBadRPCCalls_Type = DisplayString
_NfssServPcntBadRPCCalls_Object = MibScalar
nfssServPcntBadRPCCalls = _NfssServPcntBadRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 3),
    _NfssServPcntBadRPCCalls_Type()
)
nfssServPcntBadRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServPcntBadRPCCalls.setStatus("current")
if mibBuilder.loadTexts:
    nfssServPcntBadRPCCalls.setUnits("%")
_NfssServRPCCallRate_Type = DisplayString
_NfssServRPCCallRate_Object = MibScalar
nfssServRPCCallRate = _NfssServRPCCallRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1, 4),
    _NfssServRPCCallRate_Type()
)
nfssServRPCCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServRPCCallRate.setStatus("current")
if mibBuilder.loadTexts:
    nfssServRPCCallRate.setUnits("/sec")
_NfssServTotNFSCalls_Type = Integer32
_NfssServTotNFSCalls_Object = MibScalar
nfssServTotNFSCalls = _NfssServTotNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 1),
    _NfssServTotNFSCalls_Type()
)
nfssServTotNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServTotNFSCalls.setStatus("current")
_NfssServBadNFSCalls_Type = Integer32
_NfssServBadNFSCalls_Object = MibScalar
nfssServBadNFSCalls = _NfssServBadNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 2),
    _NfssServBadNFSCalls_Type()
)
nfssServBadNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServBadNFSCalls.setStatus("current")
_NfssServPcntBadNFSCalls_Type = DisplayString
_NfssServPcntBadNFSCalls_Object = MibScalar
nfssServPcntBadNFSCalls = _NfssServPcntBadNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 3),
    _NfssServPcntBadNFSCalls_Type()
)
nfssServPcntBadNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServPcntBadNFSCalls.setStatus("current")
if mibBuilder.loadTexts:
    nfssServPcntBadNFSCalls.setUnits("%")
_NfssServNFSCallRate_Type = DisplayString
_NfssServNFSCallRate_Object = MibScalar
nfssServNFSCallRate = _NfssServNFSCallRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2, 4),
    _NfssServNFSCallRate_Type()
)
nfssServNFSCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssServNFSCallRate.setStatus("current")
if mibBuilder.loadTexts:
    nfssServNFSCallRate.setUnits("/sec")
_NfssCliTotRPCCalls_Type = Integer32
_NfssCliTotRPCCalls_Object = MibScalar
nfssCliTotRPCCalls = _NfssCliTotRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 1),
    _NfssCliTotRPCCalls_Type()
)
nfssCliTotRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliTotRPCCalls.setStatus("current")
_NfssCliBadRPCCalls_Type = Integer32
_NfssCliBadRPCCalls_Object = MibScalar
nfssCliBadRPCCalls = _NfssCliBadRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 2),
    _NfssCliBadRPCCalls_Type()
)
nfssCliBadRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliBadRPCCalls.setStatus("current")
_NfssCliPcntBadRPCCalls_Type = DisplayString
_NfssCliPcntBadRPCCalls_Object = MibScalar
nfssCliPcntBadRPCCalls = _NfssCliPcntBadRPCCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 3),
    _NfssCliPcntBadRPCCalls_Type()
)
nfssCliPcntBadRPCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliPcntBadRPCCalls.setStatus("current")
if mibBuilder.loadTexts:
    nfssCliPcntBadRPCCalls.setUnits("%")
_NfssCliRPCCallRate_Type = DisplayString
_NfssCliRPCCallRate_Object = MibScalar
nfssCliRPCCallRate = _NfssCliRPCCallRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3, 4),
    _NfssCliRPCCallRate_Type()
)
nfssCliRPCCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliRPCCallRate.setStatus("current")
if mibBuilder.loadTexts:
    nfssCliRPCCallRate.setUnits("/sec")
_NfssCliTotNFSCalls_Type = Integer32
_NfssCliTotNFSCalls_Object = MibScalar
nfssCliTotNFSCalls = _NfssCliTotNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 1),
    _NfssCliTotNFSCalls_Type()
)
nfssCliTotNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliTotNFSCalls.setStatus("current")
_NfssCliBadNFSCalls_Type = Integer32
_NfssCliBadNFSCalls_Object = MibScalar
nfssCliBadNFSCalls = _NfssCliBadNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 2),
    _NfssCliBadNFSCalls_Type()
)
nfssCliBadNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliBadNFSCalls.setStatus("current")
_NfssCliPcntBadNFSCalls_Type = DisplayString
_NfssCliPcntBadNFSCalls_Object = MibScalar
nfssCliPcntBadNFSCalls = _NfssCliPcntBadNFSCalls_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 3),
    _NfssCliPcntBadNFSCalls_Type()
)
nfssCliPcntBadNFSCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliPcntBadNFSCalls.setStatus("current")
if mibBuilder.loadTexts:
    nfssCliPcntBadNFSCalls.setUnits("%")
_NfssCliNFSCallRate_Type = DisplayString
_NfssCliNFSCallRate_Object = MibScalar
nfssCliNFSCallRate = _NfssCliNFSCallRate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4, 4),
    _NfssCliNFSCallRate_Type()
)
nfssCliNFSCallRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nfssCliNFSCallRate.setStatus("current")
if mibBuilder.loadTexts:
    nfssCliNFSCallRate.setUnits("/sec")

# Managed Objects groups

nfssServerRPCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 1)
)
nfssServerRPCStatGroup.setObjects(
      *(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssTotServRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServBadRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServPcntBadRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServRPCCallRate"))
)
if mibBuilder.loadTexts:
    nfssServerRPCStatGroup.setStatus("current")

nfssServerNFSStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 2)
)
nfssServerNFSStatGroup.setObjects(
      *(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServTotNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServBadNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServPcntBadNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssServNFSCallRate"))
)
if mibBuilder.loadTexts:
    nfssServerNFSStatGroup.setStatus("current")

nfssClientRPCStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 3)
)
nfssClientRPCStatGroup.setObjects(
      *(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliTotRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliBadRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliPcntBadRPCCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliRPCCallRate"))
)
if mibBuilder.loadTexts:
    nfssClientRPCStatGroup.setStatus("current")

nfssClientNFSStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 12, 2, 2, 28, 1, 4)
)
nfssClientNFSStatGroup.setObjects(
      *(("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliTotNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliBadNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliPcntBadNFSCalls"),
        ("NFSSTAT-SUNMANAGEMENTCENTER-MIB2", "nfssCliNFSCallRate"))
)
if mibBuilder.loadTexts:
    nfssClientNFSStatGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NFSSTAT-SUNMANAGEMENTCENTER-MIB2",
    **{"sun": sun,
       "prod": prod,
       "sunsymon": sunsymon,
       "agent": agent,
       "modules": modules,
       "nfsstat": nfsstat,
       "nfsStats": nfsStats,
       "nfssServerRPCStatGroup": nfssServerRPCStatGroup,
       "nfssTotServRPCCalls": nfssTotServRPCCalls,
       "nfssServBadRPCCalls": nfssServBadRPCCalls,
       "nfssServPcntBadRPCCalls": nfssServPcntBadRPCCalls,
       "nfssServRPCCallRate": nfssServRPCCallRate,
       "nfssServerNFSStatGroup": nfssServerNFSStatGroup,
       "nfssServTotNFSCalls": nfssServTotNFSCalls,
       "nfssServBadNFSCalls": nfssServBadNFSCalls,
       "nfssServPcntBadNFSCalls": nfssServPcntBadNFSCalls,
       "nfssServNFSCallRate": nfssServNFSCallRate,
       "nfssClientRPCStatGroup": nfssClientRPCStatGroup,
       "nfssCliTotRPCCalls": nfssCliTotRPCCalls,
       "nfssCliBadRPCCalls": nfssCliBadRPCCalls,
       "nfssCliPcntBadRPCCalls": nfssCliPcntBadRPCCalls,
       "nfssCliRPCCallRate": nfssCliRPCCallRate,
       "nfssClientNFSStatGroup": nfssClientNFSStatGroup,
       "nfssCliTotNFSCalls": nfssCliTotNFSCalls,
       "nfssCliBadNFSCalls": nfssCliBadNFSCalls,
       "nfssCliPcntBadNFSCalls": nfssCliPcntBadNFSCalls,
       "nfssCliNFSCallRate": nfssCliNFSCallRate}
)
