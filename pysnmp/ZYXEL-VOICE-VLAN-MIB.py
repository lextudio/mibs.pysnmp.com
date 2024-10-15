# SNMP MIB module (ZYXEL-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-VOICE-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:23:06 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelVoiceVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelVoiceVlanSetup_ObjectIdentity = ObjectIdentity
zyxelVoiceVlanSetup = _ZyxelVoiceVlanSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1)
)


class _ZyxelVoiceVlanID_Type(Integer32):
    """Custom type zyxelVoiceVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZyxelVoiceVlanID_Type.__name__ = "Integer32"
_ZyxelVoiceVlanID_Object = MibScalar
zyxelVoiceVlanID = _ZyxelVoiceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 1),
    _ZyxelVoiceVlanID_Type()
)
zyxelVoiceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyxelVoiceVlanID.setStatus("current")


class _ZyxelVoiceVlanPriority_Type(Integer32):
    """Custom type zyxelVoiceVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZyxelVoiceVlanPriority_Type.__name__ = "Integer32"
_ZyxelVoiceVlanPriority_Object = MibScalar
zyxelVoiceVlanPriority = _ZyxelVoiceVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 2),
    _ZyxelVoiceVlanPriority_Type()
)
zyxelVoiceVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyxelVoiceVlanPriority.setStatus("current")
_ZyxelVoiceVlanMaxNumberOfOUI_Type = Integer32
_ZyxelVoiceVlanMaxNumberOfOUI_Object = MibScalar
zyxelVoiceVlanMaxNumberOfOUI = _ZyxelVoiceVlanMaxNumberOfOUI_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 5),
    _ZyxelVoiceVlanMaxNumberOfOUI_Type()
)
zyxelVoiceVlanMaxNumberOfOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyxelVoiceVlanMaxNumberOfOUI.setStatus("current")
_ZyxelVoiceVlanOUITable_Object = MibTable
zyxelVoiceVlanOUITable = _ZyxelVoiceVlanOUITable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6)
)
if mibBuilder.loadTexts:
    zyxelVoiceVlanOUITable.setStatus("current")
_ZyxelVoiceVlanOUIEntry_Object = MibTableRow
zyxelVoiceVlanOUIEntry = _ZyxelVoiceVlanOUIEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6, 1)
)
zyxelVoiceVlanOUIEntry.setIndexNames(
    (0, "ZYXEL-VOICE-VLAN-MIB", "zyVoiceVlanOUIAddress"),
    (0, "ZYXEL-VOICE-VLAN-MIB", "zyVoiceVlanOUIMask"),
)
if mibBuilder.loadTexts:
    zyxelVoiceVlanOUIEntry.setStatus("current")
_ZyVoiceVlanOUIAddress_Type = MacAddress
_ZyVoiceVlanOUIAddress_Object = MibTableColumn
zyVoiceVlanOUIAddress = _ZyVoiceVlanOUIAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6, 1, 1),
    _ZyVoiceVlanOUIAddress_Type()
)
zyVoiceVlanOUIAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVoiceVlanOUIAddress.setStatus("current")
_ZyVoiceVlanOUIMask_Type = MacAddress
_ZyVoiceVlanOUIMask_Object = MibTableColumn
zyVoiceVlanOUIMask = _ZyVoiceVlanOUIMask_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6, 1, 2),
    _ZyVoiceVlanOUIMask_Type()
)
zyVoiceVlanOUIMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyVoiceVlanOUIMask.setStatus("current")
_ZyVoiceVlanOUIDescription_Type = DisplayString
_ZyVoiceVlanOUIDescription_Object = MibTableColumn
zyVoiceVlanOUIDescription = _ZyVoiceVlanOUIDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6, 1, 3),
    _ZyVoiceVlanOUIDescription_Type()
)
zyVoiceVlanOUIDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVoiceVlanOUIDescription.setStatus("current")
_ZyVoiceVlanOUIRowStatus_Type = RowStatus
_ZyVoiceVlanOUIRowStatus_Object = MibTableColumn
zyVoiceVlanOUIRowStatus = _ZyVoiceVlanOUIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 96, 1, 6, 1, 4),
    _ZyVoiceVlanOUIRowStatus_Type()
)
zyVoiceVlanOUIRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyVoiceVlanOUIRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-VOICE-VLAN-MIB",
    **{"zyxelVoiceVlan": zyxelVoiceVlan,
       "zyxelVoiceVlanSetup": zyxelVoiceVlanSetup,
       "zyxelVoiceVlanID": zyxelVoiceVlanID,
       "zyxelVoiceVlanPriority": zyxelVoiceVlanPriority,
       "zyxelVoiceVlanMaxNumberOfOUI": zyxelVoiceVlanMaxNumberOfOUI,
       "zyxelVoiceVlanOUITable": zyxelVoiceVlanOUITable,
       "zyxelVoiceVlanOUIEntry": zyxelVoiceVlanOUIEntry,
       "zyVoiceVlanOUIAddress": zyVoiceVlanOUIAddress,
       "zyVoiceVlanOUIMask": zyVoiceVlanOUIMask,
       "zyVoiceVlanOUIDescription": zyVoiceVlanOUIDescription,
       "zyVoiceVlanOUIRowStatus": zyVoiceVlanOUIRowStatus}
)
