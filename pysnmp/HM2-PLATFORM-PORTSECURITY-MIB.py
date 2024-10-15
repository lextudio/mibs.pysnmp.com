# SNMP MIB module (HM2-PLATFORM-PORTSECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-PORTSECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:18 2024
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

(HmEnabledStatus,
 hm2PlatformMibs) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "HmEnabledStatus",
    "hm2PlatformMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

hm2PlatformPortSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 20)
)
hm2PlatformPortSecurity.setRevisions(
        ("2011-07-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentPortSecurityGroup_ObjectIdentity = ObjectIdentity
hm2AgentPortSecurityGroup = _Hm2AgentPortSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1)
)


class _Hm2AgentGlobalPortSecurityMode_Type(HmEnabledStatus):
    """Custom type hm2AgentGlobalPortSecurityMode based on HmEnabledStatus"""


_Hm2AgentGlobalPortSecurityMode_Object = MibScalar
hm2AgentGlobalPortSecurityMode = _Hm2AgentGlobalPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 1),
    _Hm2AgentGlobalPortSecurityMode_Type()
)
hm2AgentGlobalPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentGlobalPortSecurityMode.setStatus("current")
_Hm2AgentPortSecurityTable_Object = MibTable
hm2AgentPortSecurityTable = _Hm2AgentPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2)
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityTable.setStatus("current")
_Hm2AgentPortSecurityEntry_Object = MibTableRow
hm2AgentPortSecurityEntry = _Hm2AgentPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1)
)
hm2AgentPortSecurityEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityEntry.setStatus("current")


class _Hm2AgentPortSecurityMode_Type(HmEnabledStatus):
    """Custom type hm2AgentPortSecurityMode based on HmEnabledStatus"""


_Hm2AgentPortSecurityMode_Object = MibTableColumn
hm2AgentPortSecurityMode = _Hm2AgentPortSecurityMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 1),
    _Hm2AgentPortSecurityMode_Type()
)
hm2AgentPortSecurityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityMode.setStatus("current")


class _Hm2AgentPortSecurityDynamicLimit_Type(Unsigned32):
    """Custom type hm2AgentPortSecurityDynamicLimit based on Unsigned32"""
    defaultValue = 600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_Hm2AgentPortSecurityDynamicLimit_Type.__name__ = "Unsigned32"
_Hm2AgentPortSecurityDynamicLimit_Object = MibTableColumn
hm2AgentPortSecurityDynamicLimit = _Hm2AgentPortSecurityDynamicLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 2),
    _Hm2AgentPortSecurityDynamicLimit_Type()
)
hm2AgentPortSecurityDynamicLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicLimit.setStatus("current")


class _Hm2AgentPortSecurityStaticLimit_Type(Unsigned32):
    """Custom type hm2AgentPortSecurityStaticLimit based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hm2AgentPortSecurityStaticLimit_Type.__name__ = "Unsigned32"
_Hm2AgentPortSecurityStaticLimit_Object = MibTableColumn
hm2AgentPortSecurityStaticLimit = _Hm2AgentPortSecurityStaticLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 3),
    _Hm2AgentPortSecurityStaticLimit_Type()
)
hm2AgentPortSecurityStaticLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticLimit.setStatus("current")


class _Hm2AgentPortSecurityViolationTrapMode_Type(HmEnabledStatus):
    """Custom type hm2AgentPortSecurityViolationTrapMode based on HmEnabledStatus"""


_Hm2AgentPortSecurityViolationTrapMode_Object = MibTableColumn
hm2AgentPortSecurityViolationTrapMode = _Hm2AgentPortSecurityViolationTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 4),
    _Hm2AgentPortSecurityViolationTrapMode_Type()
)
hm2AgentPortSecurityViolationTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityViolationTrapMode.setStatus("current")


class _Hm2AgentPortSecurityStaticMACs_Type(DisplayString):
    """Custom type hm2AgentPortSecurityStaticMACs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1536),
    )


_Hm2AgentPortSecurityStaticMACs_Type.__name__ = "DisplayString"
_Hm2AgentPortSecurityStaticMACs_Object = MibTableColumn
hm2AgentPortSecurityStaticMACs = _Hm2AgentPortSecurityStaticMACs_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 6),
    _Hm2AgentPortSecurityStaticMACs_Type()
)
hm2AgentPortSecurityStaticMACs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticMACs.setStatus("current")
_Hm2AgentPortSecurityLastDiscardedMAC_Type = DisplayString
_Hm2AgentPortSecurityLastDiscardedMAC_Object = MibTableColumn
hm2AgentPortSecurityLastDiscardedMAC = _Hm2AgentPortSecurityLastDiscardedMAC_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 7),
    _Hm2AgentPortSecurityLastDiscardedMAC_Type()
)
hm2AgentPortSecurityLastDiscardedMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityLastDiscardedMAC.setStatus("current")
_Hm2AgentPortSecurityMACAddressAdd_Type = DisplayString
_Hm2AgentPortSecurityMACAddressAdd_Object = MibTableColumn
hm2AgentPortSecurityMACAddressAdd = _Hm2AgentPortSecurityMACAddressAdd_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 8),
    _Hm2AgentPortSecurityMACAddressAdd_Type()
)
hm2AgentPortSecurityMACAddressAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityMACAddressAdd.setStatus("current")
_Hm2AgentPortSecurityMACAddressRemove_Type = DisplayString
_Hm2AgentPortSecurityMACAddressRemove_Object = MibTableColumn
hm2AgentPortSecurityMACAddressRemove = _Hm2AgentPortSecurityMACAddressRemove_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 9),
    _Hm2AgentPortSecurityMACAddressRemove_Type()
)
hm2AgentPortSecurityMACAddressRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityMACAddressRemove.setStatus("current")
_Hm2AgentPortSecurityMACAddressMove_Type = HmEnabledStatus
_Hm2AgentPortSecurityMACAddressMove_Object = MibTableColumn
hm2AgentPortSecurityMACAddressMove = _Hm2AgentPortSecurityMACAddressMove_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 10),
    _Hm2AgentPortSecurityMACAddressMove_Type()
)
hm2AgentPortSecurityMACAddressMove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityMACAddressMove.setStatus("current")
_Hm2AgentPortSecurityDynamicCount_Type = Unsigned32
_Hm2AgentPortSecurityDynamicCount_Object = MibTableColumn
hm2AgentPortSecurityDynamicCount = _Hm2AgentPortSecurityDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 20),
    _Hm2AgentPortSecurityDynamicCount_Type()
)
hm2AgentPortSecurityDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicCount.setStatus("current")
_Hm2AgentPortSecurityStaticCount_Type = Unsigned32
_Hm2AgentPortSecurityStaticCount_Object = MibTableColumn
hm2AgentPortSecurityStaticCount = _Hm2AgentPortSecurityStaticCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 21),
    _Hm2AgentPortSecurityStaticCount_Type()
)
hm2AgentPortSecurityStaticCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticCount.setStatus("current")
_Hm2AgentPortSecurityViolationTrapCount_Type = Unsigned32
_Hm2AgentPortSecurityViolationTrapCount_Object = MibTableColumn
hm2AgentPortSecurityViolationTrapCount = _Hm2AgentPortSecurityViolationTrapCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 22),
    _Hm2AgentPortSecurityViolationTrapCount_Type()
)
hm2AgentPortSecurityViolationTrapCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityViolationTrapCount.setStatus("current")


class _Hm2AgentPortSecurityViolationTrapFrequency_Type(Unsigned32):
    """Custom type hm2AgentPortSecurityViolationTrapFrequency based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_Hm2AgentPortSecurityViolationTrapFrequency_Type.__name__ = "Unsigned32"
_Hm2AgentPortSecurityViolationTrapFrequency_Object = MibTableColumn
hm2AgentPortSecurityViolationTrapFrequency = _Hm2AgentPortSecurityViolationTrapFrequency_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 23),
    _Hm2AgentPortSecurityViolationTrapFrequency_Type()
)
hm2AgentPortSecurityViolationTrapFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityViolationTrapFrequency.setStatus("current")


class _Hm2AgentPortSecurityAutoDisable_Type(TruthValue):
    """Custom type hm2AgentPortSecurityAutoDisable based on TruthValue"""


_Hm2AgentPortSecurityAutoDisable_Object = MibTableColumn
hm2AgentPortSecurityAutoDisable = _Hm2AgentPortSecurityAutoDisable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 2, 1, 248),
    _Hm2AgentPortSecurityAutoDisable_Type()
)
hm2AgentPortSecurityAutoDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityAutoDisable.setStatus("current")
_Hm2AgentPortSecurityDynamicTable_Object = MibTable
hm2AgentPortSecurityDynamicTable = _Hm2AgentPortSecurityDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3)
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicTable.setStatus("current")
_Hm2AgentPortSecurityDynamicEntry_Object = MibTableRow
hm2AgentPortSecurityDynamicEntry = _Hm2AgentPortSecurityDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1)
)
hm2AgentPortSecurityDynamicEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityDynamicVLANId"),
    (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityDynamicMACAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicEntry.setStatus("current")
_Hm2AgentPortSecurityDynamicVLANId_Type = Unsigned32
_Hm2AgentPortSecurityDynamicVLANId_Object = MibTableColumn
hm2AgentPortSecurityDynamicVLANId = _Hm2AgentPortSecurityDynamicVLANId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1, 1),
    _Hm2AgentPortSecurityDynamicVLANId_Type()
)
hm2AgentPortSecurityDynamicVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicVLANId.setStatus("current")
_Hm2AgentPortSecurityDynamicMACAddress_Type = MacAddress
_Hm2AgentPortSecurityDynamicMACAddress_Object = MibTableColumn
hm2AgentPortSecurityDynamicMACAddress = _Hm2AgentPortSecurityDynamicMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 3, 1, 2),
    _Hm2AgentPortSecurityDynamicMACAddress_Type()
)
hm2AgentPortSecurityDynamicMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityDynamicMACAddress.setStatus("current")
_Hm2AgentPortSecurityStaticTable_Object = MibTable
hm2AgentPortSecurityStaticTable = _Hm2AgentPortSecurityStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10)
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticTable.setStatus("current")
_Hm2AgentPortSecurityStaticEntry_Object = MibTableRow
hm2AgentPortSecurityStaticEntry = _Hm2AgentPortSecurityStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1)
)
hm2AgentPortSecurityStaticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityStaticVLANId"),
    (0, "HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityStaticMACAddress"),
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticEntry.setStatus("current")
_Hm2AgentPortSecurityStaticVLANId_Type = Unsigned32
_Hm2AgentPortSecurityStaticVLANId_Object = MibTableColumn
hm2AgentPortSecurityStaticVLANId = _Hm2AgentPortSecurityStaticVLANId_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1, 1),
    _Hm2AgentPortSecurityStaticVLANId_Type()
)
hm2AgentPortSecurityStaticVLANId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticVLANId.setStatus("current")
_Hm2AgentPortSecurityStaticMACAddress_Type = MacAddress
_Hm2AgentPortSecurityStaticMACAddress_Object = MibTableColumn
hm2AgentPortSecurityStaticMACAddress = _Hm2AgentPortSecurityStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 1, 10, 1, 2),
    _Hm2AgentPortSecurityStaticMACAddress_Type()
)
hm2AgentPortSecurityStaticMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2AgentPortSecurityStaticMACAddress.setStatus("current")
_Hm2AgentPortSecurityTraps_ObjectIdentity = ObjectIdentity
hm2AgentPortSecurityTraps = _Hm2AgentPortSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 2)
)

# Managed Objects groups


# Notification objects

hm2AgentPortSecurityViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 12, 20, 2, 1)
)
hm2AgentPortSecurityViolation.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("HM2-PLATFORM-PORTSECURITY-MIB", "hm2AgentPortSecurityLastDiscardedMAC"))
)
if mibBuilder.loadTexts:
    hm2AgentPortSecurityViolation.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-PORTSECURITY-MIB",
    **{"hm2PlatformPortSecurity": hm2PlatformPortSecurity,
       "hm2AgentPortSecurityGroup": hm2AgentPortSecurityGroup,
       "hm2AgentGlobalPortSecurityMode": hm2AgentGlobalPortSecurityMode,
       "hm2AgentPortSecurityTable": hm2AgentPortSecurityTable,
       "hm2AgentPortSecurityEntry": hm2AgentPortSecurityEntry,
       "hm2AgentPortSecurityMode": hm2AgentPortSecurityMode,
       "hm2AgentPortSecurityDynamicLimit": hm2AgentPortSecurityDynamicLimit,
       "hm2AgentPortSecurityStaticLimit": hm2AgentPortSecurityStaticLimit,
       "hm2AgentPortSecurityViolationTrapMode": hm2AgentPortSecurityViolationTrapMode,
       "hm2AgentPortSecurityStaticMACs": hm2AgentPortSecurityStaticMACs,
       "hm2AgentPortSecurityLastDiscardedMAC": hm2AgentPortSecurityLastDiscardedMAC,
       "hm2AgentPortSecurityMACAddressAdd": hm2AgentPortSecurityMACAddressAdd,
       "hm2AgentPortSecurityMACAddressRemove": hm2AgentPortSecurityMACAddressRemove,
       "hm2AgentPortSecurityMACAddressMove": hm2AgentPortSecurityMACAddressMove,
       "hm2AgentPortSecurityDynamicCount": hm2AgentPortSecurityDynamicCount,
       "hm2AgentPortSecurityStaticCount": hm2AgentPortSecurityStaticCount,
       "hm2AgentPortSecurityViolationTrapCount": hm2AgentPortSecurityViolationTrapCount,
       "hm2AgentPortSecurityViolationTrapFrequency": hm2AgentPortSecurityViolationTrapFrequency,
       "hm2AgentPortSecurityAutoDisable": hm2AgentPortSecurityAutoDisable,
       "hm2AgentPortSecurityDynamicTable": hm2AgentPortSecurityDynamicTable,
       "hm2AgentPortSecurityDynamicEntry": hm2AgentPortSecurityDynamicEntry,
       "hm2AgentPortSecurityDynamicVLANId": hm2AgentPortSecurityDynamicVLANId,
       "hm2AgentPortSecurityDynamicMACAddress": hm2AgentPortSecurityDynamicMACAddress,
       "hm2AgentPortSecurityStaticTable": hm2AgentPortSecurityStaticTable,
       "hm2AgentPortSecurityStaticEntry": hm2AgentPortSecurityStaticEntry,
       "hm2AgentPortSecurityStaticVLANId": hm2AgentPortSecurityStaticVLANId,
       "hm2AgentPortSecurityStaticMACAddress": hm2AgentPortSecurityStaticMACAddress,
       "hm2AgentPortSecurityTraps": hm2AgentPortSecurityTraps,
       "hm2AgentPortSecurityViolation": hm2AgentPortSecurityViolation}
)
