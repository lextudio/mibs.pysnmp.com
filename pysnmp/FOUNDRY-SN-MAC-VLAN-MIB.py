# SNMP MIB module (FOUNDRY-SN-MAC-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-MAC-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:58 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

snMacVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30)
)
snMacVlan.setRevisions(
        ("2007-06-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnMacVlanGlobalObjects_ObjectIdentity = ObjectIdentity
snMacVlanGlobalObjects = _SnMacVlanGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1)
)


class _SnMacVlanGlobalClearOper_Type(Integer32):
    """Custom type snMacVlanGlobalClearOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacVlanGlobalClearOper_Type.__name__ = "Integer32"
_SnMacVlanGlobalClearOper_Object = MibScalar
snMacVlanGlobalClearOper = _SnMacVlanGlobalClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 1),
    _SnMacVlanGlobalClearOper_Type()
)
snMacVlanGlobalClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanGlobalClearOper.setStatus("current")


class _SnMacVlanGlobalDynConfigState_Type(Integer32):
    """Custom type snMacVlanGlobalDynConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnMacVlanGlobalDynConfigState_Type.__name__ = "Integer32"
_SnMacVlanGlobalDynConfigState_Object = MibScalar
snMacVlanGlobalDynConfigState = _SnMacVlanGlobalDynConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 1, 2),
    _SnMacVlanGlobalDynConfigState_Type()
)
snMacVlanGlobalDynConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanGlobalDynConfigState.setStatus("current")
_SnMacVlanTableObjects_ObjectIdentity = ObjectIdentity
snMacVlanTableObjects = _SnMacVlanTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2)
)
_SnMacVlanPortMemberTable_Object = MibTable
snMacVlanPortMemberTable = _SnMacVlanPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1)
)
if mibBuilder.loadTexts:
    snMacVlanPortMemberTable.setStatus("current")
_SnMacVlanPortMemberEntry_Object = MibTableRow
snMacVlanPortMemberEntry = _SnMacVlanPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1)
)
snMacVlanPortMemberEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberVLanId"),
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanPortMemberPortId"),
)
if mibBuilder.loadTexts:
    snMacVlanPortMemberEntry.setStatus("current")


class _SnMacVlanPortMemberVLanId_Type(Integer32):
    """Custom type snMacVlanPortMemberVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnMacVlanPortMemberVLanId_Type.__name__ = "Integer32"
_SnMacVlanPortMemberVLanId_Object = MibTableColumn
snMacVlanPortMemberVLanId = _SnMacVlanPortMemberVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 1),
    _SnMacVlanPortMemberVLanId_Type()
)
snMacVlanPortMemberVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacVlanPortMemberVLanId.setStatus("current")
_SnMacVlanPortMemberPortId_Type = InterfaceIndex
_SnMacVlanPortMemberPortId_Object = MibTableColumn
snMacVlanPortMemberPortId = _SnMacVlanPortMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 2),
    _SnMacVlanPortMemberPortId_Type()
)
snMacVlanPortMemberPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacVlanPortMemberPortId.setStatus("current")


class _SnMacVlanPortMemberRowStatus_Type(Integer32):
    """Custom type snMacVlanPortMemberRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnMacVlanPortMemberRowStatus_Type.__name__ = "Integer32"
_SnMacVlanPortMemberRowStatus_Object = MibTableColumn
snMacVlanPortMemberRowStatus = _SnMacVlanPortMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 1, 1, 3),
    _SnMacVlanPortMemberRowStatus_Type()
)
snMacVlanPortMemberRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanPortMemberRowStatus.setStatus("current")
_SnMacVlanIfTable_Object = MibTable
snMacVlanIfTable = _SnMacVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2)
)
if mibBuilder.loadTexts:
    snMacVlanIfTable.setStatus("current")
_SnMacVlanIfEntry_Object = MibTableRow
snMacVlanIfEntry = _SnMacVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1)
)
snMacVlanIfEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"),
)
if mibBuilder.loadTexts:
    snMacVlanIfEntry.setStatus("current")
_SnMacVlanIfIndex_Type = InterfaceIndex
_SnMacVlanIfIndex_Object = MibTableColumn
snMacVlanIfIndex = _SnMacVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 1),
    _SnMacVlanIfIndex_Type()
)
snMacVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacVlanIfIndex.setStatus("current")


class _SnMacVlanIfEnable_Type(Integer32):
    """Custom type snMacVlanIfEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SnMacVlanIfEnable_Type.__name__ = "Integer32"
_SnMacVlanIfEnable_Object = MibTableColumn
snMacVlanIfEnable = _SnMacVlanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 2),
    _SnMacVlanIfEnable_Type()
)
snMacVlanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanIfEnable.setStatus("current")


class _SnMacVlanIfMaxEntry_Type(Integer32):
    """Custom type snMacVlanIfMaxEntry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_SnMacVlanIfMaxEntry_Type.__name__ = "Integer32"
_SnMacVlanIfMaxEntry_Object = MibTableColumn
snMacVlanIfMaxEntry = _SnMacVlanIfMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 3),
    _SnMacVlanIfMaxEntry_Type()
)
snMacVlanIfMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanIfMaxEntry.setStatus("current")


class _SnMacVlanIfClearOper_Type(Integer32):
    """Custom type snMacVlanIfClearOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacVlanIfClearOper_Type.__name__ = "Integer32"
_SnMacVlanIfClearOper_Object = MibTableColumn
snMacVlanIfClearOper = _SnMacVlanIfClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 4),
    _SnMacVlanIfClearOper_Type()
)
snMacVlanIfClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanIfClearOper.setStatus("current")


class _SnMacVlanIfClearConfig_Type(Integer32):
    """Custom type snMacVlanIfClearConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("valid", 0))
    )


_SnMacVlanIfClearConfig_Type.__name__ = "Integer32"
_SnMacVlanIfClearConfig_Object = MibTableColumn
snMacVlanIfClearConfig = _SnMacVlanIfClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 2, 1, 5),
    _SnMacVlanIfClearConfig_Type()
)
snMacVlanIfClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacVlanIfClearConfig.setStatus("current")
_SnMacBasedVlanTable_Object = MibTable
snMacBasedVlanTable = _SnMacBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3)
)
if mibBuilder.loadTexts:
    snMacBasedVlanTable.setStatus("current")
_SnMacBasedVlanEntry_Object = MibTableRow
snMacBasedVlanEntry = _SnMacBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1)
)
snMacBasedVlanEntry.setIndexNames(
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacVlanIfIndex"),
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanId"),
    (0, "FOUNDRY-SN-MAC-VLAN-MIB", "snMacBasedVlanMac"),
)
if mibBuilder.loadTexts:
    snMacBasedVlanEntry.setStatus("current")


class _SnMacBasedVlanId_Type(Integer32):
    """Custom type snMacBasedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_SnMacBasedVlanId_Type.__name__ = "Integer32"
_SnMacBasedVlanId_Object = MibTableColumn
snMacBasedVlanId = _SnMacBasedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 1),
    _SnMacBasedVlanId_Type()
)
snMacBasedVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacBasedVlanId.setStatus("current")
_SnMacBasedVlanMac_Type = MacAddress
_SnMacBasedVlanMac_Object = MibTableColumn
snMacBasedVlanMac = _SnMacBasedVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 2),
    _SnMacBasedVlanMac_Type()
)
snMacBasedVlanMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snMacBasedVlanMac.setStatus("current")


class _SnMacBasedVlanPriority_Type(Integer32):
    """Custom type snMacBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SnMacBasedVlanPriority_Type.__name__ = "Integer32"
_SnMacBasedVlanPriority_Object = MibTableColumn
snMacBasedVlanPriority = _SnMacBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 3),
    _SnMacBasedVlanPriority_Type()
)
snMacBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacBasedVlanPriority.setStatus("current")


class _SnMacBasedVlanRowStatus_Type(Integer32):
    """Custom type snMacBasedVlanRowStatus based on Integer32"""
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
        *(("create", 4),
          ("delete", 3),
          ("other", 1),
          ("valid", 2))
    )


_SnMacBasedVlanRowStatus_Type.__name__ = "Integer32"
_SnMacBasedVlanRowStatus_Object = MibTableColumn
snMacBasedVlanRowStatus = _SnMacBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 30, 2, 3, 1, 4),
    _SnMacBasedVlanRowStatus_Type()
)
snMacBasedVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snMacBasedVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-MAC-VLAN-MIB",
    **{"snMacVlan": snMacVlan,
       "snMacVlanGlobalObjects": snMacVlanGlobalObjects,
       "snMacVlanGlobalClearOper": snMacVlanGlobalClearOper,
       "snMacVlanGlobalDynConfigState": snMacVlanGlobalDynConfigState,
       "snMacVlanTableObjects": snMacVlanTableObjects,
       "snMacVlanPortMemberTable": snMacVlanPortMemberTable,
       "snMacVlanPortMemberEntry": snMacVlanPortMemberEntry,
       "snMacVlanPortMemberVLanId": snMacVlanPortMemberVLanId,
       "snMacVlanPortMemberPortId": snMacVlanPortMemberPortId,
       "snMacVlanPortMemberRowStatus": snMacVlanPortMemberRowStatus,
       "snMacVlanIfTable": snMacVlanIfTable,
       "snMacVlanIfEntry": snMacVlanIfEntry,
       "snMacVlanIfIndex": snMacVlanIfIndex,
       "snMacVlanIfEnable": snMacVlanIfEnable,
       "snMacVlanIfMaxEntry": snMacVlanIfMaxEntry,
       "snMacVlanIfClearOper": snMacVlanIfClearOper,
       "snMacVlanIfClearConfig": snMacVlanIfClearConfig,
       "snMacBasedVlanTable": snMacBasedVlanTable,
       "snMacBasedVlanEntry": snMacBasedVlanEntry,
       "snMacBasedVlanId": snMacBasedVlanId,
       "snMacBasedVlanMac": snMacBasedVlanMac,
       "snMacBasedVlanPriority": snMacBasedVlanPriority,
       "snMacBasedVlanRowStatus": snMacBasedVlanRowStatus}
)
