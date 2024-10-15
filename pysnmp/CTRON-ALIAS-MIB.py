# SNMP MIB module (CTRON-ALIAS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-ALIAS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:18:30 2024
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

(ctAliasMib,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctAliasMib")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

cabletronAliasMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1)
)
cabletronAliasMib.setRevisions(
        ("2013-02-15 14:30",
         "2011-02-14 15:25",
         "2003-04-22 13:39",
         "2002-01-30 13:01",
         "2002-01-23 20:56",
         "2002-01-18 20:22",
         "1999-09-26 00:00",
         "1999-09-04 00:00",
         "1999-08-06 00:00",
         "1999-07-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CabletronProtocolTC(Integer32, TextualConvention):
    status = "current"
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("apl", 2),
          ("bgp", 20),
          ("bootpc", 8),
          ("bootps", 7),
          ("bpdu", 24),
          ("dec", 23),
          ("dhcpc", 6),
          ("dhcps", 5),
          ("hsrp", 4),
          ("igrp", 22),
          ("ip", 1),
          ("ipv6", 26),
          ("ipx", 11),
          ("ipx20", 15),
          ("llmnr", 28),
          ("mac", 3),
          ("mdns", 27),
          ("n802q", 19),
          ("nbt", 18),
          ("netBios", 17),
          ("ospf", 9),
          ("rip", 21),
          ("rtmp", 16),
          ("ssdp", 29),
          ("udp", 25),
          ("unknown", 0),
          ("vrrp", 10),
          ("xnlsp", 14),
          ("xrip", 12),
          ("xsap", 13))
    )



class AliasAddress(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x "
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CabletronProtocolBits(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CtAlias_ObjectIdentity = ObjectIdentity
ctAlias = _CtAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1)
)
_CtAliasTable_Object = MibTable
ctAliasTable = _CtAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctAliasTable.setStatus("current")
_CtAliasEntry_Object = MibTableRow
ctAliasEntry = _CtAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1)
)
ctAliasEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasTimeFilter"),
    (0, "CTRON-ALIAS-MIB", "ctAliasReference"),
)
if mibBuilder.loadTexts:
    ctAliasEntry.setStatus("current")
_CtAliasTimeFilter_Type = TimeFilter
_CtAliasTimeFilter_Object = MibTableColumn
ctAliasTimeFilter = _CtAliasTimeFilter_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 1),
    _CtAliasTimeFilter_Type()
)
ctAliasTimeFilter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAliasTimeFilter.setStatus("current")


class _CtAliasReference_Type(Integer32):
    """Custom type ctAliasReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtAliasReference_Type.__name__ = "Integer32"
_CtAliasReference_Object = MibTableColumn
ctAliasReference = _CtAliasReference_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 2),
    _CtAliasReference_Type()
)
ctAliasReference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAliasReference.setStatus("current")
_CtAliasInterface_Type = InterfaceIndex
_CtAliasInterface_Object = MibTableColumn
ctAliasInterface = _CtAliasInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 3),
    _CtAliasInterface_Type()
)
ctAliasInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterface.setStatus("current")
_CtAliasMacAddress_Type = MacAddress
_CtAliasMacAddress_Object = MibTableColumn
ctAliasMacAddress = _CtAliasMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 4),
    _CtAliasMacAddress_Type()
)
ctAliasMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddress.setStatus("current")
_CtAliasVlanID_Type = VlanIndex
_CtAliasVlanID_Object = MibTableColumn
ctAliasVlanID = _CtAliasVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 5),
    _CtAliasVlanID_Type()
)
ctAliasVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasVlanID.setStatus("current")
_CtAliasProtocol_Type = CabletronProtocolTC
_CtAliasProtocol_Object = MibTableColumn
ctAliasProtocol = _CtAliasProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 6),
    _CtAliasProtocol_Type()
)
ctAliasProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocol.setStatus("current")
_CtAliasAddress_Type = AliasAddress
_CtAliasAddress_Object = MibTableColumn
ctAliasAddress = _CtAliasAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 7),
    _CtAliasAddress_Type()
)
ctAliasAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasAddress.setStatus("current")
_CtAliasIsActive_Type = TruthValue
_CtAliasIsActive_Object = MibTableColumn
ctAliasIsActive = _CtAliasIsActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 8),
    _CtAliasIsActive_Type()
)
ctAliasIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasIsActive.setStatus("current")
_CtAliasAddressText_Type = SnmpAdminString
_CtAliasAddressText_Object = MibTableColumn
ctAliasAddressText = _CtAliasAddressText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 1, 1, 9),
    _CtAliasAddressText_Type()
)
ctAliasAddressText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasAddressText.setStatus("current")
_CtAliasControlTable_Object = MibTable
ctAliasControlTable = _CtAliasControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ctAliasControlTable.setStatus("current")
_CtAliasControlEntry_Object = MibTableRow
ctAliasControlEntry = _CtAliasControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 2, 1)
)
ctAliasControlEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasID"),
)
if mibBuilder.loadTexts:
    ctAliasControlEntry.setStatus("current")


class _CtAliasID_Type(Integer32):
    """Custom type ctAliasID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CtAliasID_Type.__name__ = "Integer32"
_CtAliasID_Object = MibTableColumn
ctAliasID = _CtAliasID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 2, 1, 1),
    _CtAliasID_Type()
)
ctAliasID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctAliasID.setStatus("current")
_CtAliasMarkInactive_Type = TruthValue
_CtAliasMarkInactive_Object = MibTableColumn
ctAliasMarkInactive = _CtAliasMarkInactive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 2, 1, 2),
    _CtAliasMarkInactive_Type()
)
ctAliasMarkInactive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasMarkInactive.setStatus("deprecated")


class _CtAliasEntryStatus_Type(Integer32):
    """Custom type ctAliasEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2),
          ("remove", 3))
    )


_CtAliasEntryStatus_Type.__name__ = "Integer32"
_CtAliasEntryStatus_Object = MibTableColumn
ctAliasEntryStatus = _CtAliasEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 2, 1, 3),
    _CtAliasEntryStatus_Type()
)
ctAliasEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasEntryStatus.setStatus("current")
_CtAliasStats_ObjectIdentity = ObjectIdentity
ctAliasStats = _CtAliasStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 3)
)
_CtAliasTableStatsTotalEntries_Type = Gauge32
_CtAliasTableStatsTotalEntries_Object = MibScalar
ctAliasTableStatsTotalEntries = _CtAliasTableStatsTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 3, 1),
    _CtAliasTableStatsTotalEntries_Type()
)
ctAliasTableStatsTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasTableStatsTotalEntries.setStatus("current")
_CtAliasTableStatsActiveEntries_Type = Gauge32
_CtAliasTableStatsActiveEntries_Object = MibScalar
ctAliasTableStatsActiveEntries = _CtAliasTableStatsActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 3, 2),
    _CtAliasTableStatsActiveEntries_Type()
)
ctAliasTableStatsActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasTableStatsActiveEntries.setStatus("current")
_CtAliasTableStatsPurgeTime_Type = TimeTicks
_CtAliasTableStatsPurgeTime_Object = MibScalar
ctAliasTableStatsPurgeTime = _CtAliasTableStatsPurgeTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 3, 3),
    _CtAliasTableStatsPurgeTime_Type()
)
ctAliasTableStatsPurgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasTableStatsPurgeTime.setStatus("current")


class _CtAliasTableStatsState_Type(Integer32):
    """Custom type ctAliasTableStatsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("notStarted", 1),
          ("ready", 2))
    )


_CtAliasTableStatsState_Type.__name__ = "Integer32"
_CtAliasTableStatsState_Object = MibScalar
ctAliasTableStatsState = _CtAliasTableStatsState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 3, 4),
    _CtAliasTableStatsState_Type()
)
ctAliasTableStatsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasTableStatsState.setStatus("current")
_CtAliasConfiguration_ObjectIdentity = ObjectIdentity
ctAliasConfiguration = _CtAliasConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4)
)
_CtAliasConfigurationSystemAllocatedEntries_Type = Gauge32
_CtAliasConfigurationSystemAllocatedEntries_Object = MibScalar
ctAliasConfigurationSystemAllocatedEntries = _CtAliasConfigurationSystemAllocatedEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 1),
    _CtAliasConfigurationSystemAllocatedEntries_Type()
)
ctAliasConfigurationSystemAllocatedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasConfigurationSystemAllocatedEntries.setStatus("current")
_CtAliasConfigurationSystemTotalEntries_Type = Gauge32
_CtAliasConfigurationSystemTotalEntries_Object = MibScalar
ctAliasConfigurationSystemTotalEntries = _CtAliasConfigurationSystemTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 2),
    _CtAliasConfigurationSystemTotalEntries_Type()
)
ctAliasConfigurationSystemTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasConfigurationSystemTotalEntries.setStatus("current")
_CtAliasConfigurationTable_Object = MibTable
ctAliasConfigurationTable = _CtAliasConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3)
)
if mibBuilder.loadTexts:
    ctAliasConfigurationTable.setStatus("current")
_CtAliasConfigurationEntry_Object = MibTableRow
ctAliasConfigurationEntry = _CtAliasConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3, 1)
)
ctAliasConfigurationEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasInterface"),
)
if mibBuilder.loadTexts:
    ctAliasConfigurationEntry.setStatus("current")
_CtAliasConfigurationInterfaceTotalEntries_Type = Gauge32
_CtAliasConfigurationInterfaceTotalEntries_Object = MibTableColumn
ctAliasConfigurationInterfaceTotalEntries = _CtAliasConfigurationInterfaceTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3, 1, 1),
    _CtAliasConfigurationInterfaceTotalEntries_Type()
)
ctAliasConfigurationInterfaceTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasConfigurationInterfaceTotalEntries.setStatus("current")
_CtAliasConfigurationInterfaceMaxEntries_Type = Gauge32
_CtAliasConfigurationInterfaceMaxEntries_Object = MibTableColumn
ctAliasConfigurationInterfaceMaxEntries = _CtAliasConfigurationInterfaceMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3, 1, 2),
    _CtAliasConfigurationInterfaceMaxEntries_Type()
)
ctAliasConfigurationInterfaceMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasConfigurationInterfaceMaxEntries.setStatus("current")


class _CtAliasConfigurationInterfaceEnableState_Type(EnabledStatus):
    """Custom type ctAliasConfigurationInterfaceEnableState based on EnabledStatus"""


_CtAliasConfigurationInterfaceEnableState_Object = MibTableColumn
ctAliasConfigurationInterfaceEnableState = _CtAliasConfigurationInterfaceEnableState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3, 1, 3),
    _CtAliasConfigurationInterfaceEnableState_Type()
)
ctAliasConfigurationInterfaceEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasConfigurationInterfaceEnableState.setStatus("current")
_CtAliasConfigurationNumQueueWraps_Type = Counter32
_CtAliasConfigurationNumQueueWraps_Object = MibTableColumn
ctAliasConfigurationNumQueueWraps = _CtAliasConfigurationNumQueueWraps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 3, 1, 4),
    _CtAliasConfigurationNumQueueWraps_Type()
)
ctAliasConfigurationNumQueueWraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasConfigurationNumQueueWraps.setStatus("current")
_CtAliasConfigurationProtocolEnableState_Type = CabletronProtocolBits
_CtAliasConfigurationProtocolEnableState_Object = MibScalar
ctAliasConfigurationProtocolEnableState = _CtAliasConfigurationProtocolEnableState_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 4, 4),
    _CtAliasConfigurationProtocolEnableState_Type()
)
ctAliasConfigurationProtocolEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasConfigurationProtocolEnableState.setStatus("current")
_CtAliasMacAddressTable_Object = MibTable
ctAliasMacAddressTable = _CtAliasMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ctAliasMacAddressTable.setStatus("current")
_CtAliasMacAddressEntry_Object = MibTableRow
ctAliasMacAddressEntry = _CtAliasMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1)
)
ctAliasMacAddressEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasMacAddress"),
    (0, "CTRON-ALIAS-MIB", "ctAliasProtocol"),
    (0, "CTRON-ALIAS-MIB", "ctAliasAddress"),
    (0, "CTRON-ALIAS-MIB", "ctAliasReference"),
)
if mibBuilder.loadTexts:
    ctAliasMacAddressEntry.setStatus("current")
_CtAliasMacAddressInterface_Type = InterfaceIndex
_CtAliasMacAddressInterface_Object = MibTableColumn
ctAliasMacAddressInterface = _CtAliasMacAddressInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1, 1),
    _CtAliasMacAddressInterface_Type()
)
ctAliasMacAddressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddressInterface.setStatus("current")
_CtAliasMacAddressVlanID_Type = VlanIndex
_CtAliasMacAddressVlanID_Object = MibTableColumn
ctAliasMacAddressVlanID = _CtAliasMacAddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1, 2),
    _CtAliasMacAddressVlanID_Type()
)
ctAliasMacAddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddressVlanID.setStatus("current")
_CtAliasMacAddressIsActive_Type = TruthValue
_CtAliasMacAddressIsActive_Object = MibTableColumn
ctAliasMacAddressIsActive = _CtAliasMacAddressIsActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1, 3),
    _CtAliasMacAddressIsActive_Type()
)
ctAliasMacAddressIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddressIsActive.setStatus("current")
_CtAliasMacAddressAddressText_Type = SnmpAdminString
_CtAliasMacAddressAddressText_Object = MibTableColumn
ctAliasMacAddressAddressText = _CtAliasMacAddressAddressText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1, 4),
    _CtAliasMacAddressAddressText_Type()
)
ctAliasMacAddressAddressText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddressAddressText.setStatus("current")
_CtAliasMacAddressTime_Type = TimeTicks
_CtAliasMacAddressTime_Object = MibTableColumn
ctAliasMacAddressTime = _CtAliasMacAddressTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 5, 1, 5),
    _CtAliasMacAddressTime_Type()
)
ctAliasMacAddressTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasMacAddressTime.setStatus("current")
_CtAliasProtocolAddressTable_Object = MibTable
ctAliasProtocolAddressTable = _CtAliasProtocolAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ctAliasProtocolAddressTable.setStatus("current")
_CtAliasProtocolAddressEntry_Object = MibTableRow
ctAliasProtocolAddressEntry = _CtAliasProtocolAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1)
)
ctAliasProtocolAddressEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasProtocol"),
    (0, "CTRON-ALIAS-MIB", "ctAliasAddress"),
    (0, "CTRON-ALIAS-MIB", "ctAliasMacAddress"),
    (0, "CTRON-ALIAS-MIB", "ctAliasReference"),
)
if mibBuilder.loadTexts:
    ctAliasProtocolAddressEntry.setStatus("current")
_CtAliasProtocolAddressInterface_Type = InterfaceIndex
_CtAliasProtocolAddressInterface_Object = MibTableColumn
ctAliasProtocolAddressInterface = _CtAliasProtocolAddressInterface_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1, 1),
    _CtAliasProtocolAddressInterface_Type()
)
ctAliasProtocolAddressInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocolAddressInterface.setStatus("current")
_CtAliasProtocolAddressVlanID_Type = VlanIndex
_CtAliasProtocolAddressVlanID_Object = MibTableColumn
ctAliasProtocolAddressVlanID = _CtAliasProtocolAddressVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1, 2),
    _CtAliasProtocolAddressVlanID_Type()
)
ctAliasProtocolAddressVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocolAddressVlanID.setStatus("current")
_CtAliasProtocolAddressIsActive_Type = TruthValue
_CtAliasProtocolAddressIsActive_Object = MibTableColumn
ctAliasProtocolAddressIsActive = _CtAliasProtocolAddressIsActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1, 3),
    _CtAliasProtocolAddressIsActive_Type()
)
ctAliasProtocolAddressIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocolAddressIsActive.setStatus("current")
_CtAliasProtocolAddressAddressText_Type = SnmpAdminString
_CtAliasProtocolAddressAddressText_Object = MibTableColumn
ctAliasProtocolAddressAddressText = _CtAliasProtocolAddressAddressText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1, 4),
    _CtAliasProtocolAddressAddressText_Type()
)
ctAliasProtocolAddressAddressText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocolAddressAddressText.setStatus("current")
_CtAliasProtocolAddressTime_Type = TimeTicks
_CtAliasProtocolAddressTime_Object = MibTableColumn
ctAliasProtocolAddressTime = _CtAliasProtocolAddressTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 6, 1, 5),
    _CtAliasProtocolAddressTime_Type()
)
ctAliasProtocolAddressTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasProtocolAddressTime.setStatus("current")
_CtAliasEntryClearAll_Type = TruthValue
_CtAliasEntryClearAll_Object = MibScalar
ctAliasEntryClearAll = _CtAliasEntryClearAll_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 7),
    _CtAliasEntryClearAll_Type()
)
ctAliasEntryClearAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctAliasEntryClearAll.setStatus("current")
_CtAliasInterfaceTable_Object = MibTable
ctAliasInterfaceTable = _CtAliasInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ctAliasInterfaceTable.setStatus("current")
_CtAliasInterfaceEntry_Object = MibTableRow
ctAliasInterfaceEntry = _CtAliasInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1)
)
ctAliasInterfaceEntry.setIndexNames(
    (0, "CTRON-ALIAS-MIB", "ctAliasInterface"),
    (0, "CTRON-ALIAS-MIB", "ctAliasReference"),
)
if mibBuilder.loadTexts:
    ctAliasInterfaceEntry.setStatus("current")
_CtAliasInterfaceMacAddress_Type = MacAddress
_CtAliasInterfaceMacAddress_Object = MibTableColumn
ctAliasInterfaceMacAddress = _CtAliasInterfaceMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 1),
    _CtAliasInterfaceMacAddress_Type()
)
ctAliasInterfaceMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceMacAddress.setStatus("current")
_CtAliasInterfaceProtocol_Type = CabletronProtocolTC
_CtAliasInterfaceProtocol_Object = MibTableColumn
ctAliasInterfaceProtocol = _CtAliasInterfaceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 2),
    _CtAliasInterfaceProtocol_Type()
)
ctAliasInterfaceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceProtocol.setStatus("current")
_CtAliasInterfaceAddress_Type = AliasAddress
_CtAliasInterfaceAddress_Object = MibTableColumn
ctAliasInterfaceAddress = _CtAliasInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 3),
    _CtAliasInterfaceAddress_Type()
)
ctAliasInterfaceAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceAddress.setStatus("current")
_CtAliasInterfaceVlanID_Type = VlanIndex
_CtAliasInterfaceVlanID_Object = MibTableColumn
ctAliasInterfaceVlanID = _CtAliasInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 4),
    _CtAliasInterfaceVlanID_Type()
)
ctAliasInterfaceVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceVlanID.setStatus("current")
_CtAliasInterfaceIsActive_Type = TruthValue
_CtAliasInterfaceIsActive_Object = MibTableColumn
ctAliasInterfaceIsActive = _CtAliasInterfaceIsActive_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 5),
    _CtAliasInterfaceIsActive_Type()
)
ctAliasInterfaceIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceIsActive.setStatus("current")
_CtAliasInterfaceAddressText_Type = SnmpAdminString
_CtAliasInterfaceAddressText_Object = MibTableColumn
ctAliasInterfaceAddressText = _CtAliasInterfaceAddressText_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 6),
    _CtAliasInterfaceAddressText_Type()
)
ctAliasInterfaceAddressText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceAddressText.setStatus("current")
_CtAliasInterfaceTime_Type = TimeTicks
_CtAliasInterfaceTime_Object = MibTableColumn
ctAliasInterfaceTime = _CtAliasInterfaceTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 1, 1, 8, 1, 7),
    _CtAliasInterfaceTime_Type()
)
ctAliasInterfaceTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctAliasInterfaceTime.setStatus("current")
_CtAliasConformance_ObjectIdentity = ObjectIdentity
ctAliasConformance = _CtAliasConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2)
)
_CtAliasGroups_ObjectIdentity = ObjectIdentity
ctAliasGroups = _CtAliasGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1)
)
_CtAliasCompliances_ObjectIdentity = ObjectIdentity
ctAliasCompliances = _CtAliasCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 2)
)

# Managed Objects groups

ctAliasBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 1)
)
ctAliasBasicGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasInterface"),
        ("CTRON-ALIAS-MIB", "ctAliasMacAddress"),
        ("CTRON-ALIAS-MIB", "ctAliasVlanID"),
        ("CTRON-ALIAS-MIB", "ctAliasProtocol"),
        ("CTRON-ALIAS-MIB", "ctAliasAddress"),
        ("CTRON-ALIAS-MIB", "ctAliasIsActive"),
        ("CTRON-ALIAS-MIB", "ctAliasAddressText"))
)
if mibBuilder.loadTexts:
    ctAliasBasicGroup.setStatus("current")

ctAliasStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 2)
)
ctAliasStatsGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasTableStatsTotalEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasTableStatsActiveEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasTableStatsPurgeTime"),
        ("CTRON-ALIAS-MIB", "ctAliasTableStatsState"))
)
if mibBuilder.loadTexts:
    ctAliasStatsGroup.setStatus("current")

ctAliasControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 3)
)
ctAliasControlGroup.setObjects(
    ("CTRON-ALIAS-MIB", "ctAliasMarkInactive")
)
if mibBuilder.loadTexts:
    ctAliasControlGroup.setStatus("deprecated")

ctAliasConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 4)
)
ctAliasConfigurationGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasConfigurationSystemAllocatedEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationSystemTotalEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceTotalEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceMaxEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceEnableState"))
)
if mibBuilder.loadTexts:
    ctAliasConfigurationGroup.setStatus("deprecated")

ctAliasMacAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 5)
)
ctAliasMacAddressGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasMacAddressInterface"),
        ("CTRON-ALIAS-MIB", "ctAliasMacAddressVlanID"),
        ("CTRON-ALIAS-MIB", "ctAliasMacAddressIsActive"),
        ("CTRON-ALIAS-MIB", "ctAliasMacAddressAddressText"),
        ("CTRON-ALIAS-MIB", "ctAliasMacAddressTime"))
)
if mibBuilder.loadTexts:
    ctAliasMacAddressGroup.setStatus("current")

ctAliasProtocolAddressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 6)
)
ctAliasProtocolAddressGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasProtocolAddressInterface"),
        ("CTRON-ALIAS-MIB", "ctAliasProtocolAddressVlanID"),
        ("CTRON-ALIAS-MIB", "ctAliasProtocolAddressIsActive"),
        ("CTRON-ALIAS-MIB", "ctAliasProtocolAddressAddressText"),
        ("CTRON-ALIAS-MIB", "ctAliasProtocolAddressTime"))
)
if mibBuilder.loadTexts:
    ctAliasProtocolAddressGroup.setStatus("current")

ctAliasControlGroupI = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 7)
)
ctAliasControlGroupI.setObjects(
    ("CTRON-ALIAS-MIB", "ctAliasEntryStatus")
)
if mibBuilder.loadTexts:
    ctAliasControlGroupI.setStatus("current")

ctAliasGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 8)
)
ctAliasGroup.setObjects(
    ("CTRON-ALIAS-MIB", "ctAliasEntryClearAll")
)
if mibBuilder.loadTexts:
    ctAliasGroup.setStatus("current")

ctAliasConfigurationGroupI = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 9)
)
ctAliasConfigurationGroupI.setObjects(
    ("CTRON-ALIAS-MIB", "ctAliasConfigurationNumQueueWraps")
)
if mibBuilder.loadTexts:
    ctAliasConfigurationGroupI.setStatus("current")

ctAliasConfigurationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 10)
)
ctAliasConfigurationGroup2.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasConfigurationSystemAllocatedEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationSystemTotalEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceTotalEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceMaxEntries"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationInterfaceEnableState"),
        ("CTRON-ALIAS-MIB", "ctAliasConfigurationProtocolEnableState"))
)
if mibBuilder.loadTexts:
    ctAliasConfigurationGroup2.setStatus("current")

ctAliasInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 1, 11)
)
ctAliasInterfaceGroup.setObjects(
      *(("CTRON-ALIAS-MIB", "ctAliasInterfaceMacAddress"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceProtocol"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceAddress"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceVlanID"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceIsActive"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceAddressText"),
        ("CTRON-ALIAS-MIB", "ctAliasInterfaceTime"))
)
if mibBuilder.loadTexts:
    ctAliasInterfaceGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctAliasCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctAliasCompliance.setStatus(
        "current"
    )

ctAliasCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ctAliasCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-ALIAS-MIB",
    **{"CabletronProtocolTC": CabletronProtocolTC,
       "AliasAddress": AliasAddress,
       "CabletronProtocolBits": CabletronProtocolBits,
       "cabletronAliasMib": cabletronAliasMib,
       "ctAlias": ctAlias,
       "ctAliasTable": ctAliasTable,
       "ctAliasEntry": ctAliasEntry,
       "ctAliasTimeFilter": ctAliasTimeFilter,
       "ctAliasReference": ctAliasReference,
       "ctAliasInterface": ctAliasInterface,
       "ctAliasMacAddress": ctAliasMacAddress,
       "ctAliasVlanID": ctAliasVlanID,
       "ctAliasProtocol": ctAliasProtocol,
       "ctAliasAddress": ctAliasAddress,
       "ctAliasIsActive": ctAliasIsActive,
       "ctAliasAddressText": ctAliasAddressText,
       "ctAliasControlTable": ctAliasControlTable,
       "ctAliasControlEntry": ctAliasControlEntry,
       "ctAliasID": ctAliasID,
       "ctAliasMarkInactive": ctAliasMarkInactive,
       "ctAliasEntryStatus": ctAliasEntryStatus,
       "ctAliasStats": ctAliasStats,
       "ctAliasTableStatsTotalEntries": ctAliasTableStatsTotalEntries,
       "ctAliasTableStatsActiveEntries": ctAliasTableStatsActiveEntries,
       "ctAliasTableStatsPurgeTime": ctAliasTableStatsPurgeTime,
       "ctAliasTableStatsState": ctAliasTableStatsState,
       "ctAliasConfiguration": ctAliasConfiguration,
       "ctAliasConfigurationSystemAllocatedEntries": ctAliasConfigurationSystemAllocatedEntries,
       "ctAliasConfigurationSystemTotalEntries": ctAliasConfigurationSystemTotalEntries,
       "ctAliasConfigurationTable": ctAliasConfigurationTable,
       "ctAliasConfigurationEntry": ctAliasConfigurationEntry,
       "ctAliasConfigurationInterfaceTotalEntries": ctAliasConfigurationInterfaceTotalEntries,
       "ctAliasConfigurationInterfaceMaxEntries": ctAliasConfigurationInterfaceMaxEntries,
       "ctAliasConfigurationInterfaceEnableState": ctAliasConfigurationInterfaceEnableState,
       "ctAliasConfigurationNumQueueWraps": ctAliasConfigurationNumQueueWraps,
       "ctAliasConfigurationProtocolEnableState": ctAliasConfigurationProtocolEnableState,
       "ctAliasMacAddressTable": ctAliasMacAddressTable,
       "ctAliasMacAddressEntry": ctAliasMacAddressEntry,
       "ctAliasMacAddressInterface": ctAliasMacAddressInterface,
       "ctAliasMacAddressVlanID": ctAliasMacAddressVlanID,
       "ctAliasMacAddressIsActive": ctAliasMacAddressIsActive,
       "ctAliasMacAddressAddressText": ctAliasMacAddressAddressText,
       "ctAliasMacAddressTime": ctAliasMacAddressTime,
       "ctAliasProtocolAddressTable": ctAliasProtocolAddressTable,
       "ctAliasProtocolAddressEntry": ctAliasProtocolAddressEntry,
       "ctAliasProtocolAddressInterface": ctAliasProtocolAddressInterface,
       "ctAliasProtocolAddressVlanID": ctAliasProtocolAddressVlanID,
       "ctAliasProtocolAddressIsActive": ctAliasProtocolAddressIsActive,
       "ctAliasProtocolAddressAddressText": ctAliasProtocolAddressAddressText,
       "ctAliasProtocolAddressTime": ctAliasProtocolAddressTime,
       "ctAliasEntryClearAll": ctAliasEntryClearAll,
       "ctAliasInterfaceTable": ctAliasInterfaceTable,
       "ctAliasInterfaceEntry": ctAliasInterfaceEntry,
       "ctAliasInterfaceMacAddress": ctAliasInterfaceMacAddress,
       "ctAliasInterfaceProtocol": ctAliasInterfaceProtocol,
       "ctAliasInterfaceAddress": ctAliasInterfaceAddress,
       "ctAliasInterfaceVlanID": ctAliasInterfaceVlanID,
       "ctAliasInterfaceIsActive": ctAliasInterfaceIsActive,
       "ctAliasInterfaceAddressText": ctAliasInterfaceAddressText,
       "ctAliasInterfaceTime": ctAliasInterfaceTime,
       "ctAliasConformance": ctAliasConformance,
       "ctAliasGroups": ctAliasGroups,
       "ctAliasBasicGroup": ctAliasBasicGroup,
       "ctAliasStatsGroup": ctAliasStatsGroup,
       "ctAliasControlGroup": ctAliasControlGroup,
       "ctAliasConfigurationGroup": ctAliasConfigurationGroup,
       "ctAliasMacAddressGroup": ctAliasMacAddressGroup,
       "ctAliasProtocolAddressGroup": ctAliasProtocolAddressGroup,
       "ctAliasControlGroupI": ctAliasControlGroupI,
       "ctAliasGroup": ctAliasGroup,
       "ctAliasConfigurationGroupI": ctAliasConfigurationGroupI,
       "ctAliasConfigurationGroup2": ctAliasConfigurationGroup2,
       "ctAliasInterfaceGroup": ctAliasInterfaceGroup,
       "ctAliasCompliances": ctAliasCompliances,
       "ctAliasCompliance": ctAliasCompliance,
       "ctAliasCompliance2": ctAliasCompliance2}
)
