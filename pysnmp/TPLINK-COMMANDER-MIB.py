# SNMP MIB module (TPLINK-COMMANDER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-COMMANDER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:53 2024
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

(clusterManage,) = mibBuilder.importSymbols(
    "TPLINK-CLUSTER-MIB",
    "clusterManage")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ClusterConfig_ObjectIdentity = ObjectIdentity
clusterConfig = _ClusterConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2)
)


class _ClusterName_Type(DisplayString):
    """Custom type clusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ClusterName_Type.__name__ = "DisplayString"
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 1),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")


class _ClusterHoldTime_Type(Integer32):
    """Custom type clusterHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClusterHoldTime_Type.__name__ = "Integer32"
_ClusterHoldTime_Object = MibScalar
clusterHoldTime = _ClusterHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 2),
    _ClusterHoldTime_Type()
)
clusterHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterHoldTime.setStatus("current")


class _ClusterIntervalTime_Type(Integer32):
    """Custom type clusterIntervalTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClusterIntervalTime_Type.__name__ = "Integer32"
_ClusterIntervalTime_Object = MibScalar
clusterIntervalTime = _ClusterIntervalTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 3),
    _ClusterIntervalTime_Type()
)
clusterIntervalTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterIntervalTime.setStatus("current")
_CommanderConfig_ObjectIdentity = ObjectIdentity
commanderConfig = _CommanderConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4)
)


class _CommanderClusterName_Type(DisplayString):
    """Custom type commanderClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CommanderClusterName_Type.__name__ = "DisplayString"
_CommanderClusterName_Object = MibScalar
commanderClusterName = _CommanderClusterName_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 1),
    _CommanderClusterName_Type()
)
commanderClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commanderClusterName.setStatus("current")
_ClusterIp_Type = IpAddress
_ClusterIp_Object = MibScalar
clusterIp = _ClusterIp_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 2),
    _ClusterIp_Type()
)
clusterIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterIp.setStatus("current")
_ClusterIpMask_Type = IpAddress
_ClusterIpMask_Object = MibScalar
clusterIpMask = _ClusterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 3),
    _ClusterIpMask_Type()
)
clusterIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterIpMask.setStatus("current")


class _ClusterCommit_Type(Integer32):
    """Custom type clusterCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("commit", 1)
    )


_ClusterCommit_Type.__name__ = "Integer32"
_ClusterCommit_Object = MibScalar
clusterCommit = _ClusterCommit_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 33, 1, 1, 3, 2, 4, 4),
    _ClusterCommit_Type()
)
clusterCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterCommit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-COMMANDER-MIB",
    **{"clusterConfig": clusterConfig,
       "clusterName": clusterName,
       "clusterHoldTime": clusterHoldTime,
       "clusterIntervalTime": clusterIntervalTime,
       "commanderConfig": commanderConfig,
       "commanderClusterName": commanderClusterName,
       "clusterIp": clusterIp,
       "clusterIpMask": clusterIpMask,
       "clusterCommit": clusterCommit}
)
