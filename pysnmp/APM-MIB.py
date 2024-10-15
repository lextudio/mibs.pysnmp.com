# SNMP MIB module (APM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/APM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:39:24 2024
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

(OwnerString,
 rmon) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString",
    "rmon")

(protocolDirLocalIndex,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "protocolDirLocalIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

apm = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23)
)
apm.setRevisions(
        ("2004-02-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AppLocalIndex(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class ProtocolDirNetworkAddress(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class DataSourceOrZero(ObjectIdentifier, TextualConvention):
    status = "current"


class RmonClientID(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )



class TransactionAggregationType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("applications", 4),
          ("clients", 2),
          ("flows", 1),
          ("servers", 3))
    )



# MIB Managed Objects in the order of their OIDs

_ApmNotifications_ObjectIdentity = ObjectIdentity
apmNotifications = _ApmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23, 0)
)
_ApmMibObjects_ObjectIdentity = ObjectIdentity
apmMibObjects = _ApmMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23, 1)
)
_ApmAppDirTable_Object = MibTable
apmAppDirTable = _ApmAppDirTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1)
)
if mibBuilder.loadTexts:
    apmAppDirTable.setStatus("current")
_ApmAppDirEntry_Object = MibTableRow
apmAppDirEntry = _ApmAppDirEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1)
)
apmAppDirEntry.setIndexNames(
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
    (0, "APM-MIB", "apmAppDirResponsivenessType"),
)
if mibBuilder.loadTexts:
    apmAppDirEntry.setStatus("current")
_ApmAppDirAppLocalIndex_Type = AppLocalIndex
_ApmAppDirAppLocalIndex_Object = MibTableColumn
apmAppDirAppLocalIndex = _ApmAppDirAppLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 1),
    _ApmAppDirAppLocalIndex_Type()
)
apmAppDirAppLocalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmAppDirAppLocalIndex.setStatus("current")


class _ApmAppDirResponsivenessType_Type(Integer32):
    """Custom type apmAppDirResponsivenessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("streamingOriented", 3),
          ("throughputOriented", 2),
          ("transactionOriented", 1))
    )


_ApmAppDirResponsivenessType_Type.__name__ = "Integer32"
_ApmAppDirResponsivenessType_Object = MibTableColumn
apmAppDirResponsivenessType = _ApmAppDirResponsivenessType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 2),
    _ApmAppDirResponsivenessType_Type()
)
apmAppDirResponsivenessType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessType.setStatus("current")


class _ApmAppDirConfig_Type(Integer32):
    """Custom type apmAppDirConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ApmAppDirConfig_Type.__name__ = "Integer32"
_ApmAppDirConfig_Object = MibTableColumn
apmAppDirConfig = _ApmAppDirConfig_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 3),
    _ApmAppDirConfig_Type()
)
apmAppDirConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirConfig.setStatus("current")
_ApmAppDirResponsivenessBoundary1_Type = Unsigned32
_ApmAppDirResponsivenessBoundary1_Object = MibTableColumn
apmAppDirResponsivenessBoundary1 = _ApmAppDirResponsivenessBoundary1_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 4),
    _ApmAppDirResponsivenessBoundary1_Type()
)
apmAppDirResponsivenessBoundary1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary1.setStatus("current")
_ApmAppDirResponsivenessBoundary2_Type = Unsigned32
_ApmAppDirResponsivenessBoundary2_Object = MibTableColumn
apmAppDirResponsivenessBoundary2 = _ApmAppDirResponsivenessBoundary2_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 5),
    _ApmAppDirResponsivenessBoundary2_Type()
)
apmAppDirResponsivenessBoundary2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary2.setStatus("current")
_ApmAppDirResponsivenessBoundary3_Type = Unsigned32
_ApmAppDirResponsivenessBoundary3_Object = MibTableColumn
apmAppDirResponsivenessBoundary3 = _ApmAppDirResponsivenessBoundary3_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 6),
    _ApmAppDirResponsivenessBoundary3_Type()
)
apmAppDirResponsivenessBoundary3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary3.setStatus("current")
_ApmAppDirResponsivenessBoundary4_Type = Unsigned32
_ApmAppDirResponsivenessBoundary4_Object = MibTableColumn
apmAppDirResponsivenessBoundary4 = _ApmAppDirResponsivenessBoundary4_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 7),
    _ApmAppDirResponsivenessBoundary4_Type()
)
apmAppDirResponsivenessBoundary4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary4.setStatus("current")
_ApmAppDirResponsivenessBoundary5_Type = Unsigned32
_ApmAppDirResponsivenessBoundary5_Object = MibTableColumn
apmAppDirResponsivenessBoundary5 = _ApmAppDirResponsivenessBoundary5_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 8),
    _ApmAppDirResponsivenessBoundary5_Type()
)
apmAppDirResponsivenessBoundary5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary5.setStatus("current")
_ApmAppDirResponsivenessBoundary6_Type = Unsigned32
_ApmAppDirResponsivenessBoundary6_Object = MibTableColumn
apmAppDirResponsivenessBoundary6 = _ApmAppDirResponsivenessBoundary6_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 1, 1, 9),
    _ApmAppDirResponsivenessBoundary6_Type()
)
apmAppDirResponsivenessBoundary6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirResponsivenessBoundary6.setStatus("current")
_ApmBucketBoundaryLastChange_Type = TimeStamp
_ApmBucketBoundaryLastChange_Object = MibScalar
apmBucketBoundaryLastChange = _ApmBucketBoundaryLastChange_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 2),
    _ApmBucketBoundaryLastChange_Type()
)
apmBucketBoundaryLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmBucketBoundaryLastChange.setStatus("current")
_ApmAppDirID_Type = ObjectIdentifier
_ApmAppDirID_Object = MibScalar
apmAppDirID = _ApmAppDirID_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 3),
    _ApmAppDirID_Type()
)
apmAppDirID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmAppDirID.setStatus("current")
_ApmHttpFilterTable_Object = MibTable
apmHttpFilterTable = _ApmHttpFilterTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4)
)
if mibBuilder.loadTexts:
    apmHttpFilterTable.setStatus("current")
_ApmHttpFilterEntry_Object = MibTableRow
apmHttpFilterEntry = _ApmHttpFilterEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1)
)
apmHttpFilterEntry.setIndexNames(
    (0, "APM-MIB", "apmHttpFilterIndex"),
)
if mibBuilder.loadTexts:
    apmHttpFilterEntry.setStatus("current")


class _ApmHttpFilterIndex_Type(Unsigned32):
    """Custom type apmHttpFilterIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApmHttpFilterIndex_Type.__name__ = "Unsigned32"
_ApmHttpFilterIndex_Object = MibTableColumn
apmHttpFilterIndex = _ApmHttpFilterIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 1),
    _ApmHttpFilterIndex_Type()
)
apmHttpFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmHttpFilterIndex.setStatus("current")
_ApmHttpFilterAppLocalIndex_Type = AppLocalIndex
_ApmHttpFilterAppLocalIndex_Object = MibTableColumn
apmHttpFilterAppLocalIndex = _ApmHttpFilterAppLocalIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 2),
    _ApmHttpFilterAppLocalIndex_Type()
)
apmHttpFilterAppLocalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmHttpFilterAppLocalIndex.setStatus("current")


class _ApmHttpFilterServerProtocol_Type(Unsigned32):
    """Custom type apmHttpFilterServerProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApmHttpFilterServerProtocol_Type.__name__ = "Unsigned32"
_ApmHttpFilterServerProtocol_Object = MibTableColumn
apmHttpFilterServerProtocol = _ApmHttpFilterServerProtocol_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 3),
    _ApmHttpFilterServerProtocol_Type()
)
apmHttpFilterServerProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterServerProtocol.setStatus("current")
_ApmHttpFilterServerAddress_Type = ProtocolDirNetworkAddress
_ApmHttpFilterServerAddress_Object = MibTableColumn
apmHttpFilterServerAddress = _ApmHttpFilterServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 4),
    _ApmHttpFilterServerAddress_Type()
)
apmHttpFilterServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterServerAddress.setStatus("current")


class _ApmHttpFilterURLPath_Type(OctetString):
    """Custom type apmHttpFilterURLPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65535),
    )


_ApmHttpFilterURLPath_Type.__name__ = "OctetString"
_ApmHttpFilterURLPath_Object = MibTableColumn
apmHttpFilterURLPath = _ApmHttpFilterURLPath_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 5),
    _ApmHttpFilterURLPath_Type()
)
apmHttpFilterURLPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterURLPath.setStatus("current")


class _ApmHttpFilterMatchType_Type(Integer32):
    """Custom type apmHttpFilterMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exact", 1),
          ("prefix", 3),
          ("stripTrailingSlash", 2))
    )


_ApmHttpFilterMatchType_Type.__name__ = "Integer32"
_ApmHttpFilterMatchType_Object = MibTableColumn
apmHttpFilterMatchType = _ApmHttpFilterMatchType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 6),
    _ApmHttpFilterMatchType_Type()
)
apmHttpFilterMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterMatchType.setStatus("current")
_ApmHttpFilterOwner_Type = OwnerString
_ApmHttpFilterOwner_Object = MibTableColumn
apmHttpFilterOwner = _ApmHttpFilterOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 7),
    _ApmHttpFilterOwner_Type()
)
apmHttpFilterOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterOwner.setStatus("current")
_ApmHttpFilterStorageType_Type = StorageType
_ApmHttpFilterStorageType_Object = MibTableColumn
apmHttpFilterStorageType = _ApmHttpFilterStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 8),
    _ApmHttpFilterStorageType_Type()
)
apmHttpFilterStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterStorageType.setStatus("current")
_ApmHttpFilterRowStatus_Type = RowStatus
_ApmHttpFilterRowStatus_Object = MibTableColumn
apmHttpFilterRowStatus = _ApmHttpFilterRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 4, 1, 9),
    _ApmHttpFilterRowStatus_Type()
)
apmHttpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmHttpFilterRowStatus.setStatus("current")
_ApmHttpIgnoreUnregisteredURLs_Type = TruthValue
_ApmHttpIgnoreUnregisteredURLs_Object = MibScalar
apmHttpIgnoreUnregisteredURLs = _ApmHttpIgnoreUnregisteredURLs_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 5),
    _ApmHttpIgnoreUnregisteredURLs_Type()
)
apmHttpIgnoreUnregisteredURLs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmHttpIgnoreUnregisteredURLs.setStatus("current")
_ApmHttp4xxIsFailure_Type = TruthValue
_ApmHttp4xxIsFailure_Object = MibScalar
apmHttp4xxIsFailure = _ApmHttp4xxIsFailure_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 6),
    _ApmHttp4xxIsFailure_Type()
)
apmHttp4xxIsFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmHttp4xxIsFailure.setStatus("current")
_ApmUserDefinedAppTable_Object = MibTable
apmUserDefinedAppTable = _ApmUserDefinedAppTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 7)
)
if mibBuilder.loadTexts:
    apmUserDefinedAppTable.setStatus("current")
_ApmUserDefinedAppEntry_Object = MibTableRow
apmUserDefinedAppEntry = _ApmUserDefinedAppEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1)
)
apmUserDefinedAppEntry.setIndexNames(
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
)
if mibBuilder.loadTexts:
    apmUserDefinedAppEntry.setStatus("current")


class _ApmUserDefinedAppParentIndex_Type(Unsigned32):
    """Custom type apmUserDefinedAppParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ApmUserDefinedAppParentIndex_Type.__name__ = "Unsigned32"
_ApmUserDefinedAppParentIndex_Object = MibTableColumn
apmUserDefinedAppParentIndex = _ApmUserDefinedAppParentIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1, 1),
    _ApmUserDefinedAppParentIndex_Type()
)
apmUserDefinedAppParentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmUserDefinedAppParentIndex.setStatus("current")
_ApmUserDefinedAppApplication_Type = SnmpAdminString
_ApmUserDefinedAppApplication_Object = MibTableColumn
apmUserDefinedAppApplication = _ApmUserDefinedAppApplication_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 7, 1, 2),
    _ApmUserDefinedAppApplication_Type()
)
apmUserDefinedAppApplication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmUserDefinedAppApplication.setStatus("current")
_ApmNameTable_Object = MibTable
apmNameTable = _ApmNameTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8)
)
if mibBuilder.loadTexts:
    apmNameTable.setStatus("current")
_ApmNameEntry_Object = MibTableRow
apmNameEntry = _ApmNameEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1)
)
apmNameEntry.setIndexNames(
    (0, "APM-MIB", "apmNameClientID"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "APM-MIB", "apmNameClientAddress"),
    (0, "APM-MIB", "apmNameMappingStartTime"),
)
if mibBuilder.loadTexts:
    apmNameEntry.setStatus("current")
_ApmNameClientID_Type = RmonClientID
_ApmNameClientID_Object = MibTableColumn
apmNameClientID = _ApmNameClientID_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 1),
    _ApmNameClientID_Type()
)
apmNameClientID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmNameClientID.setStatus("current")


class _ApmNameClientAddress_Type(ProtocolDirNetworkAddress):
    """Custom type apmNameClientAddress based on ProtocolDirNetworkAddress"""
    subtypeSpec = ProtocolDirNetworkAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApmNameClientAddress_Type.__name__ = "ProtocolDirNetworkAddress"
_ApmNameClientAddress_Object = MibTableColumn
apmNameClientAddress = _ApmNameClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 2),
    _ApmNameClientAddress_Type()
)
apmNameClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmNameClientAddress.setStatus("current")
_ApmNameMappingStartTime_Type = DateAndTime
_ApmNameMappingStartTime_Object = MibTableColumn
apmNameMappingStartTime = _ApmNameMappingStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 3),
    _ApmNameMappingStartTime_Type()
)
apmNameMappingStartTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmNameMappingStartTime.setStatus("current")
_ApmNameMachineName_Type = SnmpAdminString
_ApmNameMachineName_Object = MibTableColumn
apmNameMachineName = _ApmNameMachineName_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 4),
    _ApmNameMachineName_Type()
)
apmNameMachineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmNameMachineName.setStatus("current")
_ApmNameUserName_Type = SnmpAdminString
_ApmNameUserName_Object = MibTableColumn
apmNameUserName = _ApmNameUserName_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 8, 1, 5),
    _ApmNameUserName_Type()
)
apmNameUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmNameUserName.setStatus("current")
_ApmReportControlTable_Object = MibTable
apmReportControlTable = _ApmReportControlTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9)
)
if mibBuilder.loadTexts:
    apmReportControlTable.setStatus("current")
_ApmReportControlEntry_Object = MibTableRow
apmReportControlEntry = _ApmReportControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1)
)
apmReportControlEntry.setIndexNames(
    (0, "APM-MIB", "apmReportControlIndex"),
)
if mibBuilder.loadTexts:
    apmReportControlEntry.setStatus("current")


class _ApmReportControlIndex_Type(Unsigned32):
    """Custom type apmReportControlIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApmReportControlIndex_Type.__name__ = "Unsigned32"
_ApmReportControlIndex_Object = MibTableColumn
apmReportControlIndex = _ApmReportControlIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 1),
    _ApmReportControlIndex_Type()
)
apmReportControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmReportControlIndex.setStatus("current")
_ApmReportControlDataSource_Type = DataSourceOrZero
_ApmReportControlDataSource_Object = MibTableColumn
apmReportControlDataSource = _ApmReportControlDataSource_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 2),
    _ApmReportControlDataSource_Type()
)
apmReportControlDataSource.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlDataSource.setStatus("current")
_ApmReportControlAggregationType_Type = TransactionAggregationType
_ApmReportControlAggregationType_Object = MibTableColumn
apmReportControlAggregationType = _ApmReportControlAggregationType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 3),
    _ApmReportControlAggregationType_Type()
)
apmReportControlAggregationType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlAggregationType.setStatus("current")


class _ApmReportControlInterval_Type(Unsigned32):
    """Custom type apmReportControlInterval based on Unsigned32"""
    defaultValue = 3600


_ApmReportControlInterval_Object = MibTableColumn
apmReportControlInterval = _ApmReportControlInterval_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 4),
    _ApmReportControlInterval_Type()
)
apmReportControlInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlInterval.setStatus("current")
if mibBuilder.loadTexts:
    apmReportControlInterval.setUnits("Seconds")
_ApmReportControlRequestedSize_Type = Unsigned32
_ApmReportControlRequestedSize_Object = MibTableColumn
apmReportControlRequestedSize = _ApmReportControlRequestedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 5),
    _ApmReportControlRequestedSize_Type()
)
apmReportControlRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlRequestedSize.setStatus("current")
_ApmReportControlGrantedSize_Type = Unsigned32
_ApmReportControlGrantedSize_Object = MibTableColumn
apmReportControlGrantedSize = _ApmReportControlGrantedSize_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 6),
    _ApmReportControlGrantedSize_Type()
)
apmReportControlGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlGrantedSize.setStatus("current")


class _ApmReportControlRequestedReports_Type(Unsigned32):
    """Custom type apmReportControlRequestedReports based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApmReportControlRequestedReports_Type.__name__ = "Unsigned32"
_ApmReportControlRequestedReports_Object = MibTableColumn
apmReportControlRequestedReports = _ApmReportControlRequestedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 7),
    _ApmReportControlRequestedReports_Type()
)
apmReportControlRequestedReports.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlRequestedReports.setStatus("current")


class _ApmReportControlGrantedReports_Type(Unsigned32):
    """Custom type apmReportControlGrantedReports based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApmReportControlGrantedReports_Type.__name__ = "Unsigned32"
_ApmReportControlGrantedReports_Object = MibTableColumn
apmReportControlGrantedReports = _ApmReportControlGrantedReports_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 8),
    _ApmReportControlGrantedReports_Type()
)
apmReportControlGrantedReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlGrantedReports.setStatus("current")
_ApmReportControlStartTime_Type = TimeStamp
_ApmReportControlStartTime_Object = MibTableColumn
apmReportControlStartTime = _ApmReportControlStartTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 9),
    _ApmReportControlStartTime_Type()
)
apmReportControlStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlStartTime.setStatus("current")


class _ApmReportControlReportNumber_Type(Unsigned32):
    """Custom type apmReportControlReportNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApmReportControlReportNumber_Type.__name__ = "Unsigned32"
_ApmReportControlReportNumber_Object = MibTableColumn
apmReportControlReportNumber = _ApmReportControlReportNumber_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 10),
    _ApmReportControlReportNumber_Type()
)
apmReportControlReportNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlReportNumber.setStatus("current")
_ApmReportControlDeniedInserts_Type = Counter32
_ApmReportControlDeniedInserts_Object = MibTableColumn
apmReportControlDeniedInserts = _ApmReportControlDeniedInserts_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 11),
    _ApmReportControlDeniedInserts_Type()
)
apmReportControlDeniedInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlDeniedInserts.setStatus("current")
_ApmReportControlDroppedFrames_Type = Counter32
_ApmReportControlDroppedFrames_Object = MibTableColumn
apmReportControlDroppedFrames = _ApmReportControlDroppedFrames_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 12),
    _ApmReportControlDroppedFrames_Type()
)
apmReportControlDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportControlDroppedFrames.setStatus("current")
_ApmReportControlOwner_Type = OwnerString
_ApmReportControlOwner_Object = MibTableColumn
apmReportControlOwner = _ApmReportControlOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 13),
    _ApmReportControlOwner_Type()
)
apmReportControlOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlOwner.setStatus("current")
_ApmReportControlStorageType_Type = StorageType
_ApmReportControlStorageType_Object = MibTableColumn
apmReportControlStorageType = _ApmReportControlStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 14),
    _ApmReportControlStorageType_Type()
)
apmReportControlStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlStorageType.setStatus("current")
_ApmReportControlStatus_Type = RowStatus
_ApmReportControlStatus_Object = MibTableColumn
apmReportControlStatus = _ApmReportControlStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 9, 1, 15),
    _ApmReportControlStatus_Type()
)
apmReportControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmReportControlStatus.setStatus("current")
_ApmReportTable_Object = MibTable
apmReportTable = _ApmReportTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10)
)
if mibBuilder.loadTexts:
    apmReportTable.setStatus("current")
_ApmReportEntry_Object = MibTableRow
apmReportEntry = _ApmReportEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1)
)
apmReportEntry.setIndexNames(
    (0, "APM-MIB", "apmReportControlIndex"),
    (0, "APM-MIB", "apmReportIndex"),
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
    (0, "APM-MIB", "apmAppDirResponsivenessType"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "APM-MIB", "apmReportServerAddress"),
    (0, "APM-MIB", "apmNameClientID"),
)
if mibBuilder.loadTexts:
    apmReportEntry.setStatus("current")


class _ApmReportIndex_Type(Unsigned32):
    """Custom type apmReportIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_ApmReportIndex_Type.__name__ = "Unsigned32"
_ApmReportIndex_Object = MibTableColumn
apmReportIndex = _ApmReportIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 1),
    _ApmReportIndex_Type()
)
apmReportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmReportIndex.setStatus("current")
_ApmReportServerAddress_Type = ProtocolDirNetworkAddress
_ApmReportServerAddress_Object = MibTableColumn
apmReportServerAddress = _ApmReportServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 2),
    _ApmReportServerAddress_Type()
)
apmReportServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmReportServerAddress.setStatus("current")
_ApmReportTransactionCount_Type = Unsigned32
_ApmReportTransactionCount_Object = MibTableColumn
apmReportTransactionCount = _ApmReportTransactionCount_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 3),
    _ApmReportTransactionCount_Type()
)
apmReportTransactionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportTransactionCount.setStatus("current")
_ApmReportSuccessfulTransactions_Type = Unsigned32
_ApmReportSuccessfulTransactions_Object = MibTableColumn
apmReportSuccessfulTransactions = _ApmReportSuccessfulTransactions_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 4),
    _ApmReportSuccessfulTransactions_Type()
)
apmReportSuccessfulTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportSuccessfulTransactions.setStatus("current")
_ApmReportResponsivenessMean_Type = Unsigned32
_ApmReportResponsivenessMean_Object = MibTableColumn
apmReportResponsivenessMean = _ApmReportResponsivenessMean_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 5),
    _ApmReportResponsivenessMean_Type()
)
apmReportResponsivenessMean.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessMean.setStatus("current")
_ApmReportResponsivenessMin_Type = Unsigned32
_ApmReportResponsivenessMin_Object = MibTableColumn
apmReportResponsivenessMin = _ApmReportResponsivenessMin_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 6),
    _ApmReportResponsivenessMin_Type()
)
apmReportResponsivenessMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessMin.setStatus("current")
_ApmReportResponsivenessMax_Type = Unsigned32
_ApmReportResponsivenessMax_Object = MibTableColumn
apmReportResponsivenessMax = _ApmReportResponsivenessMax_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 7),
    _ApmReportResponsivenessMax_Type()
)
apmReportResponsivenessMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessMax.setStatus("current")
_ApmReportResponsivenessB1_Type = Unsigned32
_ApmReportResponsivenessB1_Object = MibTableColumn
apmReportResponsivenessB1 = _ApmReportResponsivenessB1_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 8),
    _ApmReportResponsivenessB1_Type()
)
apmReportResponsivenessB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB1.setStatus("current")
_ApmReportResponsivenessB2_Type = Unsigned32
_ApmReportResponsivenessB2_Object = MibTableColumn
apmReportResponsivenessB2 = _ApmReportResponsivenessB2_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 9),
    _ApmReportResponsivenessB2_Type()
)
apmReportResponsivenessB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB2.setStatus("current")
_ApmReportResponsivenessB3_Type = Unsigned32
_ApmReportResponsivenessB3_Object = MibTableColumn
apmReportResponsivenessB3 = _ApmReportResponsivenessB3_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 10),
    _ApmReportResponsivenessB3_Type()
)
apmReportResponsivenessB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB3.setStatus("current")
_ApmReportResponsivenessB4_Type = Unsigned32
_ApmReportResponsivenessB4_Object = MibTableColumn
apmReportResponsivenessB4 = _ApmReportResponsivenessB4_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 11),
    _ApmReportResponsivenessB4_Type()
)
apmReportResponsivenessB4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB4.setStatus("current")
_ApmReportResponsivenessB5_Type = Unsigned32
_ApmReportResponsivenessB5_Object = MibTableColumn
apmReportResponsivenessB5 = _ApmReportResponsivenessB5_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 12),
    _ApmReportResponsivenessB5_Type()
)
apmReportResponsivenessB5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB5.setStatus("current")
_ApmReportResponsivenessB6_Type = Unsigned32
_ApmReportResponsivenessB6_Object = MibTableColumn
apmReportResponsivenessB6 = _ApmReportResponsivenessB6_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 13),
    _ApmReportResponsivenessB6_Type()
)
apmReportResponsivenessB6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB6.setStatus("current")
_ApmReportResponsivenessB7_Type = Unsigned32
_ApmReportResponsivenessB7_Object = MibTableColumn
apmReportResponsivenessB7 = _ApmReportResponsivenessB7_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 10, 1, 14),
    _ApmReportResponsivenessB7_Type()
)
apmReportResponsivenessB7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmReportResponsivenessB7.setStatus("current")
_ApmTransactionTable_Object = MibTable
apmTransactionTable = _ApmTransactionTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11)
)
if mibBuilder.loadTexts:
    apmTransactionTable.setStatus("current")
_ApmTransactionEntry_Object = MibTableRow
apmTransactionEntry = _ApmTransactionEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1)
)
apmTransactionEntry.setIndexNames(
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
    (0, "APM-MIB", "apmAppDirResponsivenessType"),
    (0, "RMON2-MIB", "protocolDirLocalIndex"),
    (0, "APM-MIB", "apmTransactionServerAddress"),
    (0, "APM-MIB", "apmNameClientID"),
    (0, "APM-MIB", "apmTransactionID"),
)
if mibBuilder.loadTexts:
    apmTransactionEntry.setStatus("current")


class _ApmTransactionServerAddress_Type(ProtocolDirNetworkAddress):
    """Custom type apmTransactionServerAddress based on ProtocolDirNetworkAddress"""
    subtypeSpec = ProtocolDirNetworkAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApmTransactionServerAddress_Type.__name__ = "ProtocolDirNetworkAddress"
_ApmTransactionServerAddress_Object = MibTableColumn
apmTransactionServerAddress = _ApmTransactionServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 1),
    _ApmTransactionServerAddress_Type()
)
apmTransactionServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmTransactionServerAddress.setStatus("current")


class _ApmTransactionID_Type(Unsigned32):
    """Custom type apmTransactionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ApmTransactionID_Type.__name__ = "Unsigned32"
_ApmTransactionID_Object = MibTableColumn
apmTransactionID = _ApmTransactionID_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 2),
    _ApmTransactionID_Type()
)
apmTransactionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmTransactionID.setStatus("current")
_ApmTransactionResponsiveness_Type = Unsigned32
_ApmTransactionResponsiveness_Object = MibTableColumn
apmTransactionResponsiveness = _ApmTransactionResponsiveness_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 3),
    _ApmTransactionResponsiveness_Type()
)
apmTransactionResponsiveness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmTransactionResponsiveness.setStatus("current")
_ApmTransactionAge_Type = TimeInterval
_ApmTransactionAge_Object = MibTableColumn
apmTransactionAge = _ApmTransactionAge_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 4),
    _ApmTransactionAge_Type()
)
apmTransactionAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmTransactionAge.setStatus("current")
_ApmTransactionSuccess_Type = TruthValue
_ApmTransactionSuccess_Object = MibTableColumn
apmTransactionSuccess = _ApmTransactionSuccess_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 11, 1, 5),
    _ApmTransactionSuccess_Type()
)
apmTransactionSuccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmTransactionSuccess.setStatus("current")
_ApmTransactionsRequestedHistorySize_Type = Unsigned32
_ApmTransactionsRequestedHistorySize_Object = MibScalar
apmTransactionsRequestedHistorySize = _ApmTransactionsRequestedHistorySize_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 12),
    _ApmTransactionsRequestedHistorySize_Type()
)
apmTransactionsRequestedHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmTransactionsRequestedHistorySize.setStatus("current")
_ApmExceptionTable_Object = MibTable
apmExceptionTable = _ApmExceptionTable_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13)
)
if mibBuilder.loadTexts:
    apmExceptionTable.setStatus("current")
_ApmExceptionEntry_Object = MibTableRow
apmExceptionEntry = _ApmExceptionEntry_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1)
)
apmExceptionEntry.setIndexNames(
    (0, "APM-MIB", "apmAppDirAppLocalIndex"),
    (0, "APM-MIB", "apmAppDirResponsivenessType"),
    (0, "APM-MIB", "apmExceptionIndex"),
)
if mibBuilder.loadTexts:
    apmExceptionEntry.setStatus("current")


class _ApmExceptionIndex_Type(Unsigned32):
    """Custom type apmExceptionIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ApmExceptionIndex_Type.__name__ = "Unsigned32"
_ApmExceptionIndex_Object = MibTableColumn
apmExceptionIndex = _ApmExceptionIndex_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 1),
    _ApmExceptionIndex_Type()
)
apmExceptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    apmExceptionIndex.setStatus("current")


class _ApmExceptionResponsivenessComparison_Type(Integer32):
    """Custom type apmExceptionResponsivenessComparison based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("greater", 2),
          ("less", 3),
          ("none", 1))
    )


_ApmExceptionResponsivenessComparison_Type.__name__ = "Integer32"
_ApmExceptionResponsivenessComparison_Object = MibTableColumn
apmExceptionResponsivenessComparison = _ApmExceptionResponsivenessComparison_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 2),
    _ApmExceptionResponsivenessComparison_Type()
)
apmExceptionResponsivenessComparison.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionResponsivenessComparison.setStatus("current")
_ApmExceptionResponsivenessThreshold_Type = Unsigned32
_ApmExceptionResponsivenessThreshold_Object = MibTableColumn
apmExceptionResponsivenessThreshold = _ApmExceptionResponsivenessThreshold_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 3),
    _ApmExceptionResponsivenessThreshold_Type()
)
apmExceptionResponsivenessThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionResponsivenessThreshold.setStatus("current")


class _ApmExceptionUnsuccessfulException_Type(Integer32):
    """Custom type apmExceptionUnsuccessfulException based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ApmExceptionUnsuccessfulException_Type.__name__ = "Integer32"
_ApmExceptionUnsuccessfulException_Object = MibTableColumn
apmExceptionUnsuccessfulException = _ApmExceptionUnsuccessfulException_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 4),
    _ApmExceptionUnsuccessfulException_Type()
)
apmExceptionUnsuccessfulException.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionUnsuccessfulException.setStatus("current")
_ApmExceptionResponsivenessEvents_Type = Counter32
_ApmExceptionResponsivenessEvents_Object = MibTableColumn
apmExceptionResponsivenessEvents = _ApmExceptionResponsivenessEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 5),
    _ApmExceptionResponsivenessEvents_Type()
)
apmExceptionResponsivenessEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmExceptionResponsivenessEvents.setStatus("current")
_ApmExceptionUnsuccessfulEvents_Type = Counter32
_ApmExceptionUnsuccessfulEvents_Object = MibTableColumn
apmExceptionUnsuccessfulEvents = _ApmExceptionUnsuccessfulEvents_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 6),
    _ApmExceptionUnsuccessfulEvents_Type()
)
apmExceptionUnsuccessfulEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apmExceptionUnsuccessfulEvents.setStatus("current")
_ApmExceptionOwner_Type = OwnerString
_ApmExceptionOwner_Object = MibTableColumn
apmExceptionOwner = _ApmExceptionOwner_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 7),
    _ApmExceptionOwner_Type()
)
apmExceptionOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionOwner.setStatus("current")
_ApmExceptionStorageType_Type = StorageType
_ApmExceptionStorageType_Object = MibTableColumn
apmExceptionStorageType = _ApmExceptionStorageType_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 8),
    _ApmExceptionStorageType_Type()
)
apmExceptionStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionStorageType.setStatus("current")
_ApmExceptionStatus_Type = RowStatus
_ApmExceptionStatus_Object = MibTableColumn
apmExceptionStatus = _ApmExceptionStatus_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 13, 1, 9),
    _ApmExceptionStatus_Type()
)
apmExceptionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    apmExceptionStatus.setStatus("current")


class _ApmThroughputExceptionMinTime_Type(Unsigned32):
    """Custom type apmThroughputExceptionMinTime based on Unsigned32"""
    defaultValue = 10


_ApmThroughputExceptionMinTime_Object = MibScalar
apmThroughputExceptionMinTime = _ApmThroughputExceptionMinTime_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 14),
    _ApmThroughputExceptionMinTime_Type()
)
apmThroughputExceptionMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmThroughputExceptionMinTime.setStatus("current")
if mibBuilder.loadTexts:
    apmThroughputExceptionMinTime.setUnits("seconds")


class _ApmNotificationMaxRate_Type(Unsigned32):
    """Custom type apmNotificationMaxRate based on Unsigned32"""
    defaultValue = 1


_ApmNotificationMaxRate_Object = MibScalar
apmNotificationMaxRate = _ApmNotificationMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 16, 23, 1, 15),
    _ApmNotificationMaxRate_Type()
)
apmNotificationMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apmNotificationMaxRate.setStatus("current")
_ApmConformance_ObjectIdentity = ObjectIdentity
apmConformance = _ApmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23, 2)
)
_ApmCompliances_ObjectIdentity = ObjectIdentity
apmCompliances = _ApmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 1)
)
_ApmGroups_ObjectIdentity = ObjectIdentity
apmGroups = _ApmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2)
)

# Managed Objects groups

apmAppDirGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 1)
)
apmAppDirGroup.setObjects(
      *(("APM-MIB", "apmAppDirConfig"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary1"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary2"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary3"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary4"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary5"),
        ("APM-MIB", "apmAppDirResponsivenessBoundary6"),
        ("APM-MIB", "apmBucketBoundaryLastChange"),
        ("APM-MIB", "apmAppDirID"),
        ("APM-MIB", "apmNameMachineName"),
        ("APM-MIB", "apmNameUserName"))
)
if mibBuilder.loadTexts:
    apmAppDirGroup.setStatus("current")

apmUserDefinedApplicationsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 2)
)
apmUserDefinedApplicationsGroup.setObjects(
      *(("APM-MIB", "apmHttpFilterAppLocalIndex"),
        ("APM-MIB", "apmHttpFilterServerProtocol"),
        ("APM-MIB", "apmHttpFilterServerAddress"),
        ("APM-MIB", "apmHttpFilterURLPath"),
        ("APM-MIB", "apmHttpFilterMatchType"),
        ("APM-MIB", "apmHttpFilterOwner"),
        ("APM-MIB", "apmHttpFilterStorageType"),
        ("APM-MIB", "apmHttpFilterRowStatus"),
        ("APM-MIB", "apmHttpIgnoreUnregisteredURLs"),
        ("APM-MIB", "apmHttp4xxIsFailure"),
        ("APM-MIB", "apmUserDefinedAppParentIndex"),
        ("APM-MIB", "apmUserDefinedAppApplication"))
)
if mibBuilder.loadTexts:
    apmUserDefinedApplicationsGroup.setStatus("current")

apmReportGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 3)
)
apmReportGroup.setObjects(
      *(("APM-MIB", "apmReportControlDataSource"),
        ("APM-MIB", "apmReportControlAggregationType"),
        ("APM-MIB", "apmReportControlInterval"),
        ("APM-MIB", "apmReportControlRequestedSize"),
        ("APM-MIB", "apmReportControlGrantedSize"),
        ("APM-MIB", "apmReportControlRequestedReports"),
        ("APM-MIB", "apmReportControlGrantedReports"),
        ("APM-MIB", "apmReportControlStartTime"),
        ("APM-MIB", "apmReportControlReportNumber"),
        ("APM-MIB", "apmReportControlDeniedInserts"),
        ("APM-MIB", "apmReportControlDroppedFrames"),
        ("APM-MIB", "apmReportControlOwner"),
        ("APM-MIB", "apmReportControlStorageType"),
        ("APM-MIB", "apmReportControlStatus"),
        ("APM-MIB", "apmReportTransactionCount"),
        ("APM-MIB", "apmReportSuccessfulTransactions"),
        ("APM-MIB", "apmReportResponsivenessMean"),
        ("APM-MIB", "apmReportResponsivenessMin"),
        ("APM-MIB", "apmReportResponsivenessMax"),
        ("APM-MIB", "apmReportResponsivenessB1"),
        ("APM-MIB", "apmReportResponsivenessB2"),
        ("APM-MIB", "apmReportResponsivenessB3"),
        ("APM-MIB", "apmReportResponsivenessB4"),
        ("APM-MIB", "apmReportResponsivenessB5"),
        ("APM-MIB", "apmReportResponsivenessB6"),
        ("APM-MIB", "apmReportResponsivenessB7"))
)
if mibBuilder.loadTexts:
    apmReportGroup.setStatus("current")

apmTransactionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 4)
)
apmTransactionGroup.setObjects(
      *(("APM-MIB", "apmTransactionResponsiveness"),
        ("APM-MIB", "apmTransactionAge"),
        ("APM-MIB", "apmTransactionSuccess"),
        ("APM-MIB", "apmTransactionsRequestedHistorySize"))
)
if mibBuilder.loadTexts:
    apmTransactionGroup.setStatus("current")

apmExceptionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 5)
)
apmExceptionGroup.setObjects(
      *(("APM-MIB", "apmExceptionResponsivenessComparison"),
        ("APM-MIB", "apmExceptionResponsivenessThreshold"),
        ("APM-MIB", "apmExceptionUnsuccessfulException"),
        ("APM-MIB", "apmExceptionResponsivenessEvents"),
        ("APM-MIB", "apmExceptionUnsuccessfulEvents"),
        ("APM-MIB", "apmExceptionOwner"),
        ("APM-MIB", "apmExceptionStorageType"),
        ("APM-MIB", "apmExceptionStatus"),
        ("APM-MIB", "apmThroughputExceptionMinTime"),
        ("APM-MIB", "apmNotificationMaxRate"))
)
if mibBuilder.loadTexts:
    apmExceptionGroup.setStatus("current")


# Notification objects

apmTransactionResponsivenessAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 23, 0, 1)
)
apmTransactionResponsivenessAlarm.setObjects(
      *(("APM-MIB", "apmExceptionResponsivenessThreshold"),
        ("APM-MIB", "apmTransactionResponsiveness"))
)
if mibBuilder.loadTexts:
    apmTransactionResponsivenessAlarm.setStatus(
        "current"
    )

apmTransactionUnsuccessfulAlarm = NotificationType(
    (1, 3, 6, 1, 2, 1, 16, 23, 0, 2)
)
apmTransactionUnsuccessfulAlarm.setObjects(
    ("APM-MIB", "apmExceptionResponsivenessThreshold")
)
if mibBuilder.loadTexts:
    apmTransactionUnsuccessfulAlarm.setStatus(
        "current"
    )


# Notifications groups

apmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 2, 6)
)
apmNotificationGroup.setObjects(
      *(("APM-MIB", "apmTransactionResponsivenessAlarm"),
        ("APM-MIB", "apmTransactionUnsuccessfulAlarm"))
)
if mibBuilder.loadTexts:
    apmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

apmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 16, 23, 2, 1, 1)
)
if mibBuilder.loadTexts:
    apmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "APM-MIB",
    **{"AppLocalIndex": AppLocalIndex,
       "ProtocolDirNetworkAddress": ProtocolDirNetworkAddress,
       "DataSourceOrZero": DataSourceOrZero,
       "RmonClientID": RmonClientID,
       "TransactionAggregationType": TransactionAggregationType,
       "apm": apm,
       "apmNotifications": apmNotifications,
       "apmTransactionResponsivenessAlarm": apmTransactionResponsivenessAlarm,
       "apmTransactionUnsuccessfulAlarm": apmTransactionUnsuccessfulAlarm,
       "apmMibObjects": apmMibObjects,
       "apmAppDirTable": apmAppDirTable,
       "apmAppDirEntry": apmAppDirEntry,
       "apmAppDirAppLocalIndex": apmAppDirAppLocalIndex,
       "apmAppDirResponsivenessType": apmAppDirResponsivenessType,
       "apmAppDirConfig": apmAppDirConfig,
       "apmAppDirResponsivenessBoundary1": apmAppDirResponsivenessBoundary1,
       "apmAppDirResponsivenessBoundary2": apmAppDirResponsivenessBoundary2,
       "apmAppDirResponsivenessBoundary3": apmAppDirResponsivenessBoundary3,
       "apmAppDirResponsivenessBoundary4": apmAppDirResponsivenessBoundary4,
       "apmAppDirResponsivenessBoundary5": apmAppDirResponsivenessBoundary5,
       "apmAppDirResponsivenessBoundary6": apmAppDirResponsivenessBoundary6,
       "apmBucketBoundaryLastChange": apmBucketBoundaryLastChange,
       "apmAppDirID": apmAppDirID,
       "apmHttpFilterTable": apmHttpFilterTable,
       "apmHttpFilterEntry": apmHttpFilterEntry,
       "apmHttpFilterIndex": apmHttpFilterIndex,
       "apmHttpFilterAppLocalIndex": apmHttpFilterAppLocalIndex,
       "apmHttpFilterServerProtocol": apmHttpFilterServerProtocol,
       "apmHttpFilterServerAddress": apmHttpFilterServerAddress,
       "apmHttpFilterURLPath": apmHttpFilterURLPath,
       "apmHttpFilterMatchType": apmHttpFilterMatchType,
       "apmHttpFilterOwner": apmHttpFilterOwner,
       "apmHttpFilterStorageType": apmHttpFilterStorageType,
       "apmHttpFilterRowStatus": apmHttpFilterRowStatus,
       "apmHttpIgnoreUnregisteredURLs": apmHttpIgnoreUnregisteredURLs,
       "apmHttp4xxIsFailure": apmHttp4xxIsFailure,
       "apmUserDefinedAppTable": apmUserDefinedAppTable,
       "apmUserDefinedAppEntry": apmUserDefinedAppEntry,
       "apmUserDefinedAppParentIndex": apmUserDefinedAppParentIndex,
       "apmUserDefinedAppApplication": apmUserDefinedAppApplication,
       "apmNameTable": apmNameTable,
       "apmNameEntry": apmNameEntry,
       "apmNameClientID": apmNameClientID,
       "apmNameClientAddress": apmNameClientAddress,
       "apmNameMappingStartTime": apmNameMappingStartTime,
       "apmNameMachineName": apmNameMachineName,
       "apmNameUserName": apmNameUserName,
       "apmReportControlTable": apmReportControlTable,
       "apmReportControlEntry": apmReportControlEntry,
       "apmReportControlIndex": apmReportControlIndex,
       "apmReportControlDataSource": apmReportControlDataSource,
       "apmReportControlAggregationType": apmReportControlAggregationType,
       "apmReportControlInterval": apmReportControlInterval,
       "apmReportControlRequestedSize": apmReportControlRequestedSize,
       "apmReportControlGrantedSize": apmReportControlGrantedSize,
       "apmReportControlRequestedReports": apmReportControlRequestedReports,
       "apmReportControlGrantedReports": apmReportControlGrantedReports,
       "apmReportControlStartTime": apmReportControlStartTime,
       "apmReportControlReportNumber": apmReportControlReportNumber,
       "apmReportControlDeniedInserts": apmReportControlDeniedInserts,
       "apmReportControlDroppedFrames": apmReportControlDroppedFrames,
       "apmReportControlOwner": apmReportControlOwner,
       "apmReportControlStorageType": apmReportControlStorageType,
       "apmReportControlStatus": apmReportControlStatus,
       "apmReportTable": apmReportTable,
       "apmReportEntry": apmReportEntry,
       "apmReportIndex": apmReportIndex,
       "apmReportServerAddress": apmReportServerAddress,
       "apmReportTransactionCount": apmReportTransactionCount,
       "apmReportSuccessfulTransactions": apmReportSuccessfulTransactions,
       "apmReportResponsivenessMean": apmReportResponsivenessMean,
       "apmReportResponsivenessMin": apmReportResponsivenessMin,
       "apmReportResponsivenessMax": apmReportResponsivenessMax,
       "apmReportResponsivenessB1": apmReportResponsivenessB1,
       "apmReportResponsivenessB2": apmReportResponsivenessB2,
       "apmReportResponsivenessB3": apmReportResponsivenessB3,
       "apmReportResponsivenessB4": apmReportResponsivenessB4,
       "apmReportResponsivenessB5": apmReportResponsivenessB5,
       "apmReportResponsivenessB6": apmReportResponsivenessB6,
       "apmReportResponsivenessB7": apmReportResponsivenessB7,
       "apmTransactionTable": apmTransactionTable,
       "apmTransactionEntry": apmTransactionEntry,
       "apmTransactionServerAddress": apmTransactionServerAddress,
       "apmTransactionID": apmTransactionID,
       "apmTransactionResponsiveness": apmTransactionResponsiveness,
       "apmTransactionAge": apmTransactionAge,
       "apmTransactionSuccess": apmTransactionSuccess,
       "apmTransactionsRequestedHistorySize": apmTransactionsRequestedHistorySize,
       "apmExceptionTable": apmExceptionTable,
       "apmExceptionEntry": apmExceptionEntry,
       "apmExceptionIndex": apmExceptionIndex,
       "apmExceptionResponsivenessComparison": apmExceptionResponsivenessComparison,
       "apmExceptionResponsivenessThreshold": apmExceptionResponsivenessThreshold,
       "apmExceptionUnsuccessfulException": apmExceptionUnsuccessfulException,
       "apmExceptionResponsivenessEvents": apmExceptionResponsivenessEvents,
       "apmExceptionUnsuccessfulEvents": apmExceptionUnsuccessfulEvents,
       "apmExceptionOwner": apmExceptionOwner,
       "apmExceptionStorageType": apmExceptionStorageType,
       "apmExceptionStatus": apmExceptionStatus,
       "apmThroughputExceptionMinTime": apmThroughputExceptionMinTime,
       "apmNotificationMaxRate": apmNotificationMaxRate,
       "apmConformance": apmConformance,
       "apmCompliances": apmCompliances,
       "apmCompliance": apmCompliance,
       "apmGroups": apmGroups,
       "apmAppDirGroup": apmAppDirGroup,
       "apmUserDefinedApplicationsGroup": apmUserDefinedApplicationsGroup,
       "apmReportGroup": apmReportGroup,
       "apmTransactionGroup": apmTransactionGroup,
       "apmExceptionGroup": apmExceptionGroup,
       "apmNotificationGroup": apmNotificationGroup}
)
