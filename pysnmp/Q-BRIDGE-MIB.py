# SNMP MIB module (Q-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Q-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:58 2024
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

(dot1dBasePort,
 dot1dBasePortEntry,
 dot1dBridge) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry",
    "dot1dBridge")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

qBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7)
)
qBridgeMIB.setRevisions(
        ("2006-01-09 00:00",
         "1999-08-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


class VlanIndex(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


class VlanId(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class VlanIdOrAny(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )



class VlanIdOrNone(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )



class VlanIdOrAnyOrNone(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_QBridgeMIBObjects_ObjectIdentity = ObjectIdentity
qBridgeMIBObjects = _QBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1)
)
_Dot1qBase_ObjectIdentity = ObjectIdentity
dot1qBase = _Dot1qBase_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1)
)


class _Dot1qVlanVersionNumber_Type(Integer32):
    """Custom type dot1qVlanVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("version1", 1)
    )


_Dot1qVlanVersionNumber_Type.__name__ = "Integer32"
_Dot1qVlanVersionNumber_Object = MibScalar
dot1qVlanVersionNumber = _Dot1qVlanVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 1),
    _Dot1qVlanVersionNumber_Type()
)
dot1qVlanVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanVersionNumber.setStatus("current")
_Dot1qMaxVlanId_Type = VlanId
_Dot1qMaxVlanId_Object = MibScalar
dot1qMaxVlanId = _Dot1qMaxVlanId_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 2),
    _Dot1qMaxVlanId_Type()
)
dot1qMaxVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxVlanId.setStatus("current")
_Dot1qMaxSupportedVlans_Type = Unsigned32
_Dot1qMaxSupportedVlans_Object = MibScalar
dot1qMaxSupportedVlans = _Dot1qMaxSupportedVlans_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 3),
    _Dot1qMaxSupportedVlans_Type()
)
dot1qMaxSupportedVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qMaxSupportedVlans.setStatus("current")
_Dot1qNumVlans_Type = Unsigned32
_Dot1qNumVlans_Object = MibScalar
dot1qNumVlans = _Dot1qNumVlans_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 4),
    _Dot1qNumVlans_Type()
)
dot1qNumVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qNumVlans.setStatus("current")


class _Dot1qGvrpStatus_Type(EnabledStatus):
    """Custom type dot1qGvrpStatus based on EnabledStatus"""


_Dot1qGvrpStatus_Object = MibScalar
dot1qGvrpStatus = _Dot1qGvrpStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 1, 5),
    _Dot1qGvrpStatus_Type()
)
dot1qGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qGvrpStatus.setStatus("current")
_Dot1qTp_ObjectIdentity = ObjectIdentity
dot1qTp = _Dot1qTp_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2)
)
_Dot1qFdbTable_Object = MibTable
dot1qFdbTable = _Dot1qFdbTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot1qFdbTable.setStatus("current")
_Dot1qFdbEntry_Object = MibTableRow
dot1qFdbEntry = _Dot1qFdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1)
)
dot1qFdbEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
)
if mibBuilder.loadTexts:
    dot1qFdbEntry.setStatus("current")
_Dot1qFdbId_Type = Unsigned32
_Dot1qFdbId_Object = MibTableColumn
dot1qFdbId = _Dot1qFdbId_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 1),
    _Dot1qFdbId_Type()
)
dot1qFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qFdbId.setStatus("current")
_Dot1qFdbDynamicCount_Type = Counter32
_Dot1qFdbDynamicCount_Object = MibTableColumn
dot1qFdbDynamicCount = _Dot1qFdbDynamicCount_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 1, 1, 2),
    _Dot1qFdbDynamicCount_Type()
)
dot1qFdbDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qFdbDynamicCount.setStatus("current")
_Dot1qTpFdbTable_Object = MibTable
dot1qTpFdbTable = _Dot1qTpFdbTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot1qTpFdbTable.setStatus("current")
_Dot1qTpFdbEntry_Object = MibTableRow
dot1qTpFdbEntry = _Dot1qTpFdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1)
)
dot1qTpFdbEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    dot1qTpFdbEntry.setStatus("current")
_Dot1qTpFdbAddress_Type = MacAddress
_Dot1qTpFdbAddress_Object = MibTableColumn
dot1qTpFdbAddress = _Dot1qTpFdbAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 1),
    _Dot1qTpFdbAddress_Type()
)
dot1qTpFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qTpFdbAddress.setStatus("current")


class _Dot1qTpFdbPort_Type(Integer32):
    """Custom type dot1qTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qTpFdbPort_Type.__name__ = "Integer32"
_Dot1qTpFdbPort_Object = MibTableColumn
dot1qTpFdbPort = _Dot1qTpFdbPort_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 2),
    _Dot1qTpFdbPort_Type()
)
dot1qTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbPort.setStatus("current")


class _Dot1qTpFdbStatus_Type(Integer32):
    """Custom type dot1qTpFdbStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("learned", 3),
          ("mgmt", 5),
          ("other", 1),
          ("self", 4))
    )


_Dot1qTpFdbStatus_Type.__name__ = "Integer32"
_Dot1qTpFdbStatus_Object = MibTableColumn
dot1qTpFdbStatus = _Dot1qTpFdbStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 2, 1, 3),
    _Dot1qTpFdbStatus_Type()
)
dot1qTpFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpFdbStatus.setStatus("current")
_Dot1qTpGroupTable_Object = MibTable
dot1qTpGroupTable = _Dot1qTpGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot1qTpGroupTable.setStatus("current")
_Dot1qTpGroupEntry_Object = MibTableRow
dot1qTpGroupEntry = _Dot1qTpGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1)
)
dot1qTpGroupEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qTpGroupAddress"),
)
if mibBuilder.loadTexts:
    dot1qTpGroupEntry.setStatus("current")
_Dot1qTpGroupAddress_Type = MacAddress
_Dot1qTpGroupAddress_Object = MibTableColumn
dot1qTpGroupAddress = _Dot1qTpGroupAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 1),
    _Dot1qTpGroupAddress_Type()
)
dot1qTpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qTpGroupAddress.setStatus("current")
_Dot1qTpGroupEgressPorts_Type = PortList
_Dot1qTpGroupEgressPorts_Object = MibTableColumn
dot1qTpGroupEgressPorts = _Dot1qTpGroupEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 2),
    _Dot1qTpGroupEgressPorts_Type()
)
dot1qTpGroupEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpGroupEgressPorts.setStatus("current")
_Dot1qTpGroupLearnt_Type = PortList
_Dot1qTpGroupLearnt_Object = MibTableColumn
dot1qTpGroupLearnt = _Dot1qTpGroupLearnt_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 3, 1, 3),
    _Dot1qTpGroupLearnt_Type()
)
dot1qTpGroupLearnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpGroupLearnt.setStatus("current")
_Dot1qForwardAllTable_Object = MibTable
dot1qForwardAllTable = _Dot1qForwardAllTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dot1qForwardAllTable.setStatus("current")
_Dot1qForwardAllEntry_Object = MibTableRow
dot1qForwardAllEntry = _Dot1qForwardAllEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1)
)
dot1qForwardAllEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qForwardAllEntry.setStatus("current")
_Dot1qForwardAllPorts_Type = PortList
_Dot1qForwardAllPorts_Object = MibTableColumn
dot1qForwardAllPorts = _Dot1qForwardAllPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 1),
    _Dot1qForwardAllPorts_Type()
)
dot1qForwardAllPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qForwardAllPorts.setStatus("current")
_Dot1qForwardAllStaticPorts_Type = PortList
_Dot1qForwardAllStaticPorts_Object = MibTableColumn
dot1qForwardAllStaticPorts = _Dot1qForwardAllStaticPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 2),
    _Dot1qForwardAllStaticPorts_Type()
)
dot1qForwardAllStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qForwardAllStaticPorts.setStatus("current")
_Dot1qForwardAllForbiddenPorts_Type = PortList
_Dot1qForwardAllForbiddenPorts_Object = MibTableColumn
dot1qForwardAllForbiddenPorts = _Dot1qForwardAllForbiddenPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 4, 1, 3),
    _Dot1qForwardAllForbiddenPorts_Type()
)
dot1qForwardAllForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qForwardAllForbiddenPorts.setStatus("current")
_Dot1qForwardUnregisteredTable_Object = MibTable
dot1qForwardUnregisteredTable = _Dot1qForwardUnregisteredTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5)
)
if mibBuilder.loadTexts:
    dot1qForwardUnregisteredTable.setStatus("current")
_Dot1qForwardUnregisteredEntry_Object = MibTableRow
dot1qForwardUnregisteredEntry = _Dot1qForwardUnregisteredEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1)
)
dot1qForwardUnregisteredEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qForwardUnregisteredEntry.setStatus("current")
_Dot1qForwardUnregisteredPorts_Type = PortList
_Dot1qForwardUnregisteredPorts_Object = MibTableColumn
dot1qForwardUnregisteredPorts = _Dot1qForwardUnregisteredPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 1),
    _Dot1qForwardUnregisteredPorts_Type()
)
dot1qForwardUnregisteredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qForwardUnregisteredPorts.setStatus("current")
_Dot1qForwardUnregisteredStaticPorts_Type = PortList
_Dot1qForwardUnregisteredStaticPorts_Object = MibTableColumn
dot1qForwardUnregisteredStaticPorts = _Dot1qForwardUnregisteredStaticPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 2),
    _Dot1qForwardUnregisteredStaticPorts_Type()
)
dot1qForwardUnregisteredStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qForwardUnregisteredStaticPorts.setStatus("current")
_Dot1qForwardUnregisteredForbiddenPorts_Type = PortList
_Dot1qForwardUnregisteredForbiddenPorts_Object = MibTableColumn
dot1qForwardUnregisteredForbiddenPorts = _Dot1qForwardUnregisteredForbiddenPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 2, 5, 1, 3),
    _Dot1qForwardUnregisteredForbiddenPorts_Type()
)
dot1qForwardUnregisteredForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qForwardUnregisteredForbiddenPorts.setStatus("current")
_Dot1qStatic_ObjectIdentity = ObjectIdentity
dot1qStatic = _Dot1qStatic_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3)
)
_Dot1qStaticUnicastTable_Object = MibTable
dot1qStaticUnicastTable = _Dot1qStaticUnicastTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dot1qStaticUnicastTable.setStatus("current")
_Dot1qStaticUnicastEntry_Object = MibTableRow
dot1qStaticUnicastEntry = _Dot1qStaticUnicastEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1)
)
dot1qStaticUnicastEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastAddress"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticUnicastReceivePort"),
)
if mibBuilder.loadTexts:
    dot1qStaticUnicastEntry.setStatus("current")
_Dot1qStaticUnicastAddress_Type = MacAddress
_Dot1qStaticUnicastAddress_Object = MibTableColumn
dot1qStaticUnicastAddress = _Dot1qStaticUnicastAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 1),
    _Dot1qStaticUnicastAddress_Type()
)
dot1qStaticUnicastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticUnicastAddress.setStatus("current")


class _Dot1qStaticUnicastReceivePort_Type(Integer32):
    """Custom type dot1qStaticUnicastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qStaticUnicastReceivePort_Type.__name__ = "Integer32"
_Dot1qStaticUnicastReceivePort_Object = MibTableColumn
dot1qStaticUnicastReceivePort = _Dot1qStaticUnicastReceivePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 2),
    _Dot1qStaticUnicastReceivePort_Type()
)
dot1qStaticUnicastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticUnicastReceivePort.setStatus("current")
_Dot1qStaticUnicastAllowedToGoTo_Type = PortList
_Dot1qStaticUnicastAllowedToGoTo_Object = MibTableColumn
dot1qStaticUnicastAllowedToGoTo = _Dot1qStaticUnicastAllowedToGoTo_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 3),
    _Dot1qStaticUnicastAllowedToGoTo_Type()
)
dot1qStaticUnicastAllowedToGoTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticUnicastAllowedToGoTo.setStatus("current")


class _Dot1qStaticUnicastStatus_Type(Integer32):
    """Custom type dot1qStaticUnicastStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1qStaticUnicastStatus_Type.__name__ = "Integer32"
_Dot1qStaticUnicastStatus_Object = MibTableColumn
dot1qStaticUnicastStatus = _Dot1qStaticUnicastStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 1, 1, 4),
    _Dot1qStaticUnicastStatus_Type()
)
dot1qStaticUnicastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticUnicastStatus.setStatus("current")
_Dot1qStaticMulticastTable_Object = MibTable
dot1qStaticMulticastTable = _Dot1qStaticMulticastTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastTable.setStatus("current")
_Dot1qStaticMulticastEntry_Object = MibTableRow
dot1qStaticMulticastEntry = _Dot1qStaticMulticastEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1)
)
dot1qStaticMulticastEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastAddress"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    dot1qStaticMulticastEntry.setStatus("current")
_Dot1qStaticMulticastAddress_Type = MacAddress
_Dot1qStaticMulticastAddress_Object = MibTableColumn
dot1qStaticMulticastAddress = _Dot1qStaticMulticastAddress_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 1),
    _Dot1qStaticMulticastAddress_Type()
)
dot1qStaticMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticMulticastAddress.setStatus("current")


class _Dot1qStaticMulticastReceivePort_Type(Integer32):
    """Custom type dot1qStaticMulticastReceivePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qStaticMulticastReceivePort_Type.__name__ = "Integer32"
_Dot1qStaticMulticastReceivePort_Object = MibTableColumn
dot1qStaticMulticastReceivePort = _Dot1qStaticMulticastReceivePort_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 2),
    _Dot1qStaticMulticastReceivePort_Type()
)
dot1qStaticMulticastReceivePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qStaticMulticastReceivePort.setStatus("current")
_Dot1qStaticMulticastStaticEgressPorts_Type = PortList
_Dot1qStaticMulticastStaticEgressPorts_Object = MibTableColumn
dot1qStaticMulticastStaticEgressPorts = _Dot1qStaticMulticastStaticEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 3),
    _Dot1qStaticMulticastStaticEgressPorts_Type()
)
dot1qStaticMulticastStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastStaticEgressPorts.setStatus("current")
_Dot1qStaticMulticastForbiddenEgressPorts_Type = PortList
_Dot1qStaticMulticastForbiddenEgressPorts_Object = MibTableColumn
dot1qStaticMulticastForbiddenEgressPorts = _Dot1qStaticMulticastForbiddenEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 4),
    _Dot1qStaticMulticastForbiddenEgressPorts_Type()
)
dot1qStaticMulticastForbiddenEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastForbiddenEgressPorts.setStatus("current")


class _Dot1qStaticMulticastStatus_Type(Integer32):
    """Custom type dot1qStaticMulticastStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("deleteOnReset", 4),
          ("deleteOnTimeout", 5),
          ("invalid", 2),
          ("other", 1),
          ("permanent", 3))
    )


_Dot1qStaticMulticastStatus_Type.__name__ = "Integer32"
_Dot1qStaticMulticastStatus_Object = MibTableColumn
dot1qStaticMulticastStatus = _Dot1qStaticMulticastStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 3, 2, 1, 5),
    _Dot1qStaticMulticastStatus_Type()
)
dot1qStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qStaticMulticastStatus.setStatus("current")
_Dot1qVlan_ObjectIdentity = ObjectIdentity
dot1qVlan = _Dot1qVlan_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4)
)
_Dot1qVlanNumDeletes_Type = Counter32
_Dot1qVlanNumDeletes_Object = MibScalar
dot1qVlanNumDeletes = _Dot1qVlanNumDeletes_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 1),
    _Dot1qVlanNumDeletes_Type()
)
dot1qVlanNumDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanNumDeletes.setStatus("current")
_Dot1qVlanCurrentTable_Object = MibTable
dot1qVlanCurrentTable = _Dot1qVlanCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentTable.setStatus("current")
_Dot1qVlanCurrentEntry_Object = MibTableRow
dot1qVlanCurrentEntry = _Dot1qVlanCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1)
)
dot1qVlanCurrentEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanTimeMark"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanCurrentEntry.setStatus("current")
_Dot1qVlanTimeMark_Type = TimeFilter
_Dot1qVlanTimeMark_Object = MibTableColumn
dot1qVlanTimeMark = _Dot1qVlanTimeMark_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 1),
    _Dot1qVlanTimeMark_Type()
)
dot1qVlanTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanTimeMark.setStatus("current")
_Dot1qVlanIndex_Type = VlanIndex
_Dot1qVlanIndex_Object = MibTableColumn
dot1qVlanIndex = _Dot1qVlanIndex_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 2),
    _Dot1qVlanIndex_Type()
)
dot1qVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qVlanIndex.setStatus("current")
_Dot1qVlanFdbId_Type = Unsigned32
_Dot1qVlanFdbId_Object = MibTableColumn
dot1qVlanFdbId = _Dot1qVlanFdbId_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 3),
    _Dot1qVlanFdbId_Type()
)
dot1qVlanFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanFdbId.setStatus("current")
_Dot1qVlanCurrentEgressPorts_Type = PortList
_Dot1qVlanCurrentEgressPorts_Object = MibTableColumn
dot1qVlanCurrentEgressPorts = _Dot1qVlanCurrentEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 4),
    _Dot1qVlanCurrentEgressPorts_Type()
)
dot1qVlanCurrentEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCurrentEgressPorts.setStatus("current")
_Dot1qVlanCurrentUntaggedPorts_Type = PortList
_Dot1qVlanCurrentUntaggedPorts_Object = MibTableColumn
dot1qVlanCurrentUntaggedPorts = _Dot1qVlanCurrentUntaggedPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 5),
    _Dot1qVlanCurrentUntaggedPorts_Type()
)
dot1qVlanCurrentUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCurrentUntaggedPorts.setStatus("current")


class _Dot1qVlanStatus_Type(Integer32):
    """Custom type dot1qVlanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamicGvrp", 3),
          ("other", 1),
          ("permanent", 2))
    )


_Dot1qVlanStatus_Type.__name__ = "Integer32"
_Dot1qVlanStatus_Object = MibTableColumn
dot1qVlanStatus = _Dot1qVlanStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 6),
    _Dot1qVlanStatus_Type()
)
dot1qVlanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanStatus.setStatus("current")
_Dot1qVlanCreationTime_Type = TimeTicks
_Dot1qVlanCreationTime_Object = MibTableColumn
dot1qVlanCreationTime = _Dot1qVlanCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 2, 1, 7),
    _Dot1qVlanCreationTime_Type()
)
dot1qVlanCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qVlanCreationTime.setStatus("current")
_Dot1qVlanStaticTable_Object = MibTable
dot1qVlanStaticTable = _Dot1qVlanStaticTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dot1qVlanStaticTable.setStatus("current")
_Dot1qVlanStaticEntry_Object = MibTableRow
dot1qVlanStaticEntry = _Dot1qVlanStaticEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1)
)
dot1qVlanStaticEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qVlanStaticEntry.setStatus("current")


class _Dot1qVlanStaticName_Type(SnmpAdminString):
    """Custom type dot1qVlanStaticName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Dot1qVlanStaticName_Type.__name__ = "SnmpAdminString"
_Dot1qVlanStaticName_Object = MibTableColumn
dot1qVlanStaticName = _Dot1qVlanStaticName_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 1),
    _Dot1qVlanStaticName_Type()
)
dot1qVlanStaticName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticName.setStatus("current")
_Dot1qVlanStaticEgressPorts_Type = PortList
_Dot1qVlanStaticEgressPorts_Object = MibTableColumn
dot1qVlanStaticEgressPorts = _Dot1qVlanStaticEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 2),
    _Dot1qVlanStaticEgressPorts_Type()
)
dot1qVlanStaticEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticEgressPorts.setStatus("current")
_Dot1qVlanForbiddenEgressPorts_Type = PortList
_Dot1qVlanForbiddenEgressPorts_Object = MibTableColumn
dot1qVlanForbiddenEgressPorts = _Dot1qVlanForbiddenEgressPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 3),
    _Dot1qVlanForbiddenEgressPorts_Type()
)
dot1qVlanForbiddenEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanForbiddenEgressPorts.setStatus("current")
_Dot1qVlanStaticUntaggedPorts_Type = PortList
_Dot1qVlanStaticUntaggedPorts_Object = MibTableColumn
dot1qVlanStaticUntaggedPorts = _Dot1qVlanStaticUntaggedPorts_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 4),
    _Dot1qVlanStaticUntaggedPorts_Type()
)
dot1qVlanStaticUntaggedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticUntaggedPorts.setStatus("current")
_Dot1qVlanStaticRowStatus_Type = RowStatus
_Dot1qVlanStaticRowStatus_Object = MibTableColumn
dot1qVlanStaticRowStatus = _Dot1qVlanStaticRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 3, 1, 5),
    _Dot1qVlanStaticRowStatus_Type()
)
dot1qVlanStaticRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qVlanStaticRowStatus.setStatus("current")


class _Dot1qNextFreeLocalVlanIndex_Type(Integer32):
    """Custom type dot1qNextFreeLocalVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(4096, 2147483647),
    )


_Dot1qNextFreeLocalVlanIndex_Type.__name__ = "Integer32"
_Dot1qNextFreeLocalVlanIndex_Object = MibScalar
dot1qNextFreeLocalVlanIndex = _Dot1qNextFreeLocalVlanIndex_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 4),
    _Dot1qNextFreeLocalVlanIndex_Type()
)
dot1qNextFreeLocalVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qNextFreeLocalVlanIndex.setStatus("current")
_Dot1qPortVlanTable_Object = MibTable
dot1qPortVlanTable = _Dot1qPortVlanTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dot1qPortVlanTable.setStatus("current")
_Dot1qPortVlanEntry_Object = MibTableRow
dot1qPortVlanEntry = _Dot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    dot1qPortVlanEntry.setStatus("current")


class _Dot1qPvid_Type(VlanIndex):
    """Custom type dot1qPvid based on VlanIndex"""
    defaultValue = 1


_Dot1qPvid_Object = MibTableColumn
dot1qPvid = _Dot1qPvid_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 1),
    _Dot1qPvid_Type()
)
dot1qPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPvid.setStatus("current")


class _Dot1qPortAcceptableFrameTypes_Type(Integer32):
    """Custom type dot1qPortAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_Dot1qPortAcceptableFrameTypes_Type.__name__ = "Integer32"
_Dot1qPortAcceptableFrameTypes_Object = MibTableColumn
dot1qPortAcceptableFrameTypes = _Dot1qPortAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 2),
    _Dot1qPortAcceptableFrameTypes_Type()
)
dot1qPortAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortAcceptableFrameTypes.setStatus("current")


class _Dot1qPortIngressFiltering_Type(TruthValue):
    """Custom type dot1qPortIngressFiltering based on TruthValue"""


_Dot1qPortIngressFiltering_Object = MibTableColumn
dot1qPortIngressFiltering = _Dot1qPortIngressFiltering_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 3),
    _Dot1qPortIngressFiltering_Type()
)
dot1qPortIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortIngressFiltering.setStatus("current")


class _Dot1qPortGvrpStatus_Type(EnabledStatus):
    """Custom type dot1qPortGvrpStatus based on EnabledStatus"""


_Dot1qPortGvrpStatus_Object = MibTableColumn
dot1qPortGvrpStatus = _Dot1qPortGvrpStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 4),
    _Dot1qPortGvrpStatus_Type()
)
dot1qPortGvrpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortGvrpStatus.setStatus("current")
_Dot1qPortGvrpFailedRegistrations_Type = Counter32
_Dot1qPortGvrpFailedRegistrations_Object = MibTableColumn
dot1qPortGvrpFailedRegistrations = _Dot1qPortGvrpFailedRegistrations_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 5),
    _Dot1qPortGvrpFailedRegistrations_Type()
)
dot1qPortGvrpFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpFailedRegistrations.setStatus("current")
_Dot1qPortGvrpLastPduOrigin_Type = MacAddress
_Dot1qPortGvrpLastPduOrigin_Object = MibTableColumn
dot1qPortGvrpLastPduOrigin = _Dot1qPortGvrpLastPduOrigin_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 6),
    _Dot1qPortGvrpLastPduOrigin_Type()
)
dot1qPortGvrpLastPduOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qPortGvrpLastPduOrigin.setStatus("current")


class _Dot1qPortRestrictedVlanRegistration_Type(TruthValue):
    """Custom type dot1qPortRestrictedVlanRegistration based on TruthValue"""


_Dot1qPortRestrictedVlanRegistration_Object = MibTableColumn
dot1qPortRestrictedVlanRegistration = _Dot1qPortRestrictedVlanRegistration_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 5, 1, 7),
    _Dot1qPortRestrictedVlanRegistration_Type()
)
dot1qPortRestrictedVlanRegistration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qPortRestrictedVlanRegistration.setStatus("current")
_Dot1qPortVlanStatisticsTable_Object = MibTable
dot1qPortVlanStatisticsTable = _Dot1qPortVlanStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6)
)
if mibBuilder.loadTexts:
    dot1qPortVlanStatisticsTable.setStatus("current")
_Dot1qPortVlanStatisticsEntry_Object = MibTableRow
dot1qPortVlanStatisticsEntry = _Dot1qPortVlanStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1)
)
dot1qPortVlanStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qPortVlanStatisticsEntry.setStatus("current")
_Dot1qTpVlanPortInFrames_Type = Counter32
_Dot1qTpVlanPortInFrames_Object = MibTableColumn
dot1qTpVlanPortInFrames = _Dot1qTpVlanPortInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 1),
    _Dot1qTpVlanPortInFrames_Type()
)
dot1qTpVlanPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortInFrames.setStatus("current")
_Dot1qTpVlanPortOutFrames_Type = Counter32
_Dot1qTpVlanPortOutFrames_Object = MibTableColumn
dot1qTpVlanPortOutFrames = _Dot1qTpVlanPortOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 2),
    _Dot1qTpVlanPortOutFrames_Type()
)
dot1qTpVlanPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortOutFrames.setStatus("current")
_Dot1qTpVlanPortInDiscards_Type = Counter32
_Dot1qTpVlanPortInDiscards_Object = MibTableColumn
dot1qTpVlanPortInDiscards = _Dot1qTpVlanPortInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 3),
    _Dot1qTpVlanPortInDiscards_Type()
)
dot1qTpVlanPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortInDiscards.setStatus("current")
_Dot1qTpVlanPortInOverflowFrames_Type = Counter32
_Dot1qTpVlanPortInOverflowFrames_Object = MibTableColumn
dot1qTpVlanPortInOverflowFrames = _Dot1qTpVlanPortInOverflowFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 4),
    _Dot1qTpVlanPortInOverflowFrames_Type()
)
dot1qTpVlanPortInOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortInOverflowFrames.setStatus("current")
_Dot1qTpVlanPortOutOverflowFrames_Type = Counter32
_Dot1qTpVlanPortOutOverflowFrames_Object = MibTableColumn
dot1qTpVlanPortOutOverflowFrames = _Dot1qTpVlanPortOutOverflowFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 5),
    _Dot1qTpVlanPortOutOverflowFrames_Type()
)
dot1qTpVlanPortOutOverflowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortOutOverflowFrames.setStatus("current")
_Dot1qTpVlanPortInOverflowDiscards_Type = Counter32
_Dot1qTpVlanPortInOverflowDiscards_Object = MibTableColumn
dot1qTpVlanPortInOverflowDiscards = _Dot1qTpVlanPortInOverflowDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 6, 1, 6),
    _Dot1qTpVlanPortInOverflowDiscards_Type()
)
dot1qTpVlanPortInOverflowDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortInOverflowDiscards.setStatus("current")
_Dot1qPortVlanHCStatisticsTable_Object = MibTable
dot1qPortVlanHCStatisticsTable = _Dot1qPortVlanHCStatisticsTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7)
)
if mibBuilder.loadTexts:
    dot1qPortVlanHCStatisticsTable.setStatus("current")
_Dot1qPortVlanHCStatisticsEntry_Object = MibTableRow
dot1qPortVlanHCStatisticsEntry = _Dot1qPortVlanHCStatisticsEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1)
)
dot1qPortVlanHCStatisticsEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    dot1qPortVlanHCStatisticsEntry.setStatus("current")
_Dot1qTpVlanPortHCInFrames_Type = Counter64
_Dot1qTpVlanPortHCInFrames_Object = MibTableColumn
dot1qTpVlanPortHCInFrames = _Dot1qTpVlanPortHCInFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 1),
    _Dot1qTpVlanPortHCInFrames_Type()
)
dot1qTpVlanPortHCInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortHCInFrames.setStatus("current")
_Dot1qTpVlanPortHCOutFrames_Type = Counter64
_Dot1qTpVlanPortHCOutFrames_Object = MibTableColumn
dot1qTpVlanPortHCOutFrames = _Dot1qTpVlanPortHCOutFrames_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 2),
    _Dot1qTpVlanPortHCOutFrames_Type()
)
dot1qTpVlanPortHCOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortHCOutFrames.setStatus("current")
_Dot1qTpVlanPortHCInDiscards_Type = Counter64
_Dot1qTpVlanPortHCInDiscards_Object = MibTableColumn
dot1qTpVlanPortHCInDiscards = _Dot1qTpVlanPortHCInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 7, 1, 3),
    _Dot1qTpVlanPortHCInDiscards_Type()
)
dot1qTpVlanPortHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1qTpVlanPortHCInDiscards.setStatus("current")
_Dot1qLearningConstraintsTable_Object = MibTable
dot1qLearningConstraintsTable = _Dot1qLearningConstraintsTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8)
)
if mibBuilder.loadTexts:
    dot1qLearningConstraintsTable.setStatus("current")
_Dot1qLearningConstraintsEntry_Object = MibTableRow
dot1qLearningConstraintsEntry = _Dot1qLearningConstraintsEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1)
)
dot1qLearningConstraintsEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qConstraintVlan"),
    (0, "Q-BRIDGE-MIB", "dot1qConstraintSet"),
)
if mibBuilder.loadTexts:
    dot1qLearningConstraintsEntry.setStatus("current")
_Dot1qConstraintVlan_Type = VlanIndex
_Dot1qConstraintVlan_Object = MibTableColumn
dot1qConstraintVlan = _Dot1qConstraintVlan_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 1),
    _Dot1qConstraintVlan_Type()
)
dot1qConstraintVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qConstraintVlan.setStatus("current")


class _Dot1qConstraintSet_Type(Integer32):
    """Custom type dot1qConstraintSet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qConstraintSet_Type.__name__ = "Integer32"
_Dot1qConstraintSet_Object = MibTableColumn
dot1qConstraintSet = _Dot1qConstraintSet_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 2),
    _Dot1qConstraintSet_Type()
)
dot1qConstraintSet.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1qConstraintSet.setStatus("current")


class _Dot1qConstraintType_Type(Integer32):
    """Custom type dot1qConstraintType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_Dot1qConstraintType_Type.__name__ = "Integer32"
_Dot1qConstraintType_Object = MibTableColumn
dot1qConstraintType = _Dot1qConstraintType_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 3),
    _Dot1qConstraintType_Type()
)
dot1qConstraintType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qConstraintType.setStatus("current")
_Dot1qConstraintStatus_Type = RowStatus
_Dot1qConstraintStatus_Object = MibTableColumn
dot1qConstraintStatus = _Dot1qConstraintStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 8, 1, 4),
    _Dot1qConstraintStatus_Type()
)
dot1qConstraintStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1qConstraintStatus.setStatus("current")


class _Dot1qConstraintSetDefault_Type(Integer32):
    """Custom type dot1qConstraintSetDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot1qConstraintSetDefault_Type.__name__ = "Integer32"
_Dot1qConstraintSetDefault_Object = MibScalar
dot1qConstraintSetDefault = _Dot1qConstraintSetDefault_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 9),
    _Dot1qConstraintSetDefault_Type()
)
dot1qConstraintSetDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qConstraintSetDefault.setStatus("current")


class _Dot1qConstraintTypeDefault_Type(Integer32):
    """Custom type dot1qConstraintTypeDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_Dot1qConstraintTypeDefault_Type.__name__ = "Integer32"
_Dot1qConstraintTypeDefault_Object = MibScalar
dot1qConstraintTypeDefault = _Dot1qConstraintTypeDefault_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 4, 10),
    _Dot1qConstraintTypeDefault_Type()
)
dot1qConstraintTypeDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1qConstraintTypeDefault.setStatus("current")
_Dot1vProtocol_ObjectIdentity = ObjectIdentity
dot1vProtocol = _Dot1vProtocol_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5)
)
_Dot1vProtocolGroupTable_Object = MibTable
dot1vProtocolGroupTable = _Dot1vProtocolGroupTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    dot1vProtocolGroupTable.setStatus("current")
_Dot1vProtocolGroupEntry_Object = MibTableRow
dot1vProtocolGroupEntry = _Dot1vProtocolGroupEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1)
)
dot1vProtocolGroupEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1vProtocolTemplateFrameType"),
    (0, "Q-BRIDGE-MIB", "dot1vProtocolTemplateProtocolValue"),
)
if mibBuilder.loadTexts:
    dot1vProtocolGroupEntry.setStatus("current")


class _Dot1vProtocolTemplateFrameType_Type(Integer32):
    """Custom type dot1vProtocolTemplateFrameType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("llcOther", 5),
          ("rfc1042", 2),
          ("snap8021H", 3),
          ("snapOther", 4))
    )


_Dot1vProtocolTemplateFrameType_Type.__name__ = "Integer32"
_Dot1vProtocolTemplateFrameType_Object = MibTableColumn
dot1vProtocolTemplateFrameType = _Dot1vProtocolTemplateFrameType_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 1),
    _Dot1vProtocolTemplateFrameType_Type()
)
dot1vProtocolTemplateFrameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolTemplateFrameType.setStatus("current")


class _Dot1vProtocolTemplateProtocolValue_Type(OctetString):
    """Custom type dot1vProtocolTemplateProtocolValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
        ValueSizeConstraint(5, 5),
    )


_Dot1vProtocolTemplateProtocolValue_Type.__name__ = "OctetString"
_Dot1vProtocolTemplateProtocolValue_Object = MibTableColumn
dot1vProtocolTemplateProtocolValue = _Dot1vProtocolTemplateProtocolValue_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 2),
    _Dot1vProtocolTemplateProtocolValue_Type()
)
dot1vProtocolTemplateProtocolValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolTemplateProtocolValue.setStatus("current")


class _Dot1vProtocolGroupId_Type(Integer32):
    """Custom type dot1vProtocolGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Dot1vProtocolGroupId_Type.__name__ = "Integer32"
_Dot1vProtocolGroupId_Object = MibTableColumn
dot1vProtocolGroupId = _Dot1vProtocolGroupId_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 3),
    _Dot1vProtocolGroupId_Type()
)
dot1vProtocolGroupId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolGroupId.setStatus("current")
_Dot1vProtocolGroupRowStatus_Type = RowStatus
_Dot1vProtocolGroupRowStatus_Object = MibTableColumn
dot1vProtocolGroupRowStatus = _Dot1vProtocolGroupRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 1, 1, 4),
    _Dot1vProtocolGroupRowStatus_Type()
)
dot1vProtocolGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolGroupRowStatus.setStatus("current")
_Dot1vProtocolPortTable_Object = MibTable
dot1vProtocolPortTable = _Dot1vProtocolPortTable_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dot1vProtocolPortTable.setStatus("current")
_Dot1vProtocolPortEntry_Object = MibTableRow
dot1vProtocolPortEntry = _Dot1vProtocolPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1)
)
dot1vProtocolPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1vProtocolPortGroupId"),
)
if mibBuilder.loadTexts:
    dot1vProtocolPortEntry.setStatus("current")


class _Dot1vProtocolPortGroupId_Type(Integer32):
    """Custom type dot1vProtocolPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Dot1vProtocolPortGroupId_Type.__name__ = "Integer32"
_Dot1vProtocolPortGroupId_Object = MibTableColumn
dot1vProtocolPortGroupId = _Dot1vProtocolPortGroupId_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 1),
    _Dot1vProtocolPortGroupId_Type()
)
dot1vProtocolPortGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1vProtocolPortGroupId.setStatus("current")


class _Dot1vProtocolPortGroupVid_Type(Integer32):
    """Custom type dot1vProtocolPortGroupVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Dot1vProtocolPortGroupVid_Type.__name__ = "Integer32"
_Dot1vProtocolPortGroupVid_Object = MibTableColumn
dot1vProtocolPortGroupVid = _Dot1vProtocolPortGroupVid_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 2),
    _Dot1vProtocolPortGroupVid_Type()
)
dot1vProtocolPortGroupVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolPortGroupVid.setStatus("current")
_Dot1vProtocolPortRowStatus_Type = RowStatus
_Dot1vProtocolPortRowStatus_Object = MibTableColumn
dot1vProtocolPortRowStatus = _Dot1vProtocolPortRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 17, 7, 1, 5, 2, 1, 3),
    _Dot1vProtocolPortRowStatus_Type()
)
dot1vProtocolPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot1vProtocolPortRowStatus.setStatus("current")
_QBridgeConformance_ObjectIdentity = ObjectIdentity
qBridgeConformance = _QBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 2)
)
_QBridgeGroups_ObjectIdentity = ObjectIdentity
qBridgeGroups = _QBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1)
)
_QBridgeCompliances_ObjectIdentity = ObjectIdentity
qBridgeCompliances = _QBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("Q-BRIDGE-MIB",
     "dot1qPortVlanEntry")
)
dot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

qBridgeBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 1)
)
qBridgeBaseGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qVlanVersionNumber"),
        ("Q-BRIDGE-MIB", "dot1qMaxVlanId"),
        ("Q-BRIDGE-MIB", "dot1qMaxSupportedVlans"),
        ("Q-BRIDGE-MIB", "dot1qNumVlans"),
        ("Q-BRIDGE-MIB", "dot1qGvrpStatus"))
)
if mibBuilder.loadTexts:
    qBridgeBaseGroup.setStatus("current")

qBridgeFdbUnicastGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 2)
)
qBridgeFdbUnicastGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qFdbDynamicCount"),
        ("Q-BRIDGE-MIB", "dot1qTpFdbPort"),
        ("Q-BRIDGE-MIB", "dot1qTpFdbStatus"))
)
if mibBuilder.loadTexts:
    qBridgeFdbUnicastGroup.setStatus("current")

qBridgeFdbMulticastGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 3)
)
qBridgeFdbMulticastGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qTpGroupEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qTpGroupLearnt"))
)
if mibBuilder.loadTexts:
    qBridgeFdbMulticastGroup.setStatus("current")

qBridgeServiceRequirementsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 4)
)
qBridgeServiceRequirementsGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qForwardAllPorts"),
        ("Q-BRIDGE-MIB", "dot1qForwardAllStaticPorts"),
        ("Q-BRIDGE-MIB", "dot1qForwardAllForbiddenPorts"),
        ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredPorts"),
        ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredStaticPorts"),
        ("Q-BRIDGE-MIB", "dot1qForwardUnregisteredForbiddenPorts"))
)
if mibBuilder.loadTexts:
    qBridgeServiceRequirementsGroup.setStatus("current")

qBridgeFdbStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 5)
)
qBridgeFdbStaticGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qStaticUnicastAllowedToGoTo"),
        ("Q-BRIDGE-MIB", "dot1qStaticUnicastStatus"),
        ("Q-BRIDGE-MIB", "dot1qStaticMulticastStaticEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qStaticMulticastForbiddenEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qStaticMulticastStatus"))
)
if mibBuilder.loadTexts:
    qBridgeFdbStaticGroup.setStatus("current")

qBridgeVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 6)
)
qBridgeVlanGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qVlanNumDeletes"),
        ("Q-BRIDGE-MIB", "dot1qVlanFdbId"),
        ("Q-BRIDGE-MIB", "dot1qVlanCurrentEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qVlanCurrentUntaggedPorts"),
        ("Q-BRIDGE-MIB", "dot1qVlanStatus"),
        ("Q-BRIDGE-MIB", "dot1qVlanCreationTime"))
)
if mibBuilder.loadTexts:
    qBridgeVlanGroup.setStatus("current")

qBridgeVlanStaticGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 7)
)
qBridgeVlanStaticGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qVlanStaticName"),
        ("Q-BRIDGE-MIB", "dot1qVlanStaticEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qVlanForbiddenEgressPorts"),
        ("Q-BRIDGE-MIB", "dot1qVlanStaticUntaggedPorts"),
        ("Q-BRIDGE-MIB", "dot1qVlanStaticRowStatus"),
        ("Q-BRIDGE-MIB", "dot1qNextFreeLocalVlanIndex"))
)
if mibBuilder.loadTexts:
    qBridgeVlanStaticGroup.setStatus("current")

qBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 8)
)
qBridgePortGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qPvid"),
        ("Q-BRIDGE-MIB", "dot1qPortAcceptableFrameTypes"),
        ("Q-BRIDGE-MIB", "dot1qPortIngressFiltering"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpStatus"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpFailedRegistrations"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpLastPduOrigin"))
)
if mibBuilder.loadTexts:
    qBridgePortGroup.setStatus("deprecated")

qBridgeVlanStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 9)
)
qBridgeVlanStatisticsGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qTpVlanPortInFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortOutFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortInDiscards"))
)
if mibBuilder.loadTexts:
    qBridgeVlanStatisticsGroup.setStatus("current")

qBridgeVlanStatisticsOverflowGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 10)
)
qBridgeVlanStatisticsOverflowGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortOutOverflowFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortInOverflowDiscards"))
)
if mibBuilder.loadTexts:
    qBridgeVlanStatisticsOverflowGroup.setStatus("current")

qBridgeVlanHCStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 11)
)
qBridgeVlanHCStatisticsGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCOutFrames"),
        ("Q-BRIDGE-MIB", "dot1qTpVlanPortHCInDiscards"))
)
if mibBuilder.loadTexts:
    qBridgeVlanHCStatisticsGroup.setStatus("current")

qBridgeLearningConstraintsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 12)
)
qBridgeLearningConstraintsGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qConstraintType"),
        ("Q-BRIDGE-MIB", "dot1qConstraintStatus"))
)
if mibBuilder.loadTexts:
    qBridgeLearningConstraintsGroup.setStatus("current")

qBridgeLearningConstraintDefaultGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 13)
)
qBridgeLearningConstraintDefaultGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qConstraintSetDefault"),
        ("Q-BRIDGE-MIB", "dot1qConstraintTypeDefault"))
)
if mibBuilder.loadTexts:
    qBridgeLearningConstraintDefaultGroup.setStatus("current")

qBridgeClassificationDeviceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 14)
)
qBridgeClassificationDeviceGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1vProtocolGroupId"),
        ("Q-BRIDGE-MIB", "dot1vProtocolGroupRowStatus"))
)
if mibBuilder.loadTexts:
    qBridgeClassificationDeviceGroup.setStatus("current")

qBridgeClassificationPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 15)
)
qBridgeClassificationPortGroup.setObjects(
      *(("Q-BRIDGE-MIB", "dot1vProtocolPortGroupVid"),
        ("Q-BRIDGE-MIB", "dot1vProtocolPortRowStatus"))
)
if mibBuilder.loadTexts:
    qBridgeClassificationPortGroup.setStatus("current")

qBridgePortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 1, 16)
)
qBridgePortGroup2.setObjects(
      *(("Q-BRIDGE-MIB", "dot1qPvid"),
        ("Q-BRIDGE-MIB", "dot1qPortAcceptableFrameTypes"),
        ("Q-BRIDGE-MIB", "dot1qPortIngressFiltering"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpStatus"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpFailedRegistrations"),
        ("Q-BRIDGE-MIB", "dot1qPortGvrpLastPduOrigin"),
        ("Q-BRIDGE-MIB", "dot1qPortRestrictedVlanRegistration"))
)
if mibBuilder.loadTexts:
    qBridgePortGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    qBridgeCompliance.setStatus(
        "deprecated"
    )

qBridgeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 17, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    qBridgeCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Q-BRIDGE-MIB",
    **{"PortList": PortList,
       "VlanIndex": VlanIndex,
       "VlanId": VlanId,
       "VlanIdOrAny": VlanIdOrAny,
       "VlanIdOrNone": VlanIdOrNone,
       "VlanIdOrAnyOrNone": VlanIdOrAnyOrNone,
       "qBridgeMIB": qBridgeMIB,
       "qBridgeMIBObjects": qBridgeMIBObjects,
       "dot1qBase": dot1qBase,
       "dot1qVlanVersionNumber": dot1qVlanVersionNumber,
       "dot1qMaxVlanId": dot1qMaxVlanId,
       "dot1qMaxSupportedVlans": dot1qMaxSupportedVlans,
       "dot1qNumVlans": dot1qNumVlans,
       "dot1qGvrpStatus": dot1qGvrpStatus,
       "dot1qTp": dot1qTp,
       "dot1qFdbTable": dot1qFdbTable,
       "dot1qFdbEntry": dot1qFdbEntry,
       "dot1qFdbId": dot1qFdbId,
       "dot1qFdbDynamicCount": dot1qFdbDynamicCount,
       "dot1qTpFdbTable": dot1qTpFdbTable,
       "dot1qTpFdbEntry": dot1qTpFdbEntry,
       "dot1qTpFdbAddress": dot1qTpFdbAddress,
       "dot1qTpFdbPort": dot1qTpFdbPort,
       "dot1qTpFdbStatus": dot1qTpFdbStatus,
       "dot1qTpGroupTable": dot1qTpGroupTable,
       "dot1qTpGroupEntry": dot1qTpGroupEntry,
       "dot1qTpGroupAddress": dot1qTpGroupAddress,
       "dot1qTpGroupEgressPorts": dot1qTpGroupEgressPorts,
       "dot1qTpGroupLearnt": dot1qTpGroupLearnt,
       "dot1qForwardAllTable": dot1qForwardAllTable,
       "dot1qForwardAllEntry": dot1qForwardAllEntry,
       "dot1qForwardAllPorts": dot1qForwardAllPorts,
       "dot1qForwardAllStaticPorts": dot1qForwardAllStaticPorts,
       "dot1qForwardAllForbiddenPorts": dot1qForwardAllForbiddenPorts,
       "dot1qForwardUnregisteredTable": dot1qForwardUnregisteredTable,
       "dot1qForwardUnregisteredEntry": dot1qForwardUnregisteredEntry,
       "dot1qForwardUnregisteredPorts": dot1qForwardUnregisteredPorts,
       "dot1qForwardUnregisteredStaticPorts": dot1qForwardUnregisteredStaticPorts,
       "dot1qForwardUnregisteredForbiddenPorts": dot1qForwardUnregisteredForbiddenPorts,
       "dot1qStatic": dot1qStatic,
       "dot1qStaticUnicastTable": dot1qStaticUnicastTable,
       "dot1qStaticUnicastEntry": dot1qStaticUnicastEntry,
       "dot1qStaticUnicastAddress": dot1qStaticUnicastAddress,
       "dot1qStaticUnicastReceivePort": dot1qStaticUnicastReceivePort,
       "dot1qStaticUnicastAllowedToGoTo": dot1qStaticUnicastAllowedToGoTo,
       "dot1qStaticUnicastStatus": dot1qStaticUnicastStatus,
       "dot1qStaticMulticastTable": dot1qStaticMulticastTable,
       "dot1qStaticMulticastEntry": dot1qStaticMulticastEntry,
       "dot1qStaticMulticastAddress": dot1qStaticMulticastAddress,
       "dot1qStaticMulticastReceivePort": dot1qStaticMulticastReceivePort,
       "dot1qStaticMulticastStaticEgressPorts": dot1qStaticMulticastStaticEgressPorts,
       "dot1qStaticMulticastForbiddenEgressPorts": dot1qStaticMulticastForbiddenEgressPorts,
       "dot1qStaticMulticastStatus": dot1qStaticMulticastStatus,
       "dot1qVlan": dot1qVlan,
       "dot1qVlanNumDeletes": dot1qVlanNumDeletes,
       "dot1qVlanCurrentTable": dot1qVlanCurrentTable,
       "dot1qVlanCurrentEntry": dot1qVlanCurrentEntry,
       "dot1qVlanTimeMark": dot1qVlanTimeMark,
       "dot1qVlanIndex": dot1qVlanIndex,
       "dot1qVlanFdbId": dot1qVlanFdbId,
       "dot1qVlanCurrentEgressPorts": dot1qVlanCurrentEgressPorts,
       "dot1qVlanCurrentUntaggedPorts": dot1qVlanCurrentUntaggedPorts,
       "dot1qVlanStatus": dot1qVlanStatus,
       "dot1qVlanCreationTime": dot1qVlanCreationTime,
       "dot1qVlanStaticTable": dot1qVlanStaticTable,
       "dot1qVlanStaticEntry": dot1qVlanStaticEntry,
       "dot1qVlanStaticName": dot1qVlanStaticName,
       "dot1qVlanStaticEgressPorts": dot1qVlanStaticEgressPorts,
       "dot1qVlanForbiddenEgressPorts": dot1qVlanForbiddenEgressPorts,
       "dot1qVlanStaticUntaggedPorts": dot1qVlanStaticUntaggedPorts,
       "dot1qVlanStaticRowStatus": dot1qVlanStaticRowStatus,
       "dot1qNextFreeLocalVlanIndex": dot1qNextFreeLocalVlanIndex,
       "dot1qPortVlanTable": dot1qPortVlanTable,
       "dot1qPortVlanEntry": dot1qPortVlanEntry,
       "dot1qPvid": dot1qPvid,
       "dot1qPortAcceptableFrameTypes": dot1qPortAcceptableFrameTypes,
       "dot1qPortIngressFiltering": dot1qPortIngressFiltering,
       "dot1qPortGvrpStatus": dot1qPortGvrpStatus,
       "dot1qPortGvrpFailedRegistrations": dot1qPortGvrpFailedRegistrations,
       "dot1qPortGvrpLastPduOrigin": dot1qPortGvrpLastPduOrigin,
       "dot1qPortRestrictedVlanRegistration": dot1qPortRestrictedVlanRegistration,
       "dot1qPortVlanStatisticsTable": dot1qPortVlanStatisticsTable,
       "dot1qPortVlanStatisticsEntry": dot1qPortVlanStatisticsEntry,
       "dot1qTpVlanPortInFrames": dot1qTpVlanPortInFrames,
       "dot1qTpVlanPortOutFrames": dot1qTpVlanPortOutFrames,
       "dot1qTpVlanPortInDiscards": dot1qTpVlanPortInDiscards,
       "dot1qTpVlanPortInOverflowFrames": dot1qTpVlanPortInOverflowFrames,
       "dot1qTpVlanPortOutOverflowFrames": dot1qTpVlanPortOutOverflowFrames,
       "dot1qTpVlanPortInOverflowDiscards": dot1qTpVlanPortInOverflowDiscards,
       "dot1qPortVlanHCStatisticsTable": dot1qPortVlanHCStatisticsTable,
       "dot1qPortVlanHCStatisticsEntry": dot1qPortVlanHCStatisticsEntry,
       "dot1qTpVlanPortHCInFrames": dot1qTpVlanPortHCInFrames,
       "dot1qTpVlanPortHCOutFrames": dot1qTpVlanPortHCOutFrames,
       "dot1qTpVlanPortHCInDiscards": dot1qTpVlanPortHCInDiscards,
       "dot1qLearningConstraintsTable": dot1qLearningConstraintsTable,
       "dot1qLearningConstraintsEntry": dot1qLearningConstraintsEntry,
       "dot1qConstraintVlan": dot1qConstraintVlan,
       "dot1qConstraintSet": dot1qConstraintSet,
       "dot1qConstraintType": dot1qConstraintType,
       "dot1qConstraintStatus": dot1qConstraintStatus,
       "dot1qConstraintSetDefault": dot1qConstraintSetDefault,
       "dot1qConstraintTypeDefault": dot1qConstraintTypeDefault,
       "dot1vProtocol": dot1vProtocol,
       "dot1vProtocolGroupTable": dot1vProtocolGroupTable,
       "dot1vProtocolGroupEntry": dot1vProtocolGroupEntry,
       "dot1vProtocolTemplateFrameType": dot1vProtocolTemplateFrameType,
       "dot1vProtocolTemplateProtocolValue": dot1vProtocolTemplateProtocolValue,
       "dot1vProtocolGroupId": dot1vProtocolGroupId,
       "dot1vProtocolGroupRowStatus": dot1vProtocolGroupRowStatus,
       "dot1vProtocolPortTable": dot1vProtocolPortTable,
       "dot1vProtocolPortEntry": dot1vProtocolPortEntry,
       "dot1vProtocolPortGroupId": dot1vProtocolPortGroupId,
       "dot1vProtocolPortGroupVid": dot1vProtocolPortGroupVid,
       "dot1vProtocolPortRowStatus": dot1vProtocolPortRowStatus,
       "qBridgeConformance": qBridgeConformance,
       "qBridgeGroups": qBridgeGroups,
       "qBridgeBaseGroup": qBridgeBaseGroup,
       "qBridgeFdbUnicastGroup": qBridgeFdbUnicastGroup,
       "qBridgeFdbMulticastGroup": qBridgeFdbMulticastGroup,
       "qBridgeServiceRequirementsGroup": qBridgeServiceRequirementsGroup,
       "qBridgeFdbStaticGroup": qBridgeFdbStaticGroup,
       "qBridgeVlanGroup": qBridgeVlanGroup,
       "qBridgeVlanStaticGroup": qBridgeVlanStaticGroup,
       "qBridgePortGroup": qBridgePortGroup,
       "qBridgeVlanStatisticsGroup": qBridgeVlanStatisticsGroup,
       "qBridgeVlanStatisticsOverflowGroup": qBridgeVlanStatisticsOverflowGroup,
       "qBridgeVlanHCStatisticsGroup": qBridgeVlanHCStatisticsGroup,
       "qBridgeLearningConstraintsGroup": qBridgeLearningConstraintsGroup,
       "qBridgeLearningConstraintDefaultGroup": qBridgeLearningConstraintDefaultGroup,
       "qBridgeClassificationDeviceGroup": qBridgeClassificationDeviceGroup,
       "qBridgeClassificationPortGroup": qBridgeClassificationPortGroup,
       "qBridgePortGroup2": qBridgePortGroup2,
       "qBridgeCompliances": qBridgeCompliances,
       "qBridgeCompliance": qBridgeCompliance,
       "qBridgeCompliance2": qBridgeCompliance2}
)
