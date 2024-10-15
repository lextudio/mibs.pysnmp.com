# SNMP MIB module (FOUNDRY-MAC-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-MAC-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:45 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fdryMacVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32)
)
fdryMacVlanMIB.setRevisions(
        ("2010-06-02 00:00",
         "2008-12-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FdryMacVlanGlobalObjects_ObjectIdentity = ObjectIdentity
fdryMacVlanGlobalObjects = _FdryMacVlanGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1)
)


class _FdryMacVlanGlobalClearOper_Type(Integer32):
    """Custom type fdryMacVlanGlobalClearOper based on Integer32"""
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


_FdryMacVlanGlobalClearOper_Type.__name__ = "Integer32"
_FdryMacVlanGlobalClearOper_Object = MibScalar
fdryMacVlanGlobalClearOper = _FdryMacVlanGlobalClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1, 1),
    _FdryMacVlanGlobalClearOper_Type()
)
fdryMacVlanGlobalClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanGlobalClearOper.setStatus("current")


class _FdryMacVlanGlobalDynConfigState_Type(Integer32):
    """Custom type fdryMacVlanGlobalDynConfigState based on Integer32"""
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


_FdryMacVlanGlobalDynConfigState_Type.__name__ = "Integer32"
_FdryMacVlanGlobalDynConfigState_Object = MibScalar
fdryMacVlanGlobalDynConfigState = _FdryMacVlanGlobalDynConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 1, 2),
    _FdryMacVlanGlobalDynConfigState_Type()
)
fdryMacVlanGlobalDynConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanGlobalDynConfigState.setStatus("current")
_FdryMacVlanTableObjects_ObjectIdentity = ObjectIdentity
fdryMacVlanTableObjects = _FdryMacVlanTableObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2)
)
_FdryMacVlanPortMemberTable_Object = MibTable
fdryMacVlanPortMemberTable = _FdryMacVlanPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1)
)
if mibBuilder.loadTexts:
    fdryMacVlanPortMemberTable.setStatus("current")
_FdryMacVlanPortMemberEntry_Object = MibTableRow
fdryMacVlanPortMemberEntry = _FdryMacVlanPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1)
)
fdryMacVlanPortMemberEntry.setIndexNames(
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanPortMemberVLanId"),
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanPortMemberPortId"),
)
if mibBuilder.loadTexts:
    fdryMacVlanPortMemberEntry.setStatus("current")


class _FdryMacVlanPortMemberVLanId_Type(Integer32):
    """Custom type fdryMacVlanPortMemberVLanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FdryMacVlanPortMemberVLanId_Type.__name__ = "Integer32"
_FdryMacVlanPortMemberVLanId_Object = MibTableColumn
fdryMacVlanPortMemberVLanId = _FdryMacVlanPortMemberVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 1),
    _FdryMacVlanPortMemberVLanId_Type()
)
fdryMacVlanPortMemberVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryMacVlanPortMemberVLanId.setStatus("current")
_FdryMacVlanPortMemberPortId_Type = InterfaceIndex
_FdryMacVlanPortMemberPortId_Object = MibTableColumn
fdryMacVlanPortMemberPortId = _FdryMacVlanPortMemberPortId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 2),
    _FdryMacVlanPortMemberPortId_Type()
)
fdryMacVlanPortMemberPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryMacVlanPortMemberPortId.setStatus("current")
_FdryMacVlanPortMemberRowStatus_Type = RowStatus
_FdryMacVlanPortMemberRowStatus_Object = MibTableColumn
fdryMacVlanPortMemberRowStatus = _FdryMacVlanPortMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 1, 1, 3),
    _FdryMacVlanPortMemberRowStatus_Type()
)
fdryMacVlanPortMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryMacVlanPortMemberRowStatus.setStatus("current")
_FdryMacVlanIfTable_Object = MibTable
fdryMacVlanIfTable = _FdryMacVlanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2)
)
if mibBuilder.loadTexts:
    fdryMacVlanIfTable.setStatus("current")
_FdryMacVlanIfEntry_Object = MibTableRow
fdryMacVlanIfEntry = _FdryMacVlanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1)
)
fdryMacVlanIfEntry.setIndexNames(
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanIfIndex"),
)
if mibBuilder.loadTexts:
    fdryMacVlanIfEntry.setStatus("current")
_FdryMacVlanIfIndex_Type = InterfaceIndex
_FdryMacVlanIfIndex_Object = MibTableColumn
fdryMacVlanIfIndex = _FdryMacVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 1),
    _FdryMacVlanIfIndex_Type()
)
fdryMacVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryMacVlanIfIndex.setStatus("current")


class _FdryMacVlanIfEnable_Type(Integer32):
    """Custom type fdryMacVlanIfEnable based on Integer32"""
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


_FdryMacVlanIfEnable_Type.__name__ = "Integer32"
_FdryMacVlanIfEnable_Object = MibTableColumn
fdryMacVlanIfEnable = _FdryMacVlanIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 2),
    _FdryMacVlanIfEnable_Type()
)
fdryMacVlanIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanIfEnable.setStatus("current")


class _FdryMacVlanIfMaxEntry_Type(Integer32):
    """Custom type fdryMacVlanIfMaxEntry based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 32),
    )


_FdryMacVlanIfMaxEntry_Type.__name__ = "Integer32"
_FdryMacVlanIfMaxEntry_Object = MibTableColumn
fdryMacVlanIfMaxEntry = _FdryMacVlanIfMaxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 3),
    _FdryMacVlanIfMaxEntry_Type()
)
fdryMacVlanIfMaxEntry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanIfMaxEntry.setStatus("current")


class _FdryMacVlanIfClearOper_Type(Integer32):
    """Custom type fdryMacVlanIfClearOper based on Integer32"""
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


_FdryMacVlanIfClearOper_Type.__name__ = "Integer32"
_FdryMacVlanIfClearOper_Object = MibTableColumn
fdryMacVlanIfClearOper = _FdryMacVlanIfClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 4),
    _FdryMacVlanIfClearOper_Type()
)
fdryMacVlanIfClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanIfClearOper.setStatus("current")


class _FdryMacVlanIfClearConfig_Type(Integer32):
    """Custom type fdryMacVlanIfClearConfig based on Integer32"""
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


_FdryMacVlanIfClearConfig_Type.__name__ = "Integer32"
_FdryMacVlanIfClearConfig_Object = MibTableColumn
fdryMacVlanIfClearConfig = _FdryMacVlanIfClearConfig_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 2, 1, 5),
    _FdryMacVlanIfClearConfig_Type()
)
fdryMacVlanIfClearConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryMacVlanIfClearConfig.setStatus("current")
_FdryMacBasedVlanTable_Object = MibTable
fdryMacBasedVlanTable = _FdryMacBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3)
)
if mibBuilder.loadTexts:
    fdryMacBasedVlanTable.setStatus("current")
_FdryMacBasedVlanEntry_Object = MibTableRow
fdryMacBasedVlanEntry = _FdryMacBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1)
)
fdryMacBasedVlanEntry.setIndexNames(
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacVlanIfIndex"),
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacBasedVlanId"),
    (0, "FOUNDRY-MAC-VLAN-MIB", "fdryMacBasedVlanMac"),
)
if mibBuilder.loadTexts:
    fdryMacBasedVlanEntry.setStatus("current")


class _FdryMacBasedVlanId_Type(Integer32):
    """Custom type fdryMacBasedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FdryMacBasedVlanId_Type.__name__ = "Integer32"
_FdryMacBasedVlanId_Object = MibTableColumn
fdryMacBasedVlanId = _FdryMacBasedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 1),
    _FdryMacBasedVlanId_Type()
)
fdryMacBasedVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryMacBasedVlanId.setStatus("current")
_FdryMacBasedVlanMac_Type = MacAddress
_FdryMacBasedVlanMac_Object = MibTableColumn
fdryMacBasedVlanMac = _FdryMacBasedVlanMac_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 2),
    _FdryMacBasedVlanMac_Type()
)
fdryMacBasedVlanMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryMacBasedVlanMac.setStatus("current")


class _FdryMacBasedVlanPriority_Type(Integer32):
    """Custom type fdryMacBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FdryMacBasedVlanPriority_Type.__name__ = "Integer32"
_FdryMacBasedVlanPriority_Object = MibTableColumn
fdryMacBasedVlanPriority = _FdryMacBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 3),
    _FdryMacBasedVlanPriority_Type()
)
fdryMacBasedVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryMacBasedVlanPriority.setStatus("current")
_FdryMacBasedVlanRowStatus_Type = RowStatus
_FdryMacBasedVlanRowStatus_Object = MibTableColumn
fdryMacBasedVlanRowStatus = _FdryMacBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 32, 2, 3, 1, 4),
    _FdryMacBasedVlanRowStatus_Type()
)
fdryMacBasedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryMacBasedVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-MAC-VLAN-MIB",
    **{"fdryMacVlanMIB": fdryMacVlanMIB,
       "fdryMacVlanGlobalObjects": fdryMacVlanGlobalObjects,
       "fdryMacVlanGlobalClearOper": fdryMacVlanGlobalClearOper,
       "fdryMacVlanGlobalDynConfigState": fdryMacVlanGlobalDynConfigState,
       "fdryMacVlanTableObjects": fdryMacVlanTableObjects,
       "fdryMacVlanPortMemberTable": fdryMacVlanPortMemberTable,
       "fdryMacVlanPortMemberEntry": fdryMacVlanPortMemberEntry,
       "fdryMacVlanPortMemberVLanId": fdryMacVlanPortMemberVLanId,
       "fdryMacVlanPortMemberPortId": fdryMacVlanPortMemberPortId,
       "fdryMacVlanPortMemberRowStatus": fdryMacVlanPortMemberRowStatus,
       "fdryMacVlanIfTable": fdryMacVlanIfTable,
       "fdryMacVlanIfEntry": fdryMacVlanIfEntry,
       "fdryMacVlanIfIndex": fdryMacVlanIfIndex,
       "fdryMacVlanIfEnable": fdryMacVlanIfEnable,
       "fdryMacVlanIfMaxEntry": fdryMacVlanIfMaxEntry,
       "fdryMacVlanIfClearOper": fdryMacVlanIfClearOper,
       "fdryMacVlanIfClearConfig": fdryMacVlanIfClearConfig,
       "fdryMacBasedVlanTable": fdryMacBasedVlanTable,
       "fdryMacBasedVlanEntry": fdryMacBasedVlanEntry,
       "fdryMacBasedVlanId": fdryMacBasedVlanId,
       "fdryMacBasedVlanMac": fdryMacBasedVlanMac,
       "fdryMacBasedVlanPriority": fdryMacBasedVlanPriority,
       "fdryMacBasedVlanRowStatus": fdryMacBasedVlanRowStatus}
)
