# SNMP MIB module (T11-FC-SP-POLICY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/T11-FC-SP-POLICY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:00:36 2024
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

(FcDomainIdOrZero,
 FcNameIdOrZero,
 fcmInstanceIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "FcDomainIdOrZero",
    "FcNameIdOrZero",
    "fcmInstanceIndex")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(T11NsGs4RejectReasonCode,) = mibBuilder.importSymbols(
    "T11-FC-NAME-SERVER-MIB",
    "T11NsGs4RejectReasonCode")

(T11FcSpAlphaNumName,
 T11FcSpAlphaNumNameOrAbsent,
 T11FcSpHashCalculationStatus,
 T11FcSpPolicyHashFormat,
 T11FcSpPolicyHashValue,
 T11FcSpPolicyName,
 T11FcSpPolicyNameType,
 T11FcSpPolicyObjectType) = mibBuilder.importSymbols(
    "T11-FC-SP-TC-MIB",
    "T11FcSpAlphaNumName",
    "T11FcSpAlphaNumNameOrAbsent",
    "T11FcSpHashCalculationStatus",
    "T11FcSpPolicyHashFormat",
    "T11FcSpPolicyHashValue",
    "T11FcSpPolicyName",
    "T11FcSpPolicyNameType",
    "T11FcSpPolicyObjectType")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

t11FcSpPolicyMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 178)
)
t11FcSpPolicyMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_T11FcSpPoMIBNotifications_ObjectIdentity = ObjectIdentity
t11FcSpPoMIBNotifications = _T11FcSpPoMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 0)
)
_T11FcSpPoMIBObjects_ObjectIdentity = ObjectIdentity
t11FcSpPoMIBObjects = _T11FcSpPoMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1)
)
_T11FcSpPoActive_ObjectIdentity = ObjectIdentity
t11FcSpPoActive = _T11FcSpPoActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1, 1)
)
_T11FcSpPoTable_Object = MibTable
t11FcSpPoTable = _T11FcSpPoTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpPoTable.setStatus("current")
_T11FcSpPoEntry_Object = MibTableRow
t11FcSpPoEntry = _T11FcSpPoEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1, 1)
)
t11FcSpPoEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoEntry.setStatus("current")
_T11FcSpPoFabricIndex_Type = T11FabricIndex
_T11FcSpPoFabricIndex_Object = MibTableColumn
t11FcSpPoFabricIndex = _T11FcSpPoFabricIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1, 1, 1),
    _T11FcSpPoFabricIndex_Type()
)
t11FcSpPoFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoFabricIndex.setStatus("current")
_T11FcSpPoPolicySummaryObjName_Type = T11FcSpAlphaNumName
_T11FcSpPoPolicySummaryObjName_Object = MibTableColumn
t11FcSpPoPolicySummaryObjName = _T11FcSpPoPolicySummaryObjName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1, 1, 2),
    _T11FcSpPoPolicySummaryObjName_Type()
)
t11FcSpPoPolicySummaryObjName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoPolicySummaryObjName.setStatus("current")


class _T11FcSpPoAdminFabricName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoAdminFabricName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoAdminFabricName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoAdminFabricName_Object = MibTableColumn
t11FcSpPoAdminFabricName = _T11FcSpPoAdminFabricName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1, 1, 3),
    _T11FcSpPoAdminFabricName_Type()
)
t11FcSpPoAdminFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoAdminFabricName.setStatus("current")
_T11FcSpPoActivatedTimeStamp_Type = TimeStamp
_T11FcSpPoActivatedTimeStamp_Object = MibTableColumn
t11FcSpPoActivatedTimeStamp = _T11FcSpPoActivatedTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 1, 1, 4),
    _T11FcSpPoActivatedTimeStamp_Type()
)
t11FcSpPoActivatedTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoActivatedTimeStamp.setStatus("current")
_T11FcSpPoSummaryTable_Object = MibTable
t11FcSpPoSummaryTable = _T11FcSpPoSummaryTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2)
)
if mibBuilder.loadTexts:
    t11FcSpPoSummaryTable.setStatus("current")
_T11FcSpPoSummaryEntry_Object = MibTableRow
t11FcSpPoSummaryEntry = _T11FcSpPoSummaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1)
)
t11FcSpPoSummaryEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSummaryPolicyNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSummaryPolicyName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoSummaryEntry.setStatus("current")


class _T11FcSpPoSummaryPolicyNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoSummaryPolicyNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alphaNumericName", 7),
          ("nodeName", 1))
    )


_T11FcSpPoSummaryPolicyNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoSummaryPolicyNameType_Object = MibTableColumn
t11FcSpPoSummaryPolicyNameType = _T11FcSpPoSummaryPolicyNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1, 1),
    _T11FcSpPoSummaryPolicyNameType_Type()
)
t11FcSpPoSummaryPolicyNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSummaryPolicyNameType.setStatus("current")
_T11FcSpPoSummaryPolicyName_Type = T11FcSpPolicyName
_T11FcSpPoSummaryPolicyName_Object = MibTableColumn
t11FcSpPoSummaryPolicyName = _T11FcSpPoSummaryPolicyName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1, 2),
    _T11FcSpPoSummaryPolicyName_Type()
)
t11FcSpPoSummaryPolicyName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSummaryPolicyName.setStatus("current")
_T11FcSpPoSummaryPolicyType_Type = T11FcSpPolicyObjectType
_T11FcSpPoSummaryPolicyType_Object = MibTableColumn
t11FcSpPoSummaryPolicyType = _T11FcSpPoSummaryPolicyType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1, 3),
    _T11FcSpPoSummaryPolicyType_Type()
)
t11FcSpPoSummaryPolicyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSummaryPolicyType.setStatus("current")
_T11FcSpPoSummaryHashFormat_Type = T11FcSpPolicyHashFormat
_T11FcSpPoSummaryHashFormat_Object = MibTableColumn
t11FcSpPoSummaryHashFormat = _T11FcSpPoSummaryHashFormat_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1, 4),
    _T11FcSpPoSummaryHashFormat_Type()
)
t11FcSpPoSummaryHashFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSummaryHashFormat.setStatus("current")
_T11FcSpPoSummaryHashValue_Type = T11FcSpPolicyHashValue
_T11FcSpPoSummaryHashValue_Object = MibTableColumn
t11FcSpPoSummaryHashValue = _T11FcSpPoSummaryHashValue_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 2, 1, 5),
    _T11FcSpPoSummaryHashValue_Type()
)
t11FcSpPoSummaryHashValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSummaryHashValue.setStatus("current")
_T11FcSpPoSwMembTable_Object = MibTable
t11FcSpPoSwMembTable = _T11FcSpPoSwMembTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3)
)
if mibBuilder.loadTexts:
    t11FcSpPoSwMembTable.setStatus("current")
_T11FcSpPoSwMembEntry_Object = MibTableRow
t11FcSpPoSwMembEntry = _T11FcSpPoSwMembEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1)
)
t11FcSpPoSwMembEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembSwitchNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembSwitchName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoSwMembEntry.setStatus("current")


class _T11FcSpPoSwMembSwitchNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoSwMembSwitchNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("restrictedNodeName", 2),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoSwMembSwitchNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoSwMembSwitchNameType_Object = MibTableColumn
t11FcSpPoSwMembSwitchNameType = _T11FcSpPoSwMembSwitchNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 1),
    _T11FcSpPoSwMembSwitchNameType_Type()
)
t11FcSpPoSwMembSwitchNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembSwitchNameType.setStatus("current")


class _T11FcSpPoSwMembSwitchName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoSwMembSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoSwMembSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoSwMembSwitchName_Object = MibTableColumn
t11FcSpPoSwMembSwitchName = _T11FcSpPoSwMembSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 2),
    _T11FcSpPoSwMembSwitchName_Type()
)
t11FcSpPoSwMembSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembSwitchName.setStatus("current")


class _T11FcSpPoSwMembSwitchFlags_Type(Bits):
    """Custom type t11FcSpPoSwMembSwitchFlags based on Bits"""
    namedValues = NamedValues(
        *(("insistentDomainID", 1),
          ("managerRole", 4),
          ("physicalPortsAccess", 3),
          ("serialPortsAccess", 2),
          ("staticDomainID", 0))
    )

_T11FcSpPoSwMembSwitchFlags_Type.__name__ = "Bits"
_T11FcSpPoSwMembSwitchFlags_Object = MibTableColumn
t11FcSpPoSwMembSwitchFlags = _T11FcSpPoSwMembSwitchFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 3),
    _T11FcSpPoSwMembSwitchFlags_Type()
)
t11FcSpPoSwMembSwitchFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembSwitchFlags.setStatus("current")
_T11FcSpPoSwMembDomainID_Type = FcDomainIdOrZero
_T11FcSpPoSwMembDomainID_Object = MibTableColumn
t11FcSpPoSwMembDomainID = _T11FcSpPoSwMembDomainID_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 4),
    _T11FcSpPoSwMembDomainID_Type()
)
t11FcSpPoSwMembDomainID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembDomainID.setStatus("current")


class _T11FcSpPoSwMembPolicyDataRole_Type(Integer32):
    """Custom type t11FcSpPoSwMembPolicyDataRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autonomous", 2),
          ("client", 1),
          ("server", 3))
    )


_T11FcSpPoSwMembPolicyDataRole_Type.__name__ = "Integer32"
_T11FcSpPoSwMembPolicyDataRole_Object = MibTableColumn
t11FcSpPoSwMembPolicyDataRole = _T11FcSpPoSwMembPolicyDataRole_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 5),
    _T11FcSpPoSwMembPolicyDataRole_Type()
)
t11FcSpPoSwMembPolicyDataRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembPolicyDataRole.setStatus("current")


class _T11FcSpPoSwMembAuthBehaviour_Type(Bits):
    """Custom type t11FcSpPoSwMembAuthBehaviour based on Bits"""
    namedValues = NamedValues(
        *(("mustAuthenticate", 0),
          ("rejectIsFailure", 1))
    )

_T11FcSpPoSwMembAuthBehaviour_Type.__name__ = "Bits"
_T11FcSpPoSwMembAuthBehaviour_Object = MibTableColumn
t11FcSpPoSwMembAuthBehaviour = _T11FcSpPoSwMembAuthBehaviour_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 6),
    _T11FcSpPoSwMembAuthBehaviour_Type()
)
t11FcSpPoSwMembAuthBehaviour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembAuthBehaviour.setStatus("current")
_T11FcSpPoSwMembAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoSwMembAttribute_Object = MibTableColumn
t11FcSpPoSwMembAttribute = _T11FcSpPoSwMembAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 3, 1, 7),
    _T11FcSpPoSwMembAttribute_Type()
)
t11FcSpPoSwMembAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwMembAttribute.setStatus("current")
_T11FcSpPoNoMembTable_Object = MibTable
t11FcSpPoNoMembTable = _T11FcSpPoNoMembTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4)
)
if mibBuilder.loadTexts:
    t11FcSpPoNoMembTable.setStatus("current")
_T11FcSpPoNoMembEntry_Object = MibTableRow
t11FcSpPoNoMembEntry = _T11FcSpPoNoMembEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1)
)
t11FcSpPoNoMembEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNoMembNodeNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNoMembNodeName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNoMembEntry.setStatus("current")


class _T11FcSpPoNoMembNodeNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoNoMembNodeNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("portName", 3),
          ("restrictedNodeName", 2),
          ("restrictedPortName", 4),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoNoMembNodeNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoNoMembNodeNameType_Object = MibTableColumn
t11FcSpPoNoMembNodeNameType = _T11FcSpPoNoMembNodeNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1, 1),
    _T11FcSpPoNoMembNodeNameType_Type()
)
t11FcSpPoNoMembNodeNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNoMembNodeNameType.setStatus("current")


class _T11FcSpPoNoMembNodeName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNoMembNodeName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNoMembNodeName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNoMembNodeName_Object = MibTableColumn
t11FcSpPoNoMembNodeName = _T11FcSpPoNoMembNodeName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1, 2),
    _T11FcSpPoNoMembNodeName_Type()
)
t11FcSpPoNoMembNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNoMembNodeName.setStatus("current")


class _T11FcSpPoNoMembFlags_Type(Bits):
    """Custom type t11FcSpPoNoMembFlags based on Bits"""
    namedValues = NamedValues(
        *(("authenticationRequired", 1),
          ("scsiEnclosureAccess", 0))
    )

_T11FcSpPoNoMembFlags_Type.__name__ = "Bits"
_T11FcSpPoNoMembFlags_Object = MibTableColumn
t11FcSpPoNoMembFlags = _T11FcSpPoNoMembFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1, 3),
    _T11FcSpPoNoMembFlags_Type()
)
t11FcSpPoNoMembFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNoMembFlags.setStatus("current")


class _T11FcSpPoNoMembCtAccessIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNoMembCtAccessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoNoMembCtAccessIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNoMembCtAccessIndex_Object = MibTableColumn
t11FcSpPoNoMembCtAccessIndex = _T11FcSpPoNoMembCtAccessIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1, 4),
    _T11FcSpPoNoMembCtAccessIndex_Type()
)
t11FcSpPoNoMembCtAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNoMembCtAccessIndex.setStatus("current")
_T11FcSpPoNoMembAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoNoMembAttribute_Object = MibTableColumn
t11FcSpPoNoMembAttribute = _T11FcSpPoNoMembAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 4, 1, 5),
    _T11FcSpPoNoMembAttribute_Type()
)
t11FcSpPoNoMembAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNoMembAttribute.setStatus("current")
_T11FcSpPoCtDescrTable_Object = MibTable
t11FcSpPoCtDescrTable = _T11FcSpPoCtDescrTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5)
)
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrTable.setStatus("current")
_T11FcSpPoCtDescrEntry_Object = MibTableRow
t11FcSpPoCtDescrEntry = _T11FcSpPoCtDescrEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1)
)
t11FcSpPoCtDescrEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoCtDescrSpecifierIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoCtDescrIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrEntry.setStatus("current")


class _T11FcSpPoCtDescrSpecifierIndex_Type(Unsigned32):
    """Custom type t11FcSpPoCtDescrSpecifierIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoCtDescrSpecifierIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoCtDescrSpecifierIndex_Object = MibTableColumn
t11FcSpPoCtDescrSpecifierIndex = _T11FcSpPoCtDescrSpecifierIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1, 1),
    _T11FcSpPoCtDescrSpecifierIndex_Type()
)
t11FcSpPoCtDescrSpecifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrSpecifierIndex.setStatus("current")


class _T11FcSpPoCtDescrIndex_Type(Unsigned32):
    """Custom type t11FcSpPoCtDescrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoCtDescrIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoCtDescrIndex_Object = MibTableColumn
t11FcSpPoCtDescrIndex = _T11FcSpPoCtDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1, 2),
    _T11FcSpPoCtDescrIndex_Type()
)
t11FcSpPoCtDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrIndex.setStatus("current")


class _T11FcSpPoCtDescrFlags_Type(Bits):
    """Custom type t11FcSpPoCtDescrFlags based on Bits"""
    namedValues = NamedValues(
        *(("allow", 0),
          ("gsSubTypeWildcard", 2),
          ("gsTypeWildcard", 1),
          ("readOnly", 3))
    )

_T11FcSpPoCtDescrFlags_Type.__name__ = "Bits"
_T11FcSpPoCtDescrFlags_Object = MibTableColumn
t11FcSpPoCtDescrFlags = _T11FcSpPoCtDescrFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1, 3),
    _T11FcSpPoCtDescrFlags_Type()
)
t11FcSpPoCtDescrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrFlags.setStatus("current")


class _T11FcSpPoCtDescrGsType_Type(OctetString):
    """Custom type t11FcSpPoCtDescrGsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcSpPoCtDescrGsType_Type.__name__ = "OctetString"
_T11FcSpPoCtDescrGsType_Object = MibTableColumn
t11FcSpPoCtDescrGsType = _T11FcSpPoCtDescrGsType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1, 4),
    _T11FcSpPoCtDescrGsType_Type()
)
t11FcSpPoCtDescrGsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrGsType.setStatus("current")


class _T11FcSpPoCtDescrGsSubType_Type(OctetString):
    """Custom type t11FcSpPoCtDescrGsSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcSpPoCtDescrGsSubType_Type.__name__ = "OctetString"
_T11FcSpPoCtDescrGsSubType_Object = MibTableColumn
t11FcSpPoCtDescrGsSubType = _T11FcSpPoCtDescrGsSubType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 5, 1, 5),
    _T11FcSpPoCtDescrGsSubType_Type()
)
t11FcSpPoCtDescrGsSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoCtDescrGsSubType.setStatus("current")
_T11FcSpPoSwConnTable_Object = MibTable
t11FcSpPoSwConnTable = _T11FcSpPoSwConnTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6)
)
if mibBuilder.loadTexts:
    t11FcSpPoSwConnTable.setStatus("current")
_T11FcSpPoSwConnEntry_Object = MibTableRow
t11FcSpPoSwConnEntry = _T11FcSpPoSwConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1)
)
t11FcSpPoSwConnEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnSwitchName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnAllowedType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnPortNameOrAll"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnAllowedIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoSwConnEntry.setStatus("current")


class _T11FcSpPoSwConnSwitchName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoSwConnSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoSwConnSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoSwConnSwitchName_Object = MibTableColumn
t11FcSpPoSwConnSwitchName = _T11FcSpPoSwConnSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 1),
    _T11FcSpPoSwConnSwitchName_Type()
)
t11FcSpPoSwConnSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnSwitchName.setStatus("current")


class _T11FcSpPoSwConnAllowedType_Type(Integer32):
    """Custom type t11FcSpPoSwConnAllowedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("switch", 1))
    )


_T11FcSpPoSwConnAllowedType_Type.__name__ = "Integer32"
_T11FcSpPoSwConnAllowedType_Object = MibTableColumn
t11FcSpPoSwConnAllowedType = _T11FcSpPoSwConnAllowedType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 2),
    _T11FcSpPoSwConnAllowedType_Type()
)
t11FcSpPoSwConnAllowedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnAllowedType.setStatus("current")


class _T11FcSpPoSwConnPortNameOrAll_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoSwConnPortNameOrAll based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoSwConnPortNameOrAll_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoSwConnPortNameOrAll_Object = MibTableColumn
t11FcSpPoSwConnPortNameOrAll = _T11FcSpPoSwConnPortNameOrAll_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 3),
    _T11FcSpPoSwConnPortNameOrAll_Type()
)
t11FcSpPoSwConnPortNameOrAll.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnPortNameOrAll.setStatus("current")


class _T11FcSpPoSwConnAllowedIndex_Type(Unsigned32):
    """Custom type t11FcSpPoSwConnAllowedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoSwConnAllowedIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoSwConnAllowedIndex_Object = MibTableColumn
t11FcSpPoSwConnAllowedIndex = _T11FcSpPoSwConnAllowedIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 4),
    _T11FcSpPoSwConnAllowedIndex_Type()
)
t11FcSpPoSwConnAllowedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnAllowedIndex.setStatus("current")


class _T11FcSpPoSwConnAllowedNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoSwConnAllowedNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("portName", 3),
          ("restrictedNodeName", 2),
          ("restrictedPortName", 4),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoSwConnAllowedNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoSwConnAllowedNameType_Object = MibTableColumn
t11FcSpPoSwConnAllowedNameType = _T11FcSpPoSwConnAllowedNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 5),
    _T11FcSpPoSwConnAllowedNameType_Type()
)
t11FcSpPoSwConnAllowedNameType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnAllowedNameType.setStatus("current")


class _T11FcSpPoSwConnAllowedName_Type(T11FcSpPolicyName):
    """Custom type t11FcSpPoSwConnAllowedName based on T11FcSpPolicyName"""
    subtypeSpec = T11FcSpPolicyName.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoSwConnAllowedName_Type.__name__ = "T11FcSpPolicyName"
_T11FcSpPoSwConnAllowedName_Object = MibTableColumn
t11FcSpPoSwConnAllowedName = _T11FcSpPoSwConnAllowedName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 6, 1, 6),
    _T11FcSpPoSwConnAllowedName_Type()
)
t11FcSpPoSwConnAllowedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoSwConnAllowedName.setStatus("current")
_T11FcSpPoIpMgmtTable_Object = MibTable
t11FcSpPoIpMgmtTable = _T11FcSpPoIpMgmtTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7)
)
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtTable.setStatus("current")
_T11FcSpPoIpMgmtEntry_Object = MibTableRow
t11FcSpPoIpMgmtEntry = _T11FcSpPoIpMgmtEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1)
)
t11FcSpPoIpMgmtEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoIpMgmtEntryNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoIpMgmtEntryNameLow"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoIpMgmtEntryNameHigh"),
)
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtEntry.setStatus("current")
_T11FcSpPoIpMgmtEntryNameType_Type = InetAddressType
_T11FcSpPoIpMgmtEntryNameType_Object = MibTableColumn
t11FcSpPoIpMgmtEntryNameType = _T11FcSpPoIpMgmtEntryNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1, 1),
    _T11FcSpPoIpMgmtEntryNameType_Type()
)
t11FcSpPoIpMgmtEntryNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtEntryNameType.setStatus("current")


class _T11FcSpPoIpMgmtEntryNameLow_Type(InetAddress):
    """Custom type t11FcSpPoIpMgmtEntryNameLow based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_T11FcSpPoIpMgmtEntryNameLow_Type.__name__ = "InetAddress"
_T11FcSpPoIpMgmtEntryNameLow_Object = MibTableColumn
t11FcSpPoIpMgmtEntryNameLow = _T11FcSpPoIpMgmtEntryNameLow_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1, 2),
    _T11FcSpPoIpMgmtEntryNameLow_Type()
)
t11FcSpPoIpMgmtEntryNameLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtEntryNameLow.setStatus("current")


class _T11FcSpPoIpMgmtEntryNameHigh_Type(InetAddress):
    """Custom type t11FcSpPoIpMgmtEntryNameHigh based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_T11FcSpPoIpMgmtEntryNameHigh_Type.__name__ = "InetAddress"
_T11FcSpPoIpMgmtEntryNameHigh_Object = MibTableColumn
t11FcSpPoIpMgmtEntryNameHigh = _T11FcSpPoIpMgmtEntryNameHigh_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1, 3),
    _T11FcSpPoIpMgmtEntryNameHigh_Type()
)
t11FcSpPoIpMgmtEntryNameHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtEntryNameHigh.setStatus("current")


class _T11FcSpPoIpMgmtWkpIndex_Type(Unsigned32):
    """Custom type t11FcSpPoIpMgmtWkpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoIpMgmtWkpIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoIpMgmtWkpIndex_Object = MibTableColumn
t11FcSpPoIpMgmtWkpIndex = _T11FcSpPoIpMgmtWkpIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1, 4),
    _T11FcSpPoIpMgmtWkpIndex_Type()
)
t11FcSpPoIpMgmtWkpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtWkpIndex.setStatus("current")
_T11FcSpPoIpMgmtAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoIpMgmtAttribute_Object = MibTableColumn
t11FcSpPoIpMgmtAttribute = _T11FcSpPoIpMgmtAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 7, 1, 5),
    _T11FcSpPoIpMgmtAttribute_Type()
)
t11FcSpPoIpMgmtAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoIpMgmtAttribute.setStatus("current")
_T11FcSpPoWkpDescrTable_Object = MibTable
t11FcSpPoWkpDescrTable = _T11FcSpPoWkpDescrTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8)
)
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrTable.setStatus("current")
_T11FcSpPoWkpDescrEntry_Object = MibTableRow
t11FcSpPoWkpDescrEntry = _T11FcSpPoWkpDescrEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1)
)
t11FcSpPoWkpDescrEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoWkpDescrSpecifierIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoWkpDescrIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrEntry.setStatus("current")


class _T11FcSpPoWkpDescrSpecifierIndex_Type(Unsigned32):
    """Custom type t11FcSpPoWkpDescrSpecifierIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoWkpDescrSpecifierIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoWkpDescrSpecifierIndex_Object = MibTableColumn
t11FcSpPoWkpDescrSpecifierIndex = _T11FcSpPoWkpDescrSpecifierIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1, 1),
    _T11FcSpPoWkpDescrSpecifierIndex_Type()
)
t11FcSpPoWkpDescrSpecifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrSpecifierIndex.setStatus("current")


class _T11FcSpPoWkpDescrIndex_Type(Unsigned32):
    """Custom type t11FcSpPoWkpDescrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoWkpDescrIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoWkpDescrIndex_Object = MibTableColumn
t11FcSpPoWkpDescrIndex = _T11FcSpPoWkpDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1, 2),
    _T11FcSpPoWkpDescrIndex_Type()
)
t11FcSpPoWkpDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrIndex.setStatus("current")


class _T11FcSpPoWkpDescrFlags_Type(Bits):
    """Custom type t11FcSpPoWkpDescrFlags based on Bits"""
    namedValues = NamedValues(
        *(("allow", 0),
          ("destPortWildcard", 2),
          ("readOnly", 3),
          ("wkpWildcard", 1))
    )

_T11FcSpPoWkpDescrFlags_Type.__name__ = "Bits"
_T11FcSpPoWkpDescrFlags_Object = MibTableColumn
t11FcSpPoWkpDescrFlags = _T11FcSpPoWkpDescrFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1, 3),
    _T11FcSpPoWkpDescrFlags_Type()
)
t11FcSpPoWkpDescrFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrFlags.setStatus("current")


class _T11FcSpPoWkpDescrWkpNumber_Type(Unsigned32):
    """Custom type t11FcSpPoWkpDescrWkpNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11FcSpPoWkpDescrWkpNumber_Type.__name__ = "Unsigned32"
_T11FcSpPoWkpDescrWkpNumber_Object = MibTableColumn
t11FcSpPoWkpDescrWkpNumber = _T11FcSpPoWkpDescrWkpNumber_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1, 4),
    _T11FcSpPoWkpDescrWkpNumber_Type()
)
t11FcSpPoWkpDescrWkpNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrWkpNumber.setStatus("current")
_T11FcSpPoWkpDescrDestPort_Type = InetPortNumber
_T11FcSpPoWkpDescrDestPort_Object = MibTableColumn
t11FcSpPoWkpDescrDestPort = _T11FcSpPoWkpDescrDestPort_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 8, 1, 5),
    _T11FcSpPoWkpDescrDestPort_Type()
)
t11FcSpPoWkpDescrDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoWkpDescrDestPort.setStatus("current")
_T11FcSpPoAttribTable_Object = MibTable
t11FcSpPoAttribTable = _T11FcSpPoAttribTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9)
)
if mibBuilder.loadTexts:
    t11FcSpPoAttribTable.setStatus("current")
_T11FcSpPoAttribEntry_Object = MibTableRow
t11FcSpPoAttribEntry = _T11FcSpPoAttribEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1)
)
t11FcSpPoAttribEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribEntryIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribPartIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoAttribEntry.setStatus("current")
_T11FcSpPoAttribName_Type = T11FcSpAlphaNumName
_T11FcSpPoAttribName_Object = MibTableColumn
t11FcSpPoAttribName = _T11FcSpPoAttribName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 1),
    _T11FcSpPoAttribName_Type()
)
t11FcSpPoAttribName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoAttribName.setStatus("current")


class _T11FcSpPoAttribEntryIndex_Type(Unsigned32):
    """Custom type t11FcSpPoAttribEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoAttribEntryIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoAttribEntryIndex_Object = MibTableColumn
t11FcSpPoAttribEntryIndex = _T11FcSpPoAttribEntryIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 2),
    _T11FcSpPoAttribEntryIndex_Type()
)
t11FcSpPoAttribEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoAttribEntryIndex.setStatus("current")


class _T11FcSpPoAttribPartIndex_Type(Unsigned32):
    """Custom type t11FcSpPoAttribPartIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoAttribPartIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoAttribPartIndex_Object = MibTableColumn
t11FcSpPoAttribPartIndex = _T11FcSpPoAttribPartIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 3),
    _T11FcSpPoAttribPartIndex_Type()
)
t11FcSpPoAttribPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoAttribPartIndex.setStatus("current")


class _T11FcSpPoAttribType_Type(Unsigned32):
    """Custom type t11FcSpPoAttribType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoAttribType_Type.__name__ = "Unsigned32"
_T11FcSpPoAttribType_Object = MibTableColumn
t11FcSpPoAttribType = _T11FcSpPoAttribType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 4),
    _T11FcSpPoAttribType_Type()
)
t11FcSpPoAttribType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoAttribType.setStatus("current")


class _T11FcSpPoAttribValue_Type(OctetString):
    """Custom type t11FcSpPoAttribValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FcSpPoAttribValue_Type.__name__ = "OctetString"
_T11FcSpPoAttribValue_Object = MibTableColumn
t11FcSpPoAttribValue = _T11FcSpPoAttribValue_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 5),
    _T11FcSpPoAttribValue_Type()
)
t11FcSpPoAttribValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoAttribValue.setStatus("current")
_T11FcSpPoAttribExtension_Type = ObjectIdentifier
_T11FcSpPoAttribExtension_Object = MibTableColumn
t11FcSpPoAttribExtension = _T11FcSpPoAttribExtension_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 9, 1, 6),
    _T11FcSpPoAttribExtension_Type()
)
t11FcSpPoAttribExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoAttribExtension.setStatus("current")
_T11FcSpPoAuthProtTable_Object = MibTable
t11FcSpPoAuthProtTable = _T11FcSpPoAuthProtTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 10)
)
if mibBuilder.loadTexts:
    t11FcSpPoAuthProtTable.setStatus("current")
_T11FcSpPoAuthProtEntry_Object = MibTableRow
t11FcSpPoAuthProtEntry = _T11FcSpPoAuthProtEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 10, 1)
)
t11FcSpPoAuthProtEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribEntryIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAuthProtIdentifier"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoAuthProtPartIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoAuthProtEntry.setStatus("current")


class _T11FcSpPoAuthProtIdentifier_Type(Unsigned32):
    """Custom type t11FcSpPoAuthProtIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoAuthProtIdentifier_Type.__name__ = "Unsigned32"
_T11FcSpPoAuthProtIdentifier_Object = MibTableColumn
t11FcSpPoAuthProtIdentifier = _T11FcSpPoAuthProtIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 10, 1, 1),
    _T11FcSpPoAuthProtIdentifier_Type()
)
t11FcSpPoAuthProtIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoAuthProtIdentifier.setStatus("current")


class _T11FcSpPoAuthProtPartIndex_Type(Unsigned32):
    """Custom type t11FcSpPoAuthProtPartIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoAuthProtPartIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoAuthProtPartIndex_Object = MibTableColumn
t11FcSpPoAuthProtPartIndex = _T11FcSpPoAuthProtPartIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 10, 1, 2),
    _T11FcSpPoAuthProtPartIndex_Type()
)
t11FcSpPoAuthProtPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoAuthProtPartIndex.setStatus("current")


class _T11FcSpPoAuthProtParams_Type(OctetString):
    """Custom type t11FcSpPoAuthProtParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FcSpPoAuthProtParams_Type.__name__ = "OctetString"
_T11FcSpPoAuthProtParams_Object = MibTableColumn
t11FcSpPoAuthProtParams = _T11FcSpPoAuthProtParams_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 1, 10, 1, 3),
    _T11FcSpPoAuthProtParams_Type()
)
t11FcSpPoAuthProtParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoAuthProtParams.setStatus("current")
_T11FcSpPoOperations_ObjectIdentity = ObjectIdentity
t11FcSpPoOperations = _T11FcSpPoOperations_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1, 2)
)
_T11FcSpPoOperTable_Object = MibTable
t11FcSpPoOperTable = _T11FcSpPoOperTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1)
)
if mibBuilder.loadTexts:
    t11FcSpPoOperTable.setStatus("current")
_T11FcSpPoOperEntry_Object = MibTableRow
t11FcSpPoOperEntry = _T11FcSpPoOperEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1, 1)
)
t11FcSpPoOperEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoOperEntry.setStatus("current")
_T11FcSpPoOperActivate_Type = T11FcSpAlphaNumName
_T11FcSpPoOperActivate_Object = MibTableColumn
t11FcSpPoOperActivate = _T11FcSpPoOperActivate_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1, 1, 1),
    _T11FcSpPoOperActivate_Type()
)
t11FcSpPoOperActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpPoOperActivate.setStatus("current")
_T11FcSpPoOperDeActivate_Type = T11FcSpAlphaNumName
_T11FcSpPoOperDeActivate_Object = MibTableColumn
t11FcSpPoOperDeActivate = _T11FcSpPoOperDeActivate_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1, 1, 2),
    _T11FcSpPoOperDeActivate_Type()
)
t11FcSpPoOperDeActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpPoOperDeActivate.setStatus("current")


class _T11FcSpPoOperResult_Type(Integer32):
    """Custom type t11FcSpPoOperResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("activateFailure", 3),
          ("activateSuccess", 1),
          ("badSummaryObject", 2),
          ("deactivateFailure", 5),
          ("deactivateSuccess", 4),
          ("inProgress", 6),
          ("none", 7))
    )


_T11FcSpPoOperResult_Type.__name__ = "Integer32"
_T11FcSpPoOperResult_Object = MibTableColumn
t11FcSpPoOperResult = _T11FcSpPoOperResult_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1, 1, 3),
    _T11FcSpPoOperResult_Type()
)
t11FcSpPoOperResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoOperResult.setStatus("current")


class _T11FcSpPoOperFailCause_Type(SnmpAdminString):
    """Custom type t11FcSpPoOperFailCause based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_T11FcSpPoOperFailCause_Type.__name__ = "SnmpAdminString"
_T11FcSpPoOperFailCause_Object = MibTableColumn
t11FcSpPoOperFailCause = _T11FcSpPoOperFailCause_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 2, 1, 1, 4),
    _T11FcSpPoOperFailCause_Type()
)
t11FcSpPoOperFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoOperFailCause.setStatus("current")
_T11FcSpPoNonActive_ObjectIdentity = ObjectIdentity
t11FcSpPoNonActive = _T11FcSpPoNonActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1, 3)
)
_T11FcSpPoNaSummaryTable_Object = MibTable
t11FcSpPoNaSummaryTable = _T11FcSpPoNaSummaryTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryTable.setStatus("current")
_T11FcSpPoNaSummaryEntry_Object = MibTableRow
t11FcSpPoNaSummaryEntry = _T11FcSpPoNaSummaryEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1)
)
t11FcSpPoNaSummaryEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryPolicyType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryPolicyIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryEntry.setStatus("current")
_T11FcSpPoNaSummaryName_Type = T11FcSpAlphaNumName
_T11FcSpPoNaSummaryName_Object = MibTableColumn
t11FcSpPoNaSummaryName = _T11FcSpPoNaSummaryName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 1),
    _T11FcSpPoNaSummaryName_Type()
)
t11FcSpPoNaSummaryName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryName.setStatus("current")
_T11FcSpPoNaSummaryPolicyType_Type = T11FcSpPolicyObjectType
_T11FcSpPoNaSummaryPolicyType_Object = MibTableColumn
t11FcSpPoNaSummaryPolicyType = _T11FcSpPoNaSummaryPolicyType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 2),
    _T11FcSpPoNaSummaryPolicyType_Type()
)
t11FcSpPoNaSummaryPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryPolicyType.setStatus("current")


class _T11FcSpPoNaSummaryPolicyIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaSummaryPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaSummaryPolicyIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaSummaryPolicyIndex_Object = MibTableColumn
t11FcSpPoNaSummaryPolicyIndex = _T11FcSpPoNaSummaryPolicyIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 3),
    _T11FcSpPoNaSummaryPolicyIndex_Type()
)
t11FcSpPoNaSummaryPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryPolicyIndex.setStatus("current")


class _T11FcSpPoNaSummaryPolicyNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoNaSummaryPolicyNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alphaNumericName", 7),
          ("nodeName", 1))
    )


_T11FcSpPoNaSummaryPolicyNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoNaSummaryPolicyNameType_Object = MibTableColumn
t11FcSpPoNaSummaryPolicyNameType = _T11FcSpPoNaSummaryPolicyNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 4),
    _T11FcSpPoNaSummaryPolicyNameType_Type()
)
t11FcSpPoNaSummaryPolicyNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryPolicyNameType.setStatus("current")
_T11FcSpPoNaSummaryPolicyName_Type = T11FcSpPolicyName
_T11FcSpPoNaSummaryPolicyName_Object = MibTableColumn
t11FcSpPoNaSummaryPolicyName = _T11FcSpPoNaSummaryPolicyName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 5),
    _T11FcSpPoNaSummaryPolicyName_Type()
)
t11FcSpPoNaSummaryPolicyName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryPolicyName.setStatus("current")


class _T11FcSpPoNaSummaryHashStatus_Type(T11FcSpHashCalculationStatus):
    """Custom type t11FcSpPoNaSummaryHashStatus based on T11FcSpHashCalculationStatus"""


_T11FcSpPoNaSummaryHashStatus_Object = MibTableColumn
t11FcSpPoNaSummaryHashStatus = _T11FcSpPoNaSummaryHashStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 6),
    _T11FcSpPoNaSummaryHashStatus_Type()
)
t11FcSpPoNaSummaryHashStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryHashStatus.setStatus("current")


class _T11FcSpPoNaSummaryHashFormat_Type(T11FcSpPolicyHashFormat):
    """Custom type t11FcSpPoNaSummaryHashFormat based on T11FcSpPolicyHashFormat"""
    defaultHexValue = "00000001"


_T11FcSpPoNaSummaryHashFormat_Object = MibTableColumn
t11FcSpPoNaSummaryHashFormat = _T11FcSpPoNaSummaryHashFormat_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 7),
    _T11FcSpPoNaSummaryHashFormat_Type()
)
t11FcSpPoNaSummaryHashFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryHashFormat.setStatus("current")
_T11FcSpPoNaSummaryHashValue_Type = T11FcSpPolicyHashValue
_T11FcSpPoNaSummaryHashValue_Object = MibTableColumn
t11FcSpPoNaSummaryHashValue = _T11FcSpPoNaSummaryHashValue_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 8),
    _T11FcSpPoNaSummaryHashValue_Type()
)
t11FcSpPoNaSummaryHashValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryHashValue.setStatus("current")
_T11FcSpPoNaSummaryRowStatus_Type = RowStatus
_T11FcSpPoNaSummaryRowStatus_Object = MibTableColumn
t11FcSpPoNaSummaryRowStatus = _T11FcSpPoNaSummaryRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 1, 1, 9),
    _T11FcSpPoNaSummaryRowStatus_Type()
)
t11FcSpPoNaSummaryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSummaryRowStatus.setStatus("current")
_T11FcSpPoNaSwListTable_Object = MibTable
t11FcSpPoNaSwListTable = _T11FcSpPoNaSwListTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 2)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwListTable.setStatus("current")
_T11FcSpPoNaSwListEntry_Object = MibTableRow
t11FcSpPoNaSwListEntry = _T11FcSpPoNaSwListEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 2, 1)
)
t11FcSpPoNaSwListEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwListName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwListEntry.setStatus("current")
_T11FcSpPoNaSwListName_Type = T11FcSpAlphaNumName
_T11FcSpPoNaSwListName_Object = MibTableColumn
t11FcSpPoNaSwListName = _T11FcSpPoNaSwListName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 2, 1, 1),
    _T11FcSpPoNaSwListName_Type()
)
t11FcSpPoNaSwListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwListName.setStatus("current")
_T11FcSpPoNaSwListFabricName_Type = FcNameIdOrZero
_T11FcSpPoNaSwListFabricName_Object = MibTableColumn
t11FcSpPoNaSwListFabricName = _T11FcSpPoNaSwListFabricName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 2, 1, 2),
    _T11FcSpPoNaSwListFabricName_Type()
)
t11FcSpPoNaSwListFabricName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwListFabricName.setStatus("current")
_T11FcSpPoNaSwListRowStatus_Type = RowStatus
_T11FcSpPoNaSwListRowStatus_Object = MibTableColumn
t11FcSpPoNaSwListRowStatus = _T11FcSpPoNaSwListRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 2, 1, 3),
    _T11FcSpPoNaSwListRowStatus_Type()
)
t11FcSpPoNaSwListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwListRowStatus.setStatus("current")
_T11FcSpPoNaSwMembTable_Object = MibTable
t11FcSpPoNaSwMembTable = _T11FcSpPoNaSwMembTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembTable.setStatus("current")
_T11FcSpPoNaSwMembEntry_Object = MibTableRow
t11FcSpPoNaSwMembEntry = _T11FcSpPoNaSwMembEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1)
)
t11FcSpPoNaSwMembEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwListName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembSwitchNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembSwitchName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembEntry.setStatus("current")


class _T11FcSpPoNaSwMembSwitchNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoNaSwMembSwitchNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("restrictedNodeName", 2),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoNaSwMembSwitchNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoNaSwMembSwitchNameType_Object = MibTableColumn
t11FcSpPoNaSwMembSwitchNameType = _T11FcSpPoNaSwMembSwitchNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 1),
    _T11FcSpPoNaSwMembSwitchNameType_Type()
)
t11FcSpPoNaSwMembSwitchNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembSwitchNameType.setStatus("current")


class _T11FcSpPoNaSwMembSwitchName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNaSwMembSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNaSwMembSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNaSwMembSwitchName_Object = MibTableColumn
t11FcSpPoNaSwMembSwitchName = _T11FcSpPoNaSwMembSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 2),
    _T11FcSpPoNaSwMembSwitchName_Type()
)
t11FcSpPoNaSwMembSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembSwitchName.setStatus("current")


class _T11FcSpPoNaSwMembFlags_Type(Bits):
    """Custom type t11FcSpPoNaSwMembFlags based on Bits"""
    namedValues = NamedValues(
        *(("insistentDomainID", 1),
          ("managerRole", 4),
          ("physicalPortsAccess", 3),
          ("serialPortsAccess", 2),
          ("staticDomainID", 0))
    )

_T11FcSpPoNaSwMembFlags_Type.__name__ = "Bits"
_T11FcSpPoNaSwMembFlags_Object = MibTableColumn
t11FcSpPoNaSwMembFlags = _T11FcSpPoNaSwMembFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 3),
    _T11FcSpPoNaSwMembFlags_Type()
)
t11FcSpPoNaSwMembFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembFlags.setStatus("current")
_T11FcSpPoNaSwMembDomainID_Type = FcDomainIdOrZero
_T11FcSpPoNaSwMembDomainID_Object = MibTableColumn
t11FcSpPoNaSwMembDomainID = _T11FcSpPoNaSwMembDomainID_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 4),
    _T11FcSpPoNaSwMembDomainID_Type()
)
t11FcSpPoNaSwMembDomainID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembDomainID.setStatus("current")


class _T11FcSpPoNaSwMembPolicyDataRole_Type(Integer32):
    """Custom type t11FcSpPoNaSwMembPolicyDataRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autonomous", 2),
          ("client", 1),
          ("server", 3))
    )


_T11FcSpPoNaSwMembPolicyDataRole_Type.__name__ = "Integer32"
_T11FcSpPoNaSwMembPolicyDataRole_Object = MibTableColumn
t11FcSpPoNaSwMembPolicyDataRole = _T11FcSpPoNaSwMembPolicyDataRole_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 5),
    _T11FcSpPoNaSwMembPolicyDataRole_Type()
)
t11FcSpPoNaSwMembPolicyDataRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembPolicyDataRole.setStatus("current")


class _T11FcSpPoNaSwMembAuthBehaviour_Type(Bits):
    """Custom type t11FcSpPoNaSwMembAuthBehaviour based on Bits"""
    namedValues = NamedValues(
        *(("mustAuthenticate", 0),
          ("rejectIsFailure", 1))
    )

_T11FcSpPoNaSwMembAuthBehaviour_Type.__name__ = "Bits"
_T11FcSpPoNaSwMembAuthBehaviour_Object = MibTableColumn
t11FcSpPoNaSwMembAuthBehaviour = _T11FcSpPoNaSwMembAuthBehaviour_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 6),
    _T11FcSpPoNaSwMembAuthBehaviour_Type()
)
t11FcSpPoNaSwMembAuthBehaviour.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembAuthBehaviour.setStatus("current")
_T11FcSpPoNaSwMembAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoNaSwMembAttribute_Object = MibTableColumn
t11FcSpPoNaSwMembAttribute = _T11FcSpPoNaSwMembAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 7),
    _T11FcSpPoNaSwMembAttribute_Type()
)
t11FcSpPoNaSwMembAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembAttribute.setStatus("current")
_T11FcSpPoNaSwMembRowStatus_Type = RowStatus
_T11FcSpPoNaSwMembRowStatus_Object = MibTableColumn
t11FcSpPoNaSwMembRowStatus = _T11FcSpPoNaSwMembRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 3, 1, 8),
    _T11FcSpPoNaSwMembRowStatus_Type()
)
t11FcSpPoNaSwMembRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwMembRowStatus.setStatus("current")
_T11FcSpPoNaNoMembTable_Object = MibTable
t11FcSpPoNaNoMembTable = _T11FcSpPoNaNoMembTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembTable.setStatus("current")
_T11FcSpPoNaNoMembEntry_Object = MibTableRow
t11FcSpPoNaNoMembEntry = _T11FcSpPoNaNoMembEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1)
)
t11FcSpPoNaNoMembEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembListName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembNodeNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembNodeName"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembEntry.setStatus("current")
_T11FcSpPoNaNoMembListName_Type = T11FcSpAlphaNumName
_T11FcSpPoNaNoMembListName_Object = MibTableColumn
t11FcSpPoNaNoMembListName = _T11FcSpPoNaNoMembListName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 1),
    _T11FcSpPoNaNoMembListName_Type()
)
t11FcSpPoNaNoMembListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembListName.setStatus("current")


class _T11FcSpPoNaNoMembNodeNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoNaNoMembNodeNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("portName", 3),
          ("restrictedNodeName", 2),
          ("restrictedPortName", 4),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoNaNoMembNodeNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoNaNoMembNodeNameType_Object = MibTableColumn
t11FcSpPoNaNoMembNodeNameType = _T11FcSpPoNaNoMembNodeNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 2),
    _T11FcSpPoNaNoMembNodeNameType_Type()
)
t11FcSpPoNaNoMembNodeNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembNodeNameType.setStatus("current")


class _T11FcSpPoNaNoMembNodeName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNaNoMembNodeName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNaNoMembNodeName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNaNoMembNodeName_Object = MibTableColumn
t11FcSpPoNaNoMembNodeName = _T11FcSpPoNaNoMembNodeName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 3),
    _T11FcSpPoNaNoMembNodeName_Type()
)
t11FcSpPoNaNoMembNodeName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembNodeName.setStatus("current")


class _T11FcSpPoNaNoMembFlags_Type(Bits):
    """Custom type t11FcSpPoNaNoMembFlags based on Bits"""
    namedValues = NamedValues(
        *(("authenticationRequired", 1),
          ("scsiEnclosureAccess", 0))
    )

_T11FcSpPoNaNoMembFlags_Type.__name__ = "Bits"
_T11FcSpPoNaNoMembFlags_Object = MibTableColumn
t11FcSpPoNaNoMembFlags = _T11FcSpPoNaNoMembFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 4),
    _T11FcSpPoNaNoMembFlags_Type()
)
t11FcSpPoNaNoMembFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembFlags.setStatus("current")


class _T11FcSpPoNaNoMembCtAccessIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaNoMembCtAccessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoNaNoMembCtAccessIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaNoMembCtAccessIndex_Object = MibTableColumn
t11FcSpPoNaNoMembCtAccessIndex = _T11FcSpPoNaNoMembCtAccessIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 5),
    _T11FcSpPoNaNoMembCtAccessIndex_Type()
)
t11FcSpPoNaNoMembCtAccessIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembCtAccessIndex.setStatus("current")
_T11FcSpPoNaNoMembAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoNaNoMembAttribute_Object = MibTableColumn
t11FcSpPoNaNoMembAttribute = _T11FcSpPoNaNoMembAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 6),
    _T11FcSpPoNaNoMembAttribute_Type()
)
t11FcSpPoNaNoMembAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembAttribute.setStatus("current")
_T11FcSpPoNaNoMembRowStatus_Type = RowStatus
_T11FcSpPoNaNoMembRowStatus_Object = MibTableColumn
t11FcSpPoNaNoMembRowStatus = _T11FcSpPoNaNoMembRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 4, 1, 7),
    _T11FcSpPoNaNoMembRowStatus_Type()
)
t11FcSpPoNaNoMembRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaNoMembRowStatus.setStatus("current")
_T11FcSpPoNaCtDescrTable_Object = MibTable
t11FcSpPoNaCtDescrTable = _T11FcSpPoNaCtDescrTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrTable.setStatus("current")
_T11FcSpPoNaCtDescrEntry_Object = MibTableRow
t11FcSpPoNaCtDescrEntry = _T11FcSpPoNaCtDescrEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1)
)
t11FcSpPoNaCtDescrEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrSpecifierIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrEntry.setStatus("current")


class _T11FcSpPoNaCtDescrSpecifierIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaCtDescrSpecifierIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaCtDescrSpecifierIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaCtDescrSpecifierIndex_Object = MibTableColumn
t11FcSpPoNaCtDescrSpecifierIndex = _T11FcSpPoNaCtDescrSpecifierIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 1),
    _T11FcSpPoNaCtDescrSpecifierIndex_Type()
)
t11FcSpPoNaCtDescrSpecifierIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrSpecifierIndex.setStatus("current")


class _T11FcSpPoNaCtDescrIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaCtDescrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaCtDescrIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaCtDescrIndex_Object = MibTableColumn
t11FcSpPoNaCtDescrIndex = _T11FcSpPoNaCtDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 2),
    _T11FcSpPoNaCtDescrIndex_Type()
)
t11FcSpPoNaCtDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrIndex.setStatus("current")


class _T11FcSpPoNaCtDescrFlags_Type(Bits):
    """Custom type t11FcSpPoNaCtDescrFlags based on Bits"""
    namedValues = NamedValues(
        *(("allow", 0),
          ("gsSubTypeWildcard", 2),
          ("gsTypeWildcard", 1),
          ("readOnly", 3))
    )

_T11FcSpPoNaCtDescrFlags_Type.__name__ = "Bits"
_T11FcSpPoNaCtDescrFlags_Object = MibTableColumn
t11FcSpPoNaCtDescrFlags = _T11FcSpPoNaCtDescrFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 3),
    _T11FcSpPoNaCtDescrFlags_Type()
)
t11FcSpPoNaCtDescrFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrFlags.setStatus("current")


class _T11FcSpPoNaCtDescrGsType_Type(OctetString):
    """Custom type t11FcSpPoNaCtDescrGsType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcSpPoNaCtDescrGsType_Type.__name__ = "OctetString"
_T11FcSpPoNaCtDescrGsType_Object = MibTableColumn
t11FcSpPoNaCtDescrGsType = _T11FcSpPoNaCtDescrGsType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 4),
    _T11FcSpPoNaCtDescrGsType_Type()
)
t11FcSpPoNaCtDescrGsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrGsType.setStatus("current")


class _T11FcSpPoNaCtDescrGsSubType_Type(OctetString):
    """Custom type t11FcSpPoNaCtDescrGsSubType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_T11FcSpPoNaCtDescrGsSubType_Type.__name__ = "OctetString"
_T11FcSpPoNaCtDescrGsSubType_Object = MibTableColumn
t11FcSpPoNaCtDescrGsSubType = _T11FcSpPoNaCtDescrGsSubType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 5),
    _T11FcSpPoNaCtDescrGsSubType_Type()
)
t11FcSpPoNaCtDescrGsSubType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrGsSubType.setStatus("current")
_T11FcSpPoNaCtDescrRowStatus_Type = RowStatus
_T11FcSpPoNaCtDescrRowStatus_Object = MibTableColumn
t11FcSpPoNaCtDescrRowStatus = _T11FcSpPoNaCtDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 5, 1, 6),
    _T11FcSpPoNaCtDescrRowStatus_Type()
)
t11FcSpPoNaCtDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaCtDescrRowStatus.setStatus("current")
_T11FcSpPoNaSwConnTable_Object = MibTable
t11FcSpPoNaSwConnTable = _T11FcSpPoNaSwConnTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnTable.setStatus("current")
_T11FcSpPoNaSwConnEntry_Object = MibTableRow
t11FcSpPoNaSwConnEntry = _T11FcSpPoNaSwConnEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1)
)
t11FcSpPoNaSwConnEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnSwitchName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnAllowedType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnPortNameOrAll"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnAllowedIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnEntry.setStatus("current")


class _T11FcSpPoNaSwConnSwitchName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNaSwConnSwitchName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNaSwConnSwitchName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNaSwConnSwitchName_Object = MibTableColumn
t11FcSpPoNaSwConnSwitchName = _T11FcSpPoNaSwConnSwitchName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 1),
    _T11FcSpPoNaSwConnSwitchName_Type()
)
t11FcSpPoNaSwConnSwitchName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnSwitchName.setStatus("current")


class _T11FcSpPoNaSwConnAllowedType_Type(Integer32):
    """Custom type t11FcSpPoNaSwConnAllowedType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("node", 2),
          ("switch", 1))
    )


_T11FcSpPoNaSwConnAllowedType_Type.__name__ = "Integer32"
_T11FcSpPoNaSwConnAllowedType_Object = MibTableColumn
t11FcSpPoNaSwConnAllowedType = _T11FcSpPoNaSwConnAllowedType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 2),
    _T11FcSpPoNaSwConnAllowedType_Type()
)
t11FcSpPoNaSwConnAllowedType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnAllowedType.setStatus("current")


class _T11FcSpPoNaSwConnPortNameOrAll_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNaSwConnPortNameOrAll based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNaSwConnPortNameOrAll_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNaSwConnPortNameOrAll_Object = MibTableColumn
t11FcSpPoNaSwConnPortNameOrAll = _T11FcSpPoNaSwConnPortNameOrAll_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 3),
    _T11FcSpPoNaSwConnPortNameOrAll_Type()
)
t11FcSpPoNaSwConnPortNameOrAll.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnPortNameOrAll.setStatus("current")


class _T11FcSpPoNaSwConnAllowedIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaSwConnAllowedIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaSwConnAllowedIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaSwConnAllowedIndex_Object = MibTableColumn
t11FcSpPoNaSwConnAllowedIndex = _T11FcSpPoNaSwConnAllowedIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 4),
    _T11FcSpPoNaSwConnAllowedIndex_Type()
)
t11FcSpPoNaSwConnAllowedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnAllowedIndex.setStatus("current")


class _T11FcSpPoNaSwConnAllowedNameType_Type(T11FcSpPolicyNameType):
    """Custom type t11FcSpPoNaSwConnAllowedNameType based on T11FcSpPolicyNameType"""
    subtypeSpec = T11FcSpPolicyNameType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("nodeName", 1),
          ("portName", 3),
          ("restrictedNodeName", 2),
          ("restrictedPortName", 4),
          ("restrictedWildcard", 6),
          ("wildcard", 5))
    )


_T11FcSpPoNaSwConnAllowedNameType_Type.__name__ = "T11FcSpPolicyNameType"
_T11FcSpPoNaSwConnAllowedNameType_Object = MibTableColumn
t11FcSpPoNaSwConnAllowedNameType = _T11FcSpPoNaSwConnAllowedNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 5),
    _T11FcSpPoNaSwConnAllowedNameType_Type()
)
t11FcSpPoNaSwConnAllowedNameType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnAllowedNameType.setStatus("current")


class _T11FcSpPoNaSwConnAllowedName_Type(FcNameIdOrZero):
    """Custom type t11FcSpPoNaSwConnAllowedName based on FcNameIdOrZero"""
    subtypeSpec = FcNameIdOrZero.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_T11FcSpPoNaSwConnAllowedName_Type.__name__ = "FcNameIdOrZero"
_T11FcSpPoNaSwConnAllowedName_Object = MibTableColumn
t11FcSpPoNaSwConnAllowedName = _T11FcSpPoNaSwConnAllowedName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 6),
    _T11FcSpPoNaSwConnAllowedName_Type()
)
t11FcSpPoNaSwConnAllowedName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnAllowedName.setStatus("current")
_T11FcSpPoNaSwConnRowStatus_Type = RowStatus
_T11FcSpPoNaSwConnRowStatus_Object = MibTableColumn
t11FcSpPoNaSwConnRowStatus = _T11FcSpPoNaSwConnRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 6, 1, 7),
    _T11FcSpPoNaSwConnRowStatus_Type()
)
t11FcSpPoNaSwConnRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaSwConnRowStatus.setStatus("current")
_T11FcSpPoNaIpMgmtTable_Object = MibTable
t11FcSpPoNaIpMgmtTable = _T11FcSpPoNaIpMgmtTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtTable.setStatus("current")
_T11FcSpPoNaIpMgmtEntry_Object = MibTableRow
t11FcSpPoNaIpMgmtEntry = _T11FcSpPoNaIpMgmtEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1)
)
t11FcSpPoNaIpMgmtEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtListName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtEntryNameType"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtEntryNameLow"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtEntryNameHigh"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtEntry.setStatus("current")
_T11FcSpPoNaIpMgmtListName_Type = T11FcSpAlphaNumName
_T11FcSpPoNaIpMgmtListName_Object = MibTableColumn
t11FcSpPoNaIpMgmtListName = _T11FcSpPoNaIpMgmtListName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 1),
    _T11FcSpPoNaIpMgmtListName_Type()
)
t11FcSpPoNaIpMgmtListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtListName.setStatus("current")


class _T11FcSpPoNaIpMgmtEntryNameType_Type(InetAddressType):
    """Custom type t11FcSpPoNaIpMgmtEntryNameType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_T11FcSpPoNaIpMgmtEntryNameType_Type.__name__ = "InetAddressType"
_T11FcSpPoNaIpMgmtEntryNameType_Object = MibTableColumn
t11FcSpPoNaIpMgmtEntryNameType = _T11FcSpPoNaIpMgmtEntryNameType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 2),
    _T11FcSpPoNaIpMgmtEntryNameType_Type()
)
t11FcSpPoNaIpMgmtEntryNameType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtEntryNameType.setStatus("current")


class _T11FcSpPoNaIpMgmtEntryNameLow_Type(InetAddress):
    """Custom type t11FcSpPoNaIpMgmtEntryNameLow based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_T11FcSpPoNaIpMgmtEntryNameLow_Type.__name__ = "InetAddress"
_T11FcSpPoNaIpMgmtEntryNameLow_Object = MibTableColumn
t11FcSpPoNaIpMgmtEntryNameLow = _T11FcSpPoNaIpMgmtEntryNameLow_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 3),
    _T11FcSpPoNaIpMgmtEntryNameLow_Type()
)
t11FcSpPoNaIpMgmtEntryNameLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtEntryNameLow.setStatus("current")


class _T11FcSpPoNaIpMgmtEntryNameHigh_Type(InetAddress):
    """Custom type t11FcSpPoNaIpMgmtEntryNameHigh based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_T11FcSpPoNaIpMgmtEntryNameHigh_Type.__name__ = "InetAddress"
_T11FcSpPoNaIpMgmtEntryNameHigh_Object = MibTableColumn
t11FcSpPoNaIpMgmtEntryNameHigh = _T11FcSpPoNaIpMgmtEntryNameHigh_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 4),
    _T11FcSpPoNaIpMgmtEntryNameHigh_Type()
)
t11FcSpPoNaIpMgmtEntryNameHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtEntryNameHigh.setStatus("current")


class _T11FcSpPoNaIpMgmtWkpIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaIpMgmtWkpIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoNaIpMgmtWkpIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaIpMgmtWkpIndex_Object = MibTableColumn
t11FcSpPoNaIpMgmtWkpIndex = _T11FcSpPoNaIpMgmtWkpIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 5),
    _T11FcSpPoNaIpMgmtWkpIndex_Type()
)
t11FcSpPoNaIpMgmtWkpIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtWkpIndex.setStatus("current")
_T11FcSpPoNaIpMgmtAttribute_Type = T11FcSpAlphaNumNameOrAbsent
_T11FcSpPoNaIpMgmtAttribute_Object = MibTableColumn
t11FcSpPoNaIpMgmtAttribute = _T11FcSpPoNaIpMgmtAttribute_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 6),
    _T11FcSpPoNaIpMgmtAttribute_Type()
)
t11FcSpPoNaIpMgmtAttribute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtAttribute.setStatus("current")
_T11FcSpPoNaIpMgmtRowStatus_Type = RowStatus
_T11FcSpPoNaIpMgmtRowStatus_Object = MibTableColumn
t11FcSpPoNaIpMgmtRowStatus = _T11FcSpPoNaIpMgmtRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 7, 1, 7),
    _T11FcSpPoNaIpMgmtRowStatus_Type()
)
t11FcSpPoNaIpMgmtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaIpMgmtRowStatus.setStatus("current")
_T11FcSpPoNaWkpDescrTable_Object = MibTable
t11FcSpPoNaWkpDescrTable = _T11FcSpPoNaWkpDescrTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrTable.setStatus("current")
_T11FcSpPoNaWkpDescrEntry_Object = MibTableRow
t11FcSpPoNaWkpDescrEntry = _T11FcSpPoNaWkpDescrEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1)
)
t11FcSpPoNaWkpDescrEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrSpecifierIndx"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrEntry.setStatus("current")


class _T11FcSpPoNaWkpDescrSpecifierIndx_Type(Unsigned32):
    """Custom type t11FcSpPoNaWkpDescrSpecifierIndx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaWkpDescrSpecifierIndx_Type.__name__ = "Unsigned32"
_T11FcSpPoNaWkpDescrSpecifierIndx_Object = MibTableColumn
t11FcSpPoNaWkpDescrSpecifierIndx = _T11FcSpPoNaWkpDescrSpecifierIndx_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 1),
    _T11FcSpPoNaWkpDescrSpecifierIndx_Type()
)
t11FcSpPoNaWkpDescrSpecifierIndx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrSpecifierIndx.setStatus("current")


class _T11FcSpPoNaWkpDescrIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaWkpDescrIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaWkpDescrIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaWkpDescrIndex_Object = MibTableColumn
t11FcSpPoNaWkpDescrIndex = _T11FcSpPoNaWkpDescrIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 2),
    _T11FcSpPoNaWkpDescrIndex_Type()
)
t11FcSpPoNaWkpDescrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrIndex.setStatus("current")


class _T11FcSpPoNaWkpDescrFlags_Type(Bits):
    """Custom type t11FcSpPoNaWkpDescrFlags based on Bits"""
    namedValues = NamedValues(
        *(("allow", 0),
          ("destPortWildcard", 2),
          ("readOnly", 3),
          ("wkpWildcard", 1))
    )

_T11FcSpPoNaWkpDescrFlags_Type.__name__ = "Bits"
_T11FcSpPoNaWkpDescrFlags_Object = MibTableColumn
t11FcSpPoNaWkpDescrFlags = _T11FcSpPoNaWkpDescrFlags_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 3),
    _T11FcSpPoNaWkpDescrFlags_Type()
)
t11FcSpPoNaWkpDescrFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrFlags.setStatus("current")


class _T11FcSpPoNaWkpDescrWkpNumber_Type(Unsigned32):
    """Custom type t11FcSpPoNaWkpDescrWkpNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11FcSpPoNaWkpDescrWkpNumber_Type.__name__ = "Unsigned32"
_T11FcSpPoNaWkpDescrWkpNumber_Object = MibTableColumn
t11FcSpPoNaWkpDescrWkpNumber = _T11FcSpPoNaWkpDescrWkpNumber_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 4),
    _T11FcSpPoNaWkpDescrWkpNumber_Type()
)
t11FcSpPoNaWkpDescrWkpNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrWkpNumber.setStatus("current")
_T11FcSpPoNaWkpDescrDestPort_Type = InetPortNumber
_T11FcSpPoNaWkpDescrDestPort_Object = MibTableColumn
t11FcSpPoNaWkpDescrDestPort = _T11FcSpPoNaWkpDescrDestPort_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 5),
    _T11FcSpPoNaWkpDescrDestPort_Type()
)
t11FcSpPoNaWkpDescrDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrDestPort.setStatus("current")
_T11FcSpPoNaWkpDescrRowStatus_Type = RowStatus
_T11FcSpPoNaWkpDescrRowStatus_Object = MibTableColumn
t11FcSpPoNaWkpDescrRowStatus = _T11FcSpPoNaWkpDescrRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 8, 1, 6),
    _T11FcSpPoNaWkpDescrRowStatus_Type()
)
t11FcSpPoNaWkpDescrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaWkpDescrRowStatus.setStatus("current")
_T11FcSpPoNaAttribTable_Object = MibTable
t11FcSpPoNaAttribTable = _T11FcSpPoNaAttribTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribTable.setStatus("current")
_T11FcSpPoNaAttribEntry_Object = MibTableRow
t11FcSpPoNaAttribEntry = _T11FcSpPoNaAttribEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1)
)
t11FcSpPoNaAttribEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribEntryIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribPartIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribEntry.setStatus("current")
_T11FcSpPoNaAttribName_Type = T11FcSpAlphaNumName
_T11FcSpPoNaAttribName_Object = MibTableColumn
t11FcSpPoNaAttribName = _T11FcSpPoNaAttribName_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 1),
    _T11FcSpPoNaAttribName_Type()
)
t11FcSpPoNaAttribName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribName.setStatus("current")


class _T11FcSpPoNaAttribEntryIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaAttribEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaAttribEntryIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaAttribEntryIndex_Object = MibTableColumn
t11FcSpPoNaAttribEntryIndex = _T11FcSpPoNaAttribEntryIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 2),
    _T11FcSpPoNaAttribEntryIndex_Type()
)
t11FcSpPoNaAttribEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribEntryIndex.setStatus("current")


class _T11FcSpPoNaAttribPartIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaAttribPartIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaAttribPartIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaAttribPartIndex_Object = MibTableColumn
t11FcSpPoNaAttribPartIndex = _T11FcSpPoNaAttribPartIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 3),
    _T11FcSpPoNaAttribPartIndex_Type()
)
t11FcSpPoNaAttribPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribPartIndex.setStatus("current")


class _T11FcSpPoNaAttribType_Type(Unsigned32):
    """Custom type t11FcSpPoNaAttribType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaAttribType_Type.__name__ = "Unsigned32"
_T11FcSpPoNaAttribType_Object = MibTableColumn
t11FcSpPoNaAttribType = _T11FcSpPoNaAttribType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 4),
    _T11FcSpPoNaAttribType_Type()
)
t11FcSpPoNaAttribType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribType.setStatus("current")


class _T11FcSpPoNaAttribValue_Type(OctetString):
    """Custom type t11FcSpPoNaAttribValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FcSpPoNaAttribValue_Type.__name__ = "OctetString"
_T11FcSpPoNaAttribValue_Object = MibTableColumn
t11FcSpPoNaAttribValue = _T11FcSpPoNaAttribValue_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 5),
    _T11FcSpPoNaAttribValue_Type()
)
t11FcSpPoNaAttribValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribValue.setStatus("current")
_T11FcSpPoNaAttribExtension_Type = ObjectIdentifier
_T11FcSpPoNaAttribExtension_Object = MibTableColumn
t11FcSpPoNaAttribExtension = _T11FcSpPoNaAttribExtension_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 6),
    _T11FcSpPoNaAttribExtension_Type()
)
t11FcSpPoNaAttribExtension.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribExtension.setStatus("current")
_T11FcSpPoNaAttribRowStatus_Type = RowStatus
_T11FcSpPoNaAttribRowStatus_Object = MibTableColumn
t11FcSpPoNaAttribRowStatus = _T11FcSpPoNaAttribRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 9, 1, 7),
    _T11FcSpPoNaAttribRowStatus_Type()
)
t11FcSpPoNaAttribRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaAttribRowStatus.setStatus("current")
_T11FcSpPoNaAuthProtTable_Object = MibTable
t11FcSpPoNaAuthProtTable = _T11FcSpPoNaAuthProtTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10)
)
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtTable.setStatus("current")
_T11FcSpPoNaAuthProtEntry_Object = MibTableRow
t11FcSpPoNaAuthProtEntry = _T11FcSpPoNaAuthProtEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10, 1)
)
t11FcSpPoNaAuthProtEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribName"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribEntryIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAuthProtIdentifier"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAuthProtPartIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtEntry.setStatus("current")


class _T11FcSpPoNaAuthProtIdentifier_Type(Unsigned32):
    """Custom type t11FcSpPoNaAuthProtIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_T11FcSpPoNaAuthProtIdentifier_Type.__name__ = "Unsigned32"
_T11FcSpPoNaAuthProtIdentifier_Object = MibTableColumn
t11FcSpPoNaAuthProtIdentifier = _T11FcSpPoNaAuthProtIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10, 1, 1),
    _T11FcSpPoNaAuthProtIdentifier_Type()
)
t11FcSpPoNaAuthProtIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtIdentifier.setStatus("current")


class _T11FcSpPoNaAuthProtPartIndex_Type(Unsigned32):
    """Custom type t11FcSpPoNaAuthProtPartIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_T11FcSpPoNaAuthProtPartIndex_Type.__name__ = "Unsigned32"
_T11FcSpPoNaAuthProtPartIndex_Object = MibTableColumn
t11FcSpPoNaAuthProtPartIndex = _T11FcSpPoNaAuthProtPartIndex_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10, 1, 2),
    _T11FcSpPoNaAuthProtPartIndex_Type()
)
t11FcSpPoNaAuthProtPartIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtPartIndex.setStatus("current")


class _T11FcSpPoNaAuthProtParams_Type(OctetString):
    """Custom type t11FcSpPoNaAuthProtParams based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_T11FcSpPoNaAuthProtParams_Type.__name__ = "OctetString"
_T11FcSpPoNaAuthProtParams_Object = MibTableColumn
t11FcSpPoNaAuthProtParams = _T11FcSpPoNaAuthProtParams_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10, 1, 3),
    _T11FcSpPoNaAuthProtParams_Type()
)
t11FcSpPoNaAuthProtParams.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtParams.setStatus("current")
_T11FcSpPoNaAuthProtRowStatus_Type = RowStatus
_T11FcSpPoNaAuthProtRowStatus_Object = MibTableColumn
t11FcSpPoNaAuthProtRowStatus = _T11FcSpPoNaAuthProtRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 3, 10, 1, 4),
    _T11FcSpPoNaAuthProtRowStatus_Type()
)
t11FcSpPoNaAuthProtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    t11FcSpPoNaAuthProtRowStatus.setStatus("current")
_T11FcSpPoStatistics_ObjectIdentity = ObjectIdentity
t11FcSpPoStatistics = _T11FcSpPoStatistics_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1, 4)
)
_T11FcSpPoStatsTable_Object = MibTable
t11FcSpPoStatsTable = _T11FcSpPoStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 4, 1)
)
if mibBuilder.loadTexts:
    t11FcSpPoStatsTable.setStatus("current")
_T11FcSpPoStatsEntry_Object = MibTableRow
t11FcSpPoStatsEntry = _T11FcSpPoStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 4, 1, 1)
)
t11FcSpPoStatsEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoStatsEntry.setStatus("current")
_T11FcSpPoInRequests_Type = Counter32
_T11FcSpPoInRequests_Object = MibTableColumn
t11FcSpPoInRequests = _T11FcSpPoInRequests_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 4, 1, 1, 1),
    _T11FcSpPoInRequests_Type()
)
t11FcSpPoInRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoInRequests.setStatus("current")
_T11FcSpPoInAccepts_Type = Counter32
_T11FcSpPoInAccepts_Object = MibTableColumn
t11FcSpPoInAccepts = _T11FcSpPoInAccepts_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 4, 1, 1, 2),
    _T11FcSpPoInAccepts_Type()
)
t11FcSpPoInAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoInAccepts.setStatus("current")
_T11FcSpPoInRejects_Type = Counter32
_T11FcSpPoInRejects_Object = MibTableColumn
t11FcSpPoInRejects = _T11FcSpPoInRejects_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 4, 1, 1, 3),
    _T11FcSpPoInRejects_Type()
)
t11FcSpPoInRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoInRejects.setStatus("current")
_T11FcSpPoControl_ObjectIdentity = ObjectIdentity
t11FcSpPoControl = _T11FcSpPoControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 1, 5)
)
_T11FcSpPoServerAddress_Type = FcNameIdOrZero
_T11FcSpPoServerAddress_Object = MibScalar
t11FcSpPoServerAddress = _T11FcSpPoServerAddress_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 1),
    _T11FcSpPoServerAddress_Type()
)
t11FcSpPoServerAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    t11FcSpPoServerAddress.setStatus("current")
_T11FcSpPoControlTable_Object = MibTable
t11FcSpPoControlTable = _T11FcSpPoControlTable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2)
)
if mibBuilder.loadTexts:
    t11FcSpPoControlTable.setStatus("current")
_T11FcSpPoControlEntry_Object = MibTableRow
t11FcSpPoControlEntry = _T11FcSpPoControlEntry_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1)
)
t11FcSpPoControlEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "T11-FC-SP-POLICY-MIB", "t11FcSpPoFabricIndex"),
)
if mibBuilder.loadTexts:
    t11FcSpPoControlEntry.setStatus("current")
_T11FcSpPoStorageType_Type = StorageType
_T11FcSpPoStorageType_Object = MibTableColumn
t11FcSpPoStorageType = _T11FcSpPoStorageType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 1),
    _T11FcSpPoStorageType_Type()
)
t11FcSpPoStorageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpPoStorageType.setStatus("current")
_T11FcSpPoNotificationEnable_Type = TruthValue
_T11FcSpPoNotificationEnable_Object = MibTableColumn
t11FcSpPoNotificationEnable = _T11FcSpPoNotificationEnable_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 2),
    _T11FcSpPoNotificationEnable_Type()
)
t11FcSpPoNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    t11FcSpPoNotificationEnable.setStatus("current")


class _T11FcSpPoLastNotifyType_Type(Integer32):
    """Custom type t11FcSpPoLastNotifyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("activateFail", 3),
          ("activation", 2),
          ("deactivateFail", 5),
          ("deactivation", 4),
          ("none", 1))
    )


_T11FcSpPoLastNotifyType_Type.__name__ = "Integer32"
_T11FcSpPoLastNotifyType_Object = MibTableColumn
t11FcSpPoLastNotifyType = _T11FcSpPoLastNotifyType_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 3),
    _T11FcSpPoLastNotifyType_Type()
)
t11FcSpPoLastNotifyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoLastNotifyType.setStatus("current")
_T11FcSpPoRequestSource_Type = FcNameIdOrZero
_T11FcSpPoRequestSource_Object = MibTableColumn
t11FcSpPoRequestSource = _T11FcSpPoRequestSource_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 4),
    _T11FcSpPoRequestSource_Type()
)
t11FcSpPoRequestSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoRequestSource.setStatus("current")
_T11FcSpPoReasonCode_Type = T11NsGs4RejectReasonCode
_T11FcSpPoReasonCode_Object = MibTableColumn
t11FcSpPoReasonCode = _T11FcSpPoReasonCode_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 5),
    _T11FcSpPoReasonCode_Type()
)
t11FcSpPoReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoReasonCode.setStatus("current")


class _T11FcSpPoCtCommandString_Type(OctetString):
    """Custom type t11FcSpPoCtCommandString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_T11FcSpPoCtCommandString_Type.__name__ = "OctetString"
_T11FcSpPoCtCommandString_Object = MibTableColumn
t11FcSpPoCtCommandString = _T11FcSpPoCtCommandString_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 6),
    _T11FcSpPoCtCommandString_Type()
)
t11FcSpPoCtCommandString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoCtCommandString.setStatus("current")


class _T11FcSpPoReasonCodeExp_Type(Unsigned32):
    """Custom type t11FcSpPoReasonCodeExp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_T11FcSpPoReasonCodeExp_Type.__name__ = "Unsigned32"
_T11FcSpPoReasonCodeExp_Object = MibTableColumn
t11FcSpPoReasonCodeExp = _T11FcSpPoReasonCodeExp_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 7),
    _T11FcSpPoReasonCodeExp_Type()
)
t11FcSpPoReasonCodeExp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoReasonCodeExp.setStatus("current")


class _T11FcSpPoReasonVendorCode_Type(OctetString):
    """Custom type t11FcSpPoReasonVendorCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(1, 1),
    )


_T11FcSpPoReasonVendorCode_Type.__name__ = "OctetString"
_T11FcSpPoReasonVendorCode_Object = MibTableColumn
t11FcSpPoReasonVendorCode = _T11FcSpPoReasonVendorCode_Object(
    (1, 3, 6, 1, 2, 1, 178, 1, 5, 2, 1, 8),
    _T11FcSpPoReasonVendorCode_Type()
)
t11FcSpPoReasonVendorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    t11FcSpPoReasonVendorCode.setStatus("current")
_T11FcSpPoMIBConformance_ObjectIdentity = ObjectIdentity
t11FcSpPoMIBConformance = _T11FcSpPoMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 2)
)
_T11FcSpPoMIBCompliances_ObjectIdentity = ObjectIdentity
t11FcSpPoMIBCompliances = _T11FcSpPoMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 2, 1)
)
_T11FcSpPoMIBGroups_ObjectIdentity = ObjectIdentity
t11FcSpPoMIBGroups = _T11FcSpPoMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 178, 2, 2)
)

# Managed Objects groups

t11FcSpPoActiveObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 1)
)
t11FcSpPoActiveObjectsGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoPolicySummaryObjName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoAdminFabricName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoActivatedTimeStamp"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSummaryPolicyType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSummaryHashFormat"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSummaryHashValue"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembSwitchFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembDomainID"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembPolicyDataRole"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembAuthBehaviour"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwMembAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNoMembFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNoMembCtAccessIndex"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNoMembAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtDescrFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtDescrGsType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtDescrGsSubType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnAllowedNameType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoSwConnAllowedName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoIpMgmtWkpIndex"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoIpMgmtAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoWkpDescrFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoWkpDescrWkpNumber"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoWkpDescrDestPort"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribValue"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoAttribExtension"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoAuthProtParams"))
)
if mibBuilder.loadTexts:
    t11FcSpPoActiveObjectsGroup.setStatus("current")

t11FcSpPoOperationsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 2)
)
t11FcSpPoOperationsObjectsGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoOperActivate"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoOperDeActivate"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoOperResult"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoOperFailCause"))
)
if mibBuilder.loadTexts:
    t11FcSpPoOperationsObjectsGroup.setStatus("current")

t11FcSpPoNonActiveObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 3)
)
t11FcSpPoNonActiveObjectsGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoStorageType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryPolicyNameType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryPolicyName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryHashStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryHashFormat"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryHashValue"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSummaryRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwListFabricName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwListRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembDomainID"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembPolicyDataRole"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembAuthBehaviour"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwMembRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembCtAccessIndex"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaNoMembRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrGsType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrGsSubType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaCtDescrRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnAllowedNameType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnAllowedName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaSwConnRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtWkpIndex"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtAttribute"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaIpMgmtRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrFlags"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrWkpNumber"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrDestPort"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaWkpDescrRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribValue"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribExtension"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAttribRowStatus"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAuthProtParams"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNaAuthProtRowStatus"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNonActiveObjectsGroup.setStatus("current")

t11FcSpPoStatsObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 4)
)
t11FcSpPoStatsObjectsGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoInRequests"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoInAccepts"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoInRejects"))
)
if mibBuilder.loadTexts:
    t11FcSpPoStatsObjectsGroup.setStatus("current")

t11FcSpPoNotifyObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 5)
)
t11FcSpPoNotifyObjectsGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoNotificationEnable"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoServerAddress"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoLastNotifyType"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoRequestSource"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCode"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtCommandString"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCodeExp"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotifyObjectsGroup.setStatus("current")


# Notification objects

t11FcSpPoNotifyActivation = NotificationType(
    (1, 3, 6, 1, 2, 1, 178, 0, 1)
)
t11FcSpPoNotifyActivation.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoServerAddress"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoPolicySummaryObjName"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoRequestSource"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotifyActivation.setStatus(
        "current"
    )

t11FcSpPoNotifyActivateFail = NotificationType(
    (1, 3, 6, 1, 2, 1, 178, 0, 2)
)
t11FcSpPoNotifyActivateFail.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoServerAddress"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoRequestSource"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtCommandString"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCode"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCodeExp"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotifyActivateFail.setStatus(
        "current"
    )

t11FcSpPoNotifyDeactivation = NotificationType(
    (1, 3, 6, 1, 2, 1, 178, 0, 3)
)
t11FcSpPoNotifyDeactivation.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoServerAddress"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoRequestSource"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotifyDeactivation.setStatus(
        "current"
    )

t11FcSpPoNotifyDeactivateFail = NotificationType(
    (1, 3, 6, 1, 2, 1, 178, 0, 4)
)
t11FcSpPoNotifyDeactivateFail.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoServerAddress"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoRequestSource"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoCtCommandString"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCode"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonCodeExp"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoReasonVendorCode"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotifyDeactivateFail.setStatus(
        "current"
    )


# Notifications groups

t11FcSpPoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 178, 2, 2, 6)
)
t11FcSpPoNotificationGroup.setObjects(
      *(("T11-FC-SP-POLICY-MIB", "t11FcSpPoNotifyActivation"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNotifyActivateFail"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNotifyDeactivation"),
        ("T11-FC-SP-POLICY-MIB", "t11FcSpPoNotifyDeactivateFail"))
)
if mibBuilder.loadTexts:
    t11FcSpPoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

t11FcSpPoMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 178, 2, 1, 1)
)
if mibBuilder.loadTexts:
    t11FcSpPoMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "T11-FC-SP-POLICY-MIB",
    **{"t11FcSpPolicyMIB": t11FcSpPolicyMIB,
       "t11FcSpPoMIBNotifications": t11FcSpPoMIBNotifications,
       "t11FcSpPoNotifyActivation": t11FcSpPoNotifyActivation,
       "t11FcSpPoNotifyActivateFail": t11FcSpPoNotifyActivateFail,
       "t11FcSpPoNotifyDeactivation": t11FcSpPoNotifyDeactivation,
       "t11FcSpPoNotifyDeactivateFail": t11FcSpPoNotifyDeactivateFail,
       "t11FcSpPoMIBObjects": t11FcSpPoMIBObjects,
       "t11FcSpPoActive": t11FcSpPoActive,
       "t11FcSpPoTable": t11FcSpPoTable,
       "t11FcSpPoEntry": t11FcSpPoEntry,
       "t11FcSpPoFabricIndex": t11FcSpPoFabricIndex,
       "t11FcSpPoPolicySummaryObjName": t11FcSpPoPolicySummaryObjName,
       "t11FcSpPoAdminFabricName": t11FcSpPoAdminFabricName,
       "t11FcSpPoActivatedTimeStamp": t11FcSpPoActivatedTimeStamp,
       "t11FcSpPoSummaryTable": t11FcSpPoSummaryTable,
       "t11FcSpPoSummaryEntry": t11FcSpPoSummaryEntry,
       "t11FcSpPoSummaryPolicyNameType": t11FcSpPoSummaryPolicyNameType,
       "t11FcSpPoSummaryPolicyName": t11FcSpPoSummaryPolicyName,
       "t11FcSpPoSummaryPolicyType": t11FcSpPoSummaryPolicyType,
       "t11FcSpPoSummaryHashFormat": t11FcSpPoSummaryHashFormat,
       "t11FcSpPoSummaryHashValue": t11FcSpPoSummaryHashValue,
       "t11FcSpPoSwMembTable": t11FcSpPoSwMembTable,
       "t11FcSpPoSwMembEntry": t11FcSpPoSwMembEntry,
       "t11FcSpPoSwMembSwitchNameType": t11FcSpPoSwMembSwitchNameType,
       "t11FcSpPoSwMembSwitchName": t11FcSpPoSwMembSwitchName,
       "t11FcSpPoSwMembSwitchFlags": t11FcSpPoSwMembSwitchFlags,
       "t11FcSpPoSwMembDomainID": t11FcSpPoSwMembDomainID,
       "t11FcSpPoSwMembPolicyDataRole": t11FcSpPoSwMembPolicyDataRole,
       "t11FcSpPoSwMembAuthBehaviour": t11FcSpPoSwMembAuthBehaviour,
       "t11FcSpPoSwMembAttribute": t11FcSpPoSwMembAttribute,
       "t11FcSpPoNoMembTable": t11FcSpPoNoMembTable,
       "t11FcSpPoNoMembEntry": t11FcSpPoNoMembEntry,
       "t11FcSpPoNoMembNodeNameType": t11FcSpPoNoMembNodeNameType,
       "t11FcSpPoNoMembNodeName": t11FcSpPoNoMembNodeName,
       "t11FcSpPoNoMembFlags": t11FcSpPoNoMembFlags,
       "t11FcSpPoNoMembCtAccessIndex": t11FcSpPoNoMembCtAccessIndex,
       "t11FcSpPoNoMembAttribute": t11FcSpPoNoMembAttribute,
       "t11FcSpPoCtDescrTable": t11FcSpPoCtDescrTable,
       "t11FcSpPoCtDescrEntry": t11FcSpPoCtDescrEntry,
       "t11FcSpPoCtDescrSpecifierIndex": t11FcSpPoCtDescrSpecifierIndex,
       "t11FcSpPoCtDescrIndex": t11FcSpPoCtDescrIndex,
       "t11FcSpPoCtDescrFlags": t11FcSpPoCtDescrFlags,
       "t11FcSpPoCtDescrGsType": t11FcSpPoCtDescrGsType,
       "t11FcSpPoCtDescrGsSubType": t11FcSpPoCtDescrGsSubType,
       "t11FcSpPoSwConnTable": t11FcSpPoSwConnTable,
       "t11FcSpPoSwConnEntry": t11FcSpPoSwConnEntry,
       "t11FcSpPoSwConnSwitchName": t11FcSpPoSwConnSwitchName,
       "t11FcSpPoSwConnAllowedType": t11FcSpPoSwConnAllowedType,
       "t11FcSpPoSwConnPortNameOrAll": t11FcSpPoSwConnPortNameOrAll,
       "t11FcSpPoSwConnAllowedIndex": t11FcSpPoSwConnAllowedIndex,
       "t11FcSpPoSwConnAllowedNameType": t11FcSpPoSwConnAllowedNameType,
       "t11FcSpPoSwConnAllowedName": t11FcSpPoSwConnAllowedName,
       "t11FcSpPoIpMgmtTable": t11FcSpPoIpMgmtTable,
       "t11FcSpPoIpMgmtEntry": t11FcSpPoIpMgmtEntry,
       "t11FcSpPoIpMgmtEntryNameType": t11FcSpPoIpMgmtEntryNameType,
       "t11FcSpPoIpMgmtEntryNameLow": t11FcSpPoIpMgmtEntryNameLow,
       "t11FcSpPoIpMgmtEntryNameHigh": t11FcSpPoIpMgmtEntryNameHigh,
       "t11FcSpPoIpMgmtWkpIndex": t11FcSpPoIpMgmtWkpIndex,
       "t11FcSpPoIpMgmtAttribute": t11FcSpPoIpMgmtAttribute,
       "t11FcSpPoWkpDescrTable": t11FcSpPoWkpDescrTable,
       "t11FcSpPoWkpDescrEntry": t11FcSpPoWkpDescrEntry,
       "t11FcSpPoWkpDescrSpecifierIndex": t11FcSpPoWkpDescrSpecifierIndex,
       "t11FcSpPoWkpDescrIndex": t11FcSpPoWkpDescrIndex,
       "t11FcSpPoWkpDescrFlags": t11FcSpPoWkpDescrFlags,
       "t11FcSpPoWkpDescrWkpNumber": t11FcSpPoWkpDescrWkpNumber,
       "t11FcSpPoWkpDescrDestPort": t11FcSpPoWkpDescrDestPort,
       "t11FcSpPoAttribTable": t11FcSpPoAttribTable,
       "t11FcSpPoAttribEntry": t11FcSpPoAttribEntry,
       "t11FcSpPoAttribName": t11FcSpPoAttribName,
       "t11FcSpPoAttribEntryIndex": t11FcSpPoAttribEntryIndex,
       "t11FcSpPoAttribPartIndex": t11FcSpPoAttribPartIndex,
       "t11FcSpPoAttribType": t11FcSpPoAttribType,
       "t11FcSpPoAttribValue": t11FcSpPoAttribValue,
       "t11FcSpPoAttribExtension": t11FcSpPoAttribExtension,
       "t11FcSpPoAuthProtTable": t11FcSpPoAuthProtTable,
       "t11FcSpPoAuthProtEntry": t11FcSpPoAuthProtEntry,
       "t11FcSpPoAuthProtIdentifier": t11FcSpPoAuthProtIdentifier,
       "t11FcSpPoAuthProtPartIndex": t11FcSpPoAuthProtPartIndex,
       "t11FcSpPoAuthProtParams": t11FcSpPoAuthProtParams,
       "t11FcSpPoOperations": t11FcSpPoOperations,
       "t11FcSpPoOperTable": t11FcSpPoOperTable,
       "t11FcSpPoOperEntry": t11FcSpPoOperEntry,
       "t11FcSpPoOperActivate": t11FcSpPoOperActivate,
       "t11FcSpPoOperDeActivate": t11FcSpPoOperDeActivate,
       "t11FcSpPoOperResult": t11FcSpPoOperResult,
       "t11FcSpPoOperFailCause": t11FcSpPoOperFailCause,
       "t11FcSpPoNonActive": t11FcSpPoNonActive,
       "t11FcSpPoNaSummaryTable": t11FcSpPoNaSummaryTable,
       "t11FcSpPoNaSummaryEntry": t11FcSpPoNaSummaryEntry,
       "t11FcSpPoNaSummaryName": t11FcSpPoNaSummaryName,
       "t11FcSpPoNaSummaryPolicyType": t11FcSpPoNaSummaryPolicyType,
       "t11FcSpPoNaSummaryPolicyIndex": t11FcSpPoNaSummaryPolicyIndex,
       "t11FcSpPoNaSummaryPolicyNameType": t11FcSpPoNaSummaryPolicyNameType,
       "t11FcSpPoNaSummaryPolicyName": t11FcSpPoNaSummaryPolicyName,
       "t11FcSpPoNaSummaryHashStatus": t11FcSpPoNaSummaryHashStatus,
       "t11FcSpPoNaSummaryHashFormat": t11FcSpPoNaSummaryHashFormat,
       "t11FcSpPoNaSummaryHashValue": t11FcSpPoNaSummaryHashValue,
       "t11FcSpPoNaSummaryRowStatus": t11FcSpPoNaSummaryRowStatus,
       "t11FcSpPoNaSwListTable": t11FcSpPoNaSwListTable,
       "t11FcSpPoNaSwListEntry": t11FcSpPoNaSwListEntry,
       "t11FcSpPoNaSwListName": t11FcSpPoNaSwListName,
       "t11FcSpPoNaSwListFabricName": t11FcSpPoNaSwListFabricName,
       "t11FcSpPoNaSwListRowStatus": t11FcSpPoNaSwListRowStatus,
       "t11FcSpPoNaSwMembTable": t11FcSpPoNaSwMembTable,
       "t11FcSpPoNaSwMembEntry": t11FcSpPoNaSwMembEntry,
       "t11FcSpPoNaSwMembSwitchNameType": t11FcSpPoNaSwMembSwitchNameType,
       "t11FcSpPoNaSwMembSwitchName": t11FcSpPoNaSwMembSwitchName,
       "t11FcSpPoNaSwMembFlags": t11FcSpPoNaSwMembFlags,
       "t11FcSpPoNaSwMembDomainID": t11FcSpPoNaSwMembDomainID,
       "t11FcSpPoNaSwMembPolicyDataRole": t11FcSpPoNaSwMembPolicyDataRole,
       "t11FcSpPoNaSwMembAuthBehaviour": t11FcSpPoNaSwMembAuthBehaviour,
       "t11FcSpPoNaSwMembAttribute": t11FcSpPoNaSwMembAttribute,
       "t11FcSpPoNaSwMembRowStatus": t11FcSpPoNaSwMembRowStatus,
       "t11FcSpPoNaNoMembTable": t11FcSpPoNaNoMembTable,
       "t11FcSpPoNaNoMembEntry": t11FcSpPoNaNoMembEntry,
       "t11FcSpPoNaNoMembListName": t11FcSpPoNaNoMembListName,
       "t11FcSpPoNaNoMembNodeNameType": t11FcSpPoNaNoMembNodeNameType,
       "t11FcSpPoNaNoMembNodeName": t11FcSpPoNaNoMembNodeName,
       "t11FcSpPoNaNoMembFlags": t11FcSpPoNaNoMembFlags,
       "t11FcSpPoNaNoMembCtAccessIndex": t11FcSpPoNaNoMembCtAccessIndex,
       "t11FcSpPoNaNoMembAttribute": t11FcSpPoNaNoMembAttribute,
       "t11FcSpPoNaNoMembRowStatus": t11FcSpPoNaNoMembRowStatus,
       "t11FcSpPoNaCtDescrTable": t11FcSpPoNaCtDescrTable,
       "t11FcSpPoNaCtDescrEntry": t11FcSpPoNaCtDescrEntry,
       "t11FcSpPoNaCtDescrSpecifierIndex": t11FcSpPoNaCtDescrSpecifierIndex,
       "t11FcSpPoNaCtDescrIndex": t11FcSpPoNaCtDescrIndex,
       "t11FcSpPoNaCtDescrFlags": t11FcSpPoNaCtDescrFlags,
       "t11FcSpPoNaCtDescrGsType": t11FcSpPoNaCtDescrGsType,
       "t11FcSpPoNaCtDescrGsSubType": t11FcSpPoNaCtDescrGsSubType,
       "t11FcSpPoNaCtDescrRowStatus": t11FcSpPoNaCtDescrRowStatus,
       "t11FcSpPoNaSwConnTable": t11FcSpPoNaSwConnTable,
       "t11FcSpPoNaSwConnEntry": t11FcSpPoNaSwConnEntry,
       "t11FcSpPoNaSwConnSwitchName": t11FcSpPoNaSwConnSwitchName,
       "t11FcSpPoNaSwConnAllowedType": t11FcSpPoNaSwConnAllowedType,
       "t11FcSpPoNaSwConnPortNameOrAll": t11FcSpPoNaSwConnPortNameOrAll,
       "t11FcSpPoNaSwConnAllowedIndex": t11FcSpPoNaSwConnAllowedIndex,
       "t11FcSpPoNaSwConnAllowedNameType": t11FcSpPoNaSwConnAllowedNameType,
       "t11FcSpPoNaSwConnAllowedName": t11FcSpPoNaSwConnAllowedName,
       "t11FcSpPoNaSwConnRowStatus": t11FcSpPoNaSwConnRowStatus,
       "t11FcSpPoNaIpMgmtTable": t11FcSpPoNaIpMgmtTable,
       "t11FcSpPoNaIpMgmtEntry": t11FcSpPoNaIpMgmtEntry,
       "t11FcSpPoNaIpMgmtListName": t11FcSpPoNaIpMgmtListName,
       "t11FcSpPoNaIpMgmtEntryNameType": t11FcSpPoNaIpMgmtEntryNameType,
       "t11FcSpPoNaIpMgmtEntryNameLow": t11FcSpPoNaIpMgmtEntryNameLow,
       "t11FcSpPoNaIpMgmtEntryNameHigh": t11FcSpPoNaIpMgmtEntryNameHigh,
       "t11FcSpPoNaIpMgmtWkpIndex": t11FcSpPoNaIpMgmtWkpIndex,
       "t11FcSpPoNaIpMgmtAttribute": t11FcSpPoNaIpMgmtAttribute,
       "t11FcSpPoNaIpMgmtRowStatus": t11FcSpPoNaIpMgmtRowStatus,
       "t11FcSpPoNaWkpDescrTable": t11FcSpPoNaWkpDescrTable,
       "t11FcSpPoNaWkpDescrEntry": t11FcSpPoNaWkpDescrEntry,
       "t11FcSpPoNaWkpDescrSpecifierIndx": t11FcSpPoNaWkpDescrSpecifierIndx,
       "t11FcSpPoNaWkpDescrIndex": t11FcSpPoNaWkpDescrIndex,
       "t11FcSpPoNaWkpDescrFlags": t11FcSpPoNaWkpDescrFlags,
       "t11FcSpPoNaWkpDescrWkpNumber": t11FcSpPoNaWkpDescrWkpNumber,
       "t11FcSpPoNaWkpDescrDestPort": t11FcSpPoNaWkpDescrDestPort,
       "t11FcSpPoNaWkpDescrRowStatus": t11FcSpPoNaWkpDescrRowStatus,
       "t11FcSpPoNaAttribTable": t11FcSpPoNaAttribTable,
       "t11FcSpPoNaAttribEntry": t11FcSpPoNaAttribEntry,
       "t11FcSpPoNaAttribName": t11FcSpPoNaAttribName,
       "t11FcSpPoNaAttribEntryIndex": t11FcSpPoNaAttribEntryIndex,
       "t11FcSpPoNaAttribPartIndex": t11FcSpPoNaAttribPartIndex,
       "t11FcSpPoNaAttribType": t11FcSpPoNaAttribType,
       "t11FcSpPoNaAttribValue": t11FcSpPoNaAttribValue,
       "t11FcSpPoNaAttribExtension": t11FcSpPoNaAttribExtension,
       "t11FcSpPoNaAttribRowStatus": t11FcSpPoNaAttribRowStatus,
       "t11FcSpPoNaAuthProtTable": t11FcSpPoNaAuthProtTable,
       "t11FcSpPoNaAuthProtEntry": t11FcSpPoNaAuthProtEntry,
       "t11FcSpPoNaAuthProtIdentifier": t11FcSpPoNaAuthProtIdentifier,
       "t11FcSpPoNaAuthProtPartIndex": t11FcSpPoNaAuthProtPartIndex,
       "t11FcSpPoNaAuthProtParams": t11FcSpPoNaAuthProtParams,
       "t11FcSpPoNaAuthProtRowStatus": t11FcSpPoNaAuthProtRowStatus,
       "t11FcSpPoStatistics": t11FcSpPoStatistics,
       "t11FcSpPoStatsTable": t11FcSpPoStatsTable,
       "t11FcSpPoStatsEntry": t11FcSpPoStatsEntry,
       "t11FcSpPoInRequests": t11FcSpPoInRequests,
       "t11FcSpPoInAccepts": t11FcSpPoInAccepts,
       "t11FcSpPoInRejects": t11FcSpPoInRejects,
       "t11FcSpPoControl": t11FcSpPoControl,
       "t11FcSpPoServerAddress": t11FcSpPoServerAddress,
       "t11FcSpPoControlTable": t11FcSpPoControlTable,
       "t11FcSpPoControlEntry": t11FcSpPoControlEntry,
       "t11FcSpPoStorageType": t11FcSpPoStorageType,
       "t11FcSpPoNotificationEnable": t11FcSpPoNotificationEnable,
       "t11FcSpPoLastNotifyType": t11FcSpPoLastNotifyType,
       "t11FcSpPoRequestSource": t11FcSpPoRequestSource,
       "t11FcSpPoReasonCode": t11FcSpPoReasonCode,
       "t11FcSpPoCtCommandString": t11FcSpPoCtCommandString,
       "t11FcSpPoReasonCodeExp": t11FcSpPoReasonCodeExp,
       "t11FcSpPoReasonVendorCode": t11FcSpPoReasonVendorCode,
       "t11FcSpPoMIBConformance": t11FcSpPoMIBConformance,
       "t11FcSpPoMIBCompliances": t11FcSpPoMIBCompliances,
       "t11FcSpPoMIBCompliance": t11FcSpPoMIBCompliance,
       "t11FcSpPoMIBGroups": t11FcSpPoMIBGroups,
       "t11FcSpPoActiveObjectsGroup": t11FcSpPoActiveObjectsGroup,
       "t11FcSpPoOperationsObjectsGroup": t11FcSpPoOperationsObjectsGroup,
       "t11FcSpPoNonActiveObjectsGroup": t11FcSpPoNonActiveObjectsGroup,
       "t11FcSpPoStatsObjectsGroup": t11FcSpPoStatsObjectsGroup,
       "t11FcSpPoNotifyObjectsGroup": t11FcSpPoNotifyObjectsGroup,
       "t11FcSpPoNotificationGroup": t11FcSpPoNotificationGroup}
)
