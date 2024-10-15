# SNMP MIB module (APERTUS-UA-RESPONSE-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-UA-RESPONSE-TIME-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:19 2024
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
_Aperresponsetime_ObjectIdentity = ObjectIdentity
aperresponsetime = _Aperresponsetime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5)
)
_AperResponseTimeMIB_ObjectIdentity = ObjectIdentity
aperResponseTimeMIB = _AperResponseTimeMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1)
)
_AperResponseTimeMIBObjects_ObjectIdentity = ObjectIdentity
aperResponseTimeMIBObjects = _AperResponseTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1)
)
_AperResponseTimeConfig_ObjectIdentity = ObjectIdentity
aperResponseTimeConfig = _AperResponseTimeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1)
)


class _AperResponseTimeConfigStatus_Type(Integer32):
    """Custom type aperResponseTimeConfigStatus based on Integer32"""
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


_AperResponseTimeConfigStatus_Type.__name__ = "Integer32"
_AperResponseTimeConfigStatus_Object = MibScalar
aperResponseTimeConfigStatus = _AperResponseTimeConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1, 1),
    _AperResponseTimeConfigStatus_Type()
)
aperResponseTimeConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeConfigStatus.setStatus("mandatory")
_AperResponseTimeConfigUpTime_Type = TimeTicks
_AperResponseTimeConfigUpTime_Object = MibScalar
aperResponseTimeConfigUpTime = _AperResponseTimeConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 1, 2),
    _AperResponseTimeConfigUpTime_Type()
)
aperResponseTimeConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeConfigUpTime.setStatus("mandatory")
_AperResponseTimeDomain_ObjectIdentity = ObjectIdentity
aperResponseTimeDomain = _AperResponseTimeDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2)
)
_AperResponseTimeDomainTable_Object = MibTable
aperResponseTimeDomainTable = _AperResponseTimeDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aperResponseTimeDomainTable.setStatus("mandatory")
_AperResponseTimeDomainEntry_Object = MibTableRow
aperResponseTimeDomainEntry = _AperResponseTimeDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1)
)
aperResponseTimeDomainEntry.setIndexNames(
    (0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeDomainName"),
)
if mibBuilder.loadTexts:
    aperResponseTimeDomainEntry.setStatus("mandatory")
_AperResponseTimeDomainName_Type = DisplayString
_AperResponseTimeDomainName_Object = MibTableColumn
aperResponseTimeDomainName = _AperResponseTimeDomainName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 1),
    _AperResponseTimeDomainName_Type()
)
aperResponseTimeDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeDomainName.setStatus("mandatory")


class _AperResponseTimeDomainUpServers_Type(Integer32):
    """Custom type aperResponseTimeDomainUpServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperResponseTimeDomainUpServers_Type.__name__ = "Integer32"
_AperResponseTimeDomainUpServers_Object = MibTableColumn
aperResponseTimeDomainUpServers = _AperResponseTimeDomainUpServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 2),
    _AperResponseTimeDomainUpServers_Type()
)
aperResponseTimeDomainUpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeDomainUpServers.setStatus("mandatory")


class _AperResponseTimeDomainDownServers_Type(Integer32):
    """Custom type aperResponseTimeDomainDownServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperResponseTimeDomainDownServers_Type.__name__ = "Integer32"
_AperResponseTimeDomainDownServers_Object = MibTableColumn
aperResponseTimeDomainDownServers = _AperResponseTimeDomainDownServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 3),
    _AperResponseTimeDomainDownServers_Type()
)
aperResponseTimeDomainDownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeDomainDownServers.setStatus("mandatory")


class _AperResponseTimeDomainCompareMethod_Type(Integer32):
    """Custom type aperResponseTimeDomainCompareMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 1),
          ("percentage", 2))
    )


_AperResponseTimeDomainCompareMethod_Type.__name__ = "Integer32"
_AperResponseTimeDomainCompareMethod_Object = MibTableColumn
aperResponseTimeDomainCompareMethod = _AperResponseTimeDomainCompareMethod_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 2, 1, 1, 4),
    _AperResponseTimeDomainCompareMethod_Type()
)
aperResponseTimeDomainCompareMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeDomainCompareMethod.setStatus("mandatory")
_AperResponseTimeNode_ObjectIdentity = ObjectIdentity
aperResponseTimeNode = _AperResponseTimeNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3)
)
_AperResponseTimeNodeTable_Object = MibTable
aperResponseTimeNodeTable = _AperResponseTimeNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aperResponseTimeNodeTable.setStatus("mandatory")
_AperResponseTimeNodeEntry_Object = MibTableRow
aperResponseTimeNodeEntry = _AperResponseTimeNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1)
)
aperResponseTimeNodeEntry.setIndexNames(
    (0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeNodeName"),
    (0, "APERTUS-UA-RESPONSE-TIME-MIB", "aperResponseTimeNodeIP"),
)
if mibBuilder.loadTexts:
    aperResponseTimeNodeEntry.setStatus("mandatory")
_AperResponseTimeNodeName_Type = DisplayString
_AperResponseTimeNodeName_Object = MibTableColumn
aperResponseTimeNodeName = _AperResponseTimeNodeName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 1),
    _AperResponseTimeNodeName_Type()
)
aperResponseTimeNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeName.setStatus("mandatory")
_AperResponseTimeNodeIP_Type = IpAddress
_AperResponseTimeNodeIP_Object = MibTableColumn
aperResponseTimeNodeIP = _AperResponseTimeNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 2),
    _AperResponseTimeNodeIP_Type()
)
aperResponseTimeNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeIP.setStatus("mandatory")


class _AperResponseTimeNodeWindow_Type(Integer32):
    """Custom type aperResponseTimeNodeWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AperResponseTimeNodeWindow_Type.__name__ = "Integer32"
_AperResponseTimeNodeWindow_Object = MibTableColumn
aperResponseTimeNodeWindow = _AperResponseTimeNodeWindow_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 3),
    _AperResponseTimeNodeWindow_Type()
)
aperResponseTimeNodeWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeWindow.setStatus("mandatory")


class _AperResponseTimeNodePoolIndex_Type(Integer32):
    """Custom type aperResponseTimeNodePoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AperResponseTimeNodePoolIndex_Type.__name__ = "Integer32"
_AperResponseTimeNodePoolIndex_Object = MibTableColumn
aperResponseTimeNodePoolIndex = _AperResponseTimeNodePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 4),
    _AperResponseTimeNodePoolIndex_Type()
)
aperResponseTimeNodePoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodePoolIndex.setStatus("mandatory")


class _AperResponseTimeNodeStatus_Type(Integer32):
    """Custom type aperResponseTimeNodeStatus based on Integer32"""
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


_AperResponseTimeNodeStatus_Type.__name__ = "Integer32"
_AperResponseTimeNodeStatus_Object = MibTableColumn
aperResponseTimeNodeStatus = _AperResponseTimeNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 5),
    _AperResponseTimeNodeStatus_Type()
)
aperResponseTimeNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeStatus.setStatus("mandatory")
_AperResponseTimeNodeResponseTime_Type = TimeTicks
_AperResponseTimeNodeResponseTime_Object = MibTableColumn
aperResponseTimeNodeResponseTime = _AperResponseTimeNodeResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 6),
    _AperResponseTimeNodeResponseTime_Type()
)
aperResponseTimeNodeResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeResponseTime.setStatus("mandatory")
_AperResponseTimeNodeAdjustedCompareValue_Type = TimeTicks
_AperResponseTimeNodeAdjustedCompareValue_Object = MibTableColumn
aperResponseTimeNodeAdjustedCompareValue = _AperResponseTimeNodeAdjustedCompareValue_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 5, 1, 1, 3, 1, 1, 7),
    _AperResponseTimeNodeAdjustedCompareValue_Type()
)
aperResponseTimeNodeAdjustedCompareValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperResponseTimeNodeAdjustedCompareValue.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-UA-RESPONSE-TIME-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "aperua": aperua,
       "aperresponsetime": aperresponsetime,
       "aperResponseTimeMIB": aperResponseTimeMIB,
       "aperResponseTimeMIBObjects": aperResponseTimeMIBObjects,
       "aperResponseTimeConfig": aperResponseTimeConfig,
       "aperResponseTimeConfigStatus": aperResponseTimeConfigStatus,
       "aperResponseTimeConfigUpTime": aperResponseTimeConfigUpTime,
       "aperResponseTimeDomain": aperResponseTimeDomain,
       "aperResponseTimeDomainTable": aperResponseTimeDomainTable,
       "aperResponseTimeDomainEntry": aperResponseTimeDomainEntry,
       "aperResponseTimeDomainName": aperResponseTimeDomainName,
       "aperResponseTimeDomainUpServers": aperResponseTimeDomainUpServers,
       "aperResponseTimeDomainDownServers": aperResponseTimeDomainDownServers,
       "aperResponseTimeDomainCompareMethod": aperResponseTimeDomainCompareMethod,
       "aperResponseTimeNode": aperResponseTimeNode,
       "aperResponseTimeNodeTable": aperResponseTimeNodeTable,
       "aperResponseTimeNodeEntry": aperResponseTimeNodeEntry,
       "aperResponseTimeNodeName": aperResponseTimeNodeName,
       "aperResponseTimeNodeIP": aperResponseTimeNodeIP,
       "aperResponseTimeNodeWindow": aperResponseTimeNodeWindow,
       "aperResponseTimeNodePoolIndex": aperResponseTimeNodePoolIndex,
       "aperResponseTimeNodeStatus": aperResponseTimeNodeStatus,
       "aperResponseTimeNodeResponseTime": aperResponseTimeNodeResponseTime,
       "aperResponseTimeNodeAdjustedCompareValue": aperResponseTimeNodeAdjustedCompareValue}
)
