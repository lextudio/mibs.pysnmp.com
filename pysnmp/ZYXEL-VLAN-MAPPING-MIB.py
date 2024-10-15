# SNMP MIB module (ZYXEL-VLAN-MAPPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VLAN-MAPPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:02 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelVlanMapping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVlanMappingSetup_ObjectIdentity = ObjectIdentity
zyxelVlanMappingSetup = _ZyxelVlanMappingSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1)
)
_ZyVlanMappingState_Type = EnabledStatus
_ZyVlanMappingState_Object = MibScalar
zyVlanMappingState = _ZyVlanMappingState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 1),
    _ZyVlanMappingState_Type()
)
zyVlanMappingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanMappingState.setStatus("current")
_ZyxelVlanMappingPortTable_Object = MibTable
zyxelVlanMappingPortTable = _ZyxelVlanMappingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelVlanMappingPortTable.setStatus("current")
_ZyxelVlanMappingPortEntry_Object = MibTableRow
zyxelVlanMappingPortEntry = _ZyxelVlanMappingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 2, 1)
)
zyxelVlanMappingPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelVlanMappingPortEntry.setStatus("current")
_ZyVlanMappingPortState_Type = EnabledStatus
_ZyVlanMappingPortState_Object = MibTableColumn
zyVlanMappingPortState = _ZyVlanMappingPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 2, 1, 1),
    _ZyVlanMappingPortState_Type()
)
zyVlanMappingPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanMappingPortState.setStatus("current")
_ZyVlanMappingMaxNumberOfRules_Type = Integer32
_ZyVlanMappingMaxNumberOfRules_Object = MibScalar
zyVlanMappingMaxNumberOfRules = _ZyVlanMappingMaxNumberOfRules_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 3),
    _ZyVlanMappingMaxNumberOfRules_Type()
)
zyVlanMappingMaxNumberOfRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyVlanMappingMaxNumberOfRules.setStatus("current")
_ZyxelVlanMappingTable_Object = MibTable
zyxelVlanMappingTable = _ZyxelVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4)
)
if mibBuilder.loadTexts:
    zyxelVlanMappingTable.setStatus("current")
_ZyxelVlanMappingEntry_Object = MibTableRow
zyxelVlanMappingEntry = _ZyxelVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1)
)
zyxelVlanMappingEntry.setIndexNames(
    (0, "ZYXEL-VLAN-MAPPING-MIB", "zyVlanMappingPort"),
    (0, "ZYXEL-VLAN-MAPPING-MIB", "zyVlanMappingVid"),
)
if mibBuilder.loadTexts:
    zyxelVlanMappingEntry.setStatus("current")
_ZyVlanMappingName_Type = DisplayString
_ZyVlanMappingName_Object = MibTableColumn
zyVlanMappingName = _ZyVlanMappingName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 1),
    _ZyVlanMappingName_Type()
)
zyVlanMappingName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanMappingName.setStatus("current")
_ZyVlanMappingPort_Type = Integer32
_ZyVlanMappingPort_Object = MibTableColumn
zyVlanMappingPort = _ZyVlanMappingPort_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 2),
    _ZyVlanMappingPort_Type()
)
zyVlanMappingPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVlanMappingPort.setStatus("current")
_ZyVlanMappingVid_Type = Integer32
_ZyVlanMappingVid_Object = MibTableColumn
zyVlanMappingVid = _ZyVlanMappingVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 3),
    _ZyVlanMappingVid_Type()
)
zyVlanMappingVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVlanMappingVid.setStatus("current")
_ZyVlanMappingTranslatedVid_Type = Integer32
_ZyVlanMappingTranslatedVid_Object = MibTableColumn
zyVlanMappingTranslatedVid = _ZyVlanMappingTranslatedVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 4),
    _ZyVlanMappingTranslatedVid_Type()
)
zyVlanMappingTranslatedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanMappingTranslatedVid.setStatus("current")


class _ZyVlanMappingPriority_Type(Integer32):
    """Custom type zyVlanMappingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_ZyVlanMappingPriority_Type.__name__ = "Integer32"
_ZyVlanMappingPriority_Object = MibTableColumn
zyVlanMappingPriority = _ZyVlanMappingPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 5),
    _ZyVlanMappingPriority_Type()
)
zyVlanMappingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVlanMappingPriority.setStatus("current")
_ZyVlanMappingRowStatus_Type = RowStatus
_ZyVlanMappingRowStatus_Object = MibTableColumn
zyVlanMappingRowStatus = _ZyVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 88, 1, 4, 1, 6),
    _ZyVlanMappingRowStatus_Type()
)
zyVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyVlanMappingRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VLAN-MAPPING-MIB",
    **{"zyxelVlanMapping": zyxelVlanMapping,
       "zyxelVlanMappingSetup": zyxelVlanMappingSetup,
       "zyVlanMappingState": zyVlanMappingState,
       "zyxelVlanMappingPortTable": zyxelVlanMappingPortTable,
       "zyxelVlanMappingPortEntry": zyxelVlanMappingPortEntry,
       "zyVlanMappingPortState": zyVlanMappingPortState,
       "zyVlanMappingMaxNumberOfRules": zyVlanMappingMaxNumberOfRules,
       "zyxelVlanMappingTable": zyxelVlanMappingTable,
       "zyxelVlanMappingEntry": zyxelVlanMappingEntry,
       "zyVlanMappingName": zyVlanMappingName,
       "zyVlanMappingPort": zyVlanMappingPort,
       "zyVlanMappingVid": zyVlanMappingVid,
       "zyVlanMappingTranslatedVid": zyVlanMappingTranslatedVid,
       "zyVlanMappingPriority": zyVlanMappingPriority,
       "zyVlanMappingRowStatus": zyVlanMappingRowStatus}
)
