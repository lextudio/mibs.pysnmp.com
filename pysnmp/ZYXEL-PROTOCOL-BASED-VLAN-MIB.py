# SNMP MIB module (ZYXEL-PROTOCOL-BASED-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-PROTOCOL-BASED-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:39 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelProtocolBasedVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelProtocolBasedVlanSetup_ObjectIdentity = ObjectIdentity
zyxelProtocolBasedVlanSetup = _ZyxelProtocolBasedVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1)
)
_ZyProtocolBasedVlanMaxNumberOfVlans_Type = Integer32
_ZyProtocolBasedVlanMaxNumberOfVlans_Object = MibScalar
zyProtocolBasedVlanMaxNumberOfVlans = _ZyProtocolBasedVlanMaxNumberOfVlans_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 1),
    _ZyProtocolBasedVlanMaxNumberOfVlans_Type()
)
zyProtocolBasedVlanMaxNumberOfVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanMaxNumberOfVlans.setStatus("current")
_ZyxelProtocolBasedVlanTable_Object = MibTable
zyxelProtocolBasedVlanTable = _ZyxelProtocolBasedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelProtocolBasedVlanTable.setStatus("current")
_ZyxelProtocolBasedVlanEntry_Object = MibTableRow
zyxelProtocolBasedVlanEntry = _ZyxelProtocolBasedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1)
)
zyxelProtocolBasedVlanEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-PROTOCOL-BASED-VLAN-MIB", "zyProtocolBasedVlanPacketType"),
    (0, "ZYXEL-PROTOCOL-BASED-VLAN-MIB", "zyProtocolBasedVlanEthernetType"),
)
if mibBuilder.loadTexts:
    zyxelProtocolBasedVlanEntry.setStatus("current")


class _ZyProtocolBasedVlanPacketType_Type(Integer32):
    """Custom type zyProtocolBasedVlanPacketType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("etherII", 1),
          ("llc", 3),
          ("snap", 2))
    )


_ZyProtocolBasedVlanPacketType_Type.__name__ = "Integer32"
_ZyProtocolBasedVlanPacketType_Object = MibTableColumn
zyProtocolBasedVlanPacketType = _ZyProtocolBasedVlanPacketType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 1),
    _ZyProtocolBasedVlanPacketType_Type()
)
zyProtocolBasedVlanPacketType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanPacketType.setStatus("current")
_ZyProtocolBasedVlanEthernetType_Type = Integer32
_ZyProtocolBasedVlanEthernetType_Object = MibTableColumn
zyProtocolBasedVlanEthernetType = _ZyProtocolBasedVlanEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 2),
    _ZyProtocolBasedVlanEthernetType_Type()
)
zyProtocolBasedVlanEthernetType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanEthernetType.setStatus("current")


class _ZyProtocolBasedVlanName_Type(DisplayString):
    """Custom type zyProtocolBasedVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZyProtocolBasedVlanName_Type.__name__ = "DisplayString"
_ZyProtocolBasedVlanName_Object = MibTableColumn
zyProtocolBasedVlanName = _ZyProtocolBasedVlanName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 3),
    _ZyProtocolBasedVlanName_Type()
)
zyProtocolBasedVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanName.setStatus("current")


class _ZyProtocolBasedVlanVid_Type(Integer32):
    """Custom type zyProtocolBasedVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZyProtocolBasedVlanVid_Type.__name__ = "Integer32"
_ZyProtocolBasedVlanVid_Object = MibTableColumn
zyProtocolBasedVlanVid = _ZyProtocolBasedVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 4),
    _ZyProtocolBasedVlanVid_Type()
)
zyProtocolBasedVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanVid.setStatus("current")


class _ZyProtocolBasedVlanPriority_Type(Integer32):
    """Custom type zyProtocolBasedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZyProtocolBasedVlanPriority_Type.__name__ = "Integer32"
_ZyProtocolBasedVlanPriority_Object = MibTableColumn
zyProtocolBasedVlanPriority = _ZyProtocolBasedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 5),
    _ZyProtocolBasedVlanPriority_Type()
)
zyProtocolBasedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanPriority.setStatus("current")
_ZyProtocolBasedVlanRowStatus_Type = RowStatus
_ZyProtocolBasedVlanRowStatus_Object = MibTableColumn
zyProtocolBasedVlanRowStatus = _ZyProtocolBasedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 69, 1, 2, 1, 6),
    _ZyProtocolBasedVlanRowStatus_Type()
)
zyProtocolBasedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zyProtocolBasedVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-PROTOCOL-BASED-VLAN-MIB",
    **{"zyxelProtocolBasedVlan": zyxelProtocolBasedVlan,
       "zyxelProtocolBasedVlanSetup": zyxelProtocolBasedVlanSetup,
       "zyProtocolBasedVlanMaxNumberOfVlans": zyProtocolBasedVlanMaxNumberOfVlans,
       "zyxelProtocolBasedVlanTable": zyxelProtocolBasedVlanTable,
       "zyxelProtocolBasedVlanEntry": zyxelProtocolBasedVlanEntry,
       "zyProtocolBasedVlanPacketType": zyProtocolBasedVlanPacketType,
       "zyProtocolBasedVlanEthernetType": zyProtocolBasedVlanEthernetType,
       "zyProtocolBasedVlanName": zyProtocolBasedVlanName,
       "zyProtocolBasedVlanVid": zyProtocolBasedVlanVid,
       "zyProtocolBasedVlanPriority": zyProtocolBasedVlanPriority,
       "zyProtocolBasedVlanRowStatus": zyProtocolBasedVlanRowStatus}
)
