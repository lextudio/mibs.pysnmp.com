# SNMP MIB module (HH3C-SNMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-SNMP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:55 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(SnmpAdminString,
 SnmpSecurityLevel,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityLevel",
    "SnmpSecurityModel")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cSnmpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104)
)
hh3cSnmpExt.setRevisions(
        ("2009-04-07 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cSnmpExtScalarObjects_ObjectIdentity = ObjectIdentity
hh3cSnmpExtScalarObjects = _Hh3cSnmpExtScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1)
)


class _Hh3cSnmpExtSnmpChannel_Type(Integer32):
    """Custom type hh3cSnmpExtSnmpChannel based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cSnmpExtSnmpChannel_Type.__name__ = "Integer32"
_Hh3cSnmpExtSnmpChannel_Object = MibScalar
hh3cSnmpExtSnmpChannel = _Hh3cSnmpExtSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 1),
    _Hh3cSnmpExtSnmpChannel_Type()
)
hh3cSnmpExtSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtSnmpChannel.setStatus("current")


class _Hh3cSnmpExtReadCommunitySingle_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtReadCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtReadCommunitySingle_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtReadCommunitySingle_Object = MibScalar
hh3cSnmpExtReadCommunitySingle = _Hh3cSnmpExtReadCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 2),
    _Hh3cSnmpExtReadCommunitySingle_Type()
)
hh3cSnmpExtReadCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtReadCommunitySingle.setStatus("current")


class _Hh3cSnmpExtWriteCommunitySingle_Type(SnmpAdminString):
    """Custom type hh3cSnmpExtWriteCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtWriteCommunitySingle_Type.__name__ = "SnmpAdminString"
_Hh3cSnmpExtWriteCommunitySingle_Object = MibScalar
hh3cSnmpExtWriteCommunitySingle = _Hh3cSnmpExtWriteCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 1, 3),
    _Hh3cSnmpExtWriteCommunitySingle_Type()
)
hh3cSnmpExtWriteCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtWriteCommunitySingle.setStatus("current")
_Hh3cSnmpExtTables_ObjectIdentity = ObjectIdentity
hh3cSnmpExtTables = _Hh3cSnmpExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2)
)
_Hh3cSnmpExtCommunityTable_Object = MibTable
hh3cSnmpExtCommunityTable = _Hh3cSnmpExtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityTable.setStatus("current")
_Hh3cSnmpExtCommunityEntry_Object = MibTableRow
hh3cSnmpExtCommunityEntry = _Hh3cSnmpExtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1)
)
hh3cSnmpExtCommunityEntry.setIndexNames(
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityLevel"),
    (0, "HH3C-SNMP-EXT-MIB", "hh3cSnmpExtCommunitySecurityName"),
)
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityEntry.setStatus("current")
_Hh3cSnmpExtCommunitySecurityLevel_Type = SnmpSecurityModel
_Hh3cSnmpExtCommunitySecurityLevel_Object = MibTableColumn
hh3cSnmpExtCommunitySecurityLevel = _Hh3cSnmpExtCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 1),
    _Hh3cSnmpExtCommunitySecurityLevel_Type()
)
hh3cSnmpExtCommunitySecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunitySecurityLevel.setStatus("current")
_Hh3cSnmpExtCommunitySecurityName_Type = SnmpAdminString
_Hh3cSnmpExtCommunitySecurityName_Object = MibTableColumn
hh3cSnmpExtCommunitySecurityName = _Hh3cSnmpExtCommunitySecurityName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 2),
    _Hh3cSnmpExtCommunitySecurityName_Type()
)
hh3cSnmpExtCommunitySecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunitySecurityName.setStatus("current")


class _Hh3cSnmpExtCommunityName_Type(OctetString):
    """Custom type hh3cSnmpExtCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Hh3cSnmpExtCommunityName_Type.__name__ = "OctetString"
_Hh3cSnmpExtCommunityName_Object = MibTableColumn
hh3cSnmpExtCommunityName = _Hh3cSnmpExtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 3),
    _Hh3cSnmpExtCommunityName_Type()
)
hh3cSnmpExtCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityName.setStatus("current")


class _Hh3cSnmpExtCommunityAclNum_Type(Integer32):
    """Custom type hh3cSnmpExtCommunityAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_Hh3cSnmpExtCommunityAclNum_Type.__name__ = "Integer32"
_Hh3cSnmpExtCommunityAclNum_Object = MibTableColumn
hh3cSnmpExtCommunityAclNum = _Hh3cSnmpExtCommunityAclNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 2, 1, 1, 4),
    _Hh3cSnmpExtCommunityAclNum_Type()
)
hh3cSnmpExtCommunityAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cSnmpExtCommunityAclNum.setStatus("current")
_Hh3cSnmpExtNotifications_ObjectIdentity = ObjectIdentity
hh3cSnmpExtNotifications = _Hh3cSnmpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 104, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-SNMP-EXT-MIB",
    **{"hh3cSnmpExt": hh3cSnmpExt,
       "hh3cSnmpExtScalarObjects": hh3cSnmpExtScalarObjects,
       "hh3cSnmpExtSnmpChannel": hh3cSnmpExtSnmpChannel,
       "hh3cSnmpExtReadCommunitySingle": hh3cSnmpExtReadCommunitySingle,
       "hh3cSnmpExtWriteCommunitySingle": hh3cSnmpExtWriteCommunitySingle,
       "hh3cSnmpExtTables": hh3cSnmpExtTables,
       "hh3cSnmpExtCommunityTable": hh3cSnmpExtCommunityTable,
       "hh3cSnmpExtCommunityEntry": hh3cSnmpExtCommunityEntry,
       "hh3cSnmpExtCommunitySecurityLevel": hh3cSnmpExtCommunitySecurityLevel,
       "hh3cSnmpExtCommunitySecurityName": hh3cSnmpExtCommunitySecurityName,
       "hh3cSnmpExtCommunityName": hh3cSnmpExtCommunityName,
       "hh3cSnmpExtCommunityAclNum": hh3cSnmpExtCommunityAclNum,
       "hh3cSnmpExtNotifications": hh3cSnmpExtNotifications}
)
