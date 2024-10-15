# SNMP MIB module (APERTUS-UA-THRESHOLD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APERTUS-UA-THRESHOLD-MIB
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
_Aperthresh_ObjectIdentity = ObjectIdentity
aperthresh = _Aperthresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2)
)
_AperThreshMIB_ObjectIdentity = ObjectIdentity
aperThreshMIB = _AperThreshMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1)
)
_AperThreshMIBObjects_ObjectIdentity = ObjectIdentity
aperThreshMIBObjects = _AperThreshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1)
)
_AperThreshConfig_ObjectIdentity = ObjectIdentity
aperThreshConfig = _AperThreshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 1)
)


class _AperThreshConfigStatus_Type(Integer32):
    """Custom type aperThreshConfigStatus based on Integer32"""
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


_AperThreshConfigStatus_Type.__name__ = "Integer32"
_AperThreshConfigStatus_Object = MibScalar
aperThreshConfigStatus = _AperThreshConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 1, 1),
    _AperThreshConfigStatus_Type()
)
aperThreshConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshConfigStatus.setStatus("mandatory")
_AperThreshConfigUpTime_Type = TimeTicks
_AperThreshConfigUpTime_Object = MibScalar
aperThreshConfigUpTime = _AperThreshConfigUpTime_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 1, 2),
    _AperThreshConfigUpTime_Type()
)
aperThreshConfigUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshConfigUpTime.setStatus("mandatory")
_AperThreshDomain_ObjectIdentity = ObjectIdentity
aperThreshDomain = _AperThreshDomain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2)
)
_AperThreshDomainTable_Object = MibTable
aperThreshDomainTable = _AperThreshDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    aperThreshDomainTable.setStatus("mandatory")
_AperThreshDomainEntry_Object = MibTableRow
aperThreshDomainEntry = _AperThreshDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1)
)
aperThreshDomainEntry.setIndexNames(
    (0, "APERTUS-UA-THRESHOLD-MIB", "aperThreshDomainName"),
)
if mibBuilder.loadTexts:
    aperThreshDomainEntry.setStatus("mandatory")
_AperThreshDomainName_Type = DisplayString
_AperThreshDomainName_Object = MibTableColumn
aperThreshDomainName = _AperThreshDomainName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 1),
    _AperThreshDomainName_Type()
)
aperThreshDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainName.setStatus("mandatory")
_AperThreshDomainLbparms_Type = DisplayString
_AperThreshDomainLbparms_Object = MibTableColumn
aperThreshDomainLbparms = _AperThreshDomainLbparms_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 2),
    _AperThreshDomainLbparms_Type()
)
aperThreshDomainLbparms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainLbparms.setStatus("mandatory")


class _AperThreshDomainFreeSessions_Type(Integer32):
    """Custom type aperThreshDomainFreeSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshDomainFreeSessions_Type.__name__ = "Integer32"
_AperThreshDomainFreeSessions_Object = MibTableColumn
aperThreshDomainFreeSessions = _AperThreshDomainFreeSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 3),
    _AperThreshDomainFreeSessions_Type()
)
aperThreshDomainFreeSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainFreeSessions.setStatus("mandatory")


class _AperThreshDomainMaxSessions_Type(Integer32):
    """Custom type aperThreshDomainMaxSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshDomainMaxSessions_Type.__name__ = "Integer32"
_AperThreshDomainMaxSessions_Object = MibTableColumn
aperThreshDomainMaxSessions = _AperThreshDomainMaxSessions_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 4),
    _AperThreshDomainMaxSessions_Type()
)
aperThreshDomainMaxSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainMaxSessions.setStatus("mandatory")


class _AperThreshDomainUpServers_Type(Integer32):
    """Custom type aperThreshDomainUpServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshDomainUpServers_Type.__name__ = "Integer32"
_AperThreshDomainUpServers_Object = MibTableColumn
aperThreshDomainUpServers = _AperThreshDomainUpServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 5),
    _AperThreshDomainUpServers_Type()
)
aperThreshDomainUpServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainUpServers.setStatus("mandatory")


class _AperThreshDomainDownServers_Type(Integer32):
    """Custom type aperThreshDomainDownServers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshDomainDownServers_Type.__name__ = "Integer32"
_AperThreshDomainDownServers_Object = MibTableColumn
aperThreshDomainDownServers = _AperThreshDomainDownServers_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 6),
    _AperThreshDomainDownServers_Type()
)
aperThreshDomainDownServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainDownServers.setStatus("mandatory")


class _AperThreshDomainCmpMethod_Type(Integer32):
    """Custom type aperThreshDomainCmpMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absolute", 2),
          ("percent", 1))
    )


_AperThreshDomainCmpMethod_Type.__name__ = "Integer32"
_AperThreshDomainCmpMethod_Object = MibTableColumn
aperThreshDomainCmpMethod = _AperThreshDomainCmpMethod_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 2, 1, 1, 7),
    _AperThreshDomainCmpMethod_Type()
)
aperThreshDomainCmpMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshDomainCmpMethod.setStatus("mandatory")
_AperThreshNode_ObjectIdentity = ObjectIdentity
aperThreshNode = _AperThreshNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3)
)
_AperThreshNodeTable_Object = MibTable
aperThreshNodeTable = _AperThreshNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    aperThreshNodeTable.setStatus("mandatory")
_AperThreshNodeEntry_Object = MibTableRow
aperThreshNodeEntry = _AperThreshNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1)
)
aperThreshNodeEntry.setIndexNames(
    (0, "APERTUS-UA-THRESHOLD-MIB", "aperThreshNodeName"),
    (0, "APERTUS-UA-THRESHOLD-MIB", "aperThreshNodeIP"),
)
if mibBuilder.loadTexts:
    aperThreshNodeEntry.setStatus("mandatory")
_AperThreshNodeName_Type = DisplayString
_AperThreshNodeName_Object = MibTableColumn
aperThreshNodeName = _AperThreshNodeName_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 1),
    _AperThreshNodeName_Type()
)
aperThreshNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeName.setStatus("mandatory")
_AperThreshNodeIP_Type = IpAddress
_AperThreshNodeIP_Object = MibTableColumn
aperThreshNodeIP = _AperThreshNodeIP_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 2),
    _AperThreshNodeIP_Type()
)
aperThreshNodeIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeIP.setStatus("mandatory")


class _AperThreshNodeThresholdPercent_Type(Integer32):
    """Custom type aperThreshNodeThresholdPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AperThreshNodeThresholdPercent_Type.__name__ = "Integer32"
_AperThreshNodeThresholdPercent_Object = MibTableColumn
aperThreshNodeThresholdPercent = _AperThreshNodeThresholdPercent_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 3),
    _AperThreshNodeThresholdPercent_Type()
)
aperThreshNodeThresholdPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeThresholdPercent.setStatus("mandatory")


class _AperThreshNodeStatus_Type(Integer32):
    """Custom type aperThreshNodeStatus based on Integer32"""
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


_AperThreshNodeStatus_Type.__name__ = "Integer32"
_AperThreshNodeStatus_Object = MibTableColumn
aperThreshNodeStatus = _AperThreshNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 4),
    _AperThreshNodeStatus_Type()
)
aperThreshNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeStatus.setStatus("mandatory")


class _AperThreshNodeSessionsAvailable_Type(Integer32):
    """Custom type aperThreshNodeSessionsAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshNodeSessionsAvailable_Type.__name__ = "Integer32"
_AperThreshNodeSessionsAvailable_Object = MibTableColumn
aperThreshNodeSessionsAvailable = _AperThreshNodeSessionsAvailable_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 5),
    _AperThreshNodeSessionsAvailable_Type()
)
aperThreshNodeSessionsAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeSessionsAvailable.setStatus("mandatory")


class _AperThreshNodeSessionsPossible_Type(Integer32):
    """Custom type aperThreshNodeSessionsPossible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshNodeSessionsPossible_Type.__name__ = "Integer32"
_AperThreshNodeSessionsPossible_Object = MibTableColumn
aperThreshNodeSessionsPossible = _AperThreshNodeSessionsPossible_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 6),
    _AperThreshNodeSessionsPossible_Type()
)
aperThreshNodeSessionsPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeSessionsPossible.setStatus("mandatory")


class _AperThreshNodeHandFasted_Type(Integer32):
    """Custom type aperThreshNodeHandFasted based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_AperThreshNodeHandFasted_Type.__name__ = "Integer32"
_AperThreshNodeHandFasted_Object = MibTableColumn
aperThreshNodeHandFasted = _AperThreshNodeHandFasted_Object(
    (1, 3, 6, 1, 4, 1, 543, 3, 3, 2, 1, 1, 3, 1, 1, 7),
    _AperThreshNodeHandFasted_Type()
)
aperThreshNodeHandFasted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aperThreshNodeHandFasted.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APERTUS-UA-THRESHOLD-MIB",
    **{"internet": internet,
       "directory": directory,
       "mgmt": mgmt,
       "experimental": experimental,
       "private": private,
       "enterprises": enterprises,
       "apertus": apertus,
       "isg": isg,
       "aperua": aperua,
       "aperthresh": aperthresh,
       "aperThreshMIB": aperThreshMIB,
       "aperThreshMIBObjects": aperThreshMIBObjects,
       "aperThreshConfig": aperThreshConfig,
       "aperThreshConfigStatus": aperThreshConfigStatus,
       "aperThreshConfigUpTime": aperThreshConfigUpTime,
       "aperThreshDomain": aperThreshDomain,
       "aperThreshDomainTable": aperThreshDomainTable,
       "aperThreshDomainEntry": aperThreshDomainEntry,
       "aperThreshDomainName": aperThreshDomainName,
       "aperThreshDomainLbparms": aperThreshDomainLbparms,
       "aperThreshDomainFreeSessions": aperThreshDomainFreeSessions,
       "aperThreshDomainMaxSessions": aperThreshDomainMaxSessions,
       "aperThreshDomainUpServers": aperThreshDomainUpServers,
       "aperThreshDomainDownServers": aperThreshDomainDownServers,
       "aperThreshDomainCmpMethod": aperThreshDomainCmpMethod,
       "aperThreshNode": aperThreshNode,
       "aperThreshNodeTable": aperThreshNodeTable,
       "aperThreshNodeEntry": aperThreshNodeEntry,
       "aperThreshNodeName": aperThreshNodeName,
       "aperThreshNodeIP": aperThreshNodeIP,
       "aperThreshNodeThresholdPercent": aperThreshNodeThresholdPercent,
       "aperThreshNodeStatus": aperThreshNodeStatus,
       "aperThreshNodeSessionsAvailable": aperThreshNodeSessionsAvailable,
       "aperThreshNodeSessionsPossible": aperThreshNodeSessionsPossible,
       "aperThreshNodeHandFasted": aperThreshNodeHandFasted}
)
