# SNMP MIB module (HP-ICF-DEVICEIDENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DEVICEIDENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:15 2024
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

hpicfDeviceIdentityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135)
)
hpicfDeviceIdentityMIB.setRevisions(
        ("2017-01-03 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDeviceIdentityConfig_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityConfig = _HpicfDeviceIdentityConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1)
)
_HpicfDeviceIdentityTable_Object = MibTable
hpicfDeviceIdentityTable = _HpicfDeviceIdentityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityTable.setStatus("current")
_HpicfDeviceIdentityEntry_Object = MibTableRow
hpicfDeviceIdentityEntry = _HpicfDeviceIdentityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1)
)
hpicfDeviceIdentityEntry.setIndexNames(
    (0, "HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityIndex"),
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityEntry.setStatus("current")


class _HpicfDeviceIdentityIndex_Type(Unsigned32):
    """Custom type hpicfDeviceIdentityIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HpicfDeviceIdentityIndex_Type.__name__ = "Unsigned32"
_HpicfDeviceIdentityIndex_Object = MibTableColumn
hpicfDeviceIdentityIndex = _HpicfDeviceIdentityIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 1),
    _HpicfDeviceIdentityIndex_Type()
)
hpicfDeviceIdentityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityIndex.setStatus("current")
_HpicfDeviceIdentityRowStatus_Type = RowStatus
_HpicfDeviceIdentityRowStatus_Object = MibTableColumn
hpicfDeviceIdentityRowStatus = _HpicfDeviceIdentityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 2),
    _HpicfDeviceIdentityRowStatus_Type()
)
hpicfDeviceIdentityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityRowStatus.setStatus("current")


class _HpicfDeviceIdentityName_Type(OctetString):
    """Custom type hpicfDeviceIdentityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_HpicfDeviceIdentityName_Type.__name__ = "OctetString"
_HpicfDeviceIdentityName_Object = MibTableColumn
hpicfDeviceIdentityName = _HpicfDeviceIdentityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 3),
    _HpicfDeviceIdentityName_Type()
)
hpicfDeviceIdentityName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityName.setStatus("current")


class _HpicfDeviceIdentityLldpOui_Type(OctetString):
    """Custom type hpicfDeviceIdentityLldpOui based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpicfDeviceIdentityLldpOui_Type.__name__ = "OctetString"
_HpicfDeviceIdentityLldpOui_Object = MibTableColumn
hpicfDeviceIdentityLldpOui = _HpicfDeviceIdentityLldpOui_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 4),
    _HpicfDeviceIdentityLldpOui_Type()
)
hpicfDeviceIdentityLldpOui.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpOui.setStatus("current")


class _HpicfDeviceIdentityLldpSubType_Type(Integer32):
    """Custom type hpicfDeviceIdentityLldpSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpicfDeviceIdentityLldpSubType_Type.__name__ = "Integer32"
_HpicfDeviceIdentityLldpSubType_Object = MibTableColumn
hpicfDeviceIdentityLldpSubType = _HpicfDeviceIdentityLldpSubType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 1, 1, 1, 5),
    _HpicfDeviceIdentityLldpSubType_Type()
)
hpicfDeviceIdentityLldpSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDeviceIdentityLldpSubType.setStatus("current")
_HpicfDeviceIdentityConformance_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityConformance = _HpicfDeviceIdentityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2)
)
_HpicfDeviceIdentityGroups_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityGroups = _HpicfDeviceIdentityGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1)
)
_HpicfDeviceIdentityCompliances_ObjectIdentity = ObjectIdentity
hpicfDeviceIdentityCompliances = _HpicfDeviceIdentityCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2)
)

# Managed Objects groups

hpicfDeviceIdentityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 1, 1)
)
hpicfDeviceIdentityGroup.setObjects(
      *(("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityRowStatus"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityName"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpOui"),
        ("HP-ICF-DEVICEIDENTITY-MIB", "hpicfDeviceIdentityLldpSubType"))
)
if mibBuilder.loadTexts:
    hpicfDeviceIdentityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfiDeviceIdentityCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 135, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfiDeviceIdentityCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DEVICEIDENTITY-MIB",
    **{"hpicfDeviceIdentityMIB": hpicfDeviceIdentityMIB,
       "hpicfDeviceIdentityConfig": hpicfDeviceIdentityConfig,
       "hpicfDeviceIdentityTable": hpicfDeviceIdentityTable,
       "hpicfDeviceIdentityEntry": hpicfDeviceIdentityEntry,
       "hpicfDeviceIdentityIndex": hpicfDeviceIdentityIndex,
       "hpicfDeviceIdentityRowStatus": hpicfDeviceIdentityRowStatus,
       "hpicfDeviceIdentityName": hpicfDeviceIdentityName,
       "hpicfDeviceIdentityLldpOui": hpicfDeviceIdentityLldpOui,
       "hpicfDeviceIdentityLldpSubType": hpicfDeviceIdentityLldpSubType,
       "hpicfDeviceIdentityConformance": hpicfDeviceIdentityConformance,
       "hpicfDeviceIdentityGroups": hpicfDeviceIdentityGroups,
       "hpicfDeviceIdentityGroup": hpicfDeviceIdentityGroup,
       "hpicfDeviceIdentityCompliances": hpicfDeviceIdentityCompliances,
       "hpicfiDeviceIdentityCompliance": hpicfiDeviceIdentityCompliance}
)
