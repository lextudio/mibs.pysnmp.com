# SNMP MIB module (TIARA-NETWORKS-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TIARA-NETWORKS-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:41 2024
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

(tiaraMgmt,) = mibBuilder.importSymbols(
    "TIARA-NETWORKS-SMI",
    "tiaraMgmt")


# MODULE-IDENTITY

tiaraSnmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5)
)
tiaraSnmpMib.setRevisions(
        ("1999-04-23 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpObjects_ObjectIdentity = ObjectIdentity
snmpObjects = _SnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1)
)


class _SnmpAgentType_Type(Integer32):
    """Custom type snmpAgentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("snmpV1", 2),
          ("snmpV2V1", 3),
          ("snmpV2cV1", 4))
    )


_SnmpAgentType_Type.__name__ = "Integer32"
_SnmpAgentType_Object = MibScalar
snmpAgentType = _SnmpAgentType_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 1),
    _SnmpAgentType_Type()
)
snmpAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpAgentType.setStatus("current")


class _SnmpRmonSupported_Type(Integer32):
    """Custom type snmpRmonSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 2),
          ("supported", 1))
    )


_SnmpRmonSupported_Type.__name__ = "Integer32"
_SnmpRmonSupported_Object = MibScalar
snmpRmonSupported = _SnmpRmonSupported_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 2),
    _SnmpRmonSupported_Type()
)
snmpRmonSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpRmonSupported.setStatus("current")
_SnmpTrapRcvrTable_Object = MibTable
snmpTrapRcvrTable = _SnmpTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4)
)
if mibBuilder.loadTexts:
    snmpTrapRcvrTable.setStatus("current")
_SnmpTrapRcvrEntry_Object = MibTableRow
snmpTrapRcvrEntry = _SnmpTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1)
)
snmpTrapRcvrEntry.setIndexNames(
    (0, "TIARA-NETWORKS-SNMP-MIB", "snmpTrapRcvrAddress"),
)
if mibBuilder.loadTexts:
    snmpTrapRcvrEntry.setStatus("current")


class _SnmpTrapRcvrEntryStatus_Type(Integer32):
    """Custom type snmpTrapRcvrEntryStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SnmpTrapRcvrEntryStatus_Type.__name__ = "Integer32"
_SnmpTrapRcvrEntryStatus_Object = MibTableColumn
snmpTrapRcvrEntryStatus = _SnmpTrapRcvrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 1),
    _SnmpTrapRcvrEntryStatus_Type()
)
snmpTrapRcvrEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvrEntryStatus.setStatus("current")
_SnmpTrapRcvrAddress_Type = IpAddress
_SnmpTrapRcvrAddress_Object = MibTableColumn
snmpTrapRcvrAddress = _SnmpTrapRcvrAddress_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 2),
    _SnmpTrapRcvrAddress_Type()
)
snmpTrapRcvrAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvrAddress.setStatus("current")


class _SnmpTrapRcvrCommunity_Type(DisplayString):
    """Custom type snmpTrapRcvrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnmpTrapRcvrCommunity_Type.__name__ = "DisplayString"
_SnmpTrapRcvrCommunity_Object = MibTableColumn
snmpTrapRcvrCommunity = _SnmpTrapRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3174, 2, 5, 1, 4, 1, 3),
    _SnmpTrapRcvrCommunity_Type()
)
snmpTrapRcvrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapRcvrCommunity.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIARA-NETWORKS-SNMP-MIB",
    **{"tiaraSnmpMib": tiaraSnmpMib,
       "snmpObjects": snmpObjects,
       "snmpAgentType": snmpAgentType,
       "snmpRmonSupported": snmpRmonSupported,
       "snmpTrapRcvrTable": snmpTrapRcvrTable,
       "snmpTrapRcvrEntry": snmpTrapRcvrEntry,
       "snmpTrapRcvrEntryStatus": snmpTrapRcvrEntryStatus,
       "snmpTrapRcvrAddress": snmpTrapRcvrAddress,
       "snmpTrapRcvrCommunity": snmpTrapRcvrCommunity}
)
