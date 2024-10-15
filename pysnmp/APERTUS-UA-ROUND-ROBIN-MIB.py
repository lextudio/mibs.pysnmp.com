# SNMP MIB module (APERTUS-UA-ROUND-ROBIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-UA-ROUND-ROBIN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:20 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Directory_ObjectIdentity = ObjectIdentity
directory = _Directory_ObjectIdentity(
    (1, 3, 6, 1, 1)
)
_Mgmt_ObjectIdentity = ObjectIdentity
mgmt = _Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 2)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 3)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Apertus_ObjectIdentity = ObjectIdentity
apertus = _Apertus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543)
)
_Isg_ObjectIdentity = ObjectIdentity
isg = _Isg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3)
)
_Aperua_ObjectIdentity = ObjectIdentity
aperua = _Aperua_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3)
)
_Aperroundrobin_ObjectIdentity = ObjectIdentity
aperroundrobin = _Aperroundrobin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4)
)
_AperRoundRobinMIB_ObjectIdentity = ObjectIdentity
aperRoundRobinMIB = _AperRoundRobinMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1)
)
_AperRoundRobinMIBObjects_ObjectIdentity = ObjectIdentity
aperRoundRobinMIBObjects = _AperRoundRobinMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1)
)
_AperRoundRobinConfig_ObjectIdentity = ObjectIdentity
aperRoundRobinConfig = _AperRoundRobinConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 1)
)


class _AperRoundRobinConfigStatus_Type(Integer32):
    """Custom type aperRoundRobinConfigStatus based on Integer32"""
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
          ("loading", 2),
          ("ready", 1))
    )


_AperRoundRobinConfigStatus_Type.__name__ = "Integer32"
_AperRoundRobinConfigStatus_Object = MibScalar
aperRoundRobinConfigStatus = _AperRoundRobinConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 1, 1),
    _AperRoundRobinConfigStatus_Type()
)
aperRoundRobinConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinConfigStatus.setStatus("mandatory")
_AperRoundRobinConfigUpTime_Type = TimeTicks
_AperRoundRobinConfigUpTime_Object = MibScalar
aperRoundRobinConfigUpTime = _AperRoundRobinConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 1, 2),
    _AperRoundRobinConfigUpTime_Type()
)
aperRoundRobinConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinConfigUpTime.setStatus("mandatory")
_AperRoundRobinDomain_ObjectIdentity = ObjectIdentity
aperRoundRobinDomain = _AperRoundRobinDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2)
)
_AperRoundRobinDomainTable_Object = MibTable
aperRoundRobinDomainTable = _AperRoundRobinDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aperRoundRobinDomainTable.setStatus("mandatory")
_AperRoundRobinDomainEntry_Object = MibTableRow
aperRoundRobinDomainEntry = _AperRoundRobinDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1, 1)
)
aperRoundRobinDomainEntry.setIndexNames(
    (0, "APERTUS-UA-ROUND-ROBIN-MIB", "aperRoundRobinDomainName"),
)
if mibBuilder.loadTexts:
    aperRoundRobinDomainEntry.setStatus("mandatory")
_AperRoundRobinDomainName_Type = DisplayString
_AperRoundRobinDomainName_Object = MibTableColumn
aperRoundRobinDomainName = _AperRoundRobinDomainName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1, 1, 1),
    _AperRoundRobinDomainName_Type()
)
aperRoundRobinDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinDomainName.setStatus("mandatory")


class _AperRoundRobinDomainLastHostIndex_Type(Integer32):
    """Custom type aperRoundRobinDomainLastHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AperRoundRobinDomainLastHostIndex_Type.__name__ = "Integer32"
_AperRoundRobinDomainLastHostIndex_Object = MibTableColumn
aperRoundRobinDomainLastHostIndex = _AperRoundRobinDomainLastHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1, 1, 2),
    _AperRoundRobinDomainLastHostIndex_Type()
)
aperRoundRobinDomainLastHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinDomainLastHostIndex.setStatus("mandatory")


class _AperRoundRobinDomainUpServers_Type(Integer32):
    """Custom type aperRoundRobinDomainUpServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperRoundRobinDomainUpServers_Type.__name__ = "Integer32"
_AperRoundRobinDomainUpServers_Object = MibTableColumn
aperRoundRobinDomainUpServers = _AperRoundRobinDomainUpServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1, 1, 3),
    _AperRoundRobinDomainUpServers_Type()
)
aperRoundRobinDomainUpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinDomainUpServers.setStatus("mandatory")


class _AperRoundRobinDomainDownServers_Type(Integer32):
    """Custom type aperRoundRobinDomainDownServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperRoundRobinDomainDownServers_Type.__name__ = "Integer32"
_AperRoundRobinDomainDownServers_Object = MibTableColumn
aperRoundRobinDomainDownServers = _AperRoundRobinDomainDownServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 2, 1, 1, 4),
    _AperRoundRobinDomainDownServers_Type()
)
aperRoundRobinDomainDownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinDomainDownServers.setStatus("mandatory")
_AperRoundRobinNode_ObjectIdentity = ObjectIdentity
aperRoundRobinNode = _AperRoundRobinNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3)
)
_AperRoundRobinNodeTable_Object = MibTable
aperRoundRobinNodeTable = _AperRoundRobinNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aperRoundRobinNodeTable.setStatus("mandatory")
_AperRoundRobinNodeEntry_Object = MibTableRow
aperRoundRobinNodeEntry = _AperRoundRobinNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1)
)
aperRoundRobinNodeEntry.setIndexNames(
    (0, "APERTUS-UA-ROUND-ROBIN-MIB", "aperRoundRobinNodeName"),
    (0, "APERTUS-UA-ROUND-ROBIN-MIB", "aperRoundRobinNodeIP"),
)
if mibBuilder.loadTexts:
    aperRoundRobinNodeEntry.setStatus("mandatory")
_AperRoundRobinNodeName_Type = DisplayString
_AperRoundRobinNodeName_Object = MibTableColumn
aperRoundRobinNodeName = _AperRoundRobinNodeName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 1),
    _AperRoundRobinNodeName_Type()
)
aperRoundRobinNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodeName.setStatus("mandatory")
_AperRoundRobinNodeIP_Type = IpAddress
_AperRoundRobinNodeIP_Object = MibTableColumn
aperRoundRobinNodeIP = _AperRoundRobinNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 2),
    _AperRoundRobinNodeIP_Type()
)
aperRoundRobinNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodeIP.setStatus("mandatory")


class _AperRoundRobinNodeHostIndex_Type(Integer32):
    """Custom type aperRoundRobinNodeHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AperRoundRobinNodeHostIndex_Type.__name__ = "Integer32"
_AperRoundRobinNodeHostIndex_Object = MibTableColumn
aperRoundRobinNodeHostIndex = _AperRoundRobinNodeHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 3),
    _AperRoundRobinNodeHostIndex_Type()
)
aperRoundRobinNodeHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodeHostIndex.setStatus("mandatory")


class _AperRoundRobinNodePoolIndex_Type(Integer32):
    """Custom type aperRoundRobinNodePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AperRoundRobinNodePoolIndex_Type.__name__ = "Integer32"
_AperRoundRobinNodePoolIndex_Object = MibTableColumn
aperRoundRobinNodePoolIndex = _AperRoundRobinNodePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 4),
    _AperRoundRobinNodePoolIndex_Type()
)
aperRoundRobinNodePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodePoolIndex.setStatus("mandatory")


class _AperRoundRobinNodeStatus_Type(Integer32):
    """Custom type aperRoundRobinNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("notqueried", 3),
          ("up", 1))
    )


_AperRoundRobinNodeStatus_Type.__name__ = "Integer32"
_AperRoundRobinNodeStatus_Object = MibTableColumn
aperRoundRobinNodeStatus = _AperRoundRobinNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 5),
    _AperRoundRobinNodeStatus_Type()
)
aperRoundRobinNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodeStatus.setStatus("mandatory")
_AperRoundRobinNodeResponseTime_Type = TimeTicks
_AperRoundRobinNodeResponseTime_Object = MibTableColumn
aperRoundRobinNodeResponseTime = _AperRoundRobinNodeResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 4, 1, 1, 3, 1, 1, 6),
    _AperRoundRobinNodeResponseTime_Type()
)
aperRoundRobinNodeResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperRoundRobinNodeResponseTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-UA-ROUND-ROBIN-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "aperua": aperua,
       "aperroundrobin": aperroundrobin,
       "aperRoundRobinMIB": aperRoundRobinMIB,
       "aperRoundRobinMIBObjects": aperRoundRobinMIBObjects,
       "aperRoundRobinConfig": aperRoundRobinConfig,
       "aperRoundRobinConfigStatus": aperRoundRobinConfigStatus,
       "aperRoundRobinConfigUpTime": aperRoundRobinConfigUpTime,
       "aperRoundRobinDomain": aperRoundRobinDomain,
       "aperRoundRobinDomainTable": aperRoundRobinDomainTable,
       "aperRoundRobinDomainEntry": aperRoundRobinDomainEntry,
       "aperRoundRobinDomainName": aperRoundRobinDomainName,
       "aperRoundRobinDomainLastHostIndex": aperRoundRobinDomainLastHostIndex,
       "aperRoundRobinDomainUpServers": aperRoundRobinDomainUpServers,
       "aperRoundRobinDomainDownServers": aperRoundRobinDomainDownServers,
       "aperRoundRobinNode": aperRoundRobinNode,
       "aperRoundRobinNodeTable": aperRoundRobinNodeTable,
       "aperRoundRobinNodeEntry": aperRoundRobinNodeEntry,
       "aperRoundRobinNodeName": aperRoundRobinNodeName,
       "aperRoundRobinNodeIP": aperRoundRobinNodeIP,
       "aperRoundRobinNodeHostIndex": aperRoundRobinNodeHostIndex,
       "aperRoundRobinNodePoolIndex": aperRoundRobinNodePoolIndex,
       "aperRoundRobinNodeStatus": aperRoundRobinNodeStatus,
       "aperRoundRobinNodeResponseTime": aperRoundRobinNodeResponseTime}
)
