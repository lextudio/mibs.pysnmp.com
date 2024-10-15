# SNMP MIB module (HP-ICF-UDP-FORWARD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-UDP-FORWARD
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:21 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfUdpFwd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23)
)
hpicfUdpFwd.setRevisions(
        ("2017-06-13 06:30",
         "2013-01-04 06:30",
         "2009-08-04 06:30",
         "2004-05-19 06:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfUdpFwdNotification_ObjectIdentity = ObjectIdentity
hpicfUdpFwdNotification = _HpicfUdpFwdNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 0)
)
_HpicfUdpFwdObjects_ObjectIdentity = ObjectIdentity
hpicfUdpFwdObjects = _HpicfUdpFwdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1)
)


class _HpicfUdpBcastFwdAdminStatus_Type(Integer32):
    """Custom type hpicfUdpBcastFwdAdminStatus based on Integer32"""
    defaultValue = 2

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


_HpicfUdpBcastFwdAdminStatus_Type.__name__ = "Integer32"
_HpicfUdpBcastFwdAdminStatus_Object = MibScalar
hpicfUdpBcastFwdAdminStatus = _HpicfUdpBcastFwdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 1),
    _HpicfUdpBcastFwdAdminStatus_Type()
)
hpicfUdpBcastFwdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpBcastFwdAdminStatus.setStatus("current")
_HpicfUdpFwdServersTable_Object = MibTable
hpicfUdpFwdServersTable = _HpicfUdpFwdServersTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfUdpFwdServersTable.setStatus("current")
_HpicfUdpFwdServersEntry_Object = MibTableRow
hpicfUdpFwdServersEntry = _HpicfUdpFwdServersEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1)
)
hpicfUdpFwdServersEntry.setIndexNames(
    (0, "HP-ICF-UDP-FORWARD", "hpicfUdpFwdVlanId"),
    (0, "HP-ICF-UDP-FORWARD", "hpicfUdpFwdServerIndex"),
)
if mibBuilder.loadTexts:
    hpicfUdpFwdServersEntry.setStatus("current")
_HpicfUdpFwdVlanId_Type = VlanId
_HpicfUdpFwdVlanId_Object = MibTableColumn
hpicfUdpFwdVlanId = _HpicfUdpFwdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 1),
    _HpicfUdpFwdVlanId_Type()
)
hpicfUdpFwdVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUdpFwdVlanId.setStatus("current")


class _HpicfUdpFwdServerIndex_Type(Integer32):
    """Custom type hpicfUdpFwdServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HpicfUdpFwdServerIndex_Type.__name__ = "Integer32"
_HpicfUdpFwdServerIndex_Object = MibTableColumn
hpicfUdpFwdServerIndex = _HpicfUdpFwdServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 2),
    _HpicfUdpFwdServerIndex_Type()
)
hpicfUdpFwdServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfUdpFwdServerIndex.setStatus("current")
_HpicfUdpFwdServerAddressType_Type = InetAddressType
_HpicfUdpFwdServerAddressType_Object = MibTableColumn
hpicfUdpFwdServerAddressType = _HpicfUdpFwdServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 3),
    _HpicfUdpFwdServerAddressType_Type()
)
hpicfUdpFwdServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpFwdServerAddressType.setStatus("current")


class _HpicfUdpFwdServerAddress_Type(InetAddress):
    """Custom type hpicfUdpFwdServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 36),
    )


_HpicfUdpFwdServerAddress_Type.__name__ = "InetAddress"
_HpicfUdpFwdServerAddress_Object = MibTableColumn
hpicfUdpFwdServerAddress = _HpicfUdpFwdServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 4),
    _HpicfUdpFwdServerAddress_Type()
)
hpicfUdpFwdServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpFwdServerAddress.setStatus("current")
_HpicfUdpFwdPortNumber_Type = InetPortNumber
_HpicfUdpFwdPortNumber_Object = MibTableColumn
hpicfUdpFwdPortNumber = _HpicfUdpFwdPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 5),
    _HpicfUdpFwdPortNumber_Type()
)
hpicfUdpFwdPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpFwdPortNumber.setStatus("current")
_HpicfUdpFwdRowStatus_Type = RowStatus
_HpicfUdpFwdRowStatus_Object = MibTableColumn
hpicfUdpFwdRowStatus = _HpicfUdpFwdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 2, 1, 6),
    _HpicfUdpFwdRowStatus_Type()
)
hpicfUdpFwdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfUdpFwdRowStatus.setStatus("current")
_HpicfUdpFwdDhcpRelayClientDiscards_Type = Counter32
_HpicfUdpFwdDhcpRelayClientDiscards_Object = MibScalar
hpicfUdpFwdDhcpRelayClientDiscards = _HpicfUdpFwdDhcpRelayClientDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 3),
    _HpicfUdpFwdDhcpRelayClientDiscards_Type()
)
hpicfUdpFwdDhcpRelayClientDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayClientDiscards.setStatus("current")
_HpicfUdpFwdDhcpRelayClientForwards_Type = Counter32
_HpicfUdpFwdDhcpRelayClientForwards_Object = MibScalar
hpicfUdpFwdDhcpRelayClientForwards = _HpicfUdpFwdDhcpRelayClientForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 4),
    _HpicfUdpFwdDhcpRelayClientForwards_Type()
)
hpicfUdpFwdDhcpRelayClientForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayClientForwards.setStatus("current")
_HpicfUdpFwdDhcpRelayServerDiscards_Type = Counter32
_HpicfUdpFwdDhcpRelayServerDiscards_Object = MibScalar
hpicfUdpFwdDhcpRelayServerDiscards = _HpicfUdpFwdDhcpRelayServerDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 5),
    _HpicfUdpFwdDhcpRelayServerDiscards_Type()
)
hpicfUdpFwdDhcpRelayServerDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayServerDiscards.setStatus("current")
_HpicfUdpFwdDhcpRelayServerForwards_Type = Counter32
_HpicfUdpFwdDhcpRelayServerForwards_Object = MibScalar
hpicfUdpFwdDhcpRelayServerForwards = _HpicfUdpFwdDhcpRelayServerForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 6),
    _HpicfUdpFwdDhcpRelayServerForwards_Type()
)
hpicfUdpFwdDhcpRelayServerForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayServerForwards.setStatus("current")


class _HpicfUdpFwdDhcpRelayAdminStatus_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayAdminStatus based on Integer32"""
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


_HpicfUdpFwdDhcpRelayAdminStatus_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayAdminStatus_Object = MibScalar
hpicfUdpFwdDhcpRelayAdminStatus = _HpicfUdpFwdDhcpRelayAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 7),
    _HpicfUdpFwdDhcpRelayAdminStatus_Type()
)
hpicfUdpFwdDhcpRelayAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayAdminStatus.setStatus("current")
_HpicfUdpFwdDhcpRelayOption82Objects_ObjectIdentity = ObjectIdentity
hpicfUdpFwdDhcpRelayOption82Objects = _HpicfUdpFwdDhcpRelayOption82Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 8)
)


class _HpicfUdpFwdDhcpRelayOption82AdminStatus_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayOption82AdminStatus based on Integer32"""
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


_HpicfUdpFwdDhcpRelayOption82AdminStatus_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayOption82AdminStatus_Object = MibScalar
hpicfUdpFwdDhcpRelayOption82AdminStatus = _HpicfUdpFwdDhcpRelayOption82AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 8, 1),
    _HpicfUdpFwdDhcpRelayOption82AdminStatus_Type()
)
hpicfUdpFwdDhcpRelayOption82AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayOption82AdminStatus.setStatus("current")


class _HpicfUdpFwdDhcpRelayOption82Policy_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayOption82Policy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 3),
          ("keep", 2),
          ("replace", 1))
    )


_HpicfUdpFwdDhcpRelayOption82Policy_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayOption82Policy_Object = MibScalar
hpicfUdpFwdDhcpRelayOption82Policy = _HpicfUdpFwdDhcpRelayOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 8, 2),
    _HpicfUdpFwdDhcpRelayOption82Policy_Type()
)
hpicfUdpFwdDhcpRelayOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayOption82Policy.setStatus("current")


class _HpicfUdpFwdDhcpRelayOption82ResponseValidate_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayOption82ResponseValidate based on Integer32"""
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


_HpicfUdpFwdDhcpRelayOption82ResponseValidate_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayOption82ResponseValidate_Object = MibScalar
hpicfUdpFwdDhcpRelayOption82ResponseValidate = _HpicfUdpFwdDhcpRelayOption82ResponseValidate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 8, 3),
    _HpicfUdpFwdDhcpRelayOption82ResponseValidate_Type()
)
hpicfUdpFwdDhcpRelayOption82ResponseValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayOption82ResponseValidate.setStatus("current")


class _HpicfUdpFwdDhcpRelayOption82RemoteId_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayOption82RemoteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ip", 2),
          ("mac", 1),
          ("mgmtvlan", 3))
    )


_HpicfUdpFwdDhcpRelayOption82RemoteId_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayOption82RemoteId_Object = MibScalar
hpicfUdpFwdDhcpRelayOption82RemoteId = _HpicfUdpFwdDhcpRelayOption82RemoteId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 8, 4),
    _HpicfUdpFwdDhcpRelayOption82RemoteId_Type()
)
hpicfUdpFwdDhcpRelayOption82RemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayOption82RemoteId.setStatus("current")


class _HpicfUdpFwdDhcpRelayHopCount_Type(Integer32):
    """Custom type hpicfUdpFwdDhcpRelayHopCount based on Integer32"""
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


_HpicfUdpFwdDhcpRelayHopCount_Type.__name__ = "Integer32"
_HpicfUdpFwdDhcpRelayHopCount_Object = MibScalar
hpicfUdpFwdDhcpRelayHopCount = _HpicfUdpFwdDhcpRelayHopCount_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 1, 9),
    _HpicfUdpFwdDhcpRelayHopCount_Type()
)
hpicfUdpFwdDhcpRelayHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayHopCount.setStatus("current")
_HpicfUdpFwdConformance_ObjectIdentity = ObjectIdentity
hpicfUdpFwdConformance = _HpicfUdpFwdConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2)
)
_HpicfUdpFwdCompliances_ObjectIdentity = ObjectIdentity
hpicfUdpFwdCompliances = _HpicfUdpFwdCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 1)
)
_HpicfUdpFwdGroups_ObjectIdentity = ObjectIdentity
hpicfUdpFwdGroups = _HpicfUdpFwdGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 2)
)

# Managed Objects groups

hpicfUdpFwdCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 2, 1)
)
hpicfUdpFwdCfgGroup.setObjects(
    ("HP-ICF-UDP-FORWARD", "hpicfUdpBcastFwdAdminStatus")
)
if mibBuilder.loadTexts:
    hpicfUdpFwdCfgGroup.setStatus("current")

hpicfUdpFwdServerTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 2, 2)
)
hpicfUdpFwdServerTableGroup.setObjects(
      *(("HP-ICF-UDP-FORWARD", "hpicfUdpFwdServerAddressType"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdServerAddress"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdPortNumber"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfUdpFwdServerTableGroup.setStatus("current")

hpicfUdpFwdDhcpRelayStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 2, 3)
)
hpicfUdpFwdDhcpRelayStatsGroup.setObjects(
      *(("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayClientDiscards"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayClientForwards"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayServerDiscards"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayServerForwards"))
)
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayStatsGroup.setStatus("current")

hpicfUdpFwdDhcpRelayCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 2, 4)
)
hpicfUdpFwdDhcpRelayCfgGroup.setObjects(
      *(("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayAdminStatus"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayOption82AdminStatus"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayOption82Policy"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayOption82ResponseValidate"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayOption82RemoteId"),
        ("HP-ICF-UDP-FORWARD", "hpicfUdpFwdDhcpRelayHopCount"))
)
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfUdpFwdCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfUdpFwdCompliance.setStatus(
        "current"
    )

hpicfUdpFwdStatCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfUdpFwdStatCompliance.setStatus(
        "current"
    )

hpicfUdpFwdDhcpRelayCfgCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 23, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfUdpFwdDhcpRelayCfgCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-UDP-FORWARD",
    **{"hpicfUdpFwd": hpicfUdpFwd,
       "hpicfUdpFwdNotification": hpicfUdpFwdNotification,
       "hpicfUdpFwdObjects": hpicfUdpFwdObjects,
       "hpicfUdpBcastFwdAdminStatus": hpicfUdpBcastFwdAdminStatus,
       "hpicfUdpFwdServersTable": hpicfUdpFwdServersTable,
       "hpicfUdpFwdServersEntry": hpicfUdpFwdServersEntry,
       "hpicfUdpFwdVlanId": hpicfUdpFwdVlanId,
       "hpicfUdpFwdServerIndex": hpicfUdpFwdServerIndex,
       "hpicfUdpFwdServerAddressType": hpicfUdpFwdServerAddressType,
       "hpicfUdpFwdServerAddress": hpicfUdpFwdServerAddress,
       "hpicfUdpFwdPortNumber": hpicfUdpFwdPortNumber,
       "hpicfUdpFwdRowStatus": hpicfUdpFwdRowStatus,
       "hpicfUdpFwdDhcpRelayClientDiscards": hpicfUdpFwdDhcpRelayClientDiscards,
       "hpicfUdpFwdDhcpRelayClientForwards": hpicfUdpFwdDhcpRelayClientForwards,
       "hpicfUdpFwdDhcpRelayServerDiscards": hpicfUdpFwdDhcpRelayServerDiscards,
       "hpicfUdpFwdDhcpRelayServerForwards": hpicfUdpFwdDhcpRelayServerForwards,
       "hpicfUdpFwdDhcpRelayAdminStatus": hpicfUdpFwdDhcpRelayAdminStatus,
       "hpicfUdpFwdDhcpRelayOption82Objects": hpicfUdpFwdDhcpRelayOption82Objects,
       "hpicfUdpFwdDhcpRelayOption82AdminStatus": hpicfUdpFwdDhcpRelayOption82AdminStatus,
       "hpicfUdpFwdDhcpRelayOption82Policy": hpicfUdpFwdDhcpRelayOption82Policy,
       "hpicfUdpFwdDhcpRelayOption82ResponseValidate": hpicfUdpFwdDhcpRelayOption82ResponseValidate,
       "hpicfUdpFwdDhcpRelayOption82RemoteId": hpicfUdpFwdDhcpRelayOption82RemoteId,
       "hpicfUdpFwdDhcpRelayHopCount": hpicfUdpFwdDhcpRelayHopCount,
       "hpicfUdpFwdConformance": hpicfUdpFwdConformance,
       "hpicfUdpFwdCompliances": hpicfUdpFwdCompliances,
       "hpicfUdpFwdCompliance": hpicfUdpFwdCompliance,
       "hpicfUdpFwdStatCompliance": hpicfUdpFwdStatCompliance,
       "hpicfUdpFwdDhcpRelayCfgCompliance": hpicfUdpFwdDhcpRelayCfgCompliance,
       "hpicfUdpFwdGroups": hpicfUdpFwdGroups,
       "hpicfUdpFwdCfgGroup": hpicfUdpFwdCfgGroup,
       "hpicfUdpFwdServerTableGroup": hpicfUdpFwdServerTableGroup,
       "hpicfUdpFwdDhcpRelayStatsGroup": hpicfUdpFwdDhcpRelayStatsGroup,
       "hpicfUdpFwdDhcpRelayCfgGroup": hpicfUdpFwdDhcpRelayCfgGroup}
)
