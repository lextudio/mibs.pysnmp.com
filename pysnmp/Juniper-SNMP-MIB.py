# SNMP MIB module (Juniper-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:20 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

juniSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16)
)
juniSnmpMIB.setRevisions(
        ("2008-09-30 06:59",
         "2008-04-03 10:29",
         "2006-09-18 08:09",
         "2006-04-26 13:49",
         "2006-01-01 00:00",
         "2005-06-23 13:49",
         "2005-05-12 21:53",
         "2004-06-23 13:49",
         "2004-01-05 16:09",
         "2003-12-10 15:00",
         "2003-02-05 22:24",
         "2002-11-20 14:40",
         "2002-08-15 20:18",
         "2002-08-14 19:09",
         "2001-11-07 17:09",
         "2001-11-07 15:00",
         "2001-05-08 12:06",
         "2000-08-02 00:00",
         "2000-05-09 00:00",
         "1999-02-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniSnmpCommunityName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class JuniSnmpAccessListName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class JuniSnmpTrapMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class JuniTrapSeverity(Integer32, TextualConvention):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("trapAlert", 1),
          ("trapCritical", 2),
          ("trapDebug", 7),
          ("trapEmergency", 0),
          ("trapError", 3),
          ("trapInformational", 6),
          ("trapNotice", 5),
          ("trapWarning", 4))
    )



class JuniSnmpIntfCompRestrictedMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class JuniSnmpManagementApplicationIndex(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("eventMgr", 1)
    )



# MIB Managed Objects in the order of their OIDs

_JuniSnmpObjects_ObjectIdentity = ObjectIdentity
juniSnmpObjects = _JuniSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1)
)
_JuniSnmpGeneral_ObjectIdentity = ObjectIdentity
juniSnmpGeneral = _JuniSnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1)
)


class _JuniSnmpMaxPduSize_Type(Integer32):
    """Custom type juniSnmpMaxPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 8192),
    )


_JuniSnmpMaxPduSize_Type.__name__ = "Integer32"
_JuniSnmpMaxPduSize_Object = MibScalar
juniSnmpMaxPduSize = _JuniSnmpMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 1),
    _JuniSnmpMaxPduSize_Type()
)
juniSnmpMaxPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpMaxPduSize.setStatus("current")


class _JuniSnmpInterfaceMode_Type(Integer32):
    """Custom type juniSnmpInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compress", 2),
          ("enhanced", 3),
          ("verbose", 1))
    )


_JuniSnmpInterfaceMode_Type.__name__ = "Integer32"
_JuniSnmpInterfaceMode_Object = MibScalar
juniSnmpInterfaceMode = _JuniSnmpInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 2),
    _JuniSnmpInterfaceMode_Type()
)
juniSnmpInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpInterfaceMode.setStatus("obsolete")
_JuniSnmpInterfaceCompress_ObjectIdentity = ObjectIdentity
juniSnmpInterfaceCompress = _JuniSnmpInterfaceCompress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3)
)


class _JuniSnmpIntfCompCompressed_Type(TruthValue):
    """Custom type juniSnmpIntfCompCompressed based on TruthValue"""


_JuniSnmpIntfCompCompressed_Object = MibScalar
juniSnmpIntfCompCompressed = _JuniSnmpIntfCompCompressed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 1),
    _JuniSnmpIntfCompCompressed_Type()
)
juniSnmpIntfCompCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpIntfCompCompressed.setStatus("current")


class _JuniSnmpIntfCompEnhanced_Type(OctetString):
    """Custom type juniSnmpIntfCompEnhanced based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 16),
    )


_JuniSnmpIntfCompEnhanced_Type.__name__ = "OctetString"
_JuniSnmpIntfCompEnhanced_Object = MibScalar
juniSnmpIntfCompEnhanced = _JuniSnmpIntfCompEnhanced_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 2),
    _JuniSnmpIntfCompEnhanced_Type()
)
juniSnmpIntfCompEnhanced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpIntfCompEnhanced.setStatus("current")


class _JuniSnmpIntfCompEnhancedDisplay_Type(OctetString):
    """Custom type juniSnmpIntfCompEnhancedDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_JuniSnmpIntfCompEnhancedDisplay_Type.__name__ = "OctetString"
_JuniSnmpIntfCompEnhancedDisplay_Object = MibScalar
juniSnmpIntfCompEnhancedDisplay = _JuniSnmpIntfCompEnhancedDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 3),
    _JuniSnmpIntfCompEnhancedDisplay_Type()
)
juniSnmpIntfCompEnhancedDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpIntfCompEnhancedDisplay.setStatus("current")
_JuniSnmpIntfCompRestricted_Type = JuniSnmpIntfCompRestrictedMask
_JuniSnmpIntfCompRestricted_Object = MibScalar
juniSnmpIntfCompRestricted = _JuniSnmpIntfCompRestricted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 4),
    _JuniSnmpIntfCompRestricted_Type()
)
juniSnmpIntfCompRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpIntfCompRestricted.setStatus("current")


class _JuniSnmpIntfCompRestrictedDisplay_Type(SnmpAdminString):
    """Custom type juniSnmpIntfCompRestrictedDisplay based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_JuniSnmpIntfCompRestrictedDisplay_Type.__name__ = "SnmpAdminString"
_JuniSnmpIntfCompRestrictedDisplay_Object = MibScalar
juniSnmpIntfCompRestrictedDisplay = _JuniSnmpIntfCompRestrictedDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 5),
    _JuniSnmpIntfCompRestrictedDisplay_Type()
)
juniSnmpIntfCompRestrictedDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpIntfCompRestrictedDisplay.setStatus("current")
_JuniSnmpIntfCompTable_Object = MibTable
juniSnmpIntfCompTable = _JuniSnmpIntfCompTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    juniSnmpIntfCompTable.setStatus("current")
_JuniSnmpIntfCompEntry_Object = MibTableRow
juniSnmpIntfCompEntry = _JuniSnmpIntfCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1)
)
juniSnmpIntfCompEntry.setIndexNames(
    (0, "Juniper-SNMP-MIB", "juniSnmpIntfCompTableType"),
)
if mibBuilder.loadTexts:
    juniSnmpIntfCompEntry.setStatus("current")


class _JuniSnmpIntfCompTableType_Type(Integer32):
    """Custom type juniSnmpIntfCompTableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ifStackTables", 2),
          ("ifTables", 1),
          ("others", 0))
    )


_JuniSnmpIntfCompTableType_Type.__name__ = "Integer32"
_JuniSnmpIntfCompTableType_Object = MibTableColumn
juniSnmpIntfCompTableType = _JuniSnmpIntfCompTableType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 1),
    _JuniSnmpIntfCompTableType_Type()
)
juniSnmpIntfCompTableType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSnmpIntfCompTableType.setStatus("current")


class _JuniSnmpIntfCompEntryCompressed_Type(TruthValue):
    """Custom type juniSnmpIntfCompEntryCompressed based on TruthValue"""


_JuniSnmpIntfCompEntryCompressed_Object = MibTableColumn
juniSnmpIntfCompEntryCompressed = _JuniSnmpIntfCompEntryCompressed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 2),
    _JuniSnmpIntfCompEntryCompressed_Type()
)
juniSnmpIntfCompEntryCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpIntfCompEntryCompressed.setStatus("current")


class _JuniSnmpIntfCompMask_Type(OctetString):
    """Custom type juniSnmpIntfCompMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 16),
    )


_JuniSnmpIntfCompMask_Type.__name__ = "OctetString"
_JuniSnmpIntfCompMask_Object = MibTableColumn
juniSnmpIntfCompMask = _JuniSnmpIntfCompMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 3),
    _JuniSnmpIntfCompMask_Type()
)
juniSnmpIntfCompMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpIntfCompMask.setStatus("current")


class _JuniSnmpIntfCompMaskDisplay_Type(OctetString):
    """Custom type juniSnmpIntfCompMaskDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1000),
    )


_JuniSnmpIntfCompMaskDisplay_Type.__name__ = "OctetString"
_JuniSnmpIntfCompMaskDisplay_Object = MibTableColumn
juniSnmpIntfCompMaskDisplay = _JuniSnmpIntfCompMaskDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 6, 1, 4),
    _JuniSnmpIntfCompMaskDisplay_Type()
)
juniSnmpIntfCompMaskDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpIntfCompMaskDisplay.setStatus("current")


class _JuniSnmpProxyStatus_Type(JuniEnable):
    """Custom type juniSnmpProxyStatus based on JuniEnable"""


_JuniSnmpProxyStatus_Object = MibScalar
juniSnmpProxyStatus = _JuniSnmpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 4),
    _JuniSnmpProxyStatus_Type()
)
juniSnmpProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpProxyStatus.setStatus("current")


class _JuniSnmpAccessPermission_Type(Integer32):
    """Custom type juniSnmpAccessPermission based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAccess", 1),
          ("readAccess", 2),
          ("readWriteAccess", 3))
    )


_JuniSnmpAccessPermission_Type.__name__ = "Integer32"
_JuniSnmpAccessPermission_Object = MibScalar
juniSnmpAccessPermission = _JuniSnmpAccessPermission_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 5),
    _JuniSnmpAccessPermission_Type()
)
juniSnmpAccessPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpAccessPermission.setStatus("current")
_JuniSnmpManagementApplicationTable_Object = MibTable
juniSnmpManagementApplicationTable = _JuniSnmpManagementApplicationTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6)
)
if mibBuilder.loadTexts:
    juniSnmpManagementApplicationTable.setStatus("current")
_JuniSnmpManagementApplicationEntry_Object = MibTableRow
juniSnmpManagementApplicationEntry = _JuniSnmpManagementApplicationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1)
)
juniSnmpManagementApplicationEntry.setIndexNames(
    (0, "Juniper-SNMP-MIB", "juniSnmpManagementApplicationRouterIndex"),
    (0, "Juniper-SNMP-MIB", "juniSnmpManagementApplicationIndex"),
)
if mibBuilder.loadTexts:
    juniSnmpManagementApplicationEntry.setStatus("current")
_JuniSnmpManagementApplicationRouterIndex_Type = Unsigned32
_JuniSnmpManagementApplicationRouterIndex_Object = MibTableColumn
juniSnmpManagementApplicationRouterIndex = _JuniSnmpManagementApplicationRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 1),
    _JuniSnmpManagementApplicationRouterIndex_Type()
)
juniSnmpManagementApplicationRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSnmpManagementApplicationRouterIndex.setStatus("current")
_JuniSnmpManagementApplicationIndex_Type = JuniSnmpManagementApplicationIndex
_JuniSnmpManagementApplicationIndex_Object = MibTableColumn
juniSnmpManagementApplicationIndex = _JuniSnmpManagementApplicationIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 2),
    _JuniSnmpManagementApplicationIndex_Type()
)
juniSnmpManagementApplicationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSnmpManagementApplicationIndex.setStatus("current")
_JuniSnmpManagementApplicationRowStatus_Type = RowStatus
_JuniSnmpManagementApplicationRowStatus_Object = MibTableColumn
juniSnmpManagementApplicationRowStatus = _JuniSnmpManagementApplicationRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 6, 1, 3),
    _JuniSnmpManagementApplicationRowStatus_Type()
)
juniSnmpManagementApplicationRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpManagementApplicationRowStatus.setStatus("current")
_JuniSnmpCommunity_ObjectIdentity = ObjectIdentity
juniSnmpCommunity = _JuniSnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2)
)
_JuniSnmpCommunityTable_Object = MibTable
juniSnmpCommunityTable = _JuniSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniSnmpCommunityTable.setStatus("current")
_JuniSnmpCommunityEntry_Object = MibTableRow
juniSnmpCommunityEntry = _JuniSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1)
)
juniSnmpCommunityEntry.setIndexNames(
    (1, "Juniper-SNMP-MIB", "juniSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    juniSnmpCommunityEntry.setStatus("current")
_JuniSnmpCommunityName_Type = JuniSnmpCommunityName
_JuniSnmpCommunityName_Object = MibTableColumn
juniSnmpCommunityName = _JuniSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 1),
    _JuniSnmpCommunityName_Type()
)
juniSnmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpCommunityName.setStatus("current")
_JuniSnmpCommunityRowStatus_Type = RowStatus
_JuniSnmpCommunityRowStatus_Object = MibTableColumn
juniSnmpCommunityRowStatus = _JuniSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 2),
    _JuniSnmpCommunityRowStatus_Type()
)
juniSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpCommunityRowStatus.setStatus("current")


class _JuniSnmpCommunityPrivilege_Type(Integer32):
    """Custom type juniSnmpCommunityPrivilege based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("readOnly", 1),
          ("readWrite", 2))
    )


_JuniSnmpCommunityPrivilege_Type.__name__ = "Integer32"
_JuniSnmpCommunityPrivilege_Object = MibTableColumn
juniSnmpCommunityPrivilege = _JuniSnmpCommunityPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 3),
    _JuniSnmpCommunityPrivilege_Type()
)
juniSnmpCommunityPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpCommunityPrivilege.setStatus("current")


class _JuniSnmpCommunityAccessList_Type(Integer32):
    """Custom type juniSnmpCommunityAccessList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_JuniSnmpCommunityAccessList_Type.__name__ = "Integer32"
_JuniSnmpCommunityAccessList_Object = MibTableColumn
juniSnmpCommunityAccessList = _JuniSnmpCommunityAccessList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 4),
    _JuniSnmpCommunityAccessList_Type()
)
juniSnmpCommunityAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpCommunityAccessList.setStatus("current")
_JuniSnmpCommunityAccessListName_Type = JuniSnmpAccessListName
_JuniSnmpCommunityAccessListName_Object = MibTableColumn
juniSnmpCommunityAccessListName = _JuniSnmpCommunityAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 5),
    _JuniSnmpCommunityAccessListName_Type()
)
juniSnmpCommunityAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpCommunityAccessListName.setStatus("current")


class _JuniSnmpCommunityView_Type(SnmpAdminString):
    """Custom type juniSnmpCommunityView based on SnmpAdminString"""
    defaultValue = OctetString("user")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_JuniSnmpCommunityView_Type.__name__ = "SnmpAdminString"
_JuniSnmpCommunityView_Object = MibTableColumn
juniSnmpCommunityView = _JuniSnmpCommunityView_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 6),
    _JuniSnmpCommunityView_Type()
)
juniSnmpCommunityView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpCommunityView.setStatus("current")
_JuniSnmpTrap_ObjectIdentity = ObjectIdentity
juniSnmpTrap = _JuniSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3)
)
_JuniSnmpTrapGlobalFilter_Type = JuniSnmpTrapMask
_JuniSnmpTrapGlobalFilter_Object = MibScalar
juniSnmpTrapGlobalFilter = _JuniSnmpTrapGlobalFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 1),
    _JuniSnmpTrapGlobalFilter_Type()
)
juniSnmpTrapGlobalFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpTrapGlobalFilter.setStatus("current")


class _JuniSnmpTrapSource_Type(Integer32):
    """Custom type juniSnmpTrapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniSnmpTrapSource_Type.__name__ = "Integer32"
_JuniSnmpTrapSource_Object = MibScalar
juniSnmpTrapSource = _JuniSnmpTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 2),
    _JuniSnmpTrapSource_Type()
)
juniSnmpTrapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpTrapSource.setStatus("current")
_JuniSnmpTrapHostTable_Object = MibTable
juniSnmpTrapHostTable = _JuniSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniSnmpTrapHostTable.setStatus("current")
_JuniSnmpTrapHostEntry_Object = MibTableRow
juniSnmpTrapHostEntry = _JuniSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1)
)
juniSnmpTrapHostEntry.setIndexNames(
    (0, "Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
)
if mibBuilder.loadTexts:
    juniSnmpTrapHostEntry.setStatus("current")
_JuniSnmpTrapHostIpAddress_Type = IpAddress
_JuniSnmpTrapHostIpAddress_Object = MibTableColumn
juniSnmpTrapHostIpAddress = _JuniSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 1),
    _JuniSnmpTrapHostIpAddress_Type()
)
juniSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostIpAddress.setStatus("current")
_JuniSnmpTrapHostRowStatus_Type = RowStatus
_JuniSnmpTrapHostRowStatus_Object = MibTableColumn
juniSnmpTrapHostRowStatus = _JuniSnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 2),
    _JuniSnmpTrapHostRowStatus_Type()
)
juniSnmpTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostRowStatus.setStatus("current")


class _JuniSnmpTrapHostUdpPort_Type(Integer32):
    """Custom type juniSnmpTrapHostUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniSnmpTrapHostUdpPort_Type.__name__ = "Integer32"
_JuniSnmpTrapHostUdpPort_Object = MibTableColumn
juniSnmpTrapHostUdpPort = _JuniSnmpTrapHostUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 3),
    _JuniSnmpTrapHostUdpPort_Type()
)
juniSnmpTrapHostUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostUdpPort.setStatus("current")
_JuniSnmpTrapHostCommunity_Type = JuniSnmpCommunityName
_JuniSnmpTrapHostCommunity_Object = MibTableColumn
juniSnmpTrapHostCommunity = _JuniSnmpTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 4),
    _JuniSnmpTrapHostCommunity_Type()
)
juniSnmpTrapHostCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostCommunity.setStatus("current")


class _JuniSnmpTrapHostProtocolVersion_Type(Integer32):
    """Custom type juniSnmpTrapHostProtocolVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 0),
          ("v2c", 1),
          ("v3", 2))
    )


_JuniSnmpTrapHostProtocolVersion_Type.__name__ = "Integer32"
_JuniSnmpTrapHostProtocolVersion_Object = MibTableColumn
juniSnmpTrapHostProtocolVersion = _JuniSnmpTrapHostProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 5),
    _JuniSnmpTrapHostProtocolVersion_Type()
)
juniSnmpTrapHostProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostProtocolVersion.setStatus("current")
_JuniSnmpTrapHostFilter_Type = JuniSnmpTrapMask
_JuniSnmpTrapHostFilter_Object = MibTableColumn
juniSnmpTrapHostFilter = _JuniSnmpTrapHostFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 6),
    _JuniSnmpTrapHostFilter_Type()
)
juniSnmpTrapHostFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostFilter.setStatus("current")
_JuniSnmpTrapHostSends_Type = Counter32
_JuniSnmpTrapHostSends_Object = MibTableColumn
juniSnmpTrapHostSends = _JuniSnmpTrapHostSends_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 7),
    _JuniSnmpTrapHostSends_Type()
)
juniSnmpTrapHostSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostSends.setStatus("current")
_JuniSnmpTrapHostDiscards_Type = Counter32
_JuniSnmpTrapHostDiscards_Object = MibTableColumn
juniSnmpTrapHostDiscards = _JuniSnmpTrapHostDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 8),
    _JuniSnmpTrapHostDiscards_Type()
)
juniSnmpTrapHostDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostDiscards.setStatus("current")
_JuniSnmpTrapHostSeverityFilter_Type = JuniTrapSeverity
_JuniSnmpTrapHostSeverityFilter_Object = MibTableColumn
juniSnmpTrapHostSeverityFilter = _JuniSnmpTrapHostSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 9),
    _JuniSnmpTrapHostSeverityFilter_Type()
)
juniSnmpTrapHostSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostSeverityFilter.setStatus("current")


class _JuniSnmpTrapHostPingTimeOut_Type(Integer32):
    """Custom type juniSnmpTrapHostPingTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_JuniSnmpTrapHostPingTimeOut_Type.__name__ = "Integer32"
_JuniSnmpTrapHostPingTimeOut_Object = MibTableColumn
juniSnmpTrapHostPingTimeOut = _JuniSnmpTrapHostPingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 10),
    _JuniSnmpTrapHostPingTimeOut_Type()
)
juniSnmpTrapHostPingTimeOut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostPingTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    juniSnmpTrapHostPingTimeOut.setUnits("Minutes")


class _JuniSnmpTrapHostIncludeLogVarbinds_Type(TruthValue):
    """Custom type juniSnmpTrapHostIncludeLogVarbinds based on TruthValue"""


_JuniSnmpTrapHostIncludeLogVarbinds_Object = MibTableColumn
juniSnmpTrapHostIncludeLogVarbinds = _JuniSnmpTrapHostIncludeLogVarbinds_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 11),
    _JuniSnmpTrapHostIncludeLogVarbinds_Type()
)
juniSnmpTrapHostIncludeLogVarbinds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostIncludeLogVarbinds.setStatus("current")


class _JuniSnmpTrapHostQueueSize_Type(Integer32):
    """Custom type juniSnmpTrapHostQueueSize based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 2147483647),
    )


_JuniSnmpTrapHostQueueSize_Type.__name__ = "Integer32"
_JuniSnmpTrapHostQueueSize_Object = MibTableColumn
juniSnmpTrapHostQueueSize = _JuniSnmpTrapHostQueueSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 12),
    _JuniSnmpTrapHostQueueSize_Type()
)
juniSnmpTrapHostQueueSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostQueueSize.setStatus("current")


class _JuniSnmpTrapHostQueueDrainRate_Type(Integer32):
    """Custom type juniSnmpTrapHostQueueDrainRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniSnmpTrapHostQueueDrainRate_Type.__name__ = "Integer32"
_JuniSnmpTrapHostQueueDrainRate_Object = MibTableColumn
juniSnmpTrapHostQueueDrainRate = _JuniSnmpTrapHostQueueDrainRate_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 13),
    _JuniSnmpTrapHostQueueDrainRate_Type()
)
juniSnmpTrapHostQueueDrainRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostQueueDrainRate.setStatus("current")


class _JuniSnmpTrapHostQueueFull_Type(Integer32):
    """Custom type juniSnmpTrapHostQueueFull based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dropFirstIn", 1),
          ("dropLastIn", 0))
    )


_JuniSnmpTrapHostQueueFull_Type.__name__ = "Integer32"
_JuniSnmpTrapHostQueueFull_Object = MibTableColumn
juniSnmpTrapHostQueueFull = _JuniSnmpTrapHostQueueFull_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 14),
    _JuniSnmpTrapHostQueueFull_Type()
)
juniSnmpTrapHostQueueFull.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniSnmpTrapHostQueueFull.setStatus("current")
_JuniSnmpTrapHostBadEncodingDiscards_Type = Counter32
_JuniSnmpTrapHostBadEncodingDiscards_Object = MibTableColumn
juniSnmpTrapHostBadEncodingDiscards = _JuniSnmpTrapHostBadEncodingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 15),
    _JuniSnmpTrapHostBadEncodingDiscards_Type()
)
juniSnmpTrapHostBadEncodingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostBadEncodingDiscards.setStatus("current")
_JuniSnmpTrapHostQueueFullDiscards_Type = Counter32
_JuniSnmpTrapHostQueueFullDiscards_Object = MibTableColumn
juniSnmpTrapHostQueueFullDiscards = _JuniSnmpTrapHostQueueFullDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 16),
    _JuniSnmpTrapHostQueueFullDiscards_Type()
)
juniSnmpTrapHostQueueFullDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostQueueFullDiscards.setStatus("current")
_JuniSnmpTrapHostNoResponseDiscards_Type = Counter32
_JuniSnmpTrapHostNoResponseDiscards_Object = MibTableColumn
juniSnmpTrapHostNoResponseDiscards = _JuniSnmpTrapHostNoResponseDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 17),
    _JuniSnmpTrapHostNoResponseDiscards_Type()
)
juniSnmpTrapHostNoResponseDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapHostNoResponseDiscards.setStatus("current")
_JuniSnmpTrapProxy_Type = TruthValue
_JuniSnmpTrapProxy_Object = MibScalar
juniSnmpTrapProxy = _JuniSnmpTrapProxy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 4),
    _JuniSnmpTrapProxy_Type()
)
juniSnmpTrapProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpTrapProxy.setStatus("current")
_JuniSnmpTrapTrapSeverity_Type = JuniTrapSeverity
_JuniSnmpTrapTrapSeverity_Object = MibScalar
juniSnmpTrapTrapSeverity = _JuniSnmpTrapTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 5),
    _JuniSnmpTrapTrapSeverity_Type()
)
juniSnmpTrapTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSnmpTrapTrapSeverity.setStatus("current")
_JuniSnmpTrapGlobalDiscards_Type = Counter32
_JuniSnmpTrapGlobalDiscards_Object = MibScalar
juniSnmpTrapGlobalDiscards = _JuniSnmpTrapGlobalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 6),
    _JuniSnmpTrapGlobalDiscards_Type()
)
juniSnmpTrapGlobalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapGlobalDiscards.setStatus("current")
_JuniSnmpTrapGlobalSeverityFilter_Type = JuniTrapSeverity
_JuniSnmpTrapGlobalSeverityFilter_Object = MibScalar
juniSnmpTrapGlobalSeverityFilter = _JuniSnmpTrapGlobalSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 7),
    _JuniSnmpTrapGlobalSeverityFilter_Type()
)
juniSnmpTrapGlobalSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpTrapGlobalSeverityFilter.setStatus("current")
_JuniSnmpTrapTotalTrapsReceived_Type = Counter32
_JuniSnmpTrapTotalTrapsReceived_Object = MibScalar
juniSnmpTrapTotalTrapsReceived = _JuniSnmpTrapTotalTrapsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 8),
    _JuniSnmpTrapTotalTrapsReceived_Type()
)
juniSnmpTrapTotalTrapsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapTotalTrapsReceived.setStatus("current")
_JuniSnmpTrapLocalTrapsSubmitted_Type = Counter32
_JuniSnmpTrapLocalTrapsSubmitted_Object = MibScalar
juniSnmpTrapLocalTrapsSubmitted = _JuniSnmpTrapLocalTrapsSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 9),
    _JuniSnmpTrapLocalTrapsSubmitted_Type()
)
juniSnmpTrapLocalTrapsSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapLocalTrapsSubmitted.setStatus("current")
_JuniSnmpTrapProxyTrapsSubmitted_Type = Counter32
_JuniSnmpTrapProxyTrapsSubmitted_Object = MibScalar
juniSnmpTrapProxyTrapsSubmitted = _JuniSnmpTrapProxyTrapsSubmitted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 10),
    _JuniSnmpTrapProxyTrapsSubmitted_Type()
)
juniSnmpTrapProxyTrapsSubmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapProxyTrapsSubmitted.setStatus("current")
_JuniSnmpTrapTotalTrapsDiscarded_Type = Counter32
_JuniSnmpTrapTotalTrapsDiscarded_Object = MibScalar
juniSnmpTrapTotalTrapsDiscarded = _JuniSnmpTrapTotalTrapsDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 11),
    _JuniSnmpTrapTotalTrapsDiscarded_Type()
)
juniSnmpTrapTotalTrapsDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapTotalTrapsDiscarded.setStatus("current")
_JuniSnmpTrapNoMemoryDiscards_Type = Counter32
_JuniSnmpTrapNoMemoryDiscards_Object = MibScalar
juniSnmpTrapNoMemoryDiscards = _JuniSnmpTrapNoMemoryDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 12),
    _JuniSnmpTrapNoMemoryDiscards_Type()
)
juniSnmpTrapNoMemoryDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapNoMemoryDiscards.setStatus("current")
_JuniSnmpTrapNoQueueResourceDiscards_Type = Counter32
_JuniSnmpTrapNoQueueResourceDiscards_Object = MibScalar
juniSnmpTrapNoQueueResourceDiscards = _JuniSnmpTrapNoQueueResourceDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 13),
    _JuniSnmpTrapNoQueueResourceDiscards_Type()
)
juniSnmpTrapNoQueueResourceDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapNoQueueResourceDiscards.setStatus("current")
_JuniSnmpTrapAgentSnmpNotAbleDiscards_Type = Counter32
_JuniSnmpTrapAgentSnmpNotAbleDiscards_Object = MibScalar
juniSnmpTrapAgentSnmpNotAbleDiscards = _JuniSnmpTrapAgentSnmpNotAbleDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 14),
    _JuniSnmpTrapAgentSnmpNotAbleDiscards_Type()
)
juniSnmpTrapAgentSnmpNotAbleDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapAgentSnmpNotAbleDiscards.setStatus("current")
_JuniSnmpTrapTotalTrapsOut_Type = Counter32
_JuniSnmpTrapTotalTrapsOut_Object = MibScalar
juniSnmpTrapTotalTrapsOut = _JuniSnmpTrapTotalTrapsOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 15),
    _JuniSnmpTrapTotalTrapsOut_Type()
)
juniSnmpTrapTotalTrapsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapTotalTrapsOut.setStatus("current")
_JuniSnmpTrapTotalProxyOut_Type = Counter32
_JuniSnmpTrapTotalProxyOut_Object = MibScalar
juniSnmpTrapTotalProxyOut = _JuniSnmpTrapTotalProxyOut_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 16),
    _JuniSnmpTrapTotalProxyOut_Type()
)
juniSnmpTrapTotalProxyOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniSnmpTrapTotalProxyOut.setStatus("current")
_JuniSnmpTrapSeverityFilterTable_Object = MibTable
juniSnmpTrapSeverityFilterTable = _JuniSnmpTrapSeverityFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17)
)
if mibBuilder.loadTexts:
    juniSnmpTrapSeverityFilterTable.setStatus("current")
_JuniSnmpTrapSeverityFilterEntry_Object = MibTableRow
juniSnmpTrapSeverityFilterEntry = _JuniSnmpTrapSeverityFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1)
)
juniSnmpTrapSeverityFilterEntry.setIndexNames(
    (0, "Juniper-SNMP-MIB", "juniSnmpTrapCategory"),
)
if mibBuilder.loadTexts:
    juniSnmpTrapSeverityFilterEntry.setStatus("current")


class _JuniSnmpTrapCategory_Type(Integer32):
    """Custom type juniSnmpTrapCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_JuniSnmpTrapCategory_Type.__name__ = "Integer32"
_JuniSnmpTrapCategory_Object = MibTableColumn
juniSnmpTrapCategory = _JuniSnmpTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1, 1),
    _JuniSnmpTrapCategory_Type()
)
juniSnmpTrapCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniSnmpTrapCategory.setStatus("current")
_JuniSnmpTrapSeverityFilter_Type = JuniTrapSeverity
_JuniSnmpTrapSeverityFilter_Object = MibTableColumn
juniSnmpTrapSeverityFilter = _JuniSnmpTrapSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 17, 1, 2),
    _JuniSnmpTrapSeverityFilter_Type()
)
juniSnmpTrapSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniSnmpTrapSeverityFilter.setStatus("current")
_JuniSnmpAuthFailId_ObjectIdentity = ObjectIdentity
juniSnmpAuthFailId = _JuniSnmpAuthFailId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4)
)
_JuniSnmpAuthFailIdIpAddress_Type = IpAddress
_JuniSnmpAuthFailIdIpAddress_Object = MibScalar
juniSnmpAuthFailIdIpAddress = _JuniSnmpAuthFailIdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 1),
    _JuniSnmpAuthFailIdIpAddress_Type()
)
juniSnmpAuthFailIdIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSnmpAuthFailIdIpAddress.setStatus("current")
_JuniSnmpAuthFailIdUdpPort_Type = Integer32
_JuniSnmpAuthFailIdUdpPort_Object = MibScalar
juniSnmpAuthFailIdUdpPort = _JuniSnmpAuthFailIdUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 2),
    _JuniSnmpAuthFailIdUdpPort_Type()
)
juniSnmpAuthFailIdUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSnmpAuthFailIdUdpPort.setStatus("current")
_JuniSnmpAuthFailIdCommunity_Type = OctetString
_JuniSnmpAuthFailIdCommunity_Object = MibScalar
juniSnmpAuthFailIdCommunity = _JuniSnmpAuthFailIdCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 3),
    _JuniSnmpAuthFailIdCommunity_Type()
)
juniSnmpAuthFailIdCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSnmpAuthFailIdCommunity.setStatus("current")


class _JuniSnmpAuthFailIdReason_Type(Integer32):
    """Custom type juniSnmpAuthFailIdReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("badCommmunityUse", 2),
          ("badCommunityName", 1),
          ("hostDenied", 3),
          ("other", 0))
    )


_JuniSnmpAuthFailIdReason_Type.__name__ = "Integer32"
_JuniSnmpAuthFailIdReason_Object = MibScalar
juniSnmpAuthFailIdReason = _JuniSnmpAuthFailIdReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 4),
    _JuniSnmpAuthFailIdReason_Type()
)
juniSnmpAuthFailIdReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    juniSnmpAuthFailIdReason.setStatus("current")
_JuniSnmpConformance_ObjectIdentity = ObjectIdentity
juniSnmpConformance = _JuniSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2)
)
_JuniSnmpCompliances_ObjectIdentity = ObjectIdentity
juniSnmpCompliances = _JuniSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1)
)
_JuniSnmpGroups_ObjectIdentity = ObjectIdentity
juniSnmpGroups = _JuniSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2)
)

# Managed Objects groups

juniSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 1)
)
juniSnmpGroup.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    juniSnmpGroup.setStatus("obsolete")

juniSnmpAuthFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 2)
)
juniSnmpAuthFailGroup.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpAuthFailIdIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpAuthFailIdReason"))
)
if mibBuilder.loadTexts:
    juniSnmpAuthFailGroup.setStatus("current")

juniSnmpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 3)
)
juniSnmpGroup2.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityView"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    juniSnmpGroup2.setStatus("obsolete")

juniSnmpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 4)
)
juniSnmpGroup3.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpInterfaceMode"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityView"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    juniSnmpGroup3.setStatus("obsolete")

juniSnmpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 5)
)
juniSnmpGeneralGroup.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"))
)
if mibBuilder.loadTexts:
    juniSnmpGeneralGroup.setStatus("obsolete")

juniSnmpAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 6)
)
juniSnmpAccessGroup.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpCommunityName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityPrivilege"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessList"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityAccessListName"),
        ("Juniper-SNMP-MIB", "juniSnmpCommunityView"))
)
if mibBuilder.loadTexts:
    juniSnmpAccessGroup.setStatus("current")

juniSnmpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 7)
)
juniSnmpTrapGroup.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"))
)
if mibBuilder.loadTexts:
    juniSnmpTrapGroup.setStatus("obsolete")

juniSnmpGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 8)
)
juniSnmpGeneralGroup2.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"))
)
if mibBuilder.loadTexts:
    juniSnmpGeneralGroup2.setStatus("obsolete")

juniSnmpTrapGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 9)
)
juniSnmpTrapGroup2.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostPingTimeOut"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIncludeLogVarbinds"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueSize"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueDrainRate"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFull"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostBadEncodingDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFullDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostNoResponseDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsReceived"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapLocalTrapsSubmitted"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxyTrapsSubmitted"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsDiscarded"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapNoMemoryDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapNoQueueResourceDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapAgentSnmpNotAbleDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsOut"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalProxyOut"))
)
if mibBuilder.loadTexts:
    juniSnmpTrapGroup2.setStatus("obsolete")

juniSnmpGeneralGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 10)
)
juniSnmpGeneralGroup3.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpAccessPermission"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpManagementApplicationRowStatus"))
)
if mibBuilder.loadTexts:
    juniSnmpGeneralGroup3.setStatus("obsolete")

juniSnmpTrapGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 11)
)
juniSnmpTrapGroup3.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpTrapGlobalFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSource"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxy"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIpAddress"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostUdpPort"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostCommunity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostProtocolVersion"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSends"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostSeverityFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostPingTimeOut"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostIncludeLogVarbinds"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueSize"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueDrainRate"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFull"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostBadEncodingDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostQueueFullDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapHostNoResponseDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTrapSeverity"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapGlobalSeverityFilter"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsReceived"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapLocalTrapsSubmitted"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapProxyTrapsSubmitted"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsDiscarded"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapNoMemoryDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapNoQueueResourceDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapAgentSnmpNotAbleDiscards"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalTrapsOut"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapTotalProxyOut"),
        ("Juniper-SNMP-MIB", "juniSnmpTrapSeverityFilter"))
)
if mibBuilder.loadTexts:
    juniSnmpTrapGroup3.setStatus("current")

juniSnmpGeneralGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 12)
)
juniSnmpGeneralGroup4.setObjects(
      *(("Juniper-SNMP-MIB", "juniSnmpMaxPduSize"),
        ("Juniper-SNMP-MIB", "juniSnmpProxyStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpAccessPermission"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompCompressed"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhanced"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEnhancedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestricted"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompRestrictedDisplay"),
        ("Juniper-SNMP-MIB", "juniSnmpManagementApplicationRowStatus"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompEntryCompressed"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompMask"),
        ("Juniper-SNMP-MIB", "juniSnmpIntfCompMaskDisplay"))
)
if mibBuilder.loadTexts:
    juniSnmpGeneralGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance.setStatus(
        "obsolete"
    )

juniSnmpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance2.setStatus(
        "obsolete"
    )

juniSnmpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 3)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance3.setStatus(
        "obsolete"
    )

juniSnmpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 4)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance4.setStatus(
        "obsolete"
    )

juniSnmpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 5)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance5.setStatus(
        "obsolete"
    )

juniSnmpCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 6)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance6.setStatus(
        "obsolete"
    )

juniSnmpCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 7)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance7.setStatus(
        "obsolete"
    )

juniSnmpCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 8)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance8.setStatus(
        "obsolete"
    )

juniSnmpCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 9)
)
if mibBuilder.loadTexts:
    juniSnmpCompliance9.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-SNMP-MIB",
    **{"JuniSnmpCommunityName": JuniSnmpCommunityName,
       "JuniSnmpAccessListName": JuniSnmpAccessListName,
       "JuniSnmpTrapMask": JuniSnmpTrapMask,
       "JuniTrapSeverity": JuniTrapSeverity,
       "JuniSnmpIntfCompRestrictedMask": JuniSnmpIntfCompRestrictedMask,
       "JuniSnmpManagementApplicationIndex": JuniSnmpManagementApplicationIndex,
       "juniSnmpMIB": juniSnmpMIB,
       "juniSnmpObjects": juniSnmpObjects,
       "juniSnmpGeneral": juniSnmpGeneral,
       "juniSnmpMaxPduSize": juniSnmpMaxPduSize,
       "juniSnmpInterfaceMode": juniSnmpInterfaceMode,
       "juniSnmpInterfaceCompress": juniSnmpInterfaceCompress,
       "juniSnmpIntfCompCompressed": juniSnmpIntfCompCompressed,
       "juniSnmpIntfCompEnhanced": juniSnmpIntfCompEnhanced,
       "juniSnmpIntfCompEnhancedDisplay": juniSnmpIntfCompEnhancedDisplay,
       "juniSnmpIntfCompRestricted": juniSnmpIntfCompRestricted,
       "juniSnmpIntfCompRestrictedDisplay": juniSnmpIntfCompRestrictedDisplay,
       "juniSnmpIntfCompTable": juniSnmpIntfCompTable,
       "juniSnmpIntfCompEntry": juniSnmpIntfCompEntry,
       "juniSnmpIntfCompTableType": juniSnmpIntfCompTableType,
       "juniSnmpIntfCompEntryCompressed": juniSnmpIntfCompEntryCompressed,
       "juniSnmpIntfCompMask": juniSnmpIntfCompMask,
       "juniSnmpIntfCompMaskDisplay": juniSnmpIntfCompMaskDisplay,
       "juniSnmpProxyStatus": juniSnmpProxyStatus,
       "juniSnmpAccessPermission": juniSnmpAccessPermission,
       "juniSnmpManagementApplicationTable": juniSnmpManagementApplicationTable,
       "juniSnmpManagementApplicationEntry": juniSnmpManagementApplicationEntry,
       "juniSnmpManagementApplicationRouterIndex": juniSnmpManagementApplicationRouterIndex,
       "juniSnmpManagementApplicationIndex": juniSnmpManagementApplicationIndex,
       "juniSnmpManagementApplicationRowStatus": juniSnmpManagementApplicationRowStatus,
       "juniSnmpCommunity": juniSnmpCommunity,
       "juniSnmpCommunityTable": juniSnmpCommunityTable,
       "juniSnmpCommunityEntry": juniSnmpCommunityEntry,
       "juniSnmpCommunityName": juniSnmpCommunityName,
       "juniSnmpCommunityRowStatus": juniSnmpCommunityRowStatus,
       "juniSnmpCommunityPrivilege": juniSnmpCommunityPrivilege,
       "juniSnmpCommunityAccessList": juniSnmpCommunityAccessList,
       "juniSnmpCommunityAccessListName": juniSnmpCommunityAccessListName,
       "juniSnmpCommunityView": juniSnmpCommunityView,
       "juniSnmpTrap": juniSnmpTrap,
       "juniSnmpTrapGlobalFilter": juniSnmpTrapGlobalFilter,
       "juniSnmpTrapSource": juniSnmpTrapSource,
       "juniSnmpTrapHostTable": juniSnmpTrapHostTable,
       "juniSnmpTrapHostEntry": juniSnmpTrapHostEntry,
       "juniSnmpTrapHostIpAddress": juniSnmpTrapHostIpAddress,
       "juniSnmpTrapHostRowStatus": juniSnmpTrapHostRowStatus,
       "juniSnmpTrapHostUdpPort": juniSnmpTrapHostUdpPort,
       "juniSnmpTrapHostCommunity": juniSnmpTrapHostCommunity,
       "juniSnmpTrapHostProtocolVersion": juniSnmpTrapHostProtocolVersion,
       "juniSnmpTrapHostFilter": juniSnmpTrapHostFilter,
       "juniSnmpTrapHostSends": juniSnmpTrapHostSends,
       "juniSnmpTrapHostDiscards": juniSnmpTrapHostDiscards,
       "juniSnmpTrapHostSeverityFilter": juniSnmpTrapHostSeverityFilter,
       "juniSnmpTrapHostPingTimeOut": juniSnmpTrapHostPingTimeOut,
       "juniSnmpTrapHostIncludeLogVarbinds": juniSnmpTrapHostIncludeLogVarbinds,
       "juniSnmpTrapHostQueueSize": juniSnmpTrapHostQueueSize,
       "juniSnmpTrapHostQueueDrainRate": juniSnmpTrapHostQueueDrainRate,
       "juniSnmpTrapHostQueueFull": juniSnmpTrapHostQueueFull,
       "juniSnmpTrapHostBadEncodingDiscards": juniSnmpTrapHostBadEncodingDiscards,
       "juniSnmpTrapHostQueueFullDiscards": juniSnmpTrapHostQueueFullDiscards,
       "juniSnmpTrapHostNoResponseDiscards": juniSnmpTrapHostNoResponseDiscards,
       "juniSnmpTrapProxy": juniSnmpTrapProxy,
       "juniSnmpTrapTrapSeverity": juniSnmpTrapTrapSeverity,
       "juniSnmpTrapGlobalDiscards": juniSnmpTrapGlobalDiscards,
       "juniSnmpTrapGlobalSeverityFilter": juniSnmpTrapGlobalSeverityFilter,
       "juniSnmpTrapTotalTrapsReceived": juniSnmpTrapTotalTrapsReceived,
       "juniSnmpTrapLocalTrapsSubmitted": juniSnmpTrapLocalTrapsSubmitted,
       "juniSnmpTrapProxyTrapsSubmitted": juniSnmpTrapProxyTrapsSubmitted,
       "juniSnmpTrapTotalTrapsDiscarded": juniSnmpTrapTotalTrapsDiscarded,
       "juniSnmpTrapNoMemoryDiscards": juniSnmpTrapNoMemoryDiscards,
       "juniSnmpTrapNoQueueResourceDiscards": juniSnmpTrapNoQueueResourceDiscards,
       "juniSnmpTrapAgentSnmpNotAbleDiscards": juniSnmpTrapAgentSnmpNotAbleDiscards,
       "juniSnmpTrapTotalTrapsOut": juniSnmpTrapTotalTrapsOut,
       "juniSnmpTrapTotalProxyOut": juniSnmpTrapTotalProxyOut,
       "juniSnmpTrapSeverityFilterTable": juniSnmpTrapSeverityFilterTable,
       "juniSnmpTrapSeverityFilterEntry": juniSnmpTrapSeverityFilterEntry,
       "juniSnmpTrapCategory": juniSnmpTrapCategory,
       "juniSnmpTrapSeverityFilter": juniSnmpTrapSeverityFilter,
       "juniSnmpAuthFailId": juniSnmpAuthFailId,
       "juniSnmpAuthFailIdIpAddress": juniSnmpAuthFailIdIpAddress,
       "juniSnmpAuthFailIdUdpPort": juniSnmpAuthFailIdUdpPort,
       "juniSnmpAuthFailIdCommunity": juniSnmpAuthFailIdCommunity,
       "juniSnmpAuthFailIdReason": juniSnmpAuthFailIdReason,
       "juniSnmpConformance": juniSnmpConformance,
       "juniSnmpCompliances": juniSnmpCompliances,
       "juniSnmpCompliance": juniSnmpCompliance,
       "juniSnmpCompliance2": juniSnmpCompliance2,
       "juniSnmpCompliance3": juniSnmpCompliance3,
       "juniSnmpCompliance4": juniSnmpCompliance4,
       "juniSnmpCompliance5": juniSnmpCompliance5,
       "juniSnmpCompliance6": juniSnmpCompliance6,
       "juniSnmpCompliance7": juniSnmpCompliance7,
       "juniSnmpCompliance8": juniSnmpCompliance8,
       "juniSnmpCompliance9": juniSnmpCompliance9,
       "juniSnmpGroups": juniSnmpGroups,
       "juniSnmpGroup": juniSnmpGroup,
       "juniSnmpAuthFailGroup": juniSnmpAuthFailGroup,
       "juniSnmpGroup2": juniSnmpGroup2,
       "juniSnmpGroup3": juniSnmpGroup3,
       "juniSnmpGeneralGroup": juniSnmpGeneralGroup,
       "juniSnmpAccessGroup": juniSnmpAccessGroup,
       "juniSnmpTrapGroup": juniSnmpTrapGroup,
       "juniSnmpGeneralGroup2": juniSnmpGeneralGroup2,
       "juniSnmpTrapGroup2": juniSnmpTrapGroup2,
       "juniSnmpGeneralGroup3": juniSnmpGeneralGroup3,
       "juniSnmpTrapGroup3": juniSnmpTrapGroup3,
       "juniSnmpGeneralGroup4": juniSnmpGeneralGroup4}
)
