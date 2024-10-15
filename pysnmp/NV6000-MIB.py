# SNMP MIB module (NV6000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NV6000-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:02 2024
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

_Ibm_ObjectIdentity = ObjectIdentity
ibm = _Ibm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2)
)
_IbmProd_ObjectIdentity = ObjectIdentity
ibmProd = _IbmProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6)
)
_NetView6000SubAgent_ObjectIdentity = ObjectIdentity
netView6000SubAgent = _NetView6000SubAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4)
)
_Nv6saTrap_ObjectIdentity = ObjectIdentity
nv6saTrap = _Nv6saTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 2)
)
_Nv6saTrapNum_Type = Counter32
_Nv6saTrapNum_Object = MibScalar
nv6saTrapNum = _Nv6saTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 2, 1),
    _Nv6saTrapNum_Type()
)
nv6saTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saTrapNum.setStatus("optional")
_Nv6saTrapThrottleCount_Type = Counter32
_Nv6saTrapThrottleCount_Object = MibScalar
nv6saTrapThrottleCount = _Nv6saTrapThrottleCount_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 2, 2),
    _Nv6saTrapThrottleCount_Type()
)
nv6saTrapThrottleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saTrapThrottleCount.setStatus("optional")
_Nv6saTrapThrottleId_Type = Integer32
_Nv6saTrapThrottleId_Object = MibScalar
nv6saTrapThrottleId = _Nv6saTrapThrottleId_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 2, 3),
    _Nv6saTrapThrottleId_Type()
)
nv6saTrapThrottleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saTrapThrottleId.setStatus("optional")
_Nv6saTrapThrottleTime_Type = Integer32
_Nv6saTrapThrottleTime_Object = MibScalar
nv6saTrapThrottleTime = _Nv6saTrapThrottleTime_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 2, 4),
    _Nv6saTrapThrottleTime_Type()
)
nv6saTrapThrottleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saTrapThrottleTime.setStatus("optional")
_Nv6saIcmp_ObjectIdentity = ObjectIdentity
nv6saIcmp = _Nv6saIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 3)
)
_Nv6saIcmpEchoReq_Type = Integer32
_Nv6saIcmpEchoReq_Object = MibScalar
nv6saIcmpEchoReq = _Nv6saIcmpEchoReq_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 3, 1),
    _Nv6saIcmpEchoReq_Type()
)
nv6saIcmpEchoReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saIcmpEchoReq.setStatus("mandatory")
_Nv6saFileSystem_ObjectIdentity = ObjectIdentity
nv6saFileSystem = _Nv6saFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 4)
)
_Nv6saFileSystemMounted_Type = Gauge32
_Nv6saFileSystemMounted_Object = MibScalar
nv6saFileSystemMounted = _Nv6saFileSystemMounted_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 4, 1),
    _Nv6saFileSystemMounted_Type()
)
nv6saFileSystemMounted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saFileSystemMounted.setStatus("optional")
_Nv6saComputerSystem_ObjectIdentity = ObjectIdentity
nv6saComputerSystem = _Nv6saComputerSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 5)
)
_Nv6saComputerSystemLoad_Type = Gauge32
_Nv6saComputerSystemLoad_Object = MibScalar
nv6saComputerSystemLoad = _Nv6saComputerSystemLoad_Object(
    (1, 3, 6, 1, 4, 1, 2, 6, 4, 5, 1),
    _Nv6saComputerSystemLoad_Type()
)
nv6saComputerSystemLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nv6saComputerSystemLoad.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NV6000-MIB",
    **{"ibm": ibm,
       "ibmProd": ibmProd,
       "netView6000SubAgent": netView6000SubAgent,
       "nv6saTrap": nv6saTrap,
       "nv6saTrapNum": nv6saTrapNum,
       "nv6saTrapThrottleCount": nv6saTrapThrottleCount,
       "nv6saTrapThrottleId": nv6saTrapThrottleId,
       "nv6saTrapThrottleTime": nv6saTrapThrottleTime,
       "nv6saIcmp": nv6saIcmp,
       "nv6saIcmpEchoReq": nv6saIcmpEchoReq,
       "nv6saFileSystem": nv6saFileSystem,
       "nv6saFileSystemMounted": nv6saFileSystemMounted,
       "nv6saComputerSystem": nv6saComputerSystem,
       "nv6saComputerSystemLoad": nv6saComputerSystemLoad}
)
