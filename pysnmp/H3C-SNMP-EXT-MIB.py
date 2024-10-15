# SNMP MIB module (H3C-SNMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-SNMP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:23 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cSnmpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104)
)
h3cSnmpExt.setRevisions(
        ("2009-04-07 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cSnmpExtScalarObjects_ObjectIdentity = ObjectIdentity
h3cSnmpExtScalarObjects = _H3cSnmpExtScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1)
)


class _H3cSnmpExtSnmpChannel_Type(Integer32):
    """Custom type h3cSnmpExtSnmpChannel based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cSnmpExtSnmpChannel_Type.__name__ = "Integer32"
_H3cSnmpExtSnmpChannel_Object = MibScalar
h3cSnmpExtSnmpChannel = _H3cSnmpExtSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 1),
    _H3cSnmpExtSnmpChannel_Type()
)
h3cSnmpExtSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnmpExtSnmpChannel.setStatus("current")


class _H3cSnmpExtReadCommunitySingle_Type(SnmpAdminString):
    """Custom type h3cSnmpExtReadCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cSnmpExtReadCommunitySingle_Type.__name__ = "SnmpAdminString"
_H3cSnmpExtReadCommunitySingle_Object = MibScalar
h3cSnmpExtReadCommunitySingle = _H3cSnmpExtReadCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 2),
    _H3cSnmpExtReadCommunitySingle_Type()
)
h3cSnmpExtReadCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnmpExtReadCommunitySingle.setStatus("current")


class _H3cSnmpExtWriteCommunitySingle_Type(SnmpAdminString):
    """Custom type h3cSnmpExtWriteCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cSnmpExtWriteCommunitySingle_Type.__name__ = "SnmpAdminString"
_H3cSnmpExtWriteCommunitySingle_Object = MibScalar
h3cSnmpExtWriteCommunitySingle = _H3cSnmpExtWriteCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 1, 3),
    _H3cSnmpExtWriteCommunitySingle_Type()
)
h3cSnmpExtWriteCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnmpExtWriteCommunitySingle.setStatus("current")
_H3cSnmpExtTables_ObjectIdentity = ObjectIdentity
h3cSnmpExtTables = _H3cSnmpExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2)
)
_H3cSnmpExtCommunityTable_Object = MibTable
h3cSnmpExtCommunityTable = _H3cSnmpExtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1)
)
if mibBuilder.loadTexts:
    h3cSnmpExtCommunityTable.setStatus("current")
_H3cSnmpExtCommunityEntry_Object = MibTableRow
h3cSnmpExtCommunityEntry = _H3cSnmpExtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1)
)
h3cSnmpExtCommunityEntry.setIndexNames(
    (0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityLevel"),
    (0, "H3C-SNMP-EXT-MIB", "h3cSnmpExtCommunitySecurityName"),
)
if mibBuilder.loadTexts:
    h3cSnmpExtCommunityEntry.setStatus("current")
_H3cSnmpExtCommunitySecurityLevel_Type = SnmpSecurityModel
_H3cSnmpExtCommunitySecurityLevel_Object = MibTableColumn
h3cSnmpExtCommunitySecurityLevel = _H3cSnmpExtCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 1),
    _H3cSnmpExtCommunitySecurityLevel_Type()
)
h3cSnmpExtCommunitySecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSnmpExtCommunitySecurityLevel.setStatus("current")
_H3cSnmpExtCommunitySecurityName_Type = SnmpAdminString
_H3cSnmpExtCommunitySecurityName_Object = MibTableColumn
h3cSnmpExtCommunitySecurityName = _H3cSnmpExtCommunitySecurityName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 2),
    _H3cSnmpExtCommunitySecurityName_Type()
)
h3cSnmpExtCommunitySecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cSnmpExtCommunitySecurityName.setStatus("current")


class _H3cSnmpExtCommunityName_Type(OctetString):
    """Custom type h3cSnmpExtCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_H3cSnmpExtCommunityName_Type.__name__ = "OctetString"
_H3cSnmpExtCommunityName_Object = MibTableColumn
h3cSnmpExtCommunityName = _H3cSnmpExtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 3),
    _H3cSnmpExtCommunityName_Type()
)
h3cSnmpExtCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cSnmpExtCommunityName.setStatus("current")


class _H3cSnmpExtCommunityAclNum_Type(Integer32):
    """Custom type h3cSnmpExtCommunityAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_H3cSnmpExtCommunityAclNum_Type.__name__ = "Integer32"
_H3cSnmpExtCommunityAclNum_Object = MibTableColumn
h3cSnmpExtCommunityAclNum = _H3cSnmpExtCommunityAclNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 2, 1, 1, 4),
    _H3cSnmpExtCommunityAclNum_Type()
)
h3cSnmpExtCommunityAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cSnmpExtCommunityAclNum.setStatus("current")
_H3cSnmpExtNotifications_ObjectIdentity = ObjectIdentity
h3cSnmpExtNotifications = _H3cSnmpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 104, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-SNMP-EXT-MIB",
    **{"h3cSnmpExt": h3cSnmpExt,
       "h3cSnmpExtScalarObjects": h3cSnmpExtScalarObjects,
       "h3cSnmpExtSnmpChannel": h3cSnmpExtSnmpChannel,
       "h3cSnmpExtReadCommunitySingle": h3cSnmpExtReadCommunitySingle,
       "h3cSnmpExtWriteCommunitySingle": h3cSnmpExtWriteCommunitySingle,
       "h3cSnmpExtTables": h3cSnmpExtTables,
       "h3cSnmpExtCommunityTable": h3cSnmpExtCommunityTable,
       "h3cSnmpExtCommunityEntry": h3cSnmpExtCommunityEntry,
       "h3cSnmpExtCommunitySecurityLevel": h3cSnmpExtCommunitySecurityLevel,
       "h3cSnmpExtCommunitySecurityName": h3cSnmpExtCommunitySecurityName,
       "h3cSnmpExtCommunityName": h3cSnmpExtCommunityName,
       "h3cSnmpExtCommunityAclNum": h3cSnmpExtCommunityAclNum,
       "h3cSnmpExtNotifications": h3cSnmpExtNotifications}
)
