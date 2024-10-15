# SNMP MIB module (CISCO-ISCSI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ISCSI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:07 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(AutonomousType,
 DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoIscsiModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94)
)
ciscoIscsiModule.setRevisions(
        ("2002-10-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CIscsiTransportProtocols(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class CIscsiDigestMethod(Integer32, TextualConvention):
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



# MIB Managed Objects in the order of their OIDs

_CIscsiObjects_ObjectIdentity = ObjectIdentity
cIscsiObjects = _CIscsiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1)
)
_CIscsiDescriptors_ObjectIdentity = ObjectIdentity
cIscsiDescriptors = _CIscsiDescriptors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1)
)
_CIscsiHeaderIntegrityTypes_ObjectIdentity = ObjectIdentity
cIscsiHeaderIntegrityTypes = _CIscsiHeaderIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 1)
)
_CIscsiHdrIntegrityNone_ObjectIdentity = ObjectIdentity
cIscsiHdrIntegrityNone = _CIscsiHdrIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cIscsiHdrIntegrityNone.setStatus("current")
_CIscsiHdrIntegrityCrc32c_ObjectIdentity = ObjectIdentity
cIscsiHdrIntegrityCrc32c = _CIscsiHdrIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cIscsiHdrIntegrityCrc32c.setStatus("current")
_CIscsiDataIntegrityTypes_ObjectIdentity = ObjectIdentity
cIscsiDataIntegrityTypes = _CIscsiDataIntegrityTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 2)
)
_CIscsiDataIntegrityNone_ObjectIdentity = ObjectIdentity
cIscsiDataIntegrityNone = _CIscsiDataIntegrityNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiDataIntegrityNone.setStatus("current")
_CIscsiDataIntegrityCrc32c_ObjectIdentity = ObjectIdentity
cIscsiDataIntegrityCrc32c = _CIscsiDataIntegrityCrc32c_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIscsiDataIntegrityCrc32c.setStatus("current")
_CIscsiInstance_ObjectIdentity = ObjectIdentity
cIscsiInstance = _CIscsiInstance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2)
)
_CIscsiInstanceAttributesTable_Object = MibTable
cIscsiInstanceAttributesTable = _CIscsiInstanceAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiInstanceAttributesTable.setStatus("current")
_CIscsiInstanceAttributesEntry_Object = MibTableRow
cIscsiInstanceAttributesEntry = _CIscsiInstanceAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1)
)
cIscsiInstanceAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
)
if mibBuilder.loadTexts:
    cIscsiInstanceAttributesEntry.setStatus("current")


class _CIscsiInstIndex_Type(Unsigned32):
    """Custom type cIscsiInstIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiInstIndex_Type.__name__ = "Unsigned32"
_CIscsiInstIndex_Object = MibTableColumn
cIscsiInstIndex = _CIscsiInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 1),
    _CIscsiInstIndex_Type()
)
cIscsiInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiInstIndex.setStatus("current")
_CIscsiInstDescr_Type = SnmpAdminString
_CIscsiInstDescr_Object = MibTableColumn
cIscsiInstDescr = _CIscsiInstDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 2),
    _CIscsiInstDescr_Type()
)
cIscsiInstDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstDescr.setStatus("current")


class _CIscsiInstVersionMin_Type(Unsigned32):
    """Custom type cIscsiInstVersionMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIscsiInstVersionMin_Type.__name__ = "Unsigned32"
_CIscsiInstVersionMin_Object = MibTableColumn
cIscsiInstVersionMin = _CIscsiInstVersionMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 3),
    _CIscsiInstVersionMin_Type()
)
cIscsiInstVersionMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstVersionMin.setStatus("current")


class _CIscsiInstVersionMax_Type(Unsigned32):
    """Custom type cIscsiInstVersionMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIscsiInstVersionMax_Type.__name__ = "Unsigned32"
_CIscsiInstVersionMax_Object = MibTableColumn
cIscsiInstVersionMax = _CIscsiInstVersionMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 4),
    _CIscsiInstVersionMax_Type()
)
cIscsiInstVersionMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstVersionMax.setStatus("current")
_CIscsiInstVendorID_Type = SnmpAdminString
_CIscsiInstVendorID_Object = MibTableColumn
cIscsiInstVendorID = _CIscsiInstVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 5),
    _CIscsiInstVendorID_Type()
)
cIscsiInstVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstVendorID.setStatus("current")
_CIscsiInstVendorVersion_Type = SnmpAdminString
_CIscsiInstVendorVersion_Object = MibTableColumn
cIscsiInstVendorVersion = _CIscsiInstVendorVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 6),
    _CIscsiInstVendorVersion_Type()
)
cIscsiInstVendorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstVendorVersion.setStatus("current")


class _CIscsiInstPortalNumber_Type(Unsigned32):
    """Custom type cIscsiInstPortalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiInstPortalNumber_Type.__name__ = "Unsigned32"
_CIscsiInstPortalNumber_Object = MibTableColumn
cIscsiInstPortalNumber = _CIscsiInstPortalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 7),
    _CIscsiInstPortalNumber_Type()
)
cIscsiInstPortalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstPortalNumber.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstPortalNumber.setUnits("transport endpoints")


class _CIscsiInstNodeNumber_Type(Unsigned32):
    """Custom type cIscsiInstNodeNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiInstNodeNumber_Type.__name__ = "Unsigned32"
_CIscsiInstNodeNumber_Object = MibTableColumn
cIscsiInstNodeNumber = _CIscsiInstNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 8),
    _CIscsiInstNodeNumber_Type()
)
cIscsiInstNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstNodeNumber.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstNodeNumber.setUnits("Internet Network Addresses")


class _CIscsiInstSessionNumber_Type(Unsigned32):
    """Custom type cIscsiInstSessionNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiInstSessionNumber_Type.__name__ = "Unsigned32"
_CIscsiInstSessionNumber_Object = MibTableColumn
cIscsiInstSessionNumber = _CIscsiInstSessionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 9),
    _CIscsiInstSessionNumber_Type()
)
cIscsiInstSessionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstSessionNumber.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstSessionNumber.setUnits("sessions")
_CIscsiInstSsnFailures_Type = Counter32
_CIscsiInstSsnFailures_Object = MibTableColumn
cIscsiInstSsnFailures = _CIscsiInstSsnFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 10),
    _CIscsiInstSsnFailures_Type()
)
cIscsiInstSsnFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstSsnFailures.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstSsnFailures.setUnits("sessions")
_CIscsiInstLastSsnFailureType_Type = AutonomousType
_CIscsiInstLastSsnFailureType_Object = MibTableColumn
cIscsiInstLastSsnFailureType = _CIscsiInstLastSsnFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 11),
    _CIscsiInstLastSsnFailureType_Type()
)
cIscsiInstLastSsnFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstLastSsnFailureType.setStatus("current")
_CIscsiInstLastSsnRmtNodeName_Type = SnmpAdminString
_CIscsiInstLastSsnRmtNodeName_Object = MibTableColumn
cIscsiInstLastSsnRmtNodeName = _CIscsiInstLastSsnRmtNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 1, 1, 12),
    _CIscsiInstLastSsnRmtNodeName_Type()
)
cIscsiInstLastSsnRmtNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstLastSsnRmtNodeName.setStatus("current")
_CIscsiInstanceSsnErrorStatsTable_Object = MibTable
cIscsiInstanceSsnErrorStatsTable = _CIscsiInstanceSsnErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cIscsiInstanceSsnErrorStatsTable.setStatus("current")
_CIscsiInstanceSsnErrorStatsEntry_Object = MibTableRow
cIscsiInstanceSsnErrorStatsEntry = _CIscsiInstanceSsnErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiInstanceSsnErrorStatsEntry.setStatus("current")
_CIscsiInstSsnDigestErrors_Type = Counter32
_CIscsiInstSsnDigestErrors_Object = MibTableColumn
cIscsiInstSsnDigestErrors = _CIscsiInstSsnDigestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 2, 1, 1),
    _CIscsiInstSsnDigestErrors_Type()
)
cIscsiInstSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstSsnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstSsnDigestErrors.setUnits("sessions")
_CIscsiInstSsnCxnTimeoutErrors_Type = Counter32
_CIscsiInstSsnCxnTimeoutErrors_Object = MibTableColumn
cIscsiInstSsnCxnTimeoutErrors = _CIscsiInstSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 2, 1, 2),
    _CIscsiInstSsnCxnTimeoutErrors_Type()
)
cIscsiInstSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstSsnCxnTimeoutErrors.setUnits("sessions")
_CIscsiInstSsnFormatErrors_Type = Counter32
_CIscsiInstSsnFormatErrors_Object = MibTableColumn
cIscsiInstSsnFormatErrors = _CIscsiInstSsnFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 2, 2, 1, 3),
    _CIscsiInstSsnFormatErrors_Type()
)
cIscsiInstSsnFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiInstSsnFormatErrors.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiInstSsnFormatErrors.setUnits("sessions")
_CIscsiPortal_ObjectIdentity = ObjectIdentity
cIscsiPortal = _CIscsiPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3)
)
_CIscsiPortalAttributesTable_Object = MibTable
cIscsiPortalAttributesTable = _CIscsiPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cIscsiPortalAttributesTable.setStatus("current")
_CIscsiPortalAttributesEntry_Object = MibTableRow
cIscsiPortalAttributesEntry = _CIscsiPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1)
)
cIscsiPortalAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cIscsiPortalAttributesEntry.setStatus("current")


class _CIscsiPortalIndex_Type(Unsigned32):
    """Custom type cIscsiPortalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiPortalIndex_Type.__name__ = "Unsigned32"
_CIscsiPortalIndex_Object = MibTableColumn
cIscsiPortalIndex = _CIscsiPortalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 1),
    _CIscsiPortalIndex_Type()
)
cIscsiPortalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiPortalIndex.setStatus("current")
_CIscsiPortalRowStatus_Type = RowStatus
_CIscsiPortalRowStatus_Object = MibTableColumn
cIscsiPortalRowStatus = _CIscsiPortalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 2),
    _CIscsiPortalRowStatus_Type()
)
cIscsiPortalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalRowStatus.setStatus("current")


class _CIscsiPortalRoles_Type(Bits):
    """Custom type cIscsiPortalRoles based on Bits"""
    namedValues = NamedValues(
        *(("initiatorTypePortal", 1),
          ("targetTypePortal", 0))
    )

_CIscsiPortalRoles_Type.__name__ = "Bits"
_CIscsiPortalRoles_Object = MibTableColumn
cIscsiPortalRoles = _CIscsiPortalRoles_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 3),
    _CIscsiPortalRoles_Type()
)
cIscsiPortalRoles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalRoles.setStatus("current")
_CIscsiPortalAddrType_Type = InetAddressType
_CIscsiPortalAddrType_Object = MibTableColumn
cIscsiPortalAddrType = _CIscsiPortalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 4),
    _CIscsiPortalAddrType_Type()
)
cIscsiPortalAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalAddrType.setStatus("current")
_CIscsiPortalAddr_Type = InetAddress
_CIscsiPortalAddr_Object = MibTableColumn
cIscsiPortalAddr = _CIscsiPortalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 5),
    _CIscsiPortalAddr_Type()
)
cIscsiPortalAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalAddr.setStatus("current")


class _CIscsiPortalProtocol_Type(CIscsiTransportProtocols):
    """Custom type cIscsiPortalProtocol based on CIscsiTransportProtocols"""
    defaultValue = 6


_CIscsiPortalProtocol_Object = MibTableColumn
cIscsiPortalProtocol = _CIscsiPortalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 6),
    _CIscsiPortalProtocol_Type()
)
cIscsiPortalProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalProtocol.setStatus("current")


class _CIscsiPortalMaxRecvDataSegLength_Type(Unsigned32):
    """Custom type cIscsiPortalMaxRecvDataSegLength based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiPortalMaxRecvDataSegLength_Type.__name__ = "Unsigned32"
_CIscsiPortalMaxRecvDataSegLength_Object = MibTableColumn
cIscsiPortalMaxRecvDataSegLength = _CIscsiPortalMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 7),
    _CIscsiPortalMaxRecvDataSegLength_Type()
)
cIscsiPortalMaxRecvDataSegLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalMaxRecvDataSegLength.setStatus("current")


class _CIscsiPortalPrimaryHdrDigest_Type(CIscsiDigestMethod):
    """Custom type cIscsiPortalPrimaryHdrDigest based on CIscsiDigestMethod"""


_CIscsiPortalPrimaryHdrDigest_Object = MibTableColumn
cIscsiPortalPrimaryHdrDigest = _CIscsiPortalPrimaryHdrDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 8),
    _CIscsiPortalPrimaryHdrDigest_Type()
)
cIscsiPortalPrimaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalPrimaryHdrDigest.setStatus("current")


class _CIscsiPortalPrimaryDataDigest_Type(CIscsiDigestMethod):
    """Custom type cIscsiPortalPrimaryDataDigest based on CIscsiDigestMethod"""


_CIscsiPortalPrimaryDataDigest_Object = MibTableColumn
cIscsiPortalPrimaryDataDigest = _CIscsiPortalPrimaryDataDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 9),
    _CIscsiPortalPrimaryDataDigest_Type()
)
cIscsiPortalPrimaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalPrimaryDataDigest.setStatus("current")


class _CIscsiPortalSecondaryHdrDigest_Type(CIscsiDigestMethod):
    """Custom type cIscsiPortalSecondaryHdrDigest based on CIscsiDigestMethod"""


_CIscsiPortalSecondaryHdrDigest_Object = MibTableColumn
cIscsiPortalSecondaryHdrDigest = _CIscsiPortalSecondaryHdrDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 10),
    _CIscsiPortalSecondaryHdrDigest_Type()
)
cIscsiPortalSecondaryHdrDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalSecondaryHdrDigest.setStatus("current")


class _CIscsiPortalSecondaryDataDigest_Type(CIscsiDigestMethod):
    """Custom type cIscsiPortalSecondaryDataDigest based on CIscsiDigestMethod"""


_CIscsiPortalSecondaryDataDigest_Object = MibTableColumn
cIscsiPortalSecondaryDataDigest = _CIscsiPortalSecondaryDataDigest_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 11),
    _CIscsiPortalSecondaryDataDigest_Type()
)
cIscsiPortalSecondaryDataDigest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalSecondaryDataDigest.setStatus("current")
_CIscsiPortalRecvMarker_Type = TruthValue
_CIscsiPortalRecvMarker_Object = MibTableColumn
cIscsiPortalRecvMarker = _CIscsiPortalRecvMarker_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 3, 1, 1, 12),
    _CIscsiPortalRecvMarker_Type()
)
cIscsiPortalRecvMarker.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiPortalRecvMarker.setStatus("current")
_CIscsiTargetPortal_ObjectIdentity = ObjectIdentity
cIscsiTargetPortal = _CIscsiTargetPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 4)
)
_CIscsiTgtPortalAttributesTable_Object = MibTable
cIscsiTgtPortalAttributesTable = _CIscsiTgtPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cIscsiTgtPortalAttributesTable.setStatus("current")
_CIscsiTgtPortalAttributesEntry_Object = MibTableRow
cIscsiTgtPortalAttributesEntry = _CIscsiTgtPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 4, 1, 1)
)
cIscsiTgtPortalAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cIscsiTgtPortalAttributesEntry.setStatus("current")


class _CIscsiTgtPortalPort_Type(Unsigned32):
    """Custom type cIscsiTgtPortalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiTgtPortalPort_Type.__name__ = "Unsigned32"
_CIscsiTgtPortalPort_Object = MibTableColumn
cIscsiTgtPortalPort = _CIscsiTgtPortalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 4, 1, 1, 1),
    _CIscsiTgtPortalPort_Type()
)
cIscsiTgtPortalPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiTgtPortalPort.setStatus("current")


class _CIscsiTgtPortalTag_Type(Unsigned32):
    """Custom type cIscsiTgtPortalTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiTgtPortalTag_Type.__name__ = "Unsigned32"
_CIscsiTgtPortalTag_Object = MibTableColumn
cIscsiTgtPortalTag = _CIscsiTgtPortalTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 4, 1, 1, 2),
    _CIscsiTgtPortalTag_Type()
)
cIscsiTgtPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiTgtPortalTag.setStatus("current")
_CIscsiInitiatorPortal_ObjectIdentity = ObjectIdentity
cIscsiInitiatorPortal = _CIscsiInitiatorPortal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 5)
)
_CIscsiIntrPortalAttributesTable_Object = MibTable
cIscsiIntrPortalAttributesTable = _CIscsiIntrPortalAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cIscsiIntrPortalAttributesTable.setStatus("current")
_CIscsiIntrPortalAttributesEntry_Object = MibTableRow
cIscsiIntrPortalAttributesEntry = _CIscsiIntrPortalAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 5, 1, 1)
)
cIscsiIntrPortalAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiPortalIndex"),
)
if mibBuilder.loadTexts:
    cIscsiIntrPortalAttributesEntry.setStatus("current")


class _CIscsiIntrPortalTag_Type(Unsigned32):
    """Custom type cIscsiIntrPortalTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiIntrPortalTag_Type.__name__ = "Unsigned32"
_CIscsiIntrPortalTag_Object = MibTableColumn
cIscsiIntrPortalTag = _CIscsiIntrPortalTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 5, 1, 1, 1),
    _CIscsiIntrPortalTag_Type()
)
cIscsiIntrPortalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiIntrPortalTag.setStatus("current")
_CIscsiNode_ObjectIdentity = ObjectIdentity
cIscsiNode = _CIscsiNode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6)
)
_CIscsiNodeAttributesTable_Object = MibTable
cIscsiNodeAttributesTable = _CIscsiNodeAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cIscsiNodeAttributesTable.setStatus("current")
_CIscsiNodeAttributesEntry_Object = MibTableRow
cIscsiNodeAttributesEntry = _CIscsiNodeAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1)
)
cIscsiNodeAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    cIscsiNodeAttributesEntry.setStatus("current")


class _CIscsiNodeIndex_Type(Unsigned32):
    """Custom type cIscsiNodeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiNodeIndex_Type.__name__ = "Unsigned32"
_CIscsiNodeIndex_Object = MibTableColumn
cIscsiNodeIndex = _CIscsiNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 1),
    _CIscsiNodeIndex_Type()
)
cIscsiNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiNodeIndex.setStatus("current")
_CIscsiNodeName_Type = SnmpAdminString
_CIscsiNodeName_Object = MibTableColumn
cIscsiNodeName = _CIscsiNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 2),
    _CIscsiNodeName_Type()
)
cIscsiNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeName.setStatus("current")
_CIscsiNodeAlias_Type = SnmpAdminString
_CIscsiNodeAlias_Object = MibTableColumn
cIscsiNodeAlias = _CIscsiNodeAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 3),
    _CIscsiNodeAlias_Type()
)
cIscsiNodeAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeAlias.setStatus("current")


class _CIscsiNodeRoles_Type(Bits):
    """Custom type cIscsiNodeRoles based on Bits"""
    namedValues = NamedValues(
        *(("initiatorTypeNode", 1),
          ("targetTypeNode", 0))
    )

_CIscsiNodeRoles_Type.__name__ = "Bits"
_CIscsiNodeRoles_Object = MibTableColumn
cIscsiNodeRoles = _CIscsiNodeRoles_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 4),
    _CIscsiNodeRoles_Type()
)
cIscsiNodeRoles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeRoles.setStatus("current")
_CIscsiNodeTransportType_Type = RowPointer
_CIscsiNodeTransportType_Object = MibTableColumn
cIscsiNodeTransportType = _CIscsiNodeTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 5),
    _CIscsiNodeTransportType_Type()
)
cIscsiNodeTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeTransportType.setStatus("current")


class _CIscsiNodeInitialR2T_Type(TruthValue):
    """Custom type cIscsiNodeInitialR2T based on TruthValue"""


_CIscsiNodeInitialR2T_Object = MibTableColumn
cIscsiNodeInitialR2T = _CIscsiNodeInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 6),
    _CIscsiNodeInitialR2T_Type()
)
cIscsiNodeInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeInitialR2T.setStatus("current")


class _CIscsiNodeBidiInitialR2T_Type(TruthValue):
    """Custom type cIscsiNodeBidiInitialR2T based on TruthValue"""


_CIscsiNodeBidiInitialR2T_Object = MibTableColumn
cIscsiNodeBidiInitialR2T = _CIscsiNodeBidiInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 7),
    _CIscsiNodeBidiInitialR2T_Type()
)
cIscsiNodeBidiInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiNodeBidiInitialR2T.setStatus("current")


class _CIscsiNodeImmediateData_Type(TruthValue):
    """Custom type cIscsiNodeImmediateData based on TruthValue"""


_CIscsiNodeImmediateData_Object = MibTableColumn
cIscsiNodeImmediateData = _CIscsiNodeImmediateData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 8),
    _CIscsiNodeImmediateData_Type()
)
cIscsiNodeImmediateData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeImmediateData.setStatus("current")


class _CIscsiNodeMaxOutstandingR2T_Type(Unsigned32):
    """Custom type cIscsiNodeMaxOutstandingR2T based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiNodeMaxOutstandingR2T_Type.__name__ = "Unsigned32"
_CIscsiNodeMaxOutstandingR2T_Object = MibTableColumn
cIscsiNodeMaxOutstandingR2T = _CIscsiNodeMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 9),
    _CIscsiNodeMaxOutstandingR2T_Type()
)
cIscsiNodeMaxOutstandingR2T.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeMaxOutstandingR2T.setStatus("current")


class _CIscsiNodeFirstBurstSize_Type(Unsigned32):
    """Custom type cIscsiNodeFirstBurstSize based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiNodeFirstBurstSize_Type.__name__ = "Unsigned32"
_CIscsiNodeFirstBurstSize_Object = MibTableColumn
cIscsiNodeFirstBurstSize = _CIscsiNodeFirstBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 10),
    _CIscsiNodeFirstBurstSize_Type()
)
cIscsiNodeFirstBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeFirstBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiNodeFirstBurstSize.setUnits("bytes")


class _CIscsiNodeMaxBurstSize_Type(Unsigned32):
    """Custom type cIscsiNodeMaxBurstSize based on Unsigned32"""
    defaultValue = 262144

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiNodeMaxBurstSize_Type.__name__ = "Unsigned32"
_CIscsiNodeMaxBurstSize_Object = MibTableColumn
cIscsiNodeMaxBurstSize = _CIscsiNodeMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 11),
    _CIscsiNodeMaxBurstSize_Type()
)
cIscsiNodeMaxBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiNodeMaxBurstSize.setUnits("bytes")


class _CIscsiNodeMaxConnections_Type(Unsigned32):
    """Custom type cIscsiNodeMaxConnections based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiNodeMaxConnections_Type.__name__ = "Unsigned32"
_CIscsiNodeMaxConnections_Object = MibTableColumn
cIscsiNodeMaxConnections = _CIscsiNodeMaxConnections_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 12),
    _CIscsiNodeMaxConnections_Type()
)
cIscsiNodeMaxConnections.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeMaxConnections.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiNodeMaxConnections.setUnits("connections")


class _CIscsiNodeDataSequenceInOrder_Type(TruthValue):
    """Custom type cIscsiNodeDataSequenceInOrder based on TruthValue"""


_CIscsiNodeDataSequenceInOrder_Object = MibTableColumn
cIscsiNodeDataSequenceInOrder = _CIscsiNodeDataSequenceInOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 13),
    _CIscsiNodeDataSequenceInOrder_Type()
)
cIscsiNodeDataSequenceInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeDataSequenceInOrder.setStatus("current")


class _CIscsiNodeDataPduInOrder_Type(TruthValue):
    """Custom type cIscsiNodeDataPduInOrder based on TruthValue"""


_CIscsiNodeDataPduInOrder_Object = MibTableColumn
cIscsiNodeDataPduInOrder = _CIscsiNodeDataPduInOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 14),
    _CIscsiNodeDataPduInOrder_Type()
)
cIscsiNodeDataPduInOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeDataPduInOrder.setStatus("current")


class _CIscsiNodeDefaultTime2Wait_Type(Unsigned32):
    """Custom type cIscsiNodeDefaultTime2Wait based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CIscsiNodeDefaultTime2Wait_Type.__name__ = "Unsigned32"
_CIscsiNodeDefaultTime2Wait_Object = MibTableColumn
cIscsiNodeDefaultTime2Wait = _CIscsiNodeDefaultTime2Wait_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 15),
    _CIscsiNodeDefaultTime2Wait_Type()
)
cIscsiNodeDefaultTime2Wait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeDefaultTime2Wait.setStatus("current")


class _CIscsiNodeDefaultTime2Retain_Type(Unsigned32):
    """Custom type cIscsiNodeDefaultTime2Retain based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CIscsiNodeDefaultTime2Retain_Type.__name__ = "Unsigned32"
_CIscsiNodeDefaultTime2Retain_Object = MibTableColumn
cIscsiNodeDefaultTime2Retain = _CIscsiNodeDefaultTime2Retain_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 16),
    _CIscsiNodeDefaultTime2Retain_Type()
)
cIscsiNodeDefaultTime2Retain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeDefaultTime2Retain.setStatus("current")


class _CIscsiNodeErrorRecoveryLevel_Type(Unsigned32):
    """Custom type cIscsiNodeErrorRecoveryLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIscsiNodeErrorRecoveryLevel_Type.__name__ = "Unsigned32"
_CIscsiNodeErrorRecoveryLevel_Object = MibTableColumn
cIscsiNodeErrorRecoveryLevel = _CIscsiNodeErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 6, 1, 1, 17),
    _CIscsiNodeErrorRecoveryLevel_Type()
)
cIscsiNodeErrorRecoveryLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cIscsiNodeErrorRecoveryLevel.setStatus("current")
_CIscsiTarget_ObjectIdentity = ObjectIdentity
cIscsiTarget = _CIscsiTarget_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7)
)
_CIscsiTargetAttributesTable_Object = MibTable
cIscsiTargetAttributesTable = _CIscsiTargetAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cIscsiTargetAttributesTable.setStatus("current")
_CIscsiTargetAttributesEntry_Object = MibTableRow
cIscsiTargetAttributesEntry = _CIscsiTargetAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1)
)
cIscsiTargetAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    cIscsiTargetAttributesEntry.setStatus("current")
_CIscsiTgtLoginFailures_Type = Counter32
_CIscsiTgtLoginFailures_Object = MibTableColumn
cIscsiTgtLoginFailures = _CIscsiTgtLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 1),
    _CIscsiTgtLoginFailures_Type()
)
cIscsiTgtLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginFailures.setUnits("failed login attempts")
_CIscsiTgtLastFailureTime_Type = TimeStamp
_CIscsiTgtLastFailureTime_Object = MibTableColumn
cIscsiTgtLastFailureTime = _CIscsiTgtLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 2),
    _CIscsiTgtLastFailureTime_Type()
)
cIscsiTgtLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLastFailureTime.setStatus("current")
_CIscsiTgtLastFailureType_Type = AutonomousType
_CIscsiTgtLastFailureType_Object = MibTableColumn
cIscsiTgtLastFailureType = _CIscsiTgtLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 3),
    _CIscsiTgtLastFailureType_Type()
)
cIscsiTgtLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLastFailureType.setStatus("current")
_CIscsiTgtLastIntrFailureName_Type = SnmpAdminString
_CIscsiTgtLastIntrFailureName_Object = MibTableColumn
cIscsiTgtLastIntrFailureName = _CIscsiTgtLastIntrFailureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 4),
    _CIscsiTgtLastIntrFailureName_Type()
)
cIscsiTgtLastIntrFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLastIntrFailureName.setStatus("current")
_CIscsiTgtLastIntrFailureAddrType_Type = InetAddressType
_CIscsiTgtLastIntrFailureAddrType_Object = MibTableColumn
cIscsiTgtLastIntrFailureAddrType = _CIscsiTgtLastIntrFailureAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 5),
    _CIscsiTgtLastIntrFailureAddrType_Type()
)
cIscsiTgtLastIntrFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLastIntrFailureAddrType.setStatus("current")
_CIscsiTgtLastIntrFailureAddr_Type = InetAddress
_CIscsiTgtLastIntrFailureAddr_Object = MibTableColumn
cIscsiTgtLastIntrFailureAddr = _CIscsiTgtLastIntrFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 1, 1, 6),
    _CIscsiTgtLastIntrFailureAddr_Type()
)
cIscsiTgtLastIntrFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLastIntrFailureAddr.setStatus("current")
_CIscsiTargetLoginStatsTable_Object = MibTable
cIscsiTargetLoginStatsTable = _CIscsiTargetLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cIscsiTargetLoginStatsTable.setStatus("current")
_CIscsiTargetLoginStatsEntry_Object = MibTableRow
cIscsiTargetLoginStatsEntry = _CIscsiTargetLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiTargetLoginStatsEntry.setStatus("current")
_CIscsiTgtLoginAccepts_Type = Counter32
_CIscsiTgtLoginAccepts_Object = MibTableColumn
cIscsiTgtLoginAccepts = _CIscsiTgtLoginAccepts_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 1),
    _CIscsiTgtLoginAccepts_Type()
)
cIscsiTgtLoginAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAccepts.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAccepts.setUnits("successful logins")
_CIscsiTgtLoginOtherFails_Type = Counter32
_CIscsiTgtLoginOtherFails_Object = MibTableColumn
cIscsiTgtLoginOtherFails = _CIscsiTgtLoginOtherFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 2),
    _CIscsiTgtLoginOtherFails_Type()
)
cIscsiTgtLoginOtherFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginOtherFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginOtherFails.setUnits("failed logins")
_CIscsiTgtLoginRedirects_Type = Counter32
_CIscsiTgtLoginRedirects_Object = MibTableColumn
cIscsiTgtLoginRedirects = _CIscsiTgtLoginRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 3),
    _CIscsiTgtLoginRedirects_Type()
)
cIscsiTgtLoginRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginRedirects.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginRedirects.setUnits("failed logins")
_CIscsiTgtLoginAuthorizeFails_Type = Counter32
_CIscsiTgtLoginAuthorizeFails_Object = MibTableColumn
cIscsiTgtLoginAuthorizeFails = _CIscsiTgtLoginAuthorizeFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 4),
    _CIscsiTgtLoginAuthorizeFails_Type()
)
cIscsiTgtLoginAuthorizeFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAuthorizeFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAuthorizeFails.setUnits("failed logins")
_CIscsiTgtLoginAuthenticateFails_Type = Counter32
_CIscsiTgtLoginAuthenticateFails_Object = MibTableColumn
cIscsiTgtLoginAuthenticateFails = _CIscsiTgtLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 5),
    _CIscsiTgtLoginAuthenticateFails_Type()
)
cIscsiTgtLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginAuthenticateFails.setUnits("failed logins")
_CIscsiTgtLoginNegotiateFails_Type = Counter32
_CIscsiTgtLoginNegotiateFails_Object = MibTableColumn
cIscsiTgtLoginNegotiateFails = _CIscsiTgtLoginNegotiateFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 2, 1, 6),
    _CIscsiTgtLoginNegotiateFails_Type()
)
cIscsiTgtLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLoginNegotiateFails.setUnits("failed logins")
_CIscsiTargetLogoutStatsTable_Object = MibTable
cIscsiTargetLogoutStatsTable = _CIscsiTargetLogoutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cIscsiTargetLogoutStatsTable.setStatus("current")
_CIscsiTargetLogoutStatsEntry_Object = MibTableRow
cIscsiTargetLogoutStatsEntry = _CIscsiTargetLogoutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 3, 1)
)
if mibBuilder.loadTexts:
    cIscsiTargetLogoutStatsEntry.setStatus("current")
_CIscsiTgtLogoutNormals_Type = Counter32
_CIscsiTgtLogoutNormals_Object = MibTableColumn
cIscsiTgtLogoutNormals = _CIscsiTgtLogoutNormals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 3, 1, 1),
    _CIscsiTgtLogoutNormals_Type()
)
cIscsiTgtLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLogoutNormals.setUnits("normal logouts")
_CIscsiTgtLogoutOthers_Type = Counter32
_CIscsiTgtLogoutOthers_Object = MibTableColumn
cIscsiTgtLogoutOthers = _CIscsiTgtLogoutOthers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 7, 3, 1, 2),
    _CIscsiTgtLogoutOthers_Type()
)
cIscsiTgtLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiTgtLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiTgtLogoutOthers.setUnits("abnormal logouts")
_CIscsiTgtAuthorization_ObjectIdentity = ObjectIdentity
cIscsiTgtAuthorization = _CIscsiTgtAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8)
)
_CIscsiTgtAuthAttributesTable_Object = MibTable
cIscsiTgtAuthAttributesTable = _CIscsiTgtAuthAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cIscsiTgtAuthAttributesTable.setStatus("current")
_CIscsiTgtAuthAttributesEntry_Object = MibTableRow
cIscsiTgtAuthAttributesEntry = _CIscsiTgtAuthAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8, 1, 1)
)
cIscsiTgtAuthAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiTgtAuthIndex"),
)
if mibBuilder.loadTexts:
    cIscsiTgtAuthAttributesEntry.setStatus("current")


class _CIscsiTgtAuthIndex_Type(Unsigned32):
    """Custom type cIscsiTgtAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiTgtAuthIndex_Type.__name__ = "Unsigned32"
_CIscsiTgtAuthIndex_Object = MibTableColumn
cIscsiTgtAuthIndex = _CIscsiTgtAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8, 1, 1, 1),
    _CIscsiTgtAuthIndex_Type()
)
cIscsiTgtAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiTgtAuthIndex.setStatus("current")
_CIscsiTgtAuthRowStatus_Type = RowStatus
_CIscsiTgtAuthRowStatus_Object = MibTableColumn
cIscsiTgtAuthRowStatus = _CIscsiTgtAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8, 1, 1, 2),
    _CIscsiTgtAuthRowStatus_Type()
)
cIscsiTgtAuthRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiTgtAuthRowStatus.setStatus("current")
_CIscsiTgtAuthIdentity_Type = RowPointer
_CIscsiTgtAuthIdentity_Object = MibTableColumn
cIscsiTgtAuthIdentity = _CIscsiTgtAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 8, 1, 1, 3),
    _CIscsiTgtAuthIdentity_Type()
)
cIscsiTgtAuthIdentity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cIscsiTgtAuthIdentity.setStatus("current")
_CIscsiInitiator_ObjectIdentity = ObjectIdentity
cIscsiInitiator = _CIscsiInitiator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9)
)
_CIscsiInitiatorAttributesTable_Object = MibTable
cIscsiInitiatorAttributesTable = _CIscsiInitiatorAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cIscsiInitiatorAttributesTable.setStatus("current")
_CIscsiInitiatorAttributesEntry_Object = MibTableRow
cIscsiInitiatorAttributesEntry = _CIscsiInitiatorAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1)
)
cIscsiInitiatorAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
)
if mibBuilder.loadTexts:
    cIscsiInitiatorAttributesEntry.setStatus("current")
_CIscsiIntrLoginFailures_Type = Counter32
_CIscsiIntrLoginFailures_Object = MibTableColumn
cIscsiIntrLoginFailures = _CIscsiIntrLoginFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 1),
    _CIscsiIntrLoginFailures_Type()
)
cIscsiIntrLoginFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginFailures.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginFailures.setUnits("failed logins")
_CIscsiIntrLastFailureTime_Type = TimeStamp
_CIscsiIntrLastFailureTime_Object = MibTableColumn
cIscsiIntrLastFailureTime = _CIscsiIntrLastFailureTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 2),
    _CIscsiIntrLastFailureTime_Type()
)
cIscsiIntrLastFailureTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLastFailureTime.setStatus("current")
_CIscsiIntrLastFailureType_Type = AutonomousType
_CIscsiIntrLastFailureType_Object = MibTableColumn
cIscsiIntrLastFailureType = _CIscsiIntrLastFailureType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 3),
    _CIscsiIntrLastFailureType_Type()
)
cIscsiIntrLastFailureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLastFailureType.setStatus("current")
_CIscsiIntrLastTgtFailureName_Type = SnmpAdminString
_CIscsiIntrLastTgtFailureName_Object = MibTableColumn
cIscsiIntrLastTgtFailureName = _CIscsiIntrLastTgtFailureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 4),
    _CIscsiIntrLastTgtFailureName_Type()
)
cIscsiIntrLastTgtFailureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLastTgtFailureName.setStatus("current")
_CIscsiIntrLastTgtFailureAddrType_Type = InetAddressType
_CIscsiIntrLastTgtFailureAddrType_Object = MibTableColumn
cIscsiIntrLastTgtFailureAddrType = _CIscsiIntrLastTgtFailureAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 5),
    _CIscsiIntrLastTgtFailureAddrType_Type()
)
cIscsiIntrLastTgtFailureAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLastTgtFailureAddrType.setStatus("current")
_CIscsiIntrLastTgtFailureAddr_Type = InetAddress
_CIscsiIntrLastTgtFailureAddr_Object = MibTableColumn
cIscsiIntrLastTgtFailureAddr = _CIscsiIntrLastTgtFailureAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 1, 1, 6),
    _CIscsiIntrLastTgtFailureAddr_Type()
)
cIscsiIntrLastTgtFailureAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLastTgtFailureAddr.setStatus("current")
_CIscsiInitiatorLoginStatsTable_Object = MibTable
cIscsiInitiatorLoginStatsTable = _CIscsiInitiatorLoginStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2)
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLoginStatsTable.setStatus("current")
_CIscsiInitiatorLoginStatsEntry_Object = MibTableRow
cIscsiInitiatorLoginStatsEntry = _CIscsiInitiatorLoginStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLoginStatsEntry.setStatus("current")
_CIscsiIntrLoginAcceptRsps_Type = Counter32
_CIscsiIntrLoginAcceptRsps_Object = MibTableColumn
cIscsiIntrLoginAcceptRsps = _CIscsiIntrLoginAcceptRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 1),
    _CIscsiIntrLoginAcceptRsps_Type()
)
cIscsiIntrLoginAcceptRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAcceptRsps.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAcceptRsps.setUnits("successful logins")
_CIscsiIntrLoginOtherFailRsps_Type = Counter32
_CIscsiIntrLoginOtherFailRsps_Object = MibTableColumn
cIscsiIntrLoginOtherFailRsps = _CIscsiIntrLoginOtherFailRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 2),
    _CIscsiIntrLoginOtherFailRsps_Type()
)
cIscsiIntrLoginOtherFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginOtherFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginOtherFailRsps.setUnits("failed logins")
_CIscsiIntrLoginRedirectRsps_Type = Counter32
_CIscsiIntrLoginRedirectRsps_Object = MibTableColumn
cIscsiIntrLoginRedirectRsps = _CIscsiIntrLoginRedirectRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 3),
    _CIscsiIntrLoginRedirectRsps_Type()
)
cIscsiIntrLoginRedirectRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginRedirectRsps.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginRedirectRsps.setUnits("failed logins")
_CIscsiIntrLoginAuthFailRsps_Type = Counter32
_CIscsiIntrLoginAuthFailRsps_Object = MibTableColumn
cIscsiIntrLoginAuthFailRsps = _CIscsiIntrLoginAuthFailRsps_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 4),
    _CIscsiIntrLoginAuthFailRsps_Type()
)
cIscsiIntrLoginAuthFailRsps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAuthFailRsps.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAuthFailRsps.setUnits("failed logins")
_CIscsiIntrLoginAuthenticateFails_Type = Counter32
_CIscsiIntrLoginAuthenticateFails_Object = MibTableColumn
cIscsiIntrLoginAuthenticateFails = _CIscsiIntrLoginAuthenticateFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 5),
    _CIscsiIntrLoginAuthenticateFails_Type()
)
cIscsiIntrLoginAuthenticateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAuthenticateFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginAuthenticateFails.setUnits("failed logins")
_CIscsiIntrLoginNegotiateFails_Type = Counter32
_CIscsiIntrLoginNegotiateFails_Object = MibTableColumn
cIscsiIntrLoginNegotiateFails = _CIscsiIntrLoginNegotiateFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 2, 1, 6),
    _CIscsiIntrLoginNegotiateFails_Type()
)
cIscsiIntrLoginNegotiateFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLoginNegotiateFails.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLoginNegotiateFails.setUnits("failed logins")
_CIscsiInitiatorLogoutStatsTable_Object = MibTable
cIscsiInitiatorLogoutStatsTable = _CIscsiInitiatorLogoutStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 3)
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLogoutStatsTable.setStatus("current")
_CIscsiInitiatorLogoutStatsEntry_Object = MibTableRow
cIscsiInitiatorLogoutStatsEntry = _CIscsiInitiatorLogoutStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 3, 1)
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLogoutStatsEntry.setStatus("current")
_CIscsiIntrLogoutNormals_Type = Counter32
_CIscsiIntrLogoutNormals_Object = MibTableColumn
cIscsiIntrLogoutNormals = _CIscsiIntrLogoutNormals_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 3, 1, 1),
    _CIscsiIntrLogoutNormals_Type()
)
cIscsiIntrLogoutNormals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLogoutNormals.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLogoutNormals.setUnits("normal logouts")
_CIscsiIntrLogoutOthers_Type = Counter32
_CIscsiIntrLogoutOthers_Object = MibTableColumn
cIscsiIntrLogoutOthers = _CIscsiIntrLogoutOthers_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 9, 3, 1, 2),
    _CIscsiIntrLogoutOthers_Type()
)
cIscsiIntrLogoutOthers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrLogoutOthers.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiIntrLogoutOthers.setUnits("abnormal logouts")
_CIscsiIntrAuthorization_ObjectIdentity = ObjectIdentity
cIscsiIntrAuthorization = _CIscsiIntrAuthorization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10)
)
_CIscsiIntrAuthAttributesTable_Object = MibTable
cIscsiIntrAuthAttributesTable = _CIscsiIntrAuthAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cIscsiIntrAuthAttributesTable.setStatus("current")
_CIscsiIntrAuthAttributesEntry_Object = MibTableRow
cIscsiIntrAuthAttributesEntry = _CIscsiIntrAuthAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10, 1, 1)
)
cIscsiIntrAuthAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiIntrAuthIndex"),
)
if mibBuilder.loadTexts:
    cIscsiIntrAuthAttributesEntry.setStatus("current")


class _CIscsiIntrAuthIndex_Type(Unsigned32):
    """Custom type cIscsiIntrAuthIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiIntrAuthIndex_Type.__name__ = "Unsigned32"
_CIscsiIntrAuthIndex_Object = MibTableColumn
cIscsiIntrAuthIndex = _CIscsiIntrAuthIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10, 1, 1, 1),
    _CIscsiIntrAuthIndex_Type()
)
cIscsiIntrAuthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiIntrAuthIndex.setStatus("current")
_CIscsiIntrAuthRowStatus_Type = RowStatus
_CIscsiIntrAuthRowStatus_Object = MibTableColumn
cIscsiIntrAuthRowStatus = _CIscsiIntrAuthRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10, 1, 1, 2),
    _CIscsiIntrAuthRowStatus_Type()
)
cIscsiIntrAuthRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrAuthRowStatus.setStatus("current")
_CIscsiIntrAuthIdentity_Type = RowPointer
_CIscsiIntrAuthIdentity_Object = MibTableColumn
cIscsiIntrAuthIdentity = _CIscsiIntrAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 10, 1, 1, 3),
    _CIscsiIntrAuthIdentity_Type()
)
cIscsiIntrAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiIntrAuthIdentity.setStatus("current")
_CIscsiSession_ObjectIdentity = ObjectIdentity
cIscsiSession = _CIscsiSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11)
)
_CIscsiSessionAttributesTable_Object = MibTable
cIscsiSessionAttributesTable = _CIscsiSessionAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cIscsiSessionAttributesTable.setStatus("current")
_CIscsiSessionAttributesEntry_Object = MibTableRow
cIscsiSessionAttributesEntry = _CIscsiSessionAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1)
)
cIscsiSessionAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiSsnIndex"),
)
if mibBuilder.loadTexts:
    cIscsiSessionAttributesEntry.setStatus("current")


class _CIscsiSsnIndex_Type(Unsigned32):
    """Custom type cIscsiSsnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiSsnIndex_Type.__name__ = "Unsigned32"
_CIscsiSsnIndex_Object = MibTableColumn
cIscsiSsnIndex = _CIscsiSsnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 1),
    _CIscsiSsnIndex_Type()
)
cIscsiSsnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiSsnIndex.setStatus("current")


class _CIscsiSsnDirection_Type(Integer32):
    """Custom type cIscsiSsnDirection based on Integer32"""
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


_CIscsiSsnDirection_Type.__name__ = "Integer32"
_CIscsiSsnDirection_Object = MibTableColumn
cIscsiSsnDirection = _CIscsiSsnDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 2),
    _CIscsiSsnDirection_Type()
)
cIscsiSsnDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnDirection.setStatus("current")
_CIscsiSsnInitiatorName_Type = SnmpAdminString
_CIscsiSsnInitiatorName_Object = MibTableColumn
cIscsiSsnInitiatorName = _CIscsiSsnInitiatorName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 3),
    _CIscsiSsnInitiatorName_Type()
)
cIscsiSsnInitiatorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnInitiatorName.setStatus("current")
_CIscsiSsnTargetName_Type = SnmpAdminString
_CIscsiSsnTargetName_Object = MibTableColumn
cIscsiSsnTargetName = _CIscsiSsnTargetName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 4),
    _CIscsiSsnTargetName_Type()
)
cIscsiSsnTargetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnTargetName.setStatus("current")


class _CIscsiSsnTsih_Type(Unsigned32):
    """Custom type cIscsiSsnTsih based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiSsnTsih_Type.__name__ = "Unsigned32"
_CIscsiSsnTsih_Object = MibTableColumn
cIscsiSsnTsih = _CIscsiSsnTsih_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 5),
    _CIscsiSsnTsih_Type()
)
cIscsiSsnTsih.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnTsih.setStatus("current")


class _CIscsiSsnIsid_Type(OctetString):
    """Custom type cIscsiSsnIsid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CIscsiSsnIsid_Type.__name__ = "OctetString"
_CIscsiSsnIsid_Object = MibTableColumn
cIscsiSsnIsid = _CIscsiSsnIsid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 6),
    _CIscsiSsnIsid_Type()
)
cIscsiSsnIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnIsid.setStatus("current")
_CIscsiSsnInitiatorAlias_Type = SnmpAdminString
_CIscsiSsnInitiatorAlias_Object = MibTableColumn
cIscsiSsnInitiatorAlias = _CIscsiSsnInitiatorAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 7),
    _CIscsiSsnInitiatorAlias_Type()
)
cIscsiSsnInitiatorAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnInitiatorAlias.setStatus("current")
_CIscsiSsnTargetAlias_Type = SnmpAdminString
_CIscsiSsnTargetAlias_Object = MibTableColumn
cIscsiSsnTargetAlias = _CIscsiSsnTargetAlias_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 8),
    _CIscsiSsnTargetAlias_Type()
)
cIscsiSsnTargetAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnTargetAlias.setStatus("current")
_CIscsiSsnInitialR2T_Type = TruthValue
_CIscsiSsnInitialR2T_Object = MibTableColumn
cIscsiSsnInitialR2T = _CIscsiSsnInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 9),
    _CIscsiSsnInitialR2T_Type()
)
cIscsiSsnInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnInitialR2T.setStatus("current")
_CIscsiSsnBidiInitialR2T_Type = TruthValue
_CIscsiSsnBidiInitialR2T_Object = MibTableColumn
cIscsiSsnBidiInitialR2T = _CIscsiSsnBidiInitialR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 10),
    _CIscsiSsnBidiInitialR2T_Type()
)
cIscsiSsnBidiInitialR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnBidiInitialR2T.setStatus("current")
_CIscsiSsnImmediateData_Type = TruthValue
_CIscsiSsnImmediateData_Object = MibTableColumn
cIscsiSsnImmediateData = _CIscsiSsnImmediateData_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 11),
    _CIscsiSsnImmediateData_Type()
)
cIscsiSsnImmediateData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnImmediateData.setStatus("current")


class _CIscsiSsnType_Type(Integer32):
    """Custom type cIscsiSsnType based on Integer32"""
    defaultValue = 1

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


_CIscsiSsnType_Type.__name__ = "Integer32"
_CIscsiSsnType_Object = MibTableColumn
cIscsiSsnType = _CIscsiSsnType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 12),
    _CIscsiSsnType_Type()
)
cIscsiSsnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnType.setStatus("current")


class _CIscsiSsnMaxOutstandingR2T_Type(Unsigned32):
    """Custom type cIscsiSsnMaxOutstandingR2T based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiSsnMaxOutstandingR2T_Type.__name__ = "Unsigned32"
_CIscsiSsnMaxOutstandingR2T_Object = MibTableColumn
cIscsiSsnMaxOutstandingR2T = _CIscsiSsnMaxOutstandingR2T_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 13),
    _CIscsiSsnMaxOutstandingR2T_Type()
)
cIscsiSsnMaxOutstandingR2T.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnMaxOutstandingR2T.setStatus("current")


class _CIscsiSsnFirstBurstSize_Type(Unsigned32):
    """Custom type cIscsiSsnFirstBurstSize based on Unsigned32"""
    defaultValue = 65536

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiSsnFirstBurstSize_Type.__name__ = "Unsigned32"
_CIscsiSsnFirstBurstSize_Object = MibTableColumn
cIscsiSsnFirstBurstSize = _CIscsiSsnFirstBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 14),
    _CIscsiSsnFirstBurstSize_Type()
)
cIscsiSsnFirstBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnFirstBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnFirstBurstSize.setUnits("bytes")


class _CIscsiSsnMaxBurstSize_Type(Unsigned32):
    """Custom type cIscsiSsnMaxBurstSize based on Unsigned32"""
    defaultValue = 262144

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiSsnMaxBurstSize_Type.__name__ = "Unsigned32"
_CIscsiSsnMaxBurstSize_Object = MibTableColumn
cIscsiSsnMaxBurstSize = _CIscsiSsnMaxBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 15),
    _CIscsiSsnMaxBurstSize_Type()
)
cIscsiSsnMaxBurstSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnMaxBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnMaxBurstSize.setUnits("bytes")


class _CIscsiSsnConnectionNumber_Type(Gauge32):
    """Custom type cIscsiSsnConnectionNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiSsnConnectionNumber_Type.__name__ = "Gauge32"
_CIscsiSsnConnectionNumber_Object = MibTableColumn
cIscsiSsnConnectionNumber = _CIscsiSsnConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 16),
    _CIscsiSsnConnectionNumber_Type()
)
cIscsiSsnConnectionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnConnectionNumber.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnConnectionNumber.setUnits("connections")
_CIscsiSsnAuthIdentity_Type = RowPointer
_CIscsiSsnAuthIdentity_Object = MibTableColumn
cIscsiSsnAuthIdentity = _CIscsiSsnAuthIdentity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 17),
    _CIscsiSsnAuthIdentity_Type()
)
cIscsiSsnAuthIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnAuthIdentity.setStatus("current")
_CIscsiSsnDataSequenceInOrder_Type = TruthValue
_CIscsiSsnDataSequenceInOrder_Object = MibTableColumn
cIscsiSsnDataSequenceInOrder = _CIscsiSsnDataSequenceInOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 18),
    _CIscsiSsnDataSequenceInOrder_Type()
)
cIscsiSsnDataSequenceInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnDataSequenceInOrder.setStatus("current")
_CIscsiSsnDataPduInOrder_Type = TruthValue
_CIscsiSsnDataPduInOrder_Object = MibTableColumn
cIscsiSsnDataPduInOrder = _CIscsiSsnDataPduInOrder_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 19),
    _CIscsiSsnDataPduInOrder_Type()
)
cIscsiSsnDataPduInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnDataPduInOrder.setStatus("current")


class _CIscsiSsnErrorRecoveryLevel_Type(Unsigned32):
    """Custom type cIscsiSsnErrorRecoveryLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CIscsiSsnErrorRecoveryLevel_Type.__name__ = "Unsigned32"
_CIscsiSsnErrorRecoveryLevel_Object = MibTableColumn
cIscsiSsnErrorRecoveryLevel = _CIscsiSsnErrorRecoveryLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 1, 1, 20),
    _CIscsiSsnErrorRecoveryLevel_Type()
)
cIscsiSsnErrorRecoveryLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnErrorRecoveryLevel.setStatus("current")
_CIscsiSessionStatsTable_Object = MibTable
cIscsiSessionStatsTable = _CIscsiSessionStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2)
)
if mibBuilder.loadTexts:
    cIscsiSessionStatsTable.setStatus("current")
_CIscsiSessionStatsEntry_Object = MibTableRow
cIscsiSessionStatsEntry = _CIscsiSessionStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiSessionStatsEntry.setStatus("current")
_CIscsiSsnCmdPdus_Type = Counter32
_CIscsiSsnCmdPdus_Object = MibTableColumn
cIscsiSsnCmdPdus = _CIscsiSsnCmdPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2, 1, 1),
    _CIscsiSsnCmdPdus_Type()
)
cIscsiSsnCmdPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnCmdPdus.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnCmdPdus.setUnits("PDUs")
_CIscsiSsnRspPdus_Type = Counter32
_CIscsiSsnRspPdus_Object = MibTableColumn
cIscsiSsnRspPdus = _CIscsiSsnRspPdus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2, 1, 2),
    _CIscsiSsnRspPdus_Type()
)
cIscsiSsnRspPdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnRspPdus.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnRspPdus.setUnits("PDUs")
_CIscsiSsnTxDataOctets_Type = Counter64
_CIscsiSsnTxDataOctets_Object = MibTableColumn
cIscsiSsnTxDataOctets = _CIscsiSsnTxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2, 1, 3),
    _CIscsiSsnTxDataOctets_Type()
)
cIscsiSsnTxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnTxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnTxDataOctets.setUnits("octets")
_CIscsiSsnRxDataOctets_Type = Counter64
_CIscsiSsnRxDataOctets_Object = MibTableColumn
cIscsiSsnRxDataOctets = _CIscsiSsnRxDataOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 2, 1, 4),
    _CIscsiSsnRxDataOctets_Type()
)
cIscsiSsnRxDataOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnRxDataOctets.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnRxDataOctets.setUnits("octets")
_CIscsiSessionCxnErrorStatsTable_Object = MibTable
cIscsiSessionCxnErrorStatsTable = _CIscsiSessionCxnErrorStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 3)
)
if mibBuilder.loadTexts:
    cIscsiSessionCxnErrorStatsTable.setStatus("current")
_CIscsiSessionCxnErrorStatsEntry_Object = MibTableRow
cIscsiSessionCxnErrorStatsEntry = _CIscsiSessionCxnErrorStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 3, 1)
)
if mibBuilder.loadTexts:
    cIscsiSessionCxnErrorStatsEntry.setStatus("current")
_CIscsiSsnDigestErrors_Type = Counter32
_CIscsiSsnDigestErrors_Object = MibTableColumn
cIscsiSsnDigestErrors = _CIscsiSsnDigestErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 3, 1, 1),
    _CIscsiSsnDigestErrors_Type()
)
cIscsiSsnDigestErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnDigestErrors.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnDigestErrors.setUnits("PDUs")
_CIscsiSsnCxnTimeoutErrors_Type = Counter32
_CIscsiSsnCxnTimeoutErrors_Object = MibTableColumn
cIscsiSsnCxnTimeoutErrors = _CIscsiSsnCxnTimeoutErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 11, 3, 1, 2),
    _CIscsiSsnCxnTimeoutErrors_Type()
)
cIscsiSsnCxnTimeoutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiSsnCxnTimeoutErrors.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiSsnCxnTimeoutErrors.setUnits("sequences")
_CIscsiConnection_ObjectIdentity = ObjectIdentity
cIscsiConnection = _CIscsiConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12)
)
_CIscsiConnectionAttributesTable_Object = MibTable
cIscsiConnectionAttributesTable = _CIscsiConnectionAttributesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cIscsiConnectionAttributesTable.setStatus("current")
_CIscsiConnectionAttributesEntry_Object = MibTableRow
cIscsiConnectionAttributesEntry = _CIscsiConnectionAttributesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1)
)
cIscsiConnectionAttributesEntry.setIndexNames(
    (0, "CISCO-ISCSI-MIB", "cIscsiInstIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiNodeIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiSsnIndex"),
    (0, "CISCO-ISCSI-MIB", "cIscsiCxnIndex"),
)
if mibBuilder.loadTexts:
    cIscsiConnectionAttributesEntry.setStatus("current")


class _CIscsiCxnIndex_Type(Unsigned32):
    """Custom type cIscsiCxnIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CIscsiCxnIndex_Type.__name__ = "Unsigned32"
_CIscsiCxnIndex_Object = MibTableColumn
cIscsiCxnIndex = _CIscsiCxnIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 1),
    _CIscsiCxnIndex_Type()
)
cIscsiCxnIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cIscsiCxnIndex.setStatus("current")


class _CIscsiCxnCid_Type(Unsigned32):
    """Custom type cIscsiCxnCid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CIscsiCxnCid_Type.__name__ = "Unsigned32"
_CIscsiCxnCid_Object = MibTableColumn
cIscsiCxnCid = _CIscsiCxnCid_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 2),
    _CIscsiCxnCid_Type()
)
cIscsiCxnCid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnCid.setStatus("current")


class _CIscsiCxnState_Type(Integer32):
    """Custom type cIscsiCxnState based on Integer32"""
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


_CIscsiCxnState_Type.__name__ = "Integer32"
_CIscsiCxnState_Object = MibTableColumn
cIscsiCxnState = _CIscsiCxnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 3),
    _CIscsiCxnState_Type()
)
cIscsiCxnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnState.setStatus("current")
_CIscsiCxnLocalAddrType_Type = InetAddressType
_CIscsiCxnLocalAddrType_Object = MibTableColumn
cIscsiCxnLocalAddrType = _CIscsiCxnLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 4),
    _CIscsiCxnLocalAddrType_Type()
)
cIscsiCxnLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnLocalAddrType.setStatus("current")
_CIscsiCxnLocalAddr_Type = InetAddress
_CIscsiCxnLocalAddr_Object = MibTableColumn
cIscsiCxnLocalAddr = _CIscsiCxnLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 5),
    _CIscsiCxnLocalAddr_Type()
)
cIscsiCxnLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnLocalAddr.setStatus("current")


class _CIscsiCxnProtocol_Type(CIscsiTransportProtocols):
    """Custom type cIscsiCxnProtocol based on CIscsiTransportProtocols"""
    defaultValue = 6


_CIscsiCxnProtocol_Object = MibTableColumn
cIscsiCxnProtocol = _CIscsiCxnProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 6),
    _CIscsiCxnProtocol_Type()
)
cIscsiCxnProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnProtocol.setStatus("current")
_CIscsiCxnLocalPort_Type = Unsigned32
_CIscsiCxnLocalPort_Object = MibTableColumn
cIscsiCxnLocalPort = _CIscsiCxnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 7),
    _CIscsiCxnLocalPort_Type()
)
cIscsiCxnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnLocalPort.setStatus("current")
_CIscsiCxnRemoteAddrType_Type = InetAddressType
_CIscsiCxnRemoteAddrType_Object = MibTableColumn
cIscsiCxnRemoteAddrType = _CIscsiCxnRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 8),
    _CIscsiCxnRemoteAddrType_Type()
)
cIscsiCxnRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnRemoteAddrType.setStatus("current")
_CIscsiCxnRemoteAddr_Type = InetAddress
_CIscsiCxnRemoteAddr_Object = MibTableColumn
cIscsiCxnRemoteAddr = _CIscsiCxnRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 9),
    _CIscsiCxnRemoteAddr_Type()
)
cIscsiCxnRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnRemoteAddr.setStatus("current")
_CIscsiCxnRemotePort_Type = Unsigned32
_CIscsiCxnRemotePort_Object = MibTableColumn
cIscsiCxnRemotePort = _CIscsiCxnRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 10),
    _CIscsiCxnRemotePort_Type()
)
cIscsiCxnRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnRemotePort.setStatus("current")


class _CIscsiCxnMaxRecvDataSegLength_Type(Unsigned32):
    """Custom type cIscsiCxnMaxRecvDataSegLength based on Unsigned32"""
    defaultValue = 8192

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 16777215),
    )


_CIscsiCxnMaxRecvDataSegLength_Type.__name__ = "Unsigned32"
_CIscsiCxnMaxRecvDataSegLength_Object = MibTableColumn
cIscsiCxnMaxRecvDataSegLength = _CIscsiCxnMaxRecvDataSegLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 11),
    _CIscsiCxnMaxRecvDataSegLength_Type()
)
cIscsiCxnMaxRecvDataSegLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnMaxRecvDataSegLength.setStatus("current")
if mibBuilder.loadTexts:
    cIscsiCxnMaxRecvDataSegLength.setUnits("bytes")
_CIscsiCxnHeaderIntegrity_Type = CIscsiDigestMethod
_CIscsiCxnHeaderIntegrity_Object = MibTableColumn
cIscsiCxnHeaderIntegrity = _CIscsiCxnHeaderIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 12),
    _CIscsiCxnHeaderIntegrity_Type()
)
cIscsiCxnHeaderIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnHeaderIntegrity.setStatus("current")
_CIscsiCxnDataIntegrity_Type = CIscsiDigestMethod
_CIscsiCxnDataIntegrity_Object = MibTableColumn
cIscsiCxnDataIntegrity = _CIscsiCxnDataIntegrity_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 13),
    _CIscsiCxnDataIntegrity_Type()
)
cIscsiCxnDataIntegrity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnDataIntegrity.setStatus("current")
_CIscsiCxnRecvMarker_Type = TruthValue
_CIscsiCxnRecvMarker_Object = MibTableColumn
cIscsiCxnRecvMarker = _CIscsiCxnRecvMarker_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 14),
    _CIscsiCxnRecvMarker_Type()
)
cIscsiCxnRecvMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnRecvMarker.setStatus("current")
_CIscsiCxnSendMarker_Type = TruthValue
_CIscsiCxnSendMarker_Object = MibTableColumn
cIscsiCxnSendMarker = _CIscsiCxnSendMarker_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 1, 12, 1, 1, 15),
    _CIscsiCxnSendMarker_Type()
)
cIscsiCxnSendMarker.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cIscsiCxnSendMarker.setStatus("current")
_CIscsiNotifications_ObjectIdentity = ObjectIdentity
cIscsiNotifications = _CIscsiNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 2)
)
_CIscsiNotificationsPrefix_ObjectIdentity = ObjectIdentity
cIscsiNotificationsPrefix = _CIscsiNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 2, 0)
)
_CIscsiConformance_ObjectIdentity = ObjectIdentity
cIscsiConformance = _CIscsiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3)
)
_CIscsiGroups_ObjectIdentity = ObjectIdentity
cIscsiGroups = _CIscsiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1)
)
_CIscsiCompliances_ObjectIdentity = ObjectIdentity
cIscsiCompliances = _CIscsiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 2)
)
cIscsiInstanceAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiInstanceSsnErrorStatsEntry")
)
cIscsiInstanceSsnErrorStatsEntry.setIndexNames(*cIscsiInstanceAttributesEntry.getIndexNames())
cIscsiTargetAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiTargetLoginStatsEntry")
)
cIscsiTargetLoginStatsEntry.setIndexNames(*cIscsiTargetAttributesEntry.getIndexNames())
cIscsiTargetAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiTargetLogoutStatsEntry")
)
cIscsiTargetLogoutStatsEntry.setIndexNames(*cIscsiTargetAttributesEntry.getIndexNames())
cIscsiInitiatorAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiInitiatorLoginStatsEntry")
)
cIscsiInitiatorLoginStatsEntry.setIndexNames(*cIscsiInitiatorAttributesEntry.getIndexNames())
cIscsiInitiatorAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiInitiatorLogoutStatsEntry")
)
cIscsiInitiatorLogoutStatsEntry.setIndexNames(*cIscsiInitiatorAttributesEntry.getIndexNames())
cIscsiSessionAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiSessionStatsEntry")
)
cIscsiSessionStatsEntry.setIndexNames(*cIscsiSessionAttributesEntry.getIndexNames())
cIscsiSessionAttributesEntry.registerAugmentions(
    ("CISCO-ISCSI-MIB",
     "cIscsiSessionCxnErrorStatsEntry")
)
cIscsiSessionCxnErrorStatsEntry.setIndexNames(*cIscsiSessionAttributesEntry.getIndexNames())

# Managed Objects groups

cIscsiInstanceAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 1)
)
cIscsiInstanceAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiInstDescr"),
        ("CISCO-ISCSI-MIB", "cIscsiInstVersionMin"),
        ("CISCO-ISCSI-MIB", "cIscsiInstVersionMax"),
        ("CISCO-ISCSI-MIB", "cIscsiInstVendorID"),
        ("CISCO-ISCSI-MIB", "cIscsiInstVendorVersion"),
        ("CISCO-ISCSI-MIB", "cIscsiInstPortalNumber"),
        ("CISCO-ISCSI-MIB", "cIscsiInstNodeNumber"),
        ("CISCO-ISCSI-MIB", "cIscsiInstSessionNumber"),
        ("CISCO-ISCSI-MIB", "cIscsiInstSsnFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiInstLastSsnFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiInstLastSsnRmtNodeName"))
)
if mibBuilder.loadTexts:
    cIscsiInstanceAttributesGroup.setStatus("current")

cIscsiInstanceSsnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 2)
)
cIscsiInstanceSsnErrorStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiInstSsnDigestErrors"),
        ("CISCO-ISCSI-MIB", "cIscsiInstSsnCxnTimeoutErrors"),
        ("CISCO-ISCSI-MIB", "cIscsiInstSsnFormatErrors"))
)
if mibBuilder.loadTexts:
    cIscsiInstanceSsnErrorStatsGroup.setStatus("current")

cIscsiPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 3)
)
cIscsiPortalAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiPortalRowStatus"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalRoles"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalAddr"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalProtocol"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalMaxRecvDataSegLength"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalPrimaryHdrDigest"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalPrimaryDataDigest"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalSecondaryHdrDigest"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalSecondaryDataDigest"),
        ("CISCO-ISCSI-MIB", "cIscsiPortalRecvMarker"))
)
if mibBuilder.loadTexts:
    cIscsiPortalAttributesGroup.setStatus("current")

cIscsiTgtPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 4)
)
cIscsiTgtPortalAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtPortalPort"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtPortalTag"))
)
if mibBuilder.loadTexts:
    cIscsiTgtPortalAttributesGroup.setStatus("current")

cIscsiIntrPortalAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 5)
)
cIscsiIntrPortalAttributesGroup.setObjects(
    ("CISCO-ISCSI-MIB", "cIscsiIntrPortalTag")
)
if mibBuilder.loadTexts:
    cIscsiIntrPortalAttributesGroup.setStatus("current")

cIscsiNodeAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 6)
)
cIscsiNodeAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiNodeName"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeAlias"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeRoles"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeTransportType"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeInitialR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeBidiInitialR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeImmediateData"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeMaxOutstandingR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeFirstBurstSize"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeMaxBurstSize"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeMaxConnections"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeDataSequenceInOrder"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeDataPduInOrder"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeDefaultTime2Wait"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeDefaultTime2Retain"),
        ("CISCO-ISCSI-MIB", "cIscsiNodeErrorRecoveryLevel"))
)
if mibBuilder.loadTexts:
    cIscsiNodeAttributesGroup.setStatus("current")

cIscsiTargetAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 7)
)
cIscsiTargetAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtLoginFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastFailureTime"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureName"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureAddr"))
)
if mibBuilder.loadTexts:
    cIscsiTargetAttributesGroup.setStatus("current")

cIscsiTargetLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 8)
)
cIscsiTargetLoginStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtLoginAccepts"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLoginOtherFails"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLoginRedirects"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLoginAuthorizeFails"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLoginAuthenticateFails"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLoginNegotiateFails"))
)
if mibBuilder.loadTexts:
    cIscsiTargetLoginStatsGroup.setStatus("current")

cIscsiTargetLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 9)
)
cIscsiTargetLogoutStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtLogoutNormals"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLogoutOthers"))
)
if mibBuilder.loadTexts:
    cIscsiTargetLogoutStatsGroup.setStatus("current")

cIscsiTargetAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 10)
)
cIscsiTargetAuthGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtAuthRowStatus"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtAuthIdentity"))
)
if mibBuilder.loadTexts:
    cIscsiTargetAuthGroup.setStatus("current")

cIscsiInitiatorAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 11)
)
cIscsiInitiatorAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiIntrLoginFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastFailureTime"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureName"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureAddr"))
)
if mibBuilder.loadTexts:
    cIscsiInitiatorAttributesGroup.setStatus("current")

cIscsiInitiatorLoginStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 12)
)
cIscsiInitiatorLoginStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiIntrLoginAcceptRsps"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLoginOtherFailRsps"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLoginRedirectRsps"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLoginAuthFailRsps"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLoginAuthenticateFails"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLoginNegotiateFails"))
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLoginStatsGroup.setStatus("current")

cIscsiInitiatorLogoutStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 13)
)
cIscsiInitiatorLogoutStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiIntrLogoutNormals"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLogoutOthers"))
)
if mibBuilder.loadTexts:
    cIscsiInitiatorLogoutStatsGroup.setStatus("current")

cIscsiInitiatorAuthGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 14)
)
cIscsiInitiatorAuthGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiIntrAuthRowStatus"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrAuthIdentity"))
)
if mibBuilder.loadTexts:
    cIscsiInitiatorAuthGroup.setStatus("current")

cIscsiSessionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 15)
)
cIscsiSessionAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiSsnDirection"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnInitiatorName"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnTargetName"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnTsih"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnIsid"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnInitiatorAlias"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnTargetAlias"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnInitialR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnBidiInitialR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnImmediateData"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnType"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnMaxOutstandingR2T"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnFirstBurstSize"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnMaxBurstSize"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnConnectionNumber"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnAuthIdentity"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnDataSequenceInOrder"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnDataPduInOrder"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnErrorRecoveryLevel"))
)
if mibBuilder.loadTexts:
    cIscsiSessionAttributesGroup.setStatus("current")

cIscsiSessionStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 16)
)
cIscsiSessionStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiSsnCmdPdus"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnRspPdus"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnTxDataOctets"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnRxDataOctets"))
)
if mibBuilder.loadTexts:
    cIscsiSessionStatsGroup.setStatus("current")

cIscsiSessionCxnErrorStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 17)
)
cIscsiSessionCxnErrorStatsGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiSsnDigestErrors"),
        ("CISCO-ISCSI-MIB", "cIscsiSsnCxnTimeoutErrors"))
)
if mibBuilder.loadTexts:
    cIscsiSessionCxnErrorStatsGroup.setStatus("current")

cIscsiConnectionAttributesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 18)
)
cIscsiConnectionAttributesGroup.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiCxnCid"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnState"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnProtocol"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnLocalAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnLocalAddr"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnLocalPort"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnRemoteAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnRemoteAddr"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnRemotePort"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnMaxRecvDataSegLength"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnHeaderIntegrity"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnDataIntegrity"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnRecvMarker"),
        ("CISCO-ISCSI-MIB", "cIscsiCxnSendMarker"))
)
if mibBuilder.loadTexts:
    cIscsiConnectionAttributesGroup.setStatus("current")


# Notification objects

cIscsiTgtLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 2, 0, 1)
)
cIscsiTgtLoginFailure.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiTgtLoginFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureName"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiTgtLastIntrFailureAddr"))
)
if mibBuilder.loadTexts:
    cIscsiTgtLoginFailure.setStatus(
        "current"
    )

cIscsiIntrLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 2, 0, 2)
)
cIscsiIntrLoginFailure.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiIntrLoginFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureName"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureAddrType"),
        ("CISCO-ISCSI-MIB", "cIscsiIntrLastTgtFailureAddr"))
)
if mibBuilder.loadTexts:
    cIscsiIntrLoginFailure.setStatus(
        "current"
    )

cIscsiInstSessionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 2, 0, 3)
)
cIscsiInstSessionFailure.setObjects(
      *(("CISCO-ISCSI-MIB", "cIscsiInstSsnFailures"),
        ("CISCO-ISCSI-MIB", "cIscsiInstLastSsnFailureType"),
        ("CISCO-ISCSI-MIB", "cIscsiInstLastSsnRmtNodeName"))
)
if mibBuilder.loadTexts:
    cIscsiInstSessionFailure.setStatus(
        "current"
    )


# Notifications groups

cIscsiTgtLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 19)
)
cIscsiTgtLgnNotificationsGroup.setObjects(
    ("CISCO-ISCSI-MIB", "cIscsiTgtLoginFailure")
)
if mibBuilder.loadTexts:
    cIscsiTgtLgnNotificationsGroup.setStatus(
        "current"
    )

cIscsiIntrLgnNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 20)
)
cIscsiIntrLgnNotificationsGroup.setObjects(
    ("CISCO-ISCSI-MIB", "cIscsiIntrLoginFailure")
)
if mibBuilder.loadTexts:
    cIscsiIntrLgnNotificationsGroup.setStatus(
        "current"
    )

cIscsiSsnFlrNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 1, 21)
)
cIscsiSsnFlrNotificationsGroup.setObjects(
    ("CISCO-ISCSI-MIB", "cIscsiInstSessionFailure")
)
if mibBuilder.loadTexts:
    cIscsiSsnFlrNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cIscsiComplianceV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 94, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cIscsiComplianceV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ISCSI-MIB",
    **{"CIscsiTransportProtocols": CIscsiTransportProtocols,
       "CIscsiDigestMethod": CIscsiDigestMethod,
       "ciscoIscsiModule": ciscoIscsiModule,
       "cIscsiObjects": cIscsiObjects,
       "cIscsiDescriptors": cIscsiDescriptors,
       "cIscsiHeaderIntegrityTypes": cIscsiHeaderIntegrityTypes,
       "cIscsiHdrIntegrityNone": cIscsiHdrIntegrityNone,
       "cIscsiHdrIntegrityCrc32c": cIscsiHdrIntegrityCrc32c,
       "cIscsiDataIntegrityTypes": cIscsiDataIntegrityTypes,
       "cIscsiDataIntegrityNone": cIscsiDataIntegrityNone,
       "cIscsiDataIntegrityCrc32c": cIscsiDataIntegrityCrc32c,
       "cIscsiInstance": cIscsiInstance,
       "cIscsiInstanceAttributesTable": cIscsiInstanceAttributesTable,
       "cIscsiInstanceAttributesEntry": cIscsiInstanceAttributesEntry,
       "cIscsiInstIndex": cIscsiInstIndex,
       "cIscsiInstDescr": cIscsiInstDescr,
       "cIscsiInstVersionMin": cIscsiInstVersionMin,
       "cIscsiInstVersionMax": cIscsiInstVersionMax,
       "cIscsiInstVendorID": cIscsiInstVendorID,
       "cIscsiInstVendorVersion": cIscsiInstVendorVersion,
       "cIscsiInstPortalNumber": cIscsiInstPortalNumber,
       "cIscsiInstNodeNumber": cIscsiInstNodeNumber,
       "cIscsiInstSessionNumber": cIscsiInstSessionNumber,
       "cIscsiInstSsnFailures": cIscsiInstSsnFailures,
       "cIscsiInstLastSsnFailureType": cIscsiInstLastSsnFailureType,
       "cIscsiInstLastSsnRmtNodeName": cIscsiInstLastSsnRmtNodeName,
       "cIscsiInstanceSsnErrorStatsTable": cIscsiInstanceSsnErrorStatsTable,
       "cIscsiInstanceSsnErrorStatsEntry": cIscsiInstanceSsnErrorStatsEntry,
       "cIscsiInstSsnDigestErrors": cIscsiInstSsnDigestErrors,
       "cIscsiInstSsnCxnTimeoutErrors": cIscsiInstSsnCxnTimeoutErrors,
       "cIscsiInstSsnFormatErrors": cIscsiInstSsnFormatErrors,
       "cIscsiPortal": cIscsiPortal,
       "cIscsiPortalAttributesTable": cIscsiPortalAttributesTable,
       "cIscsiPortalAttributesEntry": cIscsiPortalAttributesEntry,
       "cIscsiPortalIndex": cIscsiPortalIndex,
       "cIscsiPortalRowStatus": cIscsiPortalRowStatus,
       "cIscsiPortalRoles": cIscsiPortalRoles,
       "cIscsiPortalAddrType": cIscsiPortalAddrType,
       "cIscsiPortalAddr": cIscsiPortalAddr,
       "cIscsiPortalProtocol": cIscsiPortalProtocol,
       "cIscsiPortalMaxRecvDataSegLength": cIscsiPortalMaxRecvDataSegLength,
       "cIscsiPortalPrimaryHdrDigest": cIscsiPortalPrimaryHdrDigest,
       "cIscsiPortalPrimaryDataDigest": cIscsiPortalPrimaryDataDigest,
       "cIscsiPortalSecondaryHdrDigest": cIscsiPortalSecondaryHdrDigest,
       "cIscsiPortalSecondaryDataDigest": cIscsiPortalSecondaryDataDigest,
       "cIscsiPortalRecvMarker": cIscsiPortalRecvMarker,
       "cIscsiTargetPortal": cIscsiTargetPortal,
       "cIscsiTgtPortalAttributesTable": cIscsiTgtPortalAttributesTable,
       "cIscsiTgtPortalAttributesEntry": cIscsiTgtPortalAttributesEntry,
       "cIscsiTgtPortalPort": cIscsiTgtPortalPort,
       "cIscsiTgtPortalTag": cIscsiTgtPortalTag,
       "cIscsiInitiatorPortal": cIscsiInitiatorPortal,
       "cIscsiIntrPortalAttributesTable": cIscsiIntrPortalAttributesTable,
       "cIscsiIntrPortalAttributesEntry": cIscsiIntrPortalAttributesEntry,
       "cIscsiIntrPortalTag": cIscsiIntrPortalTag,
       "cIscsiNode": cIscsiNode,
       "cIscsiNodeAttributesTable": cIscsiNodeAttributesTable,
       "cIscsiNodeAttributesEntry": cIscsiNodeAttributesEntry,
       "cIscsiNodeIndex": cIscsiNodeIndex,
       "cIscsiNodeName": cIscsiNodeName,
       "cIscsiNodeAlias": cIscsiNodeAlias,
       "cIscsiNodeRoles": cIscsiNodeRoles,
       "cIscsiNodeTransportType": cIscsiNodeTransportType,
       "cIscsiNodeInitialR2T": cIscsiNodeInitialR2T,
       "cIscsiNodeBidiInitialR2T": cIscsiNodeBidiInitialR2T,
       "cIscsiNodeImmediateData": cIscsiNodeImmediateData,
       "cIscsiNodeMaxOutstandingR2T": cIscsiNodeMaxOutstandingR2T,
       "cIscsiNodeFirstBurstSize": cIscsiNodeFirstBurstSize,
       "cIscsiNodeMaxBurstSize": cIscsiNodeMaxBurstSize,
       "cIscsiNodeMaxConnections": cIscsiNodeMaxConnections,
       "cIscsiNodeDataSequenceInOrder": cIscsiNodeDataSequenceInOrder,
       "cIscsiNodeDataPduInOrder": cIscsiNodeDataPduInOrder,
       "cIscsiNodeDefaultTime2Wait": cIscsiNodeDefaultTime2Wait,
       "cIscsiNodeDefaultTime2Retain": cIscsiNodeDefaultTime2Retain,
       "cIscsiNodeErrorRecoveryLevel": cIscsiNodeErrorRecoveryLevel,
       "cIscsiTarget": cIscsiTarget,
       "cIscsiTargetAttributesTable": cIscsiTargetAttributesTable,
       "cIscsiTargetAttributesEntry": cIscsiTargetAttributesEntry,
       "cIscsiTgtLoginFailures": cIscsiTgtLoginFailures,
       "cIscsiTgtLastFailureTime": cIscsiTgtLastFailureTime,
       "cIscsiTgtLastFailureType": cIscsiTgtLastFailureType,
       "cIscsiTgtLastIntrFailureName": cIscsiTgtLastIntrFailureName,
       "cIscsiTgtLastIntrFailureAddrType": cIscsiTgtLastIntrFailureAddrType,
       "cIscsiTgtLastIntrFailureAddr": cIscsiTgtLastIntrFailureAddr,
       "cIscsiTargetLoginStatsTable": cIscsiTargetLoginStatsTable,
       "cIscsiTargetLoginStatsEntry": cIscsiTargetLoginStatsEntry,
       "cIscsiTgtLoginAccepts": cIscsiTgtLoginAccepts,
       "cIscsiTgtLoginOtherFails": cIscsiTgtLoginOtherFails,
       "cIscsiTgtLoginRedirects": cIscsiTgtLoginRedirects,
       "cIscsiTgtLoginAuthorizeFails": cIscsiTgtLoginAuthorizeFails,
       "cIscsiTgtLoginAuthenticateFails": cIscsiTgtLoginAuthenticateFails,
       "cIscsiTgtLoginNegotiateFails": cIscsiTgtLoginNegotiateFails,
       "cIscsiTargetLogoutStatsTable": cIscsiTargetLogoutStatsTable,
       "cIscsiTargetLogoutStatsEntry": cIscsiTargetLogoutStatsEntry,
       "cIscsiTgtLogoutNormals": cIscsiTgtLogoutNormals,
       "cIscsiTgtLogoutOthers": cIscsiTgtLogoutOthers,
       "cIscsiTgtAuthorization": cIscsiTgtAuthorization,
       "cIscsiTgtAuthAttributesTable": cIscsiTgtAuthAttributesTable,
       "cIscsiTgtAuthAttributesEntry": cIscsiTgtAuthAttributesEntry,
       "cIscsiTgtAuthIndex": cIscsiTgtAuthIndex,
       "cIscsiTgtAuthRowStatus": cIscsiTgtAuthRowStatus,
       "cIscsiTgtAuthIdentity": cIscsiTgtAuthIdentity,
       "cIscsiInitiator": cIscsiInitiator,
       "cIscsiInitiatorAttributesTable": cIscsiInitiatorAttributesTable,
       "cIscsiInitiatorAttributesEntry": cIscsiInitiatorAttributesEntry,
       "cIscsiIntrLoginFailures": cIscsiIntrLoginFailures,
       "cIscsiIntrLastFailureTime": cIscsiIntrLastFailureTime,
       "cIscsiIntrLastFailureType": cIscsiIntrLastFailureType,
       "cIscsiIntrLastTgtFailureName": cIscsiIntrLastTgtFailureName,
       "cIscsiIntrLastTgtFailureAddrType": cIscsiIntrLastTgtFailureAddrType,
       "cIscsiIntrLastTgtFailureAddr": cIscsiIntrLastTgtFailureAddr,
       "cIscsiInitiatorLoginStatsTable": cIscsiInitiatorLoginStatsTable,
       "cIscsiInitiatorLoginStatsEntry": cIscsiInitiatorLoginStatsEntry,
       "cIscsiIntrLoginAcceptRsps": cIscsiIntrLoginAcceptRsps,
       "cIscsiIntrLoginOtherFailRsps": cIscsiIntrLoginOtherFailRsps,
       "cIscsiIntrLoginRedirectRsps": cIscsiIntrLoginRedirectRsps,
       "cIscsiIntrLoginAuthFailRsps": cIscsiIntrLoginAuthFailRsps,
       "cIscsiIntrLoginAuthenticateFails": cIscsiIntrLoginAuthenticateFails,
       "cIscsiIntrLoginNegotiateFails": cIscsiIntrLoginNegotiateFails,
       "cIscsiInitiatorLogoutStatsTable": cIscsiInitiatorLogoutStatsTable,
       "cIscsiInitiatorLogoutStatsEntry": cIscsiInitiatorLogoutStatsEntry,
       "cIscsiIntrLogoutNormals": cIscsiIntrLogoutNormals,
       "cIscsiIntrLogoutOthers": cIscsiIntrLogoutOthers,
       "cIscsiIntrAuthorization": cIscsiIntrAuthorization,
       "cIscsiIntrAuthAttributesTable": cIscsiIntrAuthAttributesTable,
       "cIscsiIntrAuthAttributesEntry": cIscsiIntrAuthAttributesEntry,
       "cIscsiIntrAuthIndex": cIscsiIntrAuthIndex,
       "cIscsiIntrAuthRowStatus": cIscsiIntrAuthRowStatus,
       "cIscsiIntrAuthIdentity": cIscsiIntrAuthIdentity,
       "cIscsiSession": cIscsiSession,
       "cIscsiSessionAttributesTable": cIscsiSessionAttributesTable,
       "cIscsiSessionAttributesEntry": cIscsiSessionAttributesEntry,
       "cIscsiSsnIndex": cIscsiSsnIndex,
       "cIscsiSsnDirection": cIscsiSsnDirection,
       "cIscsiSsnInitiatorName": cIscsiSsnInitiatorName,
       "cIscsiSsnTargetName": cIscsiSsnTargetName,
       "cIscsiSsnTsih": cIscsiSsnTsih,
       "cIscsiSsnIsid": cIscsiSsnIsid,
       "cIscsiSsnInitiatorAlias": cIscsiSsnInitiatorAlias,
       "cIscsiSsnTargetAlias": cIscsiSsnTargetAlias,
       "cIscsiSsnInitialR2T": cIscsiSsnInitialR2T,
       "cIscsiSsnBidiInitialR2T": cIscsiSsnBidiInitialR2T,
       "cIscsiSsnImmediateData": cIscsiSsnImmediateData,
       "cIscsiSsnType": cIscsiSsnType,
       "cIscsiSsnMaxOutstandingR2T": cIscsiSsnMaxOutstandingR2T,
       "cIscsiSsnFirstBurstSize": cIscsiSsnFirstBurstSize,
       "cIscsiSsnMaxBurstSize": cIscsiSsnMaxBurstSize,
       "cIscsiSsnConnectionNumber": cIscsiSsnConnectionNumber,
       "cIscsiSsnAuthIdentity": cIscsiSsnAuthIdentity,
       "cIscsiSsnDataSequenceInOrder": cIscsiSsnDataSequenceInOrder,
       "cIscsiSsnDataPduInOrder": cIscsiSsnDataPduInOrder,
       "cIscsiSsnErrorRecoveryLevel": cIscsiSsnErrorRecoveryLevel,
       "cIscsiSessionStatsTable": cIscsiSessionStatsTable,
       "cIscsiSessionStatsEntry": cIscsiSessionStatsEntry,
       "cIscsiSsnCmdPdus": cIscsiSsnCmdPdus,
       "cIscsiSsnRspPdus": cIscsiSsnRspPdus,
       "cIscsiSsnTxDataOctets": cIscsiSsnTxDataOctets,
       "cIscsiSsnRxDataOctets": cIscsiSsnRxDataOctets,
       "cIscsiSessionCxnErrorStatsTable": cIscsiSessionCxnErrorStatsTable,
       "cIscsiSessionCxnErrorStatsEntry": cIscsiSessionCxnErrorStatsEntry,
       "cIscsiSsnDigestErrors": cIscsiSsnDigestErrors,
       "cIscsiSsnCxnTimeoutErrors": cIscsiSsnCxnTimeoutErrors,
       "cIscsiConnection": cIscsiConnection,
       "cIscsiConnectionAttributesTable": cIscsiConnectionAttributesTable,
       "cIscsiConnectionAttributesEntry": cIscsiConnectionAttributesEntry,
       "cIscsiCxnIndex": cIscsiCxnIndex,
       "cIscsiCxnCid": cIscsiCxnCid,
       "cIscsiCxnState": cIscsiCxnState,
       "cIscsiCxnLocalAddrType": cIscsiCxnLocalAddrType,
       "cIscsiCxnLocalAddr": cIscsiCxnLocalAddr,
       "cIscsiCxnProtocol": cIscsiCxnProtocol,
       "cIscsiCxnLocalPort": cIscsiCxnLocalPort,
       "cIscsiCxnRemoteAddrType": cIscsiCxnRemoteAddrType,
       "cIscsiCxnRemoteAddr": cIscsiCxnRemoteAddr,
       "cIscsiCxnRemotePort": cIscsiCxnRemotePort,
       "cIscsiCxnMaxRecvDataSegLength": cIscsiCxnMaxRecvDataSegLength,
       "cIscsiCxnHeaderIntegrity": cIscsiCxnHeaderIntegrity,
       "cIscsiCxnDataIntegrity": cIscsiCxnDataIntegrity,
       "cIscsiCxnRecvMarker": cIscsiCxnRecvMarker,
       "cIscsiCxnSendMarker": cIscsiCxnSendMarker,
       "cIscsiNotifications": cIscsiNotifications,
       "cIscsiNotificationsPrefix": cIscsiNotificationsPrefix,
       "cIscsiTgtLoginFailure": cIscsiTgtLoginFailure,
       "cIscsiIntrLoginFailure": cIscsiIntrLoginFailure,
       "cIscsiInstSessionFailure": cIscsiInstSessionFailure,
       "cIscsiConformance": cIscsiConformance,
       "cIscsiGroups": cIscsiGroups,
       "cIscsiInstanceAttributesGroup": cIscsiInstanceAttributesGroup,
       "cIscsiInstanceSsnErrorStatsGroup": cIscsiInstanceSsnErrorStatsGroup,
       "cIscsiPortalAttributesGroup": cIscsiPortalAttributesGroup,
       "cIscsiTgtPortalAttributesGroup": cIscsiTgtPortalAttributesGroup,
       "cIscsiIntrPortalAttributesGroup": cIscsiIntrPortalAttributesGroup,
       "cIscsiNodeAttributesGroup": cIscsiNodeAttributesGroup,
       "cIscsiTargetAttributesGroup": cIscsiTargetAttributesGroup,
       "cIscsiTargetLoginStatsGroup": cIscsiTargetLoginStatsGroup,
       "cIscsiTargetLogoutStatsGroup": cIscsiTargetLogoutStatsGroup,
       "cIscsiTargetAuthGroup": cIscsiTargetAuthGroup,
       "cIscsiInitiatorAttributesGroup": cIscsiInitiatorAttributesGroup,
       "cIscsiInitiatorLoginStatsGroup": cIscsiInitiatorLoginStatsGroup,
       "cIscsiInitiatorLogoutStatsGroup": cIscsiInitiatorLogoutStatsGroup,
       "cIscsiInitiatorAuthGroup": cIscsiInitiatorAuthGroup,
       "cIscsiSessionAttributesGroup": cIscsiSessionAttributesGroup,
       "cIscsiSessionStatsGroup": cIscsiSessionStatsGroup,
       "cIscsiSessionCxnErrorStatsGroup": cIscsiSessionCxnErrorStatsGroup,
       "cIscsiConnectionAttributesGroup": cIscsiConnectionAttributesGroup,
       "cIscsiTgtLgnNotificationsGroup": cIscsiTgtLgnNotificationsGroup,
       "cIscsiIntrLgnNotificationsGroup": cIscsiIntrLgnNotificationsGroup,
       "cIscsiSsnFlrNotificationsGroup": cIscsiSsnFlrNotificationsGroup,
       "cIscsiCompliances": cIscsiCompliances,
       "cIscsiComplianceV1": cIscsiComplianceV1}
)
