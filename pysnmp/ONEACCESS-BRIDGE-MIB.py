# SNMP MIB module (ONEACCESS-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ONEACCESS-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:49 2024
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(oacExpIMIp,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMIp",
    "oacMIBModules")

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

oacBridgeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 682)
)
oacBridgeMIB.setRevisions(
        ("2011-06-15 00:00",
         "2010-07-08 10:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacBridgeObjects_ObjectIdentity = ObjectIdentity
oacBridgeObjects = _OacBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7)
)
_OacBridgeConfigObjects_ObjectIdentity = ObjectIdentity
oacBridgeConfigObjects = _OacBridgeConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1)
)
_OacBridgeGroupTable_Object = MibTable
oacBridgeGroupTable = _OacBridgeGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 1)
)
if mibBuilder.loadTexts:
    oacBridgeGroupTable.setStatus("current")
_OacBridgeGroupEntry_Object = MibTableRow
oacBridgeGroupEntry = _OacBridgeGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 1, 1)
)
oacBridgeGroupEntry.setIndexNames(
    (0, "ONEACCESS-BRIDGE-MIB", "oacBridgeGroupValue"),
)
if mibBuilder.loadTexts:
    oacBridgeGroupEntry.setStatus("current")


class _OacBridgeGroupValue_Type(Unsigned32):
    """Custom type oacBridgeGroupValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OacBridgeGroupValue_Type.__name__ = "Unsigned32"
_OacBridgeGroupValue_Object = MibTableColumn
oacBridgeGroupValue = _OacBridgeGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 1, 1, 1),
    _OacBridgeGroupValue_Type()
)
oacBridgeGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacBridgeGroupValue.setStatus("current")


class _OacBridgeTransparency_Type(TruthValue):
    """Custom type oacBridgeTransparency based on TruthValue"""


_OacBridgeTransparency_Object = MibTableColumn
oacBridgeTransparency = _OacBridgeTransparency_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 1, 1, 2),
    _OacBridgeTransparency_Type()
)
oacBridgeTransparency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacBridgeTransparency.setStatus("current")
_OacBridgeGroupRowStatus_Type = RowStatus
_OacBridgeGroupRowStatus_Object = MibTableColumn
oacBridgeGroupRowStatus = _OacBridgeGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 1, 1, 3),
    _OacBridgeGroupRowStatus_Type()
)
oacBridgeGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacBridgeGroupRowStatus.setStatus("current")
_OacBridgeGroupInterfaceTable_Object = MibTable
oacBridgeGroupInterfaceTable = _OacBridgeGroupInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 2)
)
if mibBuilder.loadTexts:
    oacBridgeGroupInterfaceTable.setStatus("current")
_OacBridgeGroupInterfaceEntry_Object = MibTableRow
oacBridgeGroupInterfaceEntry = _OacBridgeGroupInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 2, 1)
)
oacBridgeGroupInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oacBridgeGroupInterfaceEntry.setStatus("current")


class _OacInBridgeGroupValue_Type(Unsigned32):
    """Custom type oacInBridgeGroupValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OacInBridgeGroupValue_Type.__name__ = "Unsigned32"
_OacInBridgeGroupValue_Object = MibTableColumn
oacInBridgeGroupValue = _OacInBridgeGroupValue_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 2, 1, 1),
    _OacInBridgeGroupValue_Type()
)
oacInBridgeGroupValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacInBridgeGroupValue.setStatus("current")
_OacBridgeGroupInterfaceName_Type = DisplayString
_OacBridgeGroupInterfaceName_Object = MibTableColumn
oacBridgeGroupInterfaceName = _OacBridgeGroupInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 2, 1, 2),
    _OacBridgeGroupInterfaceName_Type()
)
oacBridgeGroupInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacBridgeGroupInterfaceName.setStatus("current")
_OacBridgeGroupInterfaceRowStatus_Type = RowStatus
_OacBridgeGroupInterfaceRowStatus_Object = MibTableColumn
oacBridgeGroupInterfaceRowStatus = _OacBridgeGroupInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 1, 2, 1, 3),
    _OacBridgeGroupInterfaceRowStatus_Type()
)
oacBridgeGroupInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oacBridgeGroupInterfaceRowStatus.setStatus("current")
_OacBridgeConformance_ObjectIdentity = ObjectIdentity
oacBridgeConformance = _OacBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 10)
)
_OacBridgeGroupConfigGroups_ObjectIdentity = ObjectIdentity
oacBridgeGroupConfigGroups = _OacBridgeGroupConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 10, 1)
)
_OacBridgeGroupCompls_ObjectIdentity = ObjectIdentity
oacBridgeGroupCompls = _OacBridgeGroupCompls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 10, 2)
)

# Managed Objects groups

oacBridgeGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 7, 10, 1, 1)
)
oacBridgeGroupConfigGroup.setObjects(
      *(("ONEACCESS-BRIDGE-MIB", "oacBridgeGroupValue"),
        ("ONEACCESS-BRIDGE-MIB", "oacBridgeGroupInterfaceName"))
)
if mibBuilder.loadTexts:
    oacBridgeGroupConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ONEACCESS-BRIDGE-MIB",
    **{"oacBridgeMIB": oacBridgeMIB,
       "oacBridgeObjects": oacBridgeObjects,
       "oacBridgeConfigObjects": oacBridgeConfigObjects,
       "oacBridgeGroupTable": oacBridgeGroupTable,
       "oacBridgeGroupEntry": oacBridgeGroupEntry,
       "oacBridgeGroupValue": oacBridgeGroupValue,
       "oacBridgeTransparency": oacBridgeTransparency,
       "oacBridgeGroupRowStatus": oacBridgeGroupRowStatus,
       "oacBridgeGroupInterfaceTable": oacBridgeGroupInterfaceTable,
       "oacBridgeGroupInterfaceEntry": oacBridgeGroupInterfaceEntry,
       "oacInBridgeGroupValue": oacInBridgeGroupValue,
       "oacBridgeGroupInterfaceName": oacBridgeGroupInterfaceName,
       "oacBridgeGroupInterfaceRowStatus": oacBridgeGroupInterfaceRowStatus,
       "oacBridgeConformance": oacBridgeConformance,
       "oacBridgeGroupConfigGroups": oacBridgeGroupConfigGroups,
       "oacBridgeGroupConfigGroup": oacBridgeGroupConfigGroup,
       "oacBridgeGroupCompls": oacBridgeGroupCompls}
)
