# SNMP MIB module (FDRY-DAI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-DAI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:36 2024
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fdryDaiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35)
)
fdryDaiMIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class ArpType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 5),
          ("dynamic", 3),
          ("dynamicDhcp", 6),
          ("host", 8),
          ("inspect", 4),
          ("other", 1),
          ("static", 2),
          ("staticDhcp", 7))
    )



class ArpState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pend", 3),
          ("valid", 2))
    )



# MIB Managed Objects in the order of their OIDs

_FdryDaiVlan_ObjectIdentity = ObjectIdentity
fdryDaiVlan = _FdryDaiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1)
)
_FdryDaiVlanConfigTable_Object = MibTable
fdryDaiVlanConfigTable = _FdryDaiVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1)
)
if mibBuilder.loadTexts:
    fdryDaiVlanConfigTable.setStatus("current")
_FdryDaiVlanConfigEntry_Object = MibTableRow
fdryDaiVlanConfigEntry = _FdryDaiVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1)
)
fdryDaiVlanConfigEntry.setIndexNames(
    (0, "FDRY-DAI-MIB", "fdryDaiVlanVLanId"),
)
if mibBuilder.loadTexts:
    fdryDaiVlanConfigEntry.setStatus("current")
_FdryDaiVlanVLanId_Type = VlanIndex
_FdryDaiVlanVLanId_Object = MibTableColumn
fdryDaiVlanVLanId = _FdryDaiVlanVLanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1, 1),
    _FdryDaiVlanVLanId_Type()
)
fdryDaiVlanVLanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDaiVlanVLanId.setStatus("current")
_FdryDaiVlanDynArpInspEnable_Type = TruthValue
_FdryDaiVlanDynArpInspEnable_Object = MibTableColumn
fdryDaiVlanDynArpInspEnable = _FdryDaiVlanDynArpInspEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 1, 1, 1, 2),
    _FdryDaiVlanDynArpInspEnable_Type()
)
fdryDaiVlanDynArpInspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDaiVlanDynArpInspEnable.setStatus("current")
_FdryDaiInterface_ObjectIdentity = ObjectIdentity
fdryDaiInterface = _FdryDaiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2)
)
_FdryDaiIfConfigTable_Object = MibTable
fdryDaiIfConfigTable = _FdryDaiIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1)
)
if mibBuilder.loadTexts:
    fdryDaiIfConfigTable.setStatus("current")
_FdryDaiIfConfigEntry_Object = MibTableRow
fdryDaiIfConfigEntry = _FdryDaiIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1, 1)
)
fdryDaiIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryDaiIfConfigEntry.setStatus("current")
_FdryDaiIfTrustValue_Type = TruthValue
_FdryDaiIfTrustValue_Object = MibTableColumn
fdryDaiIfTrustValue = _FdryDaiIfTrustValue_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 2, 1, 1, 1),
    _FdryDaiIfTrustValue_Type()
)
fdryDaiIfTrustValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryDaiIfTrustValue.setStatus("current")
_FdryDaiArpInspect_ObjectIdentity = ObjectIdentity
fdryDaiArpInspect = _FdryDaiArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3)
)
_FdryDaiArpInspectTable_Object = MibTable
fdryDaiArpInspectTable = _FdryDaiArpInspectTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1)
)
if mibBuilder.loadTexts:
    fdryDaiArpInspectTable.setStatus("current")
_FdryDaiArpInspectEntry_Object = MibTableRow
fdryDaiArpInspectEntry = _FdryDaiArpInspectEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1)
)
fdryDaiArpInspectEntry.setIndexNames(
    (0, "FDRY-DAI-MIB", "fdryDaiArpInspectIpAddr"),
)
if mibBuilder.loadTexts:
    fdryDaiArpInspectEntry.setStatus("current")
_FdryDaiArpInspectIpAddr_Type = IpAddress
_FdryDaiArpInspectIpAddr_Object = MibTableColumn
fdryDaiArpInspectIpAddr = _FdryDaiArpInspectIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 1),
    _FdryDaiArpInspectIpAddr_Type()
)
fdryDaiArpInspectIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryDaiArpInspectIpAddr.setStatus("current")
_FdryDaiArpInspectMacAddr_Type = MacAddress
_FdryDaiArpInspectMacAddr_Object = MibTableColumn
fdryDaiArpInspectMacAddr = _FdryDaiArpInspectMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 2),
    _FdryDaiArpInspectMacAddr_Type()
)
fdryDaiArpInspectMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDaiArpInspectMacAddr.setStatus("current")
_FdryDaiArpInspectRowStatus_Type = RowStatus
_FdryDaiArpInspectRowStatus_Object = MibTableColumn
fdryDaiArpInspectRowStatus = _FdryDaiArpInspectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 3),
    _FdryDaiArpInspectRowStatus_Type()
)
fdryDaiArpInspectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryDaiArpInspectRowStatus.setStatus("current")
_FdryDaiArpInspectType_Type = ArpType
_FdryDaiArpInspectType_Object = MibTableColumn
fdryDaiArpInspectType = _FdryDaiArpInspectType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 4),
    _FdryDaiArpInspectType_Type()
)
fdryDaiArpInspectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDaiArpInspectType.setStatus("current")
_FdryDaiArpInspectState_Type = ArpState
_FdryDaiArpInspectState_Object = MibTableColumn
fdryDaiArpInspectState = _FdryDaiArpInspectState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 5),
    _FdryDaiArpInspectState_Type()
)
fdryDaiArpInspectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDaiArpInspectState.setStatus("current")
_FdryDaiArpInspectAge_Type = Unsigned32
_FdryDaiArpInspectAge_Object = MibTableColumn
fdryDaiArpInspectAge = _FdryDaiArpInspectAge_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 6),
    _FdryDaiArpInspectAge_Type()
)
fdryDaiArpInspectAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDaiArpInspectAge.setStatus("current")
_FdryDaiArpInspectPort_Type = DisplayString
_FdryDaiArpInspectPort_Object = MibTableColumn
fdryDaiArpInspectPort = _FdryDaiArpInspectPort_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 35, 3, 1, 1, 7),
    _FdryDaiArpInspectPort_Type()
)
fdryDaiArpInspectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryDaiArpInspectPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-DAI-MIB",
    **{"ArpType": ArpType,
       "ArpState": ArpState,
       "fdryDaiMIB": fdryDaiMIB,
       "fdryDaiVlan": fdryDaiVlan,
       "fdryDaiVlanConfigTable": fdryDaiVlanConfigTable,
       "fdryDaiVlanConfigEntry": fdryDaiVlanConfigEntry,
       "fdryDaiVlanVLanId": fdryDaiVlanVLanId,
       "fdryDaiVlanDynArpInspEnable": fdryDaiVlanDynArpInspEnable,
       "fdryDaiInterface": fdryDaiInterface,
       "fdryDaiIfConfigTable": fdryDaiIfConfigTable,
       "fdryDaiIfConfigEntry": fdryDaiIfConfigEntry,
       "fdryDaiIfTrustValue": fdryDaiIfTrustValue,
       "fdryDaiArpInspect": fdryDaiArpInspect,
       "fdryDaiArpInspectTable": fdryDaiArpInspectTable,
       "fdryDaiArpInspectEntry": fdryDaiArpInspectEntry,
       "fdryDaiArpInspectIpAddr": fdryDaiArpInspectIpAddr,
       "fdryDaiArpInspectMacAddr": fdryDaiArpInspectMacAddr,
       "fdryDaiArpInspectRowStatus": fdryDaiArpInspectRowStatus,
       "fdryDaiArpInspectType": fdryDaiArpInspectType,
       "fdryDaiArpInspectState": fdryDaiArpInspectState,
       "fdryDaiArpInspectAge": fdryDaiArpInspectAge,
       "fdryDaiArpInspectPort": fdryDaiArpInspectPort}
)
