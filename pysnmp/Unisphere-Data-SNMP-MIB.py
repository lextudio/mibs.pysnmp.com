# SNMP MIB module (Unisphere-Data-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SNMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:37 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdSnmpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16)
)
usdSnmpMIB.setRevisions(
        ("2002-08-15 20:18",
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



class UsdSnmpCommunityName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )



class UsdSnmpAccessListName(OctetString, TextualConvention):
    status = "current"
    displayHint = "31a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



class UsdSnmpTrapMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class UsdTrapSeverity(Integer32, TextualConvention):
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



class UsdSnmpIntfCompRestrictedMask(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



# MIB Managed Objects in the order of their OIDs

_UsdSnmpObjects_ObjectIdentity = ObjectIdentity
usdSnmpObjects = _UsdSnmpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1)
)
_UsdSnmpGeneral_ObjectIdentity = ObjectIdentity
usdSnmpGeneral = _UsdSnmpGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1)
)


class _UsdSnmpMaxPduSize_Type(Integer32):
    """Custom type usdSnmpMaxPduSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(484, 8192),
    )


_UsdSnmpMaxPduSize_Type.__name__ = "Integer32"
_UsdSnmpMaxPduSize_Object = MibScalar
usdSnmpMaxPduSize = _UsdSnmpMaxPduSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 1),
    _UsdSnmpMaxPduSize_Type()
)
usdSnmpMaxPduSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpMaxPduSize.setStatus("current")


class _UsdSnmpInterfaceMode_Type(Integer32):
    """Custom type usdSnmpInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("usdSnmpInterfaceModeCompress", 2),
          ("usdSnmpInterfaceModeEnhanced", 3),
          ("usdSnmpInterfaceModeVerbose", 1))
    )


_UsdSnmpInterfaceMode_Type.__name__ = "Integer32"
_UsdSnmpInterfaceMode_Object = MibScalar
usdSnmpInterfaceMode = _UsdSnmpInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 2),
    _UsdSnmpInterfaceMode_Type()
)
usdSnmpInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpInterfaceMode.setStatus("obsolete")
_UsdSnmpInterfaceCompress_ObjectIdentity = ObjectIdentity
usdSnmpInterfaceCompress = _UsdSnmpInterfaceCompress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3)
)


class _UsdSnmpIntfCompCompressed_Type(TruthValue):
    """Custom type usdSnmpIntfCompCompressed based on TruthValue"""


_UsdSnmpIntfCompCompressed_Object = MibScalar
usdSnmpIntfCompCompressed = _UsdSnmpIntfCompCompressed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 1),
    _UsdSnmpIntfCompCompressed_Type()
)
usdSnmpIntfCompCompressed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpIntfCompCompressed.setStatus("current")


class _UsdSnmpIntfCompEnhanced_Type(OctetString):
    """Custom type usdSnmpIntfCompEnhanced based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 16),
    )


_UsdSnmpIntfCompEnhanced_Type.__name__ = "OctetString"
_UsdSnmpIntfCompEnhanced_Object = MibScalar
usdSnmpIntfCompEnhanced = _UsdSnmpIntfCompEnhanced_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 2),
    _UsdSnmpIntfCompEnhanced_Type()
)
usdSnmpIntfCompEnhanced.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpIntfCompEnhanced.setStatus("current")


class _UsdSnmpIntfCompEnhancedDisplay_Type(OctetString):
    """Custom type usdSnmpIntfCompEnhancedDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1000),
    )


_UsdSnmpIntfCompEnhancedDisplay_Type.__name__ = "OctetString"
_UsdSnmpIntfCompEnhancedDisplay_Object = MibScalar
usdSnmpIntfCompEnhancedDisplay = _UsdSnmpIntfCompEnhancedDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 3),
    _UsdSnmpIntfCompEnhancedDisplay_Type()
)
usdSnmpIntfCompEnhancedDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpIntfCompEnhancedDisplay.setStatus("current")
_UsdSnmpIntfCompRestricted_Type = UsdSnmpIntfCompRestrictedMask
_UsdSnmpIntfCompRestricted_Object = MibScalar
usdSnmpIntfCompRestricted = _UsdSnmpIntfCompRestricted_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 4),
    _UsdSnmpIntfCompRestricted_Type()
)
usdSnmpIntfCompRestricted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpIntfCompRestricted.setStatus("current")


class _UsdSnmpIntfCompRestrictedDisplay_Type(OctetString):
    """Custom type usdSnmpIntfCompRestrictedDisplay based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_UsdSnmpIntfCompRestrictedDisplay_Type.__name__ = "OctetString"
_UsdSnmpIntfCompRestrictedDisplay_Object = MibScalar
usdSnmpIntfCompRestrictedDisplay = _UsdSnmpIntfCompRestrictedDisplay_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 3, 5),
    _UsdSnmpIntfCompRestrictedDisplay_Type()
)
usdSnmpIntfCompRestrictedDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpIntfCompRestrictedDisplay.setStatus("current")


class _UsdSnmpProxyStatus_Type(UsdEnable):
    """Custom type usdSnmpProxyStatus based on UsdEnable"""


_UsdSnmpProxyStatus_Object = MibScalar
usdSnmpProxyStatus = _UsdSnmpProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 1, 4),
    _UsdSnmpProxyStatus_Type()
)
usdSnmpProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpProxyStatus.setStatus("current")
_UsdSnmpCommunity_ObjectIdentity = ObjectIdentity
usdSnmpCommunity = _UsdSnmpCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2)
)
_UsdSnmpCommunityTable_Object = MibTable
usdSnmpCommunityTable = _UsdSnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdSnmpCommunityTable.setStatus("current")
_UsdSnmpCommunityEntry_Object = MibTableRow
usdSnmpCommunityEntry = _UsdSnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1)
)
usdSnmpCommunityEntry.setIndexNames(
    (1, "Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"),
)
if mibBuilder.loadTexts:
    usdSnmpCommunityEntry.setStatus("current")
_UsdSnmpCommunityName_Type = UsdSnmpCommunityName
_UsdSnmpCommunityName_Object = MibTableColumn
usdSnmpCommunityName = _UsdSnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 1),
    _UsdSnmpCommunityName_Type()
)
usdSnmpCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpCommunityName.setStatus("current")
_UsdSnmpCommunityRowStatus_Type = RowStatus
_UsdSnmpCommunityRowStatus_Object = MibTableColumn
usdSnmpCommunityRowStatus = _UsdSnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 2),
    _UsdSnmpCommunityRowStatus_Type()
)
usdSnmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpCommunityRowStatus.setStatus("current")


class _UsdSnmpCommunityPrivilege_Type(Integer32):
    """Custom type usdSnmpCommunityPrivilege based on Integer32"""
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


_UsdSnmpCommunityPrivilege_Type.__name__ = "Integer32"
_UsdSnmpCommunityPrivilege_Object = MibTableColumn
usdSnmpCommunityPrivilege = _UsdSnmpCommunityPrivilege_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 3),
    _UsdSnmpCommunityPrivilege_Type()
)
usdSnmpCommunityPrivilege.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpCommunityPrivilege.setStatus("current")


class _UsdSnmpCommunityAccessList_Type(Integer32):
    """Custom type usdSnmpCommunityAccessList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UsdSnmpCommunityAccessList_Type.__name__ = "Integer32"
_UsdSnmpCommunityAccessList_Object = MibTableColumn
usdSnmpCommunityAccessList = _UsdSnmpCommunityAccessList_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 4),
    _UsdSnmpCommunityAccessList_Type()
)
usdSnmpCommunityAccessList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpCommunityAccessList.setStatus("current")
_UsdSnmpCommunityAccessListName_Type = UsdSnmpAccessListName
_UsdSnmpCommunityAccessListName_Object = MibTableColumn
usdSnmpCommunityAccessListName = _UsdSnmpCommunityAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 5),
    _UsdSnmpCommunityAccessListName_Type()
)
usdSnmpCommunityAccessListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpCommunityAccessListName.setStatus("current")


class _UsdSnmpCommunityView_Type(Integer32):
    """Custom type usdSnmpCommunityView based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("everything", 1),
          ("nothing", 3),
          ("user", 2))
    )


_UsdSnmpCommunityView_Type.__name__ = "Integer32"
_UsdSnmpCommunityView_Object = MibTableColumn
usdSnmpCommunityView = _UsdSnmpCommunityView_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 2, 1, 1, 6),
    _UsdSnmpCommunityView_Type()
)
usdSnmpCommunityView.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpCommunityView.setStatus("current")
_UsdSnmpTrap_ObjectIdentity = ObjectIdentity
usdSnmpTrap = _UsdSnmpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3)
)
_UsdSnmpTrapGlobalFilter_Type = UsdSnmpTrapMask
_UsdSnmpTrapGlobalFilter_Object = MibScalar
usdSnmpTrapGlobalFilter = _UsdSnmpTrapGlobalFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 1),
    _UsdSnmpTrapGlobalFilter_Type()
)
usdSnmpTrapGlobalFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpTrapGlobalFilter.setStatus("current")


class _UsdSnmpTrapSource_Type(Integer32):
    """Custom type usdSnmpTrapSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdSnmpTrapSource_Type.__name__ = "Integer32"
_UsdSnmpTrapSource_Object = MibScalar
usdSnmpTrapSource = _UsdSnmpTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 2),
    _UsdSnmpTrapSource_Type()
)
usdSnmpTrapSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpTrapSource.setStatus("current")
_UsdSnmpTrapHostTable_Object = MibTable
usdSnmpTrapHostTable = _UsdSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3)
)
if mibBuilder.loadTexts:
    usdSnmpTrapHostTable.setStatus("current")
_UsdSnmpTrapHostEntry_Object = MibTableRow
usdSnmpTrapHostEntry = _UsdSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1)
)
usdSnmpTrapHostEntry.setIndexNames(
    (0, "Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"),
)
if mibBuilder.loadTexts:
    usdSnmpTrapHostEntry.setStatus("current")
_UsdSnmpTrapHostIpAddress_Type = IpAddress
_UsdSnmpTrapHostIpAddress_Object = MibTableColumn
usdSnmpTrapHostIpAddress = _UsdSnmpTrapHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 1),
    _UsdSnmpTrapHostIpAddress_Type()
)
usdSnmpTrapHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpTrapHostIpAddress.setStatus("current")
_UsdSnmpTrapHostRowStatus_Type = RowStatus
_UsdSnmpTrapHostRowStatus_Object = MibTableColumn
usdSnmpTrapHostRowStatus = _UsdSnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 2),
    _UsdSnmpTrapHostRowStatus_Type()
)
usdSnmpTrapHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostRowStatus.setStatus("current")


class _UsdSnmpTrapHostUdpPort_Type(Integer32):
    """Custom type usdSnmpTrapHostUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdSnmpTrapHostUdpPort_Type.__name__ = "Integer32"
_UsdSnmpTrapHostUdpPort_Object = MibTableColumn
usdSnmpTrapHostUdpPort = _UsdSnmpTrapHostUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 3),
    _UsdSnmpTrapHostUdpPort_Type()
)
usdSnmpTrapHostUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostUdpPort.setStatus("current")
_UsdSnmpTrapHostCommunity_Type = UsdSnmpCommunityName
_UsdSnmpTrapHostCommunity_Object = MibTableColumn
usdSnmpTrapHostCommunity = _UsdSnmpTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 4),
    _UsdSnmpTrapHostCommunity_Type()
)
usdSnmpTrapHostCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostCommunity.setStatus("current")


class _UsdSnmpTrapHostProtocolVersion_Type(Integer32):
    """Custom type usdSnmpTrapHostProtocolVersion based on Integer32"""
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


_UsdSnmpTrapHostProtocolVersion_Type.__name__ = "Integer32"
_UsdSnmpTrapHostProtocolVersion_Object = MibTableColumn
usdSnmpTrapHostProtocolVersion = _UsdSnmpTrapHostProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 5),
    _UsdSnmpTrapHostProtocolVersion_Type()
)
usdSnmpTrapHostProtocolVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostProtocolVersion.setStatus("current")
_UsdSnmpTrapHostFilter_Type = UsdSnmpTrapMask
_UsdSnmpTrapHostFilter_Object = MibTableColumn
usdSnmpTrapHostFilter = _UsdSnmpTrapHostFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 6),
    _UsdSnmpTrapHostFilter_Type()
)
usdSnmpTrapHostFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostFilter.setStatus("current")
_UsdSnmpTrapHostSends_Type = Counter32
_UsdSnmpTrapHostSends_Object = MibTableColumn
usdSnmpTrapHostSends = _UsdSnmpTrapHostSends_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 7),
    _UsdSnmpTrapHostSends_Type()
)
usdSnmpTrapHostSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpTrapHostSends.setStatus("current")
_UsdSnmpTrapHostDiscards_Type = Counter32
_UsdSnmpTrapHostDiscards_Object = MibTableColumn
usdSnmpTrapHostDiscards = _UsdSnmpTrapHostDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 8),
    _UsdSnmpTrapHostDiscards_Type()
)
usdSnmpTrapHostDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpTrapHostDiscards.setStatus("current")
_UsdSnmpTrapHostSeverityFilter_Type = UsdTrapSeverity
_UsdSnmpTrapHostSeverityFilter_Object = MibTableColumn
usdSnmpTrapHostSeverityFilter = _UsdSnmpTrapHostSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 3, 1, 9),
    _UsdSnmpTrapHostSeverityFilter_Type()
)
usdSnmpTrapHostSeverityFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdSnmpTrapHostSeverityFilter.setStatus("current")
_UsdSnmpTrapProxy_Type = TruthValue
_UsdSnmpTrapProxy_Object = MibScalar
usdSnmpTrapProxy = _UsdSnmpTrapProxy_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 4),
    _UsdSnmpTrapProxy_Type()
)
usdSnmpTrapProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpTrapProxy.setStatus("current")
_UsdSnmpTrapTrapSeverity_Type = UsdTrapSeverity
_UsdSnmpTrapTrapSeverity_Object = MibScalar
usdSnmpTrapTrapSeverity = _UsdSnmpTrapTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 5),
    _UsdSnmpTrapTrapSeverity_Type()
)
usdSnmpTrapTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdSnmpTrapTrapSeverity.setStatus("current")
_UsdSnmpTrapGlobalDiscards_Type = Counter32
_UsdSnmpTrapGlobalDiscards_Object = MibScalar
usdSnmpTrapGlobalDiscards = _UsdSnmpTrapGlobalDiscards_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 6),
    _UsdSnmpTrapGlobalDiscards_Type()
)
usdSnmpTrapGlobalDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdSnmpTrapGlobalDiscards.setStatus("current")
_UsdSnmpTrapGlobalSeverityFilter_Type = UsdTrapSeverity
_UsdSnmpTrapGlobalSeverityFilter_Object = MibScalar
usdSnmpTrapGlobalSeverityFilter = _UsdSnmpTrapGlobalSeverityFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 3, 7),
    _UsdSnmpTrapGlobalSeverityFilter_Type()
)
usdSnmpTrapGlobalSeverityFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSnmpTrapGlobalSeverityFilter.setStatus("current")
_UsdSnmpAuthFailId_ObjectIdentity = ObjectIdentity
usdSnmpAuthFailId = _UsdSnmpAuthFailId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4)
)
_UsdSnmpAuthFailIdIpAddress_Type = IpAddress
_UsdSnmpAuthFailIdIpAddress_Object = MibScalar
usdSnmpAuthFailIdIpAddress = _UsdSnmpAuthFailIdIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 1),
    _UsdSnmpAuthFailIdIpAddress_Type()
)
usdSnmpAuthFailIdIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdSnmpAuthFailIdIpAddress.setStatus("current")
_UsdSnmpAuthFailIdUdpPort_Type = Integer32
_UsdSnmpAuthFailIdUdpPort_Object = MibScalar
usdSnmpAuthFailIdUdpPort = _UsdSnmpAuthFailIdUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 2),
    _UsdSnmpAuthFailIdUdpPort_Type()
)
usdSnmpAuthFailIdUdpPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdSnmpAuthFailIdUdpPort.setStatus("current")
_UsdSnmpAuthFailIdCommunity_Type = OctetString
_UsdSnmpAuthFailIdCommunity_Object = MibScalar
usdSnmpAuthFailIdCommunity = _UsdSnmpAuthFailIdCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 3),
    _UsdSnmpAuthFailIdCommunity_Type()
)
usdSnmpAuthFailIdCommunity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdSnmpAuthFailIdCommunity.setStatus("current")


class _UsdSnmpAuthFailIdReason_Type(Integer32):
    """Custom type usdSnmpAuthFailIdReason based on Integer32"""
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


_UsdSnmpAuthFailIdReason_Type.__name__ = "Integer32"
_UsdSnmpAuthFailIdReason_Object = MibScalar
usdSnmpAuthFailIdReason = _UsdSnmpAuthFailIdReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 1, 4, 4),
    _UsdSnmpAuthFailIdReason_Type()
)
usdSnmpAuthFailIdReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    usdSnmpAuthFailIdReason.setStatus("current")
_UsdSnmpConformance_ObjectIdentity = ObjectIdentity
usdSnmpConformance = _UsdSnmpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2)
)
_UsdSnmpCompliances_ObjectIdentity = ObjectIdentity
usdSnmpCompliances = _UsdSnmpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1)
)
_UsdSnmpGroups_ObjectIdentity = ObjectIdentity
usdSnmpGroups = _UsdSnmpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2)
)

# Managed Objects groups

usdSnmpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 1)
)
usdSnmpGroup.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    usdSnmpGroup.setStatus("obsolete")

usdSnmpAuthFailGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 2)
)
usdSnmpAuthFailGroup.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdIpAddress"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdUdpPort"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdCommunity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpAuthFailIdReason"))
)
if mibBuilder.loadTexts:
    usdSnmpAuthFailGroup.setStatus("current")

usdSnmpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 3)
)
usdSnmpGroup2.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    usdSnmpGroup2.setStatus("obsolete")

usdSnmpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 4)
)
usdSnmpGroup3.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpInterfaceMode"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"))
)
if mibBuilder.loadTexts:
    usdSnmpGroup3.setStatus("obsolete")

usdSnmpGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 5)
)
usdSnmpGeneralGroup.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
)
if mibBuilder.loadTexts:
    usdSnmpGeneralGroup.setStatus("obsolete")

usdSnmpAccessGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 6)
)
usdSnmpAccessGroup.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityPrivilege"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessList"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityAccessListName"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpCommunityView"))
)
if mibBuilder.loadTexts:
    usdSnmpAccessGroup.setStatus("current")

usdSnmpTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 7)
)
usdSnmpTrapGroup.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapSource"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapProxy"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostIpAddress"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostRowStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostUdpPort"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostCommunity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostProtocolVersion"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSends"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostDiscards"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapHostSeverityFilter"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapTrapSeverity"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalDiscards"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpTrapGlobalSeverityFilter"))
)
if mibBuilder.loadTexts:
    usdSnmpTrapGroup.setStatus("current")

usdSnmpGeneralGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 2, 8)
)
usdSnmpGeneralGroup2.setObjects(
      *(("Unisphere-Data-SNMP-MIB", "usdSnmpMaxPduSize"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpProxyStatus"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompCompressed"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhanced"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompEnhancedDisplay"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestricted"),
        ("Unisphere-Data-SNMP-MIB", "usdSnmpIntfCompRestrictedDisplay"))
)
if mibBuilder.loadTexts:
    usdSnmpGeneralGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSnmpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdSnmpCompliance.setStatus(
        "obsolete"
    )

usdSnmpCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdSnmpCompliance2.setStatus(
        "obsolete"
    )

usdSnmpCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 3)
)
if mibBuilder.loadTexts:
    usdSnmpCompliance3.setStatus(
        "obsolete"
    )

usdSnmpCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 4)
)
if mibBuilder.loadTexts:
    usdSnmpCompliance4.setStatus(
        "obsolete"
    )

usdSnmpCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 16, 2, 1, 5)
)
if mibBuilder.loadTexts:
    usdSnmpCompliance5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SNMP-MIB",
    **{"UsdSnmpCommunityName": UsdSnmpCommunityName,
       "UsdSnmpAccessListName": UsdSnmpAccessListName,
       "UsdSnmpTrapMask": UsdSnmpTrapMask,
       "UsdTrapSeverity": UsdTrapSeverity,
       "UsdSnmpIntfCompRestrictedMask": UsdSnmpIntfCompRestrictedMask,
       "usdSnmpMIB": usdSnmpMIB,
       "usdSnmpObjects": usdSnmpObjects,
       "usdSnmpGeneral": usdSnmpGeneral,
       "usdSnmpMaxPduSize": usdSnmpMaxPduSize,
       "usdSnmpInterfaceMode": usdSnmpInterfaceMode,
       "usdSnmpInterfaceCompress": usdSnmpInterfaceCompress,
       "usdSnmpIntfCompCompressed": usdSnmpIntfCompCompressed,
       "usdSnmpIntfCompEnhanced": usdSnmpIntfCompEnhanced,
       "usdSnmpIntfCompEnhancedDisplay": usdSnmpIntfCompEnhancedDisplay,
       "usdSnmpIntfCompRestricted": usdSnmpIntfCompRestricted,
       "usdSnmpIntfCompRestrictedDisplay": usdSnmpIntfCompRestrictedDisplay,
       "usdSnmpProxyStatus": usdSnmpProxyStatus,
       "usdSnmpCommunity": usdSnmpCommunity,
       "usdSnmpCommunityTable": usdSnmpCommunityTable,
       "usdSnmpCommunityEntry": usdSnmpCommunityEntry,
       "usdSnmpCommunityName": usdSnmpCommunityName,
       "usdSnmpCommunityRowStatus": usdSnmpCommunityRowStatus,
       "usdSnmpCommunityPrivilege": usdSnmpCommunityPrivilege,
       "usdSnmpCommunityAccessList": usdSnmpCommunityAccessList,
       "usdSnmpCommunityAccessListName": usdSnmpCommunityAccessListName,
       "usdSnmpCommunityView": usdSnmpCommunityView,
       "usdSnmpTrap": usdSnmpTrap,
       "usdSnmpTrapGlobalFilter": usdSnmpTrapGlobalFilter,
       "usdSnmpTrapSource": usdSnmpTrapSource,
       "usdSnmpTrapHostTable": usdSnmpTrapHostTable,
       "usdSnmpTrapHostEntry": usdSnmpTrapHostEntry,
       "usdSnmpTrapHostIpAddress": usdSnmpTrapHostIpAddress,
       "usdSnmpTrapHostRowStatus": usdSnmpTrapHostRowStatus,
       "usdSnmpTrapHostUdpPort": usdSnmpTrapHostUdpPort,
       "usdSnmpTrapHostCommunity": usdSnmpTrapHostCommunity,
       "usdSnmpTrapHostProtocolVersion": usdSnmpTrapHostProtocolVersion,
       "usdSnmpTrapHostFilter": usdSnmpTrapHostFilter,
       "usdSnmpTrapHostSends": usdSnmpTrapHostSends,
       "usdSnmpTrapHostDiscards": usdSnmpTrapHostDiscards,
       "usdSnmpTrapHostSeverityFilter": usdSnmpTrapHostSeverityFilter,
       "usdSnmpTrapProxy": usdSnmpTrapProxy,
       "usdSnmpTrapTrapSeverity": usdSnmpTrapTrapSeverity,
       "usdSnmpTrapGlobalDiscards": usdSnmpTrapGlobalDiscards,
       "usdSnmpTrapGlobalSeverityFilter": usdSnmpTrapGlobalSeverityFilter,
       "usdSnmpAuthFailId": usdSnmpAuthFailId,
       "usdSnmpAuthFailIdIpAddress": usdSnmpAuthFailIdIpAddress,
       "usdSnmpAuthFailIdUdpPort": usdSnmpAuthFailIdUdpPort,
       "usdSnmpAuthFailIdCommunity": usdSnmpAuthFailIdCommunity,
       "usdSnmpAuthFailIdReason": usdSnmpAuthFailIdReason,
       "usdSnmpConformance": usdSnmpConformance,
       "usdSnmpCompliances": usdSnmpCompliances,
       "usdSnmpCompliance": usdSnmpCompliance,
       "usdSnmpCompliance2": usdSnmpCompliance2,
       "usdSnmpCompliance3": usdSnmpCompliance3,
       "usdSnmpCompliance4": usdSnmpCompliance4,
       "usdSnmpCompliance5": usdSnmpCompliance5,
       "usdSnmpGroups": usdSnmpGroups,
       "usdSnmpGroup": usdSnmpGroup,
       "usdSnmpAuthFailGroup": usdSnmpAuthFailGroup,
       "usdSnmpGroup2": usdSnmpGroup2,
       "usdSnmpGroup3": usdSnmpGroup3,
       "usdSnmpGeneralGroup": usdSnmpGeneralGroup,
       "usdSnmpAccessGroup": usdSnmpAccessGroup,
       "usdSnmpTrapGroup": usdSnmpTrapGroup,
       "usdSnmpGeneralGroup2": usdSnmpGeneralGroup2}
)
