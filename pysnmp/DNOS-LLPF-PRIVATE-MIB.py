# SNMP MIB module (DNOS-LLPF-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-LLPF-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:02 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathLlpf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48)
)
fastPathLlpf.setRevisions(
        ("2011-01-26 00:00",
         "2009-10-26 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSwitchLlpfGroup_ObjectIdentity = ObjectIdentity
agentSwitchLlpfGroup = _AgentSwitchLlpfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1)
)
_AgentSwitchLlpfPortConfigTable_Object = MibTable
agentSwitchLlpfPortConfigTable = _AgentSwitchLlpfPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1)
)
if mibBuilder.loadTexts:
    agentSwitchLlpfPortConfigTable.setStatus("current")
_AgentSwitchLlpfPortConfigEntry_Object = MibTableRow
agentSwitchLlpfPortConfigEntry = _AgentSwitchLlpfPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1)
)
agentSwitchLlpfPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DNOS-LLPF-PRIVATE-MIB", "agentSwitchLlpfProtocolType"),
)
if mibBuilder.loadTexts:
    agentSwitchLlpfPortConfigEntry.setStatus("current")


class _AgentSwitchLlpfProtocolType_Type(Unsigned32):
    """Custom type agentSwitchLlpfProtocolType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_AgentSwitchLlpfProtocolType_Type.__name__ = "Unsigned32"
_AgentSwitchLlpfProtocolType_Object = MibTableColumn
agentSwitchLlpfProtocolType = _AgentSwitchLlpfProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 1),
    _AgentSwitchLlpfProtocolType_Type()
)
agentSwitchLlpfProtocolType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentSwitchLlpfProtocolType.setStatus("current")


class _AgentSwitchLlpfPortBlockMode_Type(Integer32):
    """Custom type agentSwitchLlpfPortBlockMode based on Integer32"""
    defaultValue = 2

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


_AgentSwitchLlpfPortBlockMode_Type.__name__ = "Integer32"
_AgentSwitchLlpfPortBlockMode_Object = MibTableColumn
agentSwitchLlpfPortBlockMode = _AgentSwitchLlpfPortBlockMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 48, 1, 1, 1, 2),
    _AgentSwitchLlpfPortBlockMode_Type()
)
agentSwitchLlpfPortBlockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwitchLlpfPortBlockMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-LLPF-PRIVATE-MIB",
    **{"fastPathLlpf": fastPathLlpf,
       "agentSwitchLlpfGroup": agentSwitchLlpfGroup,
       "agentSwitchLlpfPortConfigTable": agentSwitchLlpfPortConfigTable,
       "agentSwitchLlpfPortConfigEntry": agentSwitchLlpfPortConfigEntry,
       "agentSwitchLlpfProtocolType": agentSwitchLlpfProtocolType,
       "agentSwitchLlpfPortBlockMode": agentSwitchLlpfPortBlockMode}
)
