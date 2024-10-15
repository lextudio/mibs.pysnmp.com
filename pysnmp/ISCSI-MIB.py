# SNMP MIB module (ISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ISCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:06 2024
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

iscsiMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 142)
)
iscsiMibModule.setRevisions(
        ("2014-02-18 00:00",
         "2006-05-22 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IscsiTransportProtocol(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class IscsiDigestMethod(Integer32, TextualConvention):
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
        *(("crc32c", 4),
          ("noDigest", 3),
          ("none", 1),
          ("other", 2))
    )



class IscsiName(OctetString, TextualConvention):
    status = "current"
    displayHint = "223t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(16, 223),
    )



# MIB Managed Objects in the order of their OIDs

_IscsiNotifications_ObjectIdentity = ObjectIdentity
iscsiNotifications = _IscsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 0)
)
_IscsiObjects_ObjectIdentity = ObjectIdentity
iscsiObjects = _IscsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1)
)
_IscsiInstance_ObjectIdentity = ObjectIdentity
iscsiInstance = _IscsiInstance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 1)
)
_IscsiInstanceAttributesTable_Object = MibTable
iscsiInstanceAttributesTable = _IscsiInstanceAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesTable.setStatus("current")
_IscsiInstanceAttributesEntry_Object = MibTableRow
iscsiInstanceAttributesEntry = _IscsiInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1)
)
iscsiInstanceAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesEntry.setStatus("current")


class _IscsiInstIndex_Type(Unsigned32):
    """Custom type iscsiInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiInstIndex_Type.__name__ = "Unsigned32"
_IscsiInstIndex_Object = MibTableColumn
iscsiInstIndex = _IscsiInstIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 1),
    _IscsiInstIndex_Type()
)
iscsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiInstIndex.setStatus("current")
_IscsiInstDescr_Type = SnmpAdminString
_IscsiInstDescr_Object = MibTableColumn
iscsiInstDescr = _IscsiInstDescr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 2),
    _IscsiInstDescr_Type()
)
iscsiInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstDescr.setStatus("current")


class _IscsiInstVersionMin_Type(Unsigned32):
    """Custom type iscsiInstVersionMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiInstVersionMin_Type.__name__ = "Unsigned32"
_IscsiInstVersionMin_Object = MibTableColumn
iscsiInstVersionMin = _IscsiInstVersionMin_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 3),
    _IscsiInstVersionMin_Type()
)
iscsiInstVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVersionMin.setStatus("current")


class _IscsiInstVersionMax_Type(Unsigned32):
    """Custom type iscsiInstVersionMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiInstVersionMax_Type.__name__ = "Unsigned32"
_IscsiInstVersionMax_Object = MibTableColumn
iscsiInstVersionMax = _IscsiInstVersionMax_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 4),
    _IscsiInstVersionMax_Type()
)
iscsiInstVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVersionMax.setStatus("current")
_IscsiInstVendorID_Type = SnmpAdminString
_IscsiInstVendorID_Object = MibTableColumn
iscsiInstVendorID = _IscsiInstVendorID_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 5),
    _IscsiInstVendorID_Type()
)
iscsiInstVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVendorID.setStatus("current")
_IscsiInstVendorVersion_Type = SnmpAdminString
_IscsiInstVendorVersion_Object = MibTableColumn
iscsiInstVendorVersion = _IscsiInstVendorVersion_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 6),
    _IscsiInstVendorVersion_Type()
)
iscsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstVendorVersion.setStatus("current")
_IscsiInstPortalNumber_Type = Unsigned32
_IscsiInstPortalNumber_Object = MibTableColumn
iscsiInstPortalNumber = _IscsiInstPortalNumber_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 7),
    _IscsiInstPortalNumber_Type()
)
iscsiInstPortalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstPortalNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstPortalNumber.setUnits("transport endpoints")
_IscsiInstNodeNumber_Type = Unsigned32
_IscsiInstNodeNumber_Object = MibTableColumn
iscsiInstNodeNumber = _IscsiInstNodeNumber_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 8),
    _IscsiInstNodeNumber_Type()
)
iscsiInstNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstNodeNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstNodeNumber.setUnits("iSCSI nodes")
_IscsiInstSessionNumber_Type = Unsigned32
_IscsiInstSessionNumber_Object = MibTableColumn
iscsiInstSessionNumber = _IscsiInstSessionNumber_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 9),
    _IscsiInstSessionNumber_Type()
)
iscsiInstSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSessionNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSessionNumber.setUnits("sessions")
_IscsiInstSsnFailures_Type = Counter32
_IscsiInstSsnFailures_Object = MibTableColumn
iscsiInstSsnFailures = _IscsiInstSsnFailures_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 10),
    _IscsiInstSsnFailures_Type()
)
iscsiInstSsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnFailures.setUnits("sessions")
_IscsiInstLastSsnFailureType_Type = AutonomousType
_IscsiInstLastSsnFailureType_Object = MibTableColumn
iscsiInstLastSsnFailureType = _IscsiInstLastSsnFailureType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 11),
    _IscsiInstLastSsnFailureType_Type()
)
iscsiInstLastSsnFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstLastSsnFailureType.setStatus("current")
_IscsiInstLastSsnRmtNodeName_Type = IscsiName
_IscsiInstLastSsnRmtNodeName_Object = MibTableColumn
iscsiInstLastSsnRmtNodeName = _IscsiInstLastSsnRmtNodeName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 12),
    _IscsiInstLastSsnRmtNodeName_Type()
)
iscsiInstLastSsnRmtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstLastSsnRmtNodeName.setStatus("current")
_IscsiInstDiscontinuityTime_Type = TimeStamp
_IscsiInstDiscontinuityTime_Object = MibTableColumn
iscsiInstDiscontinuityTime = _IscsiInstDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 13),
    _IscsiInstDiscontinuityTime_Type()
)
iscsiInstDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstDiscontinuityTime.setStatus("current")
_IscsiInstXNodeArchitecture_Type = SnmpAdminString
_IscsiInstXNodeArchitecture_Object = MibTableColumn
iscsiInstXNodeArchitecture = _IscsiInstXNodeArchitecture_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 1, 1, 14),
    _IscsiInstXNodeArchitecture_Type()
)
iscsiInstXNodeArchitecture.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstXNodeArchitecture.setStatus("current")
_IscsiInstanceSsnErrorStatsTable_Object = MibTable
iscsiInstanceSsnErrorStatsTable = _IscsiInstanceSsnErrorStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsTable.setStatus("current")
_IscsiInstanceSsnErrorStatsEntry_Object = MibTableRow
iscsiInstanceSsnErrorStatsEntry = _IscsiInstanceSsnErrorStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsEntry.setStatus("current")
_IscsiInstSsnDigestErrors_Type = Counter32
_IscsiInstSsnDigestErrors_Object = MibTableColumn
iscsiInstSsnDigestErrors = _IscsiInstSsnDigestErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2, 1, 1),
    _IscsiInstSsnDigestErrors_Type()
)
iscsiInstSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnDigestErrors.setUnits("sessions")
_IscsiInstSsnCxnTimeoutErrors_Type = Counter32
_IscsiInstSsnCxnTimeoutErrors_Object = MibTableColumn
iscsiInstSsnCxnTimeoutErrors = _IscsiInstSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2, 1, 2),
    _IscsiInstSsnCxnTimeoutErrors_Type()
)
iscsiInstSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnCxnTimeoutErrors.setUnits("sessions")
_IscsiInstSsnFormatErrors_Type = Counter32
_IscsiInstSsnFormatErrors_Object = MibTableColumn
iscsiInstSsnFormatErrors = _IscsiInstSsnFormatErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2, 1, 3),
    _IscsiInstSsnFormatErrors_Type()
)
iscsiInstSsnFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnFormatErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnFormatErrors.setUnits("sessions")
_IscsiInstSsnTgtUnmappedErrors_Type = Counter32
_IscsiInstSsnTgtUnmappedErrors_Object = MibTableColumn
iscsiInstSsnTgtUnmappedErrors = _IscsiInstSsnTgtUnmappedErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 1, 2, 1, 4),
    _IscsiInstSsnTgtUnmappedErrors_Type()
)
iscsiInstSsnTgtUnmappedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiInstSsnTgtUnmappedErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiInstSsnTgtUnmappedErrors.setUnits("sessions")
_IscsiPortal_ObjectIdentity = ObjectIdentity
iscsiPortal = _IscsiPortal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 2)
)
_IscsiPortalAttributesTable_Object = MibTable
iscsiPortalAttributesTable = _IscsiPortalAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesTable.setStatus("current")
_IscsiPortalAttributesEntry_Object = MibTableRow
iscsiPortalAttributesEntry = _IscsiPortalAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1)
)
iscsiPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesEntry.setStatus("current")


class _IscsiPortalIndex_Type(Unsigned32):
    """Custom type iscsiPortalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiPortalIndex_Type.__name__ = "Unsigned32"
_IscsiPortalIndex_Object = MibTableColumn
iscsiPortalIndex = _IscsiPortalIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 1),
    _IscsiPortalIndex_Type()
)
iscsiPortalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiPortalIndex.setStatus("current")
_IscsiPortalRowStatus_Type = RowStatus
_IscsiPortalRowStatus_Object = MibTableColumn
iscsiPortalRowStatus = _IscsiPortalRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 2),
    _IscsiPortalRowStatus_Type()
)
iscsiPortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalRowStatus.setStatus("current")


class _IscsiPortalRoles_Type(Bits):
    """Custom type iscsiPortalRoles based on Bits"""
    namedValues = NamedValues(
        *(("initiatorTypePortal", 1),
          ("targetTypePortal", 0))
    )

_IscsiPortalRoles_Type.__name__ = "Bits"
_IscsiPortalRoles_Object = MibTableColumn
iscsiPortalRoles = _IscsiPortalRoles_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 3),
    _IscsiPortalRoles_Type()
)
iscsiPortalRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalRoles.setStatus("current")


class _IscsiPortalAddrType_Type(InetAddressType):
    """Custom type iscsiPortalAddrType based on InetAddressType"""


_IscsiPortalAddrType_Object = MibTableColumn
iscsiPortalAddrType = _IscsiPortalAddrType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 4),
    _IscsiPortalAddrType_Type()
)
iscsiPortalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalAddrType.setStatus("current")
_IscsiPortalAddr_Type = InetAddress
_IscsiPortalAddr_Object = MibTableColumn
iscsiPortalAddr = _IscsiPortalAddr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 5),
    _IscsiPortalAddr_Type()
)
iscsiPortalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalAddr.setStatus("current")


class _IscsiPortalProtocol_Type(IscsiTransportProtocol):
    """Custom type iscsiPortalProtocol based on IscsiTransportProtocol"""
    defaultValue = 6


_IscsiPortalProtocol_Object = MibTableColumn
iscsiPortalProtocol = _IscsiPortalProtocol_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 6),
    _IscsiPortalProtocol_Type()
)
iscsiPortalProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalProtocol.setStatus("current")


class _IscsiPortalMaxRecvDataSegLength_Type(Unsigned32):
    """Custom type iscsiPortalMaxRecvDataSegLength based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiPortalMaxRecvDataSegLength_Type.__name__ = "Unsigned32"
_IscsiPortalMaxRecvDataSegLength_Object = MibTableColumn
iscsiPortalMaxRecvDataSegLength = _IscsiPortalMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 7),
    _IscsiPortalMaxRecvDataSegLength_Type()
)
iscsiPortalMaxRecvDataSegLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalMaxRecvDataSegLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiPortalMaxRecvDataSegLength.setUnits("bytes")


class _IscsiPortalPrimaryHdrDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalPrimaryHdrDigest based on IscsiDigestMethod"""


_IscsiPortalPrimaryHdrDigest_Object = MibTableColumn
iscsiPortalPrimaryHdrDigest = _IscsiPortalPrimaryHdrDigest_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 8),
    _IscsiPortalPrimaryHdrDigest_Type()
)
iscsiPortalPrimaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalPrimaryHdrDigest.setStatus("current")


class _IscsiPortalPrimaryDataDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalPrimaryDataDigest based on IscsiDigestMethod"""


_IscsiPortalPrimaryDataDigest_Object = MibTableColumn
iscsiPortalPrimaryDataDigest = _IscsiPortalPrimaryDataDigest_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 9),
    _IscsiPortalPrimaryDataDigest_Type()
)
iscsiPortalPrimaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalPrimaryDataDigest.setStatus("current")


class _IscsiPortalSecondaryHdrDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalSecondaryHdrDigest based on IscsiDigestMethod"""


_IscsiPortalSecondaryHdrDigest_Object = MibTableColumn
iscsiPortalSecondaryHdrDigest = _IscsiPortalSecondaryHdrDigest_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 10),
    _IscsiPortalSecondaryHdrDigest_Type()
)
iscsiPortalSecondaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalSecondaryHdrDigest.setStatus("current")


class _IscsiPortalSecondaryDataDigest_Type(IscsiDigestMethod):
    """Custom type iscsiPortalSecondaryDataDigest based on IscsiDigestMethod"""


_IscsiPortalSecondaryDataDigest_Object = MibTableColumn
iscsiPortalSecondaryDataDigest = _IscsiPortalSecondaryDataDigest_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 11),
    _IscsiPortalSecondaryDataDigest_Type()
)
iscsiPortalSecondaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalSecondaryDataDigest.setStatus("current")


class _IscsiPortalRecvMarker_Type(TruthValue):
    """Custom type iscsiPortalRecvMarker based on TruthValue"""


_IscsiPortalRecvMarker_Object = MibTableColumn
iscsiPortalRecvMarker = _IscsiPortalRecvMarker_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 12),
    _IscsiPortalRecvMarker_Type()
)
iscsiPortalRecvMarker.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalRecvMarker.setStatus("deprecated")


class _IscsiPortalStorageType_Type(StorageType):
    """Custom type iscsiPortalStorageType based on StorageType"""


_IscsiPortalStorageType_Object = MibTableColumn
iscsiPortalStorageType = _IscsiPortalStorageType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 13),
    _IscsiPortalStorageType_Type()
)
iscsiPortalStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiPortalStorageType.setStatus("current")
_IscsiPortalDescr_Type = SnmpAdminString
_IscsiPortalDescr_Object = MibTableColumn
iscsiPortalDescr = _IscsiPortalDescr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 2, 1, 1, 14),
    _IscsiPortalDescr_Type()
)
iscsiPortalDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiPortalDescr.setStatus("current")
_IscsiTargetPortal_ObjectIdentity = ObjectIdentity
iscsiTargetPortal = _IscsiTargetPortal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 3)
)
_IscsiTgtPortalAttributesTable_Object = MibTable
iscsiTgtPortalAttributesTable = _IscsiTgtPortalAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesTable.setStatus("current")
_IscsiTgtPortalAttributesEntry_Object = MibTableRow
iscsiTgtPortalAttributesEntry = _IscsiTgtPortalAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 3, 1, 1)
)
iscsiTgtPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
    (0, "ISCSI-MIB", "iscsiTgtPortalNodeIndexOrZero"),
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesEntry.setStatus("current")


class _IscsiTgtPortalNodeIndexOrZero_Type(Unsigned32):
    """Custom type iscsiTgtPortalNodeIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IscsiTgtPortalNodeIndexOrZero_Type.__name__ = "Unsigned32"
_IscsiTgtPortalNodeIndexOrZero_Object = MibTableColumn
iscsiTgtPortalNodeIndexOrZero = _IscsiTgtPortalNodeIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 3, 1, 1, 1),
    _IscsiTgtPortalNodeIndexOrZero_Type()
)
iscsiTgtPortalNodeIndexOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiTgtPortalNodeIndexOrZero.setStatus("current")


class _IscsiTgtPortalPort_Type(InetPortNumber):
    """Custom type iscsiTgtPortalPort based on InetPortNumber"""
    subtypeSpec = InetPortNumber.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiTgtPortalPort_Type.__name__ = "InetPortNumber"
_IscsiTgtPortalPort_Object = MibTableColumn
iscsiTgtPortalPort = _IscsiTgtPortalPort_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 3, 1, 1, 2),
    _IscsiTgtPortalPort_Type()
)
iscsiTgtPortalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTgtPortalPort.setStatus("current")


class _IscsiTgtPortalTag_Type(Unsigned32):
    """Custom type iscsiTgtPortalTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiTgtPortalTag_Type.__name__ = "Unsigned32"
_IscsiTgtPortalTag_Object = MibTableColumn
iscsiTgtPortalTag = _IscsiTgtPortalTag_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 3, 1, 1, 3),
    _IscsiTgtPortalTag_Type()
)
iscsiTgtPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiTgtPortalTag.setStatus("current")
_IscsiInitiatorPortal_ObjectIdentity = ObjectIdentity
iscsiInitiatorPortal = _IscsiInitiatorPortal_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 4)
)
_IscsiIntrPortalAttributesTable_Object = MibTable
iscsiIntrPortalAttributesTable = _IscsiIntrPortalAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 4, 1)
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesTable.setStatus("current")
_IscsiIntrPortalAttributesEntry_Object = MibTableRow
iscsiIntrPortalAttributesEntry = _IscsiIntrPortalAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 4, 1, 1)
)
iscsiIntrPortalAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiPortalIndex"),
    (0, "ISCSI-MIB", "iscsiIntrPortalNodeIndexOrZero"),
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesEntry.setStatus("current")


class _IscsiIntrPortalNodeIndexOrZero_Type(Unsigned32):
    """Custom type iscsiIntrPortalNodeIndexOrZero based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IscsiIntrPortalNodeIndexOrZero_Type.__name__ = "Unsigned32"
_IscsiIntrPortalNodeIndexOrZero_Object = MibTableColumn
iscsiIntrPortalNodeIndexOrZero = _IscsiIntrPortalNodeIndexOrZero_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 4, 1, 1, 1),
    _IscsiIntrPortalNodeIndexOrZero_Type()
)
iscsiIntrPortalNodeIndexOrZero.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiIntrPortalNodeIndexOrZero.setStatus("current")


class _IscsiIntrPortalTag_Type(Unsigned32):
    """Custom type iscsiIntrPortalTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiIntrPortalTag_Type.__name__ = "Unsigned32"
_IscsiIntrPortalTag_Object = MibTableColumn
iscsiIntrPortalTag = _IscsiIntrPortalTag_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 4, 1, 1, 2),
    _IscsiIntrPortalTag_Type()
)
iscsiIntrPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiIntrPortalTag.setStatus("current")
_IscsiNode_ObjectIdentity = ObjectIdentity
iscsiNode = _IscsiNode_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 5)
)
_IscsiNodeAttributesTable_Object = MibTable
iscsiNodeAttributesTable = _IscsiNodeAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1)
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesTable.setStatus("current")
_IscsiNodeAttributesEntry_Object = MibTableRow
iscsiNodeAttributesEntry = _IscsiNodeAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1)
)
iscsiNodeAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesEntry.setStatus("current")


class _IscsiNodeIndex_Type(Unsigned32):
    """Custom type iscsiNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiNodeIndex_Type.__name__ = "Unsigned32"
_IscsiNodeIndex_Object = MibTableColumn
iscsiNodeIndex = _IscsiNodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 1),
    _IscsiNodeIndex_Type()
)
iscsiNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiNodeIndex.setStatus("current")
_IscsiNodeName_Type = IscsiName
_IscsiNodeName_Object = MibTableColumn
iscsiNodeName = _IscsiNodeName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 2),
    _IscsiNodeName_Type()
)
iscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeName.setStatus("current")
_IscsiNodeAlias_Type = SnmpAdminString
_IscsiNodeAlias_Object = MibTableColumn
iscsiNodeAlias = _IscsiNodeAlias_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 3),
    _IscsiNodeAlias_Type()
)
iscsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeAlias.setStatus("current")


class _IscsiNodeRoles_Type(Bits):
    """Custom type iscsiNodeRoles based on Bits"""
    namedValues = NamedValues(
        *(("initiatorTypeNode", 1),
          ("targetTypeNode", 0))
    )

_IscsiNodeRoles_Type.__name__ = "Bits"
_IscsiNodeRoles_Object = MibTableColumn
iscsiNodeRoles = _IscsiNodeRoles_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 4),
    _IscsiNodeRoles_Type()
)
iscsiNodeRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeRoles.setStatus("current")
_IscsiNodeTransportType_Type = RowPointer
_IscsiNodeTransportType_Object = MibTableColumn
iscsiNodeTransportType = _IscsiNodeTransportType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 5),
    _IscsiNodeTransportType_Type()
)
iscsiNodeTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeTransportType.setStatus("current")
_IscsiNodeInitialR2T_Type = TruthValue
_IscsiNodeInitialR2T_Object = MibTableColumn
iscsiNodeInitialR2T = _IscsiNodeInitialR2T_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 6),
    _IscsiNodeInitialR2T_Type()
)
iscsiNodeInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeInitialR2T.setStatus("current")


class _IscsiNodeImmediateData_Type(TruthValue):
    """Custom type iscsiNodeImmediateData based on TruthValue"""


_IscsiNodeImmediateData_Object = MibTableColumn
iscsiNodeImmediateData = _IscsiNodeImmediateData_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 7),
    _IscsiNodeImmediateData_Type()
)
iscsiNodeImmediateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeImmediateData.setStatus("current")


class _IscsiNodeMaxOutstandingR2T_Type(Unsigned32):
    """Custom type iscsiNodeMaxOutstandingR2T based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiNodeMaxOutstandingR2T_Type.__name__ = "Unsigned32"
_IscsiNodeMaxOutstandingR2T_Object = MibTableColumn
iscsiNodeMaxOutstandingR2T = _IscsiNodeMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 8),
    _IscsiNodeMaxOutstandingR2T_Type()
)
iscsiNodeMaxOutstandingR2T.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxOutstandingR2T.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeMaxOutstandingR2T.setUnits("R2Ts")


class _IscsiNodeFirstBurstLength_Type(Unsigned32):
    """Custom type iscsiNodeFirstBurstLength based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiNodeFirstBurstLength_Type.__name__ = "Unsigned32"
_IscsiNodeFirstBurstLength_Object = MibTableColumn
iscsiNodeFirstBurstLength = _IscsiNodeFirstBurstLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 9),
    _IscsiNodeFirstBurstLength_Type()
)
iscsiNodeFirstBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeFirstBurstLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeFirstBurstLength.setUnits("bytes")


class _IscsiNodeMaxBurstLength_Type(Unsigned32):
    """Custom type iscsiNodeMaxBurstLength based on Unsigned32"""
    defaultValue = 262144

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiNodeMaxBurstLength_Type.__name__ = "Unsigned32"
_IscsiNodeMaxBurstLength_Object = MibTableColumn
iscsiNodeMaxBurstLength = _IscsiNodeMaxBurstLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 10),
    _IscsiNodeMaxBurstLength_Type()
)
iscsiNodeMaxBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxBurstLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeMaxBurstLength.setUnits("bytes")


class _IscsiNodeMaxConnections_Type(Unsigned32):
    """Custom type iscsiNodeMaxConnections based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiNodeMaxConnections_Type.__name__ = "Unsigned32"
_IscsiNodeMaxConnections_Object = MibTableColumn
iscsiNodeMaxConnections = _IscsiNodeMaxConnections_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 11),
    _IscsiNodeMaxConnections_Type()
)
iscsiNodeMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeMaxConnections.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeMaxConnections.setUnits("connections")


class _IscsiNodeDataSequenceInOrder_Type(TruthValue):
    """Custom type iscsiNodeDataSequenceInOrder based on TruthValue"""


_IscsiNodeDataSequenceInOrder_Object = MibTableColumn
iscsiNodeDataSequenceInOrder = _IscsiNodeDataSequenceInOrder_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 12),
    _IscsiNodeDataSequenceInOrder_Type()
)
iscsiNodeDataSequenceInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDataSequenceInOrder.setStatus("current")


class _IscsiNodeDataPDUInOrder_Type(TruthValue):
    """Custom type iscsiNodeDataPDUInOrder based on TruthValue"""


_IscsiNodeDataPDUInOrder_Object = MibTableColumn
iscsiNodeDataPDUInOrder = _IscsiNodeDataPDUInOrder_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 13),
    _IscsiNodeDataPDUInOrder_Type()
)
iscsiNodeDataPDUInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDataPDUInOrder.setStatus("current")


class _IscsiNodeDefaultTime2Wait_Type(Unsigned32):
    """Custom type iscsiNodeDefaultTime2Wait based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IscsiNodeDefaultTime2Wait_Type.__name__ = "Unsigned32"
_IscsiNodeDefaultTime2Wait_Object = MibTableColumn
iscsiNodeDefaultTime2Wait = _IscsiNodeDefaultTime2Wait_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 14),
    _IscsiNodeDefaultTime2Wait_Type()
)
iscsiNodeDefaultTime2Wait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Wait.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Wait.setUnits("seconds")


class _IscsiNodeDefaultTime2Retain_Type(Unsigned32):
    """Custom type iscsiNodeDefaultTime2Retain based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_IscsiNodeDefaultTime2Retain_Type.__name__ = "Unsigned32"
_IscsiNodeDefaultTime2Retain_Object = MibTableColumn
iscsiNodeDefaultTime2Retain = _IscsiNodeDefaultTime2Retain_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 15),
    _IscsiNodeDefaultTime2Retain_Type()
)
iscsiNodeDefaultTime2Retain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Retain.setStatus("current")
if mibBuilder.loadTexts:
    iscsiNodeDefaultTime2Retain.setUnits("seconds")


class _IscsiNodeErrorRecoveryLevel_Type(Unsigned32):
    """Custom type iscsiNodeErrorRecoveryLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiNodeErrorRecoveryLevel_Type.__name__ = "Unsigned32"
_IscsiNodeErrorRecoveryLevel_Object = MibTableColumn
iscsiNodeErrorRecoveryLevel = _IscsiNodeErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 16),
    _IscsiNodeErrorRecoveryLevel_Type()
)
iscsiNodeErrorRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeErrorRecoveryLevel.setStatus("current")
_IscsiNodeDiscontinuityTime_Type = TimeStamp
_IscsiNodeDiscontinuityTime_Object = MibTableColumn
iscsiNodeDiscontinuityTime = _IscsiNodeDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 17),
    _IscsiNodeDiscontinuityTime_Type()
)
iscsiNodeDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiNodeDiscontinuityTime.setStatus("current")


class _IscsiNodeStorageType_Type(StorageType):
    """Custom type iscsiNodeStorageType based on StorageType"""


_IscsiNodeStorageType_Object = MibTableColumn
iscsiNodeStorageType = _IscsiNodeStorageType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 5, 1, 1, 18),
    _IscsiNodeStorageType_Type()
)
iscsiNodeStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iscsiNodeStorageType.setStatus("current")
_IscsiTarget_ObjectIdentity = ObjectIdentity
iscsiTarget = _IscsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 6)
)
_IscsiTargetAttributesTable_Object = MibTable
iscsiTargetAttributesTable = _IscsiTargetAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesTable.setStatus("current")
_IscsiTargetAttributesEntry_Object = MibTableRow
iscsiTargetAttributesEntry = _IscsiTargetAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1)
)
iscsiTargetAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesEntry.setStatus("current")
_IscsiTgtLoginFailures_Type = Counter32
_IscsiTgtLoginFailures_Object = MibTableColumn
iscsiTgtLoginFailures = _IscsiTgtLoginFailures_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 1),
    _IscsiTgtLoginFailures_Type()
)
iscsiTgtLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginFailures.setUnits("failed login attempts")
_IscsiTgtLastFailureTime_Type = TimeStamp
_IscsiTgtLastFailureTime_Object = MibTableColumn
iscsiTgtLastFailureTime = _IscsiTgtLastFailureTime_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 2),
    _IscsiTgtLastFailureTime_Type()
)
iscsiTgtLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastFailureTime.setStatus("current")
_IscsiTgtLastFailureType_Type = AutonomousType
_IscsiTgtLastFailureType_Object = MibTableColumn
iscsiTgtLastFailureType = _IscsiTgtLastFailureType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 3),
    _IscsiTgtLastFailureType_Type()
)
iscsiTgtLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastFailureType.setStatus("current")
_IscsiTgtLastIntrFailureName_Type = IscsiName
_IscsiTgtLastIntrFailureName_Object = MibTableColumn
iscsiTgtLastIntrFailureName = _IscsiTgtLastIntrFailureName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 4),
    _IscsiTgtLastIntrFailureName_Type()
)
iscsiTgtLastIntrFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureName.setStatus("current")
_IscsiTgtLastIntrFailureAddrType_Type = InetAddressType
_IscsiTgtLastIntrFailureAddrType_Object = MibTableColumn
iscsiTgtLastIntrFailureAddrType = _IscsiTgtLastIntrFailureAddrType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 5),
    _IscsiTgtLastIntrFailureAddrType_Type()
)
iscsiTgtLastIntrFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureAddrType.setStatus("current")
_IscsiTgtLastIntrFailureAddr_Type = InetAddress
_IscsiTgtLastIntrFailureAddr_Object = MibTableColumn
iscsiTgtLastIntrFailureAddr = _IscsiTgtLastIntrFailureAddr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 6),
    _IscsiTgtLastIntrFailureAddr_Type()
)
iscsiTgtLastIntrFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailureAddr.setStatus("current")
_IscsiTgtLastIntrFailurePort_Type = InetPortNumber
_IscsiTgtLastIntrFailurePort_Object = MibTableColumn
iscsiTgtLastIntrFailurePort = _IscsiTgtLastIntrFailurePort_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 1, 1, 7),
    _IscsiTgtLastIntrFailurePort_Type()
)
iscsiTgtLastIntrFailurePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLastIntrFailurePort.setStatus("current")
_IscsiTargetLoginStatsTable_Object = MibTable
iscsiTargetLoginStatsTable = _IscsiTargetLoginStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2)
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsTable.setStatus("current")
_IscsiTargetLoginStatsEntry_Object = MibTableRow
iscsiTargetLoginStatsEntry = _IscsiTargetLoginStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsEntry.setStatus("current")
_IscsiTgtLoginAccepts_Type = Counter32
_IscsiTgtLoginAccepts_Object = MibTableColumn
iscsiTgtLoginAccepts = _IscsiTgtLoginAccepts_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 1),
    _IscsiTgtLoginAccepts_Type()
)
iscsiTgtLoginAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAccepts.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAccepts.setUnits("successful logins")
_IscsiTgtLoginOtherFails_Type = Counter32
_IscsiTgtLoginOtherFails_Object = MibTableColumn
iscsiTgtLoginOtherFails = _IscsiTgtLoginOtherFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 2),
    _IscsiTgtLoginOtherFails_Type()
)
iscsiTgtLoginOtherFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginOtherFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginOtherFails.setUnits("failed logins")
_IscsiTgtLoginRedirects_Type = Counter32
_IscsiTgtLoginRedirects_Object = MibTableColumn
iscsiTgtLoginRedirects = _IscsiTgtLoginRedirects_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 3),
    _IscsiTgtLoginRedirects_Type()
)
iscsiTgtLoginRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginRedirects.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginRedirects.setUnits("redirected logins")
_IscsiTgtLoginAuthorizeFails_Type = Counter32
_IscsiTgtLoginAuthorizeFails_Object = MibTableColumn
iscsiTgtLoginAuthorizeFails = _IscsiTgtLoginAuthorizeFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 4),
    _IscsiTgtLoginAuthorizeFails_Type()
)
iscsiTgtLoginAuthorizeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthorizeFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthorizeFails.setUnits("failed logins")
_IscsiTgtLoginAuthenticateFails_Type = Counter32
_IscsiTgtLoginAuthenticateFails_Object = MibTableColumn
iscsiTgtLoginAuthenticateFails = _IscsiTgtLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 5),
    _IscsiTgtLoginAuthenticateFails_Type()
)
iscsiTgtLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginAuthenticateFails.setUnits("failed logins")
_IscsiTgtLoginNegotiateFails_Type = Counter32
_IscsiTgtLoginNegotiateFails_Object = MibTableColumn
iscsiTgtLoginNegotiateFails = _IscsiTgtLoginNegotiateFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 2, 1, 6),
    _IscsiTgtLoginNegotiateFails_Type()
)
iscsiTgtLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLoginNegotiateFails.setUnits("failed logins")
_IscsiTargetLogoutStatsTable_Object = MibTable
iscsiTargetLogoutStatsTable = _IscsiTargetLogoutStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3)
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsTable.setStatus("current")
_IscsiTargetLogoutStatsEntry_Object = MibTableRow
iscsiTargetLogoutStatsEntry = _IscsiTargetLogoutStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsEntry.setStatus("current")
_IscsiTgtLogoutNormals_Type = Counter32
_IscsiTgtLogoutNormals_Object = MibTableColumn
iscsiTgtLogoutNormals = _IscsiTgtLogoutNormals_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3, 1, 1),
    _IscsiTgtLogoutNormals_Type()
)
iscsiTgtLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutNormals.setUnits("normal logouts")
_IscsiTgtLogoutOthers_Type = Counter32
_IscsiTgtLogoutOthers_Object = MibTableColumn
iscsiTgtLogoutOthers = _IscsiTgtLogoutOthers_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3, 1, 2),
    _IscsiTgtLogoutOthers_Type()
)
iscsiTgtLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutOthers.setUnits("abnormal logouts")
_IscsiTgtLogoutCxnClosed_Type = Counter32
_IscsiTgtLogoutCxnClosed_Object = MibTableColumn
iscsiTgtLogoutCxnClosed = _IscsiTgtLogoutCxnClosed_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3, 1, 3),
    _IscsiTgtLogoutCxnClosed_Type()
)
iscsiTgtLogoutCxnClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutCxnClosed.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutCxnClosed.setUnits("abnormal logouts")
_IscsiTgtLogoutCxnRemoved_Type = Counter32
_IscsiTgtLogoutCxnRemoved_Object = MibTableColumn
iscsiTgtLogoutCxnRemoved = _IscsiTgtLogoutCxnRemoved_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 6, 3, 1, 4),
    _IscsiTgtLogoutCxnRemoved_Type()
)
iscsiTgtLogoutCxnRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiTgtLogoutCxnRemoved.setStatus("current")
if mibBuilder.loadTexts:
    iscsiTgtLogoutCxnRemoved.setUnits("abnormal logouts")
_IscsiTgtAuthorization_ObjectIdentity = ObjectIdentity
iscsiTgtAuthorization = _IscsiTgtAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 7)
)
_IscsiTgtAuthAttributesTable_Object = MibTable
iscsiTgtAuthAttributesTable = _IscsiTgtAuthAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1)
)
if mibBuilder.loadTexts:
    iscsiTgtAuthAttributesTable.setStatus("current")
_IscsiTgtAuthAttributesEntry_Object = MibTableRow
iscsiTgtAuthAttributesEntry = _IscsiTgtAuthAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1, 1)
)
iscsiTgtAuthAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiTgtAuthIndex"),
)
if mibBuilder.loadTexts:
    iscsiTgtAuthAttributesEntry.setStatus("current")


class _IscsiTgtAuthIndex_Type(Unsigned32):
    """Custom type iscsiTgtAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiTgtAuthIndex_Type.__name__ = "Unsigned32"
_IscsiTgtAuthIndex_Object = MibTableColumn
iscsiTgtAuthIndex = _IscsiTgtAuthIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1, 1, 1),
    _IscsiTgtAuthIndex_Type()
)
iscsiTgtAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiTgtAuthIndex.setStatus("current")
_IscsiTgtAuthRowStatus_Type = RowStatus
_IscsiTgtAuthRowStatus_Object = MibTableColumn
iscsiTgtAuthRowStatus = _IscsiTgtAuthRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1, 1, 2),
    _IscsiTgtAuthRowStatus_Type()
)
iscsiTgtAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiTgtAuthRowStatus.setStatus("current")
_IscsiTgtAuthIdentity_Type = RowPointer
_IscsiTgtAuthIdentity_Object = MibTableColumn
iscsiTgtAuthIdentity = _IscsiTgtAuthIdentity_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1, 1, 3),
    _IscsiTgtAuthIdentity_Type()
)
iscsiTgtAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiTgtAuthIdentity.setStatus("current")


class _IscsiTgtAuthStorageType_Type(StorageType):
    """Custom type iscsiTgtAuthStorageType based on StorageType"""


_IscsiTgtAuthStorageType_Object = MibTableColumn
iscsiTgtAuthStorageType = _IscsiTgtAuthStorageType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 7, 1, 1, 4),
    _IscsiTgtAuthStorageType_Type()
)
iscsiTgtAuthStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiTgtAuthStorageType.setStatus("current")
_IscsiInitiator_ObjectIdentity = ObjectIdentity
iscsiInitiator = _IscsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 8)
)
_IscsiInitiatorAttributesTable_Object = MibTable
iscsiInitiatorAttributesTable = _IscsiInitiatorAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesTable.setStatus("current")
_IscsiInitiatorAttributesEntry_Object = MibTableRow
iscsiInitiatorAttributesEntry = _IscsiInitiatorAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1)
)
iscsiInitiatorAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesEntry.setStatus("current")
_IscsiIntrLoginFailures_Type = Counter32
_IscsiIntrLoginFailures_Object = MibTableColumn
iscsiIntrLoginFailures = _IscsiIntrLoginFailures_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 1),
    _IscsiIntrLoginFailures_Type()
)
iscsiIntrLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginFailures.setUnits("failed logins")
_IscsiIntrLastFailureTime_Type = TimeStamp
_IscsiIntrLastFailureTime_Object = MibTableColumn
iscsiIntrLastFailureTime = _IscsiIntrLastFailureTime_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 2),
    _IscsiIntrLastFailureTime_Type()
)
iscsiIntrLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastFailureTime.setStatus("current")
_IscsiIntrLastFailureType_Type = AutonomousType
_IscsiIntrLastFailureType_Object = MibTableColumn
iscsiIntrLastFailureType = _IscsiIntrLastFailureType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 3),
    _IscsiIntrLastFailureType_Type()
)
iscsiIntrLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastFailureType.setStatus("current")
_IscsiIntrLastTgtFailureName_Type = IscsiName
_IscsiIntrLastTgtFailureName_Object = MibTableColumn
iscsiIntrLastTgtFailureName = _IscsiIntrLastTgtFailureName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 4),
    _IscsiIntrLastTgtFailureName_Type()
)
iscsiIntrLastTgtFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureName.setStatus("current")
_IscsiIntrLastTgtFailureAddrType_Type = InetAddressType
_IscsiIntrLastTgtFailureAddrType_Object = MibTableColumn
iscsiIntrLastTgtFailureAddrType = _IscsiIntrLastTgtFailureAddrType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 5),
    _IscsiIntrLastTgtFailureAddrType_Type()
)
iscsiIntrLastTgtFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureAddrType.setStatus("current")
_IscsiIntrLastTgtFailureAddr_Type = InetAddress
_IscsiIntrLastTgtFailureAddr_Object = MibTableColumn
iscsiIntrLastTgtFailureAddr = _IscsiIntrLastTgtFailureAddr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 6),
    _IscsiIntrLastTgtFailureAddr_Type()
)
iscsiIntrLastTgtFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailureAddr.setStatus("current")
_IscsiIntrLastTgtFailurePort_Type = InetPortNumber
_IscsiIntrLastTgtFailurePort_Object = MibTableColumn
iscsiIntrLastTgtFailurePort = _IscsiIntrLastTgtFailurePort_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 1, 1, 7),
    _IscsiIntrLastTgtFailurePort_Type()
)
iscsiIntrLastTgtFailurePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLastTgtFailurePort.setStatus("current")
_IscsiInitiatorLoginStatsTable_Object = MibTable
iscsiInitiatorLoginStatsTable = _IscsiInitiatorLoginStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsTable.setStatus("current")
_IscsiInitiatorLoginStatsEntry_Object = MibTableRow
iscsiInitiatorLoginStatsEntry = _IscsiInitiatorLoginStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsEntry.setStatus("current")
_IscsiIntrLoginAcceptRsps_Type = Counter32
_IscsiIntrLoginAcceptRsps_Object = MibTableColumn
iscsiIntrLoginAcceptRsps = _IscsiIntrLoginAcceptRsps_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 1),
    _IscsiIntrLoginAcceptRsps_Type()
)
iscsiIntrLoginAcceptRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAcceptRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAcceptRsps.setUnits("successful logins")
_IscsiIntrLoginOtherFailRsps_Type = Counter32
_IscsiIntrLoginOtherFailRsps_Object = MibTableColumn
iscsiIntrLoginOtherFailRsps = _IscsiIntrLoginOtherFailRsps_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 2),
    _IscsiIntrLoginOtherFailRsps_Type()
)
iscsiIntrLoginOtherFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginOtherFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginOtherFailRsps.setUnits("failed logins")
_IscsiIntrLoginRedirectRsps_Type = Counter32
_IscsiIntrLoginRedirectRsps_Object = MibTableColumn
iscsiIntrLoginRedirectRsps = _IscsiIntrLoginRedirectRsps_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 3),
    _IscsiIntrLoginRedirectRsps_Type()
)
iscsiIntrLoginRedirectRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginRedirectRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginRedirectRsps.setUnits("failed logins")
_IscsiIntrLoginAuthFailRsps_Type = Counter32
_IscsiIntrLoginAuthFailRsps_Object = MibTableColumn
iscsiIntrLoginAuthFailRsps = _IscsiIntrLoginAuthFailRsps_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 4),
    _IscsiIntrLoginAuthFailRsps_Type()
)
iscsiIntrLoginAuthFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthFailRsps.setUnits("failed logins")
_IscsiIntrLoginAuthenticateFails_Type = Counter32
_IscsiIntrLoginAuthenticateFails_Object = MibTableColumn
iscsiIntrLoginAuthenticateFails = _IscsiIntrLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 5),
    _IscsiIntrLoginAuthenticateFails_Type()
)
iscsiIntrLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthenticateFails.setUnits("failed logins")
_IscsiIntrLoginNegotiateFails_Type = Counter32
_IscsiIntrLoginNegotiateFails_Object = MibTableColumn
iscsiIntrLoginNegotiateFails = _IscsiIntrLoginNegotiateFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 6),
    _IscsiIntrLoginNegotiateFails_Type()
)
iscsiIntrLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginNegotiateFails.setUnits("failed logins")
_IscsiIntrLoginAuthorizeFails_Type = Counter32
_IscsiIntrLoginAuthorizeFails_Object = MibTableColumn
iscsiIntrLoginAuthorizeFails = _IscsiIntrLoginAuthorizeFails_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 2, 1, 7),
    _IscsiIntrLoginAuthorizeFails_Type()
)
iscsiIntrLoginAuthorizeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthorizeFails.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLoginAuthorizeFails.setUnits("failed logins")
_IscsiInitiatorLogoutStatsTable_Object = MibTable
iscsiInitiatorLogoutStatsTable = _IscsiInitiatorLogoutStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 3)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsTable.setStatus("current")
_IscsiInitiatorLogoutStatsEntry_Object = MibTableRow
iscsiInitiatorLogoutStatsEntry = _IscsiInitiatorLogoutStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsEntry.setStatus("current")
_IscsiIntrLogoutNormals_Type = Counter32
_IscsiIntrLogoutNormals_Object = MibTableColumn
iscsiIntrLogoutNormals = _IscsiIntrLogoutNormals_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 3, 1, 1),
    _IscsiIntrLogoutNormals_Type()
)
iscsiIntrLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLogoutNormals.setUnits("normal logouts")
_IscsiIntrLogoutOthers_Type = Counter32
_IscsiIntrLogoutOthers_Object = MibTableColumn
iscsiIntrLogoutOthers = _IscsiIntrLogoutOthers_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 8, 3, 1, 2),
    _IscsiIntrLogoutOthers_Type()
)
iscsiIntrLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiIntrLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    iscsiIntrLogoutOthers.setUnits("abnormal logouts")
_IscsiIntrAuthorization_ObjectIdentity = ObjectIdentity
iscsiIntrAuthorization = _IscsiIntrAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 9)
)
_IscsiIntrAuthAttributesTable_Object = MibTable
iscsiIntrAuthAttributesTable = _IscsiIntrAuthAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1)
)
if mibBuilder.loadTexts:
    iscsiIntrAuthAttributesTable.setStatus("current")
_IscsiIntrAuthAttributesEntry_Object = MibTableRow
iscsiIntrAuthAttributesEntry = _IscsiIntrAuthAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1, 1)
)
iscsiIntrAuthAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiNodeIndex"),
    (0, "ISCSI-MIB", "iscsiIntrAuthIndex"),
)
if mibBuilder.loadTexts:
    iscsiIntrAuthAttributesEntry.setStatus("current")


class _IscsiIntrAuthIndex_Type(Unsigned32):
    """Custom type iscsiIntrAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiIntrAuthIndex_Type.__name__ = "Unsigned32"
_IscsiIntrAuthIndex_Object = MibTableColumn
iscsiIntrAuthIndex = _IscsiIntrAuthIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1, 1, 1),
    _IscsiIntrAuthIndex_Type()
)
iscsiIntrAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiIntrAuthIndex.setStatus("current")
_IscsiIntrAuthRowStatus_Type = RowStatus
_IscsiIntrAuthRowStatus_Object = MibTableColumn
iscsiIntrAuthRowStatus = _IscsiIntrAuthRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1, 1, 2),
    _IscsiIntrAuthRowStatus_Type()
)
iscsiIntrAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiIntrAuthRowStatus.setStatus("current")
_IscsiIntrAuthIdentity_Type = RowPointer
_IscsiIntrAuthIdentity_Object = MibTableColumn
iscsiIntrAuthIdentity = _IscsiIntrAuthIdentity_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1, 1, 3),
    _IscsiIntrAuthIdentity_Type()
)
iscsiIntrAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiIntrAuthIdentity.setStatus("current")


class _IscsiIntrAuthStorageType_Type(StorageType):
    """Custom type iscsiIntrAuthStorageType based on StorageType"""


_IscsiIntrAuthStorageType_Object = MibTableColumn
iscsiIntrAuthStorageType = _IscsiIntrAuthStorageType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 9, 1, 1, 4),
    _IscsiIntrAuthStorageType_Type()
)
iscsiIntrAuthStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iscsiIntrAuthStorageType.setStatus("current")
_IscsiSession_ObjectIdentity = ObjectIdentity
iscsiSession = _IscsiSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 10)
)
_IscsiSessionAttributesTable_Object = MibTable
iscsiSessionAttributesTable = _IscsiSessionAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesTable.setStatus("current")
_IscsiSessionAttributesEntry_Object = MibTableRow
iscsiSessionAttributesEntry = _IscsiSessionAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1)
)
iscsiSessionAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiSsnNodeIndex"),
    (0, "ISCSI-MIB", "iscsiSsnIndex"),
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesEntry.setStatus("current")


class _IscsiSsnNodeIndex_Type(Unsigned32):
    """Custom type iscsiSsnNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_IscsiSsnNodeIndex_Type.__name__ = "Unsigned32"
_IscsiSsnNodeIndex_Object = MibTableColumn
iscsiSsnNodeIndex = _IscsiSsnNodeIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 1),
    _IscsiSsnNodeIndex_Type()
)
iscsiSsnNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiSsnNodeIndex.setStatus("current")


class _IscsiSsnIndex_Type(Unsigned32):
    """Custom type iscsiSsnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiSsnIndex_Type.__name__ = "Unsigned32"
_IscsiSsnIndex_Object = MibTableColumn
iscsiSsnIndex = _IscsiSsnIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 2),
    _IscsiSsnIndex_Type()
)
iscsiSsnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiSsnIndex.setStatus("current")


class _IscsiSsnDirection_Type(Integer32):
    """Custom type iscsiSsnDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inboundSession", 1),
          ("outboundSession", 2))
    )


_IscsiSsnDirection_Type.__name__ = "Integer32"
_IscsiSsnDirection_Object = MibTableColumn
iscsiSsnDirection = _IscsiSsnDirection_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 3),
    _IscsiSsnDirection_Type()
)
iscsiSsnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDirection.setStatus("current")
_IscsiSsnInitiatorName_Type = IscsiName
_IscsiSsnInitiatorName_Object = MibTableColumn
iscsiSsnInitiatorName = _IscsiSsnInitiatorName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 4),
    _IscsiSsnInitiatorName_Type()
)
iscsiSsnInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitiatorName.setStatus("current")
_IscsiSsnTargetName_Type = IscsiName
_IscsiSsnTargetName_Object = MibTableColumn
iscsiSsnTargetName = _IscsiSsnTargetName_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 5),
    _IscsiSsnTargetName_Type()
)
iscsiSsnTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTargetName.setStatus("current")


class _IscsiSsnTSIH_Type(Unsigned32):
    """Custom type iscsiSsnTSIH based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnTSIH_Type.__name__ = "Unsigned32"
_IscsiSsnTSIH_Object = MibTableColumn
iscsiSsnTSIH = _IscsiSsnTSIH_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 6),
    _IscsiSsnTSIH_Type()
)
iscsiSsnTSIH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTSIH.setStatus("current")


class _IscsiSsnISID_Type(OctetString):
    """Custom type iscsiSsnISID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_IscsiSsnISID_Type.__name__ = "OctetString"
_IscsiSsnISID_Object = MibTableColumn
iscsiSsnISID = _IscsiSsnISID_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 7),
    _IscsiSsnISID_Type()
)
iscsiSsnISID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnISID.setStatus("current")
_IscsiSsnInitiatorAlias_Type = SnmpAdminString
_IscsiSsnInitiatorAlias_Object = MibTableColumn
iscsiSsnInitiatorAlias = _IscsiSsnInitiatorAlias_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 8),
    _IscsiSsnInitiatorAlias_Type()
)
iscsiSsnInitiatorAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitiatorAlias.setStatus("current")
_IscsiSsnTargetAlias_Type = SnmpAdminString
_IscsiSsnTargetAlias_Object = MibTableColumn
iscsiSsnTargetAlias = _IscsiSsnTargetAlias_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 9),
    _IscsiSsnTargetAlias_Type()
)
iscsiSsnTargetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTargetAlias.setStatus("current")
_IscsiSsnInitialR2T_Type = TruthValue
_IscsiSsnInitialR2T_Object = MibTableColumn
iscsiSsnInitialR2T = _IscsiSsnInitialR2T_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 10),
    _IscsiSsnInitialR2T_Type()
)
iscsiSsnInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnInitialR2T.setStatus("current")
_IscsiSsnImmediateData_Type = TruthValue
_IscsiSsnImmediateData_Object = MibTableColumn
iscsiSsnImmediateData = _IscsiSsnImmediateData_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 11),
    _IscsiSsnImmediateData_Type()
)
iscsiSsnImmediateData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnImmediateData.setStatus("current")


class _IscsiSsnType_Type(Integer32):
    """Custom type iscsiSsnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discoverySession", 2),
          ("normalSession", 1))
    )


_IscsiSsnType_Type.__name__ = "Integer32"
_IscsiSsnType_Object = MibTableColumn
iscsiSsnType = _IscsiSsnType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 12),
    _IscsiSsnType_Type()
)
iscsiSsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnType.setStatus("current")


class _IscsiSsnMaxOutstandingR2T_Type(Unsigned32):
    """Custom type iscsiSsnMaxOutstandingR2T based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnMaxOutstandingR2T_Type.__name__ = "Unsigned32"
_IscsiSsnMaxOutstandingR2T_Object = MibTableColumn
iscsiSsnMaxOutstandingR2T = _IscsiSsnMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 13),
    _IscsiSsnMaxOutstandingR2T_Type()
)
iscsiSsnMaxOutstandingR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnMaxOutstandingR2T.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnMaxOutstandingR2T.setUnits("R2Ts")


class _IscsiSsnFirstBurstLength_Type(Unsigned32):
    """Custom type iscsiSsnFirstBurstLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiSsnFirstBurstLength_Type.__name__ = "Unsigned32"
_IscsiSsnFirstBurstLength_Object = MibTableColumn
iscsiSsnFirstBurstLength = _IscsiSsnFirstBurstLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 14),
    _IscsiSsnFirstBurstLength_Type()
)
iscsiSsnFirstBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnFirstBurstLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnFirstBurstLength.setUnits("bytes")


class _IscsiSsnMaxBurstLength_Type(Unsigned32):
    """Custom type iscsiSsnMaxBurstLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiSsnMaxBurstLength_Type.__name__ = "Unsigned32"
_IscsiSsnMaxBurstLength_Object = MibTableColumn
iscsiSsnMaxBurstLength = _IscsiSsnMaxBurstLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 15),
    _IscsiSsnMaxBurstLength_Type()
)
iscsiSsnMaxBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnMaxBurstLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnMaxBurstLength.setUnits("bytes")


class _IscsiSsnConnectionNumber_Type(Gauge32):
    """Custom type iscsiSsnConnectionNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiSsnConnectionNumber_Type.__name__ = "Gauge32"
_IscsiSsnConnectionNumber_Object = MibTableColumn
iscsiSsnConnectionNumber = _IscsiSsnConnectionNumber_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 16),
    _IscsiSsnConnectionNumber_Type()
)
iscsiSsnConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnConnectionNumber.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnConnectionNumber.setUnits("connections")
_IscsiSsnAuthIdentity_Type = RowPointer
_IscsiSsnAuthIdentity_Object = MibTableColumn
iscsiSsnAuthIdentity = _IscsiSsnAuthIdentity_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 17),
    _IscsiSsnAuthIdentity_Type()
)
iscsiSsnAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnAuthIdentity.setStatus("current")
_IscsiSsnDataSequenceInOrder_Type = TruthValue
_IscsiSsnDataSequenceInOrder_Object = MibTableColumn
iscsiSsnDataSequenceInOrder = _IscsiSsnDataSequenceInOrder_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 18),
    _IscsiSsnDataSequenceInOrder_Type()
)
iscsiSsnDataSequenceInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDataSequenceInOrder.setStatus("current")
_IscsiSsnDataPDUInOrder_Type = TruthValue
_IscsiSsnDataPDUInOrder_Object = MibTableColumn
iscsiSsnDataPDUInOrder = _IscsiSsnDataPDUInOrder_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 19),
    _IscsiSsnDataPDUInOrder_Type()
)
iscsiSsnDataPDUInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDataPDUInOrder.setStatus("current")


class _IscsiSsnErrorRecoveryLevel_Type(Unsigned32):
    """Custom type iscsiSsnErrorRecoveryLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiSsnErrorRecoveryLevel_Type.__name__ = "Unsigned32"
_IscsiSsnErrorRecoveryLevel_Object = MibTableColumn
iscsiSsnErrorRecoveryLevel = _IscsiSsnErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 20),
    _IscsiSsnErrorRecoveryLevel_Type()
)
iscsiSsnErrorRecoveryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnErrorRecoveryLevel.setStatus("current")
_IscsiSsnDiscontinuityTime_Type = TimeStamp
_IscsiSsnDiscontinuityTime_Object = MibTableColumn
iscsiSsnDiscontinuityTime = _IscsiSsnDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 21),
    _IscsiSsnDiscontinuityTime_Type()
)
iscsiSsnDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnDiscontinuityTime.setStatus("current")


class _IscsiSsnProtocolLevel_Type(Unsigned32):
    """Custom type iscsiSsnProtocolLevel based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IscsiSsnProtocolLevel_Type.__name__ = "Unsigned32"
_IscsiSsnProtocolLevel_Object = MibTableColumn
iscsiSsnProtocolLevel = _IscsiSsnProtocolLevel_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 22),
    _IscsiSsnProtocolLevel_Type()
)
iscsiSsnProtocolLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnProtocolLevel.setStatus("current")


class _IscsiSsnTaskReporting_Type(Bits):
    """Custom type iscsiSsnTaskReporting based on Bits"""
    namedValues = NamedValues(
        *(("taskReportingFastAbort", 2),
          ("taskReportingResponseFence", 1),
          ("taskReportingRfc3720", 0))
    )

_IscsiSsnTaskReporting_Type.__name__ = "Bits"
_IscsiSsnTaskReporting_Object = MibTableColumn
iscsiSsnTaskReporting = _IscsiSsnTaskReporting_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 1, 1, 23),
    _IscsiSsnTaskReporting_Type()
)
iscsiSsnTaskReporting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTaskReporting.setStatus("current")
_IscsiSessionStatsTable_Object = MibTable
iscsiSessionStatsTable = _IscsiSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2)
)
if mibBuilder.loadTexts:
    iscsiSessionStatsTable.setStatus("current")
_IscsiSessionStatsEntry_Object = MibTableRow
iscsiSessionStatsEntry = _IscsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionStatsEntry.setStatus("current")
_IscsiSsnCmdPDUs_Type = Counter32
_IscsiSsnCmdPDUs_Object = MibTableColumn
iscsiSsnCmdPDUs = _IscsiSsnCmdPDUs_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 1),
    _IscsiSsnCmdPDUs_Type()
)
iscsiSsnCmdPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnCmdPDUs.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnCmdPDUs.setUnits("PDUs")
_IscsiSsnRspPDUs_Type = Counter32
_IscsiSsnRspPDUs_Object = MibTableColumn
iscsiSsnRspPDUs = _IscsiSsnRspPDUs_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 2),
    _IscsiSsnRspPDUs_Type()
)
iscsiSsnRspPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnRspPDUs.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnRspPDUs.setUnits("PDUs")
_IscsiSsnTxDataOctets_Type = Counter64
_IscsiSsnTxDataOctets_Object = MibTableColumn
iscsiSsnTxDataOctets = _IscsiSsnTxDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 3),
    _IscsiSsnTxDataOctets_Type()
)
iscsiSsnTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnTxDataOctets.setUnits("octets")
_IscsiSsnRxDataOctets_Type = Counter64
_IscsiSsnRxDataOctets_Object = MibTableColumn
iscsiSsnRxDataOctets = _IscsiSsnRxDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 4),
    _IscsiSsnRxDataOctets_Type()
)
iscsiSsnRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnRxDataOctets.setUnits("octets")
_IscsiSsnLCTxDataOctets_Type = Counter32
_IscsiSsnLCTxDataOctets_Object = MibTableColumn
iscsiSsnLCTxDataOctets = _IscsiSsnLCTxDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 5),
    _IscsiSsnLCTxDataOctets_Type()
)
iscsiSsnLCTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnLCTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnLCTxDataOctets.setUnits("octets")
_IscsiSsnLCRxDataOctets_Type = Counter32
_IscsiSsnLCRxDataOctets_Object = MibTableColumn
iscsiSsnLCRxDataOctets = _IscsiSsnLCRxDataOctets_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 6),
    _IscsiSsnLCRxDataOctets_Type()
)
iscsiSsnLCRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnLCRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnLCRxDataOctets.setUnits("octets")
_IscsiSsnNopReceivedPDUs_Type = Counter32
_IscsiSsnNopReceivedPDUs_Object = MibTableColumn
iscsiSsnNopReceivedPDUs = _IscsiSsnNopReceivedPDUs_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 7),
    _IscsiSsnNopReceivedPDUs_Type()
)
iscsiSsnNopReceivedPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnNopReceivedPDUs.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnNopReceivedPDUs.setUnits("PDUs")
_IscsiSsnNopSentPDUs_Type = Counter32
_IscsiSsnNopSentPDUs_Object = MibTableColumn
iscsiSsnNopSentPDUs = _IscsiSsnNopSentPDUs_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 2, 1, 8),
    _IscsiSsnNopSentPDUs_Type()
)
iscsiSsnNopSentPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnNopSentPDUs.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnNopSentPDUs.setUnits("PDUs")
_IscsiSessionCxnErrorStatsTable_Object = MibTable
iscsiSessionCxnErrorStatsTable = _IscsiSessionCxnErrorStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 3)
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsTable.setStatus("current")
_IscsiSessionCxnErrorStatsEntry_Object = MibTableRow
iscsiSessionCxnErrorStatsEntry = _IscsiSessionCxnErrorStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsEntry.setStatus("current")
_IscsiSsnCxnDigestErrors_Type = Counter32
_IscsiSsnCxnDigestErrors_Object = MibTableColumn
iscsiSsnCxnDigestErrors = _IscsiSsnCxnDigestErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 3, 1, 1),
    _IscsiSsnCxnDigestErrors_Type()
)
iscsiSsnCxnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnCxnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnCxnDigestErrors.setUnits("PDUs")
_IscsiSsnCxnTimeoutErrors_Type = Counter32
_IscsiSsnCxnTimeoutErrors_Object = MibTableColumn
iscsiSsnCxnTimeoutErrors = _IscsiSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 10, 3, 1, 2),
    _IscsiSsnCxnTimeoutErrors_Type()
)
iscsiSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    iscsiSsnCxnTimeoutErrors.setUnits("connections")
_IscsiConnection_ObjectIdentity = ObjectIdentity
iscsiConnection = _IscsiConnection_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 1, 11)
)
_IscsiConnectionAttributesTable_Object = MibTable
iscsiConnectionAttributesTable = _IscsiConnectionAttributesTable_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1)
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesTable.setStatus("current")
_IscsiConnectionAttributesEntry_Object = MibTableRow
iscsiConnectionAttributesEntry = _IscsiConnectionAttributesEntry_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1)
)
iscsiConnectionAttributesEntry.setIndexNames(
    (0, "ISCSI-MIB", "iscsiInstIndex"),
    (0, "ISCSI-MIB", "iscsiSsnNodeIndex"),
    (0, "ISCSI-MIB", "iscsiSsnIndex"),
    (0, "ISCSI-MIB", "iscsiCxnIndex"),
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesEntry.setStatus("current")


class _IscsiCxnIndex_Type(Unsigned32):
    """Custom type iscsiCxnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_IscsiCxnIndex_Type.__name__ = "Unsigned32"
_IscsiCxnIndex_Object = MibTableColumn
iscsiCxnIndex = _IscsiCxnIndex_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 1),
    _IscsiCxnIndex_Type()
)
iscsiCxnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iscsiCxnIndex.setStatus("current")


class _IscsiCxnCid_Type(Unsigned32):
    """Custom type iscsiCxnCid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IscsiCxnCid_Type.__name__ = "Unsigned32"
_IscsiCxnCid_Object = MibTableColumn
iscsiCxnCid = _IscsiCxnCid_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 2),
    _IscsiCxnCid_Type()
)
iscsiCxnCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnCid.setStatus("current")


class _IscsiCxnState_Type(Integer32):
    """Custom type iscsiCxnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 2),
          ("login", 1),
          ("logout", 3))
    )


_IscsiCxnState_Type.__name__ = "Integer32"
_IscsiCxnState_Object = MibTableColumn
iscsiCxnState = _IscsiCxnState_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 3),
    _IscsiCxnState_Type()
)
iscsiCxnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnState.setStatus("current")
_IscsiCxnAddrType_Type = InetAddressType
_IscsiCxnAddrType_Object = MibTableColumn
iscsiCxnAddrType = _IscsiCxnAddrType_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 4),
    _IscsiCxnAddrType_Type()
)
iscsiCxnAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnAddrType.setStatus("current")
_IscsiCxnLocalAddr_Type = InetAddress
_IscsiCxnLocalAddr_Object = MibTableColumn
iscsiCxnLocalAddr = _IscsiCxnLocalAddr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 5),
    _IscsiCxnLocalAddr_Type()
)
iscsiCxnLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnLocalAddr.setStatus("current")
_IscsiCxnProtocol_Type = IscsiTransportProtocol
_IscsiCxnProtocol_Object = MibTableColumn
iscsiCxnProtocol = _IscsiCxnProtocol_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 6),
    _IscsiCxnProtocol_Type()
)
iscsiCxnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnProtocol.setStatus("current")
_IscsiCxnLocalPort_Type = InetPortNumber
_IscsiCxnLocalPort_Object = MibTableColumn
iscsiCxnLocalPort = _IscsiCxnLocalPort_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 7),
    _IscsiCxnLocalPort_Type()
)
iscsiCxnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnLocalPort.setStatus("current")
_IscsiCxnRemoteAddr_Type = InetAddress
_IscsiCxnRemoteAddr_Object = MibTableColumn
iscsiCxnRemoteAddr = _IscsiCxnRemoteAddr_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 8),
    _IscsiCxnRemoteAddr_Type()
)
iscsiCxnRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRemoteAddr.setStatus("current")
_IscsiCxnRemotePort_Type = InetPortNumber
_IscsiCxnRemotePort_Object = MibTableColumn
iscsiCxnRemotePort = _IscsiCxnRemotePort_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 9),
    _IscsiCxnRemotePort_Type()
)
iscsiCxnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRemotePort.setStatus("current")


class _IscsiCxnMaxRecvDataSegLength_Type(Unsigned32):
    """Custom type iscsiCxnMaxRecvDataSegLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiCxnMaxRecvDataSegLength_Type.__name__ = "Unsigned32"
_IscsiCxnMaxRecvDataSegLength_Object = MibTableColumn
iscsiCxnMaxRecvDataSegLength = _IscsiCxnMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 10),
    _IscsiCxnMaxRecvDataSegLength_Type()
)
iscsiCxnMaxRecvDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnMaxRecvDataSegLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiCxnMaxRecvDataSegLength.setUnits("bytes")


class _IscsiCxnMaxXmitDataSegLength_Type(Unsigned32):
    """Custom type iscsiCxnMaxXmitDataSegLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_IscsiCxnMaxXmitDataSegLength_Type.__name__ = "Unsigned32"
_IscsiCxnMaxXmitDataSegLength_Object = MibTableColumn
iscsiCxnMaxXmitDataSegLength = _IscsiCxnMaxXmitDataSegLength_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 11),
    _IscsiCxnMaxXmitDataSegLength_Type()
)
iscsiCxnMaxXmitDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnMaxXmitDataSegLength.setStatus("current")
if mibBuilder.loadTexts:
    iscsiCxnMaxXmitDataSegLength.setUnits("bytes")
_IscsiCxnHeaderIntegrity_Type = IscsiDigestMethod
_IscsiCxnHeaderIntegrity_Object = MibTableColumn
iscsiCxnHeaderIntegrity = _IscsiCxnHeaderIntegrity_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 12),
    _IscsiCxnHeaderIntegrity_Type()
)
iscsiCxnHeaderIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnHeaderIntegrity.setStatus("current")
_IscsiCxnDataIntegrity_Type = IscsiDigestMethod
_IscsiCxnDataIntegrity_Object = MibTableColumn
iscsiCxnDataIntegrity = _IscsiCxnDataIntegrity_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 13),
    _IscsiCxnDataIntegrity_Type()
)
iscsiCxnDataIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnDataIntegrity.setStatus("current")
_IscsiCxnRecvMarker_Type = TruthValue
_IscsiCxnRecvMarker_Object = MibTableColumn
iscsiCxnRecvMarker = _IscsiCxnRecvMarker_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 14),
    _IscsiCxnRecvMarker_Type()
)
iscsiCxnRecvMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnRecvMarker.setStatus("deprecated")
_IscsiCxnSendMarker_Type = TruthValue
_IscsiCxnSendMarker_Object = MibTableColumn
iscsiCxnSendMarker = _IscsiCxnSendMarker_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 15),
    _IscsiCxnSendMarker_Type()
)
iscsiCxnSendMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnSendMarker.setStatus("deprecated")


class _IscsiCxnVersionActive_Type(Unsigned32):
    """Custom type iscsiCxnVersionActive based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IscsiCxnVersionActive_Type.__name__ = "Unsigned32"
_IscsiCxnVersionActive_Object = MibTableColumn
iscsiCxnVersionActive = _IscsiCxnVersionActive_Object(
    (1, 3, 6, 1, 2, 1, 142, 1, 11, 1, 1, 16),
    _IscsiCxnVersionActive_Type()
)
iscsiCxnVersionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscsiCxnVersionActive.setStatus("current")
_IscsiConformance_ObjectIdentity = ObjectIdentity
iscsiConformance = _IscsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 2)
)
_IscsiCompliances_ObjectIdentity = ObjectIdentity
iscsiCompliances = _IscsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 2, 1)
)
_IscsiGroups_ObjectIdentity = ObjectIdentity
iscsiGroups = _IscsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 2, 2)
)
_IscsiAdmin_ObjectIdentity = ObjectIdentity
iscsiAdmin = _IscsiAdmin_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3)
)
_IscsiDescriptors_ObjectIdentity = ObjectIdentity
iscsiDescriptors = _IscsiDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1)
)
_IscsiHeaderIntegrityTypes_ObjectIdentity = ObjectIdentity
iscsiHeaderIntegrityTypes = _IscsiHeaderIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 1)
)
_IscsiHdrIntegrityNone_ObjectIdentity = ObjectIdentity
iscsiHdrIntegrityNone = _IscsiHdrIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiHdrIntegrityNone.setStatus("current")
_IscsiHdrIntegrityCrc32c_ObjectIdentity = ObjectIdentity
iscsiHdrIntegrityCrc32c = _IscsiHdrIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    iscsiHdrIntegrityCrc32c.setStatus("current")
_IscsiDataIntegrityTypes_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityTypes = _IscsiDataIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 2)
)
_IscsiDataIntegrityNone_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityNone = _IscsiDataIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    iscsiDataIntegrityNone.setStatus("current")
_IscsiDataIntegrityCrc32c_ObjectIdentity = ObjectIdentity
iscsiDataIntegrityCrc32c = _IscsiDataIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 142, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    iscsiDataIntegrityCrc32c.setStatus("current")
iscsiInstanceAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInstanceSsnErrorStatsEntry")
)
iscsiInstanceSsnErrorStatsEntry.setIndexNames(*iscsiInstanceAttributesEntry.getIndexNames())
iscsiTargetAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiTargetLoginStatsEntry")
)
iscsiTargetLoginStatsEntry.setIndexNames(*iscsiTargetAttributesEntry.getIndexNames())
iscsiTargetAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiTargetLogoutStatsEntry")
)
iscsiTargetLogoutStatsEntry.setIndexNames(*iscsiTargetAttributesEntry.getIndexNames())
iscsiInitiatorAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInitiatorLoginStatsEntry")
)
iscsiInitiatorLoginStatsEntry.setIndexNames(*iscsiInitiatorAttributesEntry.getIndexNames())
iscsiInitiatorAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiInitiatorLogoutStatsEntry")
)
iscsiInitiatorLogoutStatsEntry.setIndexNames(*iscsiInitiatorAttributesEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiSessionStatsEntry")
)
iscsiSessionStatsEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())
iscsiSessionAttributesEntry.registerAugmentions(
    ("ISCSI-MIB",
     "iscsiSessionCxnErrorStatsEntry")
)
iscsiSessionCxnErrorStatsEntry.setIndexNames(*iscsiSessionAttributesEntry.getIndexNames())

# Managed Objects groups

iscsiInstanceAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 1)
)
iscsiInstanceAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiInstDescr"),
        ("ISCSI-MIB", "iscsiInstVersionMin"),
        ("ISCSI-MIB", "iscsiInstVersionMax"),
        ("ISCSI-MIB", "iscsiInstVendorID"),
        ("ISCSI-MIB", "iscsiInstVendorVersion"),
        ("ISCSI-MIB", "iscsiInstPortalNumber"),
        ("ISCSI-MIB", "iscsiInstNodeNumber"),
        ("ISCSI-MIB", "iscsiInstSessionNumber"),
        ("ISCSI-MIB", "iscsiInstSsnFailures"),
        ("ISCSI-MIB", "iscsiInstLastSsnFailureType"),
        ("ISCSI-MIB", "iscsiInstLastSsnRmtNodeName"),
        ("ISCSI-MIB", "iscsiInstDiscontinuityTime"),
        ("ISCSI-MIB", "iscsiInstXNodeArchitecture"))
)
if mibBuilder.loadTexts:
    iscsiInstanceAttributesGroup.setStatus("current")

iscsiInstanceSsnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 2)
)
iscsiInstanceSsnErrorStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiInstSsnDigestErrors"),
        ("ISCSI-MIB", "iscsiInstSsnCxnTimeoutErrors"),
        ("ISCSI-MIB", "iscsiInstSsnFormatErrors"))
)
if mibBuilder.loadTexts:
    iscsiInstanceSsnErrorStatsGroup.setStatus("current")

iscsiPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 3)
)
iscsiPortalAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiPortalRowStatus"),
        ("ISCSI-MIB", "iscsiPortalStorageType"),
        ("ISCSI-MIB", "iscsiPortalRoles"),
        ("ISCSI-MIB", "iscsiPortalAddrType"),
        ("ISCSI-MIB", "iscsiPortalAddr"),
        ("ISCSI-MIB", "iscsiPortalProtocol"),
        ("ISCSI-MIB", "iscsiPortalMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiPortalPrimaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalPrimaryDataDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryDataDigest"),
        ("ISCSI-MIB", "iscsiPortalRecvMarker"))
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesGroup.setStatus("deprecated")

iscsiTgtPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 4)
)
iscsiTgtPortalAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtPortalPort"),
        ("ISCSI-MIB", "iscsiTgtPortalTag"))
)
if mibBuilder.loadTexts:
    iscsiTgtPortalAttributesGroup.setStatus("current")

iscsiIntrPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 5)
)
iscsiIntrPortalAttributesGroup.setObjects(
    ("ISCSI-MIB", "iscsiIntrPortalTag")
)
if mibBuilder.loadTexts:
    iscsiIntrPortalAttributesGroup.setStatus("current")

iscsiNodeAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 6)
)
iscsiNodeAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiNodeName"),
        ("ISCSI-MIB", "iscsiNodeAlias"),
        ("ISCSI-MIB", "iscsiNodeRoles"),
        ("ISCSI-MIB", "iscsiNodeTransportType"),
        ("ISCSI-MIB", "iscsiNodeInitialR2T"),
        ("ISCSI-MIB", "iscsiNodeImmediateData"),
        ("ISCSI-MIB", "iscsiNodeMaxOutstandingR2T"),
        ("ISCSI-MIB", "iscsiNodeFirstBurstLength"),
        ("ISCSI-MIB", "iscsiNodeMaxBurstLength"),
        ("ISCSI-MIB", "iscsiNodeMaxConnections"),
        ("ISCSI-MIB", "iscsiNodeDataSequenceInOrder"),
        ("ISCSI-MIB", "iscsiNodeDataPDUInOrder"),
        ("ISCSI-MIB", "iscsiNodeDefaultTime2Wait"),
        ("ISCSI-MIB", "iscsiNodeDefaultTime2Retain"),
        ("ISCSI-MIB", "iscsiNodeErrorRecoveryLevel"),
        ("ISCSI-MIB", "iscsiNodeDiscontinuityTime"),
        ("ISCSI-MIB", "iscsiNodeStorageType"))
)
if mibBuilder.loadTexts:
    iscsiNodeAttributesGroup.setStatus("current")

iscsiTargetAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 7)
)
iscsiTargetAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginFailures"),
        ("ISCSI-MIB", "iscsiTgtLastFailureTime"),
        ("ISCSI-MIB", "iscsiTgtLastFailureType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureName"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddrType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiTargetAttributesGroup.setStatus("current")

iscsiTargetLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 8)
)
iscsiTargetLoginStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginAccepts"),
        ("ISCSI-MIB", "iscsiTgtLoginOtherFails"),
        ("ISCSI-MIB", "iscsiTgtLoginRedirects"),
        ("ISCSI-MIB", "iscsiTgtLoginAuthorizeFails"),
        ("ISCSI-MIB", "iscsiTgtLoginAuthenticateFails"),
        ("ISCSI-MIB", "iscsiTgtLoginNegotiateFails"))
)
if mibBuilder.loadTexts:
    iscsiTargetLoginStatsGroup.setStatus("current")

iscsiTargetLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 9)
)
iscsiTargetLogoutStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLogoutNormals"),
        ("ISCSI-MIB", "iscsiTgtLogoutOthers"))
)
if mibBuilder.loadTexts:
    iscsiTargetLogoutStatsGroup.setStatus("current")

iscsiTargetAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 10)
)
iscsiTargetAuthGroup.setObjects(
      *(("ISCSI-MIB", "iscsiTgtAuthRowStatus"),
        ("ISCSI-MIB", "iscsiTgtAuthStorageType"),
        ("ISCSI-MIB", "iscsiTgtAuthIdentity"))
)
if mibBuilder.loadTexts:
    iscsiTargetAuthGroup.setStatus("current")

iscsiInitiatorAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 11)
)
iscsiInitiatorAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginFailures"),
        ("ISCSI-MIB", "iscsiIntrLastFailureTime"),
        ("ISCSI-MIB", "iscsiIntrLastFailureType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureName"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddrType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddr"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorAttributesGroup.setStatus("current")

iscsiInitiatorLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 12)
)
iscsiInitiatorLoginStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginAcceptRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginOtherFailRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginRedirectRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginAuthFailRsps"),
        ("ISCSI-MIB", "iscsiIntrLoginAuthenticateFails"),
        ("ISCSI-MIB", "iscsiIntrLoginNegotiateFails"),
        ("ISCSI-MIB", "iscsiIntrLoginAuthorizeFails"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorLoginStatsGroup.setStatus("current")

iscsiInitiatorLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 13)
)
iscsiInitiatorLogoutStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLogoutNormals"),
        ("ISCSI-MIB", "iscsiIntrLogoutOthers"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorLogoutStatsGroup.setStatus("current")

iscsiInitiatorAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 14)
)
iscsiInitiatorAuthGroup.setObjects(
      *(("ISCSI-MIB", "iscsiIntrAuthRowStatus"),
        ("ISCSI-MIB", "iscsiIntrAuthStorageType"),
        ("ISCSI-MIB", "iscsiIntrAuthIdentity"))
)
if mibBuilder.loadTexts:
    iscsiInitiatorAuthGroup.setStatus("current")

iscsiSessionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 15)
)
iscsiSessionAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnDirection"),
        ("ISCSI-MIB", "iscsiSsnInitiatorName"),
        ("ISCSI-MIB", "iscsiSsnTargetName"),
        ("ISCSI-MIB", "iscsiSsnTSIH"),
        ("ISCSI-MIB", "iscsiSsnISID"),
        ("ISCSI-MIB", "iscsiSsnInitiatorAlias"),
        ("ISCSI-MIB", "iscsiSsnTargetAlias"),
        ("ISCSI-MIB", "iscsiSsnInitialR2T"),
        ("ISCSI-MIB", "iscsiSsnImmediateData"),
        ("ISCSI-MIB", "iscsiSsnType"),
        ("ISCSI-MIB", "iscsiSsnMaxOutstandingR2T"),
        ("ISCSI-MIB", "iscsiSsnFirstBurstLength"),
        ("ISCSI-MIB", "iscsiSsnMaxBurstLength"),
        ("ISCSI-MIB", "iscsiSsnConnectionNumber"),
        ("ISCSI-MIB", "iscsiSsnAuthIdentity"),
        ("ISCSI-MIB", "iscsiSsnDataSequenceInOrder"),
        ("ISCSI-MIB", "iscsiSsnDataPDUInOrder"),
        ("ISCSI-MIB", "iscsiSsnErrorRecoveryLevel"),
        ("ISCSI-MIB", "iscsiSsnDiscontinuityTime"),
        ("ISCSI-MIB", "iscsiSsnProtocolLevel"),
        ("ISCSI-MIB", "iscsiSsnTaskReporting"))
)
if mibBuilder.loadTexts:
    iscsiSessionAttributesGroup.setStatus("current")

iscsiSessionPDUStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 16)
)
iscsiSessionPDUStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnCmdPDUs"),
        ("ISCSI-MIB", "iscsiSsnRspPDUs"))
)
if mibBuilder.loadTexts:
    iscsiSessionPDUStatsGroup.setStatus("current")

iscsiSessionOctetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 17)
)
iscsiSessionOctetStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnTxDataOctets"),
        ("ISCSI-MIB", "iscsiSsnRxDataOctets"))
)
if mibBuilder.loadTexts:
    iscsiSessionOctetStatsGroup.setStatus("current")

iscsiSessionLCOctetStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 18)
)
iscsiSessionLCOctetStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnLCTxDataOctets"),
        ("ISCSI-MIB", "iscsiSsnLCRxDataOctets"))
)
if mibBuilder.loadTexts:
    iscsiSessionLCOctetStatsGroup.setStatus("current")

iscsiSessionCxnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 19)
)
iscsiSessionCxnErrorStatsGroup.setObjects(
      *(("ISCSI-MIB", "iscsiSsnCxnDigestErrors"),
        ("ISCSI-MIB", "iscsiSsnCxnTimeoutErrors"))
)
if mibBuilder.loadTexts:
    iscsiSessionCxnErrorStatsGroup.setStatus("current")

iscsiConnectionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 20)
)
iscsiConnectionAttributesGroup.setObjects(
      *(("ISCSI-MIB", "iscsiCxnCid"),
        ("ISCSI-MIB", "iscsiCxnState"),
        ("ISCSI-MIB", "iscsiCxnProtocol"),
        ("ISCSI-MIB", "iscsiCxnAddrType"),
        ("ISCSI-MIB", "iscsiCxnLocalAddr"),
        ("ISCSI-MIB", "iscsiCxnLocalPort"),
        ("ISCSI-MIB", "iscsiCxnRemoteAddr"),
        ("ISCSI-MIB", "iscsiCxnRemotePort"),
        ("ISCSI-MIB", "iscsiCxnMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiCxnMaxXmitDataSegLength"),
        ("ISCSI-MIB", "iscsiCxnHeaderIntegrity"),
        ("ISCSI-MIB", "iscsiCxnDataIntegrity"),
        ("ISCSI-MIB", "iscsiCxnRecvMarker"),
        ("ISCSI-MIB", "iscsiCxnSendMarker"),
        ("ISCSI-MIB", "iscsiCxnVersionActive"))
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesGroup.setStatus("deprecated")

iscsiPortalAttributesGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 24)
)
iscsiPortalAttributesGroupV2.setObjects(
      *(("ISCSI-MIB", "iscsiPortalRowStatus"),
        ("ISCSI-MIB", "iscsiPortalStorageType"),
        ("ISCSI-MIB", "iscsiPortalRoles"),
        ("ISCSI-MIB", "iscsiPortalAddrType"),
        ("ISCSI-MIB", "iscsiPortalAddr"),
        ("ISCSI-MIB", "iscsiPortalProtocol"),
        ("ISCSI-MIB", "iscsiPortalMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiPortalPrimaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalPrimaryDataDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryHdrDigest"),
        ("ISCSI-MIB", "iscsiPortalSecondaryDataDigest"))
)
if mibBuilder.loadTexts:
    iscsiPortalAttributesGroupV2.setStatus("current")

iscsiConnectionAttributesGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 25)
)
iscsiConnectionAttributesGroupV2.setObjects(
      *(("ISCSI-MIB", "iscsiCxnCid"),
        ("ISCSI-MIB", "iscsiCxnState"),
        ("ISCSI-MIB", "iscsiCxnProtocol"),
        ("ISCSI-MIB", "iscsiCxnAddrType"),
        ("ISCSI-MIB", "iscsiCxnLocalAddr"),
        ("ISCSI-MIB", "iscsiCxnLocalPort"),
        ("ISCSI-MIB", "iscsiCxnRemoteAddr"),
        ("ISCSI-MIB", "iscsiCxnRemotePort"),
        ("ISCSI-MIB", "iscsiCxnMaxRecvDataSegLength"),
        ("ISCSI-MIB", "iscsiCxnMaxXmitDataSegLength"),
        ("ISCSI-MIB", "iscsiCxnHeaderIntegrity"),
        ("ISCSI-MIB", "iscsiCxnDataIntegrity"),
        ("ISCSI-MIB", "iscsiCxnVersionActive"))
)
if mibBuilder.loadTexts:
    iscsiConnectionAttributesGroupV2.setStatus("current")

iscsiNewObjectsV2 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 26)
)
iscsiNewObjectsV2.setObjects(
      *(("ISCSI-MIB", "iscsiInstXNodeArchitecture"),
        ("ISCSI-MIB", "iscsiSsnTaskReporting"),
        ("ISCSI-MIB", "iscsiSsnProtocolLevel"),
        ("ISCSI-MIB", "iscsiSsnNopReceivedPDUs"),
        ("ISCSI-MIB", "iscsiSsnNopSentPDUs"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailurePort"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailurePort"),
        ("ISCSI-MIB", "iscsiPortalDescr"),
        ("ISCSI-MIB", "iscsiInstSsnTgtUnmappedErrors"),
        ("ISCSI-MIB", "iscsiTgtLogoutCxnClosed"),
        ("ISCSI-MIB", "iscsiTgtLogoutCxnRemoved"))
)
if mibBuilder.loadTexts:
    iscsiNewObjectsV2.setStatus("current")


# Notification objects

iscsiTgtLoginFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 142, 0, 1)
)
iscsiTgtLoginFailure.setObjects(
      *(("ISCSI-MIB", "iscsiTgtLoginFailures"),
        ("ISCSI-MIB", "iscsiTgtLastFailureType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureName"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddrType"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailureAddr"),
        ("ISCSI-MIB", "iscsiTgtLastIntrFailurePort"))
)
if mibBuilder.loadTexts:
    iscsiTgtLoginFailure.setStatus(
        "current"
    )

iscsiIntrLoginFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 142, 0, 2)
)
iscsiIntrLoginFailure.setObjects(
      *(("ISCSI-MIB", "iscsiIntrLoginFailures"),
        ("ISCSI-MIB", "iscsiIntrLastFailureType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureName"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddrType"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailureAddr"),
        ("ISCSI-MIB", "iscsiIntrLastTgtFailurePort"))
)
if mibBuilder.loadTexts:
    iscsiIntrLoginFailure.setStatus(
        "current"
    )

iscsiInstSessionFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 142, 0, 3)
)
iscsiInstSessionFailure.setObjects(
      *(("ISCSI-MIB", "iscsiInstSsnFailures"),
        ("ISCSI-MIB", "iscsiInstLastSsnFailureType"),
        ("ISCSI-MIB", "iscsiInstLastSsnRmtNodeName"))
)
if mibBuilder.loadTexts:
    iscsiInstSessionFailure.setStatus(
        "current"
    )


# Notifications groups

iscsiTgtLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 21)
)
iscsiTgtLgnNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiTgtLoginFailure")
)
if mibBuilder.loadTexts:
    iscsiTgtLgnNotificationsGroup.setStatus(
        "current"
    )

iscsiIntrLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 22)
)
iscsiIntrLgnNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiIntrLoginFailure")
)
if mibBuilder.loadTexts:
    iscsiIntrLgnNotificationsGroup.setStatus(
        "current"
    )

iscsiSsnFlrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 142, 2, 2, 23)
)
iscsiSsnFlrNotificationsGroup.setObjects(
    ("ISCSI-MIB", "iscsiInstSessionFailure")
)
if mibBuilder.loadTexts:
    iscsiSsnFlrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

iscsiComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 142, 2, 1, 1)
)
if mibBuilder.loadTexts:
    iscsiComplianceV1.setStatus(
        "deprecated"
    )

iscsiComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 142, 2, 1, 2)
)
if mibBuilder.loadTexts:
    iscsiComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ISCSI-MIB",
    **{"IscsiTransportProtocol": IscsiTransportProtocol,
       "IscsiDigestMethod": IscsiDigestMethod,
       "IscsiName": IscsiName,
       "iscsiMibModule": iscsiMibModule,
       "iscsiNotifications": iscsiNotifications,
       "iscsiTgtLoginFailure": iscsiTgtLoginFailure,
       "iscsiIntrLoginFailure": iscsiIntrLoginFailure,
       "iscsiInstSessionFailure": iscsiInstSessionFailure,
       "iscsiObjects": iscsiObjects,
       "iscsiInstance": iscsiInstance,
       "iscsiInstanceAttributesTable": iscsiInstanceAttributesTable,
       "iscsiInstanceAttributesEntry": iscsiInstanceAttributesEntry,
       "iscsiInstIndex": iscsiInstIndex,
       "iscsiInstDescr": iscsiInstDescr,
       "iscsiInstVersionMin": iscsiInstVersionMin,
       "iscsiInstVersionMax": iscsiInstVersionMax,
       "iscsiInstVendorID": iscsiInstVendorID,
       "iscsiInstVendorVersion": iscsiInstVendorVersion,
       "iscsiInstPortalNumber": iscsiInstPortalNumber,
       "iscsiInstNodeNumber": iscsiInstNodeNumber,
       "iscsiInstSessionNumber": iscsiInstSessionNumber,
       "iscsiInstSsnFailures": iscsiInstSsnFailures,
       "iscsiInstLastSsnFailureType": iscsiInstLastSsnFailureType,
       "iscsiInstLastSsnRmtNodeName": iscsiInstLastSsnRmtNodeName,
       "iscsiInstDiscontinuityTime": iscsiInstDiscontinuityTime,
       "iscsiInstXNodeArchitecture": iscsiInstXNodeArchitecture,
       "iscsiInstanceSsnErrorStatsTable": iscsiInstanceSsnErrorStatsTable,
       "iscsiInstanceSsnErrorStatsEntry": iscsiInstanceSsnErrorStatsEntry,
       "iscsiInstSsnDigestErrors": iscsiInstSsnDigestErrors,
       "iscsiInstSsnCxnTimeoutErrors": iscsiInstSsnCxnTimeoutErrors,
       "iscsiInstSsnFormatErrors": iscsiInstSsnFormatErrors,
       "iscsiInstSsnTgtUnmappedErrors": iscsiInstSsnTgtUnmappedErrors,
       "iscsiPortal": iscsiPortal,
       "iscsiPortalAttributesTable": iscsiPortalAttributesTable,
       "iscsiPortalAttributesEntry": iscsiPortalAttributesEntry,
       "iscsiPortalIndex": iscsiPortalIndex,
       "iscsiPortalRowStatus": iscsiPortalRowStatus,
       "iscsiPortalRoles": iscsiPortalRoles,
       "iscsiPortalAddrType": iscsiPortalAddrType,
       "iscsiPortalAddr": iscsiPortalAddr,
       "iscsiPortalProtocol": iscsiPortalProtocol,
       "iscsiPortalMaxRecvDataSegLength": iscsiPortalMaxRecvDataSegLength,
       "iscsiPortalPrimaryHdrDigest": iscsiPortalPrimaryHdrDigest,
       "iscsiPortalPrimaryDataDigest": iscsiPortalPrimaryDataDigest,
       "iscsiPortalSecondaryHdrDigest": iscsiPortalSecondaryHdrDigest,
       "iscsiPortalSecondaryDataDigest": iscsiPortalSecondaryDataDigest,
       "iscsiPortalRecvMarker": iscsiPortalRecvMarker,
       "iscsiPortalStorageType": iscsiPortalStorageType,
       "iscsiPortalDescr": iscsiPortalDescr,
       "iscsiTargetPortal": iscsiTargetPortal,
       "iscsiTgtPortalAttributesTable": iscsiTgtPortalAttributesTable,
       "iscsiTgtPortalAttributesEntry": iscsiTgtPortalAttributesEntry,
       "iscsiTgtPortalNodeIndexOrZero": iscsiTgtPortalNodeIndexOrZero,
       "iscsiTgtPortalPort": iscsiTgtPortalPort,
       "iscsiTgtPortalTag": iscsiTgtPortalTag,
       "iscsiInitiatorPortal": iscsiInitiatorPortal,
       "iscsiIntrPortalAttributesTable": iscsiIntrPortalAttributesTable,
       "iscsiIntrPortalAttributesEntry": iscsiIntrPortalAttributesEntry,
       "iscsiIntrPortalNodeIndexOrZero": iscsiIntrPortalNodeIndexOrZero,
       "iscsiIntrPortalTag": iscsiIntrPortalTag,
       "iscsiNode": iscsiNode,
       "iscsiNodeAttributesTable": iscsiNodeAttributesTable,
       "iscsiNodeAttributesEntry": iscsiNodeAttributesEntry,
       "iscsiNodeIndex": iscsiNodeIndex,
       "iscsiNodeName": iscsiNodeName,
       "iscsiNodeAlias": iscsiNodeAlias,
       "iscsiNodeRoles": iscsiNodeRoles,
       "iscsiNodeTransportType": iscsiNodeTransportType,
       "iscsiNodeInitialR2T": iscsiNodeInitialR2T,
       "iscsiNodeImmediateData": iscsiNodeImmediateData,
       "iscsiNodeMaxOutstandingR2T": iscsiNodeMaxOutstandingR2T,
       "iscsiNodeFirstBurstLength": iscsiNodeFirstBurstLength,
       "iscsiNodeMaxBurstLength": iscsiNodeMaxBurstLength,
       "iscsiNodeMaxConnections": iscsiNodeMaxConnections,
       "iscsiNodeDataSequenceInOrder": iscsiNodeDataSequenceInOrder,
       "iscsiNodeDataPDUInOrder": iscsiNodeDataPDUInOrder,
       "iscsiNodeDefaultTime2Wait": iscsiNodeDefaultTime2Wait,
       "iscsiNodeDefaultTime2Retain": iscsiNodeDefaultTime2Retain,
       "iscsiNodeErrorRecoveryLevel": iscsiNodeErrorRecoveryLevel,
       "iscsiNodeDiscontinuityTime": iscsiNodeDiscontinuityTime,
       "iscsiNodeStorageType": iscsiNodeStorageType,
       "iscsiTarget": iscsiTarget,
       "iscsiTargetAttributesTable": iscsiTargetAttributesTable,
       "iscsiTargetAttributesEntry": iscsiTargetAttributesEntry,
       "iscsiTgtLoginFailures": iscsiTgtLoginFailures,
       "iscsiTgtLastFailureTime": iscsiTgtLastFailureTime,
       "iscsiTgtLastFailureType": iscsiTgtLastFailureType,
       "iscsiTgtLastIntrFailureName": iscsiTgtLastIntrFailureName,
       "iscsiTgtLastIntrFailureAddrType": iscsiTgtLastIntrFailureAddrType,
       "iscsiTgtLastIntrFailureAddr": iscsiTgtLastIntrFailureAddr,
       "iscsiTgtLastIntrFailurePort": iscsiTgtLastIntrFailurePort,
       "iscsiTargetLoginStatsTable": iscsiTargetLoginStatsTable,
       "iscsiTargetLoginStatsEntry": iscsiTargetLoginStatsEntry,
       "iscsiTgtLoginAccepts": iscsiTgtLoginAccepts,
       "iscsiTgtLoginOtherFails": iscsiTgtLoginOtherFails,
       "iscsiTgtLoginRedirects": iscsiTgtLoginRedirects,
       "iscsiTgtLoginAuthorizeFails": iscsiTgtLoginAuthorizeFails,
       "iscsiTgtLoginAuthenticateFails": iscsiTgtLoginAuthenticateFails,
       "iscsiTgtLoginNegotiateFails": iscsiTgtLoginNegotiateFails,
       "iscsiTargetLogoutStatsTable": iscsiTargetLogoutStatsTable,
       "iscsiTargetLogoutStatsEntry": iscsiTargetLogoutStatsEntry,
       "iscsiTgtLogoutNormals": iscsiTgtLogoutNormals,
       "iscsiTgtLogoutOthers": iscsiTgtLogoutOthers,
       "iscsiTgtLogoutCxnClosed": iscsiTgtLogoutCxnClosed,
       "iscsiTgtLogoutCxnRemoved": iscsiTgtLogoutCxnRemoved,
       "iscsiTgtAuthorization": iscsiTgtAuthorization,
       "iscsiTgtAuthAttributesTable": iscsiTgtAuthAttributesTable,
       "iscsiTgtAuthAttributesEntry": iscsiTgtAuthAttributesEntry,
       "iscsiTgtAuthIndex": iscsiTgtAuthIndex,
       "iscsiTgtAuthRowStatus": iscsiTgtAuthRowStatus,
       "iscsiTgtAuthIdentity": iscsiTgtAuthIdentity,
       "iscsiTgtAuthStorageType": iscsiTgtAuthStorageType,
       "iscsiInitiator": iscsiInitiator,
       "iscsiInitiatorAttributesTable": iscsiInitiatorAttributesTable,
       "iscsiInitiatorAttributesEntry": iscsiInitiatorAttributesEntry,
       "iscsiIntrLoginFailures": iscsiIntrLoginFailures,
       "iscsiIntrLastFailureTime": iscsiIntrLastFailureTime,
       "iscsiIntrLastFailureType": iscsiIntrLastFailureType,
       "iscsiIntrLastTgtFailureName": iscsiIntrLastTgtFailureName,
       "iscsiIntrLastTgtFailureAddrType": iscsiIntrLastTgtFailureAddrType,
       "iscsiIntrLastTgtFailureAddr": iscsiIntrLastTgtFailureAddr,
       "iscsiIntrLastTgtFailurePort": iscsiIntrLastTgtFailurePort,
       "iscsiInitiatorLoginStatsTable": iscsiInitiatorLoginStatsTable,
       "iscsiInitiatorLoginStatsEntry": iscsiInitiatorLoginStatsEntry,
       "iscsiIntrLoginAcceptRsps": iscsiIntrLoginAcceptRsps,
       "iscsiIntrLoginOtherFailRsps": iscsiIntrLoginOtherFailRsps,
       "iscsiIntrLoginRedirectRsps": iscsiIntrLoginRedirectRsps,
       "iscsiIntrLoginAuthFailRsps": iscsiIntrLoginAuthFailRsps,
       "iscsiIntrLoginAuthenticateFails": iscsiIntrLoginAuthenticateFails,
       "iscsiIntrLoginNegotiateFails": iscsiIntrLoginNegotiateFails,
       "iscsiIntrLoginAuthorizeFails": iscsiIntrLoginAuthorizeFails,
       "iscsiInitiatorLogoutStatsTable": iscsiInitiatorLogoutStatsTable,
       "iscsiInitiatorLogoutStatsEntry": iscsiInitiatorLogoutStatsEntry,
       "iscsiIntrLogoutNormals": iscsiIntrLogoutNormals,
       "iscsiIntrLogoutOthers": iscsiIntrLogoutOthers,
       "iscsiIntrAuthorization": iscsiIntrAuthorization,
       "iscsiIntrAuthAttributesTable": iscsiIntrAuthAttributesTable,
       "iscsiIntrAuthAttributesEntry": iscsiIntrAuthAttributesEntry,
       "iscsiIntrAuthIndex": iscsiIntrAuthIndex,
       "iscsiIntrAuthRowStatus": iscsiIntrAuthRowStatus,
       "iscsiIntrAuthIdentity": iscsiIntrAuthIdentity,
       "iscsiIntrAuthStorageType": iscsiIntrAuthStorageType,
       "iscsiSession": iscsiSession,
       "iscsiSessionAttributesTable": iscsiSessionAttributesTable,
       "iscsiSessionAttributesEntry": iscsiSessionAttributesEntry,
       "iscsiSsnNodeIndex": iscsiSsnNodeIndex,
       "iscsiSsnIndex": iscsiSsnIndex,
       "iscsiSsnDirection": iscsiSsnDirection,
       "iscsiSsnInitiatorName": iscsiSsnInitiatorName,
       "iscsiSsnTargetName": iscsiSsnTargetName,
       "iscsiSsnTSIH": iscsiSsnTSIH,
       "iscsiSsnISID": iscsiSsnISID,
       "iscsiSsnInitiatorAlias": iscsiSsnInitiatorAlias,
       "iscsiSsnTargetAlias": iscsiSsnTargetAlias,
       "iscsiSsnInitialR2T": iscsiSsnInitialR2T,
       "iscsiSsnImmediateData": iscsiSsnImmediateData,
       "iscsiSsnType": iscsiSsnType,
       "iscsiSsnMaxOutstandingR2T": iscsiSsnMaxOutstandingR2T,
       "iscsiSsnFirstBurstLength": iscsiSsnFirstBurstLength,
       "iscsiSsnMaxBurstLength": iscsiSsnMaxBurstLength,
       "iscsiSsnConnectionNumber": iscsiSsnConnectionNumber,
       "iscsiSsnAuthIdentity": iscsiSsnAuthIdentity,
       "iscsiSsnDataSequenceInOrder": iscsiSsnDataSequenceInOrder,
       "iscsiSsnDataPDUInOrder": iscsiSsnDataPDUInOrder,
       "iscsiSsnErrorRecoveryLevel": iscsiSsnErrorRecoveryLevel,
       "iscsiSsnDiscontinuityTime": iscsiSsnDiscontinuityTime,
       "iscsiSsnProtocolLevel": iscsiSsnProtocolLevel,
       "iscsiSsnTaskReporting": iscsiSsnTaskReporting,
       "iscsiSessionStatsTable": iscsiSessionStatsTable,
       "iscsiSessionStatsEntry": iscsiSessionStatsEntry,
       "iscsiSsnCmdPDUs": iscsiSsnCmdPDUs,
       "iscsiSsnRspPDUs": iscsiSsnRspPDUs,
       "iscsiSsnTxDataOctets": iscsiSsnTxDataOctets,
       "iscsiSsnRxDataOctets": iscsiSsnRxDataOctets,
       "iscsiSsnLCTxDataOctets": iscsiSsnLCTxDataOctets,
       "iscsiSsnLCRxDataOctets": iscsiSsnLCRxDataOctets,
       "iscsiSsnNopReceivedPDUs": iscsiSsnNopReceivedPDUs,
       "iscsiSsnNopSentPDUs": iscsiSsnNopSentPDUs,
       "iscsiSessionCxnErrorStatsTable": iscsiSessionCxnErrorStatsTable,
       "iscsiSessionCxnErrorStatsEntry": iscsiSessionCxnErrorStatsEntry,
       "iscsiSsnCxnDigestErrors": iscsiSsnCxnDigestErrors,
       "iscsiSsnCxnTimeoutErrors": iscsiSsnCxnTimeoutErrors,
       "iscsiConnection": iscsiConnection,
       "iscsiConnectionAttributesTable": iscsiConnectionAttributesTable,
       "iscsiConnectionAttributesEntry": iscsiConnectionAttributesEntry,
       "iscsiCxnIndex": iscsiCxnIndex,
       "iscsiCxnCid": iscsiCxnCid,
       "iscsiCxnState": iscsiCxnState,
       "iscsiCxnAddrType": iscsiCxnAddrType,
       "iscsiCxnLocalAddr": iscsiCxnLocalAddr,
       "iscsiCxnProtocol": iscsiCxnProtocol,
       "iscsiCxnLocalPort": iscsiCxnLocalPort,
       "iscsiCxnRemoteAddr": iscsiCxnRemoteAddr,
       "iscsiCxnRemotePort": iscsiCxnRemotePort,
       "iscsiCxnMaxRecvDataSegLength": iscsiCxnMaxRecvDataSegLength,
       "iscsiCxnMaxXmitDataSegLength": iscsiCxnMaxXmitDataSegLength,
       "iscsiCxnHeaderIntegrity": iscsiCxnHeaderIntegrity,
       "iscsiCxnDataIntegrity": iscsiCxnDataIntegrity,
       "iscsiCxnRecvMarker": iscsiCxnRecvMarker,
       "iscsiCxnSendMarker": iscsiCxnSendMarker,
       "iscsiCxnVersionActive": iscsiCxnVersionActive,
       "iscsiConformance": iscsiConformance,
       "iscsiCompliances": iscsiCompliances,
       "iscsiComplianceV1": iscsiComplianceV1,
       "iscsiComplianceV2": iscsiComplianceV2,
       "iscsiGroups": iscsiGroups,
       "iscsiInstanceAttributesGroup": iscsiInstanceAttributesGroup,
       "iscsiInstanceSsnErrorStatsGroup": iscsiInstanceSsnErrorStatsGroup,
       "iscsiPortalAttributesGroup": iscsiPortalAttributesGroup,
       "iscsiTgtPortalAttributesGroup": iscsiTgtPortalAttributesGroup,
       "iscsiIntrPortalAttributesGroup": iscsiIntrPortalAttributesGroup,
       "iscsiNodeAttributesGroup": iscsiNodeAttributesGroup,
       "iscsiTargetAttributesGroup": iscsiTargetAttributesGroup,
       "iscsiTargetLoginStatsGroup": iscsiTargetLoginStatsGroup,
       "iscsiTargetLogoutStatsGroup": iscsiTargetLogoutStatsGroup,
       "iscsiTargetAuthGroup": iscsiTargetAuthGroup,
       "iscsiInitiatorAttributesGroup": iscsiInitiatorAttributesGroup,
       "iscsiInitiatorLoginStatsGroup": iscsiInitiatorLoginStatsGroup,
       "iscsiInitiatorLogoutStatsGroup": iscsiInitiatorLogoutStatsGroup,
       "iscsiInitiatorAuthGroup": iscsiInitiatorAuthGroup,
       "iscsiSessionAttributesGroup": iscsiSessionAttributesGroup,
       "iscsiSessionPDUStatsGroup": iscsiSessionPDUStatsGroup,
       "iscsiSessionOctetStatsGroup": iscsiSessionOctetStatsGroup,
       "iscsiSessionLCOctetStatsGroup": iscsiSessionLCOctetStatsGroup,
       "iscsiSessionCxnErrorStatsGroup": iscsiSessionCxnErrorStatsGroup,
       "iscsiConnectionAttributesGroup": iscsiConnectionAttributesGroup,
       "iscsiTgtLgnNotificationsGroup": iscsiTgtLgnNotificationsGroup,
       "iscsiIntrLgnNotificationsGroup": iscsiIntrLgnNotificationsGroup,
       "iscsiSsnFlrNotificationsGroup": iscsiSsnFlrNotificationsGroup,
       "iscsiPortalAttributesGroupV2": iscsiPortalAttributesGroupV2,
       "iscsiConnectionAttributesGroupV2": iscsiConnectionAttributesGroupV2,
       "iscsiNewObjectsV2": iscsiNewObjectsV2,
       "iscsiAdmin": iscsiAdmin,
       "iscsiDescriptors": iscsiDescriptors,
       "iscsiHeaderIntegrityTypes": iscsiHeaderIntegrityTypes,
       "iscsiHdrIntegrityNone": iscsiHdrIntegrityNone,
       "iscsiHdrIntegrityCrc32c": iscsiHdrIntegrityCrc32c,
       "iscsiDataIntegrityTypes": iscsiDataIntegrityTypes,
       "iscsiDataIntegrityNone": iscsiDataIntegrityNone,
       "iscsiDataIntegrityCrc32c": iscsiDataIntegrityCrc32c}
)
