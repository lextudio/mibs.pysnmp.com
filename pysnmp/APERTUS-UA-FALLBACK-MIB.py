# SNMP MIB module (APERTUS-UA-FALLBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-UA-FALLBACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:18 2024
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
_Aperfallback_ObjectIdentity = ObjectIdentity
aperfallback = _Aperfallback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3)
)
_AperFallbackMIB_ObjectIdentity = ObjectIdentity
aperFallbackMIB = _AperFallbackMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1)
)
_AperFallbackMIBObjects_ObjectIdentity = ObjectIdentity
aperFallbackMIBObjects = _AperFallbackMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1)
)
_AperFallbackConfig_ObjectIdentity = ObjectIdentity
aperFallbackConfig = _AperFallbackConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1)
)


class _AperFallbackConfigStatus_Type(Integer32):
    """Custom type aperFallbackConfigStatus based on Integer32"""
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


_AperFallbackConfigStatus_Type.__name__ = "Integer32"
_AperFallbackConfigStatus_Object = MibScalar
aperFallbackConfigStatus = _AperFallbackConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 1),
    _AperFallbackConfigStatus_Type()
)
aperFallbackConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackConfigStatus.setStatus("mandatory")
_AperFallbackConfigUpTime_Type = TimeTicks
_AperFallbackConfigUpTime_Object = MibScalar
aperFallbackConfigUpTime = _AperFallbackConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 1, 2),
    _AperFallbackConfigUpTime_Type()
)
aperFallbackConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackConfigUpTime.setStatus("mandatory")
_AperFallbackDomain_ObjectIdentity = ObjectIdentity
aperFallbackDomain = _AperFallbackDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2)
)
_AperFallbackDomainTable_Object = MibTable
aperFallbackDomainTable = _AperFallbackDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aperFallbackDomainTable.setStatus("mandatory")
_AperFallbackDomainEntry_Object = MibTableRow
aperFallbackDomainEntry = _AperFallbackDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1)
)
aperFallbackDomainEntry.setIndexNames(
    (0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackDomainName"),
)
if mibBuilder.loadTexts:
    aperFallbackDomainEntry.setStatus("mandatory")
_AperFallbackDomainName_Type = DisplayString
_AperFallbackDomainName_Object = MibTableColumn
aperFallbackDomainName = _AperFallbackDomainName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 1),
    _AperFallbackDomainName_Type()
)
aperFallbackDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackDomainName.setStatus("mandatory")


class _AperFallbackDomainUpServers_Type(Integer32):
    """Custom type aperFallbackDomainUpServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperFallbackDomainUpServers_Type.__name__ = "Integer32"
_AperFallbackDomainUpServers_Object = MibTableColumn
aperFallbackDomainUpServers = _AperFallbackDomainUpServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 2),
    _AperFallbackDomainUpServers_Type()
)
aperFallbackDomainUpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackDomainUpServers.setStatus("mandatory")


class _AperFallbackDomainDownServers_Type(Integer32):
    """Custom type aperFallbackDomainDownServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperFallbackDomainDownServers_Type.__name__ = "Integer32"
_AperFallbackDomainDownServers_Object = MibTableColumn
aperFallbackDomainDownServers = _AperFallbackDomainDownServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 2, 1, 1, 3),
    _AperFallbackDomainDownServers_Type()
)
aperFallbackDomainDownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackDomainDownServers.setStatus("mandatory")
_AperFallbackNode_ObjectIdentity = ObjectIdentity
aperFallbackNode = _AperFallbackNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3)
)
_AperFallbackNodeTable_Object = MibTable
aperFallbackNodeTable = _AperFallbackNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aperFallbackNodeTable.setStatus("mandatory")
_AperFallbackNodeEntry_Object = MibTableRow
aperFallbackNodeEntry = _AperFallbackNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1)
)
aperFallbackNodeEntry.setIndexNames(
    (0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeName"),
    (0, "APERTUS-UA-FALLBACK-MIB", "aperFallbackNodeIP"),
)
if mibBuilder.loadTexts:
    aperFallbackNodeEntry.setStatus("mandatory")
_AperFallbackNodeName_Type = DisplayString
_AperFallbackNodeName_Object = MibTableColumn
aperFallbackNodeName = _AperFallbackNodeName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 1),
    _AperFallbackNodeName_Type()
)
aperFallbackNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodeName.setStatus("mandatory")
_AperFallbackNodeIP_Type = IpAddress
_AperFallbackNodeIP_Object = MibTableColumn
aperFallbackNodeIP = _AperFallbackNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 2),
    _AperFallbackNodeIP_Type()
)
aperFallbackNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodeIP.setStatus("mandatory")


class _AperFallbackNodeHostIndex_Type(Integer32):
    """Custom type aperFallbackNodeHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AperFallbackNodeHostIndex_Type.__name__ = "Integer32"
_AperFallbackNodeHostIndex_Object = MibTableColumn
aperFallbackNodeHostIndex = _AperFallbackNodeHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 3),
    _AperFallbackNodeHostIndex_Type()
)
aperFallbackNodeHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodeHostIndex.setStatus("mandatory")


class _AperFallbackNodePoolIndex_Type(Integer32):
    """Custom type aperFallbackNodePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AperFallbackNodePoolIndex_Type.__name__ = "Integer32"
_AperFallbackNodePoolIndex_Object = MibTableColumn
aperFallbackNodePoolIndex = _AperFallbackNodePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 4),
    _AperFallbackNodePoolIndex_Type()
)
aperFallbackNodePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodePoolIndex.setStatus("mandatory")


class _AperFallbackNodeStatus_Type(Integer32):
    """Custom type aperFallbackNodeStatus based on Integer32"""
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


_AperFallbackNodeStatus_Type.__name__ = "Integer32"
_AperFallbackNodeStatus_Object = MibTableColumn
aperFallbackNodeStatus = _AperFallbackNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 5),
    _AperFallbackNodeStatus_Type()
)
aperFallbackNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodeStatus.setStatus("mandatory")
_AperFallbackNodeResponseTime_Type = TimeTicks
_AperFallbackNodeResponseTime_Object = MibTableColumn
aperFallbackNodeResponseTime = _AperFallbackNodeResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 3, 1, 1, 3, 1, 1, 6),
    _AperFallbackNodeResponseTime_Type()
)
aperFallbackNodeResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperFallbackNodeResponseTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-UA-FALLBACK-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "aperua": aperua,
       "aperfallback": aperfallback,
       "aperFallbackMIB": aperFallbackMIB,
       "aperFallbackMIBObjects": aperFallbackMIBObjects,
       "aperFallbackConfig": aperFallbackConfig,
       "aperFallbackConfigStatus": aperFallbackConfigStatus,
       "aperFallbackConfigUpTime": aperFallbackConfigUpTime,
       "aperFallbackDomain": aperFallbackDomain,
       "aperFallbackDomainTable": aperFallbackDomainTable,
       "aperFallbackDomainEntry": aperFallbackDomainEntry,
       "aperFallbackDomainName": aperFallbackDomainName,
       "aperFallbackDomainUpServers": aperFallbackDomainUpServers,
       "aperFallbackDomainDownServers": aperFallbackDomainDownServers,
       "aperFallbackNode": aperFallbackNode,
       "aperFallbackNodeTable": aperFallbackNodeTable,
       "aperFallbackNodeEntry": aperFallbackNodeEntry,
       "aperFallbackNodeName": aperFallbackNodeName,
       "aperFallbackNodeIP": aperFallbackNodeIP,
       "aperFallbackNodeHostIndex": aperFallbackNodeHostIndex,
       "aperFallbackNodePoolIndex": aperFallbackNodePoolIndex,
       "aperFallbackNodeStatus": aperFallbackNodeStatus,
       "aperFallbackNodeResponseTime": aperFallbackNodeResponseTime}
)
