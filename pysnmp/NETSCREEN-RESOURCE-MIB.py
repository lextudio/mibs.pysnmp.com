# SNMP MIB module (NETSCREEN-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-RESOURCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:51 2024
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

(netscreenResource,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenResource")

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

netscreenResourceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 0)
)
netscreenResourceMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2002-05-05 00:00",
         "2001-04-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsResCPU_ObjectIdentity = ObjectIdentity
nsResCPU = _NsResCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1)
)
_NsResCpuAvg_Type = Integer32
_NsResCpuAvg_Object = MibScalar
nsResCpuAvg = _NsResCpuAvg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 1),
    _NsResCpuAvg_Type()
)
nsResCpuAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuAvg.setStatus("current")
_NsResCpuLast1Min_Type = Integer32
_NsResCpuLast1Min_Object = MibScalar
nsResCpuLast1Min = _NsResCpuLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 2),
    _NsResCpuLast1Min_Type()
)
nsResCpuLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast1Min.setStatus("current")
_NsResCpuLast5Min_Type = Integer32
_NsResCpuLast5Min_Object = MibScalar
nsResCpuLast5Min = _NsResCpuLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 3),
    _NsResCpuLast5Min_Type()
)
nsResCpuLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast5Min.setStatus("current")
_NsResCpuLast15Min_Type = Integer32
_NsResCpuLast15Min_Object = MibScalar
nsResCpuLast15Min = _NsResCpuLast15Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 4),
    _NsResCpuLast15Min_Type()
)
nsResCpuLast15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast15Min.setStatus("current")
_NsResMem_ObjectIdentity = ObjectIdentity
nsResMem = _NsResMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2)
)
_NsResMemAllocate_Type = Integer32
_NsResMemAllocate_Object = MibScalar
nsResMemAllocate = _NsResMemAllocate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 1),
    _NsResMemAllocate_Type()
)
nsResMemAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemAllocate.setStatus("current")
_NsResMemLeft_Type = Integer32
_NsResMemLeft_Object = MibScalar
nsResMemLeft = _NsResMemLeft_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 2),
    _NsResMemLeft_Type()
)
nsResMemLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemLeft.setStatus("current")
_NsResMemFrag_Type = Integer32
_NsResMemFrag_Object = MibScalar
nsResMemFrag = _NsResMemFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 3),
    _NsResMemFrag_Type()
)
nsResMemFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemFrag.setStatus("current")
_NsResSession_ObjectIdentity = ObjectIdentity
nsResSession = _NsResSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3)
)
_NsResSessAllocate_Type = Integer32
_NsResSessAllocate_Object = MibScalar
nsResSessAllocate = _NsResSessAllocate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 2),
    _NsResSessAllocate_Type()
)
nsResSessAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessAllocate.setStatus("current")
_NsResSessMaxium_Type = Integer32
_NsResSessMaxium_Object = MibScalar
nsResSessMaxium = _NsResSessMaxium_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 3),
    _NsResSessMaxium_Type()
)
nsResSessMaxium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessMaxium.setStatus("current")
_NsResSessFailed_Type = Integer32
_NsResSessFailed_Object = MibScalar
nsResSessFailed = _NsResSessFailed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 4),
    _NsResSessFailed_Type()
)
nsResSessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessFailed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-RESOURCE-MIB",
    **{"netscreenResourceMibModule": netscreenResourceMibModule,
       "nsResCPU": nsResCPU,
       "nsResCpuAvg": nsResCpuAvg,
       "nsResCpuLast1Min": nsResCpuLast1Min,
       "nsResCpuLast5Min": nsResCpuLast5Min,
       "nsResCpuLast15Min": nsResCpuLast15Min,
       "nsResMem": nsResMem,
       "nsResMemAllocate": nsResMemAllocate,
       "nsResMemLeft": nsResMemLeft,
       "nsResMemFrag": nsResMemFrag,
       "nsResSession": nsResSession,
       "nsResSessAllocate": nsResSessAllocate,
       "nsResSessMaxium": nsResSessMaxium,
       "nsResSessFailed": nsResSessFailed}
)
