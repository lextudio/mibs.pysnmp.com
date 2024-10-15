# SNMP MIB module (HPN-ICF-SNMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-SNMP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:51 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(SnmpAdminString,
 SnmpSecurityModel) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString",
    "SnmpSecurityModel")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpnicfSnmpExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104)
)
hpnicfSnmpExt.setRevisions(
        ("2009-04-07 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfSnmpExtScalarObjects_ObjectIdentity = ObjectIdentity
hpnicfSnmpExtScalarObjects = _HpnicfSnmpExtScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1)
)


class _HpnicfSnmpExtSnmpChannel_Type(Integer32):
    """Custom type hpnicfSnmpExtSnmpChannel based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSnmpExtSnmpChannel_Type.__name__ = "Integer32"
_HpnicfSnmpExtSnmpChannel_Object = MibScalar
hpnicfSnmpExtSnmpChannel = _HpnicfSnmpExtSnmpChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 1),
    _HpnicfSnmpExtSnmpChannel_Type()
)
hpnicfSnmpExtSnmpChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSnmpExtSnmpChannel.setStatus("current")


class _HpnicfSnmpExtReadCommunitySingle_Type(SnmpAdminString):
    """Custom type hpnicfSnmpExtReadCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpExtReadCommunitySingle_Type.__name__ = "SnmpAdminString"
_HpnicfSnmpExtReadCommunitySingle_Object = MibScalar
hpnicfSnmpExtReadCommunitySingle = _HpnicfSnmpExtReadCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 2),
    _HpnicfSnmpExtReadCommunitySingle_Type()
)
hpnicfSnmpExtReadCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSnmpExtReadCommunitySingle.setStatus("current")


class _HpnicfSnmpExtWriteCommunitySingle_Type(SnmpAdminString):
    """Custom type hpnicfSnmpExtWriteCommunitySingle based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpExtWriteCommunitySingle_Type.__name__ = "SnmpAdminString"
_HpnicfSnmpExtWriteCommunitySingle_Object = MibScalar
hpnicfSnmpExtWriteCommunitySingle = _HpnicfSnmpExtWriteCommunitySingle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 3),
    _HpnicfSnmpExtWriteCommunitySingle_Type()
)
hpnicfSnmpExtWriteCommunitySingle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSnmpExtWriteCommunitySingle.setStatus("current")


class _HpnicfSnmpExtMaxContextNum_Type(Integer32):
    """Custom type hpnicfSnmpExtMaxContextNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfSnmpExtMaxContextNum_Type.__name__ = "Integer32"
_HpnicfSnmpExtMaxContextNum_Object = MibScalar
hpnicfSnmpExtMaxContextNum = _HpnicfSnmpExtMaxContextNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 1, 4),
    _HpnicfSnmpExtMaxContextNum_Type()
)
hpnicfSnmpExtMaxContextNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSnmpExtMaxContextNum.setStatus("current")
_HpnicfSnmpExtTables_ObjectIdentity = ObjectIdentity
hpnicfSnmpExtTables = _HpnicfSnmpExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2)
)
_HpnicfSnmpExtCommunityTable_Object = MibTable
hpnicfSnmpExtCommunityTable = _HpnicfSnmpExtCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunityTable.setStatus("current")
_HpnicfSnmpExtCommunityEntry_Object = MibTableRow
hpnicfSnmpExtCommunityEntry = _HpnicfSnmpExtCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1)
)
hpnicfSnmpExtCommunityEntry.setIndexNames(
    (0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtCommunitySecurityLevel"),
    (0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtCommunitySecurityName"),
)
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunityEntry.setStatus("current")
_HpnicfSnmpExtCommunitySecurityLevel_Type = SnmpSecurityModel
_HpnicfSnmpExtCommunitySecurityLevel_Object = MibTableColumn
hpnicfSnmpExtCommunitySecurityLevel = _HpnicfSnmpExtCommunitySecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 1),
    _HpnicfSnmpExtCommunitySecurityLevel_Type()
)
hpnicfSnmpExtCommunitySecurityLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunitySecurityLevel.setStatus("current")


class _HpnicfSnmpExtCommunitySecurityName_Type(SnmpAdminString):
    """Custom type hpnicfSnmpExtCommunitySecurityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpExtCommunitySecurityName_Type.__name__ = "SnmpAdminString"
_HpnicfSnmpExtCommunitySecurityName_Object = MibTableColumn
hpnicfSnmpExtCommunitySecurityName = _HpnicfSnmpExtCommunitySecurityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 2),
    _HpnicfSnmpExtCommunitySecurityName_Type()
)
hpnicfSnmpExtCommunitySecurityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunitySecurityName.setStatus("current")


class _HpnicfSnmpExtCommunityName_Type(OctetString):
    """Custom type hpnicfSnmpExtCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpExtCommunityName_Type.__name__ = "OctetString"
_HpnicfSnmpExtCommunityName_Object = MibTableColumn
hpnicfSnmpExtCommunityName = _HpnicfSnmpExtCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 3),
    _HpnicfSnmpExtCommunityName_Type()
)
hpnicfSnmpExtCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunityName.setStatus("current")


class _HpnicfSnmpExtCommunityAclNum_Type(Integer32):
    """Custom type hpnicfSnmpExtCommunityAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HpnicfSnmpExtCommunityAclNum_Type.__name__ = "Integer32"
_HpnicfSnmpExtCommunityAclNum_Object = MibTableColumn
hpnicfSnmpExtCommunityAclNum = _HpnicfSnmpExtCommunityAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 1, 1, 4),
    _HpnicfSnmpExtCommunityAclNum_Type()
)
hpnicfSnmpExtCommunityAclNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfSnmpExtCommunityAclNum.setStatus("current")
_HpnicfSnmpCommunityExTable_Object = MibTable
hpnicfSnmpCommunityExTable = _HpnicfSnmpCommunityExTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExTable.setStatus("current")
_HpnicfSnmpCommunityExEntry_Object = MibTableRow
hpnicfSnmpCommunityExEntry = _HpnicfSnmpCommunityExEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1)
)
hpnicfSnmpCommunityExEntry.setIndexNames(
    (0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpCommunityExName"),
)
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExEntry.setStatus("current")


class _HpnicfSnmpCommunityExName_Type(OctetString):
    """Custom type hpnicfSnmpCommunityExName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpCommunityExName_Type.__name__ = "OctetString"
_HpnicfSnmpCommunityExName_Object = MibTableColumn
hpnicfSnmpCommunityExName = _HpnicfSnmpCommunityExName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 1),
    _HpnicfSnmpCommunityExName_Type()
)
hpnicfSnmpCommunityExName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExName.setStatus("current")


class _HpnicfSnmpCommunityExWrite_Type(TruthValue):
    """Custom type hpnicfSnmpCommunityExWrite based on TruthValue"""


_HpnicfSnmpCommunityExWrite_Object = MibTableColumn
hpnicfSnmpCommunityExWrite = _HpnicfSnmpCommunityExWrite_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 2),
    _HpnicfSnmpCommunityExWrite_Type()
)
hpnicfSnmpCommunityExWrite.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExWrite.setStatus("current")


class _HpnicfSnmpCommunityExViewName_Type(OctetString):
    """Custom type hpnicfSnmpCommunityExViewName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpCommunityExViewName_Type.__name__ = "OctetString"
_HpnicfSnmpCommunityExViewName_Object = MibTableColumn
hpnicfSnmpCommunityExViewName = _HpnicfSnmpCommunityExViewName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 3),
    _HpnicfSnmpCommunityExViewName_Type()
)
hpnicfSnmpCommunityExViewName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExViewName.setStatus("current")


class _HpnicfSnmpCommunityExAclNum_Type(Integer32):
    """Custom type hpnicfSnmpCommunityExAclNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 2999),
    )


_HpnicfSnmpCommunityExAclNum_Type.__name__ = "Integer32"
_HpnicfSnmpCommunityExAclNum_Object = MibTableColumn
hpnicfSnmpCommunityExAclNum = _HpnicfSnmpCommunityExAclNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 4),
    _HpnicfSnmpCommunityExAclNum_Type()
)
hpnicfSnmpCommunityExAclNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExAclNum.setStatus("current")
_HpnicfSnmpCommunityExRowStatus_Type = RowStatus
_HpnicfSnmpCommunityExRowStatus_Object = MibTableColumn
hpnicfSnmpCommunityExRowStatus = _HpnicfSnmpCommunityExRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 2, 1, 5),
    _HpnicfSnmpCommunityExRowStatus_Type()
)
hpnicfSnmpCommunityExRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSnmpCommunityExRowStatus.setStatus("current")
_HpnicfSnmpExtContextTable_Object = MibTable
hpnicfSnmpExtContextTable = _HpnicfSnmpExtContextTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfSnmpExtContextTable.setStatus("current")
_HpnicfSnmpExtContextEntry_Object = MibTableRow
hpnicfSnmpExtContextEntry = _HpnicfSnmpExtContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1)
)
hpnicfSnmpExtContextEntry.setIndexNames(
    (0, "HPN-ICF-SNMP-EXT-MIB", "hpnicfSnmpExtContextName"),
)
if mibBuilder.loadTexts:
    hpnicfSnmpExtContextEntry.setStatus("current")


class _HpnicfSnmpExtContextName_Type(SnmpAdminString):
    """Custom type hpnicfSnmpExtContextName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpnicfSnmpExtContextName_Type.__name__ = "SnmpAdminString"
_HpnicfSnmpExtContextName_Object = MibTableColumn
hpnicfSnmpExtContextName = _HpnicfSnmpExtContextName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1, 1),
    _HpnicfSnmpExtContextName_Type()
)
hpnicfSnmpExtContextName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfSnmpExtContextName.setStatus("current")
_HpnicfSnmpExtContextRowStatus_Type = RowStatus
_HpnicfSnmpExtContextRowStatus_Object = MibTableColumn
hpnicfSnmpExtContextRowStatus = _HpnicfSnmpExtContextRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 2, 3, 1, 2),
    _HpnicfSnmpExtContextRowStatus_Type()
)
hpnicfSnmpExtContextRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfSnmpExtContextRowStatus.setStatus("current")
_HpnicfSnmpExtNotifications_ObjectIdentity = ObjectIdentity
hpnicfSnmpExtNotifications = _HpnicfSnmpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 104, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-SNMP-EXT-MIB",
    **{"hpnicfSnmpExt": hpnicfSnmpExt,
       "hpnicfSnmpExtScalarObjects": hpnicfSnmpExtScalarObjects,
       "hpnicfSnmpExtSnmpChannel": hpnicfSnmpExtSnmpChannel,
       "hpnicfSnmpExtReadCommunitySingle": hpnicfSnmpExtReadCommunitySingle,
       "hpnicfSnmpExtWriteCommunitySingle": hpnicfSnmpExtWriteCommunitySingle,
       "hpnicfSnmpExtMaxContextNum": hpnicfSnmpExtMaxContextNum,
       "hpnicfSnmpExtTables": hpnicfSnmpExtTables,
       "hpnicfSnmpExtCommunityTable": hpnicfSnmpExtCommunityTable,
       "hpnicfSnmpExtCommunityEntry": hpnicfSnmpExtCommunityEntry,
       "hpnicfSnmpExtCommunitySecurityLevel": hpnicfSnmpExtCommunitySecurityLevel,
       "hpnicfSnmpExtCommunitySecurityName": hpnicfSnmpExtCommunitySecurityName,
       "hpnicfSnmpExtCommunityName": hpnicfSnmpExtCommunityName,
       "hpnicfSnmpExtCommunityAclNum": hpnicfSnmpExtCommunityAclNum,
       "hpnicfSnmpCommunityExTable": hpnicfSnmpCommunityExTable,
       "hpnicfSnmpCommunityExEntry": hpnicfSnmpCommunityExEntry,
       "hpnicfSnmpCommunityExName": hpnicfSnmpCommunityExName,
       "hpnicfSnmpCommunityExWrite": hpnicfSnmpCommunityExWrite,
       "hpnicfSnmpCommunityExViewName": hpnicfSnmpCommunityExViewName,
       "hpnicfSnmpCommunityExAclNum": hpnicfSnmpCommunityExAclNum,
       "hpnicfSnmpCommunityExRowStatus": hpnicfSnmpCommunityExRowStatus,
       "hpnicfSnmpExtContextTable": hpnicfSnmpExtContextTable,
       "hpnicfSnmpExtContextEntry": hpnicfSnmpExtContextEntry,
       "hpnicfSnmpExtContextName": hpnicfSnmpExtContextName,
       "hpnicfSnmpExtContextRowStatus": hpnicfSnmpExtContextRowStatus,
       "hpnicfSnmpExtNotifications": hpnicfSnmpExtNotifications}
)
