# SNMP MIB module (RDBMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RDBMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:37 2024
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

(applGroups,
 applIndex) = mibBuilder.importSymbols(
    "NETWORK-SERVICES-MIB",
    "applGroups",
    "applIndex")

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
 DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rdbmsMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdbmsObjects_ObjectIdentity = ObjectIdentity
rdbmsObjects = _RdbmsObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 1)
)
_RdbmsDbTable_Object = MibTable
rdbmsDbTable = _RdbmsDbTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1)
)
if mibBuilder.loadTexts:
    rdbmsDbTable.setStatus("current")
_RdbmsDbEntry_Object = MibTableRow
rdbmsDbEntry = _RdbmsDbEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1)
)
rdbmsDbEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    rdbmsDbEntry.setStatus("current")


class _RdbmsDbIndex_Type(Integer32):
    """Custom type rdbmsDbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbIndex_Type.__name__ = "Integer32"
_RdbmsDbIndex_Object = MibTableColumn
rdbmsDbIndex = _RdbmsDbIndex_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 1),
    _RdbmsDbIndex_Type()
)
rdbmsDbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsDbIndex.setStatus("current")
_RdbmsDbPrivateMibOID_Type = ObjectIdentifier
_RdbmsDbPrivateMibOID_Object = MibTableColumn
rdbmsDbPrivateMibOID = _RdbmsDbPrivateMibOID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 2),
    _RdbmsDbPrivateMibOID_Type()
)
rdbmsDbPrivateMibOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbPrivateMibOID.setStatus("current")
_RdbmsDbVendorName_Type = DisplayString
_RdbmsDbVendorName_Object = MibTableColumn
rdbmsDbVendorName = _RdbmsDbVendorName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 3),
    _RdbmsDbVendorName_Type()
)
rdbmsDbVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbVendorName.setStatus("current")
_RdbmsDbName_Type = DisplayString
_RdbmsDbName_Object = MibTableColumn
rdbmsDbName = _RdbmsDbName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 4),
    _RdbmsDbName_Type()
)
rdbmsDbName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbName.setStatus("current")
_RdbmsDbContact_Type = DisplayString
_RdbmsDbContact_Object = MibTableColumn
rdbmsDbContact = _RdbmsDbContact_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 1, 1, 5),
    _RdbmsDbContact_Type()
)
rdbmsDbContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbContact.setStatus("current")
_RdbmsDbInfoTable_Object = MibTable
rdbmsDbInfoTable = _RdbmsDbInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2)
)
if mibBuilder.loadTexts:
    rdbmsDbInfoTable.setStatus("current")
_RdbmsDbInfoEntry_Object = MibTableRow
rdbmsDbInfoEntry = _RdbmsDbInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1)
)
rdbmsDbInfoEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
)
if mibBuilder.loadTexts:
    rdbmsDbInfoEntry.setStatus("current")
_RdbmsDbInfoProductName_Type = DisplayString
_RdbmsDbInfoProductName_Object = MibTableColumn
rdbmsDbInfoProductName = _RdbmsDbInfoProductName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 1),
    _RdbmsDbInfoProductName_Type()
)
rdbmsDbInfoProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbInfoProductName.setStatus("current")
_RdbmsDbInfoVersion_Type = DisplayString
_RdbmsDbInfoVersion_Object = MibTableColumn
rdbmsDbInfoVersion = _RdbmsDbInfoVersion_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 2),
    _RdbmsDbInfoVersion_Type()
)
rdbmsDbInfoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbInfoVersion.setStatus("current")


class _RdbmsDbInfoSizeUnits_Type(Integer32):
    """Custom type rdbmsDbInfoSizeUnits based on Integer32"""
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
        *(("bytes", 1),
          ("gbytes", 4),
          ("kbytes", 2),
          ("mbytes", 3),
          ("tbytes", 5))
    )


_RdbmsDbInfoSizeUnits_Type.__name__ = "Integer32"
_RdbmsDbInfoSizeUnits_Object = MibTableColumn
rdbmsDbInfoSizeUnits = _RdbmsDbInfoSizeUnits_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 3),
    _RdbmsDbInfoSizeUnits_Type()
)
rdbmsDbInfoSizeUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbInfoSizeUnits.setStatus("current")


class _RdbmsDbInfoSizeAllocated_Type(Integer32):
    """Custom type rdbmsDbInfoSizeAllocated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbInfoSizeAllocated_Type.__name__ = "Integer32"
_RdbmsDbInfoSizeAllocated_Object = MibTableColumn
rdbmsDbInfoSizeAllocated = _RdbmsDbInfoSizeAllocated_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 4),
    _RdbmsDbInfoSizeAllocated_Type()
)
rdbmsDbInfoSizeAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbInfoSizeAllocated.setStatus("current")


class _RdbmsDbInfoSizeUsed_Type(Integer32):
    """Custom type rdbmsDbInfoSizeUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbInfoSizeUsed_Type.__name__ = "Integer32"
_RdbmsDbInfoSizeUsed_Object = MibTableColumn
rdbmsDbInfoSizeUsed = _RdbmsDbInfoSizeUsed_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 5),
    _RdbmsDbInfoSizeUsed_Type()
)
rdbmsDbInfoSizeUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbInfoSizeUsed.setStatus("current")
_RdbmsDbInfoLastBackup_Type = DateAndTime
_RdbmsDbInfoLastBackup_Object = MibTableColumn
rdbmsDbInfoLastBackup = _RdbmsDbInfoLastBackup_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 2, 1, 6),
    _RdbmsDbInfoLastBackup_Type()
)
rdbmsDbInfoLastBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbInfoLastBackup.setStatus("current")
_RdbmsDbParamTable_Object = MibTable
rdbmsDbParamTable = _RdbmsDbParamTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3)
)
if mibBuilder.loadTexts:
    rdbmsDbParamTable.setStatus("current")
_RdbmsDbParamEntry_Object = MibTableRow
rdbmsDbParamEntry = _RdbmsDbParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1)
)
rdbmsDbParamEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "RDBMS-MIB", "rdbmsDbParamName"),
    (0, "RDBMS-MIB", "rdbmsDbParamSubIndex"),
)
if mibBuilder.loadTexts:
    rdbmsDbParamEntry.setStatus("current")


class _RdbmsDbParamName_Type(DisplayString):
    """Custom type rdbmsDbParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RdbmsDbParamName_Type.__name__ = "DisplayString"
_RdbmsDbParamName_Object = MibTableColumn
rdbmsDbParamName = _RdbmsDbParamName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 1),
    _RdbmsDbParamName_Type()
)
rdbmsDbParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsDbParamName.setStatus("current")


class _RdbmsDbParamSubIndex_Type(Integer32):
    """Custom type rdbmsDbParamSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbParamSubIndex_Type.__name__ = "Integer32"
_RdbmsDbParamSubIndex_Object = MibTableColumn
rdbmsDbParamSubIndex = _RdbmsDbParamSubIndex_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 2),
    _RdbmsDbParamSubIndex_Type()
)
rdbmsDbParamSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsDbParamSubIndex.setStatus("current")
_RdbmsDbParamID_Type = AutonomousType
_RdbmsDbParamID_Object = MibTableColumn
rdbmsDbParamID = _RdbmsDbParamID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 3),
    _RdbmsDbParamID_Type()
)
rdbmsDbParamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbParamID.setStatus("current")
_RdbmsDbParamCurrValue_Type = DisplayString
_RdbmsDbParamCurrValue_Object = MibTableColumn
rdbmsDbParamCurrValue = _RdbmsDbParamCurrValue_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 4),
    _RdbmsDbParamCurrValue_Type()
)
rdbmsDbParamCurrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbParamCurrValue.setStatus("current")
_RdbmsDbParamComment_Type = DisplayString
_RdbmsDbParamComment_Object = MibTableColumn
rdbmsDbParamComment = _RdbmsDbParamComment_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 3, 1, 5),
    _RdbmsDbParamComment_Type()
)
rdbmsDbParamComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbParamComment.setStatus("current")
_RdbmsDbLimitedResourceTable_Object = MibTable
rdbmsDbLimitedResourceTable = _RdbmsDbLimitedResourceTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4)
)
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceTable.setStatus("current")
_RdbmsDbLimitedResourceEntry_Object = MibTableRow
rdbmsDbLimitedResourceEntry = _RdbmsDbLimitedResourceEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1)
)
rdbmsDbLimitedResourceEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "RDBMS-MIB", "rdbmsDbLimitedResourceName"),
)
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceEntry.setStatus("current")
_RdbmsDbLimitedResourceName_Type = DisplayString
_RdbmsDbLimitedResourceName_Object = MibTableColumn
rdbmsDbLimitedResourceName = _RdbmsDbLimitedResourceName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 1),
    _RdbmsDbLimitedResourceName_Type()
)
rdbmsDbLimitedResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceName.setStatus("current")
_RdbmsDbLimitedResourceID_Type = AutonomousType
_RdbmsDbLimitedResourceID_Object = MibTableColumn
rdbmsDbLimitedResourceID = _RdbmsDbLimitedResourceID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 2),
    _RdbmsDbLimitedResourceID_Type()
)
rdbmsDbLimitedResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceID.setStatus("current")


class _RdbmsDbLimitedResourceLimit_Type(Integer32):
    """Custom type rdbmsDbLimitedResourceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbLimitedResourceLimit_Type.__name__ = "Integer32"
_RdbmsDbLimitedResourceLimit_Object = MibTableColumn
rdbmsDbLimitedResourceLimit = _RdbmsDbLimitedResourceLimit_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 3),
    _RdbmsDbLimitedResourceLimit_Type()
)
rdbmsDbLimitedResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceLimit.setStatus("current")


class _RdbmsDbLimitedResourceCurrent_Type(Integer32):
    """Custom type rdbmsDbLimitedResourceCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbLimitedResourceCurrent_Type.__name__ = "Integer32"
_RdbmsDbLimitedResourceCurrent_Object = MibTableColumn
rdbmsDbLimitedResourceCurrent = _RdbmsDbLimitedResourceCurrent_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 4),
    _RdbmsDbLimitedResourceCurrent_Type()
)
rdbmsDbLimitedResourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceCurrent.setStatus("current")


class _RdbmsDbLimitedResourceHighwater_Type(Integer32):
    """Custom type rdbmsDbLimitedResourceHighwater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsDbLimitedResourceHighwater_Type.__name__ = "Integer32"
_RdbmsDbLimitedResourceHighwater_Object = MibTableColumn
rdbmsDbLimitedResourceHighwater = _RdbmsDbLimitedResourceHighwater_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 5),
    _RdbmsDbLimitedResourceHighwater_Type()
)
rdbmsDbLimitedResourceHighwater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceHighwater.setStatus("current")
_RdbmsDbLimitedResourceFailures_Type = Counter32
_RdbmsDbLimitedResourceFailures_Object = MibTableColumn
rdbmsDbLimitedResourceFailures = _RdbmsDbLimitedResourceFailures_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 6),
    _RdbmsDbLimitedResourceFailures_Type()
)
rdbmsDbLimitedResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceFailures.setStatus("current")
_RdbmsDbLimitedResourceDescription_Type = DisplayString
_RdbmsDbLimitedResourceDescription_Object = MibTableColumn
rdbmsDbLimitedResourceDescription = _RdbmsDbLimitedResourceDescription_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 4, 1, 7),
    _RdbmsDbLimitedResourceDescription_Type()
)
rdbmsDbLimitedResourceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsDbLimitedResourceDescription.setStatus("current")
_RdbmsSrvTable_Object = MibTable
rdbmsSrvTable = _RdbmsSrvTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5)
)
if mibBuilder.loadTexts:
    rdbmsSrvTable.setStatus("current")
_RdbmsSrvEntry_Object = MibTableRow
rdbmsSrvEntry = _RdbmsSrvEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5, 1)
)
rdbmsSrvEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    rdbmsSrvEntry.setStatus("current")
_RdbmsSrvPrivateMibOID_Type = ObjectIdentifier
_RdbmsSrvPrivateMibOID_Object = MibTableColumn
rdbmsSrvPrivateMibOID = _RdbmsSrvPrivateMibOID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 1),
    _RdbmsSrvPrivateMibOID_Type()
)
rdbmsSrvPrivateMibOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvPrivateMibOID.setStatus("current")
_RdbmsSrvVendorName_Type = DisplayString
_RdbmsSrvVendorName_Object = MibTableColumn
rdbmsSrvVendorName = _RdbmsSrvVendorName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 2),
    _RdbmsSrvVendorName_Type()
)
rdbmsSrvVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvVendorName.setStatus("current")
_RdbmsSrvProductName_Type = DisplayString
_RdbmsSrvProductName_Object = MibTableColumn
rdbmsSrvProductName = _RdbmsSrvProductName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 3),
    _RdbmsSrvProductName_Type()
)
rdbmsSrvProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvProductName.setStatus("current")
_RdbmsSrvContact_Type = DisplayString
_RdbmsSrvContact_Object = MibTableColumn
rdbmsSrvContact = _RdbmsSrvContact_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 5, 1, 4),
    _RdbmsSrvContact_Type()
)
rdbmsSrvContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvContact.setStatus("current")
_RdbmsSrvInfoTable_Object = MibTable
rdbmsSrvInfoTable = _RdbmsSrvInfoTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6)
)
if mibBuilder.loadTexts:
    rdbmsSrvInfoTable.setStatus("current")
_RdbmsSrvInfoEntry_Object = MibTableRow
rdbmsSrvInfoEntry = _RdbmsSrvInfoEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1)
)
rdbmsSrvInfoEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    rdbmsSrvInfoEntry.setStatus("current")
_RdbmsSrvInfoStartupTime_Type = DateAndTime
_RdbmsSrvInfoStartupTime_Object = MibTableColumn
rdbmsSrvInfoStartupTime = _RdbmsSrvInfoStartupTime_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 1),
    _RdbmsSrvInfoStartupTime_Type()
)
rdbmsSrvInfoStartupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoStartupTime.setStatus("current")
_RdbmsSrvInfoFinishedTransactions_Type = Gauge32
_RdbmsSrvInfoFinishedTransactions_Object = MibTableColumn
rdbmsSrvInfoFinishedTransactions = _RdbmsSrvInfoFinishedTransactions_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 2),
    _RdbmsSrvInfoFinishedTransactions_Type()
)
rdbmsSrvInfoFinishedTransactions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoFinishedTransactions.setStatus("current")
_RdbmsSrvInfoDiskReads_Type = Counter32
_RdbmsSrvInfoDiskReads_Object = MibTableColumn
rdbmsSrvInfoDiskReads = _RdbmsSrvInfoDiskReads_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 3),
    _RdbmsSrvInfoDiskReads_Type()
)
rdbmsSrvInfoDiskReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoDiskReads.setStatus("current")
_RdbmsSrvInfoLogicalReads_Type = Counter32
_RdbmsSrvInfoLogicalReads_Object = MibTableColumn
rdbmsSrvInfoLogicalReads = _RdbmsSrvInfoLogicalReads_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 4),
    _RdbmsSrvInfoLogicalReads_Type()
)
rdbmsSrvInfoLogicalReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoLogicalReads.setStatus("current")
_RdbmsSrvInfoDiskWrites_Type = Counter32
_RdbmsSrvInfoDiskWrites_Object = MibTableColumn
rdbmsSrvInfoDiskWrites = _RdbmsSrvInfoDiskWrites_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 5),
    _RdbmsSrvInfoDiskWrites_Type()
)
rdbmsSrvInfoDiskWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoDiskWrites.setStatus("current")
_RdbmsSrvInfoLogicalWrites_Type = Counter32
_RdbmsSrvInfoLogicalWrites_Object = MibTableColumn
rdbmsSrvInfoLogicalWrites = _RdbmsSrvInfoLogicalWrites_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 6),
    _RdbmsSrvInfoLogicalWrites_Type()
)
rdbmsSrvInfoLogicalWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoLogicalWrites.setStatus("current")
_RdbmsSrvInfoPageReads_Type = Counter32
_RdbmsSrvInfoPageReads_Object = MibTableColumn
rdbmsSrvInfoPageReads = _RdbmsSrvInfoPageReads_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 7),
    _RdbmsSrvInfoPageReads_Type()
)
rdbmsSrvInfoPageReads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoPageReads.setStatus("current")
_RdbmsSrvInfoPageWrites_Type = Counter32
_RdbmsSrvInfoPageWrites_Object = MibTableColumn
rdbmsSrvInfoPageWrites = _RdbmsSrvInfoPageWrites_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 8),
    _RdbmsSrvInfoPageWrites_Type()
)
rdbmsSrvInfoPageWrites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoPageWrites.setStatus("current")
_RdbmsSrvInfoDiskOutOfSpaces_Type = Counter32
_RdbmsSrvInfoDiskOutOfSpaces_Object = MibTableColumn
rdbmsSrvInfoDiskOutOfSpaces = _RdbmsSrvInfoDiskOutOfSpaces_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 9),
    _RdbmsSrvInfoDiskOutOfSpaces_Type()
)
rdbmsSrvInfoDiskOutOfSpaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoDiskOutOfSpaces.setStatus("current")
_RdbmsSrvInfoHandledRequests_Type = Counter32
_RdbmsSrvInfoHandledRequests_Object = MibTableColumn
rdbmsSrvInfoHandledRequests = _RdbmsSrvInfoHandledRequests_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 10),
    _RdbmsSrvInfoHandledRequests_Type()
)
rdbmsSrvInfoHandledRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoHandledRequests.setStatus("current")
_RdbmsSrvInfoRequestRecvs_Type = Counter32
_RdbmsSrvInfoRequestRecvs_Object = MibTableColumn
rdbmsSrvInfoRequestRecvs = _RdbmsSrvInfoRequestRecvs_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 11),
    _RdbmsSrvInfoRequestRecvs_Type()
)
rdbmsSrvInfoRequestRecvs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoRequestRecvs.setStatus("current")
_RdbmsSrvInfoRequestSends_Type = Counter32
_RdbmsSrvInfoRequestSends_Object = MibTableColumn
rdbmsSrvInfoRequestSends = _RdbmsSrvInfoRequestSends_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 12),
    _RdbmsSrvInfoRequestSends_Type()
)
rdbmsSrvInfoRequestSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoRequestSends.setStatus("current")
_RdbmsSrvInfoHighwaterInboundAssociations_Type = Gauge32
_RdbmsSrvInfoHighwaterInboundAssociations_Object = MibTableColumn
rdbmsSrvInfoHighwaterInboundAssociations = _RdbmsSrvInfoHighwaterInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 13),
    _RdbmsSrvInfoHighwaterInboundAssociations_Type()
)
rdbmsSrvInfoHighwaterInboundAssociations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvInfoHighwaterInboundAssociations.setStatus("current")
_RdbmsSrvInfoMaxInboundAssociations_Type = Gauge32
_RdbmsSrvInfoMaxInboundAssociations_Object = MibTableColumn
rdbmsSrvInfoMaxInboundAssociations = _RdbmsSrvInfoMaxInboundAssociations_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 6, 1, 14),
    _RdbmsSrvInfoMaxInboundAssociations_Type()
)
rdbmsSrvInfoMaxInboundAssociations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvInfoMaxInboundAssociations.setStatus("current")
_RdbmsSrvParamTable_Object = MibTable
rdbmsSrvParamTable = _RdbmsSrvParamTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7)
)
if mibBuilder.loadTexts:
    rdbmsSrvParamTable.setStatus("current")
_RdbmsSrvParamEntry_Object = MibTableRow
rdbmsSrvParamEntry = _RdbmsSrvParamEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1)
)
rdbmsSrvParamEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "RDBMS-MIB", "rdbmsSrvParamName"),
    (0, "RDBMS-MIB", "rdbmsSrvParamSubIndex"),
)
if mibBuilder.loadTexts:
    rdbmsSrvParamEntry.setStatus("current")


class _RdbmsSrvParamName_Type(DisplayString):
    """Custom type rdbmsSrvParamName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_RdbmsSrvParamName_Type.__name__ = "DisplayString"
_RdbmsSrvParamName_Object = MibTableColumn
rdbmsSrvParamName = _RdbmsSrvParamName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 1),
    _RdbmsSrvParamName_Type()
)
rdbmsSrvParamName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsSrvParamName.setStatus("current")


class _RdbmsSrvParamSubIndex_Type(Integer32):
    """Custom type rdbmsSrvParamSubIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsSrvParamSubIndex_Type.__name__ = "Integer32"
_RdbmsSrvParamSubIndex_Object = MibTableColumn
rdbmsSrvParamSubIndex = _RdbmsSrvParamSubIndex_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 2),
    _RdbmsSrvParamSubIndex_Type()
)
rdbmsSrvParamSubIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsSrvParamSubIndex.setStatus("current")
_RdbmsSrvParamID_Type = AutonomousType
_RdbmsSrvParamID_Object = MibTableColumn
rdbmsSrvParamID = _RdbmsSrvParamID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 3),
    _RdbmsSrvParamID_Type()
)
rdbmsSrvParamID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvParamID.setStatus("current")
_RdbmsSrvParamCurrValue_Type = DisplayString
_RdbmsSrvParamCurrValue_Object = MibTableColumn
rdbmsSrvParamCurrValue = _RdbmsSrvParamCurrValue_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 4),
    _RdbmsSrvParamCurrValue_Type()
)
rdbmsSrvParamCurrValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvParamCurrValue.setStatus("current")
_RdbmsSrvParamComment_Type = DisplayString
_RdbmsSrvParamComment_Object = MibTableColumn
rdbmsSrvParamComment = _RdbmsSrvParamComment_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 7, 1, 5),
    _RdbmsSrvParamComment_Type()
)
rdbmsSrvParamComment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvParamComment.setStatus("current")
_RdbmsSrvLimitedResourceTable_Object = MibTable
rdbmsSrvLimitedResourceTable = _RdbmsSrvLimitedResourceTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8)
)
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceTable.setStatus("current")
_RdbmsSrvLimitedResourceEntry_Object = MibTableRow
rdbmsSrvLimitedResourceEntry = _RdbmsSrvLimitedResourceEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1)
)
rdbmsSrvLimitedResourceEntry.setIndexNames(
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
    (0, "RDBMS-MIB", "rdbmsSrvLimitedResourceName"),
)
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceEntry.setStatus("current")
_RdbmsSrvLimitedResourceName_Type = DisplayString
_RdbmsSrvLimitedResourceName_Object = MibTableColumn
rdbmsSrvLimitedResourceName = _RdbmsSrvLimitedResourceName_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 1),
    _RdbmsSrvLimitedResourceName_Type()
)
rdbmsSrvLimitedResourceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceName.setStatus("current")
_RdbmsSrvLimitedResourceID_Type = AutonomousType
_RdbmsSrvLimitedResourceID_Object = MibTableColumn
rdbmsSrvLimitedResourceID = _RdbmsSrvLimitedResourceID_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 2),
    _RdbmsSrvLimitedResourceID_Type()
)
rdbmsSrvLimitedResourceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceID.setStatus("current")


class _RdbmsSrvLimitedResourceLimit_Type(Integer32):
    """Custom type rdbmsSrvLimitedResourceLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsSrvLimitedResourceLimit_Type.__name__ = "Integer32"
_RdbmsSrvLimitedResourceLimit_Object = MibTableColumn
rdbmsSrvLimitedResourceLimit = _RdbmsSrvLimitedResourceLimit_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 3),
    _RdbmsSrvLimitedResourceLimit_Type()
)
rdbmsSrvLimitedResourceLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceLimit.setStatus("current")


class _RdbmsSrvLimitedResourceCurrent_Type(Integer32):
    """Custom type rdbmsSrvLimitedResourceCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsSrvLimitedResourceCurrent_Type.__name__ = "Integer32"
_RdbmsSrvLimitedResourceCurrent_Object = MibTableColumn
rdbmsSrvLimitedResourceCurrent = _RdbmsSrvLimitedResourceCurrent_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 4),
    _RdbmsSrvLimitedResourceCurrent_Type()
)
rdbmsSrvLimitedResourceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceCurrent.setStatus("current")


class _RdbmsSrvLimitedResourceHighwater_Type(Integer32):
    """Custom type rdbmsSrvLimitedResourceHighwater based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RdbmsSrvLimitedResourceHighwater_Type.__name__ = "Integer32"
_RdbmsSrvLimitedResourceHighwater_Object = MibTableColumn
rdbmsSrvLimitedResourceHighwater = _RdbmsSrvLimitedResourceHighwater_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 5),
    _RdbmsSrvLimitedResourceHighwater_Type()
)
rdbmsSrvLimitedResourceHighwater.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceHighwater.setStatus("current")
_RdbmsSrvLimitedResourceFailures_Type = Counter32
_RdbmsSrvLimitedResourceFailures_Object = MibTableColumn
rdbmsSrvLimitedResourceFailures = _RdbmsSrvLimitedResourceFailures_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 6),
    _RdbmsSrvLimitedResourceFailures_Type()
)
rdbmsSrvLimitedResourceFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceFailures.setStatus("current")
_RdbmsSrvLimitedResourceDescription_Type = DisplayString
_RdbmsSrvLimitedResourceDescription_Object = MibTableColumn
rdbmsSrvLimitedResourceDescription = _RdbmsSrvLimitedResourceDescription_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 8, 1, 7),
    _RdbmsSrvLimitedResourceDescription_Type()
)
rdbmsSrvLimitedResourceDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdbmsSrvLimitedResourceDescription.setStatus("current")
_RdbmsRelTable_Object = MibTable
rdbmsRelTable = _RdbmsRelTable_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 9)
)
if mibBuilder.loadTexts:
    rdbmsRelTable.setStatus("current")
_RdbmsRelEntry_Object = MibTableRow
rdbmsRelEntry = _RdbmsRelEntry_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 9, 1)
)
rdbmsRelEntry.setIndexNames(
    (0, "RDBMS-MIB", "rdbmsDbIndex"),
    (0, "NETWORK-SERVICES-MIB", "applIndex"),
)
if mibBuilder.loadTexts:
    rdbmsRelEntry.setStatus("current")


class _RdbmsRelState_Type(Integer32):
    """Custom type rdbmsRelState based on Integer32"""
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
        *(("active", 2),
          ("available", 3),
          ("other", 1),
          ("restricted", 4),
          ("unavailable", 5))
    )


_RdbmsRelState_Type.__name__ = "Integer32"
_RdbmsRelState_Object = MibTableColumn
rdbmsRelState = _RdbmsRelState_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 9, 1, 1),
    _RdbmsRelState_Type()
)
rdbmsRelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsRelState.setStatus("current")
_RdbmsRelActiveTime_Type = DateAndTime
_RdbmsRelActiveTime_Object = MibTableColumn
rdbmsRelActiveTime = _RdbmsRelActiveTime_Object(
    (1, 3, 6, 1, 2, 1, 39, 1, 9, 1, 2),
    _RdbmsRelActiveTime_Type()
)
rdbmsRelActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdbmsRelActiveTime.setStatus("current")
_RdbmsWellKnownLimitedResources_ObjectIdentity = ObjectIdentity
rdbmsWellKnownLimitedResources = _RdbmsWellKnownLimitedResources_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 1, 10)
)
_RdbmsLogSpace_ObjectIdentity = ObjectIdentity
rdbmsLogSpace = _RdbmsLogSpace_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 1, 10, 1)
)
if mibBuilder.loadTexts:
    rdbmsLogSpace.setStatus("current")
_RdbmsTraps_ObjectIdentity = ObjectIdentity
rdbmsTraps = _RdbmsTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 2)
)
_RdbmsConformance_ObjectIdentity = ObjectIdentity
rdbmsConformance = _RdbmsConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 3)
)
_RdbmsCompliances_ObjectIdentity = ObjectIdentity
rdbmsCompliances = _RdbmsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 3, 1)
)
_RdbmsGroups_ObjectIdentity = ObjectIdentity
rdbmsGroups = _RdbmsGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 39, 3, 2)
)

# Managed Objects groups

rdbmsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 39, 3, 2, 1)
)
rdbmsGroup.setObjects(
      *(("RDBMS-MIB", "rdbmsDbPrivateMibOID"),
        ("RDBMS-MIB", "rdbmsDbVendorName"),
        ("RDBMS-MIB", "rdbmsDbName"),
        ("RDBMS-MIB", "rdbmsDbContact"),
        ("RDBMS-MIB", "rdbmsDbInfoProductName"),
        ("RDBMS-MIB", "rdbmsDbInfoVersion"),
        ("RDBMS-MIB", "rdbmsDbInfoSizeUnits"),
        ("RDBMS-MIB", "rdbmsDbInfoSizeAllocated"),
        ("RDBMS-MIB", "rdbmsDbInfoSizeUsed"),
        ("RDBMS-MIB", "rdbmsDbInfoLastBackup"),
        ("RDBMS-MIB", "rdbmsDbParamCurrValue"),
        ("RDBMS-MIB", "rdbmsDbParamComment"),
        ("RDBMS-MIB", "rdbmsDbLimitedResourceLimit"),
        ("RDBMS-MIB", "rdbmsDbLimitedResourceCurrent"),
        ("RDBMS-MIB", "rdbmsDbLimitedResourceHighwater"),
        ("RDBMS-MIB", "rdbmsDbLimitedResourceFailures"),
        ("RDBMS-MIB", "rdbmsDbLimitedResourceDescription"),
        ("RDBMS-MIB", "rdbmsSrvPrivateMibOID"),
        ("RDBMS-MIB", "rdbmsSrvVendorName"),
        ("RDBMS-MIB", "rdbmsSrvProductName"),
        ("RDBMS-MIB", "rdbmsSrvContact"),
        ("RDBMS-MIB", "rdbmsSrvInfoStartupTime"),
        ("RDBMS-MIB", "rdbmsSrvInfoFinishedTransactions"),
        ("RDBMS-MIB", "rdbmsSrvInfoDiskReads"),
        ("RDBMS-MIB", "rdbmsSrvInfoDiskWrites"),
        ("RDBMS-MIB", "rdbmsSrvInfoLogicalReads"),
        ("RDBMS-MIB", "rdbmsSrvInfoLogicalWrites"),
        ("RDBMS-MIB", "rdbmsSrvInfoPageReads"),
        ("RDBMS-MIB", "rdbmsSrvInfoPageWrites"),
        ("RDBMS-MIB", "rdbmsSrvInfoHandledRequests"),
        ("RDBMS-MIB", "rdbmsSrvInfoRequestRecvs"),
        ("RDBMS-MIB", "rdbmsSrvInfoRequestSends"),
        ("RDBMS-MIB", "rdbmsSrvInfoHighwaterInboundAssociations"),
        ("RDBMS-MIB", "rdbmsSrvInfoMaxInboundAssociations"),
        ("RDBMS-MIB", "rdbmsSrvParamCurrValue"),
        ("RDBMS-MIB", "rdbmsSrvParamComment"),
        ("RDBMS-MIB", "rdbmsSrvLimitedResourceLimit"),
        ("RDBMS-MIB", "rdbmsSrvLimitedResourceCurrent"),
        ("RDBMS-MIB", "rdbmsSrvLimitedResourceHighwater"),
        ("RDBMS-MIB", "rdbmsSrvLimitedResourceFailures"),
        ("RDBMS-MIB", "rdbmsSrvLimitedResourceDescription"),
        ("RDBMS-MIB", "rdbmsRelState"),
        ("RDBMS-MIB", "rdbmsRelActiveTime"))
)
if mibBuilder.loadTexts:
    rdbmsGroup.setStatus("current")


# Notification objects

rdbmsStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 39, 2, 1)
)
rdbmsStateChange.setObjects(
    ("RDBMS-MIB", "rdbmsRelState")
)
if mibBuilder.loadTexts:
    rdbmsStateChange.setStatus(
        "current"
    )

rdbmsOutOfSpace = NotificationType(
    (1, 3, 6, 1, 2, 1, 39, 2, 2)
)
rdbmsOutOfSpace.setObjects(
    ("RDBMS-MIB", "rdbmsSrvInfoDiskOutOfSpaces")
)
if mibBuilder.loadTexts:
    rdbmsOutOfSpace.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

rdbmsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 39, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rdbmsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDBMS-MIB",
    **{"rdbmsMIB": rdbmsMIB,
       "rdbmsObjects": rdbmsObjects,
       "rdbmsDbTable": rdbmsDbTable,
       "rdbmsDbEntry": rdbmsDbEntry,
       "rdbmsDbIndex": rdbmsDbIndex,
       "rdbmsDbPrivateMibOID": rdbmsDbPrivateMibOID,
       "rdbmsDbVendorName": rdbmsDbVendorName,
       "rdbmsDbName": rdbmsDbName,
       "rdbmsDbContact": rdbmsDbContact,
       "rdbmsDbInfoTable": rdbmsDbInfoTable,
       "rdbmsDbInfoEntry": rdbmsDbInfoEntry,
       "rdbmsDbInfoProductName": rdbmsDbInfoProductName,
       "rdbmsDbInfoVersion": rdbmsDbInfoVersion,
       "rdbmsDbInfoSizeUnits": rdbmsDbInfoSizeUnits,
       "rdbmsDbInfoSizeAllocated": rdbmsDbInfoSizeAllocated,
       "rdbmsDbInfoSizeUsed": rdbmsDbInfoSizeUsed,
       "rdbmsDbInfoLastBackup": rdbmsDbInfoLastBackup,
       "rdbmsDbParamTable": rdbmsDbParamTable,
       "rdbmsDbParamEntry": rdbmsDbParamEntry,
       "rdbmsDbParamName": rdbmsDbParamName,
       "rdbmsDbParamSubIndex": rdbmsDbParamSubIndex,
       "rdbmsDbParamID": rdbmsDbParamID,
       "rdbmsDbParamCurrValue": rdbmsDbParamCurrValue,
       "rdbmsDbParamComment": rdbmsDbParamComment,
       "rdbmsDbLimitedResourceTable": rdbmsDbLimitedResourceTable,
       "rdbmsDbLimitedResourceEntry": rdbmsDbLimitedResourceEntry,
       "rdbmsDbLimitedResourceName": rdbmsDbLimitedResourceName,
       "rdbmsDbLimitedResourceID": rdbmsDbLimitedResourceID,
       "rdbmsDbLimitedResourceLimit": rdbmsDbLimitedResourceLimit,
       "rdbmsDbLimitedResourceCurrent": rdbmsDbLimitedResourceCurrent,
       "rdbmsDbLimitedResourceHighwater": rdbmsDbLimitedResourceHighwater,
       "rdbmsDbLimitedResourceFailures": rdbmsDbLimitedResourceFailures,
       "rdbmsDbLimitedResourceDescription": rdbmsDbLimitedResourceDescription,
       "rdbmsSrvTable": rdbmsSrvTable,
       "rdbmsSrvEntry": rdbmsSrvEntry,
       "rdbmsSrvPrivateMibOID": rdbmsSrvPrivateMibOID,
       "rdbmsSrvVendorName": rdbmsSrvVendorName,
       "rdbmsSrvProductName": rdbmsSrvProductName,
       "rdbmsSrvContact": rdbmsSrvContact,
       "rdbmsSrvInfoTable": rdbmsSrvInfoTable,
       "rdbmsSrvInfoEntry": rdbmsSrvInfoEntry,
       "rdbmsSrvInfoStartupTime": rdbmsSrvInfoStartupTime,
       "rdbmsSrvInfoFinishedTransactions": rdbmsSrvInfoFinishedTransactions,
       "rdbmsSrvInfoDiskReads": rdbmsSrvInfoDiskReads,
       "rdbmsSrvInfoLogicalReads": rdbmsSrvInfoLogicalReads,
       "rdbmsSrvInfoDiskWrites": rdbmsSrvInfoDiskWrites,
       "rdbmsSrvInfoLogicalWrites": rdbmsSrvInfoLogicalWrites,
       "rdbmsSrvInfoPageReads": rdbmsSrvInfoPageReads,
       "rdbmsSrvInfoPageWrites": rdbmsSrvInfoPageWrites,
       "rdbmsSrvInfoDiskOutOfSpaces": rdbmsSrvInfoDiskOutOfSpaces,
       "rdbmsSrvInfoHandledRequests": rdbmsSrvInfoHandledRequests,
       "rdbmsSrvInfoRequestRecvs": rdbmsSrvInfoRequestRecvs,
       "rdbmsSrvInfoRequestSends": rdbmsSrvInfoRequestSends,
       "rdbmsSrvInfoHighwaterInboundAssociations": rdbmsSrvInfoHighwaterInboundAssociations,
       "rdbmsSrvInfoMaxInboundAssociations": rdbmsSrvInfoMaxInboundAssociations,
       "rdbmsSrvParamTable": rdbmsSrvParamTable,
       "rdbmsSrvParamEntry": rdbmsSrvParamEntry,
       "rdbmsSrvParamName": rdbmsSrvParamName,
       "rdbmsSrvParamSubIndex": rdbmsSrvParamSubIndex,
       "rdbmsSrvParamID": rdbmsSrvParamID,
       "rdbmsSrvParamCurrValue": rdbmsSrvParamCurrValue,
       "rdbmsSrvParamComment": rdbmsSrvParamComment,
       "rdbmsSrvLimitedResourceTable": rdbmsSrvLimitedResourceTable,
       "rdbmsSrvLimitedResourceEntry": rdbmsSrvLimitedResourceEntry,
       "rdbmsSrvLimitedResourceName": rdbmsSrvLimitedResourceName,
       "rdbmsSrvLimitedResourceID": rdbmsSrvLimitedResourceID,
       "rdbmsSrvLimitedResourceLimit": rdbmsSrvLimitedResourceLimit,
       "rdbmsSrvLimitedResourceCurrent": rdbmsSrvLimitedResourceCurrent,
       "rdbmsSrvLimitedResourceHighwater": rdbmsSrvLimitedResourceHighwater,
       "rdbmsSrvLimitedResourceFailures": rdbmsSrvLimitedResourceFailures,
       "rdbmsSrvLimitedResourceDescription": rdbmsSrvLimitedResourceDescription,
       "rdbmsRelTable": rdbmsRelTable,
       "rdbmsRelEntry": rdbmsRelEntry,
       "rdbmsRelState": rdbmsRelState,
       "rdbmsRelActiveTime": rdbmsRelActiveTime,
       "rdbmsWellKnownLimitedResources": rdbmsWellKnownLimitedResources,
       "rdbmsLogSpace": rdbmsLogSpace,
       "rdbmsTraps": rdbmsTraps,
       "rdbmsStateChange": rdbmsStateChange,
       "rdbmsOutOfSpace": rdbmsOutOfSpace,
       "rdbmsConformance": rdbmsConformance,
       "rdbmsCompliances": rdbmsCompliances,
       "rdbmsCompliance": rdbmsCompliance,
       "rdbmsGroups": rdbmsGroups,
       "rdbmsGroup": rdbmsGroup}
)
