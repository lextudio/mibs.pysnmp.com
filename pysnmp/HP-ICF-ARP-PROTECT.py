# SNMP MIB module (HP-ICF-ARP-PROTECT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-ARP-PROTECT
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:04 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfArpProtect = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37)
)
hpicfArpProtect.setRevisions(
        ("2007-08-29 00:00",
         "2006-05-03 00:27")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfArpProtectNotifications_ObjectIdentity = ObjectIdentity
hpicfArpProtectNotifications = _HpicfArpProtectNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 0)
)
_HpicfArpProtectObjects_ObjectIdentity = ObjectIdentity
hpicfArpProtectObjects = _HpicfArpProtectObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1)
)
_HpicfArpProtectConfig_ObjectIdentity = ObjectIdentity
hpicfArpProtectConfig = _HpicfArpProtectConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1)
)
_HpicfArpProtectGlobalCfg_ObjectIdentity = ObjectIdentity
hpicfArpProtectGlobalCfg = _HpicfArpProtectGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 1)
)
_HpicfArpProtectEnable_Type = TruthValue
_HpicfArpProtectEnable_Object = MibScalar
hpicfArpProtectEnable = _HpicfArpProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 1, 1),
    _HpicfArpProtectEnable_Type()
)
hpicfArpProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpProtectEnable.setStatus("current")


class _HpicfArpProtectVlanEnable_Type(OctetString):
    """Custom type hpicfArpProtectVlanEnable based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )


_HpicfArpProtectVlanEnable_Type.__name__ = "OctetString"
_HpicfArpProtectVlanEnable_Object = MibScalar
hpicfArpProtectVlanEnable = _HpicfArpProtectVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 1, 2),
    _HpicfArpProtectVlanEnable_Type()
)
hpicfArpProtectVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanEnable.setStatus("current")


class _HpicfArpProtectValidation_Type(Bits):
    """Custom type hpicfArpProtectValidation based on Bits"""
    namedValues = NamedValues(
        *(("dstMac", 1),
          ("ip", 2),
          ("srcMac", 0))
    )

_HpicfArpProtectValidation_Type.__name__ = "Bits"
_HpicfArpProtectValidation_Object = MibScalar
hpicfArpProtectValidation = _HpicfArpProtectValidation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 1, 3),
    _HpicfArpProtectValidation_Type()
)
hpicfArpProtectValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpProtectValidation.setStatus("current")


class _HpicfArpProtectErrantNotifyEnable_Type(Integer32):
    """Custom type hpicfArpProtectErrantNotifyEnable based on Integer32"""
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


_HpicfArpProtectErrantNotifyEnable_Type.__name__ = "Integer32"
_HpicfArpProtectErrantNotifyEnable_Object = MibScalar
hpicfArpProtectErrantNotifyEnable = _HpicfArpProtectErrantNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 1, 4),
    _HpicfArpProtectErrantNotifyEnable_Type()
)
hpicfArpProtectErrantNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantNotifyEnable.setStatus("current")
_HpicfArpProtectPortTable_Object = MibTable
hpicfArpProtectPortTable = _HpicfArpProtectPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfArpProtectPortTable.setStatus("current")
_HpicfArpProtectPortEntry_Object = MibTableRow
hpicfArpProtectPortEntry = _HpicfArpProtectPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 2, 1)
)
hpicfArpProtectPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfArpProtectPortEntry.setStatus("current")
_HpicfArpProtectPortTrust_Type = TruthValue
_HpicfArpProtectPortTrust_Object = MibTableColumn
hpicfArpProtectPortTrust = _HpicfArpProtectPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 1, 2, 1, 1),
    _HpicfArpProtectPortTrust_Type()
)
hpicfArpProtectPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfArpProtectPortTrust.setStatus("current")
_HpicfArpProtectStatus_ObjectIdentity = ObjectIdentity
hpicfArpProtectStatus = _HpicfArpProtectStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2)
)
_HpicfArpProtectVlanStatTable_Object = MibTable
hpicfArpProtectVlanStatTable = _HpicfArpProtectVlanStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatTable.setStatus("current")
_HpicfArpProtectVlanStatEntry_Object = MibTableRow
hpicfArpProtectVlanStatEntry = _HpicfArpProtectVlanStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1)
)
hpicfArpProtectVlanStatEntry.setIndexNames(
    (0, "HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatIndex"),
)
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatEntry.setStatus("current")
_HpicfArpProtectVlanStatIndex_Type = VlanIndex
_HpicfArpProtectVlanStatIndex_Object = MibTableColumn
hpicfArpProtectVlanStatIndex = _HpicfArpProtectVlanStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 1),
    _HpicfArpProtectVlanStatIndex_Type()
)
hpicfArpProtectVlanStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatIndex.setStatus("current")
_HpicfArpProtectVlanStatForwards_Type = Counter32
_HpicfArpProtectVlanStatForwards_Object = MibTableColumn
hpicfArpProtectVlanStatForwards = _HpicfArpProtectVlanStatForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 2),
    _HpicfArpProtectVlanStatForwards_Type()
)
hpicfArpProtectVlanStatForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatForwards.setStatus("current")
_HpicfArpProtectVlanStatBadPkts_Type = Counter32
_HpicfArpProtectVlanStatBadPkts_Object = MibTableColumn
hpicfArpProtectVlanStatBadPkts = _HpicfArpProtectVlanStatBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 3),
    _HpicfArpProtectVlanStatBadPkts_Type()
)
hpicfArpProtectVlanStatBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatBadPkts.setStatus("current")
_HpicfArpProtectVlanStatBadBindings_Type = Counter32
_HpicfArpProtectVlanStatBadBindings_Object = MibTableColumn
hpicfArpProtectVlanStatBadBindings = _HpicfArpProtectVlanStatBadBindings_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 4),
    _HpicfArpProtectVlanStatBadBindings_Type()
)
hpicfArpProtectVlanStatBadBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatBadBindings.setStatus("current")
_HpicfArpProtectVlanStatBadSrcMacs_Type = Counter32
_HpicfArpProtectVlanStatBadSrcMacs_Object = MibTableColumn
hpicfArpProtectVlanStatBadSrcMacs = _HpicfArpProtectVlanStatBadSrcMacs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 5),
    _HpicfArpProtectVlanStatBadSrcMacs_Type()
)
hpicfArpProtectVlanStatBadSrcMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatBadSrcMacs.setStatus("current")
_HpicfArpProtectVlanStatBadDstMacs_Type = Counter32
_HpicfArpProtectVlanStatBadDstMacs_Object = MibTableColumn
hpicfArpProtectVlanStatBadDstMacs = _HpicfArpProtectVlanStatBadDstMacs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 6),
    _HpicfArpProtectVlanStatBadDstMacs_Type()
)
hpicfArpProtectVlanStatBadDstMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatBadDstMacs.setStatus("current")
_HpicfArpProtectVlanStatBadIpAddrs_Type = Counter32
_HpicfArpProtectVlanStatBadIpAddrs_Object = MibTableColumn
hpicfArpProtectVlanStatBadIpAddrs = _HpicfArpProtectVlanStatBadIpAddrs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 2, 1, 1, 7),
    _HpicfArpProtectVlanStatBadIpAddrs_Type()
)
hpicfArpProtectVlanStatBadIpAddrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfArpProtectVlanStatBadIpAddrs.setStatus("current")
_HpicfArpProtectErrantCnt_Type = Counter32
_HpicfArpProtectErrantCnt_Object = MibScalar
hpicfArpProtectErrantCnt = _HpicfArpProtectErrantCnt_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 3),
    _HpicfArpProtectErrantCnt_Type()
)
hpicfArpProtectErrantCnt.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantCnt.setStatus("current")
_HpicfArpProtectErrantSrcMac_Type = MacAddress
_HpicfArpProtectErrantSrcMac_Object = MibScalar
hpicfArpProtectErrantSrcMac = _HpicfArpProtectErrantSrcMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 4),
    _HpicfArpProtectErrantSrcMac_Type()
)
hpicfArpProtectErrantSrcMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantSrcMac.setStatus("current")
_HpicfArpProtectErrantSrcIpType_Type = InetAddressType
_HpicfArpProtectErrantSrcIpType_Object = MibScalar
hpicfArpProtectErrantSrcIpType = _HpicfArpProtectErrantSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 5),
    _HpicfArpProtectErrantSrcIpType_Type()
)
hpicfArpProtectErrantSrcIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantSrcIpType.setStatus("current")
_HpicfArpProtectErrantSrcIp_Type = InetAddress
_HpicfArpProtectErrantSrcIp_Object = MibScalar
hpicfArpProtectErrantSrcIp = _HpicfArpProtectErrantSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 6),
    _HpicfArpProtectErrantSrcIp_Type()
)
hpicfArpProtectErrantSrcIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantSrcIp.setStatus("current")
_HpicfArpProtectErrantDestMac_Type = MacAddress
_HpicfArpProtectErrantDestMac_Object = MibScalar
hpicfArpProtectErrantDestMac = _HpicfArpProtectErrantDestMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 7),
    _HpicfArpProtectErrantDestMac_Type()
)
hpicfArpProtectErrantDestMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantDestMac.setStatus("current")
_HpicfArpProtectErrantDestIpType_Type = InetAddressType
_HpicfArpProtectErrantDestIpType_Object = MibScalar
hpicfArpProtectErrantDestIpType = _HpicfArpProtectErrantDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 8),
    _HpicfArpProtectErrantDestIpType_Type()
)
hpicfArpProtectErrantDestIpType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantDestIpType.setStatus("current")
_HpicfArpProtectErrantDestIp_Type = InetAddress
_HpicfArpProtectErrantDestIp_Object = MibScalar
hpicfArpProtectErrantDestIp = _HpicfArpProtectErrantDestIp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 1, 9),
    _HpicfArpProtectErrantDestIp_Type()
)
hpicfArpProtectErrantDestIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hpicfArpProtectErrantDestIp.setStatus("current")
_HpicfArpProtectConformance_ObjectIdentity = ObjectIdentity
hpicfArpProtectConformance = _HpicfArpProtectConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2)
)
_HpicfArpProtectGroups_ObjectIdentity = ObjectIdentity
hpicfArpProtectGroups = _HpicfArpProtectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2, 1)
)
_HpicfArpProtectCompliances_ObjectIdentity = ObjectIdentity
hpicfArpProtectCompliances = _HpicfArpProtectCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2, 2)
)

# Managed Objects groups

hpicfArpProtectBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2, 1, 1)
)
hpicfArpProtectBaseGroup.setObjects(
      *(("HP-ICF-ARP-PROTECT", "hpicfArpProtectEnable"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanEnable"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectValidation"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectPortTrust"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatForwards"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatBadPkts"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatBadBindings"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatBadSrcMacs"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatBadDstMacs"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectVlanStatBadIpAddrs"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcMac"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcIp"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestMac"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcIpType"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestIpType"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestIp"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantCnt"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantNotifyEnable"))
)
if mibBuilder.loadTexts:
    hpicfArpProtectBaseGroup.setStatus("current")


# Notification objects

hpicfArpProtectErrantReply = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 0, 1)
)
hpicfArpProtectErrantReply.setObjects(
      *(("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantCnt"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcMac"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcIpType"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantSrcIp"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestMac"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestIpType"),
        ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantDestIp"))
)
if mibBuilder.loadTexts:
    hpicfArpProtectErrantReply.setStatus(
        "current"
    )


# Notifications groups

hpicfArpProtectionNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2, 1, 2)
)
hpicfArpProtectionNotifications.setObjects(
    ("HP-ICF-ARP-PROTECT", "hpicfArpProtectErrantReply")
)
if mibBuilder.loadTexts:
    hpicfArpProtectionNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfArpProtectCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 37, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfArpProtectCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-ARP-PROTECT",
    **{"hpicfArpProtect": hpicfArpProtect,
       "hpicfArpProtectNotifications": hpicfArpProtectNotifications,
       "hpicfArpProtectErrantReply": hpicfArpProtectErrantReply,
       "hpicfArpProtectObjects": hpicfArpProtectObjects,
       "hpicfArpProtectConfig": hpicfArpProtectConfig,
       "hpicfArpProtectGlobalCfg": hpicfArpProtectGlobalCfg,
       "hpicfArpProtectEnable": hpicfArpProtectEnable,
       "hpicfArpProtectVlanEnable": hpicfArpProtectVlanEnable,
       "hpicfArpProtectValidation": hpicfArpProtectValidation,
       "hpicfArpProtectErrantNotifyEnable": hpicfArpProtectErrantNotifyEnable,
       "hpicfArpProtectPortTable": hpicfArpProtectPortTable,
       "hpicfArpProtectPortEntry": hpicfArpProtectPortEntry,
       "hpicfArpProtectPortTrust": hpicfArpProtectPortTrust,
       "hpicfArpProtectStatus": hpicfArpProtectStatus,
       "hpicfArpProtectVlanStatTable": hpicfArpProtectVlanStatTable,
       "hpicfArpProtectVlanStatEntry": hpicfArpProtectVlanStatEntry,
       "hpicfArpProtectVlanStatIndex": hpicfArpProtectVlanStatIndex,
       "hpicfArpProtectVlanStatForwards": hpicfArpProtectVlanStatForwards,
       "hpicfArpProtectVlanStatBadPkts": hpicfArpProtectVlanStatBadPkts,
       "hpicfArpProtectVlanStatBadBindings": hpicfArpProtectVlanStatBadBindings,
       "hpicfArpProtectVlanStatBadSrcMacs": hpicfArpProtectVlanStatBadSrcMacs,
       "hpicfArpProtectVlanStatBadDstMacs": hpicfArpProtectVlanStatBadDstMacs,
       "hpicfArpProtectVlanStatBadIpAddrs": hpicfArpProtectVlanStatBadIpAddrs,
       "hpicfArpProtectErrantCnt": hpicfArpProtectErrantCnt,
       "hpicfArpProtectErrantSrcMac": hpicfArpProtectErrantSrcMac,
       "hpicfArpProtectErrantSrcIpType": hpicfArpProtectErrantSrcIpType,
       "hpicfArpProtectErrantSrcIp": hpicfArpProtectErrantSrcIp,
       "hpicfArpProtectErrantDestMac": hpicfArpProtectErrantDestMac,
       "hpicfArpProtectErrantDestIpType": hpicfArpProtectErrantDestIpType,
       "hpicfArpProtectErrantDestIp": hpicfArpProtectErrantDestIp,
       "hpicfArpProtectConformance": hpicfArpProtectConformance,
       "hpicfArpProtectGroups": hpicfArpProtectGroups,
       "hpicfArpProtectBaseGroup": hpicfArpProtectBaseGroup,
       "hpicfArpProtectionNotifications": hpicfArpProtectionNotifications,
       "hpicfArpProtectCompliances": hpicfArpProtectCompliances,
       "hpicfArpProtectCompliance": hpicfArpProtectCompliance}
)
