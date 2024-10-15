# SNMP MIB module (DHCP-RELAY-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DHCP-RELAY-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:28:59 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

swDHCPRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwDHCPRelayCtrl_ObjectIdentity = ObjectIdentity
swDHCPRelayCtrl = _SwDHCPRelayCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 1)
)


class _SwDHCPRelayState_Type(Integer32):
    """Custom type swDHCPRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPRelayState_Type.__name__ = "Integer32"
_SwDHCPRelayState_Object = MibScalar
swDHCPRelayState = _SwDHCPRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 1),
    _SwDHCPRelayState_Type()
)
swDHCPRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayState.setStatus("current")


class _SwDHCPRelayHopCount_Type(Integer32):
    """Custom type swDHCPRelayHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwDHCPRelayHopCount_Type.__name__ = "Integer32"
_SwDHCPRelayHopCount_Object = MibScalar
swDHCPRelayHopCount = _SwDHCPRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 2),
    _SwDHCPRelayHopCount_Type()
)
swDHCPRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayHopCount.setStatus("current")


class _SwDHCPRelayTimeThreshold_Type(Integer32):
    """Custom type swDHCPRelayTimeThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwDHCPRelayTimeThreshold_Type.__name__ = "Integer32"
_SwDHCPRelayTimeThreshold_Object = MibScalar
swDHCPRelayTimeThreshold = _SwDHCPRelayTimeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 1, 3),
    _SwDHCPRelayTimeThreshold_Type()
)
swDHCPRelayTimeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayTimeThreshold.setStatus("current")
_SwDHCPRelayInfo_ObjectIdentity = ObjectIdentity
swDHCPRelayInfo = _SwDHCPRelayInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 2)
)
_SwDHCPRelayMgmt_ObjectIdentity = ObjectIdentity
swDHCPRelayMgmt = _SwDHCPRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3)
)
_SwDHCPRelayCtrlTable_Object = MibTable
swDHCPRelayCtrlTable = _SwDHCPRelayCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1)
)
if mibBuilder.loadTexts:
    swDHCPRelayCtrlTable.setStatus("current")
_SwDHCPRelayCtrlEntry_Object = MibTableRow
swDHCPRelayCtrlEntry = _SwDHCPRelayCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1)
)
swDHCPRelayCtrlEntry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayCtrlInterfaceName"),
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayCtrlServer"),
)
if mibBuilder.loadTexts:
    swDHCPRelayCtrlEntry.setStatus("current")


class _SwDHCPRelayCtrlInterfaceName_Type(DisplayString):
    """Custom type swDHCPRelayCtrlInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwDHCPRelayCtrlInterfaceName_Type.__name__ = "DisplayString"
_SwDHCPRelayCtrlInterfaceName_Object = MibTableColumn
swDHCPRelayCtrlInterfaceName = _SwDHCPRelayCtrlInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 1),
    _SwDHCPRelayCtrlInterfaceName_Type()
)
swDHCPRelayCtrlInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayCtrlInterfaceName.setStatus("current")
_SwDHCPRelayCtrlServer_Type = IpAddress
_SwDHCPRelayCtrlServer_Object = MibTableColumn
swDHCPRelayCtrlServer = _SwDHCPRelayCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 2),
    _SwDHCPRelayCtrlServer_Type()
)
swDHCPRelayCtrlServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayCtrlServer.setStatus("current")
_SwDHCPRelayCtrlRowStatus_Type = RowStatus
_SwDHCPRelayCtrlRowStatus_Object = MibTableColumn
swDHCPRelayCtrlRowStatus = _SwDHCPRelayCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 1, 1, 3),
    _SwDHCPRelayCtrlRowStatus_Type()
)
swDHCPRelayCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayCtrlRowStatus.setStatus("current")
_SwDHCPRelayOption82_ObjectIdentity = ObjectIdentity
swDHCPRelayOption82 = _SwDHCPRelayOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2)
)


class _SwDHCPRelayOption82State_Type(Integer32):
    """Custom type swDHCPRelayOption82State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPRelayOption82State_Type.__name__ = "Integer32"
_SwDHCPRelayOption82State_Object = MibScalar
swDHCPRelayOption82State = _SwDHCPRelayOption82State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 1),
    _SwDHCPRelayOption82State_Type()
)
swDHCPRelayOption82State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption82State.setStatus("current")


class _SwDHCPRelayOption82CheckState_Type(Integer32):
    """Custom type swDHCPRelayOption82CheckState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPRelayOption82CheckState_Type.__name__ = "Integer32"
_SwDHCPRelayOption82CheckState_Object = MibScalar
swDHCPRelayOption82CheckState = _SwDHCPRelayOption82CheckState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 2),
    _SwDHCPRelayOption82CheckState_Type()
)
swDHCPRelayOption82CheckState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption82CheckState.setStatus("current")


class _SwDHCPRelayOption82Policy_Type(Integer32):
    """Custom type swDHCPRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("keep", 3),
          ("replace", 1))
    )


_SwDHCPRelayOption82Policy_Type.__name__ = "Integer32"
_SwDHCPRelayOption82Policy_Object = MibScalar
swDHCPRelayOption82Policy = _SwDHCPRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 3),
    _SwDHCPRelayOption82Policy_Type()
)
swDHCPRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption82Policy.setStatus("current")


class _SwDHCPRelayOption82RemoteIDType_Type(Integer32):
    """Custom type swDHCPRelayOption82RemoteIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("user-defined", 2))
    )


_SwDHCPRelayOption82RemoteIDType_Type.__name__ = "Integer32"
_SwDHCPRelayOption82RemoteIDType_Object = MibScalar
swDHCPRelayOption82RemoteIDType = _SwDHCPRelayOption82RemoteIDType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 4),
    _SwDHCPRelayOption82RemoteIDType_Type()
)
swDHCPRelayOption82RemoteIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption82RemoteIDType.setStatus("current")
_SwDHCPRelayOption82RemoteID_Type = DisplayString
_SwDHCPRelayOption82RemoteID_Object = MibScalar
swDHCPRelayOption82RemoteID = _SwDHCPRelayOption82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 2, 5),
    _SwDHCPRelayOption82RemoteID_Type()
)
swDHCPRelayOption82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption82RemoteID.setStatus("current")
_SwDHCPRelayOption60_ObjectIdentity = ObjectIdentity
swDHCPRelayOption60 = _SwDHCPRelayOption60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3)
)


class _SwDHCPRelayOption60State_Type(Integer32):
    """Custom type swDHCPRelayOption60State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPRelayOption60State_Type.__name__ = "Integer32"
_SwDHCPRelayOption60State_Object = MibScalar
swDHCPRelayOption60State = _SwDHCPRelayOption60State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 1),
    _SwDHCPRelayOption60State_Type()
)
swDHCPRelayOption60State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption60State.setStatus("current")


class _SwDHCPRelayOption60DefMode_Type(Integer32):
    """Custom type swDHCPRelayOption60DefMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("relay", 1))
    )


_SwDHCPRelayOption60DefMode_Type.__name__ = "Integer32"
_SwDHCPRelayOption60DefMode_Object = MibScalar
swDHCPRelayOption60DefMode = _SwDHCPRelayOption60DefMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 2),
    _SwDHCPRelayOption60DefMode_Type()
)
swDHCPRelayOption60DefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption60DefMode.setStatus("current")
_SwDHCPRelayOption60DefTable_Object = MibTable
swDHCPRelayOption60DefTable = _SwDHCPRelayOption60DefTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3)
)
if mibBuilder.loadTexts:
    swDHCPRelayOption60DefTable.setStatus("current")
_SwDHCPRelayOption60DefEntry_Object = MibTableRow
swDHCPRelayOption60DefEntry = _SwDHCPRelayOption60DefEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1)
)
swDHCPRelayOption60DefEntry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60DefRelayIp"),
)
if mibBuilder.loadTexts:
    swDHCPRelayOption60DefEntry.setStatus("current")
_SwDHCPRelayOption60DefRelayIp_Type = IpAddress
_SwDHCPRelayOption60DefRelayIp_Object = MibTableColumn
swDHCPRelayOption60DefRelayIp = _SwDHCPRelayOption60DefRelayIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1, 1),
    _SwDHCPRelayOption60DefRelayIp_Type()
)
swDHCPRelayOption60DefRelayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayOption60DefRelayIp.setStatus("current")
_SwDHCPRelayOption60DefRowStatus_Type = RowStatus
_SwDHCPRelayOption60DefRowStatus_Object = MibTableColumn
swDHCPRelayOption60DefRowStatus = _SwDHCPRelayOption60DefRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 3, 1, 2),
    _SwDHCPRelayOption60DefRowStatus_Type()
)
swDHCPRelayOption60DefRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption60DefRowStatus.setStatus("current")
_SwDHCPRelayOption60Table_Object = MibTable
swDHCPRelayOption60Table = _SwDHCPRelayOption60Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4)
)
if mibBuilder.loadTexts:
    swDHCPRelayOption60Table.setStatus("current")
_SwDHCPRelayOption60Entry_Object = MibTableRow
swDHCPRelayOption60Entry = _SwDHCPRelayOption60Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1)
)
swDHCPRelayOption60Entry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60String"),
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption60RelayIp"),
)
if mibBuilder.loadTexts:
    swDHCPRelayOption60Entry.setStatus("current")
_SwDHCPRelayOption60String_Type = DisplayString
_SwDHCPRelayOption60String_Object = MibTableColumn
swDHCPRelayOption60String = _SwDHCPRelayOption60String_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 1),
    _SwDHCPRelayOption60String_Type()
)
swDHCPRelayOption60String.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayOption60String.setStatus("current")
_SwDHCPRelayOption60RelayIp_Type = IpAddress
_SwDHCPRelayOption60RelayIp_Object = MibTableColumn
swDHCPRelayOption60RelayIp = _SwDHCPRelayOption60RelayIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 2),
    _SwDHCPRelayOption60RelayIp_Type()
)
swDHCPRelayOption60RelayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayOption60RelayIp.setStatus("current")


class _SwDHCPRelayOption60MatchType_Type(Integer32):
    """Custom type swDHCPRelayOption60MatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("partial", 2))
    )


_SwDHCPRelayOption60MatchType_Type.__name__ = "Integer32"
_SwDHCPRelayOption60MatchType_Object = MibTableColumn
swDHCPRelayOption60MatchType = _SwDHCPRelayOption60MatchType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 3),
    _SwDHCPRelayOption60MatchType_Type()
)
swDHCPRelayOption60MatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption60MatchType.setStatus("current")
_SwDHCPRelayOption60RowStatus_Type = RowStatus
_SwDHCPRelayOption60RowStatus_Object = MibTableColumn
swDHCPRelayOption60RowStatus = _SwDHCPRelayOption60RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 3, 4, 1, 4),
    _SwDHCPRelayOption60RowStatus_Type()
)
swDHCPRelayOption60RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption60RowStatus.setStatus("current")
_SwDHCPRelayOption61_ObjectIdentity = ObjectIdentity
swDHCPRelayOption61 = _SwDHCPRelayOption61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4)
)


class _SwDHCPRelayOption61State_Type(Integer32):
    """Custom type swDHCPRelayOption61State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPRelayOption61State_Type.__name__ = "Integer32"
_SwDHCPRelayOption61State_Object = MibScalar
swDHCPRelayOption61State = _SwDHCPRelayOption61State_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 1),
    _SwDHCPRelayOption61State_Type()
)
swDHCPRelayOption61State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption61State.setStatus("current")


class _SwDHCPRelayOption61DefMode_Type(Integer32):
    """Custom type swDHCPRelayOption61DefMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("relay", 1))
    )


_SwDHCPRelayOption61DefMode_Type.__name__ = "Integer32"
_SwDHCPRelayOption61DefMode_Object = MibScalar
swDHCPRelayOption61DefMode = _SwDHCPRelayOption61DefMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 2),
    _SwDHCPRelayOption61DefMode_Type()
)
swDHCPRelayOption61DefMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption61DefMode.setStatus("current")
_SwDHCPRelayOption61DefRelayIp_Type = IpAddress
_SwDHCPRelayOption61DefRelayIp_Object = MibScalar
swDHCPRelayOption61DefRelayIp = _SwDHCPRelayOption61DefRelayIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 3),
    _SwDHCPRelayOption61DefRelayIp_Type()
)
swDHCPRelayOption61DefRelayIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPRelayOption61DefRelayIp.setStatus("current")
_SwDHCPRelayOption61Table_Object = MibTable
swDHCPRelayOption61Table = _SwDHCPRelayOption61Table_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4)
)
if mibBuilder.loadTexts:
    swDHCPRelayOption61Table.setStatus("current")
_SwDHCPRelayOption61Entry_Object = MibTableRow
swDHCPRelayOption61Entry = _SwDHCPRelayOption61Entry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1)
)
swDHCPRelayOption61Entry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption61ClientType"),
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayOption61ClientID"),
)
if mibBuilder.loadTexts:
    swDHCPRelayOption61Entry.setStatus("current")


class _SwDHCPRelayOption61ClientType_Type(Integer32):
    """Custom type swDHCPRelayOption61ClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("string", 2))
    )


_SwDHCPRelayOption61ClientType_Type.__name__ = "Integer32"
_SwDHCPRelayOption61ClientType_Object = MibTableColumn
swDHCPRelayOption61ClientType = _SwDHCPRelayOption61ClientType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 1),
    _SwDHCPRelayOption61ClientType_Type()
)
swDHCPRelayOption61ClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayOption61ClientType.setStatus("current")
_SwDHCPRelayOption61ClientID_Type = DisplayString
_SwDHCPRelayOption61ClientID_Object = MibTableColumn
swDHCPRelayOption61ClientID = _SwDHCPRelayOption61ClientID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 2),
    _SwDHCPRelayOption61ClientID_Type()
)
swDHCPRelayOption61ClientID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDHCPRelayOption61ClientID.setStatus("current")


class _SwDHCPRelayOption61Mode_Type(Integer32):
    """Custom type swDHCPRelayOption61Mode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 2),
          ("relay", 1))
    )


_SwDHCPRelayOption61Mode_Type.__name__ = "Integer32"
_SwDHCPRelayOption61Mode_Object = MibTableColumn
swDHCPRelayOption61Mode = _SwDHCPRelayOption61Mode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 3),
    _SwDHCPRelayOption61Mode_Type()
)
swDHCPRelayOption61Mode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption61Mode.setStatus("current")
_SwDHCPRelayOption61RelayIp_Type = IpAddress
_SwDHCPRelayOption61RelayIp_Object = MibTableColumn
swDHCPRelayOption61RelayIp = _SwDHCPRelayOption61RelayIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 4),
    _SwDHCPRelayOption61RelayIp_Type()
)
swDHCPRelayOption61RelayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption61RelayIp.setStatus("current")
_SwDHCPRelayOption61RowStatus_Type = RowStatus
_SwDHCPRelayOption61RowStatus_Object = MibTableColumn
swDHCPRelayOption61RowStatus = _SwDHCPRelayOption61RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 4, 4, 1, 5),
    _SwDHCPRelayOption61RowStatus_Type()
)
swDHCPRelayOption61RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayOption61RowStatus.setStatus("current")
_SwDHCPRelayVlanCtrlTable_Object = MibTable
swDHCPRelayVlanCtrlTable = _SwDHCPRelayVlanCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5)
)
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlTable.setStatus("current")
_SwDHCPRelayVlanCtrlEntry_Object = MibTableRow
swDHCPRelayVlanCtrlEntry = _SwDHCPRelayVlanCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1)
)
swDHCPRelayVlanCtrlEntry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPRelayVlanCtrlServer"),
)
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlEntry.setStatus("current")
_SwDHCPRelayVlanCtrlServer_Type = IpAddress
_SwDHCPRelayVlanCtrlServer_Object = MibTableColumn
swDHCPRelayVlanCtrlServer = _SwDHCPRelayVlanCtrlServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 1),
    _SwDHCPRelayVlanCtrlServer_Type()
)
swDHCPRelayVlanCtrlServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlServer.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList1to64_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList1to64 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList1to64_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList1to64_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList1to64 = _SwDHCPRelayVlanCtrlVlanRangeList1to64_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 2),
    _SwDHCPRelayVlanCtrlVlanRangeList1to64_Type()
)
swDHCPRelayVlanCtrlVlanRangeList1to64.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList1to64.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList65to128_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList65to128 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList65to128_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList65to128_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList65to128 = _SwDHCPRelayVlanCtrlVlanRangeList65to128_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 3),
    _SwDHCPRelayVlanCtrlVlanRangeList65to128_Type()
)
swDHCPRelayVlanCtrlVlanRangeList65to128.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList65to128.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList129to192_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList129to192 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList129to192_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList129to192_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList129to192 = _SwDHCPRelayVlanCtrlVlanRangeList129to192_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 4),
    _SwDHCPRelayVlanCtrlVlanRangeList129to192_Type()
)
swDHCPRelayVlanCtrlVlanRangeList129to192.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList129to192.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList193to256_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList193to256 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList193to256_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList193to256_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList193to256 = _SwDHCPRelayVlanCtrlVlanRangeList193to256_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 5),
    _SwDHCPRelayVlanCtrlVlanRangeList193to256_Type()
)
swDHCPRelayVlanCtrlVlanRangeList193to256.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList193to256.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList257to320_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList257to320 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList257to320_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList257to320_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList257to320 = _SwDHCPRelayVlanCtrlVlanRangeList257to320_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 6),
    _SwDHCPRelayVlanCtrlVlanRangeList257to320_Type()
)
swDHCPRelayVlanCtrlVlanRangeList257to320.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList257to320.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList321to384_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList321to384 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList321to384_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList321to384_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList321to384 = _SwDHCPRelayVlanCtrlVlanRangeList321to384_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 7),
    _SwDHCPRelayVlanCtrlVlanRangeList321to384_Type()
)
swDHCPRelayVlanCtrlVlanRangeList321to384.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList321to384.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList385to448_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList385to448 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList385to448_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList385to448_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList385to448 = _SwDHCPRelayVlanCtrlVlanRangeList385to448_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 8),
    _SwDHCPRelayVlanCtrlVlanRangeList385to448_Type()
)
swDHCPRelayVlanCtrlVlanRangeList385to448.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList385to448.setStatus("current")


class _SwDHCPRelayVlanCtrlVlanRangeList449to512_Type(OctetString):
    """Custom type swDHCPRelayVlanCtrlVlanRangeList449to512 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_SwDHCPRelayVlanCtrlVlanRangeList449to512_Type.__name__ = "OctetString"
_SwDHCPRelayVlanCtrlVlanRangeList449to512_Object = MibTableColumn
swDHCPRelayVlanCtrlVlanRangeList449to512 = _SwDHCPRelayVlanCtrlVlanRangeList449to512_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 9),
    _SwDHCPRelayVlanCtrlVlanRangeList449to512_Type()
)
swDHCPRelayVlanCtrlVlanRangeList449to512.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlVlanRangeList449to512.setStatus("current")
_SwDHCPRelayVlanCtrlRowStatus_Type = RowStatus
_SwDHCPRelayVlanCtrlRowStatus_Object = MibTableColumn
swDHCPRelayVlanCtrlRowStatus = _SwDHCPRelayVlanCtrlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 3, 5, 1, 10),
    _SwDHCPRelayVlanCtrlRowStatus_Type()
)
swDHCPRelayVlanCtrlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swDHCPRelayVlanCtrlRowStatus.setStatus("current")
_SwDHCPLocalRelayMgmt_ObjectIdentity = ObjectIdentity
swDHCPLocalRelayMgmt = _SwDHCPLocalRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4)
)


class _SwDHCPLocalRelayGlobalState_Type(Integer32):
    """Custom type swDHCPLocalRelayGlobalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPLocalRelayGlobalState_Type.__name__ = "Integer32"
_SwDHCPLocalRelayGlobalState_Object = MibScalar
swDHCPLocalRelayGlobalState = _SwDHCPLocalRelayGlobalState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 1),
    _SwDHCPLocalRelayGlobalState_Type()
)
swDHCPLocalRelayGlobalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPLocalRelayGlobalState.setStatus("current")
_SwDHCPLocalRelayVlanTable_Object = MibTable
swDHCPLocalRelayVlanTable = _SwDHCPLocalRelayVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2)
)
if mibBuilder.loadTexts:
    swDHCPLocalRelayVlanTable.setStatus("current")
_SwDHCPLocalRelayVlanEntry_Object = MibTableRow
swDHCPLocalRelayVlanEntry = _SwDHCPLocalRelayVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1)
)
swDHCPLocalRelayVlanEntry.setIndexNames(
    (0, "DHCP-RELAY-MGMT-MIB", "swDHCPLocalRelayVlanID"),
)
if mibBuilder.loadTexts:
    swDHCPLocalRelayVlanEntry.setStatus("current")
_SwDHCPLocalRelayVlanID_Type = VlanId
_SwDHCPLocalRelayVlanID_Object = MibTableColumn
swDHCPLocalRelayVlanID = _SwDHCPLocalRelayVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1, 1),
    _SwDHCPLocalRelayVlanID_Type()
)
swDHCPLocalRelayVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swDHCPLocalRelayVlanID.setStatus("current")


class _SwDHCPLocalRelayState_Type(Integer32):
    """Custom type swDHCPLocalRelayState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_SwDHCPLocalRelayState_Type.__name__ = "Integer32"
_SwDHCPLocalRelayState_Object = MibTableColumn
swDHCPLocalRelayState = _SwDHCPLocalRelayState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 42, 4, 2, 1, 2),
    _SwDHCPLocalRelayState_Type()
)
swDHCPLocalRelayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDHCPLocalRelayState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-RELAY-MGMT-MIB",
    **{"swDHCPRelayMIB": swDHCPRelayMIB,
       "swDHCPRelayCtrl": swDHCPRelayCtrl,
       "swDHCPRelayState": swDHCPRelayState,
       "swDHCPRelayHopCount": swDHCPRelayHopCount,
       "swDHCPRelayTimeThreshold": swDHCPRelayTimeThreshold,
       "swDHCPRelayInfo": swDHCPRelayInfo,
       "swDHCPRelayMgmt": swDHCPRelayMgmt,
       "swDHCPRelayCtrlTable": swDHCPRelayCtrlTable,
       "swDHCPRelayCtrlEntry": swDHCPRelayCtrlEntry,
       "swDHCPRelayCtrlInterfaceName": swDHCPRelayCtrlInterfaceName,
       "swDHCPRelayCtrlServer": swDHCPRelayCtrlServer,
       "swDHCPRelayCtrlRowStatus": swDHCPRelayCtrlRowStatus,
       "swDHCPRelayOption82": swDHCPRelayOption82,
       "swDHCPRelayOption82State": swDHCPRelayOption82State,
       "swDHCPRelayOption82CheckState": swDHCPRelayOption82CheckState,
       "swDHCPRelayOption82Policy": swDHCPRelayOption82Policy,
       "swDHCPRelayOption82RemoteIDType": swDHCPRelayOption82RemoteIDType,
       "swDHCPRelayOption82RemoteID": swDHCPRelayOption82RemoteID,
       "swDHCPRelayOption60": swDHCPRelayOption60,
       "swDHCPRelayOption60State": swDHCPRelayOption60State,
       "swDHCPRelayOption60DefMode": swDHCPRelayOption60DefMode,
       "swDHCPRelayOption60DefTable": swDHCPRelayOption60DefTable,
       "swDHCPRelayOption60DefEntry": swDHCPRelayOption60DefEntry,
       "swDHCPRelayOption60DefRelayIp": swDHCPRelayOption60DefRelayIp,
       "swDHCPRelayOption60DefRowStatus": swDHCPRelayOption60DefRowStatus,
       "swDHCPRelayOption60Table": swDHCPRelayOption60Table,
       "swDHCPRelayOption60Entry": swDHCPRelayOption60Entry,
       "swDHCPRelayOption60String": swDHCPRelayOption60String,
       "swDHCPRelayOption60RelayIp": swDHCPRelayOption60RelayIp,
       "swDHCPRelayOption60MatchType": swDHCPRelayOption60MatchType,
       "swDHCPRelayOption60RowStatus": swDHCPRelayOption60RowStatus,
       "swDHCPRelayOption61": swDHCPRelayOption61,
       "swDHCPRelayOption61State": swDHCPRelayOption61State,
       "swDHCPRelayOption61DefMode": swDHCPRelayOption61DefMode,
       "swDHCPRelayOption61DefRelayIp": swDHCPRelayOption61DefRelayIp,
       "swDHCPRelayOption61Table": swDHCPRelayOption61Table,
       "swDHCPRelayOption61Entry": swDHCPRelayOption61Entry,
       "swDHCPRelayOption61ClientType": swDHCPRelayOption61ClientType,
       "swDHCPRelayOption61ClientID": swDHCPRelayOption61ClientID,
       "swDHCPRelayOption61Mode": swDHCPRelayOption61Mode,
       "swDHCPRelayOption61RelayIp": swDHCPRelayOption61RelayIp,
       "swDHCPRelayOption61RowStatus": swDHCPRelayOption61RowStatus,
       "swDHCPRelayVlanCtrlTable": swDHCPRelayVlanCtrlTable,
       "swDHCPRelayVlanCtrlEntry": swDHCPRelayVlanCtrlEntry,
       "swDHCPRelayVlanCtrlServer": swDHCPRelayVlanCtrlServer,
       "swDHCPRelayVlanCtrlVlanRangeList1to64": swDHCPRelayVlanCtrlVlanRangeList1to64,
       "swDHCPRelayVlanCtrlVlanRangeList65to128": swDHCPRelayVlanCtrlVlanRangeList65to128,
       "swDHCPRelayVlanCtrlVlanRangeList129to192": swDHCPRelayVlanCtrlVlanRangeList129to192,
       "swDHCPRelayVlanCtrlVlanRangeList193to256": swDHCPRelayVlanCtrlVlanRangeList193to256,
       "swDHCPRelayVlanCtrlVlanRangeList257to320": swDHCPRelayVlanCtrlVlanRangeList257to320,
       "swDHCPRelayVlanCtrlVlanRangeList321to384": swDHCPRelayVlanCtrlVlanRangeList321to384,
       "swDHCPRelayVlanCtrlVlanRangeList385to448": swDHCPRelayVlanCtrlVlanRangeList385to448,
       "swDHCPRelayVlanCtrlVlanRangeList449to512": swDHCPRelayVlanCtrlVlanRangeList449to512,
       "swDHCPRelayVlanCtrlRowStatus": swDHCPRelayVlanCtrlRowStatus,
       "swDHCPLocalRelayMgmt": swDHCPLocalRelayMgmt,
       "swDHCPLocalRelayGlobalState": swDHCPLocalRelayGlobalState,
       "swDHCPLocalRelayVlanTable": swDHCPLocalRelayVlanTable,
       "swDHCPLocalRelayVlanEntry": swDHCPLocalRelayVlanEntry,
       "swDHCPLocalRelayVlanID": swDHCPLocalRelayVlanID,
       "swDHCPLocalRelayState": swDHCPLocalRelayState}
)
