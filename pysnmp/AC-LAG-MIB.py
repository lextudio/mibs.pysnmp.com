# SNMP MIB module (AC-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-LAG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:29 2024
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

(AcAdminStatus,
 AcNodeId,
 AcOpStatus,
 AcPortNumber,
 AcSlotNumber,
 acPport) = mibBuilder.importSymbols(
    "APPIAN-SMI-MIB",
    "AcAdminStatus",
    "AcNodeId",
    "AcOpStatus",
    "AcPortNumber",
    "AcSlotNumber",
    "acPport")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

acLagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8)
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



class PortList(OctetString, TextualConvention):
    status = "current"


class AcAggInstanceIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )



class AcAggInstanceValue(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_LagMIBObjects_ObjectIdentity = ObjectIdentity
lagMIBObjects = _LagMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1)
)
_AcDot3adAgg_ObjectIdentity = ObjectIdentity
acDot3adAgg = _AcDot3adAgg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1)
)
_AcDot3adAggTable_Object = MibTable
acDot3adAggTable = _AcDot3adAggTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    acDot3adAggTable.setStatus("current")
_AcDot3adAggEntry_Object = MibTableRow
acDot3adAggEntry = _AcDot3adAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1)
)
acDot3adAggEntry.setIndexNames(
    (0, "AC-LAG-MIB", "acDot3adAggNodeIdIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggInstanceIndex"),
)
if mibBuilder.loadTexts:
    acDot3adAggEntry.setStatus("current")
_AcDot3adAggNodeIdIndex_Type = AcNodeId
_AcDot3adAggNodeIdIndex_Object = MibTableColumn
acDot3adAggNodeIdIndex = _AcDot3adAggNodeIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 1),
    _AcDot3adAggNodeIdIndex_Type()
)
acDot3adAggNodeIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDot3adAggNodeIdIndex.setStatus("current")
_AcDot3adAggInstanceIndex_Type = AcAggInstanceIndex
_AcDot3adAggInstanceIndex_Object = MibTableColumn
acDot3adAggInstanceIndex = _AcDot3adAggInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 2),
    _AcDot3adAggInstanceIndex_Type()
)
acDot3adAggInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDot3adAggInstanceIndex.setStatus("current")
_AcDot3adAggMACAddress_Type = MacAddress
_AcDot3adAggMACAddress_Object = MibTableColumn
acDot3adAggMACAddress = _AcDot3adAggMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 3),
    _AcDot3adAggMACAddress_Type()
)
acDot3adAggMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggMACAddress.setStatus("current")


class _AcDot3adAggActorSystemPriority_Type(Integer32):
    """Custom type acDot3adAggActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggActorSystemPriority_Type.__name__ = "Integer32"
_AcDot3adAggActorSystemPriority_Object = MibTableColumn
acDot3adAggActorSystemPriority = _AcDot3adAggActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 4),
    _AcDot3adAggActorSystemPriority_Type()
)
acDot3adAggActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggActorSystemPriority.setStatus("current")
_AcDot3adAggActorSystemID_Type = MacAddress
_AcDot3adAggActorSystemID_Object = MibTableColumn
acDot3adAggActorSystemID = _AcDot3adAggActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 5),
    _AcDot3adAggActorSystemID_Type()
)
acDot3adAggActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggActorSystemID.setStatus("current")
_AcDot3adAggAggregateOrIndividual_Type = TruthValue
_AcDot3adAggAggregateOrIndividual_Object = MibTableColumn
acDot3adAggAggregateOrIndividual = _AcDot3adAggAggregateOrIndividual_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 6),
    _AcDot3adAggAggregateOrIndividual_Type()
)
acDot3adAggAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggAggregateOrIndividual.setStatus("current")
_AcDot3adAggActorAdminKey_Type = LacpKey
_AcDot3adAggActorAdminKey_Object = MibTableColumn
acDot3adAggActorAdminKey = _AcDot3adAggActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 7),
    _AcDot3adAggActorAdminKey_Type()
)
acDot3adAggActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggActorAdminKey.setStatus("current")
_AcDot3adAggActorOperKey_Type = LacpKey
_AcDot3adAggActorOperKey_Object = MibTableColumn
acDot3adAggActorOperKey = _AcDot3adAggActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 8),
    _AcDot3adAggActorOperKey_Type()
)
acDot3adAggActorOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggActorOperKey.setStatus("current")
_AcDot3adAggPartnerSystemID_Type = MacAddress
_AcDot3adAggPartnerSystemID_Object = MibTableColumn
acDot3adAggPartnerSystemID = _AcDot3adAggPartnerSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 9),
    _AcDot3adAggPartnerSystemID_Type()
)
acDot3adAggPartnerSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPartnerSystemID.setStatus("current")


class _AcDot3adAggPartnerSystemPriority_Type(Integer32):
    """Custom type acDot3adAggPartnerSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggPartnerSystemPriority_Type.__name__ = "Integer32"
_AcDot3adAggPartnerSystemPriority_Object = MibTableColumn
acDot3adAggPartnerSystemPriority = _AcDot3adAggPartnerSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 10),
    _AcDot3adAggPartnerSystemPriority_Type()
)
acDot3adAggPartnerSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPartnerSystemPriority.setStatus("current")
_AcDot3adAggPartnerOperKey_Type = LacpKey
_AcDot3adAggPartnerOperKey_Object = MibTableColumn
acDot3adAggPartnerOperKey = _AcDot3adAggPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 11),
    _AcDot3adAggPartnerOperKey_Type()
)
acDot3adAggPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPartnerOperKey.setStatus("current")


class _AcDot3adAggCollectorMaxDelay_Type(Integer32):
    """Custom type acDot3adAggCollectorMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggCollectorMaxDelay_Type.__name__ = "Integer32"
_AcDot3adAggCollectorMaxDelay_Object = MibTableColumn
acDot3adAggCollectorMaxDelay = _AcDot3adAggCollectorMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 1, 1, 12),
    _AcDot3adAggCollectorMaxDelay_Type()
)
acDot3adAggCollectorMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggCollectorMaxDelay.setStatus("current")
_AcDot3adAggPortListTable_Object = MibTable
acDot3adAggPortListTable = _AcDot3adAggPortListTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 2)
)
if mibBuilder.loadTexts:
    acDot3adAggPortListTable.setStatus("current")
_AcDot3adAggPortListEntry_Object = MibTableRow
acDot3adAggPortListEntry = _AcDot3adAggPortListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 2, 1)
)
acDot3adAggPortListEntry.setIndexNames(
    (0, "AC-LAG-MIB", "acDot3adAggNodeIdIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggInstanceIndex"),
)
if mibBuilder.loadTexts:
    acDot3adAggPortListEntry.setStatus("current")
_AcDot3adAggPortListPorts_Type = PortList
_AcDot3adAggPortListPorts_Object = MibTableColumn
acDot3adAggPortListPorts = _AcDot3adAggPortListPorts_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 1, 2, 1, 1),
    _AcDot3adAggPortListPorts_Type()
)
acDot3adAggPortListPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortListPorts.setStatus("current")
_AcDot3adAggPort_ObjectIdentity = ObjectIdentity
acDot3adAggPort = _AcDot3adAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2)
)
_AcDot3adAggPortTable_Object = MibTable
acDot3adAggPortTable = _AcDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    acDot3adAggPortTable.setStatus("current")
_AcDot3adAggPortEntry_Object = MibTableRow
acDot3adAggPortEntry = _AcDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1)
)
acDot3adAggPortEntry.setIndexNames(
    (0, "AC-LAG-MIB", "acDot3adAggPortNodeIdIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortSlotIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortPortIndex"),
)
if mibBuilder.loadTexts:
    acDot3adAggPortEntry.setStatus("current")
_AcDot3adAggPortNodeIdIndex_Type = AcNodeId
_AcDot3adAggPortNodeIdIndex_Object = MibTableColumn
acDot3adAggPortNodeIdIndex = _AcDot3adAggPortNodeIdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 1),
    _AcDot3adAggPortNodeIdIndex_Type()
)
acDot3adAggPortNodeIdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDot3adAggPortNodeIdIndex.setStatus("current")
_AcDot3adAggPortSlotIndex_Type = AcSlotNumber
_AcDot3adAggPortSlotIndex_Object = MibTableColumn
acDot3adAggPortSlotIndex = _AcDot3adAggPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 2),
    _AcDot3adAggPortSlotIndex_Type()
)
acDot3adAggPortSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDot3adAggPortSlotIndex.setStatus("current")
_AcDot3adAggPortPortIndex_Type = AcPortNumber
_AcDot3adAggPortPortIndex_Object = MibTableColumn
acDot3adAggPortPortIndex = _AcDot3adAggPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 3),
    _AcDot3adAggPortPortIndex_Type()
)
acDot3adAggPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acDot3adAggPortPortIndex.setStatus("current")


class _AcDot3adAggPortActorSystemPriority_Type(Integer32):
    """Custom type acDot3adAggPortActorSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortActorSystemPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortActorSystemPriority_Object = MibTableColumn
acDot3adAggPortActorSystemPriority = _AcDot3adAggPortActorSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 4),
    _AcDot3adAggPortActorSystemPriority_Type()
)
acDot3adAggPortActorSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortActorSystemPriority.setStatus("current")
_AcDot3adAggPortActorSystemID_Type = MacAddress
_AcDot3adAggPortActorSystemID_Object = MibTableColumn
acDot3adAggPortActorSystemID = _AcDot3adAggPortActorSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 5),
    _AcDot3adAggPortActorSystemID_Type()
)
acDot3adAggPortActorSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortActorSystemID.setStatus("current")
_AcDot3adAggPortActorAdminKey_Type = LacpKey
_AcDot3adAggPortActorAdminKey_Object = MibTableColumn
acDot3adAggPortActorAdminKey = _AcDot3adAggPortActorAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 6),
    _AcDot3adAggPortActorAdminKey_Type()
)
acDot3adAggPortActorAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortActorAdminKey.setStatus("current")
_AcDot3adAggPortActorOperKey_Type = LacpKey
_AcDot3adAggPortActorOperKey_Object = MibTableColumn
acDot3adAggPortActorOperKey = _AcDot3adAggPortActorOperKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 7),
    _AcDot3adAggPortActorOperKey_Type()
)
acDot3adAggPortActorOperKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortActorOperKey.setStatus("current")


class _AcDot3adAggPortPartnerAdminSystemPriority_Type(Integer32):
    """Custom type acDot3adAggPortPartnerAdminSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortPartnerAdminSystemPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerAdminSystemPriority_Object = MibTableColumn
acDot3adAggPortPartnerAdminSystemPriority = _AcDot3adAggPortPartnerAdminSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 8),
    _AcDot3adAggPortPartnerAdminSystemPriority_Type()
)
acDot3adAggPortPartnerAdminSystemPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminSystemPriority.setStatus("current")


class _AcDot3adAggPortPartnerOperSystemPriority_Type(Integer32):
    """Custom type acDot3adAggPortPartnerOperSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortPartnerOperSystemPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerOperSystemPriority_Object = MibTableColumn
acDot3adAggPortPartnerOperSystemPriority = _AcDot3adAggPortPartnerOperSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 9),
    _AcDot3adAggPortPartnerOperSystemPriority_Type()
)
acDot3adAggPortPartnerOperSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperSystemPriority.setStatus("current")
_AcDot3adAggPortPartnerAdminSystemID_Type = MacAddress
_AcDot3adAggPortPartnerAdminSystemID_Object = MibTableColumn
acDot3adAggPortPartnerAdminSystemID = _AcDot3adAggPortPartnerAdminSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 10),
    _AcDot3adAggPortPartnerAdminSystemID_Type()
)
acDot3adAggPortPartnerAdminSystemID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminSystemID.setStatus("current")
_AcDot3adAggPortPartnerOperSystemID_Type = MacAddress
_AcDot3adAggPortPartnerOperSystemID_Object = MibTableColumn
acDot3adAggPortPartnerOperSystemID = _AcDot3adAggPortPartnerOperSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 11),
    _AcDot3adAggPortPartnerOperSystemID_Type()
)
acDot3adAggPortPartnerOperSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperSystemID.setStatus("current")
_AcDot3adAggPortPartnerAdminKey_Type = LacpKey
_AcDot3adAggPortPartnerAdminKey_Object = MibTableColumn
acDot3adAggPortPartnerAdminKey = _AcDot3adAggPortPartnerAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 12),
    _AcDot3adAggPortPartnerAdminKey_Type()
)
acDot3adAggPortPartnerAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminKey.setStatus("current")
_AcDot3adAggPortPartnerOperKey_Type = LacpKey
_AcDot3adAggPortPartnerOperKey_Object = MibTableColumn
acDot3adAggPortPartnerOperKey = _AcDot3adAggPortPartnerOperKey_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 13),
    _AcDot3adAggPortPartnerOperKey_Type()
)
acDot3adAggPortPartnerOperKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperKey.setStatus("current")
_AcDot3adAggPortSelectedAggID_Type = AcAggInstanceValue
_AcDot3adAggPortSelectedAggID_Object = MibTableColumn
acDot3adAggPortSelectedAggID = _AcDot3adAggPortSelectedAggID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 14),
    _AcDot3adAggPortSelectedAggID_Type()
)
acDot3adAggPortSelectedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortSelectedAggID.setStatus("current")
_AcDot3adAggPortAttachedAggID_Type = AcAggInstanceValue
_AcDot3adAggPortAttachedAggID_Object = MibTableColumn
acDot3adAggPortAttachedAggID = _AcDot3adAggPortAttachedAggID_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 15),
    _AcDot3adAggPortAttachedAggID_Type()
)
acDot3adAggPortAttachedAggID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortAttachedAggID.setStatus("current")


class _AcDot3adAggPortActorPort_Type(Integer32):
    """Custom type acDot3adAggPortActorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggPortActorPort_Type.__name__ = "Integer32"
_AcDot3adAggPortActorPort_Object = MibTableColumn
acDot3adAggPortActorPort = _AcDot3adAggPortActorPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 16),
    _AcDot3adAggPortActorPort_Type()
)
acDot3adAggPortActorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortActorPort.setStatus("current")


class _AcDot3adAggPortActorPortPriority_Type(Integer32):
    """Custom type acDot3adAggPortActorPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortActorPortPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortActorPortPriority_Object = MibTableColumn
acDot3adAggPortActorPortPriority = _AcDot3adAggPortActorPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 17),
    _AcDot3adAggPortActorPortPriority_Type()
)
acDot3adAggPortActorPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortActorPortPriority.setStatus("current")


class _AcDot3adAggPortPartnerAdminPort_Type(Integer32):
    """Custom type acDot3adAggPortPartnerAdminPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggPortPartnerAdminPort_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerAdminPort_Object = MibTableColumn
acDot3adAggPortPartnerAdminPort = _AcDot3adAggPortPartnerAdminPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 18),
    _AcDot3adAggPortPartnerAdminPort_Type()
)
acDot3adAggPortPartnerAdminPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminPort.setStatus("current")


class _AcDot3adAggPortPartnerOperPort_Type(Integer32):
    """Custom type acDot3adAggPortPartnerOperPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcDot3adAggPortPartnerOperPort_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerOperPort_Object = MibTableColumn
acDot3adAggPortPartnerOperPort = _AcDot3adAggPortPartnerOperPort_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 19),
    _AcDot3adAggPortPartnerOperPort_Type()
)
acDot3adAggPortPartnerOperPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperPort.setStatus("current")


class _AcDot3adAggPortPartnerAdminPortPriority_Type(Integer32):
    """Custom type acDot3adAggPortPartnerAdminPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortPartnerAdminPortPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerAdminPortPriority_Object = MibTableColumn
acDot3adAggPortPartnerAdminPortPriority = _AcDot3adAggPortPartnerAdminPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 20),
    _AcDot3adAggPortPartnerAdminPortPriority_Type()
)
acDot3adAggPortPartnerAdminPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminPortPriority.setStatus("current")


class _AcDot3adAggPortPartnerOperPortPriority_Type(Integer32):
    """Custom type acDot3adAggPortPartnerOperPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcDot3adAggPortPartnerOperPortPriority_Type.__name__ = "Integer32"
_AcDot3adAggPortPartnerOperPortPriority_Object = MibTableColumn
acDot3adAggPortPartnerOperPortPriority = _AcDot3adAggPortPartnerOperPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 21),
    _AcDot3adAggPortPartnerOperPortPriority_Type()
)
acDot3adAggPortPartnerOperPortPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperPortPriority.setStatus("current")
_AcDot3adAggPortActorAdminState_Type = LacpState
_AcDot3adAggPortActorAdminState_Object = MibTableColumn
acDot3adAggPortActorAdminState = _AcDot3adAggPortActorAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 22),
    _AcDot3adAggPortActorAdminState_Type()
)
acDot3adAggPortActorAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortActorAdminState.setStatus("current")
_AcDot3adAggPortActorOperState_Type = LacpState
_AcDot3adAggPortActorOperState_Object = MibTableColumn
acDot3adAggPortActorOperState = _AcDot3adAggPortActorOperState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 23),
    _AcDot3adAggPortActorOperState_Type()
)
acDot3adAggPortActorOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortActorOperState.setStatus("current")
_AcDot3adAggPortPartnerAdminState_Type = LacpState
_AcDot3adAggPortPartnerAdminState_Object = MibTableColumn
acDot3adAggPortPartnerAdminState = _AcDot3adAggPortPartnerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 24),
    _AcDot3adAggPortPartnerAdminState_Type()
)
acDot3adAggPortPartnerAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerAdminState.setStatus("current")
_AcDot3adAggPortPartnerOperState_Type = LacpState
_AcDot3adAggPortPartnerOperState_Object = MibTableColumn
acDot3adAggPortPartnerOperState = _AcDot3adAggPortPartnerOperState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 25),
    _AcDot3adAggPortPartnerOperState_Type()
)
acDot3adAggPortPartnerOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortPartnerOperState.setStatus("current")
_AcDot3adAggPortAggregateOrIndividual_Type = TruthValue
_AcDot3adAggPortAggregateOrIndividual_Object = MibTableColumn
acDot3adAggPortAggregateOrIndividual = _AcDot3adAggPortAggregateOrIndividual_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 1, 1, 26),
    _AcDot3adAggPortAggregateOrIndividual_Type()
)
acDot3adAggPortAggregateOrIndividual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortAggregateOrIndividual.setStatus("current")
_AcDot3adAggPortStatsTable_Object = MibTable
acDot3adAggPortStatsTable = _AcDot3adAggPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    acDot3adAggPortStatsTable.setStatus("current")
_AcDot3adAggPortStatsEntry_Object = MibTableRow
acDot3adAggPortStatsEntry = _AcDot3adAggPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1)
)
acDot3adAggPortStatsEntry.setIndexNames(
    (0, "AC-LAG-MIB", "acDot3adAggPortNodeIdIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortSlotIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortPortIndex"),
)
if mibBuilder.loadTexts:
    acDot3adAggPortStatsEntry.setStatus("current")
_AcDot3adAggPortStatsLACPDUsRx_Type = Counter32
_AcDot3adAggPortStatsLACPDUsRx_Object = MibTableColumn
acDot3adAggPortStatsLACPDUsRx = _AcDot3adAggPortStatsLACPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 1),
    _AcDot3adAggPortStatsLACPDUsRx_Type()
)
acDot3adAggPortStatsLACPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsLACPDUsRx.setStatus("current")
_AcDot3adAggPortStatsMarkerPDUsRx_Type = Counter32
_AcDot3adAggPortStatsMarkerPDUsRx_Object = MibTableColumn
acDot3adAggPortStatsMarkerPDUsRx = _AcDot3adAggPortStatsMarkerPDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 2),
    _AcDot3adAggPortStatsMarkerPDUsRx_Type()
)
acDot3adAggPortStatsMarkerPDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsMarkerPDUsRx.setStatus("current")
_AcDot3adAggPortStatsMarkerResponsePDUsRx_Type = Counter32
_AcDot3adAggPortStatsMarkerResponsePDUsRx_Object = MibTableColumn
acDot3adAggPortStatsMarkerResponsePDUsRx = _AcDot3adAggPortStatsMarkerResponsePDUsRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 3),
    _AcDot3adAggPortStatsMarkerResponsePDUsRx_Type()
)
acDot3adAggPortStatsMarkerResponsePDUsRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsMarkerResponsePDUsRx.setStatus("current")
_AcDot3adAggPortStatsUnknownRx_Type = Counter32
_AcDot3adAggPortStatsUnknownRx_Object = MibTableColumn
acDot3adAggPortStatsUnknownRx = _AcDot3adAggPortStatsUnknownRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 4),
    _AcDot3adAggPortStatsUnknownRx_Type()
)
acDot3adAggPortStatsUnknownRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsUnknownRx.setStatus("current")
_AcDot3adAggPortStatsIllegalRx_Type = Counter32
_AcDot3adAggPortStatsIllegalRx_Object = MibTableColumn
acDot3adAggPortStatsIllegalRx = _AcDot3adAggPortStatsIllegalRx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 5),
    _AcDot3adAggPortStatsIllegalRx_Type()
)
acDot3adAggPortStatsIllegalRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsIllegalRx.setStatus("current")
_AcDot3adAggPortStatsLACPDUsTx_Type = Counter32
_AcDot3adAggPortStatsLACPDUsTx_Object = MibTableColumn
acDot3adAggPortStatsLACPDUsTx = _AcDot3adAggPortStatsLACPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 6),
    _AcDot3adAggPortStatsLACPDUsTx_Type()
)
acDot3adAggPortStatsLACPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsLACPDUsTx.setStatus("current")
_AcDot3adAggPortStatsMarkerPDUsTx_Type = Counter32
_AcDot3adAggPortStatsMarkerPDUsTx_Object = MibTableColumn
acDot3adAggPortStatsMarkerPDUsTx = _AcDot3adAggPortStatsMarkerPDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 7),
    _AcDot3adAggPortStatsMarkerPDUsTx_Type()
)
acDot3adAggPortStatsMarkerPDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsMarkerPDUsTx.setStatus("current")
_AcDot3adAggPortStatsMarkerResponsePDUsTx_Type = Counter32
_AcDot3adAggPortStatsMarkerResponsePDUsTx_Object = MibTableColumn
acDot3adAggPortStatsMarkerResponsePDUsTx = _AcDot3adAggPortStatsMarkerResponsePDUsTx_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 2, 1, 8),
    _AcDot3adAggPortStatsMarkerResponsePDUsTx_Type()
)
acDot3adAggPortStatsMarkerResponsePDUsTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortStatsMarkerResponsePDUsTx.setStatus("current")
_AcDot3adAggPortDebugTable_Object = MibTable
acDot3adAggPortDebugTable = _AcDot3adAggPortDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    acDot3adAggPortDebugTable.setStatus("current")
_AcDot3adAggPortDebugEntry_Object = MibTableRow
acDot3adAggPortDebugEntry = _AcDot3adAggPortDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1)
)
acDot3adAggPortDebugEntry.setIndexNames(
    (0, "AC-LAG-MIB", "acDot3adAggPortNodeIdIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortSlotIndex"),
    (0, "AC-LAG-MIB", "acDot3adAggPortPortIndex"),
)
if mibBuilder.loadTexts:
    acDot3adAggPortDebugEntry.setStatus("current")


class _AcDot3adAggPortDebugRxState_Type(Integer32):
    """Custom type acDot3adAggPortDebugRxState based on Integer32"""
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


_AcDot3adAggPortDebugRxState_Type.__name__ = "Integer32"
_AcDot3adAggPortDebugRxState_Object = MibTableColumn
acDot3adAggPortDebugRxState = _AcDot3adAggPortDebugRxState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 1),
    _AcDot3adAggPortDebugRxState_Type()
)
acDot3adAggPortDebugRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugRxState.setStatus("current")
_AcDot3adAggPortDebugLastRxTime_Type = TimeTicks
_AcDot3adAggPortDebugLastRxTime_Object = MibTableColumn
acDot3adAggPortDebugLastRxTime = _AcDot3adAggPortDebugLastRxTime_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 2),
    _AcDot3adAggPortDebugLastRxTime_Type()
)
acDot3adAggPortDebugLastRxTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugLastRxTime.setStatus("current")


class _AcDot3adAggPortDebugMuxState_Type(Integer32):
    """Custom type acDot3adAggPortDebugMuxState based on Integer32"""
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


_AcDot3adAggPortDebugMuxState_Type.__name__ = "Integer32"
_AcDot3adAggPortDebugMuxState_Object = MibTableColumn
acDot3adAggPortDebugMuxState = _AcDot3adAggPortDebugMuxState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 3),
    _AcDot3adAggPortDebugMuxState_Type()
)
acDot3adAggPortDebugMuxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugMuxState.setStatus("current")
_AcDot3adAggPortDebugMuxReason_Type = DisplayString
_AcDot3adAggPortDebugMuxReason_Object = MibTableColumn
acDot3adAggPortDebugMuxReason = _AcDot3adAggPortDebugMuxReason_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 4),
    _AcDot3adAggPortDebugMuxReason_Type()
)
acDot3adAggPortDebugMuxReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugMuxReason.setStatus("current")
_AcDot3adAggPortDebugActorChurnState_Type = ChurnState
_AcDot3adAggPortDebugActorChurnState_Object = MibTableColumn
acDot3adAggPortDebugActorChurnState = _AcDot3adAggPortDebugActorChurnState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 5),
    _AcDot3adAggPortDebugActorChurnState_Type()
)
acDot3adAggPortDebugActorChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugActorChurnState.setStatus("current")
_AcDot3adAggPortDebugPartnerChurnState_Type = ChurnState
_AcDot3adAggPortDebugPartnerChurnState_Object = MibTableColumn
acDot3adAggPortDebugPartnerChurnState = _AcDot3adAggPortDebugPartnerChurnState_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 6),
    _AcDot3adAggPortDebugPartnerChurnState_Type()
)
acDot3adAggPortDebugPartnerChurnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugPartnerChurnState.setStatus("current")
_AcDot3adAggPortDebugActorChurnCount_Type = Counter32
_AcDot3adAggPortDebugActorChurnCount_Object = MibTableColumn
acDot3adAggPortDebugActorChurnCount = _AcDot3adAggPortDebugActorChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 7),
    _AcDot3adAggPortDebugActorChurnCount_Type()
)
acDot3adAggPortDebugActorChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugActorChurnCount.setStatus("current")
_AcDot3adAggPortDebugPartnerChurnCount_Type = Counter32
_AcDot3adAggPortDebugPartnerChurnCount_Object = MibTableColumn
acDot3adAggPortDebugPartnerChurnCount = _AcDot3adAggPortDebugPartnerChurnCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 8),
    _AcDot3adAggPortDebugPartnerChurnCount_Type()
)
acDot3adAggPortDebugPartnerChurnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugPartnerChurnCount.setStatus("current")
_AcDot3adAggPortDebugActorSyncTransitionCount_Type = Counter32
_AcDot3adAggPortDebugActorSyncTransitionCount_Object = MibTableColumn
acDot3adAggPortDebugActorSyncTransitionCount = _AcDot3adAggPortDebugActorSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 9),
    _AcDot3adAggPortDebugActorSyncTransitionCount_Type()
)
acDot3adAggPortDebugActorSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugActorSyncTransitionCount.setStatus("current")
_AcDot3adAggPortDebugPartnerSyncTransitionCount_Type = Counter32
_AcDot3adAggPortDebugPartnerSyncTransitionCount_Object = MibTableColumn
acDot3adAggPortDebugPartnerSyncTransitionCount = _AcDot3adAggPortDebugPartnerSyncTransitionCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 10),
    _AcDot3adAggPortDebugPartnerSyncTransitionCount_Type()
)
acDot3adAggPortDebugPartnerSyncTransitionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugPartnerSyncTransitionCount.setStatus("current")
_AcDot3adAggPortDebugActorChangeCount_Type = Counter32
_AcDot3adAggPortDebugActorChangeCount_Object = MibTableColumn
acDot3adAggPortDebugActorChangeCount = _AcDot3adAggPortDebugActorChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 11),
    _AcDot3adAggPortDebugActorChangeCount_Type()
)
acDot3adAggPortDebugActorChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugActorChangeCount.setStatus("current")
_AcDot3adAggPortDebugPartnerChangeCount_Type = Counter32
_AcDot3adAggPortDebugPartnerChangeCount_Object = MibTableColumn
acDot3adAggPortDebugPartnerChangeCount = _AcDot3adAggPortDebugPartnerChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 2, 3, 1, 12),
    _AcDot3adAggPortDebugPartnerChangeCount_Type()
)
acDot3adAggPortDebugPartnerChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adAggPortDebugPartnerChangeCount.setStatus("current")
_AcDot3adTablesLastChanged_Type = TimeTicks
_AcDot3adTablesLastChanged_Object = MibScalar
acDot3adTablesLastChanged = _AcDot3adTablesLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 1, 3),
    _AcDot3adTablesLastChanged_Type()
)
acDot3adTablesLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acDot3adTablesLastChanged.setStatus("current")
_AcDot3adAggConformance_ObjectIdentity = ObjectIdentity
acDot3adAggConformance = _AcDot3adAggConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2)
)
_AcDot3adAggGroups_ObjectIdentity = ObjectIdentity
acDot3adAggGroups = _AcDot3adAggGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1)
)
_AcDot3adAggCompliances_ObjectIdentity = ObjectIdentity
acDot3adAggCompliances = _AcDot3adAggCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 2)
)

# Managed Objects groups

acDot3adAggGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 1)
)
acDot3adAggGroup.setObjects(
      *(("AC-LAG-MIB", "acDot3adAggActorSystemID"),
        ("AC-LAG-MIB", "acDot3adAggActorSystemPriority"),
        ("AC-LAG-MIB", "acDot3adAggAggregateOrIndividual"),
        ("AC-LAG-MIB", "acDot3adAggActorAdminKey"),
        ("AC-LAG-MIB", "acDot3adAggMACAddress"),
        ("AC-LAG-MIB", "acDot3adAggActorOperKey"),
        ("AC-LAG-MIB", "acDot3adAggPartnerSystemID"),
        ("AC-LAG-MIB", "acDot3adAggPartnerSystemPriority"),
        ("AC-LAG-MIB", "acDot3adAggPartnerOperKey"),
        ("AC-LAG-MIB", "acDot3adAggCollectorMaxDelay"))
)
if mibBuilder.loadTexts:
    acDot3adAggGroup.setStatus("current")

acDot3adTablesLastChangedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 1, 6)
)
acDot3adTablesLastChangedGroup.setObjects(
    ("AC-LAG-MIB", "acDot3adTablesLastChanged")
)
if mibBuilder.loadTexts:
    acDot3adTablesLastChangedGroup.setStatus("current")

acDot3adAggPortListGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 2)
)
acDot3adAggPortListGroup.setObjects(
    ("AC-LAG-MIB", "acDot3adAggPortListPorts")
)
if mibBuilder.loadTexts:
    acDot3adAggPortListGroup.setStatus("current")

acDot3adAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 3)
)
acDot3adAggPortGroup.setObjects(
      *(("AC-LAG-MIB", "acDot3adAggPortActorSystemPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortActorSystemID"),
        ("AC-LAG-MIB", "acDot3adAggPortActorAdminKey"),
        ("AC-LAG-MIB", "acDot3adAggPortActorOperKey"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminSystemPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperSystemPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminSystemID"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperSystemID"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminKey"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperKey"),
        ("AC-LAG-MIB", "acDot3adAggPortSelectedAggID"),
        ("AC-LAG-MIB", "acDot3adAggPortAttachedAggID"),
        ("AC-LAG-MIB", "acDot3adAggPortActorPort"),
        ("AC-LAG-MIB", "acDot3adAggPortActorPortPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminPort"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperPort"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminPortPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperPortPriority"),
        ("AC-LAG-MIB", "acDot3adAggPortActorAdminState"),
        ("AC-LAG-MIB", "acDot3adAggPortActorOperState"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerAdminState"),
        ("AC-LAG-MIB", "acDot3adAggPortPartnerOperState"),
        ("AC-LAG-MIB", "acDot3adAggPortAggregateOrIndividual"))
)
if mibBuilder.loadTexts:
    acDot3adAggPortGroup.setStatus("current")

acDot3adAggPortStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 4)
)
acDot3adAggPortStatsGroup.setObjects(
      *(("AC-LAG-MIB", "acDot3adAggPortStatsLACPDUsRx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsMarkerPDUsRx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsMarkerResponsePDUsRx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsUnknownRx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsIllegalRx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsLACPDUsTx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsMarkerPDUsTx"),
        ("AC-LAG-MIB", "acDot3adAggPortStatsMarkerResponsePDUsTx"))
)
if mibBuilder.loadTexts:
    acDot3adAggPortStatsGroup.setStatus("current")

acDot3adAggPortDebugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 1, 5)
)
acDot3adAggPortDebugGroup.setObjects(
      *(("AC-LAG-MIB", "acDot3adAggPortDebugRxState"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugLastRxTime"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugMuxState"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugMuxReason"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugActorChurnState"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugPartnerChurnState"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugActorChurnCount"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugPartnerChurnCount"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugActorSyncTransitionCount"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugPartnerSyncTransitionCount"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugActorChangeCount"),
        ("AC-LAG-MIB", "acDot3adAggPortDebugPartnerChangeCount"))
)
if mibBuilder.loadTexts:
    acDot3adAggPortDebugGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

acDot3adAggCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2785, 2, 3, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    acDot3adAggCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-LAG-MIB",
    **{"LacpKey": LacpKey,
       "LacpState": LacpState,
       "ChurnState": ChurnState,
       "PortList": PortList,
       "AcAggInstanceIndex": AcAggInstanceIndex,
       "AcAggInstanceValue": AcAggInstanceValue,
       "acLagMIB": acLagMIB,
       "lagMIBObjects": lagMIBObjects,
       "acDot3adAgg": acDot3adAgg,
       "acDot3adAggTable": acDot3adAggTable,
       "acDot3adAggEntry": acDot3adAggEntry,
       "acDot3adAggNodeIdIndex": acDot3adAggNodeIdIndex,
       "acDot3adAggInstanceIndex": acDot3adAggInstanceIndex,
       "acDot3adAggMACAddress": acDot3adAggMACAddress,
       "acDot3adAggActorSystemPriority": acDot3adAggActorSystemPriority,
       "acDot3adAggActorSystemID": acDot3adAggActorSystemID,
       "acDot3adAggAggregateOrIndividual": acDot3adAggAggregateOrIndividual,
       "acDot3adAggActorAdminKey": acDot3adAggActorAdminKey,
       "acDot3adAggActorOperKey": acDot3adAggActorOperKey,
       "acDot3adAggPartnerSystemID": acDot3adAggPartnerSystemID,
       "acDot3adAggPartnerSystemPriority": acDot3adAggPartnerSystemPriority,
       "acDot3adAggPartnerOperKey": acDot3adAggPartnerOperKey,
       "acDot3adAggCollectorMaxDelay": acDot3adAggCollectorMaxDelay,
       "acDot3adAggPortListTable": acDot3adAggPortListTable,
       "acDot3adAggPortListEntry": acDot3adAggPortListEntry,
       "acDot3adAggPortListPorts": acDot3adAggPortListPorts,
       "acDot3adAggPort": acDot3adAggPort,
       "acDot3adAggPortTable": acDot3adAggPortTable,
       "acDot3adAggPortEntry": acDot3adAggPortEntry,
       "acDot3adAggPortNodeIdIndex": acDot3adAggPortNodeIdIndex,
       "acDot3adAggPortSlotIndex": acDot3adAggPortSlotIndex,
       "acDot3adAggPortPortIndex": acDot3adAggPortPortIndex,
       "acDot3adAggPortActorSystemPriority": acDot3adAggPortActorSystemPriority,
       "acDot3adAggPortActorSystemID": acDot3adAggPortActorSystemID,
       "acDot3adAggPortActorAdminKey": acDot3adAggPortActorAdminKey,
       "acDot3adAggPortActorOperKey": acDot3adAggPortActorOperKey,
       "acDot3adAggPortPartnerAdminSystemPriority": acDot3adAggPortPartnerAdminSystemPriority,
       "acDot3adAggPortPartnerOperSystemPriority": acDot3adAggPortPartnerOperSystemPriority,
       "acDot3adAggPortPartnerAdminSystemID": acDot3adAggPortPartnerAdminSystemID,
       "acDot3adAggPortPartnerOperSystemID": acDot3adAggPortPartnerOperSystemID,
       "acDot3adAggPortPartnerAdminKey": acDot3adAggPortPartnerAdminKey,
       "acDot3adAggPortPartnerOperKey": acDot3adAggPortPartnerOperKey,
       "acDot3adAggPortSelectedAggID": acDot3adAggPortSelectedAggID,
       "acDot3adAggPortAttachedAggID": acDot3adAggPortAttachedAggID,
       "acDot3adAggPortActorPort": acDot3adAggPortActorPort,
       "acDot3adAggPortActorPortPriority": acDot3adAggPortActorPortPriority,
       "acDot3adAggPortPartnerAdminPort": acDot3adAggPortPartnerAdminPort,
       "acDot3adAggPortPartnerOperPort": acDot3adAggPortPartnerOperPort,
       "acDot3adAggPortPartnerAdminPortPriority": acDot3adAggPortPartnerAdminPortPriority,
       "acDot3adAggPortPartnerOperPortPriority": acDot3adAggPortPartnerOperPortPriority,
       "acDot3adAggPortActorAdminState": acDot3adAggPortActorAdminState,
       "acDot3adAggPortActorOperState": acDot3adAggPortActorOperState,
       "acDot3adAggPortPartnerAdminState": acDot3adAggPortPartnerAdminState,
       "acDot3adAggPortPartnerOperState": acDot3adAggPortPartnerOperState,
       "acDot3adAggPortAggregateOrIndividual": acDot3adAggPortAggregateOrIndividual,
       "acDot3adAggPortStatsTable": acDot3adAggPortStatsTable,
       "acDot3adAggPortStatsEntry": acDot3adAggPortStatsEntry,
       "acDot3adAggPortStatsLACPDUsRx": acDot3adAggPortStatsLACPDUsRx,
       "acDot3adAggPortStatsMarkerPDUsRx": acDot3adAggPortStatsMarkerPDUsRx,
       "acDot3adAggPortStatsMarkerResponsePDUsRx": acDot3adAggPortStatsMarkerResponsePDUsRx,
       "acDot3adAggPortStatsUnknownRx": acDot3adAggPortStatsUnknownRx,
       "acDot3adAggPortStatsIllegalRx": acDot3adAggPortStatsIllegalRx,
       "acDot3adAggPortStatsLACPDUsTx": acDot3adAggPortStatsLACPDUsTx,
       "acDot3adAggPortStatsMarkerPDUsTx": acDot3adAggPortStatsMarkerPDUsTx,
       "acDot3adAggPortStatsMarkerResponsePDUsTx": acDot3adAggPortStatsMarkerResponsePDUsTx,
       "acDot3adAggPortDebugTable": acDot3adAggPortDebugTable,
       "acDot3adAggPortDebugEntry": acDot3adAggPortDebugEntry,
       "acDot3adAggPortDebugRxState": acDot3adAggPortDebugRxState,
       "acDot3adAggPortDebugLastRxTime": acDot3adAggPortDebugLastRxTime,
       "acDot3adAggPortDebugMuxState": acDot3adAggPortDebugMuxState,
       "acDot3adAggPortDebugMuxReason": acDot3adAggPortDebugMuxReason,
       "acDot3adAggPortDebugActorChurnState": acDot3adAggPortDebugActorChurnState,
       "acDot3adAggPortDebugPartnerChurnState": acDot3adAggPortDebugPartnerChurnState,
       "acDot3adAggPortDebugActorChurnCount": acDot3adAggPortDebugActorChurnCount,
       "acDot3adAggPortDebugPartnerChurnCount": acDot3adAggPortDebugPartnerChurnCount,
       "acDot3adAggPortDebugActorSyncTransitionCount": acDot3adAggPortDebugActorSyncTransitionCount,
       "acDot3adAggPortDebugPartnerSyncTransitionCount": acDot3adAggPortDebugPartnerSyncTransitionCount,
       "acDot3adAggPortDebugActorChangeCount": acDot3adAggPortDebugActorChangeCount,
       "acDot3adAggPortDebugPartnerChangeCount": acDot3adAggPortDebugPartnerChangeCount,
       "acDot3adTablesLastChanged": acDot3adTablesLastChanged,
       "acDot3adAggConformance": acDot3adAggConformance,
       "acDot3adAggGroups": acDot3adAggGroups,
       "acDot3adAggGroup": acDot3adAggGroup,
       "acDot3adTablesLastChangedGroup": acDot3adTablesLastChangedGroup,
       "acDot3adAggPortListGroup": acDot3adAggPortListGroup,
       "acDot3adAggPortGroup": acDot3adAggPortGroup,
       "acDot3adAggPortStatsGroup": acDot3adAggPortStatsGroup,
       "acDot3adAggPortDebugGroup": acDot3adAggPortDebugGroup,
       "acDot3adAggCompliances": acDot3adAggCompliances,
       "acDot3adAggCompliance": acDot3adAggCompliance}
)
