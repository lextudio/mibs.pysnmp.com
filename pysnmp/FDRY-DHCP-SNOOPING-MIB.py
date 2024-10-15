# SNMP MIB module (FDRY-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-DHCP-SNOOPING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:38 2024
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

(ArpState,
 ArpType) = mibBuilder.importSymbols(
    "FDRY-DAI-MIB",
    "ArpState",
    "ArpType")

(DisplayString,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-AGENT-MIB",
    "DisplayString")

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fdryDhcpSnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36)
)
fdryDhcpSnoopMIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-03-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ClearAction(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_FdryDhcpSnoopGlobalObjects_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopGlobalObjects = _FdryDhcpSnoopGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1)
)
_FdryDhcpSnoopGlobalClearOper_Type = ClearAction
_FdryDhcpSnoopGlobalClearOper_Object = MibScalar
fdryDhcpSnoopGlobalClearOper = _FdryDhcpSnoopGlobalClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 1, 1),
    _FdryDhcpSnoopGlobalClearOper_Type()
)
fdryDhcpSnoopGlobalClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopGlobalClearOper.setStatus("current")
_FdryDhcpSnoopVlan_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopVlan = _FdryDhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2)
)
_FdryDhcpSnoopVlanConfigTable_Object = MibTable
fdryDhcpSnoopVlanConfigTable = _FdryDhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanConfigTable.setStatus("current")
_FdryDhcpSnoopVlanConfigEntry_Object = MibTableRow
fdryDhcpSnoopVlanConfigEntry = _FdryDhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1)
)
fdryDhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopVlanVLanId"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanConfigEntry.setStatus("current")
_FdryDhcpSnoopVlanVLanId_Type = VlanIndex
_FdryDhcpSnoopVlanVLanId_Object = MibTableColumn
fdryDhcpSnoopVlanVLanId = _FdryDhcpSnoopVlanVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 1),
    _FdryDhcpSnoopVlanVLanId_Type()
)
fdryDhcpSnoopVlanVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanVLanId.setStatus("current")
_FdryDhcpSnoopVlanDhcpSnoopEnable_Type = TruthValue
_FdryDhcpSnoopVlanDhcpSnoopEnable_Object = MibTableColumn
fdryDhcpSnoopVlanDhcpSnoopEnable = _FdryDhcpSnoopVlanDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 2, 1, 1, 2),
    _FdryDhcpSnoopVlanDhcpSnoopEnable_Type()
)
fdryDhcpSnoopVlanDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopVlanDhcpSnoopEnable.setStatus("current")
_FdryDhcpSnoopInterface_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopInterface = _FdryDhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3)
)
_FdryDhcpSnoopIfConfigTable_Object = MibTable
fdryDhcpSnoopIfConfigTable = _FdryDhcpSnoopIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfConfigTable.setStatus("current")
_FdryDhcpSnoopIfConfigEntry_Object = MibTableRow
fdryDhcpSnoopIfConfigEntry = _FdryDhcpSnoopIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1)
)
fdryDhcpSnoopIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfConfigEntry.setStatus("current")
_FdryDhcpSnoopIfTrustValue_Type = TruthValue
_FdryDhcpSnoopIfTrustValue_Object = MibTableColumn
fdryDhcpSnoopIfTrustValue = _FdryDhcpSnoopIfTrustValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 3, 1, 1, 1),
    _FdryDhcpSnoopIfTrustValue_Type()
)
fdryDhcpSnoopIfTrustValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopIfTrustValue.setStatus("current")
_FdryDhcpSnoopBind_ObjectIdentity = ObjectIdentity
fdryDhcpSnoopBind = _FdryDhcpSnoopBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4)
)
_FdryDhcpSnoopBindTable_Object = MibTable
fdryDhcpSnoopBindTable = _FdryDhcpSnoopBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1)
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindTable.setStatus("current")
_FdryDhcpSnoopBindEntry_Object = MibTableRow
fdryDhcpSnoopBindEntry = _FdryDhcpSnoopBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1)
)
fdryDhcpSnoopBindEntry.setIndexNames(
    (0, "FDRY-DHCP-SNOOPING-MIB", "fdryDhcpSnoopBindIpAddr"),
)
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindEntry.setStatus("current")
_FdryDhcpSnoopBindIpAddr_Type = IpAddress
_FdryDhcpSnoopBindIpAddr_Object = MibTableColumn
fdryDhcpSnoopBindIpAddr = _FdryDhcpSnoopBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 1),
    _FdryDhcpSnoopBindIpAddr_Type()
)
fdryDhcpSnoopBindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindIpAddr.setStatus("current")
_FdryDhcpSnoopBindMacAddr_Type = MacAddress
_FdryDhcpSnoopBindMacAddr_Object = MibTableColumn
fdryDhcpSnoopBindMacAddr = _FdryDhcpSnoopBindMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 2),
    _FdryDhcpSnoopBindMacAddr_Type()
)
fdryDhcpSnoopBindMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindMacAddr.setStatus("current")
_FdryDhcpSnoopBindType_Type = ArpType
_FdryDhcpSnoopBindType_Object = MibTableColumn
fdryDhcpSnoopBindType = _FdryDhcpSnoopBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 3),
    _FdryDhcpSnoopBindType_Type()
)
fdryDhcpSnoopBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindType.setStatus("current")
_FdryDhcpSnoopBindState_Type = ArpState
_FdryDhcpSnoopBindState_Object = MibTableColumn
fdryDhcpSnoopBindState = _FdryDhcpSnoopBindState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 4),
    _FdryDhcpSnoopBindState_Type()
)
fdryDhcpSnoopBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindState.setStatus("current")
_FdryDhcpSnoopBindPort_Type = DisplayString
_FdryDhcpSnoopBindPort_Object = MibTableColumn
fdryDhcpSnoopBindPort = _FdryDhcpSnoopBindPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 5),
    _FdryDhcpSnoopBindPort_Type()
)
fdryDhcpSnoopBindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindPort.setStatus("current")
_FdryDhcpSnoopBindVlanId_Type = VlanIndex
_FdryDhcpSnoopBindVlanId_Object = MibTableColumn
fdryDhcpSnoopBindVlanId = _FdryDhcpSnoopBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 6),
    _FdryDhcpSnoopBindVlanId_Type()
)
fdryDhcpSnoopBindVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindVlanId.setStatus("current")
_FdryDhcpSnoopBindClearOper_Type = ClearAction
_FdryDhcpSnoopBindClearOper_Object = MibTableColumn
fdryDhcpSnoopBindClearOper = _FdryDhcpSnoopBindClearOper_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 36, 4, 1, 1, 7),
    _FdryDhcpSnoopBindClearOper_Type()
)
fdryDhcpSnoopBindClearOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDhcpSnoopBindClearOper.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-DHCP-SNOOPING-MIB",
    **{"ClearAction": ClearAction,
       "fdryDhcpSnoopMIB": fdryDhcpSnoopMIB,
       "fdryDhcpSnoopGlobalObjects": fdryDhcpSnoopGlobalObjects,
       "fdryDhcpSnoopGlobalClearOper": fdryDhcpSnoopGlobalClearOper,
       "fdryDhcpSnoopVlan": fdryDhcpSnoopVlan,
       "fdryDhcpSnoopVlanConfigTable": fdryDhcpSnoopVlanConfigTable,
       "fdryDhcpSnoopVlanConfigEntry": fdryDhcpSnoopVlanConfigEntry,
       "fdryDhcpSnoopVlanVLanId": fdryDhcpSnoopVlanVLanId,
       "fdryDhcpSnoopVlanDhcpSnoopEnable": fdryDhcpSnoopVlanDhcpSnoopEnable,
       "fdryDhcpSnoopInterface": fdryDhcpSnoopInterface,
       "fdryDhcpSnoopIfConfigTable": fdryDhcpSnoopIfConfigTable,
       "fdryDhcpSnoopIfConfigEntry": fdryDhcpSnoopIfConfigEntry,
       "fdryDhcpSnoopIfTrustValue": fdryDhcpSnoopIfTrustValue,
       "fdryDhcpSnoopBind": fdryDhcpSnoopBind,
       "fdryDhcpSnoopBindTable": fdryDhcpSnoopBindTable,
       "fdryDhcpSnoopBindEntry": fdryDhcpSnoopBindEntry,
       "fdryDhcpSnoopBindIpAddr": fdryDhcpSnoopBindIpAddr,
       "fdryDhcpSnoopBindMacAddr": fdryDhcpSnoopBindMacAddr,
       "fdryDhcpSnoopBindType": fdryDhcpSnoopBindType,
       "fdryDhcpSnoopBindState": fdryDhcpSnoopBindState,
       "fdryDhcpSnoopBindPort": fdryDhcpSnoopBindPort,
       "fdryDhcpSnoopBindVlanId": fdryDhcpSnoopBindVlanId,
       "fdryDhcpSnoopBindClearOper": fdryDhcpSnoopBindClearOper}
)
