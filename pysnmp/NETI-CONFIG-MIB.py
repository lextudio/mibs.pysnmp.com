# SNMP MIB module (NETI-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETI-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:26:32 2024
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

(netiExperimentalGeneric,) = mibBuilder.importSymbols(
    "NETI-COMMON-MIB",
    "netiExperimentalGeneric")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

netiConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NetiConfigMIBObjects_ObjectIdentity = ObjectIdentity
netiConfigMIBObjects = _NetiConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1)
)
_ConfigStatusGroup_ObjectIdentity = ObjectIdentity
configStatusGroup = _ConfigStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 1)
)
_ConfigStatusIsCurrentUnsaved_Type = TruthValue
_ConfigStatusIsCurrentUnsaved_Object = MibScalar
configStatusIsCurrentUnsaved = _ConfigStatusIsCurrentUnsaved_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 1, 1),
    _ConfigStatusIsCurrentUnsaved_Type()
)
configStatusIsCurrentUnsaved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStatusIsCurrentUnsaved.setStatus("current")
_ConfigStatusCurrentLastChangedTime_Type = DateAndTime
_ConfigStatusCurrentLastChangedTime_Object = MibScalar
configStatusCurrentLastChangedTime = _ConfigStatusCurrentLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 1, 2),
    _ConfigStatusCurrentLastChangedTime_Type()
)
configStatusCurrentLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configStatusCurrentLastChangedTime.setStatus("current")
_ConfigLocalGroup_ObjectIdentity = ObjectIdentity
configLocalGroup = _ConfigLocalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2)
)
_ConfigLocalTableLastChangedTime_Type = DateAndTime
_ConfigLocalTableLastChangedTime_Object = MibScalar
configLocalTableLastChangedTime = _ConfigLocalTableLastChangedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 2),
    _ConfigLocalTableLastChangedTime_Type()
)
configLocalTableLastChangedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configLocalTableLastChangedTime.setStatus("current")
_ConfigLocalTableNrOfConfigs_Type = Gauge32
_ConfigLocalTableNrOfConfigs_Object = MibScalar
configLocalTableNrOfConfigs = _ConfigLocalTableNrOfConfigs_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 3),
    _ConfigLocalTableNrOfConfigs_Type()
)
configLocalTableNrOfConfigs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configLocalTableNrOfConfigs.setStatus("current")
_ConfigLocalTable_Object = MibTable
configLocalTable = _ConfigLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4)
)
if mibBuilder.loadTexts:
    configLocalTable.setStatus("current")
_ConfigLocalEntry_Object = MibTableRow
configLocalEntry = _ConfigLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1)
)
configLocalEntry.setIndexNames(
    (0, "NETI-CONFIG-MIB", "configLocalIndex"),
)
if mibBuilder.loadTexts:
    configLocalEntry.setStatus("current")


class _ConfigLocalIndex_Type(Integer32):
    """Custom type configLocalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ConfigLocalIndex_Type.__name__ = "Integer32"
_ConfigLocalIndex_Object = MibTableColumn
configLocalIndex = _ConfigLocalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 1),
    _ConfigLocalIndex_Type()
)
configLocalIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configLocalIndex.setStatus("current")
_ConfigLocalName_Type = DisplayString
_ConfigLocalName_Object = MibTableColumn
configLocalName = _ConfigLocalName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 2),
    _ConfigLocalName_Type()
)
configLocalName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configLocalName.setStatus("current")
_ConfigLocalDescription_Type = DisplayString
_ConfigLocalDescription_Object = MibTableColumn
configLocalDescription = _ConfigLocalDescription_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 3),
    _ConfigLocalDescription_Type()
)
configLocalDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configLocalDescription.setStatus("current")
_ConfigLocalCreatedTime_Type = DateAndTime
_ConfigLocalCreatedTime_Object = MibTableColumn
configLocalCreatedTime = _ConfigLocalCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 4),
    _ConfigLocalCreatedTime_Type()
)
configLocalCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configLocalCreatedTime.setStatus("current")


class _ConfigLocalSize_Type(Integer32):
    """Custom type configLocalSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ConfigLocalSize_Type.__name__ = "Integer32"
_ConfigLocalSize_Object = MibTableColumn
configLocalSize = _ConfigLocalSize_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 5),
    _ConfigLocalSize_Type()
)
configLocalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configLocalSize.setStatus("current")


class _ConfigLocalAdminStatus_Type(Integer32):
    """Custom type configLocalAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_ConfigLocalAdminStatus_Type.__name__ = "Integer32"
_ConfigLocalAdminStatus_Object = MibTableColumn
configLocalAdminStatus = _ConfigLocalAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 6),
    _ConfigLocalAdminStatus_Type()
)
configLocalAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configLocalAdminStatus.setStatus("current")
_ConfigLocalRowStatus_Type = RowStatus
_ConfigLocalRowStatus_Object = MibTableColumn
configLocalRowStatus = _ConfigLocalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 2, 4, 1, 7),
    _ConfigLocalRowStatus_Type()
)
configLocalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    configLocalRowStatus.setStatus("current")
_ConfigBackupGroup_ObjectIdentity = ObjectIdentity
configBackupGroup = _ConfigBackupGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 3)
)


class _ConfigBackupOperation_Type(Integer32):
    """Custom type configBackupOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("writeCurrentToLocal", 2))
    )


_ConfigBackupOperation_Type.__name__ = "Integer32"
_ConfigBackupOperation_Object = MibScalar
configBackupOperation = _ConfigBackupOperation_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 3, 1),
    _ConfigBackupOperation_Type()
)
configBackupOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBackupOperation.setStatus("current")


class _ConfigBackupStatus_Type(Integer32):
    """Custom type configBackupStatus based on Integer32"""
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
        *(("failed", 3),
          ("idle", 1),
          ("inProgress", 2),
          ("ready", 4))
    )


_ConfigBackupStatus_Type.__name__ = "Integer32"
_ConfigBackupStatus_Object = MibScalar
configBackupStatus = _ConfigBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 3, 2),
    _ConfigBackupStatus_Type()
)
configBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configBackupStatus.setStatus("current")
_ConfigBackupName_Type = DisplayString
_ConfigBackupName_Object = MibScalar
configBackupName = _ConfigBackupName_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 3, 3),
    _ConfigBackupName_Type()
)
configBackupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBackupName.setStatus("current")
_ConfigBackupDescription_Type = DisplayString
_ConfigBackupDescription_Object = MibScalar
configBackupDescription = _ConfigBackupDescription_Object(
    (1, 3, 6, 1, 4, 1, 2928, 6, 2, 7, 1, 3, 4),
    _ConfigBackupDescription_Type()
)
configBackupDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configBackupDescription.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETI-CONFIG-MIB",
    **{"netiConfigMIB": netiConfigMIB,
       "netiConfigMIBObjects": netiConfigMIBObjects,
       "configStatusGroup": configStatusGroup,
       "configStatusIsCurrentUnsaved": configStatusIsCurrentUnsaved,
       "configStatusCurrentLastChangedTime": configStatusCurrentLastChangedTime,
       "configLocalGroup": configLocalGroup,
       "configLocalTableLastChangedTime": configLocalTableLastChangedTime,
       "configLocalTableNrOfConfigs": configLocalTableNrOfConfigs,
       "configLocalTable": configLocalTable,
       "configLocalEntry": configLocalEntry,
       "configLocalIndex": configLocalIndex,
       "configLocalName": configLocalName,
       "configLocalDescription": configLocalDescription,
       "configLocalCreatedTime": configLocalCreatedTime,
       "configLocalSize": configLocalSize,
       "configLocalAdminStatus": configLocalAdminStatus,
       "configLocalRowStatus": configLocalRowStatus,
       "configBackupGroup": configBackupGroup,
       "configBackupOperation": configBackupOperation,
       "configBackupStatus": configBackupStatus,
       "configBackupName": configBackupName,
       "configBackupDescription": configBackupDescription}
)
