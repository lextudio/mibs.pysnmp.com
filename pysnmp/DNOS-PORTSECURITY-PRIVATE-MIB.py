# SNMP MIB module (DNOS-PORTSECURITY-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-PORTSECURITY-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:11 2024
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

fastPathPortSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20)
)
fastPathPortSecurity.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentPortSecurityGroup_ObjectIdentity = ObjectIdentity
agentPortSecurityGroup = _AgentPortSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1)
)


class _AgentGlobalPortSecurityMode_Type(Integer32):
    """Custom type agentGlobalPortSecurityMode based on Integer32"""
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


_AgentGlobalPortSecurityMode_Type.__name__ = "Integer32"
_AgentGlobalPortSecurityMode_Object = MibScalar
agentGlobalPortSecurityMode = _AgentGlobalPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 1),
    _AgentGlobalPortSecurityMode_Type()
)
agentGlobalPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGlobalPortSecurityMode.setStatus("current")
_AgentPortSecurityTable_Object = MibTable
agentPortSecurityTable = _AgentPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    agentPortSecurityTable.setStatus("current")
_AgentPortSecurityEntry_Object = MibTableRow
agentPortSecurityEntry = _AgentPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1)
)
agentPortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    agentPortSecurityEntry.setStatus("current")


class _AgentPortSecurityMode_Type(Integer32):
    """Custom type agentPortSecurityMode based on Integer32"""
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


_AgentPortSecurityMode_Type.__name__ = "Integer32"
_AgentPortSecurityMode_Object = MibTableColumn
agentPortSecurityMode = _AgentPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 1),
    _AgentPortSecurityMode_Type()
)
agentPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityMode.setStatus("current")


class _AgentPortSecurityDynamicLimit_Type(Unsigned32):
    """Custom type agentPortSecurityDynamicLimit based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_AgentPortSecurityDynamicLimit_Type.__name__ = "Unsigned32"
_AgentPortSecurityDynamicLimit_Object = MibTableColumn
agentPortSecurityDynamicLimit = _AgentPortSecurityDynamicLimit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 2),
    _AgentPortSecurityDynamicLimit_Type()
)
agentPortSecurityDynamicLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityDynamicLimit.setStatus("current")


class _AgentPortSecurityStaticLimit_Type(Unsigned32):
    """Custom type agentPortSecurityStaticLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentPortSecurityStaticLimit_Type.__name__ = "Unsigned32"
_AgentPortSecurityStaticLimit_Object = MibTableColumn
agentPortSecurityStaticLimit = _AgentPortSecurityStaticLimit_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 3),
    _AgentPortSecurityStaticLimit_Type()
)
agentPortSecurityStaticLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityStaticLimit.setStatus("current")


class _AgentPortSecurityViolationTrapMode_Type(Integer32):
    """Custom type agentPortSecurityViolationTrapMode based on Integer32"""
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


_AgentPortSecurityViolationTrapMode_Type.__name__ = "Integer32"
_AgentPortSecurityViolationTrapMode_Object = MibTableColumn
agentPortSecurityViolationTrapMode = _AgentPortSecurityViolationTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 4),
    _AgentPortSecurityViolationTrapMode_Type()
)
agentPortSecurityViolationTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityViolationTrapMode.setStatus("current")
_AgentPortSecurityStaticMACs_Type = DisplayString
_AgentPortSecurityStaticMACs_Object = MibTableColumn
agentPortSecurityStaticMACs = _AgentPortSecurityStaticMACs_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 6),
    _AgentPortSecurityStaticMACs_Type()
)
agentPortSecurityStaticMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSecurityStaticMACs.setStatus("current")
_AgentPortSecurityLastDiscardedMAC_Type = DisplayString
_AgentPortSecurityLastDiscardedMAC_Object = MibTableColumn
agentPortSecurityLastDiscardedMAC = _AgentPortSecurityLastDiscardedMAC_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 7),
    _AgentPortSecurityLastDiscardedMAC_Type()
)
agentPortSecurityLastDiscardedMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSecurityLastDiscardedMAC.setStatus("current")
_AgentPortSecurityMACAddressAdd_Type = DisplayString
_AgentPortSecurityMACAddressAdd_Object = MibTableColumn
agentPortSecurityMACAddressAdd = _AgentPortSecurityMACAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 8),
    _AgentPortSecurityMACAddressAdd_Type()
)
agentPortSecurityMACAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityMACAddressAdd.setStatus("current")
_AgentPortSecurityMACAddressRemove_Type = DisplayString
_AgentPortSecurityMACAddressRemove_Object = MibTableColumn
agentPortSecurityMACAddressRemove = _AgentPortSecurityMACAddressRemove_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 9),
    _AgentPortSecurityMACAddressRemove_Type()
)
agentPortSecurityMACAddressRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityMACAddressRemove.setStatus("current")


class _AgentPortSecurityMACAddressMove_Type(Integer32):
    """Custom type agentPortSecurityMACAddressMove based on Integer32"""
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


_AgentPortSecurityMACAddressMove_Type.__name__ = "Integer32"
_AgentPortSecurityMACAddressMove_Object = MibTableColumn
agentPortSecurityMACAddressMove = _AgentPortSecurityMACAddressMove_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 10),
    _AgentPortSecurityMACAddressMove_Type()
)
agentPortSecurityMACAddressMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityMACAddressMove.setStatus("current")


class _AgentPortSecurityStickyMode_Type(Integer32):
    """Custom type agentPortSecurityStickyMode based on Integer32"""
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


_AgentPortSecurityStickyMode_Type.__name__ = "Integer32"
_AgentPortSecurityStickyMode_Object = MibTableColumn
agentPortSecurityStickyMode = _AgentPortSecurityStickyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 2, 1, 11),
    _AgentPortSecurityStickyMode_Type()
)
agentPortSecurityStickyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentPortSecurityStickyMode.setStatus("current")
_AgentPortSecurityDynamicTable_Object = MibTable
agentPortSecurityDynamicTable = _AgentPortSecurityDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 3)
)
if mibBuilder.loadTexts:
    agentPortSecurityDynamicTable.setStatus("current")
_AgentPortSecurityDynamicEntry_Object = MibTableRow
agentPortSecurityDynamicEntry = _AgentPortSecurityDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 3, 1)
)
agentPortSecurityDynamicEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "DNOS-PORTSECURITY-PRIVATE-MIB", "agentPortSecurityDynamicVLANId"),
    (0, "DNOS-PORTSECURITY-PRIVATE-MIB", "agentPortSecurityDynamicMACAddress"),
)
if mibBuilder.loadTexts:
    agentPortSecurityDynamicEntry.setStatus("current")
_AgentPortSecurityDynamicVLANId_Type = Unsigned32
_AgentPortSecurityDynamicVLANId_Object = MibTableColumn
agentPortSecurityDynamicVLANId = _AgentPortSecurityDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 3, 1, 1),
    _AgentPortSecurityDynamicVLANId_Type()
)
agentPortSecurityDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSecurityDynamicVLANId.setStatus("current")
_AgentPortSecurityDynamicMACAddress_Type = MacAddress
_AgentPortSecurityDynamicMACAddress_Object = MibTableColumn
agentPortSecurityDynamicMACAddress = _AgentPortSecurityDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 3, 1, 2),
    _AgentPortSecurityDynamicMACAddress_Type()
)
agentPortSecurityDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPortSecurityDynamicMACAddress.setStatus("current")


class _AgentGlobalPortSecurityStickyMode_Type(Integer32):
    """Custom type agentGlobalPortSecurityStickyMode based on Integer32"""
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


_AgentGlobalPortSecurityStickyMode_Type.__name__ = "Integer32"
_AgentGlobalPortSecurityStickyMode_Object = MibScalar
agentGlobalPortSecurityStickyMode = _AgentGlobalPortSecurityStickyMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 4),
    _AgentGlobalPortSecurityStickyMode_Type()
)
agentGlobalPortSecurityStickyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGlobalPortSecurityStickyMode.setStatus("current")


class _AgentGlobalPortSecurityViolationTrapMode_Type(Integer32):
    """Custom type agentGlobalPortSecurityViolationTrapMode based on Integer32"""
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


_AgentGlobalPortSecurityViolationTrapMode_Type.__name__ = "Integer32"
_AgentGlobalPortSecurityViolationTrapMode_Object = MibScalar
agentGlobalPortSecurityViolationTrapMode = _AgentGlobalPortSecurityViolationTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 1, 5),
    _AgentGlobalPortSecurityViolationTrapMode_Type()
)
agentGlobalPortSecurityViolationTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGlobalPortSecurityViolationTrapMode.setStatus("current")
_AgentPortSecurityTraps_ObjectIdentity = ObjectIdentity
agentPortSecurityTraps = _AgentPortSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 2)
)

# Managed Objects groups


# Notification objects

agentPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 20, 2, 1)
)
agentPortSecurityViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("DNOS-PORTSECURITY-PRIVATE-MIB", "agentPortSecurityLastDiscardedMAC"))
)
if mibBuilder.loadTexts:
    agentPortSecurityViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-PORTSECURITY-PRIVATE-MIB",
    **{"fastPathPortSecurity": fastPathPortSecurity,
       "agentPortSecurityGroup": agentPortSecurityGroup,
       "agentGlobalPortSecurityMode": agentGlobalPortSecurityMode,
       "agentPortSecurityTable": agentPortSecurityTable,
       "agentPortSecurityEntry": agentPortSecurityEntry,
       "agentPortSecurityMode": agentPortSecurityMode,
       "agentPortSecurityDynamicLimit": agentPortSecurityDynamicLimit,
       "agentPortSecurityStaticLimit": agentPortSecurityStaticLimit,
       "agentPortSecurityViolationTrapMode": agentPortSecurityViolationTrapMode,
       "agentPortSecurityStaticMACs": agentPortSecurityStaticMACs,
       "agentPortSecurityLastDiscardedMAC": agentPortSecurityLastDiscardedMAC,
       "agentPortSecurityMACAddressAdd": agentPortSecurityMACAddressAdd,
       "agentPortSecurityMACAddressRemove": agentPortSecurityMACAddressRemove,
       "agentPortSecurityMACAddressMove": agentPortSecurityMACAddressMove,
       "agentPortSecurityStickyMode": agentPortSecurityStickyMode,
       "agentPortSecurityDynamicTable": agentPortSecurityDynamicTable,
       "agentPortSecurityDynamicEntry": agentPortSecurityDynamicEntry,
       "agentPortSecurityDynamicVLANId": agentPortSecurityDynamicVLANId,
       "agentPortSecurityDynamicMACAddress": agentPortSecurityDynamicMACAddress,
       "agentGlobalPortSecurityStickyMode": agentGlobalPortSecurityStickyMode,
       "agentGlobalPortSecurityViolationTrapMode": agentGlobalPortSecurityViolationTrapMode,
       "agentPortSecurityTraps": agentPortSecurityTraps,
       "agentPortSecurityViolation": agentPortSecurityViolation}
)
