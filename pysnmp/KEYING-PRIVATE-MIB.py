# SNMP MIB module (KEYING-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/KEYING-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:42 2024
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

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

keyingPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentFeatureKeyingGroup_ObjectIdentity = ObjectIdentity
agentFeatureKeyingGroup = _AgentFeatureKeyingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1)
)
_AgentFeatureKeyingEnableKey_Type = DisplayString
_AgentFeatureKeyingEnableKey_Object = MibScalar
agentFeatureKeyingEnableKey = _AgentFeatureKeyingEnableKey_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 1),
    _AgentFeatureKeyingEnableKey_Type()
)
agentFeatureKeyingEnableKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFeatureKeyingEnableKey.setStatus("current")
_AgentFeatureKeyingDisableKey_Type = DisplayString
_AgentFeatureKeyingDisableKey_Object = MibScalar
agentFeatureKeyingDisableKey = _AgentFeatureKeyingDisableKey_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 2),
    _AgentFeatureKeyingDisableKey_Type()
)
agentFeatureKeyingDisableKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFeatureKeyingDisableKey.setStatus("current")
_AgentFeatureKeyingTable_Object = MibTable
agentFeatureKeyingTable = _AgentFeatureKeyingTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3)
)
if mibBuilder.loadTexts:
    agentFeatureKeyingTable.setStatus("current")
_AgentFeatureKeyingEntry_Object = MibTableRow
agentFeatureKeyingEntry = _AgentFeatureKeyingEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1)
)
agentFeatureKeyingEntry.setIndexNames(
    (0, "KEYING-PRIVATE-MIB", "agentFeatureKeyingIndex"),
)
if mibBuilder.loadTexts:
    agentFeatureKeyingEntry.setStatus("current")
_AgentFeatureKeyingIndex_Type = Unsigned32
_AgentFeatureKeyingIndex_Object = MibTableColumn
agentFeatureKeyingIndex = _AgentFeatureKeyingIndex_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 1),
    _AgentFeatureKeyingIndex_Type()
)
agentFeatureKeyingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFeatureKeyingIndex.setStatus("current")
_AgentFeatureKeyingName_Type = DisplayString
_AgentFeatureKeyingName_Object = MibTableColumn
agentFeatureKeyingName = _AgentFeatureKeyingName_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 2),
    _AgentFeatureKeyingName_Type()
)
agentFeatureKeyingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFeatureKeyingName.setStatus("current")


class _AgentFeatureKeyingStatus_Type(Integer32):
    """Custom type agentFeatureKeyingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentFeatureKeyingStatus_Type.__name__ = "Integer32"
_AgentFeatureKeyingStatus_Object = MibTableColumn
agentFeatureKeyingStatus = _AgentFeatureKeyingStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 24, 1, 3, 1, 3),
    _AgentFeatureKeyingStatus_Type()
)
agentFeatureKeyingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFeatureKeyingStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KEYING-PRIVATE-MIB",
    **{"keyingPrivate": keyingPrivate,
       "agentFeatureKeyingGroup": agentFeatureKeyingGroup,
       "agentFeatureKeyingEnableKey": agentFeatureKeyingEnableKey,
       "agentFeatureKeyingDisableKey": agentFeatureKeyingDisableKey,
       "agentFeatureKeyingTable": agentFeatureKeyingTable,
       "agentFeatureKeyingEntry": agentFeatureKeyingEntry,
       "agentFeatureKeyingIndex": agentFeatureKeyingIndex,
       "agentFeatureKeyingName": agentFeatureKeyingName,
       "agentFeatureKeyingStatus": agentFeatureKeyingStatus}
)
