# SNMP MIB module (FDRY-IP-SOURCE-GUARD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FDRY-IP-SOURCE-GUARD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:44:40 2024
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

(snSwitch,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-SWITCH-GROUP-MIB",
    "snSwitch")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fdryIpSrcGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37)
)
fdryIpSrcGuardMIB.setRevisions(
        ("2010-07-26 00:00",
         "2010-02-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BindMode(Integer32, TextualConvention):
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
        *(("active", 2),
          ("inactive", 3),
          ("other", 1))
    )



class BindType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("other", 1))
    )



# MIB Managed Objects in the order of their OIDs

_FdryIpSrcGuardInterface_ObjectIdentity = ObjectIdentity
fdryIpSrcGuardInterface = _FdryIpSrcGuardInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1)
)
_FdryIpSrcGuardIfConfigTable_Object = MibTable
fdryIpSrcGuardIfConfigTable = _FdryIpSrcGuardIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1)
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardIfConfigTable.setStatus("current")
_FdryIpSrcGuardIfConfigEntry_Object = MibTableRow
fdryIpSrcGuardIfConfigEntry = _FdryIpSrcGuardIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1)
)
fdryIpSrcGuardIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardIfConfigEntry.setStatus("current")
_FdryIpSrcGuardIfEnable_Type = TruthValue
_FdryIpSrcGuardIfEnable_Object = MibTableColumn
fdryIpSrcGuardIfEnable = _FdryIpSrcGuardIfEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 1, 1, 1, 1),
    _FdryIpSrcGuardIfEnable_Type()
)
fdryIpSrcGuardIfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpSrcGuardIfEnable.setStatus("current")
_FdryIpSrcGuardPortVlan_ObjectIdentity = ObjectIdentity
fdryIpSrcGuardPortVlan = _FdryIpSrcGuardPortVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2)
)
_FdryIpSrcGuardPortVlanConfigTable_Object = MibTable
fdryIpSrcGuardPortVlanConfigTable = _FdryIpSrcGuardPortVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1)
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardPortVlanConfigTable.setStatus("current")
_FdryIpSrcGuardPortVlanConfigEntry_Object = MibTableRow
fdryIpSrcGuardPortVlanConfigEntry = _FdryIpSrcGuardPortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1)
)
fdryIpSrcGuardPortVlanConfigEntry.setIndexNames(
    (0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanPortId"),
    (0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardPortVlanVlanId"),
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardPortVlanConfigEntry.setStatus("current")
_FdryIpSrcGuardPortVlanPortId_Type = InterfaceIndex
_FdryIpSrcGuardPortVlanPortId_Object = MibTableColumn
fdryIpSrcGuardPortVlanPortId = _FdryIpSrcGuardPortVlanPortId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 1),
    _FdryIpSrcGuardPortVlanPortId_Type()
)
fdryIpSrcGuardPortVlanPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryIpSrcGuardPortVlanPortId.setStatus("current")
_FdryIpSrcGuardPortVlanVlanId_Type = VlanIndex
_FdryIpSrcGuardPortVlanVlanId_Object = MibTableColumn
fdryIpSrcGuardPortVlanVlanId = _FdryIpSrcGuardPortVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 2),
    _FdryIpSrcGuardPortVlanVlanId_Type()
)
fdryIpSrcGuardPortVlanVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryIpSrcGuardPortVlanVlanId.setStatus("current")
_FdryIpSrcGuardPortVlanEnable_Type = TruthValue
_FdryIpSrcGuardPortVlanEnable_Object = MibTableColumn
fdryIpSrcGuardPortVlanEnable = _FdryIpSrcGuardPortVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 2, 1, 1, 3),
    _FdryIpSrcGuardPortVlanEnable_Type()
)
fdryIpSrcGuardPortVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fdryIpSrcGuardPortVlanEnable.setStatus("current")
_FdryIpSrcGuardBind_ObjectIdentity = ObjectIdentity
fdryIpSrcGuardBind = _FdryIpSrcGuardBind_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3)
)
_FdryIpSrcGuardBindTable_Object = MibTable
fdryIpSrcGuardBindTable = _FdryIpSrcGuardBindTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1)
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindTable.setStatus("current")
_FdryIpSrcGuardBindEntry_Object = MibTableRow
fdryIpSrcGuardBindEntry = _FdryIpSrcGuardBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1)
)
fdryIpSrcGuardBindEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FDRY-IP-SOURCE-GUARD-MIB", "fdryIpSrcGuardBindIpAddr"),
)
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindEntry.setStatus("current")
_FdryIpSrcGuardBindIpAddr_Type = IpAddress
_FdryIpSrcGuardBindIpAddr_Object = MibTableColumn
fdryIpSrcGuardBindIpAddr = _FdryIpSrcGuardBindIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 1),
    _FdryIpSrcGuardBindIpAddr_Type()
)
fdryIpSrcGuardBindIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindIpAddr.setStatus("current")
_FdryIpSrcGuardBindVlanId_Type = Unsigned32
_FdryIpSrcGuardBindVlanId_Object = MibTableColumn
fdryIpSrcGuardBindVlanId = _FdryIpSrcGuardBindVlanId_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 2),
    _FdryIpSrcGuardBindVlanId_Type()
)
fdryIpSrcGuardBindVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindVlanId.setStatus("current")
_FdryIpSrcGuardBindRowStatus_Type = RowStatus
_FdryIpSrcGuardBindRowStatus_Object = MibTableColumn
fdryIpSrcGuardBindRowStatus = _FdryIpSrcGuardBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 3),
    _FdryIpSrcGuardBindRowStatus_Type()
)
fdryIpSrcGuardBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindRowStatus.setStatus("current")
_FdryIpSrcGuardBindMode_Type = BindMode
_FdryIpSrcGuardBindMode_Object = MibTableColumn
fdryIpSrcGuardBindMode = _FdryIpSrcGuardBindMode_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 4),
    _FdryIpSrcGuardBindMode_Type()
)
fdryIpSrcGuardBindMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindMode.setStatus("current")
_FdryIpSrcGuardBindType_Type = BindType
_FdryIpSrcGuardBindType_Object = MibTableColumn
fdryIpSrcGuardBindType = _FdryIpSrcGuardBindType_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 1, 3, 37, 3, 1, 1, 5),
    _FdryIpSrcGuardBindType_Type()
)
fdryIpSrcGuardBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdryIpSrcGuardBindType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FDRY-IP-SOURCE-GUARD-MIB",
    **{"BindMode": BindMode,
       "BindType": BindType,
       "fdryIpSrcGuardMIB": fdryIpSrcGuardMIB,
       "fdryIpSrcGuardInterface": fdryIpSrcGuardInterface,
       "fdryIpSrcGuardIfConfigTable": fdryIpSrcGuardIfConfigTable,
       "fdryIpSrcGuardIfConfigEntry": fdryIpSrcGuardIfConfigEntry,
       "fdryIpSrcGuardIfEnable": fdryIpSrcGuardIfEnable,
       "fdryIpSrcGuardPortVlan": fdryIpSrcGuardPortVlan,
       "fdryIpSrcGuardPortVlanConfigTable": fdryIpSrcGuardPortVlanConfigTable,
       "fdryIpSrcGuardPortVlanConfigEntry": fdryIpSrcGuardPortVlanConfigEntry,
       "fdryIpSrcGuardPortVlanPortId": fdryIpSrcGuardPortVlanPortId,
       "fdryIpSrcGuardPortVlanVlanId": fdryIpSrcGuardPortVlanVlanId,
       "fdryIpSrcGuardPortVlanEnable": fdryIpSrcGuardPortVlanEnable,
       "fdryIpSrcGuardBind": fdryIpSrcGuardBind,
       "fdryIpSrcGuardBindTable": fdryIpSrcGuardBindTable,
       "fdryIpSrcGuardBindEntry": fdryIpSrcGuardBindEntry,
       "fdryIpSrcGuardBindIpAddr": fdryIpSrcGuardBindIpAddr,
       "fdryIpSrcGuardBindVlanId": fdryIpSrcGuardBindVlanId,
       "fdryIpSrcGuardBindRowStatus": fdryIpSrcGuardBindRowStatus,
       "fdryIpSrcGuardBindMode": fdryIpSrcGuardBindMode,
       "fdryIpSrcGuardBindType": fdryIpSrcGuardBindType}
)
