# SNMP MIB module (NMS-IEEE8023-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-IEEE8023-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:55 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(nmslocal,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmslocal")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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

lagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LacpKey(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class LacpState(Bits, TextualConvention):
    status = "current"


class ChurnState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("churn", 2),
          ("churnMonitor", 3),
          ("noChurn", 1))
    )



class LagMode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lacpActive", 1),
          ("lacpPassive", 2),
          ("static", 3),
          ("unknown", 0))
    )



# MIB Managed Objects in the order of their OIDs

_LagMIBObjects_ObjectIdentity = ObjectIdentity
lagMIBObjects = _LagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1)
)
_Dot3adAgg_ObjectIdentity = ObjectIdentity
dot3adAgg = _Dot3adAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1)
)
_Dot3adAggTable_Object = MibTable
dot3adAggTable = _Dot3adAggTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot3adAggTable.setStatus("current")
_Dot3adAggEntry_Object = MibTableRow
dot3adAggEntry = _Dot3adAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1)
)
dot3adAggEntry.setIndexNames(
    (0, "NMS-IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggEntry.setStatus("current")
_Dot3adAggIndex_Type = InterfaceIndex
_Dot3adAggIndex_Object = MibTableColumn
dot3adAggIndex = _Dot3adAggIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 1),
    _Dot3adAggIndex_Type()
)
dot3adAggIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggIndex.setStatus("current")
_Dot3adAggMACAddress_Type = MacAddress
_Dot3adAggMACAddress_Object = MibTableColumn
dot3adAggMACAddress = _Dot3adAggMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 2),
    _Dot3adAggMACAddress_Type()
)
dot3adAggMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggMACAddress.setStatus("current")


class _Dot3adAggActorSystemPriority_Type(Integer32):
    """Custom type dot3adAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggActorSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggActorSystemPriority_Object = MibTableColumn
dot3adAggActorSystemPriority = _Dot3adAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 3),
    _Dot3adAggActorSystemPriority_Type()
)
dot3adAggActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggActorSystemPriority.setStatus("current")
_Dot3adAggActorSystemID_Type = MacAddress
_Dot3adAggActorSystemID_Object = MibTableColumn
dot3adAggActorSystemID = _Dot3adAggActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 4),
    _Dot3adAggActorSystemID_Type()
)
dot3adAggActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggActorSystemID.setStatus("current")
_Dot3adAggAggregateOrIndividual_Type = TruthValue
_Dot3adAggAggregateOrIndividual_Object = MibTableColumn
dot3adAggAggregateOrIndividual = _Dot3adAggAggregateOrIndividual_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 5),
    _Dot3adAggAggregateOrIndividual_Type()
)
dot3adAggAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggAggregateOrIndividual.setStatus("current")
_Dot3adAggActorAdminKey_Type = LacpKey
_Dot3adAggActorAdminKey_Object = MibTableColumn
dot3adAggActorAdminKey = _Dot3adAggActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 6),
    _Dot3adAggActorAdminKey_Type()
)
dot3adAggActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggActorAdminKey.setStatus("current")
_Dot3adAggActorOperKey_Type = LacpKey
_Dot3adAggActorOperKey_Object = MibTableColumn
dot3adAggActorOperKey = _Dot3adAggActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 7),
    _Dot3adAggActorOperKey_Type()
)
dot3adAggActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggActorOperKey.setStatus("current")
_Dot3adAggPartnerSystemID_Type = MacAddress
_Dot3adAggPartnerSystemID_Object = MibTableColumn
dot3adAggPartnerSystemID = _Dot3adAggPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 8),
    _Dot3adAggPartnerSystemID_Type()
)
dot3adAggPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerSystemID.setStatus("current")


class _Dot3adAggPartnerSystemPriority_Type(Integer32):
    """Custom type dot3adAggPartnerSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPartnerSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPartnerSystemPriority_Object = MibTableColumn
dot3adAggPartnerSystemPriority = _Dot3adAggPartnerSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 9),
    _Dot3adAggPartnerSystemPriority_Type()
)
dot3adAggPartnerSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerSystemPriority.setStatus("current")
_Dot3adAggPartnerOperKey_Type = LacpKey
_Dot3adAggPartnerOperKey_Object = MibTableColumn
dot3adAggPartnerOperKey = _Dot3adAggPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 10),
    _Dot3adAggPartnerOperKey_Type()
)
dot3adAggPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPartnerOperKey.setStatus("current")


class _Dot3adAggCollectorMaxDelay_Type(Integer32):
    """Custom type dot3adAggCollectorMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggCollectorMaxDelay_Type.__name__ = "Integer32"
_Dot3adAggCollectorMaxDelay_Object = MibTableColumn
dot3adAggCollectorMaxDelay = _Dot3adAggCollectorMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 11),
    _Dot3adAggCollectorMaxDelay_Type()
)
dot3adAggCollectorMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggCollectorMaxDelay.setStatus("current")
_Dot3adAggIfIndex_Type = InterfaceIndex
_Dot3adAggIfIndex_Object = MibTableColumn
dot3adAggIfIndex = _Dot3adAggIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 12),
    _Dot3adAggIfIndex_Type()
)
dot3adAggIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggIfIndex.setStatus("current")
_Dot3adAggAdminMode_Type = LagMode
_Dot3adAggAdminMode_Object = MibTableColumn
dot3adAggAdminMode = _Dot3adAggAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 13),
    _Dot3adAggAdminMode_Type()
)
dot3adAggAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggAdminMode.setStatus("current")
_Dot3adAggOperMode_Type = LagMode
_Dot3adAggOperMode_Object = MibTableColumn
dot3adAggOperMode = _Dot3adAggOperMode_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 14),
    _Dot3adAggOperMode_Type()
)
dot3adAggOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggOperMode.setStatus("current")
_Dot3adAggRowStatus_Type = RowStatus
_Dot3adAggRowStatus_Object = MibTableColumn
dot3adAggRowStatus = _Dot3adAggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 1, 1, 15),
    _Dot3adAggRowStatus_Type()
)
dot3adAggRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot3adAggRowStatus.setStatus("current")
_Dot3adAggPortListTable_Object = MibTable
dot3adAggPortListTable = _Dot3adAggPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2)
)
if mibBuilder.loadTexts:
    dot3adAggPortListTable.setStatus("current")
_Dot3adAggPortListEntry_Object = MibTableRow
dot3adAggPortListEntry = _Dot3adAggPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1)
)
dot3adAggPortListEntry.setIndexNames(
    (0, "NMS-IEEE8023-LAG-MIB", "dot3adAggIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortListEntry.setStatus("current")
_Dot3adAggPortListPorts_Type = PortList
_Dot3adAggPortListPorts_Object = MibTableColumn
dot3adAggPortListPorts = _Dot3adAggPortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1, 1),
    _Dot3adAggPortListPorts_Type()
)
dot3adAggPortListPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot3adAggPortListPorts.setStatus("current")
_Dot3adAggPortListAggregatedPorts_Type = PortList
_Dot3adAggPortListAggregatedPorts_Object = MibTableColumn
dot3adAggPortListAggregatedPorts = _Dot3adAggPortListAggregatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 1, 2, 1, 2),
    _Dot3adAggPortListAggregatedPorts_Type()
)
dot3adAggPortListAggregatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortListAggregatedPorts.setStatus("current")
_Dot3adAggPort_ObjectIdentity = ObjectIdentity
dot3adAggPort = _Dot3adAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2)
)
_Dot3adAggPortTable_Object = MibTable
dot3adAggPortTable = _Dot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dot3adAggPortTable.setStatus("current")
_Dot3adAggPortEntry_Object = MibTableRow
dot3adAggPortEntry = _Dot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1)
)
dot3adAggPortEntry.setIndexNames(
    (0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortEntry.setStatus("current")
_Dot3adAggPortIndex_Type = InterfaceIndex
_Dot3adAggPortIndex_Object = MibTableColumn
dot3adAggPortIndex = _Dot3adAggPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 1),
    _Dot3adAggPortIndex_Type()
)
dot3adAggPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot3adAggPortIndex.setStatus("current")


class _Dot3adAggPortActorSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortActorSystemPriority_Object = MibTableColumn
dot3adAggPortActorSystemPriority = _Dot3adAggPortActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 2),
    _Dot3adAggPortActorSystemPriority_Type()
)
dot3adAggPortActorSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorSystemPriority.setStatus("current")
_Dot3adAggPortActorSystemID_Type = MacAddress
_Dot3adAggPortActorSystemID_Object = MibTableColumn
dot3adAggPortActorSystemID = _Dot3adAggPortActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 3),
    _Dot3adAggPortActorSystemID_Type()
)
dot3adAggPortActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorSystemID.setStatus("current")
_Dot3adAggPortActorAdminKey_Type = LacpKey
_Dot3adAggPortActorAdminKey_Object = MibTableColumn
dot3adAggPortActorAdminKey = _Dot3adAggPortActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 4),
    _Dot3adAggPortActorAdminKey_Type()
)
dot3adAggPortActorAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminKey.setStatus("current")
_Dot3adAggPortActorOperKey_Type = LacpKey
_Dot3adAggPortActorOperKey_Object = MibTableColumn
dot3adAggPortActorOperKey = _Dot3adAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 5),
    _Dot3adAggPortActorOperKey_Type()
)
dot3adAggPortActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperKey.setStatus("current")


class _Dot3adAggPortPartnerAdminSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminSystemPriority_Object = MibTableColumn
dot3adAggPortPartnerAdminSystemPriority = _Dot3adAggPortPartnerAdminSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 6),
    _Dot3adAggPortPartnerAdminSystemPriority_Type()
)
dot3adAggPortPartnerAdminSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminSystemPriority.setStatus("current")


class _Dot3adAggPortPartnerOperSystemPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperSystemPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperSystemPriority_Object = MibTableColumn
dot3adAggPortPartnerOperSystemPriority = _Dot3adAggPortPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 7),
    _Dot3adAggPortPartnerOperSystemPriority_Type()
)
dot3adAggPortPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperSystemPriority.setStatus("current")
_Dot3adAggPortPartnerAdminSystemID_Type = MacAddress
_Dot3adAggPortPartnerAdminSystemID_Object = MibTableColumn
dot3adAggPortPartnerAdminSystemID = _Dot3adAggPortPartnerAdminSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 8),
    _Dot3adAggPortPartnerAdminSystemID_Type()
)
dot3adAggPortPartnerAdminSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminSystemID.setStatus("current")
_Dot3adAggPortPartnerOperSystemID_Type = MacAddress
_Dot3adAggPortPartnerOperSystemID_Object = MibTableColumn
dot3adAggPortPartnerOperSystemID = _Dot3adAggPortPartnerOperSystemID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 9),
    _Dot3adAggPortPartnerOperSystemID_Type()
)
dot3adAggPortPartnerOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperSystemID.setStatus("current")
_Dot3adAggPortPartnerAdminKey_Type = LacpKey
_Dot3adAggPortPartnerAdminKey_Object = MibTableColumn
dot3adAggPortPartnerAdminKey = _Dot3adAggPortPartnerAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 10),
    _Dot3adAggPortPartnerAdminKey_Type()
)
dot3adAggPortPartnerAdminKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminKey.setStatus("current")
_Dot3adAggPortPartnerOperKey_Type = LacpKey
_Dot3adAggPortPartnerOperKey_Object = MibTableColumn
dot3adAggPortPartnerOperKey = _Dot3adAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 11),
    _Dot3adAggPortPartnerOperKey_Type()
)
dot3adAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperKey.setStatus("current")
_Dot3adAggPortSelectedAggID_Type = InterfaceIndex
_Dot3adAggPortSelectedAggID_Object = MibTableColumn
dot3adAggPortSelectedAggID = _Dot3adAggPortSelectedAggID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 12),
    _Dot3adAggPortSelectedAggID_Type()
)
dot3adAggPortSelectedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortSelectedAggID.setStatus("current")
_Dot3adAggPortAttachedAggID_Type = InterfaceIndex
_Dot3adAggPortAttachedAggID_Object = MibTableColumn
dot3adAggPortAttachedAggID = _Dot3adAggPortAttachedAggID_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 13),
    _Dot3adAggPortAttachedAggID_Type()
)
dot3adAggPortAttachedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortAttachedAggID.setStatus("current")


class _Dot3adAggPortActorPort_Type(Integer32):
    """Custom type dot3adAggPortActorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorPort_Type.__name__ = "Integer32"
_Dot3adAggPortActorPort_Object = MibTableColumn
dot3adAggPortActorPort = _Dot3adAggPortActorPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 14),
    _Dot3adAggPortActorPort_Type()
)
dot3adAggPortActorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorPort.setStatus("current")


class _Dot3adAggPortActorPortPriority_Type(Integer32):
    """Custom type dot3adAggPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortActorPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortActorPortPriority_Object = MibTableColumn
dot3adAggPortActorPortPriority = _Dot3adAggPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 15),
    _Dot3adAggPortActorPortPriority_Type()
)
dot3adAggPortActorPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorPortPriority.setStatus("current")


class _Dot3adAggPortPartnerAdminPort_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminPort_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminPort_Object = MibTableColumn
dot3adAggPortPartnerAdminPort = _Dot3adAggPortPartnerAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 16),
    _Dot3adAggPortPartnerAdminPort_Type()
)
dot3adAggPortPartnerAdminPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminPort.setStatus("current")


class _Dot3adAggPortPartnerOperPort_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperPort_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperPort_Object = MibTableColumn
dot3adAggPortPartnerOperPort = _Dot3adAggPortPartnerOperPort_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 17),
    _Dot3adAggPortPartnerOperPort_Type()
)
dot3adAggPortPartnerOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperPort.setStatus("current")


class _Dot3adAggPortPartnerAdminPortPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerAdminPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerAdminPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerAdminPortPriority_Object = MibTableColumn
dot3adAggPortPartnerAdminPortPriority = _Dot3adAggPortPartnerAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 18),
    _Dot3adAggPortPartnerAdminPortPriority_Type()
)
dot3adAggPortPartnerAdminPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminPortPriority.setStatus("current")


class _Dot3adAggPortPartnerOperPortPriority_Type(Integer32):
    """Custom type dot3adAggPortPartnerOperPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Dot3adAggPortPartnerOperPortPriority_Type.__name__ = "Integer32"
_Dot3adAggPortPartnerOperPortPriority_Object = MibTableColumn
dot3adAggPortPartnerOperPortPriority = _Dot3adAggPortPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 19),
    _Dot3adAggPortPartnerOperPortPriority_Type()
)
dot3adAggPortPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperPortPriority.setStatus("current")
_Dot3adAggPortActorAdminState_Type = LacpState
_Dot3adAggPortActorAdminState_Object = MibTableColumn
dot3adAggPortActorAdminState = _Dot3adAggPortActorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 20),
    _Dot3adAggPortActorAdminState_Type()
)
dot3adAggPortActorAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorAdminState.setStatus("current")
_Dot3adAggPortActorOperState_Type = LacpState
_Dot3adAggPortActorOperState_Object = MibTableColumn
dot3adAggPortActorOperState = _Dot3adAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 21),
    _Dot3adAggPortActorOperState_Type()
)
dot3adAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortActorOperState.setStatus("current")
_Dot3adAggPortPartnerAdminState_Type = LacpState
_Dot3adAggPortPartnerAdminState_Object = MibTableColumn
dot3adAggPortPartnerAdminState = _Dot3adAggPortPartnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 22),
    _Dot3adAggPortPartnerAdminState_Type()
)
dot3adAggPortPartnerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerAdminState.setStatus("current")
_Dot3adAggPortPartnerOperState_Type = LacpState
_Dot3adAggPortPartnerOperState_Object = MibTableColumn
dot3adAggPortPartnerOperState = _Dot3adAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 23),
    _Dot3adAggPortPartnerOperState_Type()
)
dot3adAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortPartnerOperState.setStatus("current")
_Dot3adAggPortAggregateOrIndividual_Type = TruthValue
_Dot3adAggPortAggregateOrIndividual_Object = MibTableColumn
dot3adAggPortAggregateOrIndividual = _Dot3adAggPortAggregateOrIndividual_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 24),
    _Dot3adAggPortAggregateOrIndividual_Type()
)
dot3adAggPortAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortAggregateOrIndividual.setStatus("current")
_Dot3adAggPortOperMode_Type = LagMode
_Dot3adAggPortOperMode_Object = MibTableColumn
dot3adAggPortOperMode = _Dot3adAggPortOperMode_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 1, 1, 25),
    _Dot3adAggPortOperMode_Type()
)
dot3adAggPortOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortOperMode.setStatus("current")
_Dot3adAggPortStatsTable_Object = MibTable
dot3adAggPortStatsTable = _Dot3adAggPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsTable.setStatus("current")
_Dot3adAggPortStatsEntry_Object = MibTableRow
dot3adAggPortStatsEntry = _Dot3adAggPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1)
)
dot3adAggPortStatsEntry.setIndexNames(
    (0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsEntry.setStatus("current")
_Dot3adAggPortStatsLACPDUsRx_Type = Counter32
_Dot3adAggPortStatsLACPDUsRx_Object = MibTableColumn
dot3adAggPortStatsLACPDUsRx = _Dot3adAggPortStatsLACPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 1),
    _Dot3adAggPortStatsLACPDUsRx_Type()
)
dot3adAggPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsLACPDUsRx.setStatus("current")
_Dot3adAggPortStatsMarkerPDUsRx_Type = Counter32
_Dot3adAggPortStatsMarkerPDUsRx_Object = MibTableColumn
dot3adAggPortStatsMarkerPDUsRx = _Dot3adAggPortStatsMarkerPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 2),
    _Dot3adAggPortStatsMarkerPDUsRx_Type()
)
dot3adAggPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerPDUsRx.setStatus("current")
_Dot3adAggPortStatsMarkerResponsePDUsRx_Type = Counter32
_Dot3adAggPortStatsMarkerResponsePDUsRx_Object = MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsRx = _Dot3adAggPortStatsMarkerResponsePDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 3),
    _Dot3adAggPortStatsMarkerResponsePDUsRx_Type()
)
dot3adAggPortStatsMarkerResponsePDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerResponsePDUsRx.setStatus("current")
_Dot3adAggPortStatsUnknownRx_Type = Counter32
_Dot3adAggPortStatsUnknownRx_Object = MibTableColumn
dot3adAggPortStatsUnknownRx = _Dot3adAggPortStatsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 4),
    _Dot3adAggPortStatsUnknownRx_Type()
)
dot3adAggPortStatsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsUnknownRx.setStatus("current")
_Dot3adAggPortStatsIllegalRx_Type = Counter32
_Dot3adAggPortStatsIllegalRx_Object = MibTableColumn
dot3adAggPortStatsIllegalRx = _Dot3adAggPortStatsIllegalRx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 5),
    _Dot3adAggPortStatsIllegalRx_Type()
)
dot3adAggPortStatsIllegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsIllegalRx.setStatus("current")
_Dot3adAggPortStatsLACPDUsTx_Type = Counter32
_Dot3adAggPortStatsLACPDUsTx_Object = MibTableColumn
dot3adAggPortStatsLACPDUsTx = _Dot3adAggPortStatsLACPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 6),
    _Dot3adAggPortStatsLACPDUsTx_Type()
)
dot3adAggPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsLACPDUsTx.setStatus("current")
_Dot3adAggPortStatsMarkerPDUsTx_Type = Counter32
_Dot3adAggPortStatsMarkerPDUsTx_Object = MibTableColumn
dot3adAggPortStatsMarkerPDUsTx = _Dot3adAggPortStatsMarkerPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 7),
    _Dot3adAggPortStatsMarkerPDUsTx_Type()
)
dot3adAggPortStatsMarkerPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerPDUsTx.setStatus("current")
_Dot3adAggPortStatsMarkerResponsePDUsTx_Type = Counter32
_Dot3adAggPortStatsMarkerResponsePDUsTx_Object = MibTableColumn
dot3adAggPortStatsMarkerResponsePDUsTx = _Dot3adAggPortStatsMarkerResponsePDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 2, 1, 8),
    _Dot3adAggPortStatsMarkerResponsePDUsTx_Type()
)
dot3adAggPortStatsMarkerResponsePDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortStatsMarkerResponsePDUsTx.setStatus("current")
_Dot3adAggPortDebugTable_Object = MibTable
dot3adAggPortDebugTable = _Dot3adAggPortDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugTable.setStatus("current")
_Dot3adAggPortDebugEntry_Object = MibTableRow
dot3adAggPortDebugEntry = _Dot3adAggPortDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1)
)
dot3adAggPortDebugEntry.setIndexNames(
    (0, "NMS-IEEE8023-LAG-MIB", "dot3adAggPortIndex"),
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugEntry.setStatus("current")


class _Dot3adAggPortDebugRxState_Type(Integer32):
    """Custom type dot3adAggPortDebugRxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("currentRx", 1),
          ("defaulted", 3),
          ("expired", 2),
          ("initialize", 4),
          ("lacpDisabled", 5),
          ("portDisabled", 6))
    )


_Dot3adAggPortDebugRxState_Type.__name__ = "Integer32"
_Dot3adAggPortDebugRxState_Object = MibTableColumn
dot3adAggPortDebugRxState = _Dot3adAggPortDebugRxState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 1),
    _Dot3adAggPortDebugRxState_Type()
)
dot3adAggPortDebugRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugRxState.setStatus("current")
_Dot3adAggPortDebugLastRxTime_Type = TimeTicks
_Dot3adAggPortDebugLastRxTime_Object = MibTableColumn
dot3adAggPortDebugLastRxTime = _Dot3adAggPortDebugLastRxTime_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 2),
    _Dot3adAggPortDebugLastRxTime_Type()
)
dot3adAggPortDebugLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugLastRxTime.setStatus("current")


class _Dot3adAggPortDebugMuxState_Type(Integer32):
    """Custom type dot3adAggPortDebugMuxState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("attached", 3),
          ("collecting", 4),
          ("collectingDistributing", 6),
          ("detached", 1),
          ("distributing", 5),
          ("waiting", 2))
    )


_Dot3adAggPortDebugMuxState_Type.__name__ = "Integer32"
_Dot3adAggPortDebugMuxState_Object = MibTableColumn
dot3adAggPortDebugMuxState = _Dot3adAggPortDebugMuxState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 3),
    _Dot3adAggPortDebugMuxState_Type()
)
dot3adAggPortDebugMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugMuxState.setStatus("current")
_Dot3adAggPortDebugMuxReason_Type = DisplayString
_Dot3adAggPortDebugMuxReason_Object = MibTableColumn
dot3adAggPortDebugMuxReason = _Dot3adAggPortDebugMuxReason_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 4),
    _Dot3adAggPortDebugMuxReason_Type()
)
dot3adAggPortDebugMuxReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugMuxReason.setStatus("current")
_Dot3adAggPortDebugActorChurnState_Type = ChurnState
_Dot3adAggPortDebugActorChurnState_Object = MibTableColumn
dot3adAggPortDebugActorChurnState = _Dot3adAggPortDebugActorChurnState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 5),
    _Dot3adAggPortDebugActorChurnState_Type()
)
dot3adAggPortDebugActorChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChurnState.setStatus("current")
_Dot3adAggPortDebugPartnerChurnState_Type = ChurnState
_Dot3adAggPortDebugPartnerChurnState_Object = MibTableColumn
dot3adAggPortDebugPartnerChurnState = _Dot3adAggPortDebugPartnerChurnState_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 6),
    _Dot3adAggPortDebugPartnerChurnState_Type()
)
dot3adAggPortDebugPartnerChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChurnState.setStatus("current")
_Dot3adAggPortDebugActorChurnCount_Type = Counter32
_Dot3adAggPortDebugActorChurnCount_Object = MibTableColumn
dot3adAggPortDebugActorChurnCount = _Dot3adAggPortDebugActorChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 7),
    _Dot3adAggPortDebugActorChurnCount_Type()
)
dot3adAggPortDebugActorChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChurnCount.setStatus("current")
_Dot3adAggPortDebugPartnerChurnCount_Type = Counter32
_Dot3adAggPortDebugPartnerChurnCount_Object = MibTableColumn
dot3adAggPortDebugPartnerChurnCount = _Dot3adAggPortDebugPartnerChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 8),
    _Dot3adAggPortDebugPartnerChurnCount_Type()
)
dot3adAggPortDebugPartnerChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChurnCount.setStatus("current")
_Dot3adAggPortDebugActorSyncTransitionCount_Type = Counter32
_Dot3adAggPortDebugActorSyncTransitionCount_Object = MibTableColumn
dot3adAggPortDebugActorSyncTransitionCount = _Dot3adAggPortDebugActorSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 9),
    _Dot3adAggPortDebugActorSyncTransitionCount_Type()
)
dot3adAggPortDebugActorSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorSyncTransitionCount.setStatus("current")
_Dot3adAggPortDebugPartnerSyncTransitionCount_Type = Counter32
_Dot3adAggPortDebugPartnerSyncTransitionCount_Object = MibTableColumn
dot3adAggPortDebugPartnerSyncTransitionCount = _Dot3adAggPortDebugPartnerSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 10),
    _Dot3adAggPortDebugPartnerSyncTransitionCount_Type()
)
dot3adAggPortDebugPartnerSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerSyncTransitionCount.setStatus("current")
_Dot3adAggPortDebugActorChangeCount_Type = Counter32
_Dot3adAggPortDebugActorChangeCount_Object = MibTableColumn
dot3adAggPortDebugActorChangeCount = _Dot3adAggPortDebugActorChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 11),
    _Dot3adAggPortDebugActorChangeCount_Type()
)
dot3adAggPortDebugActorChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugActorChangeCount.setStatus("current")
_Dot3adAggPortDebugPartnerChangeCount_Type = Counter32
_Dot3adAggPortDebugPartnerChangeCount_Object = MibTableColumn
dot3adAggPortDebugPartnerChangeCount = _Dot3adAggPortDebugPartnerChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 2, 3, 1, 12),
    _Dot3adAggPortDebugPartnerChangeCount_Type()
)
dot3adAggPortDebugPartnerChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortDebugPartnerChangeCount.setStatus("current")
_Dot3adTablesLastChanged_Type = TimeTicks
_Dot3adTablesLastChanged_Object = MibScalar
dot3adTablesLastChanged = _Dot3adTablesLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 3),
    _Dot3adTablesLastChanged_Type()
)
dot3adTablesLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adTablesLastChanged.setStatus("current")
_Dot3adAggMaxNum_Type = Integer32
_Dot3adAggMaxNum_Object = MibScalar
dot3adAggMaxNum = _Dot3adAggMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 4),
    _Dot3adAggMaxNum_Type()
)
dot3adAggMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggMaxNum.setStatus("current")
_Dot3adAggPortsMaxNum_Type = Integer32
_Dot3adAggPortsMaxNum_Object = MibScalar
dot3adAggPortsMaxNum = _Dot3adAggPortsMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 1, 5),
    _Dot3adAggPortsMaxNum_Type()
)
dot3adAggPortsMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot3adAggPortsMaxNum.setStatus("current")
_Dot3adAggConformance_ObjectIdentity = ObjectIdentity
dot3adAggConformance = _Dot3adAggConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2)
)
_Dot3adAggGroups_ObjectIdentity = ObjectIdentity
dot3adAggGroups = _Dot3adAggGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1)
)
_Dot3adAggCompliances_ObjectIdentity = ObjectIdentity
dot3adAggCompliances = _Dot3adAggCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 2)
)

# Managed Objects groups

dot3adAggGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 1)
)
dot3adAggGroup.setObjects(
      *(("NMS-IEEE8023-LAG-MIB", "dot3adAggActorSystemID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorSystemPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggAggregateOrIndividual"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorAdminKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggMACAddress"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggActorOperKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerSystemID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerSystemPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPartnerOperKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggCollectorMaxDelay"))
)
if mibBuilder.loadTexts:
    dot3adAggGroup.setStatus("current")

dot3adTablesLastChangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 1, 6)
)
dot3adTablesLastChangedGroup.setObjects(
    ("NMS-IEEE8023-LAG-MIB", "dot3adTablesLastChanged")
)
if mibBuilder.loadTexts:
    dot3adTablesLastChangedGroup.setStatus("current")

dot3adAggPortListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 2)
)
dot3adAggPortListGroup.setObjects(
    ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortListPorts")
)
if mibBuilder.loadTexts:
    dot3adAggPortListGroup.setStatus("current")

dot3adAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 3)
)
dot3adAggPortGroup.setObjects(
      *(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorSystemPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorSystemID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorAdminKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorOperKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminSystemID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperSystemID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperKey"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortSelectedAggID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortAttachedAggID"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorPort"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorPortPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPort"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPort"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminPortPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperPortPriority"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorAdminState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortActorOperState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerAdminState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortPartnerOperState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortAggregateOrIndividual"))
)
if mibBuilder.loadTexts:
    dot3adAggPortGroup.setStatus("current")

dot3adAggPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 4)
)
dot3adAggPortStatsGroup.setObjects(
      *(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsRx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsRx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsRx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsUnknownRx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsIllegalRx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsLACPDUsTx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerPDUsTx"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortStatsMarkerResponsePDUsTx"))
)
if mibBuilder.loadTexts:
    dot3adAggPortStatsGroup.setStatus("current")

dot3adAggPortDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 1, 5)
)
dot3adAggPortDebugGroup.setObjects(
      *(("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugRxState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugLastRxTime"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugMuxReason"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnState"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChurnCount"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChurnCount"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorSyncTransitionCount"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerSyncTransitionCount"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugActorChangeCount"),
        ("NMS-IEEE8023-LAG-MIB", "dot3adAggPortDebugPartnerChangeCount"))
)
if mibBuilder.loadTexts:
    dot3adAggPortDebugGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot3adAggCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11606, 10, 2, 232, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot3adAggCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-IEEE8023-LAG-MIB",
    **{"LacpKey": LacpKey,
       "LacpState": LacpState,
       "ChurnState": ChurnState,
       "LagMode": LagMode,
       "lagMIB": lagMIB,
       "lagMIBObjects": lagMIBObjects,
       "dot3adAgg": dot3adAgg,
       "dot3adAggTable": dot3adAggTable,
       "dot3adAggEntry": dot3adAggEntry,
       "dot3adAggIndex": dot3adAggIndex,
       "dot3adAggMACAddress": dot3adAggMACAddress,
       "dot3adAggActorSystemPriority": dot3adAggActorSystemPriority,
       "dot3adAggActorSystemID": dot3adAggActorSystemID,
       "dot3adAggAggregateOrIndividual": dot3adAggAggregateOrIndividual,
       "dot3adAggActorAdminKey": dot3adAggActorAdminKey,
       "dot3adAggActorOperKey": dot3adAggActorOperKey,
       "dot3adAggPartnerSystemID": dot3adAggPartnerSystemID,
       "dot3adAggPartnerSystemPriority": dot3adAggPartnerSystemPriority,
       "dot3adAggPartnerOperKey": dot3adAggPartnerOperKey,
       "dot3adAggCollectorMaxDelay": dot3adAggCollectorMaxDelay,
       "dot3adAggIfIndex": dot3adAggIfIndex,
       "dot3adAggAdminMode": dot3adAggAdminMode,
       "dot3adAggOperMode": dot3adAggOperMode,
       "dot3adAggRowStatus": dot3adAggRowStatus,
       "dot3adAggPortListTable": dot3adAggPortListTable,
       "dot3adAggPortListEntry": dot3adAggPortListEntry,
       "dot3adAggPortListPorts": dot3adAggPortListPorts,
       "dot3adAggPortListAggregatedPorts": dot3adAggPortListAggregatedPorts,
       "dot3adAggPort": dot3adAggPort,
       "dot3adAggPortTable": dot3adAggPortTable,
       "dot3adAggPortEntry": dot3adAggPortEntry,
       "dot3adAggPortIndex": dot3adAggPortIndex,
       "dot3adAggPortActorSystemPriority": dot3adAggPortActorSystemPriority,
       "dot3adAggPortActorSystemID": dot3adAggPortActorSystemID,
       "dot3adAggPortActorAdminKey": dot3adAggPortActorAdminKey,
       "dot3adAggPortActorOperKey": dot3adAggPortActorOperKey,
       "dot3adAggPortPartnerAdminSystemPriority": dot3adAggPortPartnerAdminSystemPriority,
       "dot3adAggPortPartnerOperSystemPriority": dot3adAggPortPartnerOperSystemPriority,
       "dot3adAggPortPartnerAdminSystemID": dot3adAggPortPartnerAdminSystemID,
       "dot3adAggPortPartnerOperSystemID": dot3adAggPortPartnerOperSystemID,
       "dot3adAggPortPartnerAdminKey": dot3adAggPortPartnerAdminKey,
       "dot3adAggPortPartnerOperKey": dot3adAggPortPartnerOperKey,
       "dot3adAggPortSelectedAggID": dot3adAggPortSelectedAggID,
       "dot3adAggPortAttachedAggID": dot3adAggPortAttachedAggID,
       "dot3adAggPortActorPort": dot3adAggPortActorPort,
       "dot3adAggPortActorPortPriority": dot3adAggPortActorPortPriority,
       "dot3adAggPortPartnerAdminPort": dot3adAggPortPartnerAdminPort,
       "dot3adAggPortPartnerOperPort": dot3adAggPortPartnerOperPort,
       "dot3adAggPortPartnerAdminPortPriority": dot3adAggPortPartnerAdminPortPriority,
       "dot3adAggPortPartnerOperPortPriority": dot3adAggPortPartnerOperPortPriority,
       "dot3adAggPortActorAdminState": dot3adAggPortActorAdminState,
       "dot3adAggPortActorOperState": dot3adAggPortActorOperState,
       "dot3adAggPortPartnerAdminState": dot3adAggPortPartnerAdminState,
       "dot3adAggPortPartnerOperState": dot3adAggPortPartnerOperState,
       "dot3adAggPortAggregateOrIndividual": dot3adAggPortAggregateOrIndividual,
       "dot3adAggPortOperMode": dot3adAggPortOperMode,
       "dot3adAggPortStatsTable": dot3adAggPortStatsTable,
       "dot3adAggPortStatsEntry": dot3adAggPortStatsEntry,
       "dot3adAggPortStatsLACPDUsRx": dot3adAggPortStatsLACPDUsRx,
       "dot3adAggPortStatsMarkerPDUsRx": dot3adAggPortStatsMarkerPDUsRx,
       "dot3adAggPortStatsMarkerResponsePDUsRx": dot3adAggPortStatsMarkerResponsePDUsRx,
       "dot3adAggPortStatsUnknownRx": dot3adAggPortStatsUnknownRx,
       "dot3adAggPortStatsIllegalRx": dot3adAggPortStatsIllegalRx,
       "dot3adAggPortStatsLACPDUsTx": dot3adAggPortStatsLACPDUsTx,
       "dot3adAggPortStatsMarkerPDUsTx": dot3adAggPortStatsMarkerPDUsTx,
       "dot3adAggPortStatsMarkerResponsePDUsTx": dot3adAggPortStatsMarkerResponsePDUsTx,
       "dot3adAggPortDebugTable": dot3adAggPortDebugTable,
       "dot3adAggPortDebugEntry": dot3adAggPortDebugEntry,
       "dot3adAggPortDebugRxState": dot3adAggPortDebugRxState,
       "dot3adAggPortDebugLastRxTime": dot3adAggPortDebugLastRxTime,
       "dot3adAggPortDebugMuxState": dot3adAggPortDebugMuxState,
       "dot3adAggPortDebugMuxReason": dot3adAggPortDebugMuxReason,
       "dot3adAggPortDebugActorChurnState": dot3adAggPortDebugActorChurnState,
       "dot3adAggPortDebugPartnerChurnState": dot3adAggPortDebugPartnerChurnState,
       "dot3adAggPortDebugActorChurnCount": dot3adAggPortDebugActorChurnCount,
       "dot3adAggPortDebugPartnerChurnCount": dot3adAggPortDebugPartnerChurnCount,
       "dot3adAggPortDebugActorSyncTransitionCount": dot3adAggPortDebugActorSyncTransitionCount,
       "dot3adAggPortDebugPartnerSyncTransitionCount": dot3adAggPortDebugPartnerSyncTransitionCount,
       "dot3adAggPortDebugActorChangeCount": dot3adAggPortDebugActorChangeCount,
       "dot3adAggPortDebugPartnerChangeCount": dot3adAggPortDebugPartnerChangeCount,
       "dot3adTablesLastChanged": dot3adTablesLastChanged,
       "dot3adAggMaxNum": dot3adAggMaxNum,
       "dot3adAggPortsMaxNum": dot3adAggPortsMaxNum,
       "dot3adAggConformance": dot3adAggConformance,
       "dot3adAggGroups": dot3adAggGroups,
       "dot3adAggGroup": dot3adAggGroup,
       "dot3adTablesLastChangedGroup": dot3adTablesLastChangedGroup,
       "dot3adAggPortListGroup": dot3adAggPortListGroup,
       "dot3adAggPortGroup": dot3adAggPortGroup,
       "dot3adAggPortStatsGroup": dot3adAggPortStatsGroup,
       "dot3adAggPortDebugGroup": dot3adAggPortDebugGroup,
       "dot3adAggCompliances": dot3adAggCompliances,
       "dot3adAggCompliance": dot3adAggCompliance}
)
