# SNMP MIB module (TPLINK-MAC-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TPLINK-MAC-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:06:21 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkMacVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15)
)
tplinkMacVlanMIB.setRevisions(
        ("2009-08-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkMacVlanMIBObjects_ObjectIdentity = ObjectIdentity
tplinkMacVlanMIBObjects = _TplinkMacVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1)
)
_MacVlanConfig_ObjectIdentity = ObjectIdentity
macVlanConfig = _MacVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1)
)
_MacVlanConfigTable_Object = MibTable
macVlanConfigTable = _MacVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1)
)
if mibBuilder.loadTexts:
    macVlanConfigTable.setStatus("current")
_MacVlanEntry_Object = MibTableRow
macVlanEntry = _MacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1)
)
macVlanEntry.setIndexNames(
    (0, "TPLINK-MAC-VLAN-MIB", "macAddr"),
)
if mibBuilder.loadTexts:
    macVlanEntry.setStatus("current")
_MacAddr_Type = MacAddress
_MacAddr_Object = MibTableColumn
macAddr = _MacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 1),
    _MacAddr_Type()
)
macAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macAddr.setStatus("current")


class _MacDescription_Type(OctetString):
    """Custom type macDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MacDescription_Type.__name__ = "OctetString"
_MacDescription_Object = MibTableColumn
macDescription = _MacDescription_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 2),
    _MacDescription_Type()
)
macDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macDescription.setStatus("current")


class _MacVlanId_Type(Integer32):
    """Custom type macVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_MacVlanId_Type.__name__ = "Integer32"
_MacVlanId_Object = MibTableColumn
macVlanId = _MacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 3),
    _MacVlanId_Type()
)
macVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanId.setStatus("current")
_MacVlanStatus_Type = TPRowStatus
_MacVlanStatus_Object = MibTableColumn
macVlanStatus = _MacVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 1, 1, 1, 4),
    _MacVlanStatus_Type()
)
macVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanStatus.setStatus("current")
_MacVlanPort_ObjectIdentity = ObjectIdentity
macVlanPort = _MacVlanPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2)
)
_MacVlanPortTable_Object = MibTable
macVlanPortTable = _MacVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1)
)
if mibBuilder.loadTexts:
    macVlanPortTable.setStatus("current")
_MacVlanPortEntry_Object = MibTableRow
macVlanPortEntry = _MacVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1)
)
macVlanPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    macVlanPortEntry.setStatus("current")


class _MacVlanPortNumber_Type(OctetString):
    """Custom type macVlanPortNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_MacVlanPortNumber_Type.__name__ = "OctetString"
_MacVlanPortNumber_Object = MibTableColumn
macVlanPortNumber = _MacVlanPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 1),
    _MacVlanPortNumber_Type()
)
macVlanPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVlanPortNumber.setStatus("current")


class _MacVlanPortEnable_Type(Integer32):
    """Custom type macVlanPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MacVlanPortEnable_Type.__name__ = "Integer32"
_MacVlanPortEnable_Object = MibTableColumn
macVlanPortEnable = _MacVlanPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 2),
    _MacVlanPortEnable_Type()
)
macVlanPortEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanPortEnable.setStatus("current")


class _MacVlanPortLag_Type(OctetString):
    """Custom type macVlanPortLag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_MacVlanPortLag_Type.__name__ = "OctetString"
_MacVlanPortLag_Object = MibTableColumn
macVlanPortLag = _MacVlanPortLag_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 1, 2, 1, 1, 3),
    _MacVlanPortLag_Type()
)
macVlanPortLag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macVlanPortLag.setStatus("current")
_TplinkMacVlanNotifications_ObjectIdentity = ObjectIdentity
tplinkMacVlanNotifications = _TplinkMacVlanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 15, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-MAC-VLAN-MIB",
    **{"tplinkMacVlanMIB": tplinkMacVlanMIB,
       "tplinkMacVlanMIBObjects": tplinkMacVlanMIBObjects,
       "macVlanConfig": macVlanConfig,
       "macVlanConfigTable": macVlanConfigTable,
       "macVlanEntry": macVlanEntry,
       "macAddr": macAddr,
       "macDescription": macDescription,
       "macVlanId": macVlanId,
       "macVlanStatus": macVlanStatus,
       "macVlanPort": macVlanPort,
       "macVlanPortTable": macVlanPortTable,
       "macVlanPortEntry": macVlanPortEntry,
       "macVlanPortNumber": macVlanPortNumber,
       "macVlanPortEnable": macVlanPortEnable,
       "macVlanPortLag": macVlanPortLag,
       "tplinkMacVlanNotifications": tplinkMacVlanNotifications}
)
