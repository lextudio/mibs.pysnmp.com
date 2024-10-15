# SNMP MIB module (CABH-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-QOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:09 2024
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

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cabhQosMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6)
)
cabhQosMib.setRevisions(
        ("2003-03-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhQosMibObjects_ObjectIdentity = ObjectIdentity
cabhQosMibObjects = _CabhQosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1)
)
_CabhPriorityQosMibObjects_ObjectIdentity = ObjectIdentity
cabhPriorityQosMibObjects = _CabhPriorityQosMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1)
)
_CabhPriorityQosBase_ObjectIdentity = ObjectIdentity
cabhPriorityQosBase = _CabhPriorityQosBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1)
)
_CabhPriorityQosMasterTable_Object = MibTable
cabhPriorityQosMasterTable = _CabhPriorityQosMasterTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cabhPriorityQosMasterTable.setStatus("current")
_CabhPriorityQosMasterEntry_Object = MibTableRow
cabhPriorityQosMasterEntry = _CabhPriorityQosMasterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 1, 1)
)
cabhPriorityQosMasterEntry.setIndexNames(
    (0, "CABH-QOS-MIB", "cabhPriorityQosMasterApplicationId"),
)
if mibBuilder.loadTexts:
    cabhPriorityQosMasterEntry.setStatus("current")


class _CabhPriorityQosMasterApplicationId_Type(Unsigned32):
    """Custom type cabhPriorityQosMasterApplicationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPriorityQosMasterApplicationId_Type.__name__ = "Unsigned32"
_CabhPriorityQosMasterApplicationId_Object = MibTableColumn
cabhPriorityQosMasterApplicationId = _CabhPriorityQosMasterApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 1, 1, 1),
    _CabhPriorityQosMasterApplicationId_Type()
)
cabhPriorityQosMasterApplicationId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPriorityQosMasterApplicationId.setStatus("current")


class _CabhPriorityQosMasterDefaultCHPriority_Type(Unsigned32):
    """Custom type cabhPriorityQosMasterDefaultCHPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CabhPriorityQosMasterDefaultCHPriority_Type.__name__ = "Unsigned32"
_CabhPriorityQosMasterDefaultCHPriority_Object = MibTableColumn
cabhPriorityQosMasterDefaultCHPriority = _CabhPriorityQosMasterDefaultCHPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 1, 1, 2),
    _CabhPriorityQosMasterDefaultCHPriority_Type()
)
cabhPriorityQosMasterDefaultCHPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhPriorityQosMasterDefaultCHPriority.setStatus("current")
_CabhPriorityQosMasterRowStatus_Type = RowStatus
_CabhPriorityQosMasterRowStatus_Object = MibTableColumn
cabhPriorityQosMasterRowStatus = _CabhPriorityQosMasterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 1, 1, 3),
    _CabhPriorityQosMasterRowStatus_Type()
)
cabhPriorityQosMasterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhPriorityQosMasterRowStatus.setStatus("current")
_CabhPriorityQosSetToFactory_Type = TruthValue
_CabhPriorityQosSetToFactory_Object = MibScalar
cabhPriorityQosSetToFactory = _CabhPriorityQosSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 1, 2),
    _CabhPriorityQosSetToFactory_Type()
)
cabhPriorityQosSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPriorityQosSetToFactory.setStatus("current")
_CabhPriorityQosBp_ObjectIdentity = ObjectIdentity
cabhPriorityQosBp = _CabhPriorityQosBp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2)
)
_CabhPriorityQosBpTable_Object = MibTable
cabhPriorityQosBpTable = _CabhPriorityQosBpTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cabhPriorityQosBpTable.setStatus("current")
_CabhPriorityQosBpEntry_Object = MibTableRow
cabhPriorityQosBpEntry = _CabhPriorityQosBpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1)
)
cabhPriorityQosBpEntry.setIndexNames(
    (0, "CABH-QOS-MIB", "cabhPriorityQosMasterApplicationId"),
    (0, "CABH-QOS-MIB", "cabhPriorityQosBpIpAddrType"),
    (0, "CABH-QOS-MIB", "cabhPriorityQosBpIpAddr"),
)
if mibBuilder.loadTexts:
    cabhPriorityQosBpEntry.setStatus("current")
_CabhPriorityQosBpIpAddrType_Type = InetAddressType
_CabhPriorityQosBpIpAddrType_Object = MibTableColumn
cabhPriorityQosBpIpAddrType = _CabhPriorityQosBpIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1, 1),
    _CabhPriorityQosBpIpAddrType_Type()
)
cabhPriorityQosBpIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpIpAddrType.setStatus("current")
_CabhPriorityQosBpIpAddr_Type = InetAddress
_CabhPriorityQosBpIpAddr_Object = MibTableColumn
cabhPriorityQosBpIpAddr = _CabhPriorityQosBpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1, 2),
    _CabhPriorityQosBpIpAddr_Type()
)
cabhPriorityQosBpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpIpAddr.setStatus("current")


class _CabhPriorityQosBpApplicationId_Type(Unsigned32):
    """Custom type cabhPriorityQosBpApplicationId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPriorityQosBpApplicationId_Type.__name__ = "Unsigned32"
_CabhPriorityQosBpApplicationId_Object = MibTableColumn
cabhPriorityQosBpApplicationId = _CabhPriorityQosBpApplicationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1, 3),
    _CabhPriorityQosBpApplicationId_Type()
)
cabhPriorityQosBpApplicationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpApplicationId.setStatus("current")


class _CabhPriorityQosBpDefaultCHPriority_Type(Unsigned32):
    """Custom type cabhPriorityQosBpDefaultCHPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CabhPriorityQosBpDefaultCHPriority_Type.__name__ = "Unsigned32"
_CabhPriorityQosBpDefaultCHPriority_Object = MibTableColumn
cabhPriorityQosBpDefaultCHPriority = _CabhPriorityQosBpDefaultCHPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1, 4),
    _CabhPriorityQosBpDefaultCHPriority_Type()
)
cabhPriorityQosBpDefaultCHPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDefaultCHPriority.setStatus("current")


class _CabhPriorityQosBpIndex_Type(Unsigned32):
    """Custom type cabhPriorityQosBpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPriorityQosBpIndex_Type.__name__ = "Unsigned32"
_CabhPriorityQosBpIndex_Object = MibTableColumn
cabhPriorityQosBpIndex = _CabhPriorityQosBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 1, 1, 5),
    _CabhPriorityQosBpIndex_Type()
)
cabhPriorityQosBpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpIndex.setStatus("current")
_CabhPriorityQosBpDestTable_Object = MibTable
cabhPriorityQosBpDestTable = _CabhPriorityQosBpDestTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestTable.setStatus("current")
_CabhPriorityQosBpDestEntry_Object = MibTableRow
cabhPriorityQosBpDestEntry = _CabhPriorityQosBpDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1)
)
cabhPriorityQosBpDestEntry.setIndexNames(
    (0, "CABH-QOS-MIB", "cabhPriorityQosBpIndex"),
    (0, "CABH-QOS-MIB", "cabhPriorityQosBpDestIndex"),
)
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestEntry.setStatus("current")


class _CabhPriorityQosBpDestIndex_Type(Unsigned32):
    """Custom type cabhPriorityQosBpDestIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPriorityQosBpDestIndex_Type.__name__ = "Unsigned32"
_CabhPriorityQosBpDestIndex_Object = MibTableColumn
cabhPriorityQosBpDestIndex = _CabhPriorityQosBpDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1, 1),
    _CabhPriorityQosBpDestIndex_Type()
)
cabhPriorityQosBpDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestIndex.setStatus("current")
_CabhPriorityQosBpDestIpAddrType_Type = InetAddressType
_CabhPriorityQosBpDestIpAddrType_Object = MibTableColumn
cabhPriorityQosBpDestIpAddrType = _CabhPriorityQosBpDestIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1, 2),
    _CabhPriorityQosBpDestIpAddrType_Type()
)
cabhPriorityQosBpDestIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestIpAddrType.setStatus("current")
_CabhPriorityQosBpDestIpAddr_Type = InetAddress
_CabhPriorityQosBpDestIpAddr_Object = MibTableColumn
cabhPriorityQosBpDestIpAddr = _CabhPriorityQosBpDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1, 3),
    _CabhPriorityQosBpDestIpAddr_Type()
)
cabhPriorityQosBpDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestIpAddr.setStatus("current")
_CabhPriorityQosBpDestPort_Type = InetPortNumber
_CabhPriorityQosBpDestPort_Object = MibTableColumn
cabhPriorityQosBpDestPort = _CabhPriorityQosBpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1, 4),
    _CabhPriorityQosBpDestPort_Type()
)
cabhPriorityQosBpDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestPort.setStatus("current")


class _CabhPriorityQosBpDestIpPortPriority_Type(Unsigned32):
    """Custom type cabhPriorityQosBpDestIpPortPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CabhPriorityQosBpDestIpPortPriority_Type.__name__ = "Unsigned32"
_CabhPriorityQosBpDestIpPortPriority_Object = MibTableColumn
cabhPriorityQosBpDestIpPortPriority = _CabhPriorityQosBpDestIpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 2, 2, 1, 5),
    _CabhPriorityQosBpDestIpPortPriority_Type()
)
cabhPriorityQosBpDestIpPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosBpDestIpPortPriority.setStatus("current")
_CabhPriorityQosPs_ObjectIdentity = ObjectIdentity
cabhPriorityQosPs = _CabhPriorityQosPs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 3)
)
_CabhPriorityQosPsIfAttribTable_Object = MibTable
cabhPriorityQosPsIfAttribTable = _CabhPriorityQosPsIfAttribTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cabhPriorityQosPsIfAttribTable.setStatus("current")
_CabhPriorityQosPsIfAttribEntry_Object = MibTableRow
cabhPriorityQosPsIfAttribEntry = _CabhPriorityQosPsIfAttribEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 3, 1, 1)
)
cabhPriorityQosPsIfAttribEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cabhPriorityQosPsIfAttribEntry.setStatus("current")


class _CabhPriorityQosPsIfAttribIfNumPriorities_Type(Unsigned32):
    """Custom type cabhPriorityQosPsIfAttribIfNumPriorities based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CabhPriorityQosPsIfAttribIfNumPriorities_Type.__name__ = "Unsigned32"
_CabhPriorityQosPsIfAttribIfNumPriorities_Object = MibTableColumn
cabhPriorityQosPsIfAttribIfNumPriorities = _CabhPriorityQosPsIfAttribIfNumPriorities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 3, 1, 1, 1),
    _CabhPriorityQosPsIfAttribIfNumPriorities_Type()
)
cabhPriorityQosPsIfAttribIfNumPriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosPsIfAttribIfNumPriorities.setStatus("current")


class _CabhPriorityQosPsIfAttribIfNumQueues_Type(Unsigned32):
    """Custom type cabhPriorityQosPsIfAttribIfNumQueues based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CabhPriorityQosPsIfAttribIfNumQueues_Type.__name__ = "Unsigned32"
_CabhPriorityQosPsIfAttribIfNumQueues_Object = MibTableColumn
cabhPriorityQosPsIfAttribIfNumQueues = _CabhPriorityQosPsIfAttribIfNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 1, 1, 3, 1, 1, 2),
    _CabhPriorityQosPsIfAttribIfNumQueues_Type()
)
cabhPriorityQosPsIfAttribIfNumQueues.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPriorityQosPsIfAttribIfNumQueues.setStatus("current")
_CabhQosNotification_ObjectIdentity = ObjectIdentity
cabhQosNotification = _CabhQosNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 2)
)
_CabhPriorityQosNotification_ObjectIdentity = ObjectIdentity
cabhPriorityQosNotification = _CabhPriorityQosNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 2, 1)
)
_CabhQosConformance_ObjectIdentity = ObjectIdentity
cabhQosConformance = _CabhQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3)
)
_CabhPriorityQosConformance_ObjectIdentity = ObjectIdentity
cabhPriorityQosConformance = _CabhPriorityQosConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3, 1)
)
_CabhPriorityQosGroups_ObjectIdentity = ObjectIdentity
cabhPriorityQosGroups = _CabhPriorityQosGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3, 1, 1)
)
_CabhPriorityQosCompliances_ObjectIdentity = ObjectIdentity
cabhPriorityQosCompliances = _CabhPriorityQosCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3, 1, 2)
)

# Managed Objects groups

cabhPriorityQosGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3, 1, 1, 1)
)
cabhPriorityQosGroup.setObjects(
      *(("CABH-QOS-MIB", "cabhPriorityQosMasterDefaultCHPriority"),
        ("CABH-QOS-MIB", "cabhPriorityQosMasterRowStatus"),
        ("CABH-QOS-MIB", "cabhPriorityQosSetToFactory"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpIpAddrType"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpIpAddr"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpApplicationId"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpDefaultCHPriority"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpIndex"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpDestIpAddrType"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpDestIpAddr"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpDestPort"),
        ("CABH-QOS-MIB", "cabhPriorityQosBpDestIpPortPriority"),
        ("CABH-QOS-MIB", "cabhPriorityQosPsIfAttribIfNumPriorities"),
        ("CABH-QOS-MIB", "cabhPriorityQosPsIfAttribIfNumQueues"))
)
if mibBuilder.loadTexts:
    cabhPriorityQosGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cabhPriorityQosCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 6, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cabhPriorityQosCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-QOS-MIB",
    **{"cabhQosMib": cabhQosMib,
       "cabhQosMibObjects": cabhQosMibObjects,
       "cabhPriorityQosMibObjects": cabhPriorityQosMibObjects,
       "cabhPriorityQosBase": cabhPriorityQosBase,
       "cabhPriorityQosMasterTable": cabhPriorityQosMasterTable,
       "cabhPriorityQosMasterEntry": cabhPriorityQosMasterEntry,
       "cabhPriorityQosMasterApplicationId": cabhPriorityQosMasterApplicationId,
       "cabhPriorityQosMasterDefaultCHPriority": cabhPriorityQosMasterDefaultCHPriority,
       "cabhPriorityQosMasterRowStatus": cabhPriorityQosMasterRowStatus,
       "cabhPriorityQosSetToFactory": cabhPriorityQosSetToFactory,
       "cabhPriorityQosBp": cabhPriorityQosBp,
       "cabhPriorityQosBpTable": cabhPriorityQosBpTable,
       "cabhPriorityQosBpEntry": cabhPriorityQosBpEntry,
       "cabhPriorityQosBpIpAddrType": cabhPriorityQosBpIpAddrType,
       "cabhPriorityQosBpIpAddr": cabhPriorityQosBpIpAddr,
       "cabhPriorityQosBpApplicationId": cabhPriorityQosBpApplicationId,
       "cabhPriorityQosBpDefaultCHPriority": cabhPriorityQosBpDefaultCHPriority,
       "cabhPriorityQosBpIndex": cabhPriorityQosBpIndex,
       "cabhPriorityQosBpDestTable": cabhPriorityQosBpDestTable,
       "cabhPriorityQosBpDestEntry": cabhPriorityQosBpDestEntry,
       "cabhPriorityQosBpDestIndex": cabhPriorityQosBpDestIndex,
       "cabhPriorityQosBpDestIpAddrType": cabhPriorityQosBpDestIpAddrType,
       "cabhPriorityQosBpDestIpAddr": cabhPriorityQosBpDestIpAddr,
       "cabhPriorityQosBpDestPort": cabhPriorityQosBpDestPort,
       "cabhPriorityQosBpDestIpPortPriority": cabhPriorityQosBpDestIpPortPriority,
       "cabhPriorityQosPs": cabhPriorityQosPs,
       "cabhPriorityQosPsIfAttribTable": cabhPriorityQosPsIfAttribTable,
       "cabhPriorityQosPsIfAttribEntry": cabhPriorityQosPsIfAttribEntry,
       "cabhPriorityQosPsIfAttribIfNumPriorities": cabhPriorityQosPsIfAttribIfNumPriorities,
       "cabhPriorityQosPsIfAttribIfNumQueues": cabhPriorityQosPsIfAttribIfNumQueues,
       "cabhQosNotification": cabhQosNotification,
       "cabhPriorityQosNotification": cabhPriorityQosNotification,
       "cabhQosConformance": cabhQosConformance,
       "cabhPriorityQosConformance": cabhPriorityQosConformance,
       "cabhPriorityQosGroups": cabhPriorityQosGroups,
       "cabhPriorityQosGroup": cabhPriorityQosGroup,
       "cabhPriorityQosCompliances": cabhPriorityQosCompliances,
       "cabhPriorityQosCompliance": cabhPriorityQosCompliance}
)
