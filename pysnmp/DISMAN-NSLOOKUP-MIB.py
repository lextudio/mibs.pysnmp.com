# SNMP MIB module (DISMAN-NSLOOKUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DISMAN-NSLOOKUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:16 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lookupMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 82)
)
lookupMIB.setRevisions(
        ("2006-06-13 00:00",
         "2000-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LookupObjects_ObjectIdentity = ObjectIdentity
lookupObjects = _LookupObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 82, 1)
)


class _LookupMaxConcurrentRequests_Type(Unsigned32):
    """Custom type lookupMaxConcurrentRequests based on Unsigned32"""
    defaultValue = 10


_LookupMaxConcurrentRequests_Object = MibScalar
lookupMaxConcurrentRequests = _LookupMaxConcurrentRequests_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 1),
    _LookupMaxConcurrentRequests_Type()
)
lookupMaxConcurrentRequests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lookupMaxConcurrentRequests.setStatus("current")
if mibBuilder.loadTexts:
    lookupMaxConcurrentRequests.setUnits("requests")


class _LookupPurgeTime_Type(Unsigned32):
    """Custom type lookupPurgeTime based on Unsigned32"""
    defaultValue = 900

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_LookupPurgeTime_Type.__name__ = "Unsigned32"
_LookupPurgeTime_Object = MibScalar
lookupPurgeTime = _LookupPurgeTime_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 2),
    _LookupPurgeTime_Type()
)
lookupPurgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lookupPurgeTime.setStatus("current")
if mibBuilder.loadTexts:
    lookupPurgeTime.setUnits("seconds")
_LookupCtlTable_Object = MibTable
lookupCtlTable = _LookupCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3)
)
if mibBuilder.loadTexts:
    lookupCtlTable.setStatus("current")
_LookupCtlEntry_Object = MibTableRow
lookupCtlEntry = _LookupCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1)
)
lookupCtlEntry.setIndexNames(
    (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOwnerIndex"),
    (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOperationName"),
)
if mibBuilder.loadTexts:
    lookupCtlEntry.setStatus("current")


class _LookupCtlOwnerIndex_Type(SnmpAdminString):
    """Custom type lookupCtlOwnerIndex based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LookupCtlOwnerIndex_Type.__name__ = "SnmpAdminString"
_LookupCtlOwnerIndex_Object = MibTableColumn
lookupCtlOwnerIndex = _LookupCtlOwnerIndex_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 1),
    _LookupCtlOwnerIndex_Type()
)
lookupCtlOwnerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lookupCtlOwnerIndex.setStatus("current")


class _LookupCtlOperationName_Type(SnmpAdminString):
    """Custom type lookupCtlOperationName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_LookupCtlOperationName_Type.__name__ = "SnmpAdminString"
_LookupCtlOperationName_Object = MibTableColumn
lookupCtlOperationName = _LookupCtlOperationName_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 2),
    _LookupCtlOperationName_Type()
)
lookupCtlOperationName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lookupCtlOperationName.setStatus("current")


class _LookupCtlTargetAddressType_Type(InetAddressType):
    """Custom type lookupCtlTargetAddressType based on InetAddressType"""


_LookupCtlTargetAddressType_Object = MibTableColumn
lookupCtlTargetAddressType = _LookupCtlTargetAddressType_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 3),
    _LookupCtlTargetAddressType_Type()
)
lookupCtlTargetAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lookupCtlTargetAddressType.setStatus("current")
_LookupCtlTargetAddress_Type = InetAddress
_LookupCtlTargetAddress_Object = MibTableColumn
lookupCtlTargetAddress = _LookupCtlTargetAddress_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 4),
    _LookupCtlTargetAddress_Type()
)
lookupCtlTargetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lookupCtlTargetAddress.setStatus("current")


class _LookupCtlOperStatus_Type(Integer32):
    """Custom type lookupCtlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 3),
          ("enabled", 1),
          ("notStarted", 2))
    )


_LookupCtlOperStatus_Type.__name__ = "Integer32"
_LookupCtlOperStatus_Object = MibTableColumn
lookupCtlOperStatus = _LookupCtlOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 5),
    _LookupCtlOperStatus_Type()
)
lookupCtlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookupCtlOperStatus.setStatus("current")
_LookupCtlTime_Type = Unsigned32
_LookupCtlTime_Object = MibTableColumn
lookupCtlTime = _LookupCtlTime_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 6),
    _LookupCtlTime_Type()
)
lookupCtlTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookupCtlTime.setStatus("current")
if mibBuilder.loadTexts:
    lookupCtlTime.setUnits("milliseconds")
_LookupCtlRc_Type = Integer32
_LookupCtlRc_Object = MibTableColumn
lookupCtlRc = _LookupCtlRc_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 7),
    _LookupCtlRc_Type()
)
lookupCtlRc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookupCtlRc.setStatus("current")
_LookupCtlRowStatus_Type = RowStatus
_LookupCtlRowStatus_Object = MibTableColumn
lookupCtlRowStatus = _LookupCtlRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 3, 1, 8),
    _LookupCtlRowStatus_Type()
)
lookupCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lookupCtlRowStatus.setStatus("current")
_LookupResultsTable_Object = MibTable
lookupResultsTable = _LookupResultsTable_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 4)
)
if mibBuilder.loadTexts:
    lookupResultsTable.setStatus("current")
_LookupResultsEntry_Object = MibTableRow
lookupResultsEntry = _LookupResultsEntry_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 4, 1)
)
lookupResultsEntry.setIndexNames(
    (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOwnerIndex"),
    (0, "DISMAN-NSLOOKUP-MIB", "lookupCtlOperationName"),
    (0, "DISMAN-NSLOOKUP-MIB", "lookupResultsIndex"),
)
if mibBuilder.loadTexts:
    lookupResultsEntry.setStatus("current")


class _LookupResultsIndex_Type(Unsigned32):
    """Custom type lookupResultsIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_LookupResultsIndex_Type.__name__ = "Unsigned32"
_LookupResultsIndex_Object = MibTableColumn
lookupResultsIndex = _LookupResultsIndex_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 1),
    _LookupResultsIndex_Type()
)
lookupResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lookupResultsIndex.setStatus("current")
_LookupResultsAddressType_Type = InetAddressType
_LookupResultsAddressType_Object = MibTableColumn
lookupResultsAddressType = _LookupResultsAddressType_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 2),
    _LookupResultsAddressType_Type()
)
lookupResultsAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookupResultsAddressType.setStatus("current")
_LookupResultsAddress_Type = InetAddress
_LookupResultsAddress_Object = MibTableColumn
lookupResultsAddress = _LookupResultsAddress_Object(
    (1, 3, 6, 1, 2, 1, 82, 1, 4, 1, 3),
    _LookupResultsAddress_Type()
)
lookupResultsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lookupResultsAddress.setStatus("current")
_LookupConformance_ObjectIdentity = ObjectIdentity
lookupConformance = _LookupConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 82, 2)
)
_LookupCompliances_ObjectIdentity = ObjectIdentity
lookupCompliances = _LookupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 82, 2, 1)
)
_LookupGroups_ObjectIdentity = ObjectIdentity
lookupGroups = _LookupGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 82, 2, 2)
)

# Managed Objects groups

lookupGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 82, 2, 2, 1)
)
lookupGroup.setObjects(
      *(("DISMAN-NSLOOKUP-MIB", "lookupMaxConcurrentRequests"),
        ("DISMAN-NSLOOKUP-MIB", "lookupPurgeTime"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlOperStatus"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlTargetAddressType"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlTargetAddress"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlTime"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlRc"),
        ("DISMAN-NSLOOKUP-MIB", "lookupCtlRowStatus"),
        ("DISMAN-NSLOOKUP-MIB", "lookupResultsAddressType"),
        ("DISMAN-NSLOOKUP-MIB", "lookupResultsAddress"))
)
if mibBuilder.loadTexts:
    lookupGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lookupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 82, 2, 1, 1)
)
if mibBuilder.loadTexts:
    lookupCompliance.setStatus(
        "current"
    )

lookupMinimumCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 82, 2, 1, 2)
)
if mibBuilder.loadTexts:
    lookupMinimumCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DISMAN-NSLOOKUP-MIB",
    **{"lookupMIB": lookupMIB,
       "lookupObjects": lookupObjects,
       "lookupMaxConcurrentRequests": lookupMaxConcurrentRequests,
       "lookupPurgeTime": lookupPurgeTime,
       "lookupCtlTable": lookupCtlTable,
       "lookupCtlEntry": lookupCtlEntry,
       "lookupCtlOwnerIndex": lookupCtlOwnerIndex,
       "lookupCtlOperationName": lookupCtlOperationName,
       "lookupCtlTargetAddressType": lookupCtlTargetAddressType,
       "lookupCtlTargetAddress": lookupCtlTargetAddress,
       "lookupCtlOperStatus": lookupCtlOperStatus,
       "lookupCtlTime": lookupCtlTime,
       "lookupCtlRc": lookupCtlRc,
       "lookupCtlRowStatus": lookupCtlRowStatus,
       "lookupResultsTable": lookupResultsTable,
       "lookupResultsEntry": lookupResultsEntry,
       "lookupResultsIndex": lookupResultsIndex,
       "lookupResultsAddressType": lookupResultsAddressType,
       "lookupResultsAddress": lookupResultsAddress,
       "lookupConformance": lookupConformance,
       "lookupCompliances": lookupCompliances,
       "lookupCompliance": lookupCompliance,
       "lookupMinimumCompliance": lookupMinimumCompliance,
       "lookupGroups": lookupGroups,
       "lookupGroup": lookupGroup}
)
