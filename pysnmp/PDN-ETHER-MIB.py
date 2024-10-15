# SNMP MIB module (PDN-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-ETHER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:39 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_ether,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-ether")

(ManagementType,
 ResetStates,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "ManagementType",
    "ResetStates",
    "SwitchState")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnPortConfigMIBObjects_ObjectIdentity = ObjectIdentity
pdnPortConfigMIBObjects = _PdnPortConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1)
)
_PdnPortConfigEthernet_ObjectIdentity = ObjectIdentity
pdnPortConfigEthernet = _PdnPortConfigEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1)
)
_PdnPortConfigEthernetTable_Object = MibTable
pdnPortConfigEthernetTable = _PdnPortConfigEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigEthernetTable.setStatus("mandatory")
_PdnPortConfigEthernetEntry_Object = MibTableRow
pdnPortConfigEthernetEntry = _PdnPortConfigEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1)
)
pdnPortConfigEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPortConfigEthernetEntry.setStatus("mandatory")


class _PdnPortConfigEthernetDuplexMode_Type(SwitchState):
    """Custom type pdnPortConfigEthernetDuplexMode based on SwitchState"""


_PdnPortConfigEthernetDuplexMode_Object = MibTableColumn
pdnPortConfigEthernetDuplexMode = _PdnPortConfigEthernetDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 1),
    _PdnPortConfigEthernetDuplexMode_Type()
)
pdnPortConfigEthernetDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetDuplexMode.setStatus("mandatory")


class _PdnPortConfigEthernetManageType_Type(ManagementType):
    """Custom type pdnPortConfigEthernetManageType based on ManagementType"""


_PdnPortConfigEthernetManageType_Object = MibTableColumn
pdnPortConfigEthernetManageType = _PdnPortConfigEthernetManageType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 2),
    _PdnPortConfigEthernetManageType_Type()
)
pdnPortConfigEthernetManageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetManageType.setStatus("mandatory")


class _PdnPortConfigEthernetResetState_Type(ResetStates):
    """Custom type pdnPortConfigEthernetResetState based on ResetStates"""


_PdnPortConfigEthernetResetState_Object = MibTableColumn
pdnPortConfigEthernetResetState = _PdnPortConfigEthernetResetState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 3),
    _PdnPortConfigEthernetResetState_Type()
)
pdnPortConfigEthernetResetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetResetState.setStatus("mandatory")
_PdnPortConfigMIBTraps_ObjectIdentity = ObjectIdentity
pdnPortConfigMIBTraps = _PdnPortConfigMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ETHER-MIB",
    **{"pdnPortConfigMIBObjects": pdnPortConfigMIBObjects,
       "pdnPortConfigEthernet": pdnPortConfigEthernet,
       "pdnPortConfigEthernetTable": pdnPortConfigEthernetTable,
       "pdnPortConfigEthernetEntry": pdnPortConfigEthernetEntry,
       "pdnPortConfigEthernetDuplexMode": pdnPortConfigEthernetDuplexMode,
       "pdnPortConfigEthernetManageType": pdnPortConfigEthernetManageType,
       "pdnPortConfigEthernetResetState": pdnPortConfigEthernetResetState,
       "pdnPortConfigMIBTraps": pdnPortConfigMIBTraps}
)
